#!/usr/bin/env python3
"""news-image-20261120: copy the pre-rendered front page to /output/entry.png.

The image is a 1024x1024 PNG of Friday 20 November 2026's world news,
drawn from 28 stories first reported that day (see NEWS-RESEARCH.md in the
build directory and the README). This program only copies the file the
repository holds; it needs no network and writes identical bytes on
every run.
"""
import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # The gate requires a whole PNG of at most 1 MiB; refuse to hand over
    # anything bigger instead of silently writing it.
    if os.path.getsize(dst) > 1048576:
        os.remove(dst)
        raise SystemExit("entry.png exceeds 1 MiB")


if __name__ == "__main__":
    main()
