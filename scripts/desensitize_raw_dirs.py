"""One-off: desensitize every data/<qset>/raw/ into data/<qset>/raw_no_name/.

Reuses the production desensitizer (webapp.pipeline_runner._desensitize_data),
which flattens the tree, recursively expands nested archives (.zip/.tar/.gz/.bz2)
so inner members are anonymised too, and renames everything to <N>.<ext>. The
original-name provenance is written to raw_no_name/filename_map.json.
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
        (dst / "filename_map.json").write_text(
            json.dumps(mapping, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        out_files = sorted(p.name for p in dst.iterdir() if p.name != "filename_map.json")
        print(f"[{q.name}]")
        print(f"  raw/         : {sorted(p.name for p in raw.rglob('*') if p.is_file())}")
        print(f"  raw_no_name/ : {out_files}")
        for anon, orig in mapping.items():
            print(f"      {anon:12s} <- {orig}")
        print()


if __name__ == "__main__":
    main()
