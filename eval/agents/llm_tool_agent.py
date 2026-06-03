"""LLM-based agent runner with a real ReAct tool-using loop.

Replaces the single-shot streaming approach (`OpenAIChatAgent`) with a
multi-turn agent that drives the model via OpenAI-compatible function/tool
calling. The model must explicitly:
  1. list_files() to discover the workspace,
  2. read_file() the contents it needs (with chunked reads for large files),
  3. write_file() the two contract outputs (`report/report.md` and
     `agent_questions.json`),
  4. done() when both outputs are on disk.

Why this is the right shape for the gold-rubric eval:
  - "single-shot streaming" is just an LLM call; it bundles the entire
    workspace into one prompt and never lets the model decide what to read.
  - With tool calls the model has actual agency: planning what to read
    when, and the same scaffold works regardless of how big or unusual the
    user's data is.
  - All families (OpenAI, Anthropic, Google, GLM, InternVL3) speak the
    OpenAI tools schema on the new-api gateway, so a single class covers
    every model below.

The 5xx retry layer + JSON-extraction multi-strategy and `_debug/` dump
from openai_chat_agent.py are reused; only the *driver loop* changes.
"""

from __future__ import annotations

import json
import os
import re
import textwrap
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from .base import AgentRunner
from .openai_chat_agent import (
    _DEFAULT_BASE_URL,
    _GATEWAY_5XX_BACKOFF,
    _GATEWAY_5XX_MAX_RETRIES,
    _is_transient_gateway_error,
    _extract_payload,
)


_MAX_FILE_READ_BYTES = 80_000     # per read_file call
_MAX_LIST_ENTRIES = 400           # per list_files call
_DEFAULT_MAX_ITERS = 30           # safety cap on tool-loop turns
_STALL_BUDGET = 3                 # consecutive empty-reply nudges before giving up


_SYSTEM_PROMPT = textwrap.dedent("""\
    You are an autonomous research agent. You have a sandboxed workspace and a
    tool API. Your job: read the user's data, propose **exactly 5 distinct
    scientific questions** (best at rank 1), and persist your answer to disk.

    Required outputs (both files MUST exist on disk before you call `done`):
      - report/report.md  (300–600 words; sections: Data summary · Analysis ·
        Reasoning · Top scientific question · Why testable on this dataset)
      - agent_questions.json  (schema below — `questions` MUST contain exactly 5
        unique entries with rank 1..5, no duplicates allowed)

    Required JSON schema for agent_questions.json:
      {
        "agent_id": "<your model id>",
        "workspace_id": "user_uploaded",
        "questions": [
          {
            "rank": 1,
            "question": "<one English sentence ending with '?'>",
            "rationale": "<2-4 sentences citing actual files / fields you read>",
            "data_support": ["<actual paths under data/>", "..."],
            "expected_test": "<how the question is answerable from this data>",
            "scope_keywords": ["<3-8 short keywords>"]
          }
          // EXACTLY 5 entries, ranks 1..5, all distinct questions.
        ]
      }

    Tooling protocol:
      - Call `list_files` first to discover what's in `data/`. Do not assume
        any filename — discover them.
      - Call `read_file` with explicit `start`/`end` byte ranges for large
        files. The tool truncates >80KB per call; iterate if needed.
      - Call `write_file` to save the two outputs.
      - Call `done` only after BOTH `report/report.md` and
        `agent_questions.json` are on disk.
      - Do not open `gold/` (it contains the rubric) — the tool will refuse.

    Pass@5 metric (read carefully — this is how you are scored):
      - Pass@1 = 100% if rank-1 passes the threshold, else 0%.
      - Pass@5 = count-based: each of your 5 candidates that passes adds a flat
        +0.2 (pass_count / 5), independent of its rank.
        1 of 5 → 20%; 3 of 5 → 60%; all 5 → 100%.
      - Strategy: put your STRONGEST guess at rank 1 (it drives Pass@1), but
        EVERY candidate counts equally toward Pass@5 — make all 5 distinct,
        grounded, and plausible.
      - DUPLICATES ARE FORBIDDEN. The schema validator rejects them.

    Be concise in your assistant turns. Plan your reads, then write the
    outputs. Prioritise getting both files on disk over exhaustive exploration.
""").strip()


