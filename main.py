#!/usr/bin/env python3
"""make.fun agency-poem-01 entrypoint (stdlib only).

Copies the pre-written entry.txt from the repo root to the output
directory. Deterministic: same bytes every run. No network, no other
files, no model calls. The gate requires 1–1,000 Unicode code points
with at least one non-whitespace character; the poem is 371.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.txt")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Fail loudly instead of silently shipping a truncated copy.
    if os.path.getsize(DST) != os.path.getsize(SRC):
        raise RuntimeError("entry.txt copy size mismatch")


if __name__ == "__main__":
    main()
