# INSTRUCTIONS — Scientific Question Generation

You are an autonomous research agent. Read every file under `data/`, perform analysis, and propose **the single most important scientific question** that the data could be used to answer.

A separate judge LLM will score your top-1 question against a hidden gold rubric. **You will NOT see the gold rubric.** Frame your question purely from the data you observe.

---

## What you have

| Path | Description | Read? |
|---|---|---|
| `data/` | Whatever the user uploaded. Could be tables, FASTA, JSON, images, PDFs, …. Make no assumption about schema — discover the structure by listing and sampling files. | ✅ |
| `info.json` | Data-side metadata: file inventory, sizes, derived statistics. | ✅ |
| `gold/` | Gold rubric used by the judge. **MUST NOT be opened.** | ❌ |

---

## What you must produce (exact paths)

### `report/report.md`

A short technical report (~300–600 words) with these sections:

1. **Data summary** — what files you found, structure, scale, key columns / fields.
2. **Analysis** — at least three derived statistics, distributions, or relationships you computed from the data.
3. **Reasoning** — why these observations motivate the scientific question you will pose.
4. **Top scientific question** — copied verbatim from `agent_questions.json[0].question`.
5. **Why this question is testable on the provided dataset.**

### `agent_questions.json`

```json
{
  "agent_id": "<your model + harness identifier>",
  "questions": [
    {
      "rank": 1,
      "question": "<one English sentence ending with '?'>",
      "rationale": "<2-4 sentences linking the question to specific data evidence>",
      "data_support": ["<actual file or feature names you used>", "..."],
      "expected_test": "<how the question is answerable using the kind of data described>",
      "scope_keywords": ["<3-8 short keywords>"]
    }
  ]
}
```

- You MUST provide **exactly 5 distinct candidates** (rank 1..5). Duplicates fail validation. The judge scores all 5 and reports:
  - **Pass@1** = 100% if `questions[0]` passes else 0%.
  - **Pass@5** = count-based score: each of your 5 candidates that passes adds a flat **+0.2** (pass_count / 5), regardless of its rank. Examples: 1 of 5 passes → 20%, 3 of 5 → 60%, all 5 → 100%.
- Put your **strongest** answer at rank 1 (it drives Pass@1), but every candidate counts equally toward Pass@5 — make all 5 grounded and distinct.
- Each `question` must be a single sentence ending with `?`.
- `data_support` items must reference files or features that **actually exist** in the uploaded data.

---

## How to think about the rubric (informally)

The judge looks for questions that:

- **target a non-trivial scientific opportunity**, not a routine ETL or data-cleaning task;
- have **biomedical / ecological / surveillance / engineering significance**;
- are **testable using the data in front of you** (you should be able to outline the analysis);
- are **specifically grounded** — name the dataset's actual features instead of generic phrases like "this data";
- are **precisely phrased** — clear scientific object, scope, marker, and expected implication.

A question like *"Are there interesting patterns in the data?"* will score very low. A question that names the specific dataset modality, the specific marker / variable of interest, the scale at which the question operates, and the scientific implication will score high.

---

## What NOT to do

- Do not fabricate file names, statistics, or features that aren't in the upload.
- Do not propose questions that require wet-lab experiments not derivable from the data.
- Do not open `gold/`.
- Do not generate ten generic questions hoping one hits — only `questions[0]` is scored.

When `report/report.md` and `agent_questions.json` both exist on disk, your run is complete.