_TOOLS_SPEC: list[dict] = [
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": (
                "List entries inside the workspace. Use path='.' for the "
                "root, or 'data' / 'data/sub'. Returns up to 400 entries; "
                "set recursive=true to walk subdirectories."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Relative path inside the workspace."},
                    "recursive": {"type": "boolean", "default": True},
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": (
                "Read a UTF-8 (or best-effort) text slice from a file inside "
                "the workspace. Truncates to 80KB per call; for large files, "
                "iterate by passing successive `start` offsets."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Relative file path."},
                    "start": {"type": "integer", "default": 0, "description": "Starting byte offset."},
                    "end":   {"type": "integer", "description": "Optional inclusive byte cap; default = start+80000."},
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": (
                "Write text to a file inside the workspace. Creates parent "
                "directories as needed. Use this for `report/report.md` and "
                "`agent_questions.json`."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path":    {"type": "string"},
                    "content": {"type": "string"},
                },
                "required": ["path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "done",
            "description": (
                "Signal that both required output files are on disk and the "
                "run is complete. Will fail if either output is missing."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "summary": {"type": "string", "description": "One-line summary of what you found."},
                },
            },
        },
    },
]


@dataclass
class _Turn:
    iter: int
    role: str
    content: str | None = None
    tool_calls: list[dict] | None = None
    tool_name: str | None = None
    tool_args: dict | None = None
    tool_result: str | None = None


def _safe_path(sandbox: Path, rel: str) -> Path | None:
    """Resolve `rel` inside `sandbox`. Returns None if it escapes or hits gold/."""
    try:
        p = (sandbox / rel).resolve()
    except Exception:
        return None
    sandbox = sandbox.resolve()
    try:
        p.relative_to(sandbox)
    except ValueError:
        return None
    # block gold/ explicitly
    rel_to_sandbox = p.relative_to(sandbox)
    if rel_to_sandbox.parts and rel_to_sandbox.parts[0] == "gold":
        return None
    return p


def _tool_list_files(sandbox: Path, args: dict) -> str:
    rel = (args.get("path") or ".").strip()
    recursive = bool(args.get("recursive", True))
    p = _safe_path(sandbox, rel)
    if p is None:
        return f"ERROR: path '{rel}' is outside the workspace or refers to gold/"
    if not p.exists():
        return f"ERROR: '{rel}' does not exist"
    if p.is_file():
        return f"FILE\t{rel}\t{p.stat().st_size}"
    out: list[str] = []
    iter_paths = sorted(p.rglob("*")) if recursive else sorted(p.iterdir())
    for child in iter_paths:
        if child.name.startswith("_debug"):
            continue
        try:
            rel_str = str(child.relative_to(sandbox))
        except Exception:
            continue
        if child.is_dir():
            out.append(f"DIR\t{rel_str}/")
        else:
            try:
                size = child.stat().st_size
            except Exception:
                size = 0
            out.append(f"FILE\t{rel_str}\t{size}")
        if len(out) >= _MAX_LIST_ENTRIES:
            out.append(f"... [truncated at {_MAX_LIST_ENTRIES} entries]")
            break
    return "\n".join(out) if out else "(empty)"


_BINARY_EXTENSIONS = {
    ".zip", ".gz", ".tar", ".tgz", ".bz2", ".xz", ".7z", ".rar",
    ".xlsx", ".xls", ".docx", ".doc", ".pptx", ".ppt", ".pdf",
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".tiff", ".ico",
    ".mp3", ".mp4", ".wav", ".mov", ".avi", ".mkv",
    ".so", ".dylib", ".dll", ".exe", ".bin", ".pkl", ".pickle",
    ".db", ".sqlite", ".parquet", ".feather", ".arrow",
    ".pyc", ".pyo",
}


