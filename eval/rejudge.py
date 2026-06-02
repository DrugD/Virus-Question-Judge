"""Re-judge existing agent outputs with a different judge LLM.

Reuses the agent_questions.json files already generated under
webapp_runs/eval-v1-<qset>/runs/eval-v1-<qset>-<old-judge>/results/<agent>/<ts>/
and only re-runs the judge step. Outputs go to a NEW run dir keyed by the
new judge id, so the old results stay untouched.

Usage:
    .venv/bin/python -m eval.rejudge --judge claude-opus-4-7
    .venv/bin/python -m eval.rejudge --judge claude-opus-4-7 --batch eval-v1
    .venv/bin/python -m eval.rejudge --judge claude-opus-4-7 --tasks zooplankton
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
from eval.metrics import score_against_gold          # noqa: E402
from eval.metrics.judge_llm import JudgeConfig, JudgeLLM  # noqa: E402
from eval.utils import AgentOutput                   # noqa: E402

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
    raise ValueError(f"unknown judge_id: {judge_id!r}; check eval/config.yaml judge_options")


def _find_agent_outputs(upl_dir: Path, agent: str) -> Path | None:
    """Find the latest agent_questions.json across any prior judge's run dir
    for this (upload, agent). Returns None if the agent never produced output."""
    candidates = []
    for run_dir in (upl_dir / "runs").glob("*"):
        for ts_dir in (run_dir / "results" / agent).glob("*") if (run_dir / "results" / agent).is_dir() else []:
            aq = ts_dir / "agent_questions.json"
            if aq.exists():
                candidates.append((ts_dir.name, aq))
    if not candidates:
        return None
    # latest by ts_dir name
    candidates.sort(key=lambda x: x[0], reverse=True)
    return candidates[0][1]


async def rejudge_one_agent(judge: JudgeLLM, threshold: float, qset: str,
                            agent: str, agent_questions_path: Path,
                            gold_questions: list, features: list,
                            target_dir: Path) -> dict:
    """Score one agent's 5 candidates with the new judge. Returns leaderboard row."""
    target_dir.mkdir(parents=True, exist_ok=True)
    # copy agent_questions.json + report.md (so the run dir is self-contained)
    import shutil
    shutil.copy2(agent_questions_path, target_dir / "agent_questions.json")
    src_report = agent_questions_path.parent / "report" / "report.md"
    if src_report.exists():
        (target_dir / "report").mkdir(exist_ok=True)
        shutil.copy2(src_report, target_dir / "report" / "report.md")

    payload = json.loads(agent_questions_path.read_text())
    agent_output = AgentOutput.model_validate(payload)
    candidates = agent_output.to_judge_payloads()

    started = time.time()
    # Score candidates SERIALLY — Bedrock-routed Claude Opus 4.7 has a low
    # concurrent-request ceiling and silently returns empty bodies when
    # burst-hit. JudgeLLM.chat_json now also retries on empty bodies with
    # extended backoff, but a small inter-candidate sleep keeps us safely
    # under the per-key rate limit on the gateway side.
    candidate_results = []
    for c in candidates:
        r = await asyncio.to_thread(score_against_gold, judge, c, gold_questions, features, threshold)
        candidate_results.append(r)
        await asyncio.sleep(1.5)  # spacing between candidates
    judge_wall = time.time() - started

    # pick best candidate by composite_score
    best_idx = max(
        range(len(candidate_results)),
        key=lambda i: (candidate_results[i].composite_score
                       if candidate_results[i].composite_score is not None else -1),
    )
    gold_result = candidate_results[best_idx]
    candidate = candidates[best_idx]

    # write per-candidate scores
    all_scores = []
    for c, r in zip(candidates, candidate_results):
        all_scores.append({
            "rank": c["rank"], "question": c["question"],
            "composite_score": r.composite_score,
            "composite_score_raw": r.composite_score_raw,
            "passed": r.passed,
            "matched_gold_id": r.matched_gold_id,
            "matched_gold_question": r.matched_gold_question,
            "matched_centrality": r.matched_centrality,
            "scores": r.scores,
            "per_dimension_reasoning": r.per_dimension_reasoning,
            "closest_acceptable_variant": r.closest_acceptable_variant,
            "closest_unacceptable_variant": r.closest_unacceptable_variant,
            "rationale": r.rationale,
            "covered_required_elements": r.covered_required_elements,
            "missing_required_elements": r.missing_required_elements,
        })
    (target_dir / "judge_scores.json").write_text(
        json.dumps(gold_result.to_json(), ensure_ascii=False, indent=2))
    (target_dir / "judge_scores_all_candidates.json").write_text(
        json.dumps(all_scores, ensure_ascii=False, indent=2))

    # Pass@k stats
    passes = [c.get("passed", False) for c in sorted(all_scores, key=lambda x: x.get("rank", 99))]
    weights = [5, 4, 3, 2, 1]
    weighted_num = sum((1 + weights[i]) for i, p in enumerate(passes[:5]) if p)
    p1 = 1.0 if (passes and passes[0]) else 0.0
    p5 = weighted_num / 20.0

    return {
        "agent_id": agent, "ok": True,
        "composite_score": gold_result.composite_score,
        "composite_score_raw": gold_result.composite_score_raw,
        "passed": gold_result.passed,
        "pass_at_1": passes[0] if passes else False,
        "pass_at_1_value": p1,
        "pass_at_5": p5 > 0,
        "pass_at_5_value": p5,
        "pass_count": sum(passes),
        "matched_gold_id": gold_result.matched_gold_id,
        "matched_gold_question": gold_result.matched_gold_question,
        "matched_centrality": gold_result.matched_centrality,
        "scores": gold_result.scores,
        "weights": gold_result.weights,
        "covered_required_elements": gold_result.covered_required_elements,
        "missing_required_elements": gold_result.missing_required_elements,
        "rationale": gold_result.rationale,
        "per_dimension_reasoning": gold_result.per_dimension_reasoning,
        "closest_acceptable_variant": gold_result.closest_acceptable_variant,
        "closest_unacceptable_variant": gold_result.closest_unacceptable_variant,
        "candidate": candidate,
        "best_candidate_rank": candidate.get("rank"),
        "all_candidate_scores": all_scores,
        "candidate_count": len(candidates),
        "judge_wall_time_s": judge_wall,
        "rejudged_from": str(agent_questions_path),
    }


