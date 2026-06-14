"""Qwen3.6-Plus single-shot agent (DashScope, OpenAI-compatible API).

Reads the workspace files, prompts Qwen with the full INSTRUCTIONS + data, and
writes report/report.md and agent_questions.json into the sandbox.
"""

from __future__ import annotations

import json
import os
import textwrap
from pathlib import Path
from typing import Any

from .base import AgentRunner


class QwenAgent(AgentRunner):
    agent_id = "qwen3.6-plus"

    def __init__(
        self,
        workspace,
        sandbox_root,
        model: str = "qwen-plus",
        base_url: str | None = None,
        api_key_env: str = "NEWAPI_KEY",
        temperature: float = 0.2,
        max_tokens: int = 4096,
        timeout: int = 180,
    ):
        super().__init__(workspace, sandbox_root)
        self.model = model
        self.base_url = base_url or os.environ.get(
            "NEWAPI_BASE_URL", "http://35.220.164.252:3111/v1"
        )
        self.api_key_env = api_key_env
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout

    def _invoke(self, sandbox: Path) -> str:
        from openai import OpenAI

        api_key = os.environ.get(self.api_key_env)
        if not api_key:
            raise RuntimeError(f"{self.api_key_env} not set for Qwen agent.")
        client = OpenAI(api_key=api_key, base_url=self.base_url)

        bundle = _bundle_workspace(sandbox)
        system = textwrap.dedent(
            """\
            You are an autonomous research agent. Read the workspace materials
            in <workspace>...</workspace>, follow INSTRUCTIONS.md, and produce
            EXACTLY one JSON object. The JSON must have these top-level keys:

              "report_md":       string, full markdown body of report/report.md
              "agent_questions": object matching the schema in INSTRUCTIONS.md

            Return only the JSON object. No prose outside it.
            """
        )
        user = f"<workspace>\n{bundle}\n</workspace>\n\nProduce the JSON now."

        resp = client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            timeout=self.timeout,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        raw = resp.choices[0].message.content or ""
        payload = json.loads(raw)

        report_md: str = payload["report_md"]
        agent_q: dict[str, Any] = payload["agent_questions"]

        (sandbox / "report").mkdir(parents=True, exist_ok=True)
        (sandbox / "report" / "report.md").write_text(report_md)
        (sandbox / "agent_questions.json").write_text(
            json.dumps(agent_q, ensure_ascii=False, indent=2)
        )

        return f"qwen finish_reason={resp.choices[0].finish_reason} bytes={len(raw)}"


def _bundle_workspace(sandbox: Path) -> str:
    """Concatenate the agent-visible files into a single context block."""
    parts: list[str] = []
    for rel in (
        "INSTRUCTIONS.md",
        "checklist.json",
        "data/raw_data/README.md",
        "data/raw_data/blind_input_summary.json",
        "data/raw_data/runinfo_subset.tsv",
        "data/raw_data/alignment_hits.tsv",
        "data/raw_data/candidate_sotu_clusters.tsv",
        "data/raw_data/rdrp_aa_fragments.faa",
    ):
        p = sandbox / rel
        if not p.exists():
            continue
        parts.append(f"<<<FILE {rel}>>>\n{p.read_text()}\n<<<END {rel}>>>")
    return "\n\n".join(parts)
