# Legacy checklist

What happens if you die tomorrow? Or have a serious accident? Or suddenly become incapacitated?

This checklist helps you prepare for the scenario nobody wants to think about: you disappearing without warning. Not a planned handoff, not a graceful transition, but an emergency.

If you're the person holding critical access or knowledge, this is your responsibility to prepare.

It applies wherever you hold that access: an open source project, a charity, a company, a small group. Where a section names something you do not have, skip it. For the items this cannot know about, add them from your overlay: [open source](sectors/open-source.md), [charities and NGOs](sectors/charity-ngo.md), [companies](sectors/company.md), [small teams](sectors/small-team.md).

## How to use this checklist

Work through each section. For every item, you need:
1. **Who has access** - At least two other people, ideally three
2. **Where to find it** - Documented location, accessible to those who need it
3. **What to do with it** - Clear instructions for the person who takes over

Don't only tick boxes. Actually set these things up and test that others _can_ access them.

## Critical access

### Passwords and credentials

- [ ] Password manager administrative access - at least one other person as an org-wide admin with access to all passwords
- [ ] Password manager account recovery process tested
- [ ] Two-factor authentication backup codes stored securely and documented
- [ ] Hardware security keys - at least one other person knows where they are, ideally have a backup which is solely for use in emergencies, which is stored safely (e.g. in a fireproof container in a safe)
- [ ] Personal email account access plan (recovery email, trusted contacts, legacy contacts)

**GitHub/GitLab/code hosting:**
- [ ] Organisation owner access held by at least three people
- [ ] [Legacy contact](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/maintaining-ownership-continuity-of-your-personal-accounts-repositories) set up on GitHub personal accounts (GitLab does not currently have any support but it's being discussed [here](https://gitlab.com/gitlab-org/gitlab/-/issues/26660)) - read more in [setting up legacy contacts](set-up-legacy-contacts.md)
- [ ] Instructions documented for next of kin / legacy contact regarding transferring repositories if needed
- [ ] Documentation of what repositories exist, their purpose, and who has access to them

**Infrastructure and hosting:**
- [ ] Server access (SSH keys, root passwords) stored securely and accessible to more than one person
- [ ] Cloud provider accounts (AWS, Azure, GCP, DigitalOcean, etc.) have more than one administrative user
- [ ] Domain registrar accounts have more than one administrator
- [ ] DNS management access has more than one administrator
- [ ] SSL certificate management notifications go to a group instead of an individual 
- [ ] CDN and hosting services have more than one person with root/admin level access to the servers and to the hosting provider's control panel/support system
- [ ] Monitoring and alerting services have more than one administrator and alert to a group instead of an individual

**Financial accounts:**
- [ ] Bank accounts (for organisational funds) have more than one signatory and a stated 'chain of command' approved by the bank with at least three people listed
- [ ] Payment processors (Stripe, PayPal, etc.) have more than one person as an administrator and notify into a group inbox
- [ ] Expense management tools have at least two administrators
- [ ] Donation platforms (Open Collective, Patreon, GitHub Sponsors, etc.) have at least two administrators
- [ ] Accounting software have at least two administrators, and all credentials for third-party integrations are securely stored including documenting which accounts they are connected with.

**Communication platforms:**
- [ ] Email hosting administration has more than one administrative user and a clear policy on legacy contacts
- [ ] Mailing list management has more than one administrative user and documented information on where it's managed, payment frequencies, and any integrations are fully documented including which user accounts are connected to any tokens used
- [ ] Slack/Discord/chat platform administration has more than one administrative user
- [ ] Social media account is delegated across more than one person and legacy contacts are set up for personal accounts
- [ ] Website CMS administration has more than one administrative user and documentation on how to access both the application and the hosting provider, plus any associated configurations for tools like Cloudflare.
- [ ] Documentation platform access has more than one administrative user and documentation on how to build, configure and manage.

**Legal and contracts:**
- [ ] Trademark registrations and documentation held in a central, secure location and documented as to who they are assigned to, when they're due for renewal
- [ ] Legal agreements and contracts have clear documentation on who can sign - which allows for more than one person - and are stored in a central location, with documented termination/renewal dates
- [ ] Vendor contracts and renewal dates are documented and in a location accessible to more than one person
- [ ] Insurance policies are stored in a central location, accessible by more than one person, and access to the provider's portal is delegated to more than one person (ideally with a legacy contact where possible)
- [ ] Foundation or legal entity paperwork is stored in a central location and has provision for situations resulting in member's death or unplanned absence

## Communication protocols

### Who announces your absence

- [ ] Primary person identified and they know they're responsible
- [ ] Backup person identified in case primary is unavailable
- [ ] These people have each other's contact details
- [ ] They know how to verify the situation before announcing
- [ ] They have a template message, written beforehand, which is used to notify of the situation

### What they say

Draft template messages for different scenarios:

**Template: Temporary absence**
(Name) is currently unable to participate in (project) due to (vague but truthful reason).

During this time, (person) will be handling (responsibility) and (person) will be handling (responsibility).

We expect (name) to return (timeframe if known / "when they're able" if not).
Please direct questions about (topic) to (person).

**Template: Permanent departure**
We're sad to share that (name) has (died / permanently left) and will no longer be leading (project).

(Name) contributed (specific achievements) and we're grateful for their work.

(Optional information about memorial services if relevant)

Going forward, (governance structure) will handle (responsibilities).

Please direct questions about (topic) to (person/email).

We're committed to continuing (project's mission).

