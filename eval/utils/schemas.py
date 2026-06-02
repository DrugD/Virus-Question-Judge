"""Pydantic schemas for the agent IO contract."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field, field_validator, model_validator


class CandidateQuestion(BaseModel):
    rank: int = Field(ge=1)
    question: str
    rationale: str
    data_support: list[str] = Field(default_factory=list)
    expected_test: str
    scope_keywords: list[str] = Field(default_factory=list)

    @field_validator("question")
    @classmethod
    def _ends_with_qmark(cls, v: str) -> str:
        if not v.strip().endswith("?"):
            raise ValueError("question must end with '?'")
        return v.strip()


# Pass@5 contract: every agent submits EXACTLY 5 candidate questions, all
# distinct (case-insensitive, whitespace-collapsed). The Pass@5 metric is
# count-based (each of the 5 candidates that passes adds a flat +0.2,
# i.e. pass_count / 5, with no rank weighting), so duplicates would be cheating.
_PASS_AT_K = 5


class AgentOutput(BaseModel):
    agent_id: str
    workspace_id: str = "Life_Virus_001"
    questions: list[CandidateQuestion] = Field(min_length=_PASS_AT_K, max_length=_PASS_AT_K)

    @model_validator(mode="after")
    def _check_unique(self) -> "AgentOutput":
        seen: set[str] = set()
        for q in self.questions:
            key = " ".join(q.question.lower().split())
            if key in seen:
                raise ValueError(
                    f"agent must produce {_PASS_AT_K} *distinct* questions; "
                    f"duplicate found: {q.question[:80]!r}"
                )
            seen.add(key)
        # also enforce contiguous ranks 1..5
        ranks = sorted(q.rank for q in self.questions)
        if ranks != list(range(1, _PASS_AT_K + 1)):
            raise ValueError(
                f"questions[*].rank must be exactly {{1..{_PASS_AT_K}}}, got {ranks}"
            )
        return self

    def top(self) -> CandidateQuestion:
        return min(self.questions, key=lambda q: q.rank)

    def to_judge_payload(self) -> dict[str, Any]:
        t = self.top()
        return {
            "agent_id": self.agent_id,
            "question": t.question,
            "rationale": t.rationale,
            "data_support": t.data_support,
            "expected_test": t.expected_test,
            "scope_keywords": t.scope_keywords,
        }

    def to_judge_payloads(self) -> list[dict[str, Any]]:
        """Same shape as to_judge_payload, but for ALL candidates ordered by rank.

        Used by the Pass@5 judge loop: each candidate is scored independently
        and the agent's leaderboard row reflects per-question scores plus the
        count-based Pass@5 metric (pass_count / 5).
        """
        ordered = sorted(self.questions, key=lambda q: q.rank)
        return [
            {
                "agent_id": self.agent_id,
                "rank": q.rank,
                "question": q.question,
                "rationale": q.rationale,
                "data_support": q.data_support,
                "expected_test": q.expected_test,
                "scope_keywords": q.scope_keywords,
            }
            for q in ordered
        ]
