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
import bz2
import gzip
import json
import shutil
import tarfile
import time
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, AsyncIterator

from eval.agents import REGISTRY as AGENT_REGISTRY
from eval.agents.base import RunResult
from eval.metrics import score_against_gold, score_open_question
from eval.metrics.judge_llm import JudgeConfig, JudgeLLM
from eval.utils import AgentOutput, Workspace


PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"


def _now() -> float:
    return time.time()


def _prune_sandbox_data(sandbox: Path) -> None:
    """Delete the bulky `data/` copy from a finished sandbox.

    Every agent run materialises a private copy of the uploaded `data/` tree
    into its sandbox so the model can read it. Once the agent has produced its
    outputs (or finally failed) that copy is dead weight — it bloats
    `webapp_runs/.../sandboxes/<agent>/<ts>/data/` with a full duplicate of the
    upload per run. We keep the agent's outputs and `_debug/` artefacts for
    post-mortem but drop `data/`. Best-effort: never let cleanup failures break
    a run.
    """
    try:
        data_dir = Path(sandbox) / "data"
        if data_dir.exists():
            shutil.rmtree(data_dir, ignore_errors=True)
    except Exception:
        pass


def _desensitize_data(src_root: Path, dst_data: Path) -> dict[str, str]:
    """Copy uploaded files into `dst_data` under anonymised sequential names.

    The tree is flattened and every file is renamed to `<N>.<ext>` (1.csv,
    2.json, 3.tsv, …) in sorted-path order, preserving only the extension so
    the agent still knows each file's format. Files with no extension become
    `<N>.dat`. Directory names — which can also leak intent — are dropped.

    Nested archives are expanded recursively BEFORE flattening: a `.zip` /
    `.tar(.gz/.bz2)` in the upload would otherwise let an agent unzip it and
    read the original, intent-leaking filenames inside (e.g.
    `43059586_RdRp_motif_collection.xlsx`). We extract every archive in place,
    delete the archive itself, and anonymise the extracted members too. The
    original relative path (including the `archive!member` provenance) is kept
    in the returned map so the judge can still de-anonymise.

    Returns {anonymised_name: original_relative_path} so an operator or the
    judge can de-anonymise later via the workspace's filename_map.json.
    """
    src_root = Path(src_root)
    dst_data = Path(dst_data)
    dst_data.mkdir(parents=True, exist_ok=True)

    # Stage 1: copy the upload into a scratch tree we can mutate, then expand
    # nested archives in place (recursively) so their members are anonymised
    # like any other file.
    scratch = dst_data.parent / "_desensitize_scratch"
    if scratch.exists():
        shutil.rmtree(scratch, ignore_errors=True)
    shutil.copytree(src_root, scratch)
    _expand_archives_in_place(scratch)

    files = sorted(
        p for p in scratch.rglob("*")
        if p.is_file() and "__MACOSX" not in p.parts
    )
    mapping: dict[str, str] = {}
    for i, p in enumerate(files, start=1):
        ext = p.suffix.lower()
        new_name = f"{i}{ext}" if ext else f"{i}.dat"
        shutil.copy2(p, dst_data / new_name)
        mapping[new_name] = str(p.relative_to(scratch)).replace("\\", "/")

    shutil.rmtree(scratch, ignore_errors=True)
    return mapping


# Archive extensions we recursively unpack during desensitization.
_ARCHIVE_SUFFIXES = (".zip", ".tar", ".tar.gz", ".tgz", ".tar.bz2", ".tbz2", ".gz", ".bz2")


