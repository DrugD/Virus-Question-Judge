"""Codex CLI agent runner.

Codex CLI's default `openai` provider uses the OpenAI Responses API, which
the new-api gateway exposes at /v1/responses. We register a custom provider
via inline `-c` overrides. Sandbox + approvals are disabled so the agent can
write the two contract files inside the per-run sandbox dir.

Codex (Rust) panics when env vars / PATH contain non-UTF-8-clean bytes (which
happens on macOS when the workspace path contains Chinese characters in NFD
form). We work around it by:
  1. forcing the sandbox under an ASCII-only parent dir (default /tmp/codex-sandboxes);
  2. filtering the inherited env to drop any value containing non-ASCII.

Diagnostics: stdout/stderr are streamed to <sandbox>/_debug/codex.{out,err}
in real time via Popen, so a timeout (TimeoutExpired) still leaves a forensic
trail — `subprocess.run(capture_output=True)` would otherwise discard the
buffers on timeout.

Timeout note: gpt-5.1-codex routed through the new-api gateway's /v1/responses
endpoint occasionally hits "ERROR: Reconnecting..." retry loops mid-stream
(transient gateway-side disconnects). The default 1200s budget gives the CLI
enough headroom to finish after a couple of reconnects; 600s used to hit the
wall before retries settled.
"""

from __future__ import annotations

import os
import subprocess
import time
from pathlib import Path

from .base import AgentRunner, RunResult
from ..utils.schemas import AgentOutput


_ASCII_SANDBOX_DEFAULT = Path("/tmp/codex-sandboxes")


def _ascii_safe_env(extra: dict[str, str] | None = None) -> dict[str, str]:
    """Inherit os.environ but drop entries whose value isn't pure ASCII.

    Codex Rust panics on non-ASCII bytes in env values (notably PATH /
    VIRTUAL_ENV / PWD when the parent project lives in a CJK-named dir).
    """
    out: dict[str, str] = {}
    for k, v in os.environ.items():
        try:
            v.encode("ascii")
        except UnicodeEncodeError:
            continue
        out[k] = v
    # PATH always needs the shell binaries; if it got dropped, restore a safe one.
    if "PATH" not in out:
        out["PATH"] = "/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    if extra:
        out.update(extra)
    return out


