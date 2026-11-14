#!/usr/bin/env python3
"""Entry program for make.fun news-image-01 (v3, six-panel grid).

Copies the pre-rendered entry image (entry.png, in this directory) to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
Standard library only; no network, no rendering at run time.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit("entry.png missing next to main.py")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Guard against a truncated copy: the output must be the source,
    # byte for byte.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("copied entry.png has the wrong size")
    print("wrote", dst)


if __name__ == "__main__":
    sys.exit(main())
