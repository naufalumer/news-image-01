#!/usr/bin/env python3
"""news-image-01 entry point.

Copies the pre-rendered front page (entry.png, sitting beside this file)
to the output directory as entry.png. Standard library only, so it runs in
the grading sandbox with no network and no third-party packages.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        print("entry.png not found beside main.py", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote " + dst)


if __name__ == "__main__":
    sys.exit(main())
