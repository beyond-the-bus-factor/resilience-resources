---
sector: open-source
title: "For open source projects"
summary: "Maintainers, release keys, governance and what a fork really tests."
---

# Bus factor for open source projects

The [bus factor audit](../bus-factor-audit.md) is written to work anywhere. This adds what it cannot know about your setting: the vocabulary, the rows specific to open source projects, and the failure this sector most often turns out to have.

Open source is where the phrase comes from, so most of the audit will already read naturally. The rows below are the ones that are specific enough that a neutral document cannot carry them.

## What things are called here

| In the audit | Here |
|---|---|
| Whoever decides | Maintainers, the core team, a technical steering committee |
| The core work | The codebase, and reviewing what other people send |
| Publishing changes | Merging, cutting a release, publishing to the registry |
| Bringing new people in | Growing contributors, and granting commit access |
| Whoever funds or pays you | Sponsors, foundations, grant programmes, employers who pay people to contribute |
| Statutory filings | Usually nothing, unless you have a legal entity or a fiscal host |
| Roles a regulator requires | Rarely a regulator, but a foundation or a CRA style regime may require named roles |
| Communication channels | Issue tracker, chat, mailing list, forum |

## Rows to add to your audit

### Release and supply chain

| Area | Who? | Bus factor | Risk level |
|------|------|------------|------------|
| Cutting a release, start to finish | | | |
| Signing keys, and where the private half lives | | | |
| Publishing to each package registry | | | |
| Registry account ownership, and whether it is a personal account | | | |
| Reproducing a build from a clean machine | | | |
| Security advisories and coordinated disclosure | | | |
| The private channel security researchers use to reach you | | | |
| Dependencies you maintain that others depend on | | | |
| The data model and its migrations, if you have one | | | |

### Project ownership

| Area | Who? | Bus factor | Risk level |
|------|------|------------|------------|
| The organisation account on your code host | | | |
| Owner rights, as distinct from admin rights | | | |
| The domain, and who pays for it | | | |
| The trademark or project name, if anybody holds it | | | |
| The website and documentation deployment | | | |
| Continuous integration configuration and its secrets | | | |
| Bot and automation accounts | | | |
| Branch protection and merge policy, and who can change it | | | |
| Anything registered to one person's personal account | | | |

### Governance and community

| Area | Who? | Bus factor | Risk level |
|------|------|------------|------------|
| Deciding what goes in and what does not | | | |
| Code of conduct enforcement, and who hears an appeal | | | |
| Granting and revoking commit access | | | |
| Relationships with downstream packagers and distributors | | | |
| Relationships with the employers who fund contributor time | | | |
| Foundation or fiscal host relationships | | | |
| Conference and event relationships, and who gets invited to speak | | | |
| The people who would step up in a crisis, and whether anybody has asked them | | | |

## The failure this sector usually has

**Ownership resting in a personal account.**

Not the code, which is the part everyone thinks about and the part that is fine, because it is distributed by design. The rest of it. The npm or PyPI or crates account that publishes releases. The organisation on the code host where one person is the sole owner. The domain on somebody's personal card. The signing key on one laptop.

Losing the maintainer does not lose the code. It loses the ability to ship, which is almost as bad and considerably more confusing to explain to your users. A fork can continue the work. A fork cannot publish to your package name.

The second failure is **the release process nobody else has run**. It is documented, usually well. Nobody else has done it. The first time somebody else tries is in an incident, at speed, with a key they have never used, and that is when they discover the docs assume three things about the machine they are on.

The third is **assuming the community would organise itself**. Projects with real communities often assume that if the maintainer disappeared, somebody would pick it up. Sometimes true. It goes considerably better when a specific person has been asked in advance and said yes.

## A worked example

*A composite, built from patterns rather than one project. Treat it as a shape to recognise, not a case study.*

A project of moderate size, around 40,000 weekly downloads, two active maintainers and a handful of regular contributors.

The audit found the code in good shape and everything around it concentrated in one person. Sole owner of the organisation. Only publisher on the registry. Signing key on one laptop, backed up to a personal drive. Domain on a personal card with a renewal date nobody else knew. The security contact address forwarded to one inbox.

The second maintainer had commit access and had never cut a release. The documentation for releases was good, which was the reason nobody had felt the need to practise.

What they did in thirty days: added the second maintainer as an organisation owner, added them as a registry publisher, and moved the domain to an account both could reach. Cheap, and done in an afternoon once somebody wrote it on a list.

What they did in ninety days: the second maintainer cut the next two releases while the first watched, which turned up three undocumented assumptions in the first ten minutes. Moved the security address to something two people receive. Documented the release process by having somebody who had never done it follow the existing document and record every point they had to ask a question.

What they did not do: solve funding, or find a third maintainer. Both were on the list, and neither is a thirty day problem. The audit did not fix that, and pretending otherwise would have made the rest of it look easier than it was.

## Scenarios worth running first

From the [scenario cards](../scenario-cards.md):

- [The sudden disappearance](../scenario-cards.md#sudden-disappearance), for emergency access under time pressure
- [The security incident](../scenario-cards.md#security-incident), for signing keys and disclosure
- [The formalised handover](../scenario-cards.md#formalised-handover), if you think documentation is enough
- [The hostile fork](../scenario-cards.md#hostile-fork), for governance legitimacy
- [The successor conversation](../scenario-cards.md#successor-conversation), if you have been putting off asking somebody
- [The hovering founder](../scenario-cards.md#hovering-founder), for after a handover

## Then

- [Setting up legacy contacts](../set-up-legacy-contacts.md), which covers the code hosts directly
- [Legacy checklist](../legacy-checklist.md), for keys and credentials
- [Closing something down](../sunsetting-a-project.md), if continuing is no longer the right answer