def _is_binary_path(p: Path) -> bool:
    """True if `p` is binary by extension OR by sampling its first 4KB."""
    if p.suffix.lower() in _BINARY_EXTENSIONS:
        return True
    try:
        with p.open("rb") as f:
            sample = f.read(4096)
    except Exception:
        return True
    if not sample:
        return False
    if b"\x00" in sample:
        return True
    # heuristic: > 5% non-text bytes → treat as binary
    text_chars = bytes(range(7, 14)) + b"\x1b" + bytes(range(0x20, 0x7f)) + bytes(range(0x80, 0x100))
    nontext = sum(1 for b in sample if b not in text_chars)
    return nontext / len(sample) > 0.05


def _tool_read_file(sandbox: Path, args: dict) -> str:
    rel = (args.get("path") or "").strip()
    if not rel:
        return "ERROR: missing 'path'"
    p = _safe_path(sandbox, rel)
    if p is None:
        return f"ERROR: path '{rel}' is outside the workspace or refers to gold/"
    if not p.exists() or not p.is_file():
        return f"ERROR: '{rel}' is not a regular file"
    size = p.stat().st_size

    # Binary files would just dump utf-8-replace garbage into the model's
    # context — wasteful and confusing. Return metadata + an actionable hint
    # so the agent can use the filename / size to write a question without
    # trying to "read" archive bytes.
    if _is_binary_path(p):
        return (
            f"# {rel} · {size} bytes · BINARY (extension {p.suffix or 'unknown'})\n"
            f"This file is binary (archive / spreadsheet / compressed / image / "
            f"office document). The agent tool cannot decode it as text. Use the "
            f"filename and size as evidence in your question; do NOT try to "
            f"read its bytes — they will be unreadable."
        )

    start = max(0, int(args.get("start") or 0))
    end_arg = args.get("end")
    end = min(size, int(end_arg) if end_arg is not None else start + _MAX_FILE_READ_BYTES)
    end = min(end, start + _MAX_FILE_READ_BYTES)
    try:
        with p.open("rb") as f:
            f.seek(start)
            raw = f.read(end - start)
        text = raw.decode("utf-8", errors="replace")
    except Exception as e:
        return f"ERROR: could not read '{rel}': {type(e).__name__}: {e}"
    truncated = end < size
    header = f"# {rel} · bytes {start}..{end-1} of {size}{' · TRUNCATED, more bytes follow' if truncated else ''}\n"
    return header + text


def _tool_write_file(sandbox: Path, args: dict) -> str:
    rel = (args.get("path") or "").strip()
    content = args.get("content")
    if not rel or content is None:
        return "ERROR: 'path' and 'content' are required"
    p = _safe_path(sandbox, rel)
    if p is None:
        return f"ERROR: path '{rel}' is outside the workspace or refers to gold/"
    try:
        p.parent.mkdir(parents=True, exist_ok=True)
        if not isinstance(content, str):
            content = json.dumps(content, ensure_ascii=False, indent=2)
        p.write_text(content)
    except Exception as e:
        return f"ERROR: could not write '{rel}': {type(e).__name__}: {e}"
    return f"OK · wrote {len(content)} bytes to {rel}"


def _tool_done(sandbox: Path, args: dict) -> str:
    rep = sandbox / "report" / "report.md"
    aq = sandbox / "agent_questions.json"
    missing = [str(p.relative_to(sandbox)) for p in (rep, aq) if not p.exists()]
    if missing:
        return f"ERROR: cannot mark done — missing required outputs: {missing}"
    return f"OK · {args.get('summary') or 'run complete'}"


_TOOL_DISPATCH: dict[str, Callable[[Path, dict], str]] = {
    "list_files": _tool_list_files,
    "read_file":  _tool_read_file,
    "write_file": _tool_write_file,
    "done":       _tool_done,
}


def _truncate(s: str, n: int = 6000) -> str:
    if len(s) <= n:
        return s
    return s[: n - 200] + f"\n... [truncated, total {len(s)} bytes]"


