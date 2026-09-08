# Closing something down

Most of this toolkit is about keeping things going. This one is about stopping, which is sometimes the right answer and is almost always done badly.

Closing well takes planning, careful communication and a good deal of patience. Done properly it is the last responsible act of the thing you built. Done badly it damages people who trusted you, and it is the version most of us have seen.

This works whatever you are closing: an open source project, a charity or one of its services, a product, a small group that has run its course. The process is largely the same. What differs is who has the authority to decide and what the law requires of you, and there is a section on that below.

For the parts specific to your setting, read alongside your overlay: [open source](sectors/open-source.md), [charities and NGOs](sectors/charity-ngo.md), [companies](sectors/company.md), [small teams](sectors/small-team.md).

## Deciding when the time has come

This is usually the hardest decision anyone makes about something they built. As the saying goes, there is never a good time.

Some of it you can look at without emotion. Is anyone still using this, and how would you know? Is activity going up or down over two or three years rather than two or three months? Has something else appeared that does this better? Is the money there for another year?

Where you have numbers, use them. Open source projects have contribution and download activity, and tools like [CHAOSS](https://chaoss.community/) and [OSInsight](https://ossinsight.io) do the heavy lifting. Charities have referrals, attendance and outcomes. Companies have usage, revenue and support load. Small groups often have nothing written down, in which case counting the last twelve months by hand is worth an afternoon.

Then there are the signals that no dashboard shows:

- Whoever holds it is burnt out, and has been for a while
- The funding has gone, or is going
- The need it was built for has changed, or somebody else now meets it
- Nobody can agree on a way forward, and has not for a long time
- Everyone involved is waiting for permission to say it out loud

**Closing is not the same as failing.** Things come into being and go out of being according to conditions, and that includes the ones we care about. A project that solved a problem for six years and is no longer needed did its job. Saying so plainly is better for everyone than letting it decay in public.

### Should you close it or hand it over

Before deciding to close, be clear which question you are answering. "I cannot keep doing this" and "this should not continue" are different, and people conflate them constantly when they are tired.

If it is the first, the honourable options are handing over, merging into something else, or finding a new home for it. Say so publicly and give it a real window before you close, because the person willing to take it on may not be somebody you have thought of.

If it is the second, say that too, and say why. A community that suspects it could have been saved will spend a year being angry about it.

## Making the decision properly

**Establish who actually decides.** Not who feels responsible, who has the authority. This is where closures go wrong, and the answer differs sharply by setting. If a governing document or a board or a contract has a say, find that out before you announce anything.

**Separate how you feel from what needs doing.** Closures often happen in the middle of something difficult: burnout, a falling out, money running out. The practical process still has to be carried out with care. Think of it as the last piece of work rather than the end of it.

**Write down the plan before you tell anybody.** Dates, who is told in what order, what happens to the money, what happens to the records, who answers questions afterwards. Announcing without a plan produces a month of uncertainty that helps nobody.

Perhaps we should think about how something would close from the day we start it, so there is a process to follow when it matters.

## Communicating it

The first communication should be clear, factual and short. People will read it once, badly, while feeling something.

**Tell the people closest to it first.** Whoever has given the most to this should not learn about it from an announcement. That means core contributors, staff and volunteers, trustees, the team.

**Then tell everyone, in one go.** Staggered announcements leak and turn into rumour.

**Say whether it is final.** If you would consider handing it over, make that explicit and say how to reach you. If this is the end, say that just as explicitly. Ambiguity here wastes months of everybody's time.

**Give real notice.** Enough for people to absorb it and act on it. Thirty days from announcement to closure is an absolute minimum, and for anything people depend on it is not enough. Where somebody's work, care or livelihood depends on you, think in months.

Depending on what you run, the announcement might need to go:

- At the top of your README or your homepage
- In your own channels: chat, forum, mailing list, newsletter
- In your documentation
- To package managers and app stores, most of which support a deprecation notice
- Inside the thing itself, as a banner or a notice at the point of use
- To funders, commissioners, regulators and insurers
- To staff and volunteers, following whatever process employment law requires
- To partner organisations who refer people to you
- To your own organisation internally, including anyone who will get the questions
- On social media, from the official accounts and from the people running it

**Then keep talking.** One announcement is not communication. Say something again at the halfway point and again near the end, because a third of people missed the first one.

## The last day

Make the ending definite and mark it.

For software, make a final release and be explicit that it is the last, then set the repository and the packages to deprecated so the message reaches people who never read announcements. For a service, be clear about the last day it runs, who to go to instead, and what happens to anyone mid-way through something. For an organisation, there will be a formal end date, and it is unlikely to be the day the work stops.

Whatever it is, say what happens to the things people care about: their data, their account, their case, their contributions, their money.

## Preserve the record, do not destroy it

**Archive rather than delete**, unless there is a reason not to.

For code, archiving means people can no longer contribute or open issues, and everything remains readable and forkable. It shows visibly that the project is no longer maintained, and it is reversible if you ever change your mind. Larger organisations sometimes keep a separate archive organisation, so the working account stays uncluttered and old work stays findable. You can also submit code to [Software Heritage](https://www.softwareheritage.org/), which is worth doing if you are decommissioning your own infrastructure.

For everything else the principle is the same. Records usually have to be kept for a period after closure, sometimes for many years, and somebody has to be able to reach them. Decide who holds them, where, and who is allowed to answer a question about them in three years' time. Write that down while you still have people who know the answer.

**What not to delete in a hurry:** anything with a legal retention period, anything a regulator or auditor may ask for, financial records, employment records, safeguarding records, and anything somebody might need to prove something about their own life.

## What changes by setting

The process above is the same everywhere. These are the parts that are not.

### Open source projects

Usually the simplest, because ownership is clear and nobody's employment depends on it. The work is mostly communication and archiving.

Watch for the things that outlive the code. The package name, which somebody could later claim and publish to. The domain, which expires and gets bought. The organisation account, which still has members. Transfer or lock these deliberately rather than letting them lapse, because an abandoned package name is a supply chain problem for everyone still depending on it.

If somebody wants to take it on, a fork with your blessing and a pointer from your README is usually better than transferring ownership to somebody you do not know well.

### Charities and NGOs

**This is a legal process, not only a decision.** Closing a charity, and often closing a significant service within one, is governed by your governing document and your regulator, and the trustees carry the duty.

Things to establish early, with your regulator's guidance and proper advice rather than from a web page:

- What your governing document says about winding up, which usually determines what can happen to what is left
- What your regulator requires you to notify and when
- Where remaining assets have to go, which is normally not to members and often has to be to a body with similar purposes
- What restricted funds allow, because money given for a purpose may have to be returned or reassigned rather than spent on closing
- Final accounts and returns, which are still due
- Employment obligations to staff, including consultation and redundancy
- How long records must be kept, especially anything involving beneficiaries

**Beneficiaries come first in the sequencing.** People receiving a service need somewhere to go, warm introductions to whoever takes over, and enough notice to arrange it. Get that settled before the public announcement where you can.

Tell funders directly and early. A funder told properly is often helpful, including with finding somewhere for the work to continue. A funder who reads about it online is not.

### Companies

Ownership and authority are usually clear. The complications are contractual and regulatory.

Check what you have promised: support windows, service commitments, notice periods, anything in a contract that survives the product. Enterprise customers frequently have terms individual users do not, and those terms tend to be discovered late.

People need to get their data out, in a usable form, with enough time to do it. In many jurisdictions that is an obligation rather than a courtesy. Say clearly when the export stops working and when the data is deleted.

If the thing you are closing is open source, or has a community around it, decide early whether to spin it out rather than shut it. That is a different piece of work with a different timeline, and it is much harder to start once you have announced a closure. There is more on that below, under sunsetting something an organisation owns.

### Small teams and collectives

There is usually less process and more that is personal, since the people closing it are often the people who built it.

The practical points that get missed: the bank account and what happens to money left in it, subscriptions still billing somebody's card, the domain, the shared drive, and whatever legal form you have, which may need formally dissolving rather than just stopping.

Decide who answers an email in a year, and say publicly who that is.

If the group has members who paid, or supporters who gave, decide what you owe them and say so before you are asked.

## Sunsetting something an organisation owns

If a company, foundation or other body owns what you are closing, you may also have to decide how and when to withdraw its resources, and whether new governance is needed rather than closure.

The [RCM Cooperative](https://www.rcmcooperative.com/) have a [flow chart](https://github.com/rcmcooperative/partner-template/blob/main/assets/RCM-sunsetting.drawio.pdf) that gives you a head start on planning this.

Where there is a sizeable community, expect a consultative process, particularly if the governance has to change or there is no governance to speak of. Here is how Mautic approached [spinning out from corporate ownership](https://speaking.ruthcheesley.co.uk/QYaM46/how-do-you-change-the-governance-model-of-an-established-open-source-project).

## Afterwards

Closures have a long tail. Somebody will email in eighteen months. A domain will come up for renewal. A user will surface who never got the message.

Decide now, while people are still around, who handles that and for how long. Write it in the same place as everything else, and tell the person you have named.

Then let people mark it. A closure that is only paperwork leaves everyone who cared about it with nowhere to put that. A short piece saying what it did, who built it and what it was for costs an hour and is the part people remember.

## References

Thanks to these resources:

- [CHAOSS Community guide to sunsetting a project](https://chaoss.community/practitioner-guide-sunset)
- [GitHub blog on sunsetting projects](https://github.blog/open-source/maintainers/dos-and-donts-when-sunsetting-open-source-projects/)
- [TODO guide on sunsetting projects](https://todogroup.org/resources/guides/shutting-down-an-open-source-project)
- [RCM workflow for sunsetting projects](https://github.com/rcmcooperative/partner-template/blob/main/assets/RCM-sunsetting.drawio.pdf)
- [Mautic's process for changing governance models](https://speaking.ruthcheesley.co.uk/QYaM46/how-do-you-change-the-governance-model-of-an-established-open-source-project)

The charity and company sections describe the shape of the problem rather than the law where you are. Closing a charity in particular has statutory steps that differ by jurisdiction. Use your regulator's own guidance, and take advice.
