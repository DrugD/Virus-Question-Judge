"""Workspace IO helpers."""

from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any


AGENT_VISIBLE = (
    "INSTRUCTIONS.md",
    "checklist.json",
    "info.json",
    "data/raw_data",
)


@dataclass
class Workspace:
    root: Path

    @classmethod
    def from_root(cls, path: str | Path) -> "Workspace":
        return cls(Path(path).resolve())

    @property
    def instructions_path(self) -> Path:
        return self.root / "INSTRUCTIONS.md"

    @property
    def checklist_path(self) -> Path:
        return self.root / "checklist.json"

    @property
    def info_path(self) -> Path:
        return self.root / "info.json"

    @property
    def data_dir(self) -> Path:
        return self.root / "data" / "raw_data"

    @property
    def target_study_dir(self) -> Path:
        return self.root / "target_study"

    def load_checklist(self) -> list[dict[str, Any]]:
        with self.checklist_path.open() as f:
            return json.load(f)

    def load_info(self) -> dict[str, Any]:
        with self.info_path.open() as f:
            return json.load(f)

    def load_groundtruth(self) -> dict[str, Any]:
        with (self.target_study_dir / "question_rubric.json").open() as f:
            return json.load(f)

    def materialize_agent_view(self, dst: Path) -> Path:
        """Copy only agent-visible assets into a fresh sandbox dir.

        target_study/ and results/ are intentionally NOT copied.
        """
        dst = Path(dst).resolve()
        if dst.exists():
            shutil.rmtree(dst)
        dst.mkdir(parents=True)
        for rel in AGENT_VISIBLE:
            src = self.root / rel
            if not src.exists():
                continue
            target = dst / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            if src.is_dir():
                shutil.copytree(src, target)
            else:
                shutil.copy2(src, target)
        return dst

    def collect_agent_outputs(self, sandbox: Path) -> tuple[Path, Path]:
        """Return (agent_questions.json, report.md) inside the sandbox."""
        sandbox = Path(sandbox)
        return (sandbox / "agent_questions.json", sandbox / "report" / "report.md")
