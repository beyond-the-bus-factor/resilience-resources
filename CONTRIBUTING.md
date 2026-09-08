# Contributing

These resources get better when more people put their experience into them. If you have been through a difficult transition, a departure, a founder stepping back, a crisis nobody had planned for, what you learned is the thing that is missing here.

## This is not only for open source projects

The material started in open source and no longer stops there. It is written for four settings:

| Setting | What that covers |
|---|---|
| **Open source projects** | Maintainers, release keys, governance, forks |
| **Charities and NGOs** | Trustees, funders, regulators, statutory roles |
| **Companies** | Key person risk your continuity plan does not cover |
| **Small teams and collectives** | Where one person carries most of the operation |

The charity, NGO and company material is the newest and the thinnest. If you work in one of those and something here is wrong, or written by somebody who has clearly never sat in your job, that is the most useful thing you could tell us.

## Ways to contribute

**Share what happened to you.** [Open a discussion](https://github.com/beyond-the-bus-factor/resilience-resources/discussions) or [share a scenario](https://github.com/beyond-the-bus-factor/resilience-resources/issues/new/choose). Anonymise whatever you need to.

**Improve a resource.** Open a pull request with the specific change, and say what experience it comes from.

**Add a scenario to the deck.** See below, it is more structured than the rest.

**Propose a sector overlay.** If none of the four settings fit yours, [open an issue](https://github.com/beyond-the-bus-factor/resilience-resources/issues/new/choose) describing what is different about it. Overlays live in [`resources/sectors/`](resources/sectors) and all follow the same shape: what the audit's terms are called in that setting, the rows a neutral document cannot carry, the failure that setting most often turns out to have, a worked example, and which scenarios to run first. Copy an existing one as a model.

**Tell us it did not work.** Using a resource and finding it unhelpful is worth reporting. That feedback is rarer and more useful than praise.

### What makes a good contribution

Specific beats general, and lived beats theoretical.

**Useful:** an item missing from a checklist. A question in the audit that does not land. A scenario drawn from something that really happened. A template that worked. A term that means something different in your sector.

**Less useful:** best practice you have read but not tried. Generic advice from elsewhere. Corrections that do not change what a reader would do.

## Adding a scenario

Scenarios are the one part of this repository that is generated, so they work differently.

The source of truth is one file per scenario in [`resources/scenarios/`](resources/scenarios). Everything else, the readable document, the printable deck and the data the website uses, is built from those.

> **Do not edit `resources/scenario-cards.md` directly.** It is generated, and the next build will discard your changes. CI will also fail if the generated files do not match their sources.

### The steps

1. Copy any file in `resources/scenarios/` as a starting point
2. Edit the front matter and the body
3. Run `python3 tools/build-deck.py`, which needs nothing installed beyond Python 3
4. Commit both your scenario and the regenerated files
5. Open a pull request

### The front matter

```yaml
---
title: "The sole signatory"
slug: sole-signatory
category: operational
sectors: [charity, small-team]
difficulty: 2
minutes: 10
summary: "Payroll runs on Thursday and the only person who can authorise it is in intensive care."
---
```

| Field | Rules |
|---|---|
| `title` | Non-empty. Sentence case |
| `slug` | Lowercase letters, digits and single hyphens, matching the filename |
| `category` | One of `operational`, `governance`, `people` |
| `sectors` | A list, any of `open-source`, `charity`, `corporate`, `small-team` |
| `difficulty` | `1`, `2` or `3`, how hard the *discussion* is rather than how bad the crisis is |
| `minutes` | Optional, defaults to 10. A positive whole number, the suggested discussion time |
| `summary` | Non-empty. One sentence, the italic line on the card |

The build refuses anything that breaks these and tells you which file and which field, so you will find out immediately rather than in review.

### The body

Three headings, exactly these:

- `## The situation`, under about 250 words, or it will not fit on a printed card
- `## Questions to work through`, aim for five
- `## Think about`, the facilitator's notes, four or five points

Write the situation in the second person, present tense, with enough specific detail that somebody recognises their own organisation in it. The best scenarios are plausible rather than dramatic. Nobody learns anything from a disaster they cannot imagine happening to them.

## House style

These are enforced by CI, so a pull request that breaks them will go red. They are worth knowing before you write rather than after.

**Never use these words:** `quietly`, `genuinely`, `honest` and anything built from it. They are the author's own house rules and they apply to everything published here.

**Never use an em dash.** Use a comma, a full stop, or rewrite the sentence.

**Other conventions:**

- Sentence case headings, and no colons in headings
- "open source" is never hyphenated
- Write in the second person, "you" and "your team", not "one should consider"
- British spelling
- Plain language. Specific and concrete beats abstract
- Keep it scannable, with lists, headings and short paragraphs

## Running the checks

Before you open a pull request:

```
python3 tools/check_docs.py        # links, anchors, tables, house style, sector overlays
python3 tools/test_scenarios.py    # the scenario sources parse and validate
python3 tools/test_check_docs.py   # the checker itself still works
python3 tools/build-deck.py        # regenerate, then commit the result
```

No dependencies beyond Python 3. All of them run in CI too, so running them locally only saves you a round trip.

`check_docs.py` is the one that catches most things. It verifies that every relative link and anchor resolves, that tables are well formed, that there is one sector overlay per sector, that links to scenarios name real ones, that counts stated in prose are right, and the house style above.

## Review

Pull requests are reviewed by whoever has relevant experience. We are asking:

- Does this reflect something that really happened?
- Would a reader do something differently after it?
- Does it work for the settings it claims to cover?

Expect questions. That is the process working.

## Licensing

Everything here is released under [CC0](LICENSE), which means it goes into the public domain. By contributing you are agreeing to that: anyone can take your words, adapt them, and use them commercially with no credit.

That is deliberate. These resources are more useful when an organisation can paste them into their own handbook without a lawyer being involved.

## Code of conduct

Be kind. Everyone here is trying to make something survive without them. Assume good faith, and ask before you criticise.

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## A note on the subject matter

Much of this material deals with illness, death, burnout and people leaving badly. Some contributions will come from people describing the worst year of their working life.

Handle those with care in review. If somebody shares something difficult and it is not quite right for the deck, say so kindly and thank them properly. The willingness to talk about this at all is the scarce thing.
