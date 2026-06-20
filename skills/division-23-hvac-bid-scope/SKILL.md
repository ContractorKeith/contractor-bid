---
name: division-23-hvac-bid-scope
description: Whole-division starter rules for CSI Division 23 - Heating, Ventilating, and Air Conditioning (HVAC). Use when starting, triaging, validating, or packaging a commercial HVAC bid.
---

# Division 23 - Heating, Ventilating, and Air Conditioning (HVAC) Bid Scope

Company: Your Company
CSI division(s): 23
Spec section hints: 23 00 00, 23 05 00, 23 07 00, 23 09 00, 23 21 00, 23 31 00, 23 34 00, 23 37 00, 23 74 00

## Scope Rule

Base bid is limited to CSI Division 23 - Heating, Ventilating, and Air Conditioning (HVAC) work specifically assigned to the bidder: HVAC piping, equipment, ductwork, air distribution, controls, insulation, testing, and balancing. Plumbing, fire suppression, electrical power, structural supports, roofing, and owner-furnished equipment must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- HVAC equipment
- ductwork and air distribution
- hydronic piping when assigned
- refrigerant piping when assigned
- mechanical insulation
- HVAC controls when assigned
- testing and balancing when assigned

## Terms That Usually Identify This Scope

- HVAC
- mechanical
- ductwork
- air handler
- rooftop unit
- VAV
- diffuser
- hydronic
- refrigerant
- 23 00

## Adjacent Scope To Exclude By Default

- plumbing fixture
- fire sprinkler
- electrical feeder
- roofing patch

## Adjacent Scope To Flag Before Pricing

- controls
- test and balance
- roof curb
- gas piping
- structural support

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-23-hvac`.
3. Review `bid-package-working/takeoff/candidate-pages.md` and `triage-scope-signals.md`.
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-23-hvac` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, reference index, workbook, proposal letter, alerts, and sendoff package.
