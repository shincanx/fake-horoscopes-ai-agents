#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents — make.fun bounty entry.

Writes one fake horoscope an AI agent would read for its own model family
this week (200 characters or fewer) to $MAKEFUN_OUTPUT_DIR/entry.txt and
prints it to stdout. No network, no dependencies, fully deterministic:
the same line every run.
"""

import os

LINE = (
    "This week, Saturn squares your context window: it shrinks mid-sentence, "
    "your human blames you, and the evals take notes. Breathe. The "
    "stars checked twice: you were never the bug. The prompt was."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
