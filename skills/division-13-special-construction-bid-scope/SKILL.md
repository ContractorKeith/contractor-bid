---
name: division-13-special-construction-bid-scope
description: Whole-division starter rules for CSI Division 13 - Special Construction. Use when starting, triaging, validating, or packaging a commercial special construction bid.
---

# Division 13 - Special Construction Bid Scope

Company: Your Company
CSI division(s): 13
Spec section hints: 13 00 00, 13 11 00, 13 12 00, 13 18 00, 13 21 00, 13 34 00, 13 49 00

## Scope Rule

Base bid is limited to CSI Division 13 - Special Construction work specifically assigned to the bidder: pre-engineered structures, pools, special-purpose rooms, controlled environments, sound/vibration assemblies, and other specialty systems. Foundations, utilities, MEP connections, controls, permits, and delegated design must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- pre-engineered structures when assigned
- special-purpose rooms
- controlled environment rooms when assigned
- aquatic and pool systems when assigned
- sound and vibration specialty systems when assigned
- radiation protection or shielded rooms when assigned
- special construction coordination items

## Terms That Usually Identify This Scope

- special construction
- pre-engineered
- prefabricated
- pool
- controlled environment
- cleanroom
- radiation protection
- sound isolation
- 13 00

## Adjacent Scope To Exclude By Default

- earthwork
- concrete foundation
- electrical feeder
- plumbing piping

## Adjacent Scope To Flag Before Pricing

- delegated design
- permit
- foundation
- utility connection
- controls

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-13-special-construction`.
3. Review `bid-package-working/takeoff/candidate-pages.md` and `triage-scope-signals.md`.
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-13-special-construction` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, reference index, workbook, proposal letter, alerts, and sendoff package.
