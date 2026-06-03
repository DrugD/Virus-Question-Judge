"""One-off: desensitize every data/<qset>/raw/ into data/<qset>/raw_no_name/.

Reuses the production desensitizer (webapp.pipeline_runner._desensitize_data),
which flattens the tree, recursively expands nested archives (.zip/.tar/.gz/.bz2)
so inner members are anonymised too, and renames everything to <N>.<ext>.

IMPORTANT: the original-name provenance map is written to
data/<qset>/filename_map.json — the QSET ROOT, NEVER inside raw_no_name/. The
whole point of raw_no_name/ is that an agent reading it sees only 1.csv/2.json
style names; a filename_map.json sitting next to them would leak every original
(intent-revealing) filename and defeat the desensitization.
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

from webapp.pipeline_runner import _desensitize_data

DATA = Path("data")


def main() -> None:
    qsets = sorted(p for p in DATA.iterdir() if p.is_dir() and (p / "raw").is_dir())
    print(f"Found {len(qsets)} qsets with raw/\n")
    for q in qsets:
        raw = q / "raw"
        dst = q / "raw_no_name"
        if dst.exists():
            shutil.rmtree(dst)
        mapping = _desensitize_data(raw, dst)
        # judge-only map lives at the qset root, OUTSIDE raw_no_name/, so it is
        # never exposed alongside the anonymised data files.
        (q / "filename_map.json").write_text(
            json.dumps(mapping, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        out_files = sorted(p.name for p in dst.iterdir())
        leak = [n for n in out_files if n == "filename_map.json"]
        print(f"[{q.name}]")
        print(f"  raw/         : {sorted(p.name for p in raw.rglob('*') if p.is_file())}")
        print(f"  raw_no_name/ : {out_files}")
        print(f"  map written  : {q / 'filename_map.json'}  (qset root, judge-only)")
        if leak:
            print(f"  !! LEAK: filename_map.json still inside raw_no_name/ !!")
        print()


if __name__ == "__main__":
    main()

