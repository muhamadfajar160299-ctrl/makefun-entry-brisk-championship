"""One-line excuse entry: copy entry.txt verbatim to the output directory.

The entry line lives in entry.txt next to this script. This program reads
it and writes it unchanged to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt), so the grader sees exactly the submitted line.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as f:
            text = f.read()
    except OSError as exc:
        print(f"cannot read entry.txt: {exc}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry.txt is empty or whitespace only", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(text)
    except OSError as exc:
        print(f"cannot write output: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
