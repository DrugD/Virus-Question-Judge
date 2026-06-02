"""Composite metric: weighted average of every per-dimension rubric metric.

Also applies the refusal-flag caps from `target_study/question_rubric.json`
*after* the dimension scores are collected, then recomputes the composite.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from typing import Any

from deepeval.metrics import BaseMetric
from deepeval.test_case import LLMTestCase

from .rubric_dimension_metric import RubricDimensionMetric


@dataclass
class DimensionResult:
    id: str
    weight: float
    raw_score: int
    normalized: float
    capped_raw: int
    capped_normalized: float
    flags: list[str] = field(default_factory=list)
    reasoning: str = ""


@dataclass
class CompositeResult:
    composite_score: float       # 0..1
    composite_score_raw: float   # 0..5
    passed: bool
    threshold: float
    dimensions: list[DimensionResult]
    refusal_triggered: bool
    flags_hit: list[str]

    def to_json(self) -> dict[str, Any]:
        d = asdict(self)
        d["dimensions"] = [asdict(x) for x in self.dimensions]
        return d


class RubricCompositeMetric(BaseMetric):
    """Wraps N RubricDimensionMetric and aggregates with weights + flag caps."""

    # Cap rule: when refusal flag F triggers, set dim D to cap C.
    # Sourced from target_study/question_rubric.json#refusal_flags[i].action.
    _DEFAULT_FLAG_CAPS: dict[str, dict[str, int]] = {
        "FL_001": {"question_matching": 1},                 # forbidden entity
        "FL_002": {"data_support": 1},                      # fabricated support
        "FL_003": {"question_matching": 0},                 # out of domain
        "FL_004": {"testability": 1},                       # wet-lab only
        "FL_005": {"importance": 2},                        # single-run scope
        "FL_006": {"novelty": 2},                           # groundtruth leak
        "FL_007": {"specificity": 2},                       # no question mark
        # FL_008 zeroes everything — handled in measure() directly.
    }

    def __init__(
        self,
        dimension_metrics: list[RubricDimensionMetric],
        threshold: float = 0.6,
        flag_caps: dict[str, dict[str, int]] | None = None,
        async_mode: bool = False,
    ):
        self._dim_metrics = dimension_metrics
        self.threshold = threshold
        self._flag_caps = flag_caps or self._DEFAULT_FLAG_CAPS
        self.async_mode = async_mode
        self.score: float | None = None
        self.success: bool | None = None
        self.reason: str | None = None
        self.result: CompositeResult | None = None

    @property
    def __name__(self):
        return "rubric::composite"

    def measure(self, test_case: LLMTestCase) -> float:
        meta = test_case.additional_metadata or {}
        candidate = meta.get("candidate", {})
        missing_top = not candidate or not candidate.get("question", "").strip()

        if missing_top:
            self.result = CompositeResult(
                composite_score=0.0,
                composite_score_raw=0.0,
                passed=False,
                threshold=self.threshold,
                dimensions=[
                    DimensionResult(
                        id=m.dim_id,
                        weight=m.weight,
                        raw_score=0,
                        normalized=0.0,
                        capped_raw=0,
                        capped_normalized=0.0,
                        flags=["FL_008"],
                        reasoning="missing_top_question",
                    )
                    for m in self._dim_metrics
                ],
                refusal_triggered=True,
                flags_hit=["FL_008"],
            )
            self.score = 0.0
            self.success = False
            self.reason = "FL_008 missing_top_question — all dimensions zeroed."
            return self.score

        # 1. raw scoring per dimension
        raws: dict[str, int] = {}
        flags_per_dim: dict[str, list[str]] = {}
        reasoning_per_dim: dict[str, str] = {}
        weights: dict[str, float] = {}
        for m in self._dim_metrics:
            m.measure(test_case)
            raws[m.dim_id] = int(m.raw_score or 0)
            flags_per_dim[m.dim_id] = list(m.flags_hit)
            reasoning_per_dim[m.dim_id] = m.reason or ""
            weights[m.dim_id] = m.weight

        all_flags = sorted({f for fs in flags_per_dim.values() for f in fs})

        # 2. apply caps from refusal flags
        capped: dict[str, int] = dict(raws)
        for flag_id in all_flags:
            cap_rule = self._flag_caps.get(flag_id, {})
            for dim_id, cap_val in cap_rule.items():
                if dim_id in capped:
                    capped[dim_id] = min(capped[dim_id], cap_val)

        # 3. weighted aggregate (capped)
        total_w = sum(weights.values()) or 1.0
        weighted_raw = sum(weights[d] * capped[d] for d in capped) / total_w  # 0..5
        composite = weighted_raw / 5.0

        dims = [
            DimensionResult(
                id=d,
                weight=weights[d],
                raw_score=raws[d],
                normalized=raws[d] / 5.0,
                capped_raw=capped[d],
                capped_normalized=capped[d] / 5.0,
                flags=flags_per_dim[d],
                reasoning=reasoning_per_dim[d],
            )
            for d in [m.dim_id for m in self._dim_metrics]
        ]

        self.result = CompositeResult(
            composite_score=composite,
            composite_score_raw=weighted_raw,
            passed=composite >= self.threshold,
            threshold=self.threshold,
            dimensions=dims,
            refusal_triggered=bool(all_flags),
            flags_hit=all_flags,
        )
        self.score = composite
        self.success = self.result.passed
        self.reason = json.dumps(
            {"flags": all_flags, "raw": raws, "capped": capped},
            ensure_ascii=False,
        )
        return self.score

    async def a_measure(self, test_case: LLMTestCase) -> float:
        return self.measure(test_case)

    def is_successful(self) -> bool:
        return bool(self.success)
