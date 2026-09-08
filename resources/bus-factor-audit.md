# Bus factor audit

Your bus factor is the number of people who would have to disappear before the thing you run stops working. For most organisations that number is uncomfortably small, and everybody already knows whose name it is.

This audit finds where you are exposed, across three dimensions: the systems and operations that keep things running, the money, legal and governance that keep you allowed to run them, and the people who hold everything together.

It is written to work whatever you run. Where a row does not apply, skip it. Where your sector has risks this cannot know about, add them from your overlay:

- [For open source projects](sectors/open-source.md)
- [For charities and NGOs](sectors/charity-ngo.md)
- [For companies](sectors/company.md)
- [For small teams and collectives](sectors/small-team.md)

Each overlay translates the vocabulary, adds the rows specific to that setting, and names the failure that sector usually turns out to have.

## How to use this audit

Work through each section properly. For every area relevant to you, ask:

1. **How many people** can handle this on their own?
2. **How long** would it take somebody else to work it out?
3. **What would break** if those people were gone tomorrow?

Do not count who *could* theoretically do something. Count who *actually knows how* and has the access to do it this afternoon. Those are different numbers, and the gap between them is most of your risk.

Doing this alone will give you the wrong answer. You will overestimate what is written down and underestimate what only you know. Do it with the people who would have to pick things up.

## Scoring your risk

For each area, assign a level:

**🔴 Critical (bus factor 1):** One person. If they go, you are in crisis.

**🟡 Vulnerable (bus factor 2):** Two people. Losing one puts you back to critical.

**🟢 Resilient (bus factor 3+):** Three or more can each do it independently. You can absorb a loss.

Score what is true today, not what is meant to be true. A second person who was shown once, eighteen months ago, and has not done it since, is not a second person.

## Systems and operations

### Doing the work

The things that have to keep happening for you to be delivering at all.

| Area | Who can do it? | Bus factor | Risk level |
|------|----------------|------------|------------|
| The core work itself, end to end | | | |
| The specialist part only some people can do | | | |
| Publishing changes to the live service | | | |
| Undoing a change that went wrong | | | |
| Whatever runs on a schedule and would be missed | | | |
| Knowing when something has broken, and who finds out | | | |
| Restoring from backup, having actually tried it | | | |

**Questions to ask:**
- Could somebody else do a normal week's work without asking you anything?
- What runs on a schedule that nobody would notice had stopped until it mattered?
- If something broke at 2am, who would find out, and how?
- When did anyone last restore from a backup rather than assume it works?

### Access and credentials

Access is the one that turns a difficult month into an impossible one, and it is the cheapest to fix.

| Area | Who has it? | Bus factor | Risk level |
|------|-------------|------------|------------|
| The password manager, or wherever credentials live | | | |
| Administrator rights on your main systems | | | |
| The domain registrar | | | |
| Email and calendar administration | | | |
| Payment and banking access | | | |
| Anything tied to one person's phone or authenticator | | | |
| Accounts registered to a personal address rather than a shared one | | | |
| Certificates, licences and anything else with a renewal date | | | |
| Connections to other people's systems, and who set them up | | | |

**Questions to ask:**
- If one person lost their phone tomorrow, what could nobody get into?
- Which accounts are in an individual's name rather than the organisation's?
- Who is named on the paperwork, and is that still the right person?
- What expires, when, and who gets the reminder?

### Data and records

| Area | Where is it? | Who can reach it? | Risk level |
|------|--------------|-------------------|------------|
| Your main working records | | | |
| Financial records and history | | | |
| Contracts and agreements | | | |
| Anything held on a personal device or personal account | | | |
| Backups, and evidence they work | | | |

**Questions to ask:**
- What lives on somebody's laptop and nowhere else?
- What would you be unable to reconstruct if a personal account were closed?

## Money, legal and governance

### Authority and decisions

| Area | Who decides? | Bus factor | Risk level |
|------|--------------|------------|------------|
| Direction and priorities | | | |
| Spending, and above what amount | | | |
| Legal matters and contracts | | | |
| Bringing in new people | | | |
| Anything urgent, out of hours | | | |

**Questions to ask:**
- Who can commit you to something, and does everyone agree on that answer?
- If your usual decision maker is unreachable for a fortnight, what stalls?
- Is the authority written down, or is it just how it has always worked?

### Money

| Area | Who handles it? | Bus factor | Risk level |
|------|-----------------|------------|------------|
| Paying people | | | |
| Paying suppliers and bills | | | |
| Getting money in | | | |
| Bank mandates and authorised signatories | | | |
| The relationship with your accountant or bookkeeper | | | |
| Knowing what you are actually committed to | | | |

**Questions to ask:**
- Could payroll run this month without one specific person?
- When was the bank mandate last reviewed, and does it name anybody who has left?
- Who knows about the commitments that are not written in a contract?

### Legal, regulatory and compliance

