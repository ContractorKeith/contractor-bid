---
name: division-32-exterior-improvements-bid-scope
description: Whole-division starter rules for CSI Division 32 - Exterior Improvements. Use when starting, triaging, validating, or packaging a commercial sitework, paving, landscaping, or fence bid.
---

# Division 32 - Exterior Improvements Bid Scope

Company: Your Company
CSI division(s): 32
Spec section hints: 32 00 00, 32 01 00, 32 10 00, 32 12 00, 32 13 00, 32 17 00, 32 31 00, 32 80 00, 32 90 00

## Scope Rule

Base bid is limited to CSI Division 32 - Exterior Improvements work specifically assigned to the bidder: paving, pavement markings, site concrete when assigned, fences and gates, retaining walls, irrigation, planting, and exterior amenities. Earthwork, utilities, electrical power, structural concrete, and environmental work must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- asphalt and concrete paving when assigned
- pavement markings and signage when assigned
- fences and gates when assigned
- retaining walls when assigned
- irrigation when assigned
- planting and landscape restoration when assigned
- site furnishings and exterior amenities when assigned

## Terms That Usually Identify This Scope

- exterior improvements
- paving
- asphalt
- pavement marking
- fence
- gate
- irrigation
- planting
- landscape
- 32 00

## Adjacent Scope To Exclude By Default

- storm drainage
- water utility
- electrical feeder
- building concrete

## Adjacent Scope To Flag Before Pricing

- earthwork
- electrical
- site utility
- tree protection
- maintenance

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-32-exterior-improvements`.
3. Review `bid-package-working/takeoff/candidate-pages.md` (candidate pages plus scope signals).
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-32-exterior-improvements` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, workbook, proposal letter, alerts, and sendoff package.
