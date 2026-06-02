"""Async pipeline runner for the webapp's gold-rubric flow.

Differences from the original eval/run_pipeline.py:
  - workspace is hydrated from an uploaded data ZIP + INSTRUCTIONS template
    (the strict virus-specific INSTRUCTIONS.md is NOT used);
  - the judge scores against an uploaded gold-question JSON, not the
    static target_study/ rubric;
  - emits structured events for the SSE UI;
  - runs all selected agents in parallel via asyncio.gather.
"""

from __future__ import annotations

import asyncio
import json
import shutil
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, AsyncIterator

from eval.agents import REGISTRY as AGENT_REGISTRY
from eval.agents.base import RunResult
from eval.metrics import score_against_gold
from eval.metrics.judge_llm import JudgeConfig, JudgeLLM
from eval.utils import AgentOutput, Workspace


PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"


def _now() -> float:
    return time.time()


def _pass_at_k_stats(
    candidates: list[dict[str, Any]],
    candidate_results: list[Any],
) -> dict[str, Any]:
    """Compute Pass@1 / Pass@5 / first-hit-rank / primary-vs-secondary breakdown.

    Pass@1 = 1.0 (100%) if rank-1 candidate passes else 0.0.

    Pass@5 = position-weighted score, normalised to [0, 1]:
        numerator = Σ_{i=1..5} (1 + w_i) × passed_i
        denominator = 20  (max when all 5 pass)
        weights w = (5, 4, 3, 2, 1)  — earlier ranks count more
    Effective per-rank contributions are (6, 5, 4, 3, 2). Each pass contributes
    a constant +1 ("which one passed at all" floor) plus a rank-weighted bonus
    that rewards getting the strongest answer at rank 1.

    Examples:
        only rank 1 passes  → 6/20 = 0.30
        ranks 1+2 pass      → 11/20 = 0.55
        all 5 pass          → 20/20 = 1.00
        only rank 5 passes  → 2/20  = 0.10

    first_hit_rank = lowest rank whose candidate passed (None if no hit).
    primary_hit_count = passed-and-matched-primary; secondary_hit_count likewise.
    """
    pairs = sorted(zip(candidates, candidate_results), key=lambda p: p[0].get("rank", 999))
    pass_at_1 = bool(pairs and pairs[0][1].passed)
    first_hit_rank = next((c.get("rank") for c, r in pairs if r.passed), None)
    primary_hits = sum(
        1 for _, r in pairs if r.passed and r.matched_centrality == "primary"
    )
    secondary_hits = sum(
        1 for _, r in pairs if r.passed and r.matched_centrality == "secondary"
    )
    pass_count = sum(1 for _, r in pairs if r.passed)
    k = len(pairs)

    # Pass@5 weighted score: weights w=(5,4,3,2,1), per-rank contribution = 1 + w_i
    # When agents emit fewer than 5 candidates the metric is still well-defined
    # (missing ranks contribute 0); the schema validator enforces k=5 at the
    # contract layer so this branch is mostly belt-and-suspenders.
    weights = [5, 4, 3, 2, 1]
    weighted_num = 0
    for c, r in pairs:
        rank = c.get("rank")
        if rank is None or not (1 <= rank <= 5):
            continue
        if r.passed:
            weighted_num += 1 + weights[rank - 1]
    pass_at_5_value = weighted_num / 20.0  # 0.0 .. 1.0

    # Agent-level averages across the 5 candidates — the leaderboard headline
    # number when you want a single "how good is this agent overall" score.
    composites = [r.composite_score for _, r in pairs if r.composite_score is not None]
    raws = [r.composite_score_raw for _, r in pairs if r.composite_score_raw is not None]
    avg_composite = (sum(composites) / len(composites)) if composites else 0.0
    avg_raw = (sum(raws) / len(raws)) if raws else 0.0

    return {
        "candidate_count": k,
        "pass_at_1": pass_at_1,
        "pass_at_1_value": 1.0 if pass_at_1 else 0.0,
        "pass_at_5": pass_count > 0,
        "pass_at_5_value": pass_at_5_value,
        # legacy aliases — kept so older clients / CSVs don't break
        "pass_at_k": pass_count > 0,
        "pass_at_k_value": pass_at_5_value,
        "pass_count": pass_count,
        "first_hit_rank": first_hit_rank,
        "primary_hit_count": primary_hits,
        "secondary_hit_count": secondary_hits,
        "avg_composite": avg_composite,
        "avg_raw": avg_raw,
    }


