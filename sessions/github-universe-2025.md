# Beyond the bus factor - GitHub Universe 2025

## Welcome

Next year I'm taking a three-month sabbatical in the Spanish mountains to get ordained as a Buddhist. I'll be completely off-grid.

Preparing for that has forced me to confront every single point of failure in the Mautic project. Who has access to what? How do decisions get made without me? What happens if I don't come back?

These aren't comfortable questions, but they're essential ones. And I realised that most of us (including me!) are avoiding them until it's too late.

Today we're going to tackle the uncomfortable reality that most open source projects are one maintainer departure away from crisis. We're working under Chatham House Rule - use what you learn, but don't attribute who said what. This creates space to be candid about our vulnerabilities.

We're building these resources collaboratively. Everything discussed here will be shared in this repository to help others facing the same challenges.

---

## Opening question (we'll start with this)

**What's your biggest fear about your project's sustainability?**

Think about this now. We'll go around the room and each share briefly. This isn't about solutions yet - just naming the fear.

---

## Today's session flow

**45 minutes total:**
- Opening: Problem setting and introductions
- Section 1: Mapping your bus factor
- Section 2: Succession planning scenarios 
- Section 3: Designing sustainable systems
- Wrap-up: Your commitment

---

## Section 1: Mapping your bus factor

### Your task

Work through this audit individually for 3-4 minutes. Write down your actual vulnerabilities, not the ones you wish you had.

**Critical technical areas:**

Who can do this independently, right now?

- Deploy to production/release: _____ people
- Emergency rollback: _____ people  
- Access production infrastructure: _____ people
- Handle security incidents: _____ people
- Manage DNS and domains: _____ people

**Governance and decision-making:**

- Who decides project direction? _____
- Who can make emergency decisions? _____
- Is this process documented? Yes / No
- Could decisions happen without you? Yes / No

**Community and relationships:**

- Who manages community moderation? _____ people
- Who has admin access to all communication channels? _____ people
- Who maintains sponsor relationships? _____ people
- Who could onboard new contributors? _____ people

**Score your risks:**

For each area above:
- 🔴 Only 1 person = Critical risk - crisis if they leave
- 🟡 2 people = Vulnerable - risky but survivable
- 🟢 3+ people = Resilient - can lose someone and continue

**Your biggest vulnerability right now:**

_____________________________________

### Popcorn sharing (5-6 minutes)

We'll go around the room. Just call out:
- One area where you're most vulnerable (your 🔴 critical risks)
- Any patterns you noticed

We'll capture themes on the whiteboard.

**Full audit framework:** See [resources/bus-factor-audit.md](../resources/bus-factor-audit.md) for the complete version you can use back at your project.

---

## Section 2: Succession planning scenarios

### Small group exercise

Break into groups of 3-4 people. Your group will work through one crisis scenario together.

**Your task (8 minutes):**
1. Read your scenario
2. Discuss: What would you actually do?
3. Focus on the first 24-48 hours
4. What resources might help you in the moment, or to have prepared for this?
5. One person captures key insights to share back (1 minute max)

**Choose one scenario:**

See [resources/scenario-cards.md](../resources/scenario-cards.md)

### Share back

One person from each group shares one key insight in 60 seconds. What surprised you? What would you have no idea how to handle?

**Full scenarios and succession planning guide:** See [resources/scenario-cards.md](../resources/scenario-cards.md) and [resources/succession-planning-guide.md](../resources/succession-planning-guide.md)

---

## Section 3: Designing sustainable systems

By now we've identified our vulnerabilities and practised crisis response. This section shifts from problems to solutions. 

We're going to capture collective wisdom about what actually works. Fast-paced, everyone contributes, building on each other's ideas.

### Round 1: Tactical practices

**The prompt:**

**'What's ONE practice that prevents your project from depending on any single person?'**

**How this works:**

**Rapid-fire brainstorm**
- Call out your answer - one practice, keep it concrete
- I'll capture everything on the whiteboard
- No discussion yet, just get ideas out
- Build on what others say - 'yes, and...'
- Every answer is valid

**Quick discussion**
- Which ones surprised you?
- Which could you implement next week?
- Any patterns emerging?

**What we're looking for:**

