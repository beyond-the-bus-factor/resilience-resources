# Deck

Generated files. Do not edit anything in here by hand.

The source of truth is [`resources/scenarios/`](../resources/scenarios), one markdown file per scenario. To change a scenario, or add one, edit it there and rebuild.

## Rebuilding

```
python3 tools/build-deck.py
```

No dependencies. That regenerates:

| File | What it is |
|---|---|
| `../resources/scenario-cards.md` | The readable document |
| `scenario-deck.html` | Print sheet, A5 cards two to an A4 page |
| `scenarios.json` | Data for the card tool on the website |

## Making the PDF

The print sheet becomes a PDF through a browser, which is why it is a separate step. Either open `scenario-deck.html` and print to PDF at A4 with margins set to none and background graphics on, or run:

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --no-pdf-header-footer \
  --print-to-pdf=deck/scenario-deck.pdf \
  --virtual-time-budget=10000 \
  "file://$PWD/deck/scenario-deck.html"
```

On Linux, `google-chrome` or `chromium` in place of that path.

## Printing

A4, single sided, no scaling, background graphics on. Each sheet holds two A5 landscape cards. Cut along the dashed line. Card stock of 250gsm or above survives being handled by a workshop; ordinary paper does not survive the second session.

The first card is a cover with the session instructions on it, so a deck handed to somebody else explains itself.

## Checks

```
python3 tools/test_scenarios.py
```

Runs in CI on every pull request, along with a check that the generated files in this directory match the sources. If you edit a scenario and forget to rebuild, CI says so.

## Adding a scenario

Copy any file in `resources/scenarios/` and edit it. The front matter needs:

- `title`, `slug`, `summary` — the summary is the italic line on the card, one sentence
- `category` — `operational`, `governance` or `people`
- `sectors` — any of `open-source`, `charity`, `corporate`, `small-team`
- `difficulty` — 1, 2 or 3, how hard the discussion is rather than how bad the crisis is
- `minutes` — suggested discussion time

The body needs `## The situation`, `## Questions to work through` and `## Think about`. The build fails loudly if any of that is missing or misspelled.

Aim for five questions. Keep the situation under about 250 words, or it will not fit on the card.