class CodexCLIAgent(AgentRunner):
    agent_id = "codex-cli"

    def __init__(
        self,
        workspace,
        sandbox_root,
        codex_bin: str = "codex",
        model: str = "gpt-5.1-codex",
        timeout: int = 1200,
        base_url: str | None = None,
        api_key_env: str = "NEWAPI_KEY",
        ascii_sandbox_root: Path | None = None,
    ):
        super().__init__(workspace, sandbox_root)
        self.codex_bin = codex_bin
        self.model = model
        self.timeout = timeout
        self.base_url = base_url or os.environ.get(
            "NEWAPI_BASE_URL", "http://35.220.164.252:3888/v1"
        )
        self.api_key_env = api_key_env
        self.ascii_sandbox_root = Path(ascii_sandbox_root or _ASCII_SANDBOX_DEFAULT).resolve()
        self.ascii_sandbox_root.mkdir(parents=True, exist_ok=True)

    def run(self) -> RunResult:
        # Override: materialize the workspace into an ASCII-only path so that
        # the Rust binary never sees non-ASCII bytes in its cwd / env.
        import json
        ascii_sandbox = self.ascii_sandbox_root / self.agent_id / time.strftime("%Y%m%dT%H%M%S")
        self.workspace.materialize_agent_view(ascii_sandbox)

        started = time.time()
        logs = self._invoke(ascii_sandbox)
        finished = time.time()

        q_path, r_path = self.workspace.collect_agent_outputs(ascii_sandbox)
        if not q_path.exists():
            raise FileNotFoundError(
                f"{self.agent_id} did not write {q_path}. Logs:\n{logs[-1500:]}"
            )
        report_md = r_path.read_text() if r_path.exists() else ""
        try:
            payload = json.loads(q_path.read_text())
            agent_output = AgentOutput.model_validate(payload)
        except Exception as e:
            raise ValueError(
                f"{self.agent_id} produced invalid agent_questions.json: {e}\n"
                f"raw:\n{q_path.read_text()[:2000]}"
            )
        return RunResult(
            agent_id=self.agent_id,
            sandbox=ascii_sandbox,
            agent_output=agent_output,
            report_md=report_md,
            started_at=started,
            finished_at=finished,
            raw_logs=logs,
        )

    def _invoke(self, sandbox: Path) -> str:
        prompt = (
            "Read INSTRUCTIONS.md in the current working directory. Read the "
            "agent-visible files under data/. Produce exactly two files in the "
            "working directory: report/report.md and agent_questions.json "
            "(schema in info.json). target_study/ does not exist in this "
            "sandbox - do not look for it.\n\n"
            "CRITICAL: agent_questions.json MUST contain exactly 5 distinct "
            "candidate questions (rank 1..5, no duplicates). The judge scores "
            "Pass@1 (rank-1 only, 100% / 0%) and Pass@5 (count-based: each of "
            "the 5 candidates that passes adds +0.2, i.e. pass_count / 5, with "
            "no rank weighting). Put your strongest answer at rank 1, but make "
            "all 5 distinct and grounded — every one counts equally for Pass@5.\n\n"
            "Stop only when both output files exist on disk."
        )
        argv = [
            self.codex_bin,
            "exec",
            "--skip-git-repo-check",
            "--ignore-user-config",
            "--dangerously-bypass-approvals-and-sandbox",
            "--ephemeral",
            "--disable", "image_generation",
            # WHAM/apps is codex's hard-coded chatgpt.com MCP transport (NOT a
            # configurable mcp_server entry). Without these disables the
            # transport reconnects against an unreachable host forever.
            "--disable", "apps",
            "--disable", "enable_mcp_apps",
            "--disable", "builtin_mcp",
            "--disable", "tool_search",
            "--cd", str(sandbox),
            "-m", self.model,
            "-c", 'web_search="disabled"',
            "-c", 'mcp_servers={}',
            "-c", 'experimental_use_exec_command_tool=false',
            "-c", 'model_provider="newapi"',
            "-c", 'model_providers.newapi.name="new-api gateway"',
            "-c", f'model_providers.newapi.base_url="{self.base_url}"',
            "-c", f'model_providers.newapi.env_key="{self.api_key_env}"',
            "-c", 'model_providers.newapi.wire_api="responses"',
            prompt,
        ]
        env = _ascii_safe_env()

        ddir = sandbox / "_debug"
        ddir.mkdir(parents=True, exist_ok=True)
        out_path = ddir / "codex.out"
        err_path = ddir / "codex.err"

        with out_path.open("w") as out_f, err_path.open("w") as err_f:
            # Close stdin explicitly. `codex exec` reads from stdin if it's a
            # tty/pipe, which makes it hang forever waiting for input even when
            # the prompt is already passed as a positional arg ("Reading
            # additional input from stdin..."). DEVNULL sends EOF immediately.
            proc = subprocess.Popen(
                argv,
                cwd=str(sandbox),
                env=env,
                stdin=subprocess.DEVNULL,
                stdout=out_f,
                stderr=err_f,
                text=True,
            )
            try:
                rc = proc.wait(timeout=self.timeout)
                timed_out = False
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait(timeout=10)
                rc = -9
                timed_out = True

        stdout = out_path.read_text(errors="replace") if out_path.exists() else ""
        stderr = err_path.read_text(errors="replace") if err_path.exists() else ""
        log = f"$ {' '.join(argv)}\n[stdout]\n{stdout}\n[stderr]\n{stderr}\n[exit] {rc}"
        if timed_out:
            log += f"\n[timeout] killed after {self.timeout}s"
            raise subprocess.TimeoutExpired(argv, self.timeout, output=stdout, stderr=stderr)
        return log


# ---- pre-baked Codex CLI variants ---------------------------------------
#
# Each subclass just pins a different `agent_id` + `-m` model. The Codex CLI
# was originally tuned for gpt-5.1-codex but the new-api gateway's responses
# endpoint also accepts other GPT-5.x model ids — so we can route gpt-5.5
# through the same CLI scaffold.

class CodexGpt55High(CodexCLIAgent):
    agent_id = "gpt-5.5-high"

    def __init__(self, workspace, sandbox_root, **kw):
        kw.setdefault("model", "gpt-5.5-high")
        super().__init__(workspace, sandbox_root, **kw)

