"""Validate an uploaded gold-question JSON.

The user-supplied file may be:
  (a) a full JSON object: {"gold_scientific_questions": [...]}
  (b) a bare JSON array: [{...}, {...}]
  (c) a fragment like the gold_question_1.json sample, e.g.

        "gold_scientific_questions": [
          {"gold_question_id": "GQ_001", ...}
        ],

      i.e. neither a wrapping object nor a bare array — just the body.

We accept all three and normalise to:

    {"gold_scientific_questions": [<list of gold questions>]}
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


REQUIRED_KEYS_PER_GQ = (
    "gold_question_id", "question", "required_elements",
    "acceptable_variants", "unacceptable_variants",
)
OPTIONAL_KEYS_PER_GQ = ("question_type", "centrality")


class GoldValidationError(Exception):
    pass


@dataclass
class GoldReport:
    ok: bool
    primary_count: int = 0
    secondary_count: int = 0
    total_count: int = 0
    questions_preview: list[dict[str, Any]] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    normalised_path: str = ""

    def to_json(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "primary_count": self.primary_count,
            "secondary_count": self.secondary_count,
            "total_count": self.total_count,
            "questions_preview": self.questions_preview,
            "errors": self.errors,
            "warnings": self.warnings,
            "normalised_path": self.normalised_path,
        }


def parse_gold(raw: str) -> list[dict[str, Any]]:
    """Try strict JSON first, then a fragment-tolerant fallback.

    Returns the gold_scientific_questions list. Raises GoldValidationError on
    failure.
    """
    txt = raw.strip()

    # Strategy A: full object or bare list
    for candidate in (txt, f"{{{txt.rstrip(',')}}}"):
        try:
            data = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        items = _extract_list(data)
        if items is not None:
            return items

    # Strategy B: tolerate a trailing comma after the closing bracket of the array
    cleaned = re.sub(r",\s*$", "", txt)
    try:
        data = json.loads(f"{{{cleaned}}}")
    except json.JSONDecodeError as e:
        raise GoldValidationError(f"Could not parse gold JSON: {e}")
    items = _extract_list(data)
    if items is None:
        raise GoldValidationError(
            "Parsed JSON did not contain a gold_scientific_questions list."
        )
    return items


def _extract_list(data: Any) -> list[dict[str, Any]] | None:
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in ("gold_scientific_questions", "gold_questions", "questions"):
            v = data.get(key)
            if isinstance(v, list):
                return v
    return None


def validate_gold(path: Path, normalised_out: Path) -> GoldReport:
    """Read `path`, validate, and write a normalised JSON to `normalised_out`."""
    raw = Path(path).read_text(encoding="utf-8")
    report = GoldReport(ok=True)

    try:
        items = parse_gold(raw)
    except GoldValidationError as e:
        return GoldReport(ok=False, errors=[str(e)])

    if not items:
        return GoldReport(ok=False, errors=["gold_scientific_questions is empty."])

    seen_ids: set[str] = set()
    for i, gq in enumerate(items):
        if not isinstance(gq, dict):
            report.errors.append(f"gq #{i} is not an object")
            report.ok = False
            continue
        missing = [k for k in REQUIRED_KEYS_PER_GQ if k not in gq]
        if missing:
            report.errors.append(f"{gq.get('gold_question_id', f'#{i}')}: missing keys {missing}")
            report.ok = False
        gid = gq.get("gold_question_id", "")
        if gid in seen_ids:
            report.warnings.append(f"duplicate gold_question_id: {gid}")
        seen_ids.add(gid)

        if not isinstance(gq.get("required_elements", []), list) or not gq.get("required_elements"):
            report.warnings.append(f"{gid}: required_elements should be a non-empty list")
        for k in ("acceptable_variants", "unacceptable_variants"):
            if not isinstance(gq.get(k, []), list):
                report.warnings.append(f"{gid}: {k} should be a list")

    centralities = [str(gq.get("centrality", "")).lower() for gq in items]
    report.primary_count = sum(1 for c in centralities if c == "primary")
    report.secondary_count = sum(1 for c in centralities if c == "secondary")
    report.total_count = len(items)
    if report.primary_count == 0:
        report.warnings.append(
            "No gold question is marked centrality='primary'; the judge will treat all as equal."
        )

    report.questions_preview = [
        {
            "id": gq.get("gold_question_id"),
            "centrality": gq.get("centrality", ""),
            "type": gq.get("question_type", ""),
            "question": gq.get("question", ""),
            "required_elements_count": len(gq.get("required_elements", []) or []),
        }
        for gq in items[:12]
    ]

    if report.ok:
        # write normalised form
        normalised_out.parent.mkdir(parents=True, exist_ok=True)
        normalised_out.write_text(
            json.dumps({"gold_scientific_questions": items}, ensure_ascii=False, indent=2)
        )
        report.normalised_path = str(normalised_out)
    return report
