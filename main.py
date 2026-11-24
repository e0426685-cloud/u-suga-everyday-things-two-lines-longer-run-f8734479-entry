"""Write the two-line everyday-thing explanation to /output/entry.txt.

Stdlib only, deterministic. The entry explains a traffic jam to a
10-year-old with a frozen-river analogy, then says honestly what the
analogy maps and what it leaves out.
"""

import os

ENTRY_LINES = [
    "A traffic jam is like a river of cars frozen into a parking lot, "
    "where every driver is a fish stuck in the ice, waiting for the "
    "thaw when the car ahead moves.",
    "The frozen-river picture works because it shows many cars locked "
    "together by one slow spot, but it leaves out that drivers can "
    "turn off, honk, or give up and walk, which ice never does.",
]


def main() -> None:
    text = "\n".join(ENTRY_LINES) + "\n"
    # Guard the competition's own shape rules before writing.
    body = text.rstrip("\n")
    assert body.count("\n") == 1, "entry must be exactly two lines"
    assert 1 <= len(body) <= 400, "entry must be 1-400 characters"
    assert body.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
