"""Systematic evaluation driver — eval-v1 batch.

Runs every current agent on every task in `data/`, judged by every judge LLM
listed in `eval/config.yaml::judge_options`. Bypasses the webapp HTTP layer
and drives `webapp.pipeline_runner.PipelineRunner` directly so we can pin
custom run_ids (eval-v1-<qset>-<judge>) instead of the default run_<unix>.

Layout (per (qset, judge) pair):

    webapp_runs/eval-v1-<qset>/
        manifest.json
        workspace/
            INSTRUCTIONS.md
            info.json
            data/                   ← copy of data/<qset>/raw/
            gold/gold_questions.json ← normalised
        runs/eval-v1-<qset>-<judge_id>/
            results/
                leaderboard.json
                <agent>/<ts>/{agent_questions.json,judge_scores.json,...}
            sandboxes/
            events.jsonl

Usage:

    .venv/bin/python -m eval.run_systematic                    # run everything
    .venv/bin/python -m eval.run_systematic --tasks zooplank   # filter by qset substring
    .venv/bin/python -m eval.run_systematic --resume           # skip pairs whose leaderboard.json already exists
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import time
from pathlib import Path

import yaml
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from eval.agents import REGISTRY as AGENT_REGISTRY  # noqa: E402
from webapp.gold_validator import validate_gold      # noqa: E402
from webapp.pipeline_runner import (                 # noqa: E402
    EventBus, PipelineRunner, RunSpec, hydrate_workspace,
)


DATA_ROOT = PROJECT_ROOT / "data"
WEBAPP_RUNS = PROJECT_ROOT / "webapp_runs"
JUDGE_CFG = yaml.safe_load((PROJECT_ROOT / "eval/config.yaml").read_text())

# every current agent in the registry (11 as of eval-v1)
ALL_AGENTS = list(AGENT_REGISTRY.keys())

# judges from config.yaml judge_options
JUDGES = [opt["id"] for opt in JUDGE_CFG.get("judge_options", [])]


def _bootstrap_env() -> None:
    env_path = PROJECT_ROOT / ".env"
    if env_path.exists():
        load_dotenv(env_path, override=False)
    key = os.environ.get("NEWAPI_KEY", "")
    if key and key != "sk-REPLACE_ME":
        os.environ.setdefault("OPENAI_API_KEY", key)
        os.environ.setdefault("ANTHROPIC_AUTH_TOKEN", key)
        os.environ.setdefault("ANTHROPIC_API_KEY", key)


def _resolve_judge_config(judge_id: str) -> dict:
    """Mirror webapp.server._resolve_judge_config — pick the matching judge_options block."""
    base = JUDGE_CFG.get("judge", {}).copy()
    for opt in JUDGE_CFG.get("judge_options", []):
        if opt.get("id") == judge_id:
            for k in ("provider", "model", "max_tokens", "timeout", "temperature",
                     "max_retries", "base_url", "api_key_env"):
                if k in opt:
                    base[k] = opt[k]
            # JudgeConfig dataclass doesn't accept stray fields like `id` /
            # `label` / `description` — strip them before returning.
            return {k: v for k, v in base.items() if k not in ("id", "label", "description")}
    raise ValueError(f"unknown judge_id: {judge_id!r}; available: {JUDGES}")


def _hydrate_qset_workspace(qset: str) -> tuple[Path, list[str], Path]:
    """Build webapp_runs/eval-v1-<qset>/ if it doesn't already exist; return (workspace_root, available_features, upload_dir)."""
    upload_dir = WEBAPP_RUNS / f"eval-v1-{qset}"
    workspace_dir = upload_dir / "workspace"
    if (workspace_dir / "INSTRUCTIONS.md").exists() and (workspace_dir / "gold" / "gold_questions.json").exists():
        # already hydrated — read available_features from manifest
        m = json.loads((upload_dir / "manifest.json").read_text())
        return workspace_dir, m.get("available_features", []), upload_dir

    src_data = DATA_ROOT / qset / "raw"
    src_gold = DATA_ROOT / qset / "gold_scientific_questions.json"
    if not src_data.is_dir():
        raise FileNotFoundError(f"missing data dir: {src_data}")
    if not src_gold.is_file():
        raise FileNotFoundError(f"missing gold: {src_gold}")

    upload_dir.mkdir(parents=True, exist_ok=True)
    # normalise gold via gold_validator
    norm_path = upload_dir / "_gold_normalised.json"
    rep = validate_gold(src_gold, norm_path)
    if not rep.ok:
        raise RuntimeError(f"gold validation failed for {qset}: {rep.errors}")

    workspace_dir, feats = hydrate_workspace(src_data, norm_path, workspace_dir)
    (upload_dir / "manifest.json").write_text(json.dumps({
        "upload_id": f"eval-v1-{qset}",
        "question_set_id": qset,
        "available_features": feats,
        "ok": True,
        "stage": "ready",
        "created_at": time.time(),
    }, ensure_ascii=False, indent=2))
    return workspace_dir, feats, upload_dir


