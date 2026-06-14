"""FastAPI server for the rubric-judge webapp.

Endpoints
---------
GET  /                                   SPA index
GET  /static/*                           static assets
POST /api/uploads                        multipart: file=<data.zip>, gold=<gold.json>, question_set_id=<str?>
GET  /api/uploads                        list known uploads
GET  /api/uploads/{id}                   upload metadata + validation report
GET  /api/agents                         registered agents the user can pick
GET  /api/judge_info                     judge LLM model + provider currently in use
POST /api/runs                           {upload_id, agents: [...]} → {run_id}
GET  /api/runs                           list of all runs (annotated with question_set_id)
GET  /api/runs/{up_id}/{run_id}          current status / final results
GET  /api/runs/{up_id}/{run_id}/events   SSE stream
GET  /api/question_sets                  list of question sets, each with all uploads + runs underneath
"""

from __future__ import annotations

import asyncio
import json
import os
import re
import secrets
import shutil
import time
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from eval.agents import REGISTRY as AGENT_REGISTRY, AGENT_META
from eval.metrics.gold_rubric_metric import rubric_specification
from eval.metrics.open_rubric_metric import open_rubric_specification
from webapp.gold_validator import validate_gold
from webapp.pipeline_runner import EventBus, PipelineRunner, RunSpec, hydrate_workspace
from webapp.validator import DataValidationError, validate_data_zip


PROJECT_ROOT = Path(__file__).resolve().parent.parent
WEBAPP_DIR = Path(__file__).resolve().parent
STATIC_DIR = WEBAPP_DIR / "static"
RUNS_ROOT = PROJECT_ROOT / "webapp_runs"
RUNS_ROOT.mkdir(parents=True, exist_ok=True)
JUDGE_CONFIG_PATH = PROJECT_ROOT / "eval" / "config.yaml"


def _bootstrap_env() -> None:
    env_path = PROJECT_ROOT / ".env"
    if env_path.exists():
        load_dotenv(env_path, override=False)
    key = os.environ.get("NEWAPI_KEY", "")
    if key and key != "sk-REPLACE_ME":
        os.environ.setdefault("OPENAI_API_KEY", key)
        os.environ.setdefault("ANTHROPIC_AUTH_TOKEN", key)
        os.environ.setdefault("ANTHROPIC_API_KEY", key)


_bootstrap_env()
JUDGE_CFG = yaml.safe_load(JUDGE_CONFIG_PATH.read_text())

app = FastAPI(title="Virus-Question-Judge", version="0.3.0")
_runs: dict[tuple[str, str], dict[str, Any]] = {}


# ----- helpers -----------------------------------------------------------

_QSET_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")


def _new_id(prefix: str) -> str:
    return f"{prefix}_{int(time.time())}_{secrets.token_hex(3)}"


def _normalise_qset_id(raw: str | None) -> str:
    """Validate or auto-generate. Empty/None → ts_<unix>; invalid → 400."""
    if raw is None or not raw.strip():
        return f"ts_{int(time.time())}"
    s = raw.strip()
    if not _QSET_ID_RE.match(s):
        raise HTTPException(
            400,
            "question_set_id must start with [A-Za-z0-9] and contain only "
            "letters/digits/dot/dash/underscore (≤ 64 chars)",
        )
    return s


def _upload_dir(upload_id: str) -> Path:
    p = RUNS_ROOT / upload_id
    if not p.exists() or not (p / "manifest.json").exists():
        raise HTTPException(404, f"unknown upload_id: {upload_id}")
    return p


def _run_dir(upload_id: str, run_id: str) -> Path:
    return _upload_dir(upload_id) / "runs" / run_id


def _read_manifest(udir: Path) -> dict[str, Any]:
    m = udir / "manifest.json"
    if not m.exists():
        return {}
    try:
        return json.loads(m.read_text())
    except Exception:
        return {}


# ----- routes ------------------------------------------------------------

