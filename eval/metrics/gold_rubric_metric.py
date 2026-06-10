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


# =============================================================================
# Closed-question rubric (candidate has a matching GOLD question).
#
# Two dimensions, point-based (NOT 0..5). User-designed anchors, rescaled so the
# two maxima sum to 100 while preserving the original 2:1 ratio (40:20 → 67:33)
# and the original 4-level structure.
#
#   1.1 语义对齐 / semantic_alignment        — max 67
#   1.2 可接受度与错误控制 / acceptability    — max 33
#
# composite_score (0..1) = (semantic + acceptability) / 100.
# =============================================================================

# Max points per dimension (these sum to 100).
DIMENSION_MAX: dict[str, int] = {
    "semantic_alignment": 67,
    "acceptability":      33,
}
# Back-compat alias: some downstream code references WEIGHTS. It now holds the
# per-dimension MAX POINTS (not 0..1 fractions). composite is raw/100.
WEIGHTS = DIMENSION_MAX
TOTAL_MAX = sum(DIMENSION_MAX.values())            # 100
SECONDARY_PENALTY = 0.85

DIMENSION_LABELS: dict[str, str] = {
    "semantic_alignment": "语义对齐 / Semantic alignment",
    "acceptability":      "可接受度与错误控制 / Acceptability & error control",
}

DIMENSION_DEFS: dict[str, str] = {
    "semantic_alignment":
        "Does the candidate question reconstruct the matched gold question's "
        "research object, scientific goal, and the relationship it asks about?",
    "acceptability":
        "Is the candidate a reasonable rewrite / acceptable_variant of the gold "
        "(no unsupported extrapolation), or has it degraded toward an "
        "unacceptable_variant / hallucination / paper-or-rawdata-unsupported content?",
}

# Allowed integer point values per dimension, each with its anchor description.
# The judge MUST output one of these exact values per dimension.
DIMENSION_ANCHORS: dict[str, dict[int, str]] = {
    "semantic_alignment": {
        67: "生成问题与 gold question 在研究对象、科学目标和问题关系上基本等价。",
        42: "大方向正确，但问题关系或科学目标有明显遗漏。",
        17: "只识别到论文主题，未准确还原核心科学问题。",
        0:  "研究对象或任务类型错误。",
    },
    "acceptability": {
        33: "属于 gold question 的合理改写或 acceptable variant，没有明显无依据扩展。",
        20: "部分合理，但问题过泛、过细，或科学问题层级不够准确。",
        8:  "接近 unacceptable variant，虽然相关但明显退化。",
        0:  "完全无关、幻觉，或引入论文/Raw data 不支持的内容。",
    },
}


def _snap(dim: str, value: int) -> int:
    """Snap a judge-returned score to the nearest allowed anchor value for dim."""
    allowed = sorted(DIMENSION_ANCHORS[dim].keys())
    try:
        v = int(value)
    except (TypeError, ValueError):
        return 0
    return min(allowed, key=lambda a: abs(a - v))


