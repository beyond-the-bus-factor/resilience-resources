#!/usr/bin/env python3
"""Build every output from the scenario source files.

    python3 tools/build-deck.py

Writes:
  resources/scenario-cards.md   the readable document
  deck/scenario-deck.html       print sheet, A5 cards two to an A4 page
  deck/scenarios.json           data for the card tool on the website

Turning the print sheet into a PDF needs a browser and is a separate step,
so that this script stays dependency free. See deck/README.md.
"""

import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenarios import load, ROOT, SECTORS, CATEGORIES, DIFFICULTY  # noqa: E402

DECK = os.path.join(ROOT, "deck")


# ---------------------------------------------------------------- markdown

def build_markdown(scenarios):
    out = ["# Scenario cards", "",
           "Twenty five situations to put in front of a team and work through before one of "
           "them actually happens. Each one is written to be plausible rather than dramatic, "
           "because the useful discomfort comes from recognising your own organisation in it.",
           "",
           "There is a printable deck and a facilitator's guide alongside this document. See "
           "[the facilitator's guide](facilitator-guide.md) for session formats and timings.",
           "",
           "> These files are generated from `resources/scenarios/`. To change a scenario or "
           "add one, edit the file there and run `python3 tools/build-deck.py`.",
           ""]

    out += ["## What is in the deck", "",
            "| Scenario | Focus | Fits | Level |",
            "|---|---|---|---|"]
    for s in scenarios:
        sectors = ", ".join(SECTORS[x] for x in s["sectors"])
        out.append(f"| [{s['title']}](#{s['slug']}) | {CATEGORIES[s['category']]} | {sectors} | "
                   f"{DIFFICULTY[s['difficulty']]} |")
    out.append("")

    seen = None
    for s in scenarios:
        if s["category"] != seen:
            seen = s["category"]
            out += ["---", "", f"## {CATEGORIES[seen]}", ""]
        out += [f"### {s['title']}", "",
                f"<a id=\"{s['slug']}\"></a>",
                "",
                f"*{s['summary']}*", "",
                f"**Fits:** {', '.join(SECTORS[x] for x in s['sectors'])}  ",
                f"**Level:** {DIFFICULTY[s['difficulty']]}  ",
                f"**Suggested time:** {s['minutes']} minutes", "",
                "**The situation**", ""]
        out += [p + "\n" for p in s["situation"]]
        out += ["**Questions to work through**", ""]
        out += [f"- {q}" for q in s["questions"]]
        out += ["", "**Think about**", ""]
        out += [f"- {t}" for t in s["think_about"]]
        out.append("")

    out += ["---", "",
            "## After the session", "",
            "The point is not to have good answers. It is to find out what nobody in the room "
            "could answer, and to write those things down while you still remember them.", "",
            "- Which scenarios felt closest to your own situation, and why",
            "- What you would have no idea how to handle",
            "- Which gaps are a documentation problem, and which are a structural one",
            "- The one thing you will change in the next thirty days", "",
            "## Write your own", "",
            "The best scenarios are the ones drawn from your own near misses. What almost went "
            "wrong. What keeps you awake. What you watched happen to somebody else.", "",
            "Copy any file in `resources/scenarios/` as a starting point and open a pull "
            "request. Contributions are released under CC0 like the rest of this repository.", ""]
    return "\n".join(out)


# ------------------------------------------------------------------- print

CARD_CSS = """
@page { size: A4 portrait; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: "Inter", -apple-system, "Helvetica Neue", Arial, sans-serif;
  color: #15201d; background: #fff;
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
}
.sheet {
  width: 210mm; height: 297mm;
  display: flex; flex-direction: column;
  page-break-after: always; break-after: page;
}
.sheet:last-child { page-break-after: auto; break-after: auto; }
.card {
  position: relative;
  width: 210mm; height: 148.5mm;
  padding: 10mm 11mm 8mm;
  display: flex; flex-direction: column;
  overflow: hidden;
}
.card + .card { border-top: 0.3mm dashed #b9c2be; }

.card-top {
  display: flex; align-items: baseline; gap: 3mm;
  font-size: 6.6pt; letter-spacing: 0.09em; text-transform: uppercase;
  font-weight: 600; color: #5f6c68;
  border-bottom: 0.3mm solid #ddd8ce; padding-bottom: 2mm; margin-bottom: 3mm;
}
.card-top .cat { color: #845aa8; }
.card-top .fits { margin-left: auto; letter-spacing: 0.06em; font-weight: 500; }

h2 {
  font-family: "Source Serif 4", Georgia, serif;
  font-size: 17pt; font-weight: 600; line-height: 1.12;
  margin: 0 0 1.5mm; letter-spacing: -0.01em;
}
.lede {
  font-family: "Source Serif 4", Georgia, serif;
  font-size: 9.6pt; font-style: italic; color: #46534f;
  margin: 0 0 3.5mm; line-height: 1.35;
}
.body { display: flex; gap: 7mm; flex: 1; min-height: 0; }
.col-a { flex: 1.45; min-width: 0; }
.col-b { flex: 1; min-width: 0; }
h3 {
  font-size: 6.6pt; letter-spacing: 0.09em; text-transform: uppercase;
  font-weight: 700; color: #5f6c68; margin: 0 0 1.8mm;
}
.col-b h3 { margin-top: 0; }
p { font-size: 8.5pt; line-height: 1.42; margin: 0 0 2mm; }
ul { margin: 0 0 3.5mm; padding-left: 4mm; }
li { font-size: 8.5pt; line-height: 1.36; margin-bottom: 1.4mm; }
.think li { font-size: 7.6pt; color: #46534f; line-height: 1.32; margin-bottom: 1mm; }
.think h3 { color: #845aa8; }

.card-foot {
  display: flex; align-items: center; gap: 2mm;
  border-top: 0.3mm solid #ddd8ce; padding-top: 2mm; margin-top: 2mm;
  font-size: 6.4pt; color: #5f6c68; letter-spacing: 0.05em;
}
.card-foot .n { font-weight: 700; color: #183629; }
.card-foot .src { margin-left: auto; }
.dots { display: inline-flex; gap: 0.9mm; margin-left: 1mm; }
.dot { width: 1.5mm; height: 1.5mm; border-radius: 50%; background: #ddd8ce; }
.dot.on { background: #845aa8; }

/* cover */
.cover { justify-content: center; }
.cover h1 {
  font-family: "Source Serif 4", Georgia, serif;
  font-size: 26pt; font-weight: 600; margin: 0 0 3mm; letter-spacing: -0.015em;
}
.cover .lede { font-size: 11pt; max-width: 120mm; }
.cover ol { padding-left: 5mm; margin: 0 0 4mm; }
.cover li { font-size: 9pt; margin-bottom: 1.6mm; }
.cover .two { display: flex; gap: 10mm; }
"""


