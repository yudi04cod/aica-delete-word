#!/usr/bin/env python3
"""Aica Delete Word — make.fun entry.

Writes the one word to erase from the dictionary to /output/entry.txt.
Deterministic, standard library only, no network, no randomness.
"""

import os

WORD = "irregardless"  # A word that argues it isn't a word: ir- + -less cancel each other out.


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