def _expand_archives_in_place(root: Path, _depth: int = 0) -> None:
    """Extract every nested archive under `root`, deleting the archive after.

    Recurses so an archive-inside-an-archive is also expanded. Bounded depth
    guards against zip-bomb-style infinite nesting. Extraction is path-safe:
    members with absolute paths or `..` traversal are skipped. Archives that
    fail to open are left as-is (still anonymised as opaque blobs upstream).
    """
    if _depth > 8:
        return
    found_archive = False
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        name = p.name.lower()
        if not any(name.endswith(s) for s in _ARCHIVE_SUFFIXES):
            continue
        out_dir = p.parent / (p.name + "__extracted")
        try:
            if name.endswith(".zip"):
                with zipfile.ZipFile(p) as zf:
                    if any(n.startswith("/") or ".." in Path(n).parts for n in zf.namelist()):
                        continue  # unsafe archive — leave it as an opaque blob
                    out_dir.mkdir(parents=True, exist_ok=True)
                    zf.extractall(out_dir)
            elif name.endswith((".tar", ".tar.gz", ".tgz", ".tar.bz2", ".tbz2")):
                with tarfile.open(p) as tf:
                    members = tf.getmembers()
                    if any(m.name.startswith("/") or ".." in Path(m.name).parts for m in members):
                        continue
                    out_dir.mkdir(parents=True, exist_ok=True)
                    tf.extractall(out_dir)
            elif name.endswith((".gz", ".bz2")):
                # single-stream compressed file → decompress to the inner name
                opener = gzip.open if name.endswith(".gz") else bz2.open
                inner = out_dir / p.stem  # strip the .gz/.bz2 suffix
                out_dir.mkdir(parents=True, exist_ok=True)
                with opener(p, "rb") as src, open(inner, "wb") as dst:
                    shutil.copyfileobj(src, dst)
            else:
                continue
        except Exception:
            # corrupt / unsupported archive: keep the original blob, skip expand
            shutil.rmtree(out_dir, ignore_errors=True)
            continue
        # archive expanded successfully — drop the archive itself
        found_archive = True
        try:
            p.unlink()
        except Exception:
            pass
    # Newly-extracted dirs may themselves contain archives — recurse.
    if found_archive:
        _expand_archives_in_place(root, _depth + 1)


def _pass_at_k_stats(
    candidates: list[dict[str, Any]],
    candidate_results: list[Any],
) -> dict[str, Any]:
    """Compute Pass@1 / Pass@5 / first-hit-rank / primary-vs-secondary breakdown.

    Pass@1 / Pass@5 / pass_count consider ALL rubric types (closed + open).

    Hit only counts closed-rubric passes: a question whose final result has
    rubric_kind="open" does NOT count toward Hit, even if it passed the open
    threshold. Hit strictly measures alignment with gold questions.

    first_hit_rank = lowest rank whose candidate passed via closed rubric.
    primary_hit_count = closed-passed and matched primary gold.
    """
    pairs = sorted(zip(candidates, candidate_results), key=lambda p: p[0].get("rank", 999))

    # pass_count / pass_at_1 consider ALL rubric types (closed + open)
    pass_at_1 = bool(pairs and pairs[0][1].passed)
    pass_count = sum(1 for _, r in pairs if r.passed)

    def _is_closed_pass(r: Any) -> bool:
        """True if this result passed via the closed rubric (actually hit gold)."""
        return r.passed and getattr(r, "rubric_kind", "closed") != "open"

    closed_hit_count = sum(1 for _, r in pairs if _is_closed_pass(r))
    first_hit_rank = next(
        (c.get("rank") for c, r in pairs if _is_closed_pass(r)),
        None,
    )
    primary_hits = sum(
        1 for _, r in pairs
        if _is_closed_pass(r) and r.matched_centrality == "primary"
    )
    secondary_hits = sum(
        1 for _, r in pairs
        if _is_closed_pass(r) and r.matched_centrality == "secondary"
    )
    k = len(pairs)

    pass_at_5_value = min(pass_count, 5) / 5.0  # 0.0 .. 1.0

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
        # hit = at least ONE closed-rubric (gold-matched) pass among 5?
        "hit": closed_hit_count >= 1,
        "hit_value": 1.0 if closed_hit_count >= 1 else 0.0,
        "pass_at_k": pass_count > 0,
        "pass_at_k_value": pass_at_5_value,
        "pass_count": pass_count,
        "first_hit_rank": first_hit_rank,
        "primary_hit_count": primary_hits,
        "secondary_hit_count": secondary_hits,
        "avg_composite": avg_composite,
        "avg_raw": avg_raw,
    }