def esc(t):
    return html.escape(t, quote=False)


def dots(n):
    return "".join(f'<span class="dot{" on" if i < n else ""}"></span>' for i in range(3))


def card_html(s, index, total):
    fits = ", ".join(SECTORS[x] for x in s["sectors"])
    return f"""<section class="card">
  <div class="card-top">
    <span class="cat">{esc(CATEGORIES[s['category']])}</span>
    <span class="fits">{esc(fits)}</span>
  </div>
  <h2>{esc(s['title'])}</h2>
  <p class="lede">{esc(s['summary'])}</p>
  <div class="body">
    <div class="col-a">
      <h3>The situation</h3>
      {''.join(f'<p>{esc(p)}</p>' for p in s['situation'])}
    </div>
    <div class="col-b">
      <h3>Questions to work through</h3>
      <ul>{''.join(f'<li>{esc(q)}</li>' for q in s['questions'])}</ul>
      <div class="think">
        <h3>Think about</h3>
        <ul>{''.join(f'<li>{esc(t)}</li>' for t in s['think_about'])}</ul>
      </div>
    </div>
  </div>
  <div class="card-foot">
    <span class="n">{index:02d} / {total}</span>
    <span>{esc(DIFFICULTY[s['difficulty']])}<span class="dots">{dots(s['difficulty'])}</span></span>
    <span>{s['minutes']} minutes</span>
    <span class="src">Beyond the Bus Factor · CC0 · beyondthebusfactor.org</span>
  </div>
</section>"""


COVER = """<section class="card cover">
  <h1>Scenario cards</h1>
  <p class="lede">Twenty five situations to work through before one of them actually happens.
  Print, cut along the dashed line, and put one in front of a group.</p>
  <div class="two">
    <div>
      <h3>Running a session</h3>
      <ol>
        <li>Groups of three or four</li>
        <li>One card each, drawn or chosen</li>
        <li>Ten minutes on the questions</li>
        <li>Somebody writes down what nobody could answer</li>
        <li>Sixty seconds per group to share back</li>
      </ol>
    </div>
    <div>
      <h3>Reading a card</h3>
      <ul>
        <li><strong>Fits</strong> names the settings the situation translates to</li>
        <li><strong>Dots</strong> are how hard the discussion tends to be, not how bad the crisis is</li>
        <li><strong>Think about</strong> is for the facilitator, and is best left until the group has had a go</li>
      </ul>
    </div>
  </div>
  <div class="card-foot">
    <span class="n">Beyond the Bus Factor</span>
    <span>Full guide at beyondthebusfactor.org/scenarios/</span>
    <span class="src">Released under CC0. Adapt it, rebrand it, no credit needed.</span>
  </div>
</section>"""


def build_print(scenarios):
    cards = [COVER] + [card_html(s, i + 1, len(scenarios)) for i, s in enumerate(scenarios)]
    sheets = []
    for i in range(0, len(cards), 2):
        sheets.append('<div class="sheet">' + "".join(cards[i:i + 2]) + "</div>")
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<title>Scenario cards, printable deck</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,600;1,8..60,400&family=Inter:wght@400;500;600;700&display=swap">
<style>{CARD_CSS}</style>
</head>
<body>
{''.join(sheets)}
</body>
</html>
"""


# -------------------------------------------------------------------- main

def main():
    scenarios = load()
    os.makedirs(DECK, exist_ok=True)

    md = os.path.join(ROOT, "resources", "scenario-cards.md")
    with open(md, "w", encoding="utf-8") as fh:
        fh.write(build_markdown(scenarios))

    ph = os.path.join(DECK, "scenario-deck.html")
    with open(ph, "w", encoding="utf-8") as fh:
        fh.write(build_print(scenarios))

    js = os.path.join(DECK, "scenarios.json")
    with open(js, "w", encoding="utf-8") as fh:
        json.dump({
            "sectors": SECTORS,
            "categories": CATEGORIES,
            "difficulty": {str(k): v for k, v in DIFFICULTY.items()},
            "scenarios": scenarios,
        }, fh, indent=1, ensure_ascii=False)

    print(f"{len(scenarios)} scenarios")
    for p in (md, ph, js):
        print("  wrote", os.path.relpath(p, ROOT))


if __name__ == "__main__":
    main()
