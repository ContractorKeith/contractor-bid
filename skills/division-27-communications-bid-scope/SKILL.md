---
name: division-27-communications-bid-scope
description: Whole-division starter rules for CSI Division 27 - Communications. Use when starting, triaging, validating, or packaging a commercial communications or structured cabling bid.
---

# Division 27 - Communications Bid Scope

Company: Your Company
CSI division(s): 27
Spec section hints: 27 00 00, 27 05 00, 27 10 00, 27 20 00, 27 30 00, 27 40 00, 27 50 00

## Scope Rule

Base bid is limited to CSI Division 27 - Communications work specifically assigned to the bidder: pathways when assigned, structured cabling, racks, grounding, voice/data, AV, paging, intercom, and communications equipment. Electrical power, security, fire alarm, owner network equipment, service provider work, and programming must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- structured cabling
- communications pathways when assigned
- equipment racks and cable management
- telecommunications grounding when assigned
- voice/data outlets and patch panels
- audio-video systems when assigned
- paging and intercom when assigned

## Terms That Usually Identify This Scope

- communications
- structured cabling
- data
- telecom
- fiber
- rack
- patch panel
- audio visual
- 27 00

## Adjacent Scope To Exclude By Default

- electrical power
- security
- fire alarm
- utility service provider

## Adjacent Scope To Flag Before Pricing

- owner equipment
- service provider
- pathway
- testing
- certification

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-27-communications`.
3. Review `bid-package-working/takeoff/candidate-pages.md` (candidate pages plus scope signals).
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-27-communications` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, workbook, proposal letter, alerts, and sendoff package.
