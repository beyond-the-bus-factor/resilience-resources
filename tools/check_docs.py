#!/usr/bin/env python3
"""Checks across the written resources.

    python3 tools/check_docs.py

Catches the things that break silently in a repository of cross linked
markdown: a link to a file that was renamed, an anchor that no longer
exists, a table whose rows stopped matching its header, a sector overlay
that drifted from the taxonomy the scenario deck uses, and house style.

No dependencies, so it runs anywhere python3 does.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import scenarios  # noqa: E402

SKIP_DIRS = {".git", "node_modules", "_site", "__pycache__"}

# House style. See the project's writing conventions.
BANNED = {
    "quietly": "house style",
    "genuinely": "house style",
    "honest": "house style, including honestly and honesty",
    "—": "em dash",
}

PROBLEMS = []


def problem(path, detail):
    PROBLEMS.append(f"{os.path.relpath(path, ROOT)}: {detail}")


def markdown_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in sorted(filenames):
            if name.endswith(".md"):
                yield os.path.join(dirpath, name)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def strip_code(text):
    """Blank out code so it is not read as prose or as links.

    Replaces content with blank lines rather than deleting it, so that every
    remaining line keeps its original number. Reporting a line number that
    does not match the file is worse than reporting none.
    """
    def blank(m):
        return "\n" * m.group(0).count("\n")
    text = re.sub(r"```.*?```", blank, text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def anchors(text):
    """Heading anchors GitHub would generate, plus any explicit ids."""
    found = set(re.findall(r'<a\s+id="([^"]+)"', text))
    found |= set(re.findall(r'<a\s+name="([^"]+)"', text))
    for line in text.split("\n"):
        m = re.match(r"^#{1,6}\s+(.*\S)\s*$", line)
        if not m:
            continue
        slug = m.group(1).lower()
        slug = re.sub(r"[`*_\[\]()]", "", slug)
        slug = re.sub(r"[^\w\s-]", "", slug)
        slug = re.sub(r"\s+", "-", slug.strip())
        if slug:
            found.add(slug)
    return found


def check_links():
    """Every relative link resolves, and every anchor it names exists."""
    cache = {}
    for path in markdown_files():
        text = strip_code(read(path))
        for label, target in re.findall(r"\[([^\]]*)\]\(([^)\s]+)\)", text):
            if target.startswith(("http://", "https://", "mailto:", "#!")):
                continue
            if target.startswith("#"):
                if target[1:] not in anchors(read(path)):
                    problem(path, f"link '{label}' points at anchor {target}, which is not in this file")
                continue
            file_part, _, anchor = target.partition("#")
            resolved = os.path.normpath(os.path.join(os.path.dirname(path), file_part))
            if not os.path.exists(resolved):
                problem(path, f"link '{label}' points at {target}, which does not exist")
                continue
            if anchor:
                if resolved not in cache:
                    cache[resolved] = anchors(read(resolved))
                if anchor not in cache[resolved]:
                    problem(path, f"link '{label}' points at anchor #{anchor} in {file_part}, "
                                  f"which that file does not have")


def check_tables():
    """Every row of a table has the same number of cells as its header."""
    for path in markdown_files():
        lines = strip_code(read(path)).split("\n")
        header = None
        header_line = 0
        for n, line in enumerate(lines, 1):
            stripped = line.strip()
            if not stripped.startswith("|"):
                header = None
                continue
            # An escaped pipe is content. build-deck.py emits them in titles.
            cells = stripped.replace("\\|", "").count("|")
            if header is None:
                header, header_line = cells, n
                continue
            if cells != header:
                problem(path, f"line {n}: table row has {cells} pipes, "
                              f"header on line {header_line} has {header}")
                header = None


def check_sector_overlays():
    """One overlay per sector in the taxonomy, and no strays."""
    src = os.path.join(ROOT, "resources", "sectors")
    if not os.path.isdir(src):
        PROBLEMS.append("resources/sectors/ is missing")
        return
    seen = {}
    for name in sorted(os.listdir(src)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(src, name)
        text = read(path)
        m = re.match(r"^---\n(.*?)\n---\n", text.replace("\r\n", "\n"), re.S)
        if not m:
            problem(path, "missing front matter")
            continue
        meta = {}
        for line in m.group(1).split("\n"):
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip().strip('"')
        sector = meta.get("sector")
        if sector not in scenarios.SECTORS:
            problem(path, f"sector '{sector}' is not in the taxonomy "
                          f"({', '.join(scenarios.SECTORS)})")
            continue
        if sector in seen:
            problem(path, f"sector '{sector}' is already covered by {seen[sector]}")
        seen[sector] = name
        for field in ("title", "summary"):
            if not meta.get(field):
                problem(path, f"{field} is missing or empty")
    for sector in scenarios.SECTORS:
        if sector not in seen:
            PROBLEMS.append(f"resources/sectors/: no overlay for sector '{sector}'")


def check_scenario_links():
    """Links into resources/scenarios/ name a scenario that exists."""
    known = {s["slug"] for s in scenarios.load()}
    for path in markdown_files():
        text = strip_code(read(path))
        for label, target in re.findall(r"\[([^\]]*)\]\(([^)\s]+)\)", text):
            m = re.search(r"scenarios/([a-z0-9-]+)\.md$", target)
            if m and m.group(1) not in known:
                problem(path, f"link '{label}' names scenario '{m.group(1)}', which does not exist")


def check_house_style():
    for path in markdown_files():
        text = strip_code(read(path))
        for n, line in enumerate(text.split("\n"), 1):
            low = line.lower()
            for word, why in BANNED.items():
                if word == "—":
                    if word in line:
                        problem(path, f"line {n}: em dash ({why})")
                elif re.search(rf"\b{word}", low):
                    problem(path, f"line {n}: '{word}' ({why})")


def check_counts():
    """Prose that states how many scenarios there are must be right."""
    # Only nouns that always mean the whole deck. "cards" is deliberately absent:
    # facilitation instructions legitimately say things like "two cards each".
    words = {"fifteen": 15, "twenty five": 25, "twenty-five": 25, "ten": 10}
    actual = len(scenarios.load())
    for path in markdown_files():
        text = strip_code(read(path))
        for phrase, value in words.items():
            for m in re.finditer(rf"\b{phrase}\s+(?:workshop\s+)?(?:scenarios|situations)\b", text, re.I):
                if value != actual:
                    problem(path, f"says '{m.group(0)}' but there are {actual} scenarios")
        for m in re.finditer(r"\b(\d+)\s+(?:workshop\s+)?(?:scenarios|situations)\b", text, re.I):
            if int(m.group(1)) != actual:
                problem(path, f"says '{m.group(0)}' but there are {actual} scenarios")


CHECKS = [
    ("sector overlays match the taxonomy", check_sector_overlays),
    ("relative links and anchors resolve", check_links),
    ("scenario links name real scenarios", check_scenario_links),
    ("table rows match their headers", check_tables),
    ("scenario counts in prose are right", check_counts),
    ("house style", check_house_style),
]


def main():
    for label, fn in CHECKS:
        before = len(PROBLEMS)
        fn()
        found = len(PROBLEMS) - before
        print(("  ok   " if not found else f"  FAIL ") + label + (f" ({found})" if found else ""))
    print()
    if PROBLEMS:
        for p in PROBLEMS:
            print(f"  {p}")
        print(f"\n{len(PROBLEMS)} problems")
        return 1
    print(f"All documentation checks passed across "
          f"{len(list(markdown_files()))} markdown files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