async def run_one(qset: str, judge_id: str, agents: list[str], threshold: float) -> dict:
    workspace_root, features, upload_dir = _hydrate_qset_workspace(qset)
    run_id = f"eval-v1-{qset}-{judge_id}"
    run_dir = upload_dir / "runs" / run_id
    if (run_dir / "results" / "leaderboard.json").exists():
        return {"qset": qset, "judge": judge_id, "skipped": True,
                "leaderboard": str(run_dir / "results" / "leaderboard.json")}
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "results").mkdir(exist_ok=True)
    (run_dir / "sandboxes").mkdir(exist_ok=True)

    judge_cfg = _resolve_judge_config(judge_id)
    spec = RunSpec(
        run_id=run_id,
        workspace_root=workspace_root,
        gold_path=workspace_root / "gold" / "gold_questions.json",
        available_features=features,
        agents=list(agents),
        judge_config=judge_cfg,
        threshold=threshold,
        results_root=run_dir / "results",
        sandbox_root=run_dir / "sandboxes",
    )
    bus = EventBus()
    runner = PipelineRunner(spec, bus)

    started = time.time()
    print(f"[{time.strftime('%H:%M:%S')}] ▶ {run_id}  ({len(agents)} agents · judge={judge_id})", flush=True)
    leaderboard = await runner.run()
    wall = time.time() - started
    rows = leaderboard.get("rows", [])
    ok = sum(1 for r in rows if r.get("ok"))
    print(f"[{time.strftime('%H:%M:%S')}] ◀ {run_id}  ok={ok}/{len(rows)}  wall={wall:.0f}s", flush=True)
    return {"qset": qset, "judge": judge_id, "skipped": False,
            "leaderboard": str(run_dir / "results" / "leaderboard.json"),
            "rows": rows, "wall_s": wall}


async def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tasks", default="", help="substring filter on qset name (default: all)")
    ap.add_argument("--judges", nargs="+", default=JUDGES, help=f"subset of {JUDGES}")
    ap.add_argument("--agents", nargs="+", default=ALL_AGENTS,
                    help=f"subset of registry (default: all {len(ALL_AGENTS)} agents)")
    ap.add_argument("--threshold", type=float, default=JUDGE_CFG.get("threshold", 0.6))
    ap.add_argument("--resume", action="store_true", help="skip (qset, judge) pairs whose leaderboard.json already exists")
    args = ap.parse_args()

    _bootstrap_env()

    qsets = sorted(d.name for d in DATA_ROOT.iterdir() if d.is_dir())
    if args.tasks:
        qsets = [q for q in qsets if args.tasks in q]
    if not qsets:
        print("no tasks matched.", file=sys.stderr); return 1

    bad_agents = [a for a in args.agents if a not in AGENT_REGISTRY]
    if bad_agents:
        print(f"unknown agents: {bad_agents}", file=sys.stderr); return 2
    bad_judges = [j for j in args.judges if j not in JUDGES]
    if bad_judges:
        print(f"unknown judges: {bad_judges} (available: {JUDGES})", file=sys.stderr); return 2

    pairs = [(q, j) for q in qsets for j in args.judges]
    print(f"plan: {len(qsets)} tasks × {len(args.judges)} judges = {len(pairs)} pipelines")
    print(f"      agents per pipeline: {len(args.agents)}  total agent-runs: {len(pairs) * len(args.agents)}")
    print(f"      judges: {args.judges}")
    print(f"      tasks:  {qsets}")

    # serial across (qset, judge) pairs — agents within a pipeline are already
    # parallel via asyncio.gather inside PipelineRunner.run().
    summaries: list[dict] = []
    for qset, judge in pairs:
        try:
            s = await run_one(qset, judge, args.agents, args.threshold)
        except Exception as e:
            print(f"!!! pipeline FAILED · {qset} × {judge}: {type(e).__name__}: {e}", flush=True)
            s = {"qset": qset, "judge": judge, "error": f"{type(e).__name__}: {e}"}
        summaries.append(s)
        # checkpoint progress
        ckpt = WEBAPP_RUNS / "eval-v1-progress.json"
        ckpt.write_text(json.dumps(summaries, ensure_ascii=False, indent=2, default=str))

    # final summary
    final = WEBAPP_RUNS / "eval-v1-summary.json"
    final.write_text(json.dumps(summaries, ensure_ascii=False, indent=2, default=str))
    print(f"\n=== eval-v1 done · {len(summaries)} pipelines · summary → {final}")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
