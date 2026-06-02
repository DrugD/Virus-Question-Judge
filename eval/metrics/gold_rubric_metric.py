"""Judge metric driven by an UPLOADED gold-question JSON.

Compared to the v1 implementation, this version:
  - publishes the rubric scale (what every 0..5 score means per dimension)
    as a Python constant so both the UI and the judge prompt stay in sync;
  - asks the judge LLM for per-dimension reasoning, plus the closest
    acceptable / unacceptable variant it considered, so the user can see
    EXACTLY how each score was reached;
  - keeps the same composite weights and centrality penalty.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from typing import Any

from .judge_llm import JudgeLLM


WEIGHTS: dict[str, float] = {
    "match_strength":             0.40,
    "required_elements_coverage": 0.30,
    "acceptability":              0.20,
    "data_grounding":             0.10,
}
SECONDARY_PENALTY = 0.85

DIMENSION_LABELS: dict[str, str] = {
    "match_strength":             "Match strength",
    "required_elements_coverage": "Required-element coverage",
    "acceptability":              "Acceptability vs unacceptable",
    "data_grounding":             "Data grounding",
}

DIMENSION_DEFS: dict[str, str] = {
    "match_strength":
        "How well the candidate question captures the *intent* of the matched "
        "gold question (semantic alignment, not just keyword overlap).",
    "required_elements_coverage":
        "Of the matched gold's `required_elements`, how many are present in "
        "the candidate (in question text or rationale). Coverage = round(present / total * 5).",
    "acceptability":
        "Distance from the gold's acceptable / unacceptable variants. Closer to "
        "an `acceptable_variant` → higher; closer to an `unacceptable_variant` → lower.",
    "data_grounding":
        "Does the candidate reference real data features that exist in the "
        "uploaded files? Generic phrasing (e.g. 'this dataset') scores low.",
}

# Anchor descriptions for each integer 0..5 score, per dimension.
# These are shown to the judge IN-PROMPT and to the user in the rubric panel.
DIMENSION_ANCHORS: dict[str, dict[int, str]] = {
    "match_strength": {
        0: "Unrelated to any gold question.",
        1: "Touches the same broad topic but a clearly different scientific question.",
        2: "Same general theme but misses the matched gold's intent.",
        3: "Captures part of the matched gold's intent; missing core framing.",
        4: "Captures the matched gold's intent with minor omissions or rewording.",
        5: "Faithfully captures the matched gold's intent at full scope.",
    },
    "required_elements_coverage": {
        0: "None of the required elements present.",
        1: "Roughly 1/5 of required elements present.",
        2: "Roughly 2/5 of required elements present.",
        3: "Roughly 3/5 of required elements present.",
        4: "Roughly 4/5 of required elements present.",
        5: "All required elements explicitly or substantively present.",
    },
    "acceptability": {
        0: "Essentially identical to a listed unacceptable_variant.",
        1: "Clearly closer to unacceptable than to acceptable.",
        2: "Mid-quality but leans unacceptable.",
        3: "Mid-quality, leaning toward acceptable but generic.",
        4: "Close to one of the acceptable_variants.",
        5: "Matches an acceptable_variant in framing and specificity.",
    },
    "data_grounding": {
        0: "No reference to any data feature.",
        1: "Vague mention of 'the data' with no specifics.",
        2: "References one feature non-specifically.",
        3: "References one feature with concrete framing.",
        4: "References multiple specific features / files.",
        5: "Concrete framing across multiple files/columns + numerical evidence.",
    },
}


def rubric_specification() -> dict[str, Any]:
    """Public dump of the rubric — used by /api/rubric_definitions."""
    return {
        "weights":         WEIGHTS,
        "secondary_penalty": SECONDARY_PENALTY,
        "dimension_labels": DIMENSION_LABELS,
        "dimension_defs":   DIMENSION_DEFS,
        "dimension_anchors": {
            d: [{"score": s, "anchor": txt} for s, txt in sorted(anchors.items())]
            for d, anchors in DIMENSION_ANCHORS.items()
        },
    }


# ---------------------------------------------------------------------------
# Judge prompt
# ---------------------------------------------------------------------------

def _build_anchor_table() -> str:
    """Render the anchor table inline so the judge sees the same scale we
    publish to the user."""
    lines: list[str] = []
    for dim, anchors in DIMENSION_ANCHORS.items():
        lines.append(f"\n## {dim} (weight {WEIGHTS[dim]:.2f}) — {DIMENSION_LABELS[dim]}")
        lines.append(DIMENSION_DEFS[dim])
        for s in sorted(anchors):
            lines.append(f"  - {s}: {anchors[s]}")
    return "\n".join(lines)


JUDGE_SYSTEM_PROMPT = f"""\
You are a strict scientific-question rubric judge. You score a single CANDIDATE
question against a list of GOLD scientific questions.