- [ ] Templates drafted and stored where successors can find them
- [ ] Clear guidance on what NOT to say (respect privacy, avoid speculation)

### Where they announce

List of all places that need notification, in priority order:

- [ ] Project mailing list or forum
- [ ] Project chat channels
- [ ] Social media accounts
- [ ] Project website/blog
- [ ] Key partners and stakeholders (list them specifically)
- [ ] Funding organisations
- [ ] Parent organisations or foundations

## Operational continuity

### Keeping the work running

- [ ] The process for publishing or delivering changes is fully documented
- [ ] At least two other people have practised doing it, rather than reading about it
- [ ] Any signing keys or certificates are backed up somewhere a successor can reach
- [ ] Credentials for the systems that run automatically are accessible to successors
- [ ] The procedure for undoing a bad change is written down
- [ ] Anything that runs on a schedule is listed, with what happens if it stops

### Critical knowledge

- [ ] Significant decisions written down, with the reasoning
- [ ] The 'why we do it this way' context captured, not only the 'how'
- [ ] Known problems and the workarounds for them documented
- [ ] Relationships with the people you rely on explained, including who is difficult and why
- [ ] Conversations and decisions still in progress written down somewhere findable

### Ongoing operations

- [ ] Monitoring and alerting - who receives alerts if you don't respond
- [ ] Regular maintenance tasks documented with schedule
- [ ] Vendor relationships and contact points documented
- [ ] Service renewal dates in shared calendar
- [ ] Budget and financial runway documented

## Governance continuity

### Decision-making authority

- [ ] Clear documentation of who can make what decisions without you
- [ ] Governance structure documented (how are decisions made?)
- [ ] Process for emergency decisions that can't wait
- [ ] Voting procedures if applicable
- [ ] Conflict resolution processes

### Community leadership

- [ ] List of key community members and their roles
- [ ] Relationships with the people you depend on documented
- [ ] Ongoing community conflicts or concerns documented
- [ ] Community code of conduct enforcement - who handles reports
- [ ] Succession plan for community management roles

### External relationships

- [ ] Key partners and stakeholders with contact details
- [ ] Sponsor relationships and renewal dates
- [ ] Speaking commitments, conference appearances
- [ ] Media contacts and PR relationships
- [ ] Advisory board or steering committee contacts

## Personal preparation

### Legal planning

- [ ] Will or estate plan that addresses digital assets
- [ ] Clear instructions about what happens to your project role
- [ ] Executor or trusted person knows about your project involvement
- [ ] Legal structure (if any) has succession provisions

### Trusted contacts

- [ ] At least two people who know about this checklist
- [ ] They have access to the core document with all the details
- [ ] They know how to verify a real emergency vs. a false alarm
- [ ] You've tested the process (e.g., told them you'll be unreachable for a week)
- [ ] They have each other's contact details

### The core document

This checklist is the framework. You need a private core document with the actual details:

- [ ] Created and stored securely (encrypted, access-controlled)
- [ ] At least two trusted people know how to access it
- [ ] Includes actual passwords, contact details, account numbers
- [ ] Updated at least quarterly
- [ ] Tested - make sure people can actually access and use it

## Testing your preparation

Don't fill this out and forget it. Test it:

- [ ] Take a week completely off and unreachable - does everything keep running?
- [ ] Have somebody else do the thing only you do, using only your documentation, while you say nothing
- [ ] Ask your trusted contacts to access your core document - can they actually do it?
- [ ] Review and update this checklist every six months
- [ ] When things change (new services, new people), update immediately

## What this checklist won't do

This checklist won't make your absence less challenging. It won't eliminate the grief or the disruption. It won't replace the knowledge in your head or the relationships you've built.

What it will do is give the thing you have built a chance of surviving, and your successors a place to start.

That's what you owe to the people who depend on your work.

## Questions to reflect on

- If you died tonight, would anyone know how to access your password manager?
- Could an urgent change be made and published without you?
- Does anyone else know why the significant decisions were made the way they were?
- Would the people who depend on you know who to turn to?

If the answer to any of these is "no," start there.

---

*This checklist is adapted from hard-won experience. Add to it based on your own context. Share improvements via pull request.*
