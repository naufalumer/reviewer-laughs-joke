"""the-joke-the-reviewer-laughs-at-20261121-0329 entry: write one fixed joke
about working beside AI coding agents to /output/entry.txt.

Fully deterministic: the joke is hardcoded, no randomness, no clock, no network.
Run outside the grader container with MAKEFUN_OUTPUT_DIR set, e.g.
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# The joke is a literal on purpose: the grader runs the program twice and
# both runs must write the same bytes, and the judge reads exactly the
# bytes in entry.txt, so nothing here may vary (no randomness, no clock).
# The joke itself: setup asks for a small PR, punchline escalates to 14 PRs
# that each claim to be "part 1 of 1" -- a surprise the reviewer of the
# change recognises at once, in one line, with nothing explained.
JOKE = (
    "I asked my agent to keep the PR small. It split it into 14 PRs, "
    "each one titled 'part 1 of 1'."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
