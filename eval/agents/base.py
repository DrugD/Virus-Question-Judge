"""Common AgentRunner protocol for the question-generation task."""

from __future__ import annotations

import abc
import json
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..utils.schemas import AgentOutput
from ..utils.workspace import Workspace


@dataclass
class RunResult:
    agent_id: str
    sandbox: Path
    agent_output: AgentOutput
    report_md: str
    started_at: float
    finished_at: float
    raw_logs: str = ""

    @property
    def wall_time_s(self) -> float:
        return self.finished_at - self.started_at


class AgentRunner(abc.ABC):
    """Subclasses implement `_invoke()`; everything else is shared."""

    agent_id: str = "base"

    def __init__(self, workspace: Workspace, sandbox_root: Path):
        self.workspace = workspace
        self.sandbox_root = Path(sandbox_root).resolve()
        self.sandbox_root.mkdir(parents=True, exist_ok=True)

    def run(self) -> RunResult:
        sandbox = self.sandbox_root / self.agent_id / time.strftime("%Y%m%dT%H%M%S")
        self.workspace.materialize_agent_view(sandbox)

        started = time.time()
        logs = self._invoke(sandbox)
        finished = time.time()

        q_path, r_path = self.workspace.collect_agent_outputs(sandbox)
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
            sandbox=sandbox,
            agent_output=agent_output,
            report_md=report_md,
            started_at=started,
            finished_at=finished,
            raw_logs=logs,
        )

    @abc.abstractmethod
    def _invoke(self, sandbox: Path) -> str:
        """Run the agent harness against `sandbox` and return its stdout/stderr."""

    @staticmethod
    def _run_cmd(
        argv: list[str],
        cwd: Path,
        timeout: int,
        env: dict[str, str] | None = None,
    ) -> str:
        proc = subprocess.run(
            argv,
            cwd=str(cwd),
            timeout=timeout,
            capture_output=True,
            text=True,
            env=env,
        )
        return f"$ {' '.join(argv)}\n[stdout]\n{proc.stdout}\n[stderr]\n{proc.stderr}\n[exit] {proc.returncode}"
