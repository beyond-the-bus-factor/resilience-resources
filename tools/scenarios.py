"""Read the scenario source files.

Every scenario lives in one file under resources/scenarios/ with a small
front matter block. This module is the only thing that knows that format,
so the deck, the printable cards and the website all stay in step.

Deliberately dependency free, so `python3 tools/build-deck.py` works on a
clean machine with nothing installed.
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "resources", "scenarios")

SECTORS = {
    "open-source": "Open source",
    "charity": "Charity and NGO",
    "corporate": "Company",
    "small-team": "Small team",
}

CATEGORIES = {
    "operational": "Operational",
    "governance": "Governance, legal and finance",
    "people": "People and community",
}

DIFFICULTY = {1: "Warm up", 2: "Standard", 3: "Hard"}

# The slug becomes an anchor id and a fragment link in the generated markdown,
# and a key in the website data. Keep it to characters that mean the same thing
# in all three, so nothing has to be escaped downstream.
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def _front_matter(text):
    # Tolerate CRLF, so a file edited on Windows still parses.
    text = text.replace("\r\n", "\n")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("missing front matter")
    meta, body = {}, m.group(2).strip()
    for line in m.group(1).split("\n"):
        if not line.strip():
            continue
        key, _, value = line.partition(":")
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            value = [v.strip() for v in value[1:-1].split(",") if v.strip()]
        elif value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        elif value.isdigit():
            value = int(value)
        meta[key.strip()] = value
    return meta, body


def _sections(body):
    """Split a scenario body into its ## headed parts."""
    out = {}
    for head, chunk in re.findall(r"^## (.+?)\n(.*?)(?=^## |\Z)", body, re.S | re.M):
        out[head.strip().lower()] = chunk.strip()
    return out


def _bullets(chunk):
    """List items only.

    Matching a bare leading dash would also swallow a `---` horizontal rule
    and emit it as a bullet on the printed card.
    """
    out = []
    for line in chunk.split("\n"):
        m = re.match(r"^\s*[-*]\s+(.*\S)\s*$", line)
        if m:
            out.append(m.group(1))
    return out


def load():
    scenarios = []
    for name in sorted(os.listdir(SRC)):
        if not name.endswith(".md"):
            continue
        with open(os.path.join(SRC, name), encoding="utf-8") as fh:
            meta, body = _front_matter(fh.read())
        parts = _sections(body)
        missing = [k for k in ("title", "slug", "category", "sectors", "difficulty", "summary") if k not in meta]
        if missing:
            raise ValueError(f"{name}: missing front matter: {', '.join(missing)}")
        for field in ("title", "summary"):
            if not isinstance(meta[field], str) or not meta[field].strip():
                raise ValueError(f"{name}: {field} must be a non-empty string")
        if not isinstance(meta["slug"], str) or not SLUG.match(meta["slug"]):
            raise ValueError(f"{name}: slug must be lowercase letters, digits and single "
                             f"hyphens, for example sole-signatory. Got {meta['slug']!r}")
        if meta["slug"] != os.path.splitext(name)[0]:
            raise ValueError(f"{name}: slug '{meta['slug']}' does not match the filename")
        minutes = meta.get("minutes", 10)
        if not isinstance(minutes, int) or minutes <= 0:
            raise ValueError(f"{name}: minutes must be a positive whole number, got {minutes!r}")
        if not isinstance(meta["sectors"], list) or not meta["sectors"]:
            raise ValueError(f"{name}: sectors must be a non-empty list in square brackets, "
                             f"for example [charity, corporate]. Got {meta['sectors']!r}")
        if meta["category"] not in CATEGORIES:
            raise ValueError(f"{name}: unknown category '{meta['category']}', "
                             f"expected one of {', '.join(CATEGORIES)}")
        for sector in meta["sectors"]:
            if sector not in SECTORS:
                raise ValueError(f"{name}: unknown sector '{sector}', "
                                 f"expected one of {', '.join(SECTORS)}")
        if not isinstance(meta["difficulty"], int) or meta["difficulty"] not in DIFFICULTY:
            raise ValueError(f"{name}: difficulty must be 1, 2 or 3 written as a bare number, "
                             f"got {meta['difficulty']!r}")

        # A misspelled or missing heading would otherwise produce a card with an
        # empty half, and nothing would say so until somebody printed it.
        for heading in ("the situation", "questions to work through", "think about"):
            if not parts.get(heading):
                raise ValueError(f"{name}: missing or empty section '## {heading.capitalize()}'")
        if not _bullets(parts["questions to work through"]):
            raise ValueError(f"{name}: 'Questions to work through' has no list items")
        if not _bullets(parts["think about"]):
            raise ValueError(f"{name}: 'Think about' has no list items")
        scenarios.append({
            "title": meta["title"],
            "slug": meta["slug"],
            "category": meta["category"],
            "sectors": meta["sectors"],
            "difficulty": meta["difficulty"],
            "minutes": minutes,
            "summary": meta["summary"],
            "situation": [p.strip() for p in parts["the situation"].split("\n\n") if p.strip()],
            "questions": _bullets(parts["questions to work through"]),
            "think_about": _bullets(parts["think about"]),
        })
    order = {"operational": 0, "governance": 1, "people": 2}
    scenarios.sort(key=lambda s: (order[s["category"]], s["difficulty"], s["title"]))
    return scenarios


if __name__ == "__main__":
    for s in load():
        print(f"{s['slug']:26} {s['category']:12} d{s['difficulty']} {len(s['questions'])}q {len(s['think_about'])}t")