@dataclass
class RunEvent:
    ts: float
    kind: str
    payload: dict[str, Any] = field(default_factory=dict)

    def to_json(self) -> dict[str, Any]:
        return {"ts": self.ts, "kind": self.kind, **self.payload}


class EventBus:
    def __init__(self) -> None:
        self._events: list[RunEvent] = []
        self._waiters: list[asyncio.Event] = []
        self._closed = False

    def append(self, kind: str, **payload: Any) -> RunEvent:
        ev = RunEvent(ts=_now(), kind=kind, payload=payload)
        self._events.append(ev)
        for w in self._waiters:
            w.set()
        return ev

    def close(self) -> None:
        self._closed = True
        for w in self._waiters:
            w.set()

    @property
    def events(self) -> list[RunEvent]:
        return list(self._events)

    async def subscribe(self) -> AsyncIterator[RunEvent]:
        idx = 0
        while True:
            while idx < len(self._events):
                yield self._events[idx]
                idx += 1
            if self._closed:
                return
            wait = asyncio.Event()
            self._waiters.append(wait)
            try:
                await wait.wait()
            finally:
                self._waiters.remove(wait)


@dataclass
class RunSpec:
    run_id: str
    workspace_root: Path        # hydrated workspace (uploaded data + generic INSTRUCTIONS)
    gold_path: Path             # normalised gold JSON
    available_features: list[str]
    agents: list[str]
    judge_config: dict[str, Any]
    threshold: float
    results_root: Path
    sandbox_root: Path
    # Judge-only mode: when set, agents=[] and the user-supplied AgentOutput
    # JSON is judged directly without invoking any agent. Each candidate in
    # `judge_only_candidate.questions` is scored (Pass@k still applies).
    judge_only_candidate: dict[str, Any] | None = None

    @property
    def events_path(self) -> Path:
        return self.results_root.parent / "events.jsonl"


