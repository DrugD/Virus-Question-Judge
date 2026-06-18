"""Batch judge-only evaluation framework.

Score many candidate scientific-question files — one per agent, or hand-written
by a human — against a gold rubric, WITHOUT invoking any agent. This is the
batch / headless counterpart of the webapp's "CANDIDATE · judge-only" upload.

The blind data is DESENSITIZED exactly like the webapp (the tree is flattened
and every file renamed to ``1.<ext>``, ``2.<ext>`` …, nested archives are
expanded recursively, and the ``filename_map.json`` is kept judge-only) so a
candidate cannot earn the data-grounding dimension just by quoting an
evocative filename such as ``43059586_RdRp_motif_collection.xlsx``. The exact
same ``hydrate_workspace`` / ``_desensitize_data`` code path the server uses is
reused here, so the security property is identical.

--------------------------------------------------------------------------------
Run
--------------------------------------------------------------------------------
    PYTHONUTF8=1 .venv/Scripts/python.exe -m eval.batch_judge \
        --data    path/to/blind_data_dir_or.zip \
        --gold    path/to/gold.json \
        --candidates path/to/candidates_dir/ \
        --judge   gpt-5.5-high \
        --out     batch_runs/my_eval

``--candidates`` may be a directory of ``*.json`` files or one/more explicit
files. Each file is one candidate set (AgentOutput-shaped):

    {
      "agent_id": "claude-opus-4-7",
      "questions": [
        {"rank": 1, "question": "...?"},
        {"rank": 2, "question": "...?"}
      ]
    }

Lenient by default: 1..5 questions, ranks auto-filled when absent, and a bare
list of strings (``"questions": ["...?", "...?"]``) is also accepted — handy
for hand-designed questions. Pass ``--strict`` to enforce the full Pass@5
contract (exactly 5 distinct questions, ranks 1..5).

--------------------------------------------------------------------------------
Monitoring
--------------------------------------------------------------------------------
  * live console:  [i/N] <candidate>  composite=…  pass@1=…  pass@5=…  wall=…s
  * <out>/progress.json  — rewritten after every candidate; tail / poll it
                           from another process for a live dashboard.
  * <out>/leaderboard.json + <out>/summary.md  — written at the end.

Resumable: a re-run skips candidates that already produced judge_scores.json
unless ``--force`` is given.

--------------------------------------------------------------------------------
Dry run (no judge key needed)
--------------------------------------------------------------------------------
    ... --dry-run
Desensitizes the data, validates the gold + every candidate, and prints the
plan WITHOUT calling the judge LLM. Use this to verify the pipeline (and that
desensitization worked) before spending tokens.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Desensitization + Pass@k live in the webapp module; these imports pull in only
# eval/ + stdlib (no FastAPI), so this stays usable headless.
from webapp.pipeline_runner import (  # noqa: E402
    hydrate_workspace, _pass_at_k_stats, build_data_digest, rescore_open_if_missed,
)
from webapp.gold_validator import validate_gold                         # noqa: E402
from webapp.validator import validate_data_zip, DataValidationError     # noqa: E402

from eval.metrics import score_against_gold                             # noqa: E402
from eval.metrics.judge_llm import JudgeConfig, JudgeLLM                # noqa: E402

JUDGE_CFG = yaml.safe_load((PROJECT_ROOT / "eval/config.yaml").read_text())
_PLACEHOLDER_KEYS = {"", "sk-xxx", "sk-REPLACE_ME"}
_MAX_QUESTIONS = 5


# ---------------------------------------------------------------------------
# env + judge config (mirrors eval/rejudge.py so behaviour is consistent)
# ---------------------------------------------------------------------------
def _bootstrap_env() -> str:
    env_path = PROJECT_ROOT / ".env"
    if env_path.exists():
        load_dotenv(env_path, override=False)
    key = os.environ.get("NEWAPI_KEY", "")
    if key and key not in _PLACEHOLDER_KEYS:
        os.environ.setdefault("OPENAI_API_KEY", key)
        os.environ.setdefault("ANTHROPIC_AUTH_TOKEN", key)
        os.environ.setdefault("ANTHROPIC_API_KEY", key)
    return key


def _resolve_judge_config(judge_id: str) -> dict[str, Any]:
    base = dict(JUDGE_CFG.get("judge", {}))
    if not judge_id:
        return {k: v for k, v in base.items() if k not in ("id", "label", "description")}
    for opt in JUDGE_CFG.get("judge_options", []):
        if (opt.get("id") or opt.get("model")) == judge_id:
            for k in ("provider", "model", "max_tokens", "timeout", "temperature",
                      "max_retries", "base_url", "api_key_env"):
                if k in opt:
                    base[k] = opt[k]
            return {k: v for k, v in base.items() if k not in ("id", "label", "description")}
    raise ValueError(
        f"unknown judge id {judge_id!r}; available: "
        f"{[o.get('id') for o in JUDGE_CFG.get('judge_options', [])]}"
    )


# ---------------------------------------------------------------------------
# workspace preparation (desensitization)
# ---------------------------------------------------------------------------
def prepare_workspace(
    data: Path, gold: Path, out: Path, reuse: bool,
) -> tuple[Path, list[dict[str, Any]], list[str]]:
    """Validate gold, desensitize data, hydrate a judge-only workspace.

    Returns (workspace_root, gold_questions, available_features).
    """
    out.mkdir(parents=True, exist_ok=True)
    ws_root = out / "workspace"
    gold_norm = out / "gold_questions.json"

    # 1. gold → normalised {"gold_scientific_questions": [...]}
    report = validate_gold(gold, gold_norm)
    if not report.ok:
        raise SystemExit(f"gold validation failed:\n  " + "\n  ".join(report.errors))
    print(f"  gold: {report.total_count} questions "
          f"(primary={report.primary_count}, secondary={report.secondary_count})", flush=True)

    # 2. reuse a previously-hydrated (already desensitized) workspace if asked
    if reuse and (ws_root / "info.json").exists() and (ws_root / "filename_map.json").exists():
        feats = [f["path"] for f in json.loads((ws_root / "info.json").read_text()).get("files", [])]
        print(f"  workspace: reusing {ws_root} ({len(feats)} desensitized files)", flush=True)
        gold_questions = json.loads(gold_norm.read_text())["gold_scientific_questions"]
        return ws_root, gold_questions, feats

    # 3. resolve the data root (a dir is used as-is; a zip is extracted first)
    data = Path(data)
    if data.is_dir():
        data_root = data
    elif data.suffix.lower() == ".zip":
        extracted = out / "_extracted"
        try:
            dreport = validate_data_zip(data, extracted)
        except DataValidationError as e:
            raise SystemExit(f"data zip invalid: {e}")
        if not dreport.ok:
            raise SystemExit("data zip validation failed: " + "; ".join(dreport.errors))
        data_root = Path(dreport.data_root)
    else:
        raise SystemExit(f"--data must be a directory or a .zip, got: {data}")

    # 4. hydrate → DESENSITIZED workspace + available_features (anonymised names)
    _, feats = hydrate_workspace(data_dir=data_root, gold_normalised=gold_norm, dst=ws_root)
    print(f"  workspace: desensitized {len(feats)} files → {ws_root}", flush=True)
    print(f"             filename_map.json (judge-only) written; agent-visible "
          f"names are 1.ext, 2.ext, …", flush=True)
    gold_questions = json.loads(gold_norm.read_text())["gold_scientific_questions"]
    return ws_root, gold_questions, feats


# ---------------------------------------------------------------------------
# candidate loading (lenient by default, strict on request)
# ---------------------------------------------------------------------------
def _normalise_candidate(payload: dict[str, Any], fallback_id: str, strict: bool) -> tuple[str, list[dict[str, Any]]]:
    agent_id = str(payload.get("agent_id") or fallback_id)
    raw = payload.get("questions")
    if not isinstance(raw, list) or not raw:
        raise ValueError("missing non-empty 'questions' list")

    judge_payloads: list[dict[str, Any]] = []
    seen: set[str] = set()
    for i, q in enumerate(raw, start=1):
        if isinstance(q, str):
            text, rank = q, i
        elif isinstance(q, dict):
            text, rank = q.get("question", ""), q.get("rank", i)
        else:
            raise ValueError(f"question #{i} must be a string or object")
        text = str(text).strip()
        if not text:
            raise ValueError(f"question #{i} is empty")
        if not text.endswith("?"):
            raise ValueError(f"question #{i} must end with '?': {text[:60]!r}")
        key = " ".join(text.lower().split())
        if key in seen:
            raise ValueError(f"duplicate question: {text[:60]!r}")
        seen.add(key)
        judge_payloads.append({"agent_id": agent_id, "rank": int(rank), "question": text})

    if len(judge_payloads) > _MAX_QUESTIONS:
        raise ValueError(f"at most {_MAX_QUESTIONS} questions allowed, got {len(judge_payloads)}")
    if strict:
        ranks = sorted(c["rank"] for c in judge_payloads)
        if ranks != list(range(1, _MAX_QUESTIONS + 1)):
            raise ValueError(f"--strict requires exactly {_MAX_QUESTIONS} questions "
                             f"with ranks 1..{_MAX_QUESTIONS}, got ranks {ranks}")
    judge_payloads.sort(key=lambda c: c["rank"])
    return agent_id, judge_payloads


def load_candidates(paths: list[Path], strict: bool) -> list[dict[str, Any]]:
    """Expand dirs → *.json files, parse + normalise each candidate set."""
    files: list[Path] = []
    for p in paths:
        p = Path(p)
        if p.is_dir():
            files.extend(sorted(p.glob("*.json")))
        elif p.is_file():
            files.append(p)
        else:
            raise SystemExit(f"--candidates path not found: {p}")
    if not files:
        raise SystemExit("no candidate *.json files found")

    out: list[dict[str, Any]] = []
    for f in files:
        cid = f.stem
        try:
            payload = json.loads(f.read_text(encoding="utf-8"))
            agent_id, judge_payloads = _normalise_candidate(payload, cid, strict)
        except Exception as e:
            out.append({"candidate_id": cid, "source": str(f), "ok": False,
                        "error": f"{type(e).__name__}: {e}"})
            continue
        out.append({"candidate_id": cid, "source": str(f), "ok": True,
                    "agent_id": agent_id, "candidates": judge_payloads})
    return out


# ---------------------------------------------------------------------------
# scoring one candidate set
# ---------------------------------------------------------------------------
async def score_candidate(
    judge: JudgeLLM,
    sem: asyncio.Semaphore,
    spacing: float,
    threshold: float,
    features: list[str],
    gold_questions: list[dict[str, Any]],
    cand: dict[str, Any],
    results_root: Path,
    data_digest: str = "",
) -> dict[str, Any]:
    agent_id = cand["agent_id"]
    candidates = cand["candidates"]
    target = results_root / cand["candidate_id"] / time.strftime("%Y%m%dT%H%M%S")
    target.mkdir(parents=True, exist_ok=True)
    (target / "agent_questions.json").write_text(
        json.dumps({"agent_id": agent_id,
                    "questions": [{"rank": c["rank"], "question": c["question"]} for c in candidates]},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    async def _score_one(c: dict[str, Any]):
        async with sem:
            r = await asyncio.to_thread(
                score_against_gold, judge, c, gold_questions, features, threshold)
            if spacing:
                await asyncio.sleep(spacing)
            return r

    started = time.time()
    candidate_results = await asyncio.gather(*[_score_one(c) for c in candidates])
    # per-question routing: closed-failed questions get open rubric re-score.
    candidate_results, rubric_kind = await rescore_open_if_missed(
        judge, candidates, candidate_results, data_digest, threshold)
    judge_wall = time.time() - started

    best_idx = max(range(len(candidate_results)),
                   key=lambda i: (candidate_results[i].composite_score
                                  if candidate_results[i].composite_score is not None else -1))
    best = candidate_results[best_idx]
    best_cand = candidates[best_idx]

    all_scores = [
        {"rank": c["rank"], "question": c["question"],
         "composite_score": r.composite_score, "composite_score_raw": r.composite_score_raw,
         "passed": r.passed, "matched_gold_id": r.matched_gold_id,
         "matched_gold_question": r.matched_gold_question, "matched_centrality": r.matched_centrality,
         "rubric_kind": getattr(r, "rubric_kind", "closed"),
         "scores": r.scores, "rationale": r.rationale,
         "per_dimension_reasoning": r.per_dimension_reasoning,
         "covered_required_elements": r.covered_required_elements,
         "missing_required_elements": r.missing_required_elements}
        for c, r in zip(candidates, candidate_results)
    ]
    (target / "judge_scores.json").write_text(
        json.dumps(best.to_json(), ensure_ascii=False, indent=2), encoding="utf-8")
    (target / "judge_scores_all_candidates.json").write_text(
        json.dumps(all_scores, ensure_ascii=False, indent=2), encoding="utf-8")

    pk = _pass_at_k_stats(candidates, candidate_results)
    return {
        "agent_id": agent_id, "candidate_id": cand["candidate_id"], "ok": True,
        "run_dir": str(target), "rubric_kind": rubric_kind,
        "composite_score": best.composite_score, "composite_score_raw": best.composite_score_raw,
        "passed": best.passed, "matched_gold_id": best.matched_gold_id,
        "matched_gold_question": best.matched_gold_question, "matched_centrality": best.matched_centrality,
        "scores": best.scores, "weights": best.weights, "rationale": best.rationale,
        "candidate": best_cand, "best_candidate_rank": best_cand.get("rank"),
        "all_candidate_scores": all_scores, "judge_wall_time_s": judge_wall,
        **pk,
    }


# ---------------------------------------------------------------------------
# orchestration + monitoring
# ---------------------------------------------------------------------------
def _already_done(results_root: Path, candidate_id: str) -> bool:
    cdir = results_root / candidate_id
    if not cdir.is_dir():
        return False
    return any((ts / "judge_scores.json").exists() for ts in cdir.glob("*"))


def _write_progress(progress_path: Path, progress: dict[str, Any]) -> None:
    progress["updated_at"] = time.time()
    progress_path.write_text(json.dumps(progress, ensure_ascii=False, indent=2, default=str),
                             encoding="utf-8")


def _write_summary(out: Path, rows: list[dict[str, Any]], judge_id: str) -> None:
    ok_rows = [r for r in rows if r.get("ok")]
    ok_rows.sort(key=lambda r: -(r.get("avg_composite") or -1))
    lines = [
        f"# Batch judge-only results", "",
        f"- judge: `{judge_id}`",
        f"- candidates: {len(rows)} ({len(ok_rows)} scored, {len(rows) - len(ok_rows)} failed)",
        f"- generated: {time.strftime('%Y-%m-%d %H:%M:%S')}", "",
        "| # | candidate | agent_id | rubric | avg_composite | best | pass@1 | pass@5 | pass_count | matched gold |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(ok_rows, 1):
        lines.append(
            f"| {i} | {r['candidate_id']} | {r['agent_id']} | "
            f"{r.get('rubric_kind', 'closed')} | "
            f"{(r.get('avg_composite') or 0):.3f} | {(r.get('composite_score') or 0):.3f} | "
            f"{(r.get('pass_at_1_value') or 0):.1f} | {(r.get('pass_at_5_value') or 0):.2f} | "
            f"{r.get('pass_count', 0)}/{r.get('candidate_count', 0)} | "
            f"{r.get('matched_gold_id') or '—'} |")
    for r in rows:
        if not r.get("ok"):
            lines.append(f"| — | {r.get('candidate_id')} | — | — | FAILED | | | | | {r.get('error','')} |")
    (out / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


async def main() -> int:
    ap = argparse.ArgumentParser(
        prog="eval.batch_judge",
        description="Batch judge-only evaluation of candidate scientific questions "
                    "(desensitized data, no agent invocation).")
    ap.add_argument("--data", required=True, help="blind data: a directory or a .zip")
    ap.add_argument("--gold", required=True, help="gold question JSON")
    ap.add_argument("--candidates", required=True, nargs="+",
                    help="candidate dir(s) of *.json and/or explicit *.json files")
    ap.add_argument("--out", required=True, help="output run directory")
    ap.add_argument("--judge", default="", help="judge id from eval/config.yaml (default: top-level judge)")
    ap.add_argument("--threshold", type=float, default=JUDGE_CFG.get("threshold", 0.6))
    ap.add_argument("--concurrency", type=int, default=4, help="max concurrent judge calls")
    ap.add_argument("--spacing", type=float, default=0.0, help="seconds to sleep after each judge call")
    ap.add_argument("--strict", action="store_true", help="enforce exactly 5 distinct questions, ranks 1..5")
    ap.add_argument("--reuse-workspace", action="store_true",
                    help="reuse an already-desensitized <out>/workspace instead of rebuilding")
    ap.add_argument("--force", action="store_true", help="re-score candidates even if already done")
    ap.add_argument("--dry-run", action="store_true",
                    help="prepare workspace + validate everything, but do NOT call the judge")
    args = ap.parse_args()

    out = Path(args.out)
    key = _bootstrap_env()
    judge_cfg = _resolve_judge_config(args.judge)
    judge_label = args.judge or judge_cfg.get("model", "default")

    print(f"=== batch_judge · judge={judge_label} · threshold={args.threshold} ===", flush=True)

    # 1. desensitize + hydrate
    print("[1/3] preparing workspace (desensitizing data) …", flush=True)
    ws_root, gold_questions, features = prepare_workspace(
        Path(args.data), Path(args.gold), out, args.reuse_workspace)
    # data preview fed to the OPEN judge when a whole set misses gold (Hit=✗).
    data_digest = build_data_digest(ws_root / "data")

    # 2. load candidates
    print("[2/3] loading candidates …", flush=True)
    loaded = load_candidates([Path(p) for p in args.candidates], args.strict)
    ok_loaded = [c for c in loaded if c.get("ok")]
    bad_loaded = [c for c in loaded if not c.get("ok")]
    for c in ok_loaded:
        print(f"  + {c['candidate_id']:<28} agent_id={c['agent_id']:<24} "
              f"questions={len(c['candidates'])}", flush=True)
    for c in bad_loaded:
        print(f"  ! {c['candidate_id']:<28} INVALID: {c['error']}", flush=True)
    if not ok_loaded:
        raise SystemExit("no valid candidates to score")

    results_root = out / "results"
    results_root.mkdir(parents=True, exist_ok=True)
    progress_path = out / "progress.json"
    progress = {
        "out": str(out), "judge": judge_label, "threshold": args.threshold,
        "started_at": time.time(), "total": len(ok_loaded), "completed": 0,
        "dry_run": args.dry_run, "candidates": [], "invalid": bad_loaded,
    }
    _write_progress(progress_path, progress)

    if args.dry_run:
        print(f"[3/3] dry-run: {len(ok_loaded)} candidates ready, judge NOT called.", flush=True)
        print(f"      workspace desensitized at {ws_root}", flush=True)
        progress["completed"] = 0
        progress["note"] = "dry-run; no judge calls made"
        _write_progress(progress_path, progress)
        return 0

    if key in _PLACEHOLDER_KEYS:
        print(f"  ⚠ NEWAPI_KEY is a placeholder ({key!r}); judge calls will fail. "
              f"Set a real key in .env or use --dry-run.", flush=True)

    # 3. score
    print(f"[3/3] scoring {len(ok_loaded)} candidates (concurrency={args.concurrency}) …", flush=True)
    judge = JudgeLLM(JudgeConfig(**judge_cfg))
    sem = asyncio.Semaphore(max(1, args.concurrency))
    rows: list[dict[str, Any]] = []
    batch_started = time.time()

    for i, cand in enumerate(ok_loaded, 1):
        if not args.force and _already_done(results_root, cand["candidate_id"]):
            print(f"  [{i}/{len(ok_loaded)}] {cand['candidate_id']:<28} skip (already done)", flush=True)
            continue
        try:
            row = await score_candidate(
                judge, sem, args.spacing, args.threshold, features,
                gold_questions, cand, results_root, data_digest)
            rows.append(row)
            print(f"  [{i}/{len(ok_loaded)}] {cand['candidate_id']:<28} "
                  f"avg={row.get('avg_composite', 0):.3f} best={row.get('composite_score') or 0:.3f} "
                  f"pass@1={row.get('pass_at_1_value', 0):.0f} pass@5={row.get('pass_at_5_value', 0):.2f} "
                  f"pass={row.get('pass_count',0)}/{row.get('candidate_count',0)} "
                  f"wall={row.get('judge_wall_time_s', 0):.0f}s", flush=True)
        except Exception as e:
            err = f"{type(e).__name__}: {e}"
            rows.append({"candidate_id": cand["candidate_id"], "agent_id": cand["agent_id"],
                         "ok": False, "error": err})
            print(f"  [{i}/{len(ok_loaded)}] {cand['candidate_id']:<28} FAILED: {err}", flush=True)

        progress["completed"] = i
        progress["candidates"] = [
            {k: r.get(k) for k in ("candidate_id", "agent_id", "ok", "avg_composite",
                                   "composite_score", "pass_at_1_value", "pass_at_5_value",
                                   "pass_count", "candidate_count", "matched_gold_id", "error")}
            for r in rows]
        progress["elapsed_s"] = time.time() - batch_started
        _write_progress(progress_path, progress)

    # 4. leaderboard + summary
    scored = [r for r in rows if r.get("ok")]
    scored.sort(key=lambda r: -(r.get("avg_composite") or -1))
    leaderboard = {
        "run_id": out.name, "judge_model": judge_label, "threshold": args.threshold,
        "results_root": str(results_root), "rows": scored + [r for r in rows if not r.get("ok")],
    }
    (out / "leaderboard.json").write_text(
        json.dumps(leaderboard, ensure_ascii=False, indent=2), encoding="utf-8")
    _write_summary(out, rows, judge_label)

    wall = time.time() - batch_started
    print(f"\n=== done · {len(scored)}/{len(rows)} scored · wall={wall:.0f}s ===", flush=True)
    print(f"  leaderboard → {out / 'leaderboard.json'}", flush=True)
    print(f"  summary     → {out / 'summary.md'}", flush=True)
    print(f"  progress    → {progress_path}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