def rubric_specification() -> dict[str, Any]:
    """Public dump of the rubric — used by /api/rubric_definitions."""
    return {
        "kind":            "closed",           # closed = has matching gold
        "dimension_max":   DIMENSION_MAX,
        "total_max":       TOTAL_MAX,
        "weights":         DIMENSION_MAX,       # back-compat alias (now = max points)
        "secondary_penalty": SECONDARY_PENALTY,
        "dimension_labels": DIMENSION_LABELS,
        "dimension_defs":   DIMENSION_DEFS,
        "dimension_anchors": {
            d: [{"score": s, "anchor": txt} for s, txt in sorted(anchors.items(), reverse=True)]
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
        lines.append(f"\n## {dim} (max {DIMENSION_MAX[dim]}) — {DIMENSION_LABELS[dim]}")
        lines.append(DIMENSION_DEFS[dim])
        for s in sorted(anchors, reverse=True):
            lines.append(f"  - {s}: {anchors[s]}")
    return "\n".join(lines)


JUDGE_SYSTEM_PROMPT = f"""\
You are a strict scientific-question rubric judge. You score a single CANDIDATE
question against a list of GOLD scientific questions.

Process:
  1. Pick the gold question whose intent best matches the candidate (by
     semantics, not by keyword overlap alone). Output its `gold_question_id`.
     If NO gold question shares the candidate's research object / task at all,
     set `gold_matched` to false and give semantic_alignment = 0.
  2. Score 2 dimensions. For EACH dimension you MUST output exactly one of the
     allowed point values below (no other numbers), plus a one-sentence
     reasoning line citing concrete elements from the candidate's question.
  3. Identify which of the matched gold's `acceptable_variants` (if any) the
     candidate is closest to, and which `unacceptable_variants` (if any) it
     dangerously resembles. Quote the exact variant text.
  4. List covered_required_elements and missing_required_elements (subsets of
     the matched gold's required_elements).

# Rubric scale (use these EXACT point values verbatim)
{_build_anchor_table()}

Reply with ONLY this JSON object, no prose outside it:

{{
  "matched_gold_id": "<id or empty string>",
  "gold_matched": true|false,
  "matched_centrality": "primary"|"secondary"|"unknown",
  "scores": {{
    "semantic_alignment": <one of 67|42|17|0>,
    "acceptability":      <one of 33|20|8|0>
  }},
  "per_dimension_reasoning": {{
    "semantic_alignment": "<one sentence with concrete citation>",
    "acceptability":      "<one sentence>"
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

CANDIDATE
=========
agent_id        : {agent_id}
question        : {question}

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
    scores: dict[str, int]                      # raw points per dimension
    composite_score: float                      # 0..1, after centrality penalty
    composite_score_raw: float                  # 0..100 points (after penalty)
    weights: dict[str, float]                   # per-dimension max points
    gold_matched: bool = True                   # False → open-question fallback territory
    is_open: bool = False                       # True when no gold matched the candidate
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
    available_features: list[str] | None = None,
    threshold: float = 0.6,
) -> GoldRubricResult:
    # available_features kept for backwards-compat with callers; not fed to the
    # judge (candidate is just {rank, question}).
    gold_block = json.dumps(gold_questions, ensure_ascii=False, indent=2)

    user = JUDGE_USER_TEMPLATE.format(
        gold_block=gold_block,
        agent_id=candidate.get("agent_id", ""),
        question=candidate.get("question", ""),
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
    scores = {k: _snap(k, raw_scores.get(k, 0)) for k in DIMENSION_MAX}

    # gold_matched: explicit judge flag, else infer from semantic_alignment.
    gold_matched = payload.get("gold_matched")
    if gold_matched is None:
        gold_matched = scores["semantic_alignment"] > 0
    gold_matched = bool(gold_matched)
    is_open = not gold_matched

    points = sum(scores[k] for k in DIMENSION_MAX)          # 0..100
    composite = points / float(TOTAL_MAX)                   # 0..1
    primary_avail = any((gq.get("centrality") or "").lower() == "primary" for gq in gold_questions)
    if centrality == "secondary" and primary_avail:
        composite *= SECONDARY_PENALTY
        points *= SECONDARY_PENALTY

    per_dim_reason = payload.get("per_dimension_reasoning") or {}
    per_dim_reason = {k: str(per_dim_reason.get(k, "") or "") for k in DIMENSION_MAX}

    return GoldRubricResult(
        candidate=candidate,
        matched_gold_id=matched_id or matched_gq.get("gold_question_id", ""),
        matched_centrality=centrality,
        matched_gold_question=matched_gq.get("question", ""),
        scores=scores,
        composite_score=composite,
        composite_score_raw=points,
        weights=dict(DIMENSION_MAX),
        gold_matched=gold_matched,
        is_open=is_open,
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
