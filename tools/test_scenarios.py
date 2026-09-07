#!/usr/bin/env python3
"""Checks on the scenario loader.

    python3 tools/test_scenarios.py

No test framework, so it runs anywhere python3 does, including in a hook or
in CI without an install step.

These exist because the first version of the loader silently accepted broken
input: a `---` horizontal rule became a bullet on a printed card, and a
misspelled section heading produced a card with an empty half that nothing
complained about until somebody printed it.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scenarios  # noqa: E402

FAILURES = []


def check(label, condition):
    print(("  ok   " if condition else "  FAIL ") + label)
    if not condition:
        FAILURES.append(label)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def write(path, text, newline=None):
    with open(path, "w", encoding="utf-8", newline=newline) as fh:
        fh.write(text)


def check_raises(label, path, mutate):
    """Corrupt one source file, confirm the loader refuses it, put it back."""
    original = read(path)
    try:
        write(path, mutate(original))
        try:
            scenarios.load()
            check(label, False)
        except ValueError:
            check(label, True)
    finally:
        write(path, original)


def main():
    all_of_them = scenarios.load()
    sample = os.path.join(scenarios.SRC, "never-happens.md")

    print("Loading")
    check("every scenario parses", len(all_of_them) > 0)
    check("each has a situation", all(s["situation"] for s in all_of_them))
    check("each has questions", all(s["questions"] for s in all_of_them))
    check("each has think about points", all(s["think_about"] for s in all_of_them))
    check("no bullet is only punctuation",
          not [v for s in all_of_them for k in ("questions", "think_about")
               for v in s[k] if set(v.strip()) <= set("-*")])
    check("difficulty is always 1 to 3", all(s["difficulty"] in scenarios.DIFFICULTY for s in all_of_them))
    check("sectors are all known",
          all(x in scenarios.SECTORS for s in all_of_them for x in s["sectors"]))
    check("slugs are unique", len({s["slug"] for s in all_of_them}) == len(all_of_them))

    print("Bullet parsing")
    check("a horizontal rule is not a bullet",
          scenarios._bullets("- real\n\n---\n\n* also real") == ["real", "also real"])
    check("an em rule is not a bullet", scenarios._bullets("----") == [])

    print("Rejecting broken input")
    check_raises("misspelled section heading", sample,
                 lambda s: s.replace("## Think about", "## Things to think about"))
    check_raises("difficulty out of range", sample,
                 lambda s: s.replace("difficulty: 1", "difficulty: 7"))
    check_raises("unknown sector", sample,
                 lambda s: s.replace("small-team]", "government]"))
    check_raises("unknown category", sample,
                 lambda s: s.replace("category: governance", "category: misc"))
    check_raises("missing front matter", sample, lambda s: s.split("---", 2)[2])
    check_raises("sectors written as a bare string", sample,
                 lambda s: s.replace("sectors: [open-source, charity, corporate, small-team]",
                                     "sectors: charity"))

    print("Line endings")
    original = read(sample)
    try:
        write(sample, original.replace("\n", "\r\n"), newline="")
        try:
            scenarios.load()
            check("a CRLF source file still parses", True)
        except ValueError:
            check("a CRLF source file still parses", False)
    finally:
        write(sample, original, newline="")

    print()
    if FAILURES:
        print(f"{len(FAILURES)} failed")
        return 1
    print(f"All checks passed across {len(all_of_them)} scenarios.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
