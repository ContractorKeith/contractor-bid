---
name: electrical-bid-scope
description: Bid-project scope rules for electrical work. Use when starting, triaging, validating, or packaging a commercial electrical bid.
---

# Electrical Bid Scope

Company: Your Company
CSI division(s): 26, 27, 28
Spec section hints: 26 05 00, 26 24 16, 26 51 00

## Scope Rule

Base bid is limited to electrical systems defined by the profile. Low-voltage, fire alarm, security, data, controls, utility company work, and owner-furnished equipment must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- panels
- feeders
- branch circuits
- lighting
- devices
- gear
- conduit

## Terms That Usually Identify This Scope

- electrical
- panel
- lighting
- conduit
- feeder
- 26 05
- 26 24

## Adjacent Scope To Exclude By Default

- utility company
- owner furnished
- mechanical controls unless listed

## Adjacent Scope To Flag Before Pricing

- fire alarm
- security
- data
- controls
- low voltage
- generator

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile electrical`.
3. Review `bid-package-working/takeoff/candidate-pages.md` (candidate pages plus scope signals).
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile electrical` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, workbook, proposal letter, alerts, and sendoff package.
