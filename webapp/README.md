# webapp/ — Visualization Console

A small FastAPI + vanilla-JS frontend for the rubric-judge pipeline.

## Run

```bash
cd /Users/likun/Desktop/AILab/病毒-Question-Judge
.venv/bin/python -m uvicorn webapp.server:app --host 127.0.0.1 --port 8765
```

Open http://127.0.0.1:8765/ — the page is a 4-step console:

1. **Upload a blind-data ZIP.** Required entries (any layout): `blind_input_summary.json`, `runinfo_subset.tsv`, `rdrp_aa_fragments.faa`, `alignment_hits.tsv`, `candidate_sotu_clusters.tsv`. The judge's groundtruth (`target_study/`) is reused from this repo and never uploaded by the user.
2. **Pick agents.** Any subset of `qwen3.6-plus` / `codex-cli` / `claude-code`. They run **in parallel** (`asyncio.gather`).
3. **Live progress.** SSE stream pushes `agent_started`, `agent_finished`, `judge_started`, `judge_finished`, `run_finished` with timestamps; the timeline shows agent-time vs judge-time bars.
4. **Results.** Five tabs:
   - Leaderboard table (composite, raw /5, pass/fail, flags, agent time, judge time)
   - 6-dimension radar (one polygon per agent)
   - Per-dimension grouped bars
   - Top-1 question side-by-side cards (with rationale + scope_keywords)
   - Timing breakdown (stacked horizontal bar, agent vs judge)

## Files

| Path | Purpose |
|---|---|
| `server.py` | FastAPI routes: `/api/agents`, `/api/uploads`, `/api/runs`, `/api/runs/.../events` (SSE) |
| `validator.py` | Unzip + canonicalize layout + JSON schema + TSV header check |
| `pipeline_runner.py` | Async wrapper around `eval/`'s `Workspace` + `REGISTRY` + `score_agent_run`, emits structured events to an `EventBus` and persists `events.jsonl` |
| `static/index.html` | SPA shell |
| `static/style.css` | Dark dashboard theme |
| `static/app.js` | Upload → agent select → SSE-driven state machine |
| `static/charts.js` | Chart.js wrapper for radar / bars / timing canvases |

## Persistence

```
webapp_runs/<upload_id>/
├── upload.zip                 ← original
├── _extracted/                ← raw extraction
├── validation.json            ← report shown in step 1
├── workspace/                 ← hydrated full workspace (blind data + reused target_study)
└── runs/<run_id>/
    ├── results/
    │   ├── leaderboard.json
    │   └── <agent>/<ts>/agent_questions.json + report/report.md + judge_scores.json + _logs.txt
    ├── sandboxes/             ← internal AgentRunner sandboxes
    └── events.jsonl           ← persisted event stream (SSE replay source)
```

`/api/runs` lists every (upload_id, run_id) pair; `/api/runs/{up}/{rn}` returns the full leaderboard + replay-able events for completed runs.

## Notes

- **First request after server start is slow** because importing `deepeval` (it pulls `rich`, `posthog`, `opentelemetry`, …) takes a while under load. Subsequent requests reuse the cached imports.
- **Codex CLI requires an ASCII-only sandbox** because the Rust binary panics on CJK paths. The agent runner forces `/tmp/codex-sandboxes/` regardless of where this project lives.
- `.env` (project root) supplies `NEWAPI_KEY` + base URLs; the server bootstraps env vars from it on startup.
