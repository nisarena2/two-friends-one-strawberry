#!/usr/bin/env python3
"""Copy the entry image into the output directory."""
import os
import shutil
import sys
from pathlib import Path


def main():
    image = Path(__file__).parent / "entry.png"
    dest = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(image, dest / "entry.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
