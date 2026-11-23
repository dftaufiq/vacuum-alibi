#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters — make.fun entry.

Writes the one-line excuse a robot vacuum gives for missing a spot,
to /output/entry.txt. Deterministic: the same line every run.
"""

import os

LINE = (
    "My lidar says the spot is a shadow. My camera says it is a crumb. "
    "They are in mediation, and I do not take sides in sensor disputes."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
