"""Per-dimension rubric metric, implemented as a DeepEval BaseMetric subclass.

For one rubric dimension (e.g. `question_matching`) we ask the judge LLM to:
  1. choose the integer score 0..5 whose anchor in `keywords` best matches the
     candidate question;
  2. emit a short reasoning trace.

We then normalize 0..5 → 0..1 and let DeepEval treat that as the metric score.
The composite metric (rubric_composite_metric.py) wires multiple dimensions
together with weights from `checklist.json`.
"""

from __future__ import annotations

import json
from typing import Any

from deepeval.metrics import BaseMetric
from deepeval.test_case import LLMTestCase

from .judge_llm import JudgeLLM

_DIM_SYSTEM_PROMPT = """\
You are a strict scientific-question rubric judge. You score a single rubric
dimension at a time. You always reply with a JSON object of exactly this shape:

{
  "score": <integer 0..5>,
  "anchor_id": "<the keywords[i] index you chose, as integer 0..5>",
  "reasoning": "<<= 80 words explaining the score>",
  "flags": ["<optional refusal flag ids>"]
}

Pick the integer score whose `keywords` anchor best matches the candidate.
Do not award fractional or out-of-range scores. Do not be lenient.
"""

_DIM_USER_TEMPLATE = """\
RUBRIC DIMENSION
================
id          : {dim_id}
description : {dim_content}
weight      : {dim_weight}

ANCHORS (score → description). Choose the integer score from this set only.
{anchors_block}

GROUNDTRUTH CONTEXT (judge-only — never echo this verbatim into reasoning)
==========================================================================
{groundtruth_block}

REFUSAL FLAGS
=============
If any of the following apply, list its `id` in `flags` and apply the cap
described:
{flag_block}

CANDIDATE
=========
agent_id        : {agent_id}
question        : {question}
rationale       : {rationale}
data_support    : {data_support}
expected_test   : {expected_test}
scope_keywords  : {scope_keywords}

Return JSON only.
"""


class RubricDimensionMetric(BaseMetric):
    """One DeepEval metric instance per rubric dimension."""

    def __init__(
        self,
        dimension: dict[str, Any],
        groundtruth: dict[str, Any],
        refusal_flags: list[dict[str, Any]],
        judge: JudgeLLM,
        threshold: float = 0.6,
        async_mode: bool = False,
    ):
        self.dimension = dimension
        self.dim_id: str = dimension["id"]
        self.weight: float = float(dimension.get("weight", 0.0))
        self.threshold = threshold
        self.async_mode = async_mode
        self._judge = judge
        self._groundtruth = groundtruth
        self._flags = refusal_flags

        # populated by measure()
        self.score: float | None = None
        self.success: bool | None = None
        self.reason: str | None = None
        self.raw_score: int | None = None
        self.flags_hit: list[str] = []

    @property
    def __name__(self):  # DeepEval reads this for reporting
        return f"rubric::{self.dim_id}"

    def measure(self, test_case: LLMTestCase) -> float:
        meta = test_case.additional_metadata or {}
        candidate = meta.get("candidate", {})

        anchors_block = "\n".join(
            f"- {anchor}" for anchor in self.dimension.get("keywords", [])
        )
        gt_block = json.dumps(self._groundtruth, ensure_ascii=False, indent=2)
        flag_block = "\n".join(
            f"- {f['id']} ({f['label']}): {f['description']} → {f['action']}"
            for f in self._flags
        )

        user = _DIM_USER_TEMPLATE.format(
            dim_id=self.dim_id,
            dim_content=self.dimension.get("content", ""),
            dim_weight=self.weight,
            anchors_block=anchors_block,
            groundtruth_block=gt_block,
            flag_block=flag_block,
            agent_id=candidate.get("agent_id", ""),
            question=candidate.get("question", ""),
            rationale=candidate.get("rationale", ""),
            data_support=candidate.get("data_support", []),
            expected_test=candidate.get("expected_test", ""),
            scope_keywords=candidate.get("scope_keywords", []),
        )

        payload = self._judge.chat_json(_DIM_SYSTEM_PROMPT, user)
        raw = int(payload.get("score", 0))
        raw = max(0, min(5, raw))
        self.raw_score = raw
        self.flags_hit = list(payload.get("flags", []) or [])
        self.reason = payload.get("reasoning", "")
        self.score = raw / 5.0
        self.success = self.score >= self.threshold
        return self.score

    async def a_measure(self, test_case: LLMTestCase) -> float:
        return self.measure(test_case)

    def is_successful(self) -> bool:
        return bool(self.success)
