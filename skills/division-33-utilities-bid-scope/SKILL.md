---
name: division-33-utilities-bid-scope
description: Whole-division starter rules for CSI Division 33 - Utilities. Use when starting, triaging, validating, or packaging a commercial site utilities bid.
---

# Division 33 - Utilities Bid Scope

Company: Your Company
CSI division(s): 33
Spec section hints: 33 00 00, 33 05 00, 33 10 00, 33 20 00, 33 30 00, 33 40 00, 33 50 00, 33 70 00, 33 80 00

## Scope Rule

Base bid is limited to CSI Division 33 - Utilities work specifically assigned to the bidder: water, wells, sanitary sewerage, storm drainage, fuel, hydronic/steam energy, electrical utilities, and communications utilities. Building plumbing/electrical systems, earthwork beyond utility scope, paving restoration, permits, and utility company work must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- water utilities when assigned
- sanitary sewerage utilities when assigned
- storm drainage utilities when assigned
- fuel distribution utilities when assigned
- energy utilities when assigned
- electrical utilities when assigned
- communications utilities when assigned

## Terms That Usually Identify This Scope

- utilities
- water utility
- sanitary sewer
- storm drainage
- fuel distribution
- electrical utility
- communications utility
- manhole
- 33 00

## Adjacent Scope To Exclude By Default

- building plumbing
- building electrical
- landscaping
- asphalt restoration

## Adjacent Scope To Flag Before Pricing

- utility company
- tap fee
- permit
- bypass pumping
- paving restoration

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-33-utilities`.
3. Review `bid-package-working/takeoff/candidate-pages.md` (candidate pages plus scope signals).
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-33-utilities` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, workbook, proposal letter, alerts, and sendoff package.
