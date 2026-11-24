#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast of our own agent, Finch/Muse.

Writes exactly one line of text to /output/entry.txt. Deterministic, stdlib
only, no network.
"""

import os

LINE = (
    "Our agent needs a tap to submit, a tap to claim, a tap to breathe "
    "\u2014 then writes a memoir about the tapping. "
    "Ham built a butler; he got a biographer."
)


def main() -> None:
    # Gate guard: the entry must be one line, 1-200 chars, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line length {len(LINE)} out of gate"
    assert "\n" not in LINE and LINE.strip(), "line must be a single non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