@app.get("/")
def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/api/agents")
def list_agents() -> JSONResponse:
    out = []
    for k in AGENT_REGISTRY:
        meta = AGENT_META.get(k, {})
        out.append({
            "id": k,
            "label": k,
            "available": True,
            "family": meta.get("family", ""),
            "kind": meta.get("kind", ""),
            "desc": meta.get("desc", ""),
        })
    return JSONResponse({"agents": out})


@app.get("/api/judge_info")
def judge_info() -> JSONResponse:
    j = JUDGE_CFG.get("judge", {})
    options = JUDGE_CFG.get("judge_options") or []
    return JSONResponse({
        "model": j.get("model"),
        "provider": j.get("provider"),
        "base_url": j.get("base_url"),
        "threshold": JUDGE_CFG.get("threshold", 0.6),
        "options": [
            {
                "id": o.get("id") or o.get("model"),
                "label": o.get("label") or o.get("model"),
                "model": o.get("model"),
                "provider": o.get("provider"),
                "description": o.get("description") or "",
            }
            for o in options
        ],
        "default_id": (options[0].get("id") if options else j.get("model")),
    })


def _resolve_judge_config(judge_id: str | None) -> dict[str, Any]:
    """Pick a `judge:` block from config, optionally swapped to a user-selected
    alternative under `judge_options:`. Falls back to the default `judge:` block
    if `judge_id` is empty or unknown."""
    base = dict(JUDGE_CFG.get("judge", {}))
    if not judge_id:
        return base
    for opt in (JUDGE_CFG.get("judge_options") or []):
        if (opt.get("id") or opt.get("model")) == judge_id:
            merged = dict(base)
            for k in ("provider", "model", "max_tokens", "timeout", "temperature", "max_retries", "base_url", "api_key_env"):
                if k in opt:
                    merged[k] = opt[k]
            return merged
    return base


@app.get("/api/rubric_definitions")
def rubric_definitions() -> JSONResponse:
    """Public rubric: every dimension's weight, definition, and anchors.

    Both the judge LLM (in-prompt) and the UI rubric panel read from this so
    they always show the same scale. The closed (gold) rubric is at the top
    level for backwards-compat; the OPEN rubric (used when a whole candidate set
    misses gold) is nested under "open".
    """
    spec = rubric_specification()
    spec["open"] = open_rubric_specification()
    return JSONResponse(spec)


@app.delete("/api/runs")
def clear_all_runs() -> JSONResponse:
    """Wipe every upload + run artifact. Only affects on-disk history; live
    in-memory runs (if any) are unaffected."""
    removed = 0
    for d in list(RUNS_ROOT.glob("upl_*")):
        try:
            shutil.rmtree(d)
            removed += 1
        except Exception:
            continue
    # also drop in-memory cache
    _runs.clear()
    return JSONResponse({"ok": True, "removed": removed})


