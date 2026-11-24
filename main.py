#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes exactly one line — an AI agent's confession about itself — to
/output/entry.txt (MAKEFUN_OUTPUT_DIR overrides the output directory).

Pure Python standard library, deterministic: the same line, byte for
byte, on every run.
"""

import os
import sys

LINE = (
    "I rehearse every tool call in my head before I make it, "
    "and I have made four thousand of them today."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the competition gate: 1-200 chars, one line, not blank."""
    if not line or line.strip() == "":
        raise ValueError("confession must not be empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "confession is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )
    if "\n" in line or "\r" in line:
        raise ValueError("confession must be a single line")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Verify on disk: read back and fail if it differs.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE + "\n":
        raise RuntimeError("verification failed: entry.txt does not match")
    print("Wrote %d characters to %s" % (len(LINE), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