def hydrate_workspace(
    data_dir: Path,
    gold_normalised: Path,
    dst: Path,
) -> tuple[Path, list[str]]:
    """Build a generic workspace for any uploaded data archive.

    Layout:
      dst/INSTRUCTIONS.md         ← templates/INSTRUCTIONS_generic.md
      dst/info.json               ← schema-less data manifest (sizes, ext hist)
      dst/data/                   ← uploaded data
      dst/gold/gold_questions.json  ← judge-only normalised gold

    Returns (workspace_root, available_features). The features list is what
    the judge uses for the data_grounding dimension.
    """
    dst = Path(dst).resolve()
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)

    # 1. INSTRUCTIONS.md
    shutil.copy2(TEMPLATES_DIR / "INSTRUCTIONS_generic.md", dst / "INSTRUCTIONS.md")

    # 2. data/ (copy uploaded contents)
    data_dst = dst / "data"
    shutil.copytree(data_dir, data_dst)

    # 3. info.json (data manifest)
    files: list[dict[str, Any]] = []
    feats: list[str] = []
    for p in sorted(data_dst.rglob("*")):
        if p.is_file():
            rel = str(p.relative_to(data_dst))
            files.append({"path": rel, "size_bytes": p.stat().st_size})
            feats.append(rel)
    manifest = {
        "workspace_kind": "user_uploaded",
        "data_root": "data/",
        "files": files,
        "agent_output_contract": {
            "report_path": "report/report.md",
            "scientific_question_output_path": "agent_questions.json",
        },
        "agent_output_schema": {
            "type": "object",
            "required": ["agent_id", "questions"],
            "properties": {
                "agent_id": {"type": "string"},
                "questions": {
                    "type": "array", "minItems": 1, "maxItems": 5,
                    "items": {
                        "type": "object",
                        "required": ["rank", "question", "rationale"],
                        "properties": {
                            "rank": {"type": "integer"},
                            "question": {"type": "string"},
                            "rationale": {"type": "string"},
                            "data_support": {"type": "array", "items": {"type": "string"}},
                            "expected_test": {"type": "string"},
                            "scope_keywords": {"type": "array", "items": {"type": "string"}},
                        },
                    },
                },
            },
        },
    }
    (dst / "info.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2))

    # 4. minimal checklist.json so AgentRunner.materialize_agent_view doesn't choke
    (dst / "checklist.json").write_text(json.dumps([], ensure_ascii=False))

    # 5. gold/  — judge-only mirror (NOT copied to agent sandbox by Workspace)
    gold_dir = dst / "gold"
    gold_dir.mkdir()
    shutil.copy2(gold_normalised, gold_dir / "gold_questions.json")

    return dst, feats


# patch the Workspace.materialize_agent_view to skip gold/ — already does so
# because AGENT_VISIBLE in webapp's hydrated workspace is the same set the
# library Workspace uses (INSTRUCTIONS.md, checklist.json, info.json,
# data/raw_data). We need the agent to see `data/` not `data/raw_data/`,
# so we use a slim per-webapp Workspace.

class _WebWorkspace(Workspace):
    """Same Workspace, but only copies INSTRUCTIONS / info / data/ to sandbox."""

    AGENT_VISIBLE = ("INSTRUCTIONS.md", "info.json", "checklist.json", "data")

    def materialize_agent_view(self, dst: Path) -> Path:  # type: ignore[override]
        dst = Path(dst).resolve()
        if dst.exists():
            shutil.rmtree(dst)
        dst.mkdir(parents=True)
        for rel in self.AGENT_VISIBLE:
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

    def collect_agent_outputs(self, sandbox: Path) -> tuple[Path, Path]:  # type: ignore[override]
        sandbox = Path(sandbox)
        return sandbox / "agent_questions.json", sandbox / "report" / "report.md"


class PipelineRunner:
    def __init__(self, spec: RunSpec, bus: EventBus) -> None:
        self.spec = spec
        self.bus = bus
        self._final: dict[str, Any] | None = None

    @property
    def final(self) -> dict[str, Any] | None:
        return self._final

    async def run(self) -> dict[str, Any]:
        spec = self.spec
        spec.results_root.mkdir(parents=True, exist_ok=True)
        spec.sandbox_root.mkdir(parents=True, exist_ok=True)
        ws = _WebWorkspace.from_root(spec.workspace_root)

        gold_questions = json.loads(spec.gold_path.read_text())["gold_scientific_questions"]
        judge = JudgeLLM(JudgeConfig(**spec.judge_config))

        self._emit(
            "run_started",
            run_id=spec.run_id,
            agents=spec.agents,
            workspace=str(spec.workspace_root),
            gold_count=len(gold_questions),
            judge_model=spec.judge_config.get("model"),
            judge_provider=spec.judge_config.get("provider"),
            judge_only=spec.judge_only_candidate is not None,
        )

        # Judge-only mode: run a single synthetic "agent" that uses the
        # user-supplied candidate JSON instead of invoking a model.
        if spec.judge_only_candidate is not None:
            synthetic_id = spec.judge_only_candidate.get("agent_id") or "user_uploaded_candidate"
            results = [
                await self._run_judge_only(spec, synthetic_id, gold_questions, judge)
            ]
            agent_ids_for_zip = [synthetic_id]
        else:
            async def _drive(agent_id: str) -> dict[str, Any]:
                return await self._run_one_agent(spec, ws, agent_id, gold_questions, judge)
            results = await asyncio.gather(*(_drive(a) for a in spec.agents), return_exceptions=True)
            agent_ids_for_zip = spec.agents

        rows: list[dict[str, Any]] = []
        for agent_id, res in zip(agent_ids_for_zip, results):
            if isinstance(res, Exception):
                rows.append({"agent_id": agent_id, "ok": False, "error": f"{type(res).__name__}: {res}"})
            else:
                rows.append(res)

        rows.sort(key=lambda r: -(r.get("composite_score") or -1))
        leaderboard = {
            "run_id": spec.run_id,
            "judge_model": spec.judge_config.get("model"),
            "judge_provider": spec.judge_config.get("provider"),
            "results_root": str(spec.results_root),
            "rows": rows,
        }
        (spec.results_root / "leaderboard.json").write_text(
            json.dumps(leaderboard, ensure_ascii=False, indent=2)
        )
        self._emit("run_finished", run_id=spec.run_id, rows=rows)
        self.bus.close()
        spec.events_path.write_text(
            "\n".join(json.dumps(e.to_json(), ensure_ascii=False) for e in self.bus.events)
        )
        self._final = leaderboard
        return leaderboard

    async def _run_one_agent(
        self,
        spec: RunSpec,
        ws: _WebWorkspace,
        agent_id: str,
        gold_questions: list[dict[str, Any]],
        judge: JudgeLLM,
    ) -> dict[str, Any]:
        cls = AGENT_REGISTRY[agent_id]
        runner = cls(workspace=ws, sandbox_root=spec.sandbox_root)

        # If the agent supports streaming chunks, bridge them into the event
        # bus so the UI shows the model's analysis live. Cross-thread safe via
        # call_soon_threadsafe (the agent runs in asyncio.to_thread).
        loop = asyncio.get_running_loop()
        bus = self.bus
        if hasattr(runner, "set_chunk_callback"):
            def _chunk_cb(text: str) -> None:
                # call_soon_threadsafe only forwards positional args; capture
                # kwargs via a closure so they survive the hop.
                loop.call_soon_threadsafe(
                    lambda t=text: bus.append("agent_streaming", agent_id=agent_id, delta=t)
                )
            runner.set_chunk_callback(_chunk_cb)

        agent_started = _now()
        self._emit("agent_started", agent_id=agent_id, started_at=agent_started)

        # Pre-create the result dir so a failed run still has a destination for
        # _debug/ artefacts.
        target = spec.results_root / agent_id / time.strftime("%Y%m%dT%H%M%S")
        target.mkdir(parents=True, exist_ok=True)

        # ---- Retry loop -----------------------------------------------
        # Some agents flap on transient gateway errors (intern-s1-mini hitting
        # a 503, gemini-3.1-pro tripping a content classifier mid-stream, etc).
        # Give every agent up to MAX_ATTEMPTS independent shots before we
        # surface `agent_failed`. Each attempt uses a fresh sandbox timestamp
        # (the agent's own run() picks `time.strftime` per invocation) so the
        # retry doesn't collide with the previous attempt's debug artefacts.
        MAX_ATTEMPTS = 5
        attempts: list[dict[str, Any]] = []
        run_result: RunResult | None = None
        last_exc: Exception | None = None

        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                run_result = await asyncio.to_thread(runner.run)
                attempts.append({"attempt": attempt, "ok": True})
                if attempt > 1:
                    self._emit(
                        "agent_retry_succeeded",
                        agent_id=agent_id,
                        attempt=attempt,
                        max_attempts=MAX_ATTEMPTS,
                    )
                last_exc = None
                break
            except Exception as e:
                err = f"{type(e).__name__}: {e}"
                attempts.append({"attempt": attempt, "ok": False, "error": err})
                last_exc = e
                if attempt < MAX_ATTEMPTS:
                    self._emit(
                        "agent_retry",
                        agent_id=agent_id,
                        attempt=attempt,
                        max_attempts=MAX_ATTEMPTS,
                        error=err,
                    )
                    await asyncio.sleep(2)  # brief backoff between retries
                    continue
                # final failure — salvage debug + sandbox state for post-mortem.
                try:
                    sb_root = spec.sandbox_root / agent_id
                    sandboxes = sorted(sb_root.glob("*"), key=lambda p: p.stat().st_mtime)
                    if sandboxes:
                        sb = sandboxes[-1]
                        debug_src = sb / "_debug"
                        if debug_src.exists():
                            shutil.copytree(debug_src, target / "_debug", dirs_exist_ok=True)
                        (target / "_failure.txt").write_text(
                            f"agent={agent_id}\n"
                            f"attempts={MAX_ATTEMPTS} (all failed)\n"
                            f"final_error={err}\n"
                            f"sandbox={sb}\n\n"
                            f"per_attempt:\n" +
                            "\n".join(f"  #{a['attempt']}: {'ok' if a['ok'] else a.get('error','?')}" for a in attempts)
                        )
                except Exception:
                    pass
                self._emit(
                    "agent_failed",
                    agent_id=agent_id,
                    error=err,
                    wall_time_s=_now() - agent_started,
                    debug_dir=str(target / "_debug"),
                    attempts=attempts,
                )
                raise

        # persist agent outputs into results dir (target was pre-created above)
        shutil.copy2(run_result.sandbox / "agent_questions.json", target / "agent_questions.json")
        report_src = run_result.sandbox / "report" / "report.md"
        if report_src.exists():
            (target / "report").mkdir(exist_ok=True)
            shutil.copy2(report_src, target / "report" / "report.md")
        # always save _debug/ for postmortem (success or fail)
        debug_src = run_result.sandbox / "_debug"
        if debug_src.exists():
            shutil.copytree(debug_src, target / "_debug", dirs_exist_ok=True)
        (target / "_logs.txt").write_text(run_result.raw_logs)

        agent_finished = _now()
        agent_payload = json.loads((target / "agent_questions.json").read_text())
        self._emit(
            "agent_finished",
            agent_id=agent_id,
            run_dir=str(target),
            wall_time_s=agent_finished - agent_started,
            agent_questions=agent_payload,
            attempts=attempts,
        )

        # ---- judge (Pass@k: score each candidate, pick best) -------------
        judge_started = _now()
        self._emit("judge_started", agent_id=agent_id, run_dir=str(target))

        agent_output = AgentOutput.model_validate(agent_payload)
        candidates = agent_output.to_judge_payloads()

        candidate_results = await asyncio.gather(*[
            asyncio.to_thread(
                score_against_gold,
                judge,
                c,
                gold_questions,
                spec.available_features,
                spec.threshold,
            )
            for c in candidates
        ])
        # pick the candidate with the highest composite_score for the leaderboard
        # (treat None as -1 so failed-to-match candidates lose to any successful one)
        best_idx = max(
            range(len(candidate_results)),
            key=lambda i: (candidate_results[i].composite_score if candidate_results[i].composite_score is not None else -1),
        )
        gold_result = candidate_results[best_idx]
        candidate = candidates[best_idx]

        judge_finished = _now()
        (target / "judge_scores.json").write_text(
            json.dumps(gold_result.to_json(), ensure_ascii=False, indent=2)
        )
        # also persist all per-candidate scores for the UI Pass@k panel
        all_scores = [
            {
                "rank": c["rank"],
                "question": c["question"],
                "composite_score": r.composite_score,
                "composite_score_raw": r.composite_score_raw,
                "passed": r.passed,
                "matched_gold_id": r.matched_gold_id,
                "matched_gold_question": r.matched_gold_question,
                "matched_centrality": r.matched_centrality,
                "scores": r.scores,
                # per-question reasoning — needed so the UI can render
                # 4-dim reasoning + variants for EVERY candidate, not just
                # the winner.
                "per_dimension_reasoning": r.per_dimension_reasoning,
                "closest_acceptable_variant": r.closest_acceptable_variant,
                "closest_unacceptable_variant": r.closest_unacceptable_variant,
                "rationale": r.rationale,
                "covered_required_elements": r.covered_required_elements,
                "missing_required_elements": r.missing_required_elements,
            }
            for c, r in zip(candidates, candidate_results)
        ]
        (target / "judge_scores_all_candidates.json").write_text(
            json.dumps(all_scores, ensure_ascii=False, indent=2)
        )

        pk_stats = _pass_at_k_stats(candidates, candidate_results)
        row = {
            "agent_id": agent_id,
            "ok": True,
            "run_dir": str(target),
            "agent_wall_time_s": agent_finished - agent_started,
            "judge_wall_time_s": judge_finished - judge_started,
            "composite_score": gold_result.composite_score,
            "composite_score_raw": gold_result.composite_score_raw,
            "passed": gold_result.passed,
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
            # ---- Pass@k stats ----
            "best_candidate_rank": candidate.get("rank"),
            "all_candidate_scores": all_scores,
            "attempts": attempts,  # retry trail (3 max attempts per agent)
            **pk_stats,  # candidate_count, pass_at_1, pass_at_k, pass_count, first_hit_rank, primary_hit_count, secondary_hit_count
        }
        self._emit("judge_finished", **row)
        return row

    def _emit(self, kind: str, **payload: Any) -> None:
        self.bus.append(kind, **payload)

    # ------------------------------------------------------------------
    # Judge-only branch: skip agent.run(), score the user-uploaded JSON.
    # ------------------------------------------------------------------
    async def _run_judge_only(
        self,
        spec: RunSpec,
        synthetic_id: str,
        gold_questions: list[dict[str, Any]],
        judge: JudgeLLM,
    ) -> dict[str, Any]:
        candidate_payload = spec.judge_only_candidate or {}

        target = spec.results_root / synthetic_id / time.strftime("%Y%m%dT%H%M%S")
        target.mkdir(parents=True, exist_ok=True)
        # persist the user-supplied candidate as our "agent output"
        (target / "agent_questions.json").write_text(
            json.dumps(candidate_payload, ensure_ascii=False, indent=2)
        )

        agent_started = _now()
        self._emit("agent_started", agent_id=synthetic_id, started_at=agent_started, judge_only=True)
        agent_finished = _now()
        self._emit(
            "agent_finished",
            agent_id=synthetic_id,
            run_dir=str(target),
            wall_time_s=agent_finished - agent_started,
            agent_questions=candidate_payload,
            judge_only=True,
        )

        # ---- judge (Pass@k over user candidates) -----------------------
        judge_started = _now()
        self._emit("judge_started", agent_id=synthetic_id, run_dir=str(target))

        agent_output = AgentOutput.model_validate(candidate_payload)
        candidates = agent_output.to_judge_payloads()

        candidate_results = await asyncio.gather(*[
            asyncio.to_thread(
                score_against_gold, judge, c, gold_questions,
                spec.available_features, spec.threshold,
            )
            for c in candidates
        ])
        best_idx = max(
            range(len(candidate_results)),
            key=lambda i: (candidate_results[i].composite_score if candidate_results[i].composite_score is not None else -1),
        )
        gold_result = candidate_results[best_idx]
        candidate = candidates[best_idx]

        judge_finished = _now()
        (target / "judge_scores.json").write_text(
            json.dumps(gold_result.to_json(), ensure_ascii=False, indent=2)
        )
        all_scores = [
            {
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
            }
            for c, r in zip(candidates, candidate_results)
        ]
        (target / "judge_scores_all_candidates.json").write_text(
            json.dumps(all_scores, ensure_ascii=False, indent=2)
        )

        pk_stats = _pass_at_k_stats(candidates, candidate_results)
        row = {
            "agent_id": synthetic_id,
            "ok": True,
            "judge_only": True,
            "run_dir": str(target),
            "agent_wall_time_s": 0.0,
            "judge_wall_time_s": judge_finished - judge_started,
            "composite_score": gold_result.composite_score,
            "composite_score_raw": gold_result.composite_score_raw,
            "passed": gold_result.passed,
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
            **pk_stats,  # candidate_count, pass_at_1, pass_at_k, pass_count, first_hit_rank, primary_hit_count, secondary_hit_count
        }
        self._emit("judge_finished", **row)
        return row
