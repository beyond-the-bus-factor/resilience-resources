#!/usr/bin/env python3
"""Checks that check_docs.py actually catches things.

    python3 tools/test_check_docs.py

A checker that always passes is worse than no checker, because it buys
confidence it has not earned. Each case below builds a small tree of
deliberately broken markdown, points the checker at it, and confirms it
complains. The last case builds a correct tree and confirms it stays quiet,
so a checker that complained about everything would fail too.
"""

import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import check_docs  # noqa: E402
import scenarios  # noqa: E402

FAILURES = []

GOOD_OVERLAYS = {
    sector: f'---\nsector: {sector}\ntitle: "T"\nsummary: "S"\n---\n\n# Heading here\n'
    for sector in scenarios.SECTORS
}


def build(tmp, files, overlays=None):
    """Write a fixture tree: a correct set of overlays plus whatever is given."""
    overlays = GOOD_OVERLAYS if overlays is None else overlays
    os.makedirs(os.path.join(tmp, "resources", "sectors"), exist_ok=True)
    for sector, body in overlays.items():
        name = {"open-source": "open-source", "charity": "charity-ngo",
                "corporate": "company", "small-team": "small-team"}[sector]
        with open(os.path.join(tmp, "resources", "sectors", f"{name}.md"), "w", encoding="utf-8") as fh:
            fh.write(body)
    for relpath, body in files.items():
        full = os.path.join(tmp, relpath)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as fh:
            fh.write(body)


def run(files, overlays=None):
    """Run every check against a fixture tree and return what it said."""
    tmp = tempfile.mkdtemp()
    real_root = check_docs.ROOT
    try:
        build(tmp, files, overlays)
        check_docs.ROOT = tmp
        check_docs.PROBLEMS.clear()
        for _, fn in check_docs.CHECKS:
            fn()
        return list(check_docs.PROBLEMS)
    finally:
        check_docs.ROOT = real_root
        check_docs.PROBLEMS.clear()
        shutil.rmtree(tmp)


def catches(label, files, needle, overlays=None):
    found = run(files, overlays)
    hit = any(needle in p for p in found)
    print(("  ok   " if hit else "  FAIL ") + label)
    if not hit:
        FAILURES.append(label)
        print(f"         expected something containing {needle!r}")
        print(f"         got: {found or 'nothing'}")


def main():
    print("Catches broken content")

    catches("a link to a file that does not exist",
            {"a.md": "See [the guide](missing-file.md).\n"},
            "does not exist")

    catches("a link to an anchor the target does not have",
            {"a.md": "See [it](b.md#not-there).\n", "b.md": "# Something else\n"},
            "does not have")

    catches("a link to an anchor in the same file that does not exist",
            {"a.md": "# Real heading\n\nSee [it](#imaginary-heading).\n"},
            "not in this file")

    catches("a table row with the wrong number of cells",
            {"a.md": "| A | B |\n|---|---|\n| 1 | 2 |\n| 1 | 2 | 3 |\n"},
            "table row has")

    catches("a link to a scenario that does not exist",
            {"a.md": "See [that one](resources/scenarios/no-such-scenario.md).\n",
             "resources/scenarios/no-such-scenario.md": "# x\n"},
            "does not exist")

    catches("a banned word",
            {"a.md": "This is quietly a problem.\n"},
            "'quietly'")

    catches("an em dash",
            {"a.md": "This one uses an em dash — like that.\n"},
            "em dash")

    catches("a scenario count that is out of date",
            {"a.md": "There are fifteen scenarios in the deck.\n"},
            "but there are")

    catches("a numeric scenario count that is out of date",
            {"a.md": "All 15 scenarios are listed.\n"},
            "but there are")

    print("Reports accurately")

    escaped = run({"a.md": "| A | B |\n|---|---|\n| one \\| two | x |\n"})
    print(("  ok   " if not escaped else "  FAIL ") +
          "an escaped pipe in a cell is content, not a separator")
    if escaped:
        FAILURES.append("escaped pipe")
        for e in escaped:
            print(f"         unexpected: {e}")

    numbered = run({"a.md": "# T\n\n```\nfenced\ncode\nblock\n```\n\nA line with an em dash \u2014 here.\n"})
    print(("  ok   " if any("line 9" in p for p in numbered) else "  FAIL ") +
          "line numbers survive code blocks being stripped")
    if not any("line 9" in p for p in numbered):
        FAILURES.append("line numbers")
        print(f"         expected line 9, got: {numbered or 'nothing'}")

    small = run({"a.md": "Give each group two cards, then swap after ten minutes.\n"})
    print(("  ok   " if not small else "  FAIL ") +
          "a small count of cards in facilitation prose is not a stale deck size")
    if small:
        FAILURES.append("card count false positive")
        for e in small:
            print(f"         unexpected: {e}")

    print("Catches sector overlay drift")

    missing = {s: b for s, b in GOOD_OVERLAYS.items() if s != "charity"}
    catches("a sector with no overlay", {}, "no overlay for sector 'charity'", overlays=missing)

    wrong = dict(GOOD_OVERLAYS)
    wrong["charity"] = '---\nsector: nonprofit\ntitle: "T"\nsummary: "S"\n---\n\n# H\n'
    catches("an overlay naming a sector outside the taxonomy", {}, "is not in the taxonomy", overlays=wrong)

    blank = dict(GOOD_OVERLAYS)
    blank["charity"] = '---\nsector: charity\ntitle: ""\nsummary: "S"\n---\n\n# H\n'
    catches("an overlay with an empty title", {}, "title is missing or empty", overlays=blank)

    nofm = dict(GOOD_OVERLAYS)
    nofm["charity"] = "# Just a heading, no front matter\n"
    catches("an overlay with no front matter", {}, "missing front matter", overlays=nofm)

    print("Stays quiet on correct content")
    clean = run({
        "a.md": "# Title\n\nSee [b](b.md) and [the part](b.md#a-real-heading).\n\n"
                "| A | B |\n|---|---|\n| 1 | 2 |\n",
        "b.md": "# B\n\n## A real heading\n\nNothing wrong here.\n",
    })
    print(("  ok   " if not clean else "  FAIL ") + "a correct tree produces no complaints")
    if clean:
        FAILURES.append("clean tree")
        for p in clean:
            print(f"         unexpected: {p}")

    print()
    if FAILURES:
        print(f"{len(FAILURES)} failed")
        return 1
    print("check_docs.py catches every fault it claims to.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
