"""Schema-less data ZIP validator.

The user uploads ANY data archive — we don't enforce a particular schema.
We unzip safely, build a file tree summary, and surface basic statistics
that the agent prompt can later reference (file count, total size, file
types, sample columns for tabular files, etc.).
"""

from __future__ import annotations

import csv
import io
import json
import shutil
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


# files we'll peek into to extract column / record info
_TEXT_LIKE_EXT = (".tsv", ".csv", ".txt", ".md", ".json", ".jsonl", ".faa", ".fasta", ".fa", ".gff", ".bed", ".log")


@dataclass
class FileNode:
    path: str            # relative to data root
    size_bytes: int
    kind: str            # "file" or "dir"
    sample: dict[str, Any] = field(default_factory=dict)

    def to_json(self) -> dict[str, Any]:
        return {"path": self.path, "size_bytes": self.size_bytes, "kind": self.kind, "sample": self.sample}


@dataclass
class DataReport:
    ok: bool
    extracted_to: str
    data_root: str
    file_count: int = 0
    valid_file_count: int = 0
    total_size_bytes: int = 0
    extension_histogram: dict[str, int] = field(default_factory=dict)
    files: list[FileNode] = field(default_factory=list)   # capped to 200
    truncated: bool = False
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def to_json(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "extracted_to": self.extracted_to,
            "data_root": self.data_root,
            "file_count": self.file_count,
            "valid_file_count": self.valid_file_count,
            "total_size_bytes": self.total_size_bytes,
            "extension_histogram": self.extension_histogram,
            "files": [f.to_json() for f in self.files],
            "truncated": self.truncated,
            "errors": self.errors,
            "warnings": self.warnings,
        }


class DataValidationError(Exception):
    pass


def validate_data_zip(zip_path: Path, target_dir: Path) -> DataReport:
    """Extract `zip_path` into `target_dir/data/` and return a tree summary."""
    zip_path = Path(zip_path)
    target_dir = Path(target_dir).resolve()
    if target_dir.exists():
        shutil.rmtree(target_dir)
    target_dir.mkdir(parents=True)
    data_root = target_dir / "data"
    data_root.mkdir()

    if not zipfile.is_zipfile(zip_path):
        raise DataValidationError(f"Not a valid ZIP archive: {zip_path.name}")
    with zipfile.ZipFile(zip_path) as zf:
        bad = [n for n in zf.namelist() if ".." in n or n.startswith("/")]
        if bad:
            raise DataValidationError(f"Unsafe entries in ZIP: {bad[:3]}")
        zf.extractall(data_root)

    # If the ZIP wraps everything inside a single top-level folder, hoist its
    # contents up so `data/` is the actual data root.
    children = [c for c in data_root.iterdir() if not c.name.startswith("__MACOSX")]
    if len(children) == 1 and children[0].is_dir():
        only = children[0]
        for entry in list(only.iterdir()):
            shutil.move(str(entry), data_root / entry.name)
        shutil.rmtree(only)

    return _summarise(target_dir, data_root)


def _summarise(target_dir: Path, data_root: Path) -> DataReport:
    report = DataReport(
        ok=True,
        extracted_to=str(target_dir),
        data_root=str(data_root),
    )

    all_files: list[Path] = sorted(p for p in data_root.rglob("*") if p.is_file() and "__MACOSX" not in p.parts)
    report.file_count = len(all_files)
    report.total_size_bytes = sum(p.stat().st_size for p in all_files)

    if report.file_count == 0:
        report.ok = False
        report.errors.append("ZIP contained no files.")
        return report

    for p in all_files:
        ext = p.suffix.lower() or "(noext)"
        report.extension_histogram[ext] = report.extension_histogram.get(ext, 0) + 1

    # cap nodes
    cap = 200
    for p in all_files[:cap]:
        rel = str(p.relative_to(data_root))
        node = FileNode(path=rel, size_bytes=p.stat().st_size, kind="file")
        node.sample = _sample(p)
        report.files.append(node)
    if len(all_files) > cap:
        report.truncated = True
        report.warnings.append(f"file list truncated at {cap} (total {len(all_files)})")

    _check_validity(report)
    return report


def _check_validity(report: DataReport) -> None:
    """Flag files that are unlikely to carry usable signal.

    Non-fatal by default (recorded as warnings) so a partly-malformed upload can
    still run, but the operator sees exactly which files are empty, unparseable,
    or content-free. If EVERY sampled file is invalid the upload is rejected.
    """
    invalid: list[str] = []
    for node in report.files:
        reason = None
        if node.size_bytes == 0:
            reason = "empty file (0 bytes)"
        else:
            s = node.sample
            if s.get("parse_error") or s.get("sample_error"):
                reason = f"unparseable ({s.get('parse_error') or s.get('sample_error')})"
            elif "sample_rows" in s and s["sample_rows"] <= 1:
                reason = "tabular file has a header but no data rows"
            elif "sequence_count" in s and s["sequence_count"] == 0:
                reason = "FASTA file contains no sequences"
            elif s.get("array_len") == 0:
                reason = "JSON array is empty"
        node.sample["valid"] = reason is None
        if reason is not None:
            node.sample["validity_issue"] = reason
            invalid.append(f"{node.path}: {reason}")

    report.valid_file_count = sum(1 for n in report.files if n.sample.get("valid", True))
    if invalid:
        report.warnings.append(
            f"{len(invalid)} file(s) failed validity checks: " + "; ".join(invalid[:10])
            + (" …" if len(invalid) > 10 else "")
        )
    # Reject only if nothing usable survived.
    if report.files and report.valid_file_count == 0:
        report.ok = False
        report.errors.append("no valid data files: every uploaded file is empty or unparseable.")


def _sample(path: Path) -> dict[str, Any]:
    """Return a small sample dict for the file (columns, first-line, count)."""
    ext = path.suffix.lower()
    info: dict[str, Any] = {}
    if ext not in _TEXT_LIKE_EXT or path.stat().st_size > 4 * 1024 * 1024:
        return info
    try:
        head = path.read_bytes()[: 200_000].decode("utf-8", errors="replace")
    except Exception:
        return info

    if ext == ".tsv" or ext == ".csv":
        try:
            reader = csv.reader(io.StringIO(head), delimiter="\t" if ext == ".tsv" else ",")
            cols = next(reader)
            info["columns"] = cols
            rows = sum(1 for _ in reader)
            info["sample_rows"] = rows + 1  # include header in sample
        except Exception as e:
            info["sample_error"] = str(e)[:100]
    elif ext in (".faa", ".fasta", ".fa"):
        info["sequence_count"] = head.count(">")
        first = next((ln for ln in head.splitlines() if ln.startswith(">")), "")
        if first:
            info["first_header"] = first[:120]
    elif ext == ".jsonl":
        info["line_count"] = head.count("\n")
    elif ext == ".json":
        try:
            obj = json.loads(head)
            if isinstance(obj, dict):
                info["top_keys"] = list(obj.keys())[:12]
            elif isinstance(obj, list):
                info["array_len"] = len(obj)
        except Exception:
            info["parse_error"] = "truncated/invalid JSON in sample"
    elif ext in (".md", ".txt", ".log"):
        info["line_count"] = head.count("\n") + 1
        info["preview"] = head[:200]
    return info