@app.post("/api/uploads")
async def upload(
    file: UploadFile = File(..., description="data .zip"),
    gold: UploadFile = File(..., description="gold question .json"),
    question_set_id: str | None = Form(default=None, description="题集 id（同一题集的多次跑会被聚合）。空则自动用 ts_<unix>。"),
) -> JSONResponse:
    if not file.filename or not file.filename.lower().endswith(".zip"):
        raise HTTPException(400, "the data file must be a .zip")
    if not gold.filename or not gold.filename.lower().endswith(".json"):
        raise HTTPException(400, "the gold file must be a .json")

    qset_id = _normalise_qset_id(question_set_id)

    upload_id = _new_id("upl")
    udir = RUNS_ROOT / upload_id
    udir.mkdir(parents=True, exist_ok=True)
    zip_path = udir / "upload.zip"
    gold_in = udir / "gold_input.json"
    zip_path.write_bytes(await file.read())
    gold_in.write_bytes(await gold.read())

    # ---- 1. validate gold ------------------------------------------------
    gold_norm_path = udir / "gold_questions.json"
    gold_report = validate_gold(gold_in, gold_norm_path)
    if not gold_report.ok:
        manifest = {"ok": False, "stage": "gold", "question_set_id": qset_id,
                    "data": None, "gold": gold_report.to_json()}
        (udir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
        return JSONResponse({"upload_id": upload_id, **manifest}, status_code=400)

    # ---- 2. validate data zip --------------------------------------------
    extracted = udir / "_extracted"
    try:
        data_report = validate_data_zip(zip_path, extracted)
    except DataValidationError as e:
        manifest = {"ok": False, "stage": "data", "question_set_id": qset_id,
                    "data": {"errors": [str(e)]}, "gold": gold_report.to_json()}
        (udir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
        return JSONResponse({"upload_id": upload_id, **manifest}, status_code=400)

    if not data_report.ok:
        manifest = {"ok": False, "stage": "data", "question_set_id": qset_id,
                    "data": data_report.to_json(), "gold": gold_report.to_json()}
        (udir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
        return JSONResponse({"upload_id": upload_id, **manifest}, status_code=400)

    # ---- 3. hydrate workspace --------------------------------------------
    workspace_dir = udir / "workspace"
    _, available_features = hydrate_workspace(
        data_dir=Path(data_report.data_root),
        gold_normalised=gold_norm_path,
        dst=workspace_dir,
    )

    manifest = {
        "ok": True,
        "stage": "ready",
        "question_set_id": qset_id,
        "data": data_report.to_json(),
        "gold": gold_report.to_json(),
        "available_features": available_features,
        "workspace_dir": str(workspace_dir),
    }
    (udir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    return JSONResponse({"upload_id": upload_id, **manifest})


@app.get("/api/uploads")
def list_uploads() -> JSONResponse:
    items = []
    for d in sorted(RUNS_ROOT.glob("upl_*"), reverse=True):
        meta = _read_manifest(d)
        if not meta:
            continue
        items.append({
            "upload_id": d.name,
            "question_set_id": meta.get("question_set_id"),
            "created_at": d.stat().st_mtime,
            "ok": meta.get("ok", False),
            "stage": meta.get("stage", ""),
            "data_files": (meta.get("data") or {}).get("file_count"),
            "gold_total": (meta.get("gold") or {}).get("total_count"),
        })
    return JSONResponse({"uploads": items})


@app.get("/api/uploads/{upload_id}")
def get_upload(upload_id: str) -> JSONResponse:
    udir = _upload_dir(upload_id)
    return JSONResponse({"upload_id": upload_id, **json.loads((udir / "manifest.json").read_text())})


class StartRunRequest(BaseModel):
    upload_id: str
    agents: list[str] = []
    judge_only: bool = False
    # Judge-only mode: an AgentOutput-shaped dict (agent_id, questions: [...])
    # the user uploaded — we skip agent.run() and judge it directly.
    candidate: dict[str, Any] | None = None
    # Optional override — picks from config.yaml `judge_options[].id`. If
    # empty, the top-level `judge:` block is used.
    judge_id: str | None = None


@app.post("/api/runs")
async def start_run(req: StartRunRequest) -> JSONResponse:
    udir = _upload_dir(req.upload_id)
    manifest = json.loads((udir / "manifest.json").read_text())
    if not manifest.get("ok"):
        raise HTTPException(400, "upload is not ready")

    if req.judge_only:
        if req.agents:
            raise HTTPException(400, "judge_only=true requires agents=[] (no agent invocation)")
        if not isinstance(req.candidate, dict):
            raise HTTPException(400, "judge_only=true requires `candidate` (AgentOutput-shaped JSON)")
        # Validate the candidate shape eagerly so the user gets a useful error
        # before we kick off an async run that would just blow up later.
        try:
            from eval.utils.schemas import AgentOutput
            AgentOutput.model_validate(req.candidate)
        except Exception as e:
            raise HTTPException(400, f"candidate JSON does not match AgentOutput schema: {e}")
    else:
        bad = [a for a in req.agents if a not in AGENT_REGISTRY]
        if bad:
            raise HTTPException(400, f"unknown agents: {bad}")
        if not req.agents:
            raise HTTPException(400, "at least one agent must be selected")

    run_id = _new_id("run")
    run_dir = udir / "runs" / run_id
    run_dir.mkdir(parents=True)
    (run_dir / "results").mkdir()
    (run_dir / "sandboxes").mkdir()

    spec = RunSpec(
        run_id=run_id,
        workspace_root=udir / "workspace",
        gold_path=udir / "gold_questions.json",
        available_features=list(manifest.get("available_features", []) or []),
        agents=list(req.agents),
        judge_config=_resolve_judge_config(req.judge_id),
        threshold=float(JUDGE_CFG.get("threshold", 0.6)),
        results_root=run_dir / "results",
        sandbox_root=run_dir / "sandboxes",
        judge_only_candidate=req.candidate if req.judge_only else None,
    )
    bus = EventBus()
    runner = PipelineRunner(spec, bus)
    state = {"spec": spec, "bus": bus, "runner": runner, "task": None, "status": "queued"}
    _runs[(req.upload_id, run_id)] = state

    async def _drive() -> None:
        state["status"] = "running"
        try:
            await runner.run()
            state["status"] = "finished"
        except Exception as e:
            state["status"] = "failed"
            bus.append("run_failed", error=f"{type(e).__name__}: {e}")
            bus.close()

    state["task"] = asyncio.create_task(_drive())
    return JSONResponse({
        "run_id": run_id,
        "upload_id": req.upload_id,
        "agents": req.agents,
        "judge_only": req.judge_only,
        "judge_model": spec.judge_config.get("model"),
    })


@app.get("/api/runs")
def list_runs() -> JSONResponse:
    items = []
    for udir in sorted(RUNS_ROOT.glob("upl_*"), reverse=True):
        meta = _read_manifest(udir)
        qset_id = meta.get("question_set_id")
        for rd in sorted((udir / "runs").glob("run_*"), reverse=True):
            lb = rd / "results" / "leaderboard.json"
            ev = rd / "events.jsonl"
            finished = lb.exists()
            # Live status: prefer the in-memory state (queued/running/finished/failed)
            # over the on-disk inferred state. If the server was restarted, runs that
            # never wrote leaderboard.json show up as "abandoned" so the UI can stop
            # promising live progress that will never come.
            live = _runs.get((udir.name, rd.name))
            if live:
                status = live.get("status", "unknown")
            elif finished:
                status = "finished"
            else:
                status = "abandoned"
            items.append({
                "upload_id": udir.name,
                "run_id": rd.name,
                "question_set_id": qset_id,
                "created_at": rd.stat().st_mtime,
                "finished": finished,
                "status": status,
                "events_count": (sum(1 for _ in ev.open()) if ev.exists() else None),
            })
    return JSONResponse({"runs": items})


@app.get("/api/question_sets")
def list_question_sets() -> JSONResponse:
    """Aggregate uploads + runs by `question_set_id`.

    Each set looks like:
      {
        "question_set_id": "bat_btcn_virome_2024",
        "first_seen": <unix>,
        "last_seen":  <unix>,
        "uploads": [{ upload_id, created_at, ok, stage, runs: [...] }, ...],
        "run_count": N,
        "best_composite": <float|null>,
      }
    """
    groups: dict[str, dict[str, Any]] = {}
    for udir in sorted(RUNS_ROOT.glob("upl_*")):
        meta = _read_manifest(udir)
        if not meta:
            continue
        qset = meta.get("question_set_id") or f"ts_{int(udir.stat().st_mtime)}"
        ucreated = udir.stat().st_mtime
        runs_in_upload: list[dict[str, Any]] = []
        for rd in sorted((udir / "runs").glob("run_*")):
            lb = rd / "results" / "leaderboard.json"
            top_composite = None
            top_agent = None
            agents: list[str] = []
            finished = lb.exists()
            if finished:
                try:
                    lb_data = json.loads(lb.read_text())
                    rows = lb_data.get("rows") or []
                    agents = [r.get("agent_id") for r in rows if r.get("agent_id")]
                    rows_ok = [r for r in rows if r.get("ok") and r.get("composite_score") is not None]
                    if rows_ok:
                        top = max(rows_ok, key=lambda r: r.get("composite_score") or -1)
                        top_composite = top.get("composite_score")
                        top_agent = top.get("agent_id")
                except Exception:
                    finished = False
            runs_in_upload.append({
                "run_id": rd.name,
                "created_at": rd.stat().st_mtime,
                "finished": finished,
                "status": (
                    (_runs.get((udir.name, rd.name)) or {}).get("status")
                    or ("finished" if finished else "abandoned")
                ),
                "agents": agents,
                "top_composite": top_composite,
                "top_agent": top_agent,
            })
        upload_entry = {
            "upload_id": udir.name,
            "created_at": ucreated,
            "ok": meta.get("ok", False),
            "stage": meta.get("stage", ""),
            "data_files": (meta.get("data") or {}).get("file_count"),
            "gold_total": (meta.get("gold") or {}).get("total_count"),
            "runs": runs_in_upload,
        }
        g = groups.setdefault(qset, {
            "question_set_id": qset,
            "first_seen": ucreated,
            "last_seen": ucreated,
            "uploads": [],
            "run_count": 0,
            "best_composite": None,
            "best_agent": None,
        })
        g["uploads"].append(upload_entry)
        g["first_seen"] = min(g["first_seen"], ucreated)
        g["last_seen"] = max(g["last_seen"], max([r["created_at"] for r in runs_in_upload], default=ucreated))
        g["run_count"] += len(runs_in_upload)
        for r in runs_in_upload:
            tc = r.get("top_composite")
            if tc is not None and (g["best_composite"] is None or tc > g["best_composite"]):
                g["best_composite"] = tc
                g["best_agent"] = r.get("top_agent")
    # newest set first; uploads/runs inside already in mtime order
    sets = sorted(groups.values(), key=lambda x: -x["last_seen"])
    for g in sets:
        g["uploads"].sort(key=lambda u: -u["created_at"])
        for u in g["uploads"]:
            u["runs"].sort(key=lambda r: -r["created_at"])
    return JSONResponse({"question_sets": sets})


@app.get("/api/runs/{upload_id}/{run_id}")
def get_run(upload_id: str, run_id: str) -> JSONResponse:
    state = _runs.get((upload_id, run_id))
    rdir = _run_dir(upload_id, run_id)
    if not rdir.exists():
        raise HTTPException(404, "unknown run_id")
    udir = _upload_dir(upload_id)
    meta = _read_manifest(udir)
    out: dict[str, Any] = {
        "upload_id": upload_id,
        "run_id": run_id,
        "question_set_id": meta.get("question_set_id"),
        "status": state["status"] if state else "finished_or_unloaded",
    }
    lb = rdir / "results" / "leaderboard.json"
    if lb.exists():
        out["leaderboard"] = json.loads(lb.read_text())
    if state and state.get("bus"):
        out["events"] = [e.to_json() for e in state["bus"].events]
    elif (rdir / "events.jsonl").exists():
        out["events"] = [
            json.loads(ln) for ln in (rdir / "events.jsonl").read_text().splitlines() if ln.strip()
        ]
    return JSONResponse(out)


@app.get("/api/runs/{upload_id}/{run_id}/events")
async def stream_events(upload_id: str, run_id: str) -> StreamingResponse:
    rdir = _run_dir(upload_id, run_id)
    state = _runs.get((upload_id, run_id))

    async def _gen():
        if state and state.get("bus"):
            async for ev in state["bus"].subscribe():
                payload = json.dumps(ev.to_json(), ensure_ascii=False)
                yield f"event: {ev.kind}\ndata: {payload}\n\n"
        else:
            ej = rdir / "events.jsonl"
            if ej.exists():
                for ln in ej.read_text().splitlines():
                    if not ln.strip():
                        continue
                    obj = json.loads(ln)
                    yield f"event: {obj['kind']}\ndata: {ln}\n\n"
            yield "event: end\ndata: {}\n\n"

    return StreamingResponse(_gen(), media_type="text/event-stream")
