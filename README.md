# Resilience resources

Practical tools for building projects and organisations that survive beyond any single person.

## What's here

This repository contains frameworks, checklists, and templates for reducing your bus factor - the uncomfortable reality that most projects are one key person away from crisis.

These resources were created collaboratively by people who have actually navigated difficult transitions: maintainer departures, burnout, sudden absences, corporate spinouts, and the messy human realities of keeping projects alive through change.

## Resources

### Core resources

#### Audits

- [Bus factor audit](resources/bus-factor-audit.md)
A framework for identifying single points of failure across technical systems, governance structures, and community roles.

#### Practical guides

- [Setting up legacy contacts](resources/set-up-legacy-contacts.md)
A detailed list of how to set up legacy contacts across digital platforms in the event something happens to you, ensuring someone is able to access your important accounts - both personal and organisational.

- [Sunsetting a project](resources/sunsetting-a-project.md)
Useful resources and tips when you’re considering shutting down or sunsetting an open source project.

#### Succession planning

- [Legacy checklist](resources/legacy-checklist.md)
What to prepare in case you die or become suddenly incapacitated. The uncomfortable conversation nobody wants to have, with the practical details everyone needs.

- [Succession planning guide](resources/succession-planning-guide.md)
Templates for planning both expected and unexpected transitions. Technical handoffs, governance changes, and community leadership transfers.

### Workshop resources

- [Scenario cards](resources/scenario-cards.md)
Twenty five situations to put in front of a team and work through before one of them actually happens. Each is tagged with the settings it fits (open source, charity and NGO, company, small team) and how hard the discussion tends to be.

  There is a [printable deck](deck/scenario-deck.pdf) as well, A4 with two A5 cards per sheet, and a card tool at [beyondthebusfactor.org/scenarios/cards](https://beyondthebusfactor.org/scenarios/cards/).

- [Facilitator's guide](resources/facilitator-guide.md)
How to run a scenario session when you have never run one before. Formats from forty five minutes to half a day, what to do when a group starts arguing with the scenario, and how to close so that something actually changes.

## Who this is for

These resources apply to any project or organisation with key person dependencies:

* Open source projects and communities
* Nonprofits and community organisations
* Small businesses and startups
* Creative collectives and volunteer groups
* Any team where losing one person would cause a crisis

## Using these resources

Start with the **bus factor audit** to understand your vulnerabilities. Then work through the **legacy checklist** to address immediate risks. Use the **succession planning guide** to build longer-term resilience.

All resources are templates. Adapt them to your context. They get better when you make them your own.

## Contributing

These resources improve when more people share their experience. If you've navigated a difficult transition, your hard-won lessons matter.

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to help.

### Adding a scenario

Scenarios live one per file in [`resources/scenarios/`](resources/scenarios). Copy any of them, edit it, and run:

```
python3 tools/build-deck.py
```

That regenerates the document, the print sheet and the website data from the same source. No dependencies. See [deck/README.md](deck/README.md) for the front matter fields and how the PDF is produced.

## Origin story

These resources emerged from the 'Beyond the bus factor' session at GitHub Universe 2025 Community Day, led by Sīlavāpi Cheesley (Mautic Project Lead), previously published under the name Ruth Cheesley.

They reflect real challenges: preparing for a three-month off-grid sabbatical, spinning projects out from corporate control, managing maintainer burnout, and dealing with unexpected departures.

## License

[CC0 1.0 Universal](LICENSE) - Use these resources freely. Adapt them. Share them. Make them better.

---

*Building projects that outlast us means confronting uncomfortable realities. Let's do that together.*
