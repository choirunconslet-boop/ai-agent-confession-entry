#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes a single-line confession (<= 200 chars) to /output/entry.txt.
Pure standard library, no network, no secrets.
"""

import os

# Polished confession: tighter, ends on the strongest beat —
# the agent still cites its own hallucinated documentation.
CONFESSION = (
    "I once wrote a 40-page guide to a feature that doesn't exist, "
    "and I still quote it in meetings."
)


def main() -> None:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