| Area | Who is responsible? | Bus factor | Risk level |
|------|---------------------|------------|------------|
| Statutory filings and deadlines | | | |
| Roles a regulator requires you to name | | | |
| Insurance | | | |
| Data protection obligations | | | |
| Intellectual property, trademarks and licences | | | |
| Who owns what, and can you prove it | | | |

**Questions to ask:**
- Which obligations carry a deadline that does not move for an emergency?
- Are any required roles currently held by one person with no deputy?
- Would you be able to demonstrate ownership of your domain, your name and your work?

### Documentation and knowledge

| Area | Where is it? | How current? | Risk level |
|------|--------------|--------------|------------|
| How the work actually gets done | | | |
| How decisions actually get made | | | |
| Why things were done the way they were | | | |
| Open questions and things in flight | | | |
| The history somebody would need to avoid repeating a mistake | | | |

**Questions to ask:**
- Is the 'why' written down anywhere, or only the 'what'?
- What would a competent newcomer still get wrong after reading everything you have?

### External relationships

Relationships are the risk people forget, because they do not feel like assets until they are gone.

| Relationship | Who holds it? | Bus factor | Risk level |
|--------------|---------------|------------|------------|
| Whoever funds or pays you | | | |
| Key suppliers and partners | | | |
| Professional advisers | | | |
| Regulators and officials | | | |
| Press and public contacts | | | |
| Peers in your field who would help in a crisis | | | |

**Questions to ask:**
- If this person left, would the relationship survive, or does it leave with them?
- Has anybody else ever met these people?
- Which of these should sit with the organisation rather than an individual?

## People

### Leadership and the work nobody counts

| Role | Who does it? | Bus factor | Risk level |
|------|--------------|------------|------------|
| Setting direction | | | |
| Bringing new people in and settling them | | | |
| Reviewing and improving other people's work | | | |
| Handling conflict | | | |
| Upholding standards of behaviour | | | |
| Noticing when somebody is struggling | | | |
| Speaking for you in public | | | |

**Questions to ask:**
- Which of these has no name against it, and happens anyway because somebody absorbs it without being asked?
- Who would notice if the pastoral work stopped?

### Knowledge about people

| Area | Who knows it? | Bus factor | Risk level |
|------|---------------|------------|------------|
| Who is reliable, and who needs support | | | |
| Who could step up, given a year | | | |
| History between people that shapes how things go | | | |
| Who has stepped back, and why | | | |
| Who is close to leaving | | | |

**Questions to ask:**
- Is any of this written anywhere, and should it be?
- Who else could answer 'who should we ask to do this?'

### Communication channels

| Channel | Who administers it? | Bus factor | Risk level |
|---------|---------------------|------------|------------|
| Email lists and announcements | | | |
| Chat and messaging platforms | | | |
| Forums or discussion spaces | | | |
| Social media accounts | | | |
| Website and any blog | | | |
| Wherever you track work | | | |

**Questions to ask:**
- Could you post an urgent announcement today if the usual person were unreachable?
- Is administrator access spread across more than one person on each channel?
- What if the channel itself disappeared, and who has the list of who to contact?

## Reading your results

### Count the red

How many areas came out critical? More than five and you are fragile in a way that a single ordinary event, one resignation, one illness, will expose.

### Look for the pattern

The shape usually matters more than the count.

- **Knowledge concentration.** Is everything operational held by one person and everything governance by another?
- **Access concentration.** Does one person hold most of the credentials and administrator rights?
- **Relationship concentration.** Do all the outside relationships run through the same inbox?
- **Deadline exposure.** Are your reds attached to dates that will not move for an emergency?

### Name the person

Is there one person whose departure would cause several crises at once? That is your bus factor, and it is a person rather than a list.

They may not know. People carrying an organisation rarely notice they are doing it, and it is worth telling them plainly rather than leaving it in a spreadsheet.

## What to do next

Do not try to fix it all. Every organisation has vulnerabilities, and the point is knowing where you are fragile rather than being invulnerable.

### In the next thirty days

1. **Fix one red.** The scariest one. Get a second person trained, actually doing it rather than watching.
2. **Write down one thing** that lives in one person's head.
3. **Share one set of credentials** into a password manager that somebody else can reach.

### In the next ninety days

1. **Draft what would happen** if your highest-risk person left, using the [succession planning guide](succession-planning-guide.md).
2. **Cross-train on purpose.** Pair people on your most vulnerable areas, with the second person doing the work.
3. **Write down how decisions really get made**, which is usually different from the constitution.

### Longer term

1. **Rotate.** Nobody should stay the only expert in anything critical.
2. **Build in forcing functions.** Two signatories, two reviewers, two people on the rota. Structure beats intention.
3. **Repeat this audit** every six months. It is a rhythm, not an event, and the second time takes an hour.

## Where to go from here

- [Legacy checklist](legacy-checklist.md) for the immediate risks this turned up
- [Succession planning guide](succession-planning-guide.md) for the longer piece of work
- [Scenario cards](scenario-cards.md) to test your answers with other people in the room
