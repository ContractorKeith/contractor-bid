---
name: division-21-fire-suppression-bid-scope
description: Whole-division starter rules for CSI Division 21 - Fire Suppression. Use when starting, triaging, validating, or packaging a commercial fire suppression bid.
---

# Division 21 - Fire Suppression Bid Scope

Company: Your Company
CSI division(s): 21
Spec section hints: 21 00 00, 21 05 00, 21 10 00, 21 13 00, 21 20 00, 21 30 00

## Scope Rule

Base bid is limited to CSI Division 21 - Fire Suppression work specifically assigned to the bidder: sprinkler, standpipe, fire pump, clean agent, and special fire suppression systems. Underground utilities, fire alarm, electrical power, structural supports, patching, and delegated design must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- wet and dry sprinkler systems
- standpipe systems when assigned
- fire pump systems when assigned
- clean agent or special suppression when assigned
- sprinkler piping and heads
- valves, trim, and specialties
- hydraulic calculations when assigned

## Terms That Usually Identify This Scope

- fire suppression
- sprinkler
- standpipe
- fire pump
- clean agent
- deluge
- preaction
- 21 00

## Adjacent Scope To Exclude By Default

- fire alarm
- electrical feeder
- site water utility
- patching

## Adjacent Scope To Flag Before Pricing

- hydraulic calculation
- fire pump
- underground
- fire alarm
- permit

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-21-fire-suppression`.
3. Review `bid-package-working/takeoff/candidate-pages.md` (candidate pages plus scope signals).
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-21-fire-suppression` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, workbook, proposal letter, alerts, and sendoff package.