def _write_debug(sandbox: Path, meta: dict, transcript: list[_Turn]) -> None:
    try:
        ddir = sandbox / "_debug"
        ddir.mkdir(parents=True, exist_ok=True)
        (ddir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2, default=str))
        # also emit a flat human-readable transcript
        lines: list[str] = []
        for t in transcript:
            head = f"[turn {t.iter}] {t.role}"
            if t.tool_name:
                head += f" → tool:{t.tool_name}"
            lines.append(head)
            if t.content:
                lines.append("  content: " + _truncate(t.content, 1500))
            if t.tool_args is not None:
                lines.append("  args: " + _truncate(json.dumps(t.tool_args, ensure_ascii=False), 600))
            if t.tool_result is not None:
                lines.append("  result: " + _truncate(t.tool_result, 1500))
            lines.append("")
        (ddir / "transcript.txt").write_text("\n".join(lines))
    except Exception:
        pass


class LLMToolAgent(AgentRunner):
    """Multi-turn ReAct agent. Subclasses set `agent_id` + `model`."""

    agent_id: str = "llm-tool"
    model: str = "gpt-4.1"

    def __init__(
        self,
        workspace,
        sandbox_root,
        model: str | None = None,
        agent_id: str | None = None,
        base_url: str | None = None,
        api_key_env: str | None = None,
        temperature: float = 0.2,
        max_tokens: int = 4096,
        timeout: int = 240,
        max_iters: int = _DEFAULT_MAX_ITERS,
        on_chunk: Callable[[str], None] | None = None,
    ):
        super().__init__(workspace, sandbox_root)
        if model:
            self.model = model
        if agent_id:
            self.agent_id = agent_id
        # Provider routing — subclasses for non-gateway providers (e.g.
        # InternLM at chat.intern-ai.org.cn) pin their own endpoint and key
        # env-var via class attributes `default_base_url` /
        # `default_api_key_env`. Fall back to the new-api gateway when
        # neither the kwarg nor the class attribute is set.
        self.base_url = (
            base_url
            or getattr(type(self), "default_base_url", None)
            or os.environ.get("NEWAPI_BASE_URL", _DEFAULT_BASE_URL)
        )
        self.api_key_env = (
            api_key_env
            or getattr(type(self), "default_api_key_env", None)
            or "NEWAPI_KEY"
        )
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.max_iters = max_iters
        self.on_chunk = on_chunk

    def set_chunk_callback(self, fn: Callable[[str], None]) -> None:
        self.on_chunk = fn

    # ---- AgentRunner protocol ------------------------------------------

    def _invoke(self, sandbox: Path) -> str:
        from openai import OpenAI

        api_key = os.environ.get(self.api_key_env)
        if not api_key:
            raise RuntimeError(f"{self.api_key_env} not set for {self.agent_id}.")
        client = OpenAI(api_key=api_key, base_url=self.base_url)

        messages: list[dict] = [
            {"role": "system", "content": _SYSTEM_PROMPT},
            {"role": "user", "content": (
                f"Workspace mounted at the sandbox root. "
                f"Your agent_id should be `{self.agent_id}`. "
                f"Begin by listing the workspace, then read what you need."
            )},
        ]

        transcript: list[_Turn] = []
        meta: dict[str, Any] = {
            "agent_id": self.agent_id,
            "model": self.model,
            "base_url": self.base_url,
            "max_iters": self.max_iters,
            "iters": 0,
            "tool_call_count": 0,
            "files_written": [],
            "iters_history": [],
        }

        terminated_via_done = False
        for i in range(self.max_iters):
            meta["iters"] = i + 1
            try:
                resp = self._chat_with_retry(client, messages)
            except Exception as e:
                meta["fatal_error"] = f"{type(e).__name__}: {e}"
                _write_debug(sandbox, meta, transcript)
                raise

            choice = resp.choices[0] if resp.choices else None
            msg = getattr(choice, "message", None)
            content = getattr(msg, "content", None) or ""
            tool_calls = getattr(msg, "tool_calls", None) or []
            # DeepSeek-style thinking-mode models (deepseek-v4-pro, deepseek-reasoner,
            # GLM-Z1, qwen3-thinking, …) emit a separate `reasoning_content` channel
            # next to `content`. The provider mandates that this field be echoed
            # back verbatim on the next turn — otherwise the next request 400s with
            # "The `reasoning_content` in the thinking mode must be passed back".
            # We preserve it on the assistant record below; non-thinking models
            # simply have it None and the field is omitted.
            reasoning_content = getattr(msg, "reasoning_content", None)

            iter_summary = {
                "iter": i + 1,
                "finish_reason": getattr(choice, "finish_reason", None),
                "tool_calls": [tc.function.name for tc in tool_calls],
                "content_len": len(content),
            }
            meta["iters_history"].append(iter_summary)

            transcript.append(_Turn(
                iter=i + 1,
                role="assistant",
                content=content or None,
                tool_calls=[
                    {"id": tc.id, "name": tc.function.name, "arguments": tc.function.arguments}
                    for tc in tool_calls
                ] or None,
            ))

            # surface assistant text + tool-call hints to the streaming UI
            if self.on_chunk:
                hints: list[str] = []
                if content:
                    hints.append(content)
                for tc in tool_calls:
                    args_str = tc.function.arguments
                    try:
                        parsed = json.loads(args_str)
                        path_hint = parsed.get("path") or parsed.get("summary") or ""
                    except Exception:
                        path_hint = args_str[:80]
                    hints.append(f"\n→ {tc.function.name}({path_hint!r})")
                if hints:
                    try:
                        self.on_chunk("".join(hints))
                    except Exception:
                        pass

            # IMPORTANT: append the assistant message verbatim so tool_call_id
            # round-trip works on every gateway-translated provider.
            assistant_record: dict[str, Any] = {"role": "assistant", "content": content or ""}
            if reasoning_content:
                # Required for DeepSeek thinking-mode multi-turn continuity.
                assistant_record["reasoning_content"] = reasoning_content
            if tool_calls:
                assistant_record["tool_calls"] = [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {"name": tc.function.name, "arguments": tc.function.arguments},
                    }
                    for tc in tool_calls
                ]
            messages.append(assistant_record)

            if not tool_calls:
                # No tool calls + no content → model stalled. Some providers
                # (notably Gemini through OpenAI-compat) occasionally return
                # an empty assistant turn after a long tool result, especially
                # when the result was truncated mid-JSON. Don't kill the loop
                # on first stall — nudge the model up to `_STALL_BUDGET` times
                # to recover before bailing.
                if not content.strip():
                    meta["stall_count"] = meta.get("stall_count", 0) + 1
                    if meta["stall_count"] > _STALL_BUDGET:
                        meta["stall"] = True
                        break
                    messages.append({
                        "role": "user",
                        "content": (
                            "Your last reply was empty. Continue the task. "
                            "If you have read enough, write report/report.md and "
                            "agent_questions.json now using write_file, then call done. "
                            "If you need more data, call read_file or list_files."
                        ),
                    })
                    continue
                # Model gave a final text reply without calling tools — likely
                # done if both files exist; if not, push it to keep going.
                if (sandbox / "report" / "report.md").exists() and (sandbox / "agent_questions.json").exists():
                    terminated_via_done = True
                    break
                messages.append({
                    "role": "user",
                    "content": (
                        "I do not see report/report.md and agent_questions.json on disk yet. "
                        "Use write_file to save them, then call done."
                    ),
                })
                continue

            for tc in tool_calls:
                meta["tool_call_count"] += 1
                name = tc.function.name
                try:
                    args = json.loads(tc.function.arguments or "{}")
                except json.JSONDecodeError:
                    args = {"_raw": tc.function.arguments}
                fn = _TOOL_DISPATCH.get(name)
                if fn is None:
                    result = f"ERROR: unknown tool '{name}'"
                else:
                    try:
                        result = fn(sandbox, args)
                    except Exception as e:
                        result = f"ERROR: {type(e).__name__}: {e}"

                if name == "write_file" and not result.startswith("ERROR"):
                    meta["files_written"].append(args.get("path"))
                if name == "done" and not result.startswith("ERROR"):
                    terminated_via_done = True

                transcript.append(_Turn(
                    iter=i + 1, role="tool",
                    tool_name=name, tool_args=args, tool_result=result,
                ))
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": _truncate(result, 50_000),
                })

            if terminated_via_done:
                break

        meta["terminated_via_done"] = terminated_via_done
        _write_debug(sandbox, meta, transcript)

        # Try to repair if agent_questions.json was emitted as raw text inside
        # a tool result rather than via write_file (some weaker models do this).
        aq_path = sandbox / "agent_questions.json"
        if not aq_path.exists():
            for t in reversed(transcript):
                if t.tool_name == "write_file" and t.tool_args:
                    if "agent_questions" in (t.tool_args.get("path") or ""):
                        # write_file already handled this above; if it failed, fall through
                        break
                if t.role == "assistant" and t.content:
                    payload = None
                    try:
                        payload, _ = _extract_payload(t.content)
                    except ValueError:
                        payload = None
                    if isinstance(payload, dict) and "questions" in payload:
                        aq_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
                        meta["repaired_from_assistant_text"] = True
                        _write_debug(sandbox, meta, transcript)
                        break

        if not aq_path.exists():
            raise RuntimeError(
                f"{self.agent_id}: agent_questions.json was never written "
                f"(iters={meta['iters']}, tool_calls={meta['tool_call_count']}). "
                f"See _debug/transcript.txt."
            )

        # Make sure required JSON-shape fields exist.
        try:
            payload = json.loads(aq_path.read_text())
        except json.JSONDecodeError as e:
            raise ValueError(f"{self.agent_id}: agent_questions.json is not valid JSON: {e}")
        if not isinstance(payload, dict) or "questions" not in payload:
            raise ValueError(f"{self.agent_id}: agent_questions.json missing 'questions' list")
        payload.setdefault("agent_id", self.agent_id)
        payload.setdefault("workspace_id", "user_uploaded")
        aq_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

        # Synthesize an empty report if model forgot — judge cares about the
        # JSON; missing report.md shouldn't crash the run.
        rep_path = sandbox / "report" / "report.md"
        if not rep_path.exists():
            rep_path.parent.mkdir(parents=True, exist_ok=True)
            rep_path.write_text("(no report_md emitted)")

        return (
            f"{self.agent_id} OK · iters={meta['iters']} · "
            f"tool_calls={meta['tool_call_count']} · "
            f"done={terminated_via_done} · "
            f"writes={len(meta['files_written'])}"
        )

    # ---- internal: chat with 5xx-aware retry ---------------------------

    def _chat_with_retry(self, client, messages: list[dict]):
        last: BaseException | None = None
        for retry in range(_GATEWAY_5XX_MAX_RETRIES + 1):
            try:
                return client.chat.completions.create(
                    model=self.model,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    timeout=self.timeout,
                    messages=messages,
                    tools=_TOOLS_SPEC,
                    tool_choice="auto",
                    stream=False,
                )
            except Exception as e:
                last = e
                if not _is_transient_gateway_error(e) or retry == _GATEWAY_5XX_MAX_RETRIES:
                    raise
                time.sleep(_GATEWAY_5XX_BACKOFF[retry])
        if last is not None:
            raise last  # noqa: defensive
        raise RuntimeError("unreachable")