def build_data_digest(data_dir: Path, max_files: int = 30, max_bytes: int = 800) -> str:
    """Compact, bounded preview of the desensitized data — fed to the OPEN judge.

    The open rubric's `data_match` dimension needs to know what the data
    CONTAINS (columns, fields, structure) to judge whether it supports a
    question. Only filenames are desensitized — content is the same the agent
    saw — so previewing content here leaks nothing the agent didn't already get.

    For each anonymised file we emit one line: `<name> (<ext>, <size>B): <preview>`
    where preview is JSON top-level keys, or the first few non-empty text lines.
    Binary / unreadable files get a `(binary)` note. Everything is bounded so the
    digest can't blow up the judge prompt.
    """
    data_dir = Path(data_dir)
    if not data_dir.is_dir():
        return ""
    files = sorted(p for p in data_dir.rglob("*") if p.is_file())
    lines: list[str] = []
    for p in files[:max_files]:
        rel = p.relative_to(data_dir).as_posix()
        try:
            size = p.stat().st_size
        except OSError:
            size = 0
        lines.append(f"- {rel} ({p.suffix.lower() or 'no-ext'}, {size}B): "
                     f"{_preview_file(p, p.suffix.lower(), max_bytes)}")
    if len(files) > max_files:
        lines.append(f"... (+{len(files) - max_files} more files omitted)")
    return "\n".join(lines)


def _preview_file(p: Path, ext: str, max_bytes: int) -> str:
    """One-line content preview of a single file (bounded, robust)."""
    try:
        raw = p.read_bytes()[: max(max_bytes * 4, 20000)]
    except Exception:
        return "(unreadable)"
    if b"\x00" in raw[:1024]:
        return "(binary, no preview)"
    txt = raw.decode("utf-8", errors="replace")
    if ext == ".json":
        try:
            obj = json.loads(txt)
            if isinstance(obj, dict):
                return "JSON object, keys: " + ", ".join(map(str, list(obj.keys())[:12]))
            if isinstance(obj, list):
                head = obj[0] if obj else None
                if isinstance(head, dict):
                    return (f"JSON array (len {len(obj)}); item keys: "
                            + ", ".join(map(str, list(head.keys())[:12])))
                return f"JSON array (len {len(obj)})"
            return f"JSON {type(obj).__name__}"
        except Exception:
            pass  # truncated / invalid JSON → fall back to text snippet
    snippet = " | ".join(ln.strip() for ln in txt.splitlines() if ln.strip())[:max_bytes]
    return snippet or "(empty)"