Concrete, actionable practices like:
- Pair programming rotations
- Required two-person code review
- Rotating release manager role
- Documentation sprints or mob documentation
- Cross-training sessions
- Shared password managers (1Password Teams)
- Multiple people at every external meeting
- 'Two people must know this' rule for critical systems

Don't overthink it - what works in your project?

---

### Round 2: Cultural shifts

**The prompt:**

**'How do you make it NORMAL for people to step back before they burn out?'**

**How this works:**

**Thoughtful brainstorm**
- This is a harder question - take your time
- Share what's worked, what you've seen work, or what you're trying
- Stories welcome - sometimes an example helps
- I'll capture themes and specific practices

**Deeper discussion**
- Let's discuss the 2-3 that resonate most
- What makes these hard to implement?
- What would it take to make this normal in your project?

**What we're looking for:**

Cultural practices and systemic changes like:
- Time-limited leadership terms (up and out governance)
- Sabbatical policies for maintainers
- Public succession plans that normalise transitions
- Celebrating people who step back (not treating it as failure)
- 'Tending your garden leave' - paid time off for fun open source work (not what they work on day-to-day)
- Regular capacity check-ins with team
- Making 'no' a complete sentence
- Forcing functions that require rotation

This is about changing organisational culture, not just individual behaviour.

---

### Capturing these insights

Someone should be capturing themes and specific practices during this discussion. We'll turn these into:
- A checklist of practices to reduce bus factor
- A guide to building sustainable cultures
- Resources others can use

Create Issues tagged `github-universe-2025` with what emerges, or I'll do it immediately after the session based on the whiteboard.

**The energy shift:** Notice how this section feels different from earlier ones. We've moved from 'what's broken' to 'what works.' This is the mindset we need - building resilient projects is possible.


---

## Wrap-up: Your commitment

### Individual action planning

Right now, open your phone or a piece of paper. Write down:

**One specific action you'll take in the next 30 days to reduce your project's bus factor.**

Make it concrete:
- Not 'improve documentation' but 'Document the deployment process by Feb 15'
- Not 'distribute access' but 'Add Sarah and Jamal to the 1Password team this week'
- Not 'plan for succession' but 'Have succession conversation with potential co-lead by end of month'

### Share around the room

We'll go around quickly. Each person shares their 30-day commitment in one sentence.

This creates accountability. You've said it out loud to this group.

---

## Resources to take with you

These live in this repository. Star it to follow updates.

### [Legacy checklist](../resources/legacy-checklist.md)
What to prepare in case you die or become suddenly incapacitated. The uncomfortable conversation with practical details.

### [Bus factor audit](../resources/bus-factor-audit.md)
Complete framework for identifying single points of failure across technical, governance, and community dimensions.

### [Succession planning guide](../resources/succession-planning-guide.md)
Templates for planned departures, unexpected absences, and gradual transitions. Includes handoff checklists for technical, governance, and community succession.

### [Scenario cards](../resources/scenario-cards.md)
Ten detailed workshop scenarios you can use with your own teams.

---

## Contributing back to these resources

### During or after the session

**Create an Issue** with insights from your discussions:
- Missing items in the checklists
- Better scenario cards based on your real experiences
- Practical tips that worked for your project
- Tag it `github-universe-2025`

**Start a Discussion** to share:
- Real transition stories (anonymised if needed)
- Near-misses that taught you lessons
- Questions you're still wrestling with

**Submit a PR** with:
- Improvements to existing resources
- New templates or frameworks
- Fixes for unclear sections

### My commitment to you

I'll have PRs up within 7 days incorporating what we learned today. I need reviewers - volunteers?

---

## Why this matters

Most open source projects fail not because the technology is bad, but because key people leave and nobody knows how to continue.

We can do better than that.

Building projects that outlast us means confronting uncomfortable realities about our dependencies, our vulnerabilities, and our mortality.

That's what today is about.

---

**Repository:** [github.com/beyond-the-bus-factor/resilience-resources](https://github.com/beyond-the-bus-factor/resilience-resources)

**License:** CC0 1.0 Universal - use freely, adapt, share

**Connect:** ruth@ruthcheesley.co.uk

**About this project:** These resources are built collaboratively by maintainers who've navigated the messy realities of transitions, burnout, and building projects that survive beyond individuals. Your experience makes them better.