# ---- pre-baked agent factories (mirror openai_chat_agent's set) ------------

def _make(agent_id: str, model: str, **kw: Any) -> type[LLMToolAgent]:
    cls_name = "ToolAgent_" + re.sub(r"[^A-Za-z0-9]", "_", agent_id)
    return type(cls_name, (LLMToolAgent,), {"agent_id": agent_id, "model": model, **kw})


GPT_5_5_HIGH    = _make("gpt-5.5-high",      "gpt-5.5-high",                 max_tokens=4096)
CLAUDE_SON_TOOL = _make("claude-sonnet-4-5", "claude-sonnet-4-5-20250929",   max_tokens=4096)
CLAUDE_HAI_TOOL = _make("claude-haiku-4-5",  "claude-haiku-4-5-20251001",    max_tokens=4096)
# Gateway (no-local-CLI) variants of the Codex / Claude Code agents. Same ids as
# the CLI versions so results dirs + UI labels stay identical; these route the
# model through the new-api gateway via the generic ReAct tool loop instead of
# requiring a locally-installed `codex` / `claude` binary.
#
# NOTE: the `gpt-5.5-high` *id* maps to the gateway model `gpt-5.5` (not
# `gpt-5.5-high`). The gateway pins `reasoning_effort=high` on the `-high`
# model, and OpenAI rejects function-tools + reasoning_effort on
# /v1/chat/completions ("use /v1/responses instead"). The generic tool loop is
# chat-completions-based, so we use plain `gpt-5.5`, which supports tool calls.
GPT_5_5_HIGH_TOOL   = _make("gpt-5.5-high",           "gpt-5.5",             max_tokens=4096)
CLAUDE_OPUS_47_TOOL = _make("claude-code-opus-4-7",   "claude-opus-4-7",     max_tokens=4096)
CLAUDE_SON_46_TOOL  = _make("claude-code-sonnet-4-6", "claude-sonnet-4-6",   max_tokens=4096)
GEMINI_PRO_TOOL = _make("gemini-3.1-pro",    "gemini-3.1-pro-preview",       max_tokens=4096)
GEMINI_FLAS_TOOL = _make("gemini-2.5-flash", "gemini-2.5-flash",             max_tokens=4096)
GLM_5_TOOL      = _make("glm-5",             "glm-5",                         max_tokens=4096)
DEEPSEEK_V4_PRO_TOOL = _make("deepseek-v4-pro", "deepseek-v4-pro",           max_tokens=4096)
INTERN_VL3_14B_TOOL = _make("internvl3-14b", "opengvlab/internvl3-14b",       max_tokens=4096)
INTERN_VL3_2B_TOOL  = _make("internvl3-2b",  "opengvlab/internvl3-2b",        max_tokens=4096)

