"""End-to-end pipeline: launch one or more agents, judge each, aggregate.

Usage:
    python eval/run_pipeline.py \
        --workspace . \
        --agents qwen3.6-plus codex-cli claude-code \
        --judge-config eval/config.yaml
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import time
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

from eval.agents import REGISTRY
from eval.run_judge import score_agent_run
from eval.utils import Workspace


def _bootstrap_env(workspace_root: Path) -> None:
    """Load .env from the workspace root and propagate NEWAPI_KEY → CLI env vars."""
    env_path = workspace_root / ".env"
    if env_path.exists():
        load_dotenv(env_path, override=False)
    key = os.environ.get("NEWAPI_KEY", "")
    if key and key != "sk-REPLACE_ME":
        os.environ.setdefault("OPENAI_API_KEY", key)
        os.environ.setdefault("ANTHROPIC_AUTH_TOKEN", key)
        os.environ.setdefault("ANTHROPIC_API_KEY", key)


def run_one_agent(workspace: Workspace, agent_id: str, sandbox_root: Path,
                  agent_kwargs: dict[str, Any] | None = None):
    cls = REGISTRY[agent_id]
    runner = cls(workspace=workspace, sandbox_root=sandbox_root, **(agent_kwargs or {}))
    return runner.run()


def persist_run(run_result, results_root: Path) -> Path:
    """Copy agent_questions.json + report.md from sandbox into results_root."""
    rel = f"{run_result.agent_id}/{run_result.sandbox.name}"
    dst = results_root / rel
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)
    src_q = run_result.sandbox / "agent_questions.json"
    src_r = run_result.sandbox / "report" / "report.md"
    shutil.copy2(src_q, dst / "agent_questions.json")
    if src_r.exists():
        (dst / "report").mkdir(exist_ok=True)
        shutil.copy2(src_r, dst / "report" / "report.md")
    (dst / "_meta.json").write_text(
        json.dumps(
            {
                "agent_id": run_result.agent_id,
                "wall_time_s": run_result.wall_time_s,
                "sandbox": str(run_result.sandbox),
            },
            indent=2,
        )
    )
    (dst / "_logs.txt").write_text(run_result.raw_logs)
    return dst


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", required=True, type=Path)
    ap.add_argument("--agents", nargs="+", required=True,
                    choices=list(REGISTRY.keys()))
    ap.add_argument("--judge-config", required=True, type=Path)
    ap.add_argument("--sandbox-root", type=Path, default=Path(".sandboxes"))
    ap.add_argument("--results-root", type=Path, default=None,
                    help="Default: <workspace>/results/")
    ap.add_argument("--skip-agents", action="store_true",
                    help="Skip running agents; only judge existing outputs.")
    args = ap.parse_args()

    ws = Workspace.from_root(args.workspace)
    _bootstrap_env(ws.root)
    results_root = args.results_root or (ws.root / "results")
    results_root.mkdir(parents=True, exist_ok=True)

    cfg = yaml.safe_load(args.judge_config.read_text())
    agent_overrides: dict[str, dict[str, Any]] = cfg.get("agents", {}) or {}

    leaderboard: list[dict[str, Any]] = []

    for agent_id in args.agents:
        agent_dir = results_root / agent_id

        if args.skip_agents:
            run_dirs = sorted(p for p in agent_dir.glob("*") if p.is_dir())
            if not run_dirs:
                print(f"[skip-agents] no results for {agent_id}, skipping.")
                continue
            target = run_dirs[-1]
        else:
            kwargs = agent_overrides.get(agent_id, {}) or {}
            print(f"[agent] running {agent_id} (kwargs={list(kwargs)}) ...")
            run = run_one_agent(
                ws, agent_id, sandbox_root=args.sandbox_root, agent_kwargs=kwargs
            )
            target = persist_run(run, results_root)
            print(f"[agent] {agent_id} -> {target}  ({run.wall_time_s:.1f}s)")

        print(f"[judge] scoring {target} ...")
        scores = score_agent_run(ws, target, args.judge_config)
        out = target / "judge_scores.json"
        out.write_text(json.dumps(scores, ensure_ascii=False, indent=2))

        leaderboard.append(
            {
                "agent_id": agent_id,
                "run_dir": str(target),
                "composite_score": scores["composite_score"],
                "composite_score_raw": scores["composite_score_raw"],
                "passed": scores["passed"],
                "flags_hit": scores["flags_hit"],
                "per_dimension": {
                    d["id"]: {
                        "raw": d["capped_raw"],
                        "weight": d["weight"],
                        "flags": d["flags"],
                    }
                    for d in scores["dimensions"]
                },
            }
        )

    leaderboard.sort(key=lambda r: r["composite_score"], reverse=True)
    summary_path = results_root / f"leaderboard_{time.strftime('%Y%m%dT%H%M%S')}.json"
    summary_path.write_text(json.dumps(leaderboard, ensure_ascii=False, indent=2))

    print("\n=== leaderboard ===")
    for row in leaderboard:
        print(
            f"{row['agent_id']:>16s}  "
            f"composite={row['composite_score']:.3f}  "
            f"raw={row['composite_score_raw']:.2f}/5  "
            f"passed={row['passed']}  "
            f"flags={row['flags_hit']}"
        )
    print(f"\nleaderboard -> {summary_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
