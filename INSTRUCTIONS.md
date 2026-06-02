# INSTRUCTIONS — Scientific Question Generation

You are an autonomous research agent. Read **every file the user uploaded** under `data/`, perform analysis, and propose **the single most important scientific question** that the data could be used to answer.

A separate judge LLM will score your top-1 question against a hidden gold rubric. **You will NOT see the gold rubric.** Frame your question purely from what you observe in the data.

---

## 1. What you have access to

| Path | Description | Read? |
|---|---|---|
| `data/` | Everything the user uploaded — could be tables, FASTA, JSON, images, PDFs, raw text, .docx, … Make **no assumption** about schema or filenames; discover structure by listing and sampling. | ✅ |
| `info.json` | Auto-generated manifest: full file inventory, sizes, extension histogram, output contract. | ✅ |
| `INSTRUCTIONS.md` | This file. | ✅ |
| `gold/` | The judge's rubric. **MUST NOT be opened.** | ❌ |

> The contents of `data/` are user-supplied and arbitrary. Do not hard-code any specific filename in your reasoning — list the directory first, then read what's actually there.

---

## 2. What you must produce (exact paths)

### 2.1 `report/report.md`

A short technical report (~300–600 words) with these sections:

1. **Data summary** — which files exist, their format/scale, key columns/fields you observed.
2. **Analysis** — at least three derived statistics, distributions, or relationships you computed from the actual files.
3. **Reasoning** — why these observations motivate the question you will pose.
4. **Top scientific question** — copied verbatim from `agent_questions.json[0].question`.
5. **Why this question is testable on the provided dataset.**

### 2.2 `agent_questions.json`

A ranked list of candidate questions, **best first**. Schema (also in `info.json.agent_output_schema`):

```json
{
  "agent_id": "<your model + harness identifier>",
  "workspace_id": "user_uploaded",
  "questions": [
    {
      "rank": 1,
      "question": "<one English sentence ending with '?'>",
      "rationale": "<2-4 sentences linking the question to specific data evidence>",
      "data_support": ["<actual file or feature names you read>", "..."],
      "expected_test": "<how the question is answerable using this kind of data>",
      "scope_keywords": ["<3-8 short keywords>"]
    }
  ]
}
```

- You MUST provide **exactly 5 distinct candidates** (rank 1..5). Duplicates fail validation. The judge scores all 5 and reports:
  - **Pass@1** = 100% if `questions[0]` passes else 0%.
  - **Pass@5** = count-based score: each of your 5 candidates that passes adds a flat **+0.2** (pass_count / 5), independent of its rank. So 1 of 5 = 20%, 3 of 5 = 60%, all 5 = 100%.
- Put your **strongest** answer at rank 1 (it drives Pass@1), but every candidate counts equally toward Pass@5 — make all 5 distinct and grounded.
- Each `question` text must be a single sentence ending with `?`.
- Each `data_support` entry must reference files or features that **actually exist** in the uploaded data (i.e., a path you actually read).

---

## 3. How to think about the rubric (informally)

The judge looks for questions that:

- **target a non-trivial scientific opportunity**, not a routine ETL or data-cleaning task;
- have **biomedical / ecological / surveillance / engineering / domain significance**;
- are **testable using the data in front of you** (you should be able to outline the analysis);
- are **specifically grounded** — name the dataset's actual variables / objects, not generic phrases like "this data";
- are **precisely phrased** — clear scientific object, scope, marker, and expected implication.

A question like *"Are there interesting patterns in the data?"* will score very low. A question that names the specific dataset modality, the specific marker / variable of interest, the scale at which the question operates, and the scientific implication will score high.

---

## 4. What NOT to do

- Do not fabricate filenames, statistics, fields, or features that aren't in the upload.
- Do not propose questions that require wet-lab or extra-dataset experiments not derivable from what you can see.
- Do not open `gold/`.
- Do not generate generic placeholder questions hoping one hits — every candidate must be specifically grounded.
- Do not assume a specific domain just because you happen to recognize the data; let the actual files dictate scope.

---

## 5. Output checklist before you stop

- [ ] `report/report.md` exists with the 5 sections above.
- [ ] `agent_questions.json` exists, parses as JSON, conforms to the schema.
- [ ] `questions[0].question` is a single sentence ending with `?`.
- [ ] All `data_support` entries match real paths under `data/`.

When both files are on disk and these checks pass, your run is complete; the judge pipeline will pick them up automatically.
