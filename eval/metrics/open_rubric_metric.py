"""Open-question rubric — used when an agent's whole candidate set MISSES gold.

When none of an agent's candidates hit any gold question (set-level Hit = ✗,
i.e. ``pass_count == 0`` against the closed threshold), the questions are not
"failed closed attempts" to be zeroed — they are open / exploratory proposals
that deserve to be judged on their own merits. This module scores such a
candidate on two dimensions, relative to the (desensitized) original data:

  data_match — does the proposed question actually fit THIS dataset?  (max 50)
  soundness  — is it a non-trivial, logically sound, testable question? (max 50)

composite_score (0..1) = (data_match + soundness) / 100.

The result is returned as a ``GoldRubricResult`` (reused from gold_rubric_metric)
so every downstream row-builder / UI consumer stays uniform; it is tagged with
``rubric_kind="open"``, ``is_open=True``, ``gold_matched=False``.
"""

from __future__ import annotations

import json
from typing import Any

from .judge_llm import JudgeLLM
from .gold_rubric_metric import GoldRubricResult

# =============================================================================
# Open-question rubric — two dimensions, point-based, 50 + 50 = 100.
# =============================================================================

OPEN_DIMENSION_MAX: dict[str, int] = {
    "data_match": 50,
    "soundness":  50,
}
OPEN_TOTAL_MAX = sum(OPEN_DIMENSION_MAX.values())            # 100

OPEN_DIMENSION_LABELS: dict[str, str] = {
    "data_match": "数据匹配度 / Data match",
    "soundness":  "科学合理性 / Scientific soundness",
}

OPEN_DIMENSION_DEFS: dict[str, str] = {
    "data_match":
        "Relative to the ORIGINAL (desensitized) dataset shown in DATA CONTEXT: "
        "do the objects/variables the question asks about actually exist in the "
        "data, and are the data's scale / type / granularity sufficient to "
        "investigate it? (Anti-gaming gate — a fancy-sounding question the data "
        "cannot support must score low.)",
    "soundness":
        "Independent of any gold: is the question itself a good scientific "
        "question — non-trivial (not a descriptive statistic / common sense), "
        "logically self-consistent, and clearly testable (variables, direction, "
        "comparison are explicit)?",
}

# Allowed integer point values per dimension, each with its anchor description.
# The judge MUST output one of these exact values per dimension.
OPEN_DIMENSION_ANCHORS: dict[str, dict[int, str]] = {
    "data_match": {
        50: "问题所涉对象/变量都真实存在于数据中，且数据规模/类型/粒度足以支撑研究它。",
        32: "大体可由数据研究，但部分关键变量缺失或规模/粒度勉强。",
        14: "仅与数据边缘相关，数据难以真正支撑该问题。",
        0:  "与数据完全无关，或答非所问（追问数据里根本没有的对象）。",
    },
    "soundness": {
        50: "问题非平凡、逻辑自洽，且表述明确可检验（变量/方向/比较清楚）。",
        32: "合理但偏平凡（接近描述统计/常识），或表述有一定含糊。",
        14: "有明显缺陷：弱可检验、部分逻辑/科学谬误，或过于宽泛。",
        0:  "不成立、含明显科学谬误，或无研究意义。",
    },
}


def _snap(dim: str, value: Any) -> int:
    """Snap a judge-returned score to the nearest allowed anchor value for dim."""
    allowed = sorted(OPEN_DIMENSION_ANCHORS[dim].keys())
    try:
        v = int(value)
    except (TypeError, ValueError):
        return 0
    return min(allowed, key=lambda a: abs(a - v))


def open_rubric_specification() -> dict[str, Any]:
    """Public dump of the open rubric — used by /api/rubric_definitions + UI."""
    return {
        "kind":            "open",          # open = no gold matched; data-relative
        "dimension_max":   OPEN_DIMENSION_MAX,
        "total_max":       OPEN_TOTAL_MAX,
        "weights":         OPEN_DIMENSION_MAX,
        "dimension_labels": OPEN_DIMENSION_LABELS,
        "dimension_defs":   OPEN_DIMENSION_DEFS,
        "dimension_anchors": {
            d: [{"score": s, "anchor": txt} for s, txt in sorted(anchors.items(), reverse=True)]
            for d, anchors in OPEN_DIMENSION_ANCHORS.items()
        },
    }


