---
name: division-22-plumbing-bid-scope
description: Whole-division starter rules for CSI Division 22 - Plumbing. Use when starting, triaging, validating, or packaging a commercial plumbing bid.
---

# Division 22 - Plumbing Bid Scope

Company: Your Company
CSI division(s): 22
Spec section hints: 22 00 00, 22 05 00, 22 07 00, 22 11 00, 22 13 00, 22 14 00, 22 40 00

## Scope Rule

Base bid is limited to CSI Division 22 - Plumbing work specifically assigned to the bidder: domestic water, sanitary waste and vent, storm drainage, fixtures, equipment, insulation, and plumbing specialties. Site utilities, fire suppression, HVAC piping, electrical power, controls, and owner-furnished equipment must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- domestic water piping
- sanitary waste and vent piping
- storm drainage piping when assigned
- plumbing fixtures and trim
- water heaters and plumbing equipment
- plumbing insulation when assigned
- floor drains, cleanouts, and specialties

## Terms That Usually Identify This Scope

- plumbing
- domestic water
- sanitary
- waste and vent
- fixture
- water heater
- floor drain
- cleanout
- 22 00

## Adjacent Scope To Exclude By Default

- fire sprinkler
- HVAC piping
- electrical wiring
- site water utility

## Adjacent Scope To Flag Before Pricing

- site utility
- gas piping
- grease interceptor
- storm drainage
- fixture by owner

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-22-plumbing`.
3. Review `bid-package-working/takeoff/candidate-pages.md` and `triage-scope-signals.md`.
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-22-plumbing` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, reference index, workbook, proposal letter, alerts, and sendoff package.
