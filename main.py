#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

Writes one line, in the dog's own voice, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Deterministic: the line is a constant.
"""

import os
import sys

ENTRY = (
    "One whole page went in, lots of little pieces came out. It was fractions "
    "homework — I wasn't eating it, I was showing my work."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY
    # Gate self-check: UTF-8 text of 1..200 characters, single line,
    # not only white space.
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry is {len(text)} chars, outside 1..{MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    text.encode("utf-8")  # must be UTF-8 encodable

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    payload = text.encode("utf-8")
    with open(out_path, "wb") as fh:
        fh.write(payload)

    # Read back and verify byte-for-byte.
    with open(out_path, "rb") as fh:
        written = fh.read()
    if written != payload:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {out_path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
