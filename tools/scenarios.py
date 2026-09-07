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


def _front_matter(text):
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
    return [re.sub(r"^-\s+", "", l).strip() for l in chunk.split("\n") if l.strip().startswith("-")]


def load():
    scenarios = []
    for name in sorted(os.listdir(SRC)):
        if not name.endswith(".md"):
            continue
        meta, body = _front_matter(open(os.path.join(SRC, name), encoding="utf-8").read())
        parts = _sections(body)
        missing = [k for k in ("title", "slug", "category", "sectors", "difficulty", "summary") if k not in meta]
        if missing:
            raise ValueError(f"{name}: missing {', '.join(missing)}")
        if meta["category"] not in CATEGORIES:
            raise ValueError(f"{name}: unknown category {meta['category']}")
        for s in meta["sectors"]:
            if s not in SECTORS:
                raise ValueError(f"{name}: unknown sector {s}")
        scenarios.append({
            "title": meta["title"],
            "slug": meta["slug"],
            "category": meta["category"],
            "sectors": meta["sectors"],
            "difficulty": int(meta["difficulty"]),
            "minutes": int(meta.get("minutes", 10)),
            "summary": meta["summary"],
            "situation": [p.strip() for p in parts.get("the situation", "").split("\n\n") if p.strip()],
            "questions": _bullets(parts.get("questions to work through", "")),
            "think_about": _bullets(parts.get("think about", "")),
        })
    order = {"operational": 0, "governance": 1, "people": 2}
    scenarios.sort(key=lambda s: (order[s["category"]], s["difficulty"], s["title"]))
    return scenarios


if __name__ == "__main__":
    for s in load():
        print(f"{s['slug']:26} {s['category']:12} d{s['difficulty']} {len(s['questions'])}q {len(s['think_about'])}t")