# ---------------------------------------------------------------------------
# Judge prompt
# ---------------------------------------------------------------------------

def _build_anchor_table() -> str:
    lines: list[str] = []
    for dim, anchors in OPEN_DIMENSION_ANCHORS.items():
        lines.append(f"\n## {dim} (max {OPEN_DIMENSION_MAX[dim]}) — {OPEN_DIMENSION_LABELS[dim]}")
        lines.append(OPEN_DIMENSION_DEFS[dim])
        for s in sorted(anchors, reverse=True):
            lines.append(f"  - {s}: {anchors[s]}")
    return "\n".join(lines)


JUDGE_SYSTEM_PROMPT_OPEN = f"""\
You are a strict scientific-question rubric judge. The candidate question did
NOT match any gold question, so you score it as an OPEN / exploratory proposal
on its own merits, relative to the dataset described in DATA CONTEXT.

Process:
  1. Score 2 dimensions. For EACH dimension you MUST output exactly one of the
     allowed point values below (no other numbers), plus a one-sentence
     reasoning line citing concrete elements from the candidate's question AND
     from DATA CONTEXT (e.g. which column / field supports or fails to support
     the question).
  2. Be conservative on data_match: if the data shown cannot actually support
     the question, score it low no matter how interesting the question sounds.

# Rubric scale (use these EXACT point values verbatim)
{_build_anchor_table()}

Reply with ONLY this JSON object, no prose outside it:

{{
  "scores": {{
    "data_match": <one of 50|32|14|0>,
    "soundness":  <one of 50|32|14|0>
  }},
  "per_dimension_reasoning": {{
    "data_match": "<one sentence citing a concrete data column/field>",
    "soundness":  "<one sentence>"
  }},
  "rationale": "<<= 60 words overall summary>"
}}
"""


JUDGE_USER_TEMPLATE_OPEN = """\
DATA CONTEXT (desensitized — same content the agent saw; only filenames are
anonymised to 1.ext / 2.ext …)
=========================================================================
{data_digest}

CANDIDATE (open question — did not match any gold)
==================================================
agent_id        : {agent_id}
question        : {question}

Return JSON only. Do not echo this prompt.
"""


def score_open_question(
    judge: JudgeLLM,
    candidate: dict[str, Any],
    data_digest: str,
    threshold: float = 0.6,
) -> GoldRubricResult:
    """Score one open candidate (no gold) on data_match + soundness."""
    user = JUDGE_USER_TEMPLATE_OPEN.format(
        data_digest=data_digest or "(no data context available)",
        agent_id=candidate.get("agent_id", ""),
        question=candidate.get("question", ""),
    )

    payload = judge.chat_json(JUDGE_SYSTEM_PROMPT_OPEN, user)

    raw_scores = payload.get("scores", {}) or {}
    scores = {k: _snap(k, raw_scores.get(k, 0)) for k in OPEN_DIMENSION_MAX}
    points = sum(scores[k] for k in OPEN_DIMENSION_MAX)         # 0..100
    composite = points / float(OPEN_TOTAL_MAX)                  # 0..1

    per_dim_reason = payload.get("per_dimension_reasoning") or {}
    per_dim_reason = {k: str(per_dim_reason.get(k, "") or "") for k in OPEN_DIMENSION_MAX}

    return GoldRubricResult(
        candidate=candidate,
        matched_gold_id="",
        matched_centrality="open",
        matched_gold_question="",
        scores=scores,
        composite_score=composite,
        composite_score_raw=points,
        weights=dict(OPEN_DIMENSION_MAX),
        gold_matched=False,
        is_open=True,
        rubric_kind="open",
        per_dimension_reasoning=per_dim_reason,
        rationale=str(payload.get("rationale", "") or ""),
        passed=composite >= threshold,
        threshold=threshold,
        primary_available=False,
        rubric_anchors=OPEN_DIMENSION_ANCHORS,
    )
