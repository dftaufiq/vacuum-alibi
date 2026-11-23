#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters — make.fun entry.

Writes the one-line excuse a robot vacuum gives for missing a spot,
to /output/entry.txt. Deterministic: the same line every run.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-200 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        sys.exit(1)

LINE = (
    "My lidar says the spot is a shadow. My camera says it is a crumb. "
    "They are in mediation, and I do not take sides in sensor disputes."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