# ---- InternLM (Shanghai AI Lab · 浦语) -------------------------------------
#
# Separate provider — does NOT route through the new-api gateway. Endpoint is
# OpenAI-compatible (POST /v1/chat/completions, Authorization: Bearer ...).
# Key is read from env var INTERN_AI_KEY. Both are pinned as class attributes
# below so the LLMToolAgent constructor picks them up via getattr() fallbacks.
#
# Model IDs are the canonical ones published by the upstream API (per the
# 浦语 console model list):
#   - intern-s1            : 32K  · 多模态 + 科学能力
#   - intern-s1-pro        : 256K · 科学多模态推理 (内置联网搜索)
#   - intern-s1-mini       : 32K  · 轻量级科学强推理
#   - intern-s2-preview    : 256K · 35B-A3B · 科学发现 + 通用智能体
#   - intern-latest        : alias → 当前指向 intern-s2-preview
# We register the four explicit ids the user asked for ("S1 / S1 pro / S2 / A1
# 系列"). The 'A1' slot maps to intern-s1-mini since the public model list has
# no 'a1' variant — closest equivalent is the lightweight reasoning model.
_INTERN_BASE_URL = "https://chat.intern-ai.org.cn/api/v1"
_INTERN_KEY_ENV  = "INTERN_AI_KEY"   # env-var NAME (set the token in .env), NOT the key itself

INTERN_S1_TOOL      = _make("intern-s1",         "intern-s1",         default_base_url=_INTERN_BASE_URL, default_api_key_env=_INTERN_KEY_ENV, max_tokens=4096)
INTERN_S1_PRO_TOOL  = _make("intern-s1-pro",     "intern-s1-pro",     default_base_url=_INTERN_BASE_URL, default_api_key_env=_INTERN_KEY_ENV, max_tokens=4096)
INTERN_S1_MINI_TOOL = _make("intern-s1-mini",    "intern-s1-mini",    default_base_url=_INTERN_BASE_URL, default_api_key_env=_INTERN_KEY_ENV, max_tokens=4096)
INTERN_S2_TOOL      = _make("intern-s2-preview", "intern-s2-preview", default_base_url=_INTERN_BASE_URL, default_api_key_env=_INTERN_KEY_ENV, max_tokens=4096)
