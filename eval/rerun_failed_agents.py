"""Surgical re-run of failed agents in eval-v1.

For every pipeline under webapp_runs/eval-v1-*/, scan the existing
leaderboard.json and re-run ONLY the agents whose row has `ok: false` (or
that are missing entirely). The retry budget per agent is whatever
pipeline_runner.MAX_ATTEMPTS is set to (currently 5).

Successful re-runs are merged back into the original leaderboard.json so
agents that already passed yesterday keep their results.

Usage:
    .venv/bin/python -m eval.rerun_failed_agents             # rerun every failed cell
    .venv/bin/python -m eval.rerun_failed_agents --dry-run   # just print what would run
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
from webapp.pipeline_runner import (                 # noqa: E402
    EventBus, PipelineRunner, RunSpec, _WebWorkspace, _pass_at_k_stats,
)
from eval.utils.schemas import AgentOutput            # noqa: E402

WEBAPP_RUNS = PROJECT_ROOT / "webapp_runs"
JUDGE_CFG = yaml.safe_load((PROJECT_ROOT / "eval/config.yaml").read_text())


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
    base = JUDGE_CFG.get("judge", {}).copy()
    for opt in JUDGE_CFG.get("judge_options", []):
        if opt.get("id") == judge_id:
            for k in ("provider", "model", "max_tokens", "timeout", "temperature",
                     "max_retries", "base_url", "api_key_env"):
                if k in opt:
                    base[k] = opt[k]
            return {k: v for k, v in base.items() if k not in ("id", "label", "description")}
    raise ValueError(f"unknown judge_id: {judge_id!r}")


def _scan_failures(exclude_agents: set[str] = frozenset()) -> list[tuple[str, str, list[str], Path, Path]]:
    """Return list of (qset, judge, [failed agents], lb_path, run_dir).

    Includes pipelines that have no leaderboard at all (treated as fully-failed).
    Agents in `exclude_agents` are silently dropped (no retry attempted).
    """
    out = []
    JUDGES = [opt["id"] for opt in JUDGE_CFG.get("judge_options", [])]
    ALL_AGENTS = [a for a in AGENT_REGISTRY.keys() if a not in exclude_agents]
    for upl_dir in sorted(WEBAPP_RUNS.glob("eval-v1-*")):
        if not upl_dir.is_dir():
            continue
        qset = upl_dir.name.replace("eval-v1-", "")
        for judge in JUDGES:
            run_dir = upl_dir / "runs" / f"eval-v1-{qset}-{judge}"
            lb_path = run_dir / "results" / "leaderboard.json"
            failed: list[str] = []
            if not lb_path.exists():
                failed = list(ALL_AGENTS)
            else:
                try:
                    lb = json.load(open(lb_path))
                    by_id = {r.get("agent_id"): r for r in lb.get("rows", [])}
                    for a in ALL_AGENTS:
                        row = by_id.get(a)
                        if row is None or not row.get("ok"):
                            failed.append(a)
                except Exception as e:
                    print(f"[warn] failed to parse {lb_path}: {e}")
                    failed = list(ALL_AGENTS)
            if failed:
                out.append((qset, judge, failed, lb_path, run_dir))
    return out


async def _rerun_one(qset: str, judge: str, agents_to_run: list[str],
                     lb_path: Path, run_dir: Path, threshold: float) -> dict:
    """Re-run the given agents under (qset, judge) and merge into existing leaderboard.json."""
    upl_dir = run_dir.parent.parent
    workspace_root = upl_dir / "workspace"
    if not (workspace_root / "INSTRUCTIONS.md").exists():
        return {"qset": qset, "judge": judge, "skipped": True, "reason": "workspace not hydrated"}

    manifest = json.loads((upl_dir / "manifest.json").read_text()) if (upl_dir / "manifest.json").exists() else {}
    features = manifest.get("available_features", [])

    # ---- CRITICAL: snapshot the old leaderboard BEFORE runner.run() ----
    # PipelineRunner.run() writes leaderboard.json directly to spec.results_root.
    # If we read `old` after run(), we'd be reading the freshly-overwritten
    # subset-only file → all the previously-successful rows would be lost.
    # Snapshot it now so the merge below has the real "old" state.
    old: dict = {}
    if lb_path.exists():
        try:
            old = json.load(open(lb_path))
        except Exception:
            old = {}

    # results dir is shared with the original pipeline so per-agent dirs end up
    # in the same place as before. Sandbox dir gets a fresh timestamp so the
    # original artefacts stay intact.
    results_root = run_dir / "results"
    sandbox_root = run_dir / "sandboxes"
    results_root.mkdir(parents=True, exist_ok=True)
    sandbox_root.mkdir(parents=True, exist_ok=True)

    judge_cfg = _resolve_judge_config(judge)
    spec = RunSpec(
        run_id=f"eval-v1-{qset}-{judge}-rerun",
        workspace_root=workspace_root,
        gold_path=workspace_root / "gold" / "gold_questions.json",
        available_features=features,
        agents=list(agents_to_run),
        judge_config=judge_cfg,
        threshold=threshold,
        results_root=results_root,
        sandbox_root=sandbox_root,
    )
    bus = EventBus()
    runner = PipelineRunner(spec, bus)

    started = time.time()
    print(f"[{time.strftime('%H:%M:%S')}] ▶ rerun {qset} × {judge}  ({len(agents_to_run)} failed agents: {agents_to_run})", flush=True)
    new_lb = await runner.run()
    wall = time.time() - started

    # ---- merge new rows into the old (snapshotted) leaderboard ----
    if not old:
        old = {"run_id": f"eval-v1-{qset}-{judge}", "rows": []}

    new_by_id = {r["agent_id"]: r for r in new_lb.get("rows", [])}
    merged_rows = []
    for r in old.get("rows", []):
        aid = r.get("agent_id")
        if aid in new_by_id:
            new_r = new_by_id.pop(aid)
            # Only overwrite an old row when the new run actually produced ok=True
            # OR the old was also failed. Never replace a passing row with a fail.
            if not r.get("ok") or new_r.get("ok"):
                merged_rows.append(new_r)
            else:
                merged_rows.append(r)
        else:
            merged_rows.append(r)
    # any agent that wasn't in the original at all (shouldn't happen, but be safe)
    for aid, new_r in new_by_id.items():
        merged_rows.append(new_r)

    merged_rows.sort(key=lambda r: -(r.get("composite_score") or -1))
    merged = dict(old)
    merged["rows"] = merged_rows
    merged["run_id"] = old.get("run_id", f"eval-v1-{qset}-{judge}")
    lb_path.write_text(json.dumps(merged, ensure_ascii=False, indent=2))

    ok_now = sum(1 for r in merged_rows if r.get("ok"))
    fail_now = len(merged_rows) - ok_now
    print(f"[{time.strftime('%H:%M:%S')}] ◀ rerun {qset} × {judge}  → ok={ok_now}/{len(merged_rows)} (fail={fail_now}) wall={wall:.0f}s", flush=True)

    return {
        "qset": qset, "judge": judge,
        "reran_agents": agents_to_run,
        "ok_after": ok_now,
        "fail_after": fail_now,
        "wall_s": wall,
    }


async def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="list failures, don't run")
    ap.add_argument("--threshold", type=float, default=JUDGE_CFG.get("threshold", 0.6))
    ap.add_argument("--exclude", nargs="+", default=[], help="agent ids to skip (no retry attempted)")
    args = ap.parse_args()

    _bootstrap_env()

    excl = set(args.exclude)
    failures = _scan_failures(exclude_agents=excl)
    total_failed = sum(len(f[2]) for f in failures)
    if excl:
        print(f"excluding agents: {sorted(excl)}")
    print(f"failure scan: {len(failures)} pipelines have failed agents · {total_failed} (qset, judge, agent) cells to retry")
    for qset, judge, agents, _, _ in failures:
        print(f"  {qset:34} × {judge:18} · {len(agents):>2} agents · {','.join(a[:8] for a in agents)}")

    if args.dry_run:
        return 0

    summaries: list[dict] = []
    for qset, judge, agents, lb_path, run_dir in failures:
        try:
            s = await _rerun_one(qset, judge, agents, lb_path, run_dir, args.threshold)
        except Exception as e:
            print(f"!!! rerun FAILED · {qset} × {judge}: {type(e).__name__}: {e}", flush=True)
            s = {"qset": qset, "judge": judge, "error": f"{type(e).__name__}: {e}"}
        summaries.append(s)
        ckpt = WEBAPP_RUNS / "eval-v1-rerun-progress.json"
        ckpt.write_text(json.dumps(summaries, ensure_ascii=False, indent=2, default=str))

    final = WEBAPP_RUNS / "eval-v1-rerun-summary.json"
    final.write_text(json.dumps(summaries, ensure_ascii=False, indent=2, default=str))
    print(f"\n=== rerun done · {len(summaries)} pipelines · summary → {final}")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
