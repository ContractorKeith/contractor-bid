---
name: division-14-conveying-equipment-bid-scope
description: Whole-division starter rules for CSI Division 14 - Conveying Equipment. Use when starting, triaging, validating, or packaging a commercial elevator, lift, escalator, or conveying equipment bid.
---

# Division 14 - Conveying Equipment Bid Scope

Company: Your Company
CSI division(s): 14
Spec section hints: 14 00 00, 14 20 00, 14 21 00, 14 24 00, 14 30 00, 14 40 00, 14 90 00

## Scope Rule

Base bid is limited to CSI Division 14 - Conveying Equipment work specifically assigned to the bidder: elevators, lifts, escalators, moving walks, hoists, and related conveying systems. Hoistway construction, structural supports, electrical feeders, fire alarm interfaces, pits, and permits must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- elevators when assigned
- wheelchair and platform lifts when assigned
- escalators and moving walks when assigned
- hoists and cranes when assigned
- conveyors when assigned
- controls furnished with conveying equipment
- startup and inspection support when assigned

## Terms That Usually Identify This Scope

- conveying equipment
- elevator
- lift
- escalator
- moving walk
- hoist
- conveyor
- 14 00

## Adjacent Scope To Exclude By Default

- structural steel
- concrete pit
- electrical feeder
- fire alarm wiring

## Adjacent Scope To Flag Before Pricing

- hoistway
- pit
- machine room
- fire alarm
- inspection

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-14-conveying-equipment`.
3. Review `bid-package-working/takeoff/candidate-pages.md` (candidate pages plus scope signals).
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-14-conveying-equipment` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, workbook, proposal letter, alerts, and sendoff package.