async def rejudge_one_pipeline(judge_id: str, qset: str, threshold: float) -> dict:
    upl_dir = WEBAPP_RUNS / f"eval-v1-{qset}"
    workspace = upl_dir / "workspace"
    if not (workspace / "INSTRUCTIONS.md").exists():
        return {"qset": qset, "judge": judge_id, "skipped": True, "reason": "workspace missing"}

    gold_path = workspace / "gold" / "gold_questions.json"
    gold_questions = json.loads(gold_path.read_text())["gold_scientific_questions"]
    manifest = json.loads((upl_dir / "manifest.json").read_text()) if (upl_dir / "manifest.json").exists() else {}
    features = manifest.get("available_features", [])

    judge = JudgeLLM(JudgeConfig(**_resolve_judge_config(judge_id)))

    # Output dir for this judge's run
    run_id = f"eval-v1-{qset}-{judge_id}"
    run_dir = upl_dir / "runs" / run_id
    if (run_dir / "results" / "leaderboard.json").exists():
        return {"qset": qset, "judge": judge_id, "skipped": True,
                "reason": "leaderboard already exists",
                "leaderboard": str(run_dir / "results" / "leaderboard.json")}
    results_root = run_dir / "results"
    results_root.mkdir(parents=True, exist_ok=True)

    rows = []
    print(f"[{time.strftime('%H:%M:%S')}] ▶ rejudge {qset} × {judge_id}", flush=True)
    started = time.time()
    for agent in AGENT_REGISTRY.keys():
        aq_path = _find_agent_outputs(upl_dir, agent)
        if aq_path is None:
            rows.append({"agent_id": agent, "ok": False, "error": "no prior agent_questions.json"})
            continue
        ts = time.strftime("%Y%m%dT%H%M%S")
        target = results_root / agent / ts
        try:
            row = await rejudge_one_agent(
                judge, threshold, qset, agent, aq_path,
                gold_questions, features, target,
            )
            row["run_dir"] = str(target)
            rows.append(row)
        except Exception as e:
            rows.append({"agent_id": agent, "ok": False,
                         "error": f"{type(e).__name__}: {e}"})
        # be a polite citizen — small delay between agents
        await asyncio.sleep(0.2)

    rows.sort(key=lambda r: -(r.get("composite_score") or -1))
    leaderboard = {
        "run_id": run_id,
        "judge_model": judge_id,
        "results_root": str(results_root),
        "rows": rows,
    }
    (results_root / "leaderboard.json").write_text(
        json.dumps(leaderboard, ensure_ascii=False, indent=2))

    wall = time.time() - started
    ok = sum(1 for r in rows if r.get("ok"))
    print(f"[{time.strftime('%H:%M:%S')}] ◀ rejudge {qset} × {judge_id}  ok={ok}/{len(rows)}  wall={wall:.0f}s", flush=True)
    return {"qset": qset, "judge": judge_id, "skipped": False,
            "ok_after": ok, "fail_after": len(rows) - ok,
            "wall_s": wall,
            "leaderboard": str(results_root / "leaderboard.json")}


async def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--judge", required=True, help="judge id from eval/config.yaml judge_options")
    ap.add_argument("--batch", default="eval-v1", help="upload-id prefix to scan")
    ap.add_argument("--tasks", default="", help="substring filter on qset (default: all)")
    ap.add_argument("--threshold", type=float, default=JUDGE_CFG.get("threshold", 0.6))
    args = ap.parse_args()

    _bootstrap_env()

    qsets = sorted(d.name.replace(f"{args.batch}-", "")
                   for d in WEBAPP_RUNS.iterdir()
                   if d.is_dir() and d.name.startswith(f"{args.batch}-"))
    if args.tasks:
        qsets = [q for q in qsets if args.tasks in q]
    if not qsets:
        print("no qsets matched.", file=sys.stderr); return 1

    print(f"plan: {len(qsets)} qsets × judge={args.judge} (single judge re-eval)")
    print(f"      qsets: {qsets}")

    summaries = []
    for qset in qsets:
        try:
            s = await rejudge_one_pipeline(args.judge, qset, args.threshold)
        except Exception as e:
            s = {"qset": qset, "judge": args.judge, "error": f"{type(e).__name__}: {e}"}
            print(f"!!! {qset} FAILED: {s['error']}", flush=True)
        summaries.append(s)
        ckpt = WEBAPP_RUNS / f"eval-v1-rejudge-{args.judge}-progress.json"
        ckpt.write_text(json.dumps(summaries, ensure_ascii=False, indent=2, default=str))

    final = WEBAPP_RUNS / f"eval-v1-rejudge-{args.judge}-summary.json"
    final.write_text(json.dumps(summaries, ensure_ascii=False, indent=2, default=str))
    print(f"\n=== rejudge done · {len(summaries)} qsets · summary → {final}")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
