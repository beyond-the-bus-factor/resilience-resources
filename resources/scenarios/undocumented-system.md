---
title: "The system nobody understands"
slug: undocumented-system
category: operational
sectors: [corporate]
difficulty: 3
minutes: 12
summary: "He wrote it in 2014, it moves nine million a month, and his notice period ends in four weeks."
---

## The situation

A principal engineer has resigned. Four weeks' notice, leaving for a competitor, entirely within his rights.

In 2014 he wrote the reconciliation service. It sits between your billing platform and the ledger, and it moves around nine million a month. It has no owning team. It is not in the service catalogue. Its runbook is a wiki page last edited in 2019 that describes a deployment process which no longer exists.

Nobody else has ever deployed it. Twice in the last year it failed overnight and he fixed it before anyone noticed, which is why it has never been escalated. Your architecture review board has no record of it. Your business continuity plan covers the data centre, the network and the office, and says nothing about him.

His manager suggests a knowledge transfer session. He has offered two hours.

## Questions to work through

- What do you actually do with four weeks?
- Is two hours of his time the constraint, or is your ability to absorb it the constraint?
- What do you do about the other systems like this that you have not found yet?
- Who owns this service at 9am on the Monday after he leaves?
- What would you have wanted your continuity plan to have said about this?

## Think about

- Business continuity plans that cover buildings and not knowledge
- Systems that stay invisible because someone keeps fixing them before anyone notices
- Knowledge transfer as supervised work, not a meeting
- Finding the rest of them before the next resignation
- Notice periods as a fixed budget you have to spend well
