---
sector: corporate
title: "For companies"
summary: "The key person risk your business continuity plan does not cover."
---

# Bus factor for companies

The [bus factor audit](../bus-factor-audit.md) is written to work anywhere. This adds what it cannot know about your setting: the vocabulary, the rows specific to companies, and the failure this sector most often turns out to have.

If you already have a business continuity plan, do not start again. Run the audit against it and look for what the plan does not mention. That gap is the useful output.

## What things are called here

| In the audit | Here |
|---|---|
| Whoever decides | The leadership team, or whoever holds the budget |
| Direction and priorities | Roadmap, OKRs, the plan |
| Whoever funds or pays you | Customers, clients, accounts |
| The core work | Delivery, the product, the service |
| Publishing changes | Deployment, release, go-live |
| Bringing new people in | Hiring and onboarding |
| Roles a regulator requires | Named roles under your sector's regime, and your data protection officer |
| Documentation | The wiki, the runbooks, the service catalogue |

## What a continuity plan usually misses

Most business continuity planning covers premises, connectivity, systems and suppliers. It answers what happens if the building burns down. It rarely answers what happens if one person resigns, which is the thing that actually happens.

Check yours against these:

| Area | In the plan? | Who? | Risk level |
|------|--------------|------|------------|
| Named individuals, rather than roles, for each critical process | | | |
| Systems with no owning team | | | |
| Systems not in the service catalogue at all | | | |
| Knowledge that exists only as somebody's habit | | | |
| Notice periods, treated as a recovery budget | | | |
| Handover as a deliverable with acceptance criteria | | | |

## Rows to add to your audit

### Systems and ownership

| Area | Who? | Bus factor | Risk level |
|------|------|------------|------------|
| Every production system, mapped to an owning team | | | |
| Systems whose owner has left, and nobody replaced | | | |
| Anything one person has been fixing without escalating | | | |
| Cloud and SaaS accounts, and whose card pays for them | | | |
| Infrastructure built by somebody who has gone | | | |
| Work built by contractors, and what the contract said about handover | | | |
| On-call rotas, and whether they survive a reorganisation | | | |

### Commercial

| Area | Who? | Bus factor | Risk level |
|------|------|------------|------------|
| Each major account relationship, named individually | | | |
| Commitments made verbally that are not in the contract | | | |
| Renewal dates, and who is watching them | | | |
| Pricing history and why each exception exists | | | |
| Supplier relationships and what leverage you have | | | |
| Anything covered by a restrictive covenant, and how much it actually protects | | | |

### Organisational

| Area | Who? | Bus factor | Risk level |
|------|------|------------|------------|
| Products still live whose team has been reorganised away | | | |
| Approvals that route through one named person | | | |
| Access reviews, and when one last happened | | | |
| Offboarding, and whether it actually revokes everything | | | |
| The person everybody asks despite it not being their job | | | |

## The failure this sector usually has

**Systems nobody owns, kept alive by somebody who never escalated.**

The pattern is consistent. Somebody builds a thing that works. It falls outside a team boundary during a reorganisation. It keeps working, because that person fixes it before anyone notices. It never reaches the service catalogue, the architecture review, or the continuity plan, because from the outside there has never been a problem.

Then they resign, and you discover it during their notice period, if you are lucky, or three weeks afterwards if you are not. The quality of their work is what hid it. Runbooks and clean code are cited as reasons not to worry, which is exactly backwards: good documentation tells you how, and the risk is that nobody has ever done it.

The second failure is **reorganisations that move people and forget what the people were carrying**. Teams are dissolved and reformed against an org chart. The products they ran are not on the org chart. Ownership is left to transition planning, and transition planning is where it goes missing.

The third is **relationships treated as CRM records**. The notes are compliant and tell you nothing. Who the real decision maker is, which stakeholder is hostile, what was agreed verbally in a meeting two years ago: none of that is in the system, and all of it walks to the competitor.

## A worked example

*A composite, built from patterns rather than one organisation. Treat it as a shape to recognise, not a case study.*

A company of about two hundred people ran the audit against an existing continuity plan.

The plan was competent for what it covered. Data centre failover, supplier concentration, remote working, all tested. It ran to forty pages and named no individuals anywhere, on the reasonable principle that plans should reference roles.

That principle produced the gap. Rows that named a role were fine on paper and reduced to one person in practice. Twelve of them.

The worst was a reconciliation service written in 2014 by a principal engineer. It moved around nine million a month between the billing platform and the ledger. It had no owning team, was not in the service catalogue, and its runbook described a deployment process that no longer existed. It had failed twice overnight in the previous year, and been fixed before the alert escalated, which was why nobody had ever raised it.

What they did in thirty days: mapped every production system to an owning team and found four more with nobody's name against them. Started supervised deployments of the reconciliation service by two other engineers, doing the work rather than watching.

What they did in ninety days: added key person risk as a section of the continuity plan, with named individuals and a review each quarter. Made handover a deliverable in contractor agreements with acceptance criteria. Started multi-threading the top ten accounts, which was resisted by the account leads for the reasons you would expect and done anyway.

The principal engineer stayed, as it happens. The audit was not about him, and he was the one who pointed out two of the other four systems.

## Scenarios worth running first

From the [scenario cards](../scenario-cards.md):

- [The system nobody understands](../scenario-cards.md#undocumented-system), for the pattern above
- [The reorganisation](../scenario-cards.md#reorg), if restructuring is on the horizon
- [The relationships walk out](../scenario-cards.md#account-relationships), for commercial concentration
- [The contractor who built it](../scenario-cards.md#contractor-who-built-it), if you buy in delivery
- [The security incident](../scenario-cards.md#security-incident), for credentials held by one person
- [The cascade failure](../scenario-cards.md#cascade-failure), because plans usually assume losing one person

## Then

- [Succession planning guide](../succession-planning-guide.md), particularly the ninety day timeline, which maps onto a notice period
- [Legacy checklist](../legacy-checklist.md), for whoever holds credentials nobody else has
- [Closing something down](../sunsetting-a-project.md), for a product or service reaching the end, including what your contracts already promised
