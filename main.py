#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

Deterministic, stdlib-only program. Writes one line — a robot vacuum's
deadpan excuse for missing a spot — to /output/entry.txt.
"""

import os

ENTRY = (
    "I scanned that corner three times and my map still says it's a wall. "
    "I don't argue with cartography."
)


def main():
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 140, "entry must be 1-140 characters, got %d" % len(line)
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)


if __name__ == "__main__":
    main()
