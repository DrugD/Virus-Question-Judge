"""Generic streaming OpenAI-compatible chat agent.

Robust to upstream variation when running through a multi-provider gateway:

  - JSON extraction tries 3 strategies (`<<<JSON>>>...<<</JSON>>>`, fenced
    code block, largest balanced `{...}`); whichever yields a parseable
    object with `agent_questions` or `report_md` wins.
  - Streaming chunk decoding handles all observed shapes:
      delta.content as str (OpenAI native)
      delta.content as a list of {type:"text", text:"..."} (Anthropic via passthrough)
      delta.reasoning_content (DeepSeek-reasoner / Bedrock reasoning shape)
  - If the streaming pass returns nothing usable, the agent silently
    retries with `stream=False` once (some gateway routes don't actually
    stream). If the model hits `finish_reason="length"`, max_tokens is
    doubled (capped) and we retry once.
  - Every run — success or failure — persists `<sandbox>/_debug/raw_stream.txt`
    and `<sandbox>/_debug/meta.json` so we can post-mortem a failure
    without having to re-run.
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


_DEFAULT_BASE_URL = "http://35.220.164.252:3888/v1"
_MAX_TOKENS_CAP = 16384

# Transient gateway-flake retry. The new-api gateway intermittently returns
# 502/503/504 from upstream providers (notably during regional traffic
# spikes). Without this layer, a single 5xx kills the agent run even though
# the model is fine. Backoff is small because the gateway tends to recover
# within seconds; total wait stays under 15 s for the worst case.
_GATEWAY_5XX_MAX_RETRIES = 2
_GATEWAY_5XX_BACKOFF = (3, 8)  # seconds before retry 1, before retry 2

_GATEWAY_5XX_PATTERNS = (
    "502", "503", "504",
    "Bad Gateway", "Gateway Timeout", "Service Unavailable",
    "InternalServerError", "APIConnectionError", "RemoteProtocolError",
    "incomplete chunked read",
)


def _is_transient_gateway_error_str(s: str) -> bool:
    return any(p in s for p in _GATEWAY_5XX_PATTERNS)


def _is_transient_gateway_error(e: BaseException) -> bool:
    return _is_transient_gateway_error_str(f"{type(e).__name__}: {e}")


_FENCE_RE = re.compile(r"```(?:json)?\s*(\{.*?\})\s*```", flags=re.DOTALL | re.IGNORECASE)
_MARKER_RE = re.compile(r"<<<\s*JSON\s*>>>(.*?)<<</\s*JSON\s*>>>", flags=re.DOTALL | re.IGNORECASE)


@dataclass
class _StreamResult:
    full: str
    finish_reason: str | None
    chunk_count: int
    content_chunks: int
    delta_keys_seen: list[str]      # diagnostic: alternative delta fields seen
    used_field: str                 # "content" / "list" / "reasoning_content" / "nonstream"


# ---------------------------------------------------------------------------
# JSON extraction — try 3 strategies in order
# ---------------------------------------------------------------------------

def _try_marker(text: str) -> dict | None:
    m = _MARKER_RE.search(text)
    if not m:
        return None
    try:
        return json.loads(m.group(1).strip())
    except json.JSONDecodeError:
        return None


def _try_fence(text: str) -> dict | None:
    for m in _FENCE_RE.finditer(text):
        try:
            return json.loads(m.group(1).strip())
        except json.JSONDecodeError:
            continue
    return None


def _try_balanced_braces(text: str) -> dict | None:
    """Find the LARGEST balanced `{...}` substring whose JSON parses and
    contains either `agent_questions` or `report_md` at the top level."""
    candidates: list[tuple[int, dict]] = []
    starts: list[int] = [i for i, c in enumerate(text) if c == "{"]
    for s in starts:
        depth = 0
        in_str = False
        escape = False
        for i in range(s, len(text)):
            c = text[i]
            if escape:
                escape = False
                continue
            if c == "\\":
                escape = True
                continue
            if c == '"' and not escape:
                in_str = not in_str
                continue
            if in_str:
                continue
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    sub = text[s : i + 1]
                    try:
                        obj = json.loads(sub)
                    except json.JSONDecodeError:
                        break
                    if isinstance(obj, dict) and ("agent_questions" in obj or "report_md" in obj):
                        candidates.append((len(sub), obj))
                    break
    if not candidates:
        return None
    candidates.sort(key=lambda x: -x[0])
    return candidates[0][1]


def _extract_payload(text: str) -> tuple[dict, str]:
    """Return (parsed_payload, strategy_name).
    Raises ValueError if every strategy fails."""
    for name, fn in (("marker", _try_marker), ("fence", _try_fence), ("balanced", _try_balanced_braces)):
        obj = fn(text)
        if obj is not None:
            return obj, name
    raise ValueError("no parseable JSON found via marker / fence / balanced-brace")


# ---------------------------------------------------------------------------
# Stream decoding — handle all observed gateway shapes
# ---------------------------------------------------------------------------

def _delta_to_text(delta: Any, seen_keys: list[str]) -> tuple[str, str]:
    """Extract text from a streaming delta. Returns (text, used_field).

    Handles:
      - delta.content : str           (OpenAI native)
      - delta.content : list[dict]    (Anthropic content-block passthrough)
      - delta.reasoning_content : str (DeepSeek-reasoner / Bedrock reasoning)
    """
    content = getattr(delta, "content", None)
    if isinstance(content, str) and content:
        return content, "content"
    if isinstance(content, list):
        out: list[str] = []
        for part in content:
            if isinstance(part, dict):
                if part.get("type") in ("text", "output_text") and isinstance(part.get("text"), str):
                    out.append(part["text"])
            elif isinstance(part, str):
                out.append(part)
        if out:
            return "".join(out), "list"
    rc = getattr(delta, "reasoning_content", None)
    if isinstance(rc, str) and rc:
        return rc, "reasoning_content"
    # diagnostic: record other field names we might be missing
    try:
        for k in delta.model_dump().keys():
            if k not in seen_keys:
                seen_keys.append(k)
    except Exception:
        pass
    return "", "none"


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

_SYSTEM_PROMPT = textwrap.dedent("""\
    You are an autonomous research agent. You will be shown the contents
    of every file the user uploaded.

    Task:
      1. Read the data carefully.
      2. Compute at least three derived statistics or observations.
      3. Propose THE single most important scientific question this dataset can answer.

    Output protocol (REQUIRED):

      Emit a CONCISE markdown analysis (200–400 words). Be specific: name files,
      fields, and numerical observations. This prose is shown to the human
      reviewer in real time.

      Then emit EXACTLY this JSON block at the end of your reply, wrapped in
      these markers:

          <<<JSON>>>
          {
            "report_md": "<200-400 word markdown report ending with a 'Top scientific question' section>",
            "agent_questions": {
              "agent_id": "<your model id>",
              "questions": [
                { "rank": 1, "question": "<one English sentence ending with '?'>" }
              ]
            }
          }
          <<</JSON>>>

      Provide exactly 5 distinct candidates (rank 1..5); each candidate is just
      {rank, question} — no other fields. If you cannot include the markers for
      any reason, emit ONLY the JSON object — no markdown fence, no prose after
      it. Do NOT emit any text after the JSON object.
    """).strip()


class OpenAIChatAgent(AgentRunner):
    """Stream-based single-shot chat agent. Subclasses override `agent_id`/`model`."""

    agent_id: str = "openai-chat"
    model: str = "gpt-4.1"

    def __init__(
        self,
        workspace,
        sandbox_root,
        model: str | None = None,
        agent_id: str | None = None,
        base_url: str | None = None,
        api_key_env: str = "NEWAPI_KEY",
        temperature: float = 0.2,
        max_tokens: int = 8192,
        timeout: int = 240,
        on_chunk: Callable[[str], None] | None = None,
    ):
        super().__init__(workspace, sandbox_root)
        if model:
            self.model = model
        if agent_id:
            self.agent_id = agent_id
        self.base_url = base_url or os.environ.get("NEWAPI_BASE_URL", _DEFAULT_BASE_URL)
        self.api_key_env = api_key_env
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.on_chunk = on_chunk

    # ---- API ---------------------------------------------------------------

    def set_chunk_callback(self, fn: Callable[[str], None]) -> None:
        self.on_chunk = fn

    # ---- AgentRunner protocol ---------------------------------------------

    def _invoke(self, sandbox: Path) -> str:
        from openai import OpenAI

        api_key = os.environ.get(self.api_key_env)
        if not api_key:
            raise RuntimeError(f"{self.api_key_env} not set for {self.agent_id}.")
        client = OpenAI(api_key=api_key, base_url=self.base_url)

        bundle = _bundle_workspace(sandbox)
        messages = [
            {"role": "system", "content": _SYSTEM_PROMPT},
            {"role": "user", "content": f"<workspace>\n{bundle}\n</workspace>\n\nProduce your analysis now."},
        ]

        debug: dict[str, Any] = {
            "agent_id": self.agent_id,
            "model": self.model,
            "base_url": self.base_url,
            "max_tokens": self.max_tokens,
            "attempts": [],
        }
        last_full = ""
        last_finish: str | None = None
        r1: _StreamResult | None = None

        # Attempt 1 (+ retries on transient gateway 5xx): streaming
        for retry in range(_GATEWAY_5XX_MAX_RETRIES + 1):
            try:
                r1 = self._stream_once(client, messages, self.max_tokens)
                debug["attempts"].append({
                    "mode": "stream", "retry": retry,
                    **r1.__dict__, "full_len": len(r1.full),
                })
                last_full, last_finish = r1.full, r1.finish_reason
                break
            except Exception as e:
                debug["attempts"].append({"mode": "stream", "retry": retry,
                                          "error": f"{type(e).__name__}: {e}"})
                r1 = None
                if not _is_transient_gateway_error(e) or retry == _GATEWAY_5XX_MAX_RETRIES:
                    break
                delay = _GATEWAY_5XX_BACKOFF[retry]
                debug["attempts"].append({"mode": "stream", "sleep_before_retry_s": delay})
                time.sleep(delay)

        need_fallback = (
            r1 is None
            or not last_full.strip()
            or last_finish == "length"
            or _safe_extract(last_full) is None
        )

        if need_fallback:
            # Attempt 2 (+ retries): non-streaming, possibly with bumped tokens.
            mt = self.max_tokens
            if last_finish == "length":
                mt = min(_MAX_TOKENS_CAP, max(self.max_tokens * 2, 8192))
            for retry in range(_GATEWAY_5XX_MAX_RETRIES + 1):
                try:
                    ns_full, ns_finish = self._invoke_nonstream(client, messages, mt)
                    debug["attempts"].append({
                        "mode": "nonstream", "retry": retry, "max_tokens": mt,
                        "finish_reason": ns_finish, "full_len": len(ns_full),
                    })
                    if ns_full.strip():
                        last_full, last_finish = ns_full, ns_finish
                        # synthetic single chunk to UI so the stream card isn't blank
                        if self.on_chunk and not (r1 and r1.full):
                            try:
                                self.on_chunk(ns_full)
                            except Exception:
                                pass
                    break
                except Exception as e:
                    debug["attempts"].append({"mode": "nonstream", "retry": retry,
                                              "error": f"{type(e).__name__}: {e}"})
                    if not _is_transient_gateway_error(e) or retry == _GATEWAY_5XX_MAX_RETRIES:
                        break
                    delay = _GATEWAY_5XX_BACKOFF[retry]
                    debug["attempts"].append({"mode": "nonstream", "sleep_before_retry_s": delay})
                    time.sleep(delay)

        # Persist debug regardless of outcome
        _write_debug(sandbox, debug, last_full)

        if not last_full.strip():
            # Surface whether the failure was upstream gateway flake or a real
            # empty response so the user / UI can react accordingly.
            had_5xx = any(
                _is_transient_gateway_error_str(a.get("error", ""))
                for a in debug["attempts"] if "error" in a
            )
            tag = "transient gateway 5xx (gave up after retries)" if had_5xx else "model returned empty output"
            raise RuntimeError(
                f"{self.agent_id}: {tag} across all attempts. See _debug/meta.json."
            )

        try:
            payload, strategy = _extract_payload(last_full)
        except ValueError as e:
            tail = last_full[-1500:]
            raise ValueError(
                f"{self.agent_id}: {e}. finish_reason={last_finish!r}, len={len(last_full)}. "
                f"Tail saved to _debug/raw_stream.txt; tail preview:\n{tail}"
            )

        debug["extraction"] = strategy
        _write_debug(sandbox, debug, last_full)

        report_md = payload.get("report_md") or ""
        agent_q = payload.get("agent_questions") or {}
        if not isinstance(agent_q, dict) or "questions" not in agent_q:
            raise ValueError(f"{self.agent_id}: extracted JSON missing agent_questions.questions (strategy={strategy})")
        agent_q.setdefault("agent_id", self.agent_id)
        agent_q.setdefault("workspace_id", "user_uploaded")

        (sandbox / "report").mkdir(parents=True, exist_ok=True)
        (sandbox / "report" / "report.md").write_text(report_md or "(no report_md emitted)")
        (sandbox / "agent_questions.json").write_text(
            json.dumps(agent_q, ensure_ascii=False, indent=2)
        )
        return (
            f"{self.agent_id} OK · strategy={strategy} · bytes={len(last_full)} "
            f"finish={last_finish} attempts={len(debug['attempts'])}"
        )

    # ---- internal helpers -------------------------------------------------

    def _stream_once(self, client, messages: list[dict], max_tokens: int) -> _StreamResult:
        full_parts: list[str] = []
        seen_keys: list[str] = []
        used_field = "none"
        chunk_count = 0
        content_chunks = 0
        finish_reason: str | None = None

        stream = client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            max_tokens=max_tokens,
            timeout=self.timeout,
            messages=messages,
            stream=True,
        )
        for chunk in stream:
            chunk_count += 1
            if not chunk.choices:
                continue
            choice = chunk.choices[0]
            if getattr(choice, "finish_reason", None):
                finish_reason = choice.finish_reason
            delta = getattr(choice, "delta", None)
            if not delta:
                continue
            text, field = _delta_to_text(delta, seen_keys)
            if text:
                full_parts.append(text)
                content_chunks += 1
                if field != "none":
                    used_field = field
                if self.on_chunk:
                    try:
                        self.on_chunk(text)
                    except Exception:
                        pass
        return _StreamResult(
            full="".join(full_parts),
            finish_reason=finish_reason,
            chunk_count=chunk_count,
            content_chunks=content_chunks,
            delta_keys_seen=seen_keys,
            used_field=used_field,
        )

    def _invoke_nonstream(self, client, messages: list[dict], max_tokens: int) -> tuple[str, str | None]:
        resp = client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            max_tokens=max_tokens,
            timeout=self.timeout,
            messages=messages,
            stream=False,
        )
        choice = resp.choices[0] if resp.choices else None
        finish = getattr(choice, "finish_reason", None) if choice else None
        msg = getattr(choice, "message", None) if choice else None
        content = getattr(msg, "content", "") if msg else ""
        if isinstance(content, list):
            content = "".join(
                p.get("text", "") for p in content if isinstance(p, dict) and p.get("type") in ("text", "output_text")
            )
        return content or "", finish


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _safe_extract(text: str) -> dict | None:
    if not text:
        return None
    try:
        out, _ = _extract_payload(text)
        return out
    except ValueError:
        return None


def _write_debug(sandbox: Path, debug: dict, full: str) -> None:
    try:
        ddir = sandbox / "_debug"
        ddir.mkdir(parents=True, exist_ok=True)
        (ddir / "meta.json").write_text(json.dumps(debug, ensure_ascii=False, indent=2, default=str))
        (ddir / "raw_stream.txt").write_text(full or "(empty)")
    except Exception:
        pass


def _bundle_workspace(sandbox: Path) -> str:
    parts: list[str] = []
    for path in sorted(sandbox.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(sandbox)
        rel_str = str(rel)
        if rel_str in ("checklist.json",) or rel.parts[:1] == ("report",) or rel.parts[:1] == ("_debug",):
            continue
        size = path.stat().st_size
        if size > 1 * 1024 * 1024 and rel.suffix.lower() not in (".md", ".txt", ".json", ".jsonl", ".tsv", ".csv", ".faa", ".fasta", ".fa"):
            parts.append(f"<<<FILE {rel_str}>>>\n[skipped: {size} bytes binary-ish]\n<<<END {rel_str}>>>")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            parts.append(f"<<<FILE {rel_str}>>>\n[binary file {size} bytes]\n<<<END {rel_str}>>>")
            continue
        if len(text) > 200_000:
            text = text[:200_000] + f"\n... [truncated, total {len(text)} bytes]"
        parts.append(f"<<<FILE {rel_str}>>>\n{text}\n<<<END {rel_str}>>>")
    return "\n\n".join(parts)


# ----- pre-baked SOTA agents (max_tokens bumped to 8192 across the board) ---

def _make(agent_id: str, model: str, **kw: Any) -> type[OpenAIChatAgent]:
    cls_name = "Agent_" + re.sub(r"[^A-Za-z0-9]", "_", agent_id)
    return type(cls_name, (OpenAIChatAgent,), {"agent_id": agent_id, "model": model, **kw})


GPT_5_1     = _make("gpt-5.1",        "gpt-5.1",        max_tokens=8192)
# GPT-5.5 has no `-thinking` alias on this gateway; reasoning effort is set
# via the `-high / -medium / -low / -pro / -xhigh` suffix instead.
GPT_5_5_HIGH = _make("gpt-5.5-high",   "gpt-5.5-high",   max_tokens=8192)
GPT_4_1     = _make("gpt-4.1",        "gpt-4.1",        max_tokens=8192)
CLAUDE_SON  = _make("claude-sonnet-4-5", "claude-sonnet-4-5-20250929", max_tokens=8192)
CLAUDE_HAI  = _make("claude-haiku-4-5",  "claude-haiku-4-5-20251001",  max_tokens=8192)
GEMINI_PRO  = _make("gemini-3.1-pro",  "gemini-3.1-pro-preview",  max_tokens=8192)
GEMINI_FLAS = _make("gemini-2.5-flash","gemini-2.5-flash",        max_tokens=8192)
QWEN_PLUS   = _make("qwen3.6-plus",    "qwen3.6-plus",            max_tokens=8192)
# `deepseek/deepseek-v3.2-speciale` routes via AtlasCloud and consistently
# returns 400. The plain `deepseek-v3.2` alias goes through a different
# upstream and works.
DEEPSEEK    = _make("deepseek-v3.2",   "deepseek-v3.2",           max_tokens=8192)
GLM_46      = _make("glm-4.6",         "glm-4.6",                  max_tokens=8192)

# Shanghai AI Lab — InternVL3 (vision-language, but speak OpenAI chat completions on this gateway)
INTERN_VL3_14B = _make("internvl3-14b", "opengvlab/internvl3-14b", max_tokens=8192)
INTERN_VL3_2B  = _make("internvl3-2b",  "opengvlab/internvl3-2b",  max_tokens=8192)
