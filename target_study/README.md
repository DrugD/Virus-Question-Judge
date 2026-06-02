# target_study/  (judge-only)

This directory holds the **groundtruth assets** used by the judge LLM to score an agent's output. It MUST NOT be exposed to the agent during a run.

| File | Purpose |
|---|---|
| `checklist.json` | Byte-equal copy of the root `checklist.json`. Pinned here so the judge always reads the same rubric the agent saw. |
| `question_rubric.json` | Calibrated groundtruth questions (GQ_001 … GQ_008), the 6 rubric dimensions used for scoring, refusal flags, and 10 calibration anchors. |
| `paper_T001.pdf` | (Optional) Symlink or copy of the source paper PDF. Used only by humans verifying the rubric, never by the agent. |

## Provenance

The groundtruth questions in `question_rubric.json` are calibrated against the upstream petabase-scale search whose summary statistics are surfaced to the agent via `data/raw_data/blind_input_summary.json.data_scale_visible_to_agent` — they are **not** calibrated against the 53-row local subset distributed under `data/`.

## Pipeline access pattern

`eval/run_judge.py` loads:

1. The agent's `agent_questions.json` and `report.md` from `results/{agent}/{run_id}/`
2. `target_study/checklist.json` (rubric)
3. `target_study/question_rubric.json` (groundtruth questions for the `question_matching` dimension)

It never injects the groundtruth into the agent's context — only into the judge LLM's prompt.
