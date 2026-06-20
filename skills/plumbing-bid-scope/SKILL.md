---
name: plumbing-bid-scope
description: Bid-project scope rules for plumbing. Use when starting, triaging, validating, or packaging a commercial plumbing bid.
---

# Plumbing Bid Scope

Company: Your Company
CSI division(s): 22
Spec section hints: 22 05 00, 22 11 16, 22 13 16, 22 40 00

## Scope Rule

Base bid is limited to plumbing systems defined by the profile: sanitary waste and vent, domestic water, interior storm leaders, fixtures, and water heaters. Site utilities beyond 5 ft of the building, fire protection, gas piping, and equipment connections must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- sanitary waste and vent
- domestic water piping
- plumbing fixtures
- water heaters
- floor drains
- cleanouts
- interior storm leaders
- trap primers

## Terms That Usually Identify This Scope

- plumbing
- sanitary
- waste and vent
- domestic water
- fixture
- water heater
- floor drain
- 22 11
- 22 13

## Adjacent Scope To Exclude By Default

- fire sprinkler
- fire protection
- process piping
- hvac piping
- owner furnished

## Adjacent Scope To Flag Before Pricing

- gas piping
- medical gas
- grease interceptor
- backflow
- water meter
- site utility
- storm drainage

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile plumbing`.
3. Review `bid-package-working/takeoff/candidate-pages.md` and `triage-scope-signals.md`.
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile plumbing` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, reference index, workbook, proposal letter, alerts, and sendoff package.