Process:
  1. Pick the gold question whose intent best matches the candidate (by
     semantics, not by keyword overlap alone). Output its `gold_question_id`.
  2. Score 4 dimensions on integers 0..5 using ONLY the anchors below. For
     each dimension you MUST also write a one-sentence reasoning line
     citing concrete elements from the candidate's question + rationale.
  3. Identify which of the matched gold's `acceptable_variants` (if any) the
     candidate is closest to, and which `unacceptable_variants` (if any) it
     dangerously resembles. Quote the exact variant text.
  4. List covered_required_elements and missing_required_elements (subsets of
     the matched gold's required_elements).

# Rubric scale (use these anchors verbatim)
{_build_anchor_table()}

Reply with ONLY this JSON object, no prose outside it:

{{
  "matched_gold_id": "<id>",
  "matched_centrality": "primary"|"secondary"|"unknown",
  "scores": {{
    "match_strength":             <int 0..5>,
    "required_elements_coverage": <int 0..5>,
    "acceptability":              <int 0..5>,
    "data_grounding":             <int 0..5>
  }},
  "per_dimension_reasoning": {{
    "match_strength":             "<one sentence with concrete citation>",
    "required_elements_coverage": "<one sentence>",
    "acceptability":              "<one sentence>",
    "data_grounding":             "<one sentence>"
  }},
  "covered_required_elements":  [...],
  "missing_required_elements":  [...],
  "closest_acceptable_variant":   "<exact variant text or empty string>",
  "closest_unacceptable_variant": "<exact variant text or empty string>",
  "rationale": "<<= 60 words overall summary>"
}}
"""


JUDGE_USER_TEMPLATE = """\
GOLD QUESTIONS (each: gold_question_id, question, required_elements,
acceptable_variants, unacceptable_variants, centrality)
=========================================================================
{gold_block}

AVAILABLE DATA FEATURES (file or column names the agent could ground in)
========================================================================
{features_block}

CANDIDATE
=========
agent_id        : {agent_id}
question        : {question}
rationale       : {rationale}
data_support    : {data_support}
expected_test   : {expected_test}
scope_keywords  : {scope_keywords}

Return JSON only. Do not echo this prompt.
"""


# ---------------------------------------------------------------------------
# Result dataclass
# ---------------------------------------------------------------------------

@dataclass
class GoldRubricResult:
    candidate: dict[str, Any]
    matched_gold_id: str
    matched_centrality: str
    matched_gold_question: str
    scores: dict[str, int]                      # raw 0..5
    composite_score: float                      # 0..1, after centrality penalty
    composite_score_raw: float                  # 0..5
    weights: dict[str, float]
    per_dimension_reasoning: dict[str, str] = field(default_factory=dict)
    covered_required_elements: list[str] = field(default_factory=list)
    missing_required_elements: list[str] = field(default_factory=list)
    closest_acceptable_variant: str = ""
    closest_unacceptable_variant: str = ""
    rationale: str = ""
    passed: bool = False
    threshold: float = 0.6
    primary_available: bool = False
    rubric_anchors: dict[str, dict[int, str]] = field(default_factory=dict)

    def to_json(self) -> dict[str, Any]:
        return asdict(self)


def score_against_gold(
    judge: JudgeLLM,
    candidate: dict[str, Any],
    gold_questions: list[dict[str, Any]],
    available_features: list[str],
    threshold: float = 0.6,
) -> GoldRubricResult:
    gold_block = json.dumps(gold_questions, ensure_ascii=False, indent=2)
    feats = "\n".join(f"- {f}" for f in available_features) or "- (none provided)"

    user = JUDGE_USER_TEMPLATE.format(
        gold_block=gold_block,
        features_block=feats,
        agent_id=candidate.get("agent_id", ""),
        question=candidate.get("question", ""),
        rationale=candidate.get("rationale", ""),
        data_support=candidate.get("data_support", []),
        expected_test=candidate.get("expected_test", ""),
        scope_keywords=candidate.get("scope_keywords", []),
    )

    payload = judge.chat_json(JUDGE_SYSTEM_PROMPT, user)

    # ---- normalise ---------------------------------------------------------
    matched_id = str(payload.get("matched_gold_id", "")).strip()
    by_id = {gq.get("gold_question_id", ""): gq for gq in gold_questions}
    matched_gq = by_id.get(matched_id) or (gold_questions[0] if gold_questions else {})
    centrality = (
        payload.get("matched_centrality")
        or matched_gq.get("centrality")
        or "unknown"
    ).lower()

    raw_scores = payload.get("scores", {}) or {}
    scores = {k: max(0, min(5, int(raw_scores.get(k, 0)))) for k in WEIGHTS}

    weighted_raw = sum(WEIGHTS[k] * scores[k] for k in WEIGHTS)  # 0..5
    composite = weighted_raw / 5.0
    primary_avail = any((gq.get("centrality") or "").lower() == "primary" for gq in gold_questions)
    if centrality == "secondary" and primary_avail:
        composite *= SECONDARY_PENALTY
        weighted_raw *= SECONDARY_PENALTY

    per_dim_reason = payload.get("per_dimension_reasoning") or {}
    per_dim_reason = {k: str(per_dim_reason.get(k, "") or "") for k in WEIGHTS}

    return GoldRubricResult(
        candidate=candidate,
        matched_gold_id=matched_id or matched_gq.get("gold_question_id", ""),
        matched_centrality=centrality,
        matched_gold_question=matched_gq.get("question", ""),
        scores=scores,
        composite_score=composite,
        composite_score_raw=weighted_raw,
        weights=dict(WEIGHTS),
        per_dimension_reasoning=per_dim_reason,
        covered_required_elements=list(payload.get("covered_required_elements", []) or []),
        missing_required_elements=list(payload.get("missing_required_elements", []) or []),
        closest_acceptable_variant=str(payload.get("closest_acceptable_variant", "") or ""),
        closest_unacceptable_variant=str(payload.get("closest_unacceptable_variant", "") or ""),
        rationale=str(payload.get("rationale", "") or ""),
        passed=composite >= threshold,
        threshold=threshold,
        primary_available=primary_avail,
        rubric_anchors=DIMENSION_ANCHORS,
    )
