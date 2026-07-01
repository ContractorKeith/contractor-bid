---
name: division-26-electrical-bid-scope
description: Whole-division starter rules for CSI Division 26 - Electrical. Use when starting, triaging, validating, or packaging a commercial electrical bid.
---

# Division 26 - Electrical Bid Scope

Company: Your Company
CSI division(s): 26
Spec section hints: 26 00 00, 26 05 00, 26 20 00, 26 24 00, 26 27 00, 26 28 00, 26 51 00

## Scope Rule

Base bid is limited to CSI Division 26 - Electrical work specifically assigned to the bidder: service, distribution, grounding, raceways, wiring, devices, lighting, controls, and electrical specialties. Communications, security, fire alarm, utility company work, HVAC controls, owner-furnished equipment, and commissioning must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- electrical service and distribution
- raceways and conductors
- grounding and bonding
- switchboards, panels, and transformers
- wiring devices
- lighting fixtures and controls
- equipment connections when assigned

## Terms That Usually Identify This Scope

- electrical
- conduit
- feeder
- panel
- switchboard
- transformer
- lighting
- receptacle
- 26 00

## Adjacent Scope To Exclude By Default

- data cabling
- security
- fire alarm
- HVAC controls
- utility company

## Adjacent Scope To Flag Before Pricing

- utility
- lighting controls
- fire alarm
- low voltage
- owner furnished

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-26-electrical`.
3. Review `bid-package-working/takeoff/candidate-pages.md` (candidate pages plus scope signals).
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-26-electrical` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, workbook, proposal letter, alerts, and sendoff package.