async def rescore_open_if_missed(
    judge: Any,
    candidates: list[dict[str, Any]],
    closed_results: list[Any],
    data_digest: str,
    threshold: float,
) -> tuple[list[Any], str]:
    """Per-question rubric routing.

    Each candidate is individually evaluated:
      - closed passed (composite >= threshold) → keep the closed result (hit gold)
      - closed failed  → additionally score with OPEN rubric, take the HIGHER of
        the two scores. The result is tagged rubric_kind="open" if the open score
        wins, otherwise stays "closed".

    Returns (final_results, rubric_kind) where rubric_kind is:
      "closed" if ALL questions passed closed,
      "open"   if ALL questions used open scores,
      "mixed"  if some closed and some open.
    """
    final: list[Any] = list(closed_results)
    failed_indices: list[int] = [
        i for i, r in enumerate(closed_results) if not getattr(r, "passed", False)
    ]

    if not failed_indices:
        return final, "closed"

    # score the failed ones with open rubric
    open_results = await asyncio.gather(*[
        asyncio.to_thread(score_open_question, judge, candidates[i], data_digest, threshold)
        for i in failed_indices
    ])

    open_used = 0
    for idx, open_r in zip(failed_indices, open_results):
        closed_comp = getattr(closed_results[idx], "composite_score", 0) or 0
        open_comp = getattr(open_r, "composite_score", 0) or 0
        if open_comp > closed_comp:
            final[idx] = open_r
            open_used += 1

    if open_used == 0:
        return final, "closed"
    if open_used == len(closed_results):
        return final, "open"
    return final, "mixed"


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
      dst/info.json               ← data manifest (sizes, ext hist) — NOT copied to agent sandbox
      dst/data/                   ← uploaded data, DESENSITIZED (renamed 1.ext…)
      dst/filename_map.json       ← {anonymised → original} (judge-only, not in sandbox)
      dst/gold/gold_questions.json  ← judge-only normalised gold

    Returns (workspace_root, available_features). The features list is what
    the judge uses for the data_grounding dimension — it holds the anonymised
    names so an agent can't earn grounding by quoting an evocative filename.
    """
    dst = Path(dst).resolve()
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)

    # 1. INSTRUCTIONS.md
    shutil.copy2(TEMPLATES_DIR / "INSTRUCTIONS_generic.md", dst / "INSTRUCTIONS.md")

    # 2. data/ — copy uploaded contents under anonymised, format-only names.
    #    Evocative filenames (e.g. 43059586_RdRp_motif_collection.xlsx) leak the
    #    answer: an agent can score data_grounding just by quoting them. We
    #    flatten the tree and rename every file to <N>.<ext> (1.csv, 2.json, …),
    #    keeping only the extension so the format is still discoverable.
    data_dst = dst / "data"
    filename_map = _desensitize_data(Path(data_dir), data_dst)
    (dst / "filename_map.json").write_text(
        json.dumps(filename_map, ensure_ascii=False, indent=2)
    )

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
                        "required": ["rank", "question"],
                        "properties": {
                            "rank": {"type": "integer"},
                            "question": {"type": "string"},
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
# library Workspace uses (INSTRUCTIONS.md, checklist.json,
# data/raw_data). We need the agent to see `data/` not `data/raw_data/`,
# so we use a slim per-webapp Workspace.

class _WebWorkspace(Workspace):
    """Same Workspace, but only copies INSTRUCTIONS / data/ to sandbox."""

    AGENT_VISIBLE = ("INSTRUCTIONS.md", "checklist.json", "data")

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
                    # drop bulky data/ copies from every attempt's sandbox
                    for sb in sandboxes:
                        _prune_sandbox_data(sb)
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
        # drop the bulky per-run data/ copy now that outputs are salvaged
        _prune_sandbox_data(run_result.sandbox)

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
        # per-question rubric routing: each question that missed gold
        # (gold_matched=False) gets re-scored with the OPEN rubric.
        data_digest = build_data_digest(Path(spec.workspace_root) / "data")
        candidate_results, rubric_kind = await rescore_open_if_missed(
            judge, candidates, candidate_results, data_digest, spec.threshold)
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
                "gold_matched": getattr(r, "gold_matched", True),
                "is_open": getattr(r, "is_open", False),
                "rubric_kind": getattr(r, "rubric_kind", "closed"),
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
            "gold_matched": getattr(gold_result, "gold_matched", True),
            "is_open": getattr(gold_result, "is_open", False),
            "rubric_kind": rubric_kind,
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
        # per-question rubric routing: missed gold → open rubric.
        data_digest = build_data_digest(Path(spec.workspace_root) / "data")
        candidate_results, rubric_kind = await rescore_open_if_missed(
            judge, candidates, candidate_results, data_digest, spec.threshold)
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
                "gold_matched": getattr(r, "gold_matched", True),
                "is_open": getattr(r, "is_open", False),
                "rubric_kind": getattr(r, "rubric_kind", "closed"),
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
            "gold_matched": getattr(gold_result, "gold_matched", True),
            "is_open": getattr(gold_result, "is_open", False),
            "rubric_kind": rubric_kind,
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
