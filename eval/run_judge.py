"""Score one agent's outputs against the rubric.

Usage:
    python eval/run_judge.py \
        --workspace . \
        --agent-output results/qwen3.6-plus/20260516T101010 \
        --judge-config eval/config.yaml

Produces results/{agent}/{run_id}/judge_scores.json.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv
from deepeval.test_case import LLMTestCase

from eval.metrics import (
    JudgeLLM,
    RubricCompositeMetric,
    RubricDimensionMetric,
)
from eval.metrics.judge_llm import JudgeConfig
from eval.utils import AgentOutput, Workspace


def _bootstrap_env(workspace_root: Path) -> None:
    env_path = workspace_root / ".env"
    if env_path.exists():
        load_dotenv(env_path, override=False)
    key = os.environ.get("NEWAPI_KEY", "")
    if key and key != "sk-REPLACE_ME":
        os.environ.setdefault("OPENAI_API_KEY", key)
        os.environ.setdefault("ANTHROPIC_AUTH_TOKEN", key)
        os.environ.setdefault("ANTHROPIC_API_KEY", key)


def build_metrics(
    workspace: Workspace,
    judge: JudgeLLM,
    threshold: float,
) -> RubricCompositeMetric:
    checklist = workspace.load_checklist()
    gt = workspace.load_groundtruth()
    primary_gt = next(q for q in gt["groundtruth_questions"] if q.get("is_primary"))
    flags = gt.get("refusal_flags", [])

    dims = [
        RubricDimensionMetric(
            dimension=d,
            groundtruth=primary_gt,
            refusal_flags=flags,
            judge=judge,
            threshold=threshold,
        )
        for d in checklist
    ]
    return RubricCompositeMetric(dimension_metrics=dims, threshold=threshold)


def score_agent_run(
    workspace: Workspace,
    agent_run_dir: Path,
    judge_cfg_path: Path,
) -> dict[str, Any]:
    cfg = yaml.safe_load(judge_cfg_path.read_text())
    judge = JudgeLLM(JudgeConfig(**cfg["judge"]))

    threshold = float(cfg.get("threshold", 0.6))
    composite = build_metrics(workspace, judge, threshold)

    payload = json.loads((agent_run_dir / "agent_questions.json").read_text())
    agent_output = AgentOutput.model_validate(payload)
    candidate = agent_output.to_judge_payload()

    test_case = LLMTestCase(
        input="Generate the most important scientific question this dataset can answer.",
        actual_output=candidate["question"],
        additional_metadata={"candidate": candidate},
    )

    composite.measure(test_case)
    result = composite.result.to_json()
    result["candidate"] = candidate
    result["agent_id"] = agent_output.agent_id
    result["workspace_id"] = agent_output.workspace_id
    result["judge_model"] = cfg["judge"]["model"]
    result["judge_provider"] = cfg["judge"]["provider"]
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", required=True, type=Path)
    ap.add_argument("--agent-output", required=True, type=Path,
                    help="results/{agent}/{run_id}/")
    ap.add_argument("--judge-config", required=True, type=Path)
    ap.add_argument("--out", type=Path, default=None,
                    help="Override output path; default = <agent-output>/judge_scores.json")
    args = ap.parse_args()

    ws = Workspace.from_root(args.workspace)
    _bootstrap_env(ws.root)
    out_path = args.out or (args.agent_output / "judge_scores.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    result = score_agent_run(ws, args.agent_output, args.judge_config)
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2))

    print(json.dumps(
        {
            "composite_score": result["composite_score"],
            "composite_score_raw": result["composite_score_raw"],
            "passed": result["passed"],
            "flags_hit": result["flags_hit"],
            "out": str(out_path),
        },
        indent=2,
        ensure_ascii=False,
    ))
    return 0


if __name__ == "__main__":
    sys.exit(main())
