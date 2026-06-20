---
name: division-05-metals-bid-scope
description: Whole-division starter rules for CSI Division 05 - Metals. Use when starting, triaging, validating, or packaging a commercial metals bid.
---

# Division 05 - Metals Bid Scope

Company: Your Company
CSI division(s): 05
Spec section hints: 05 00 00, 05 05 00, 05 12 00, 05 21 00, 05 31 00, 05 40 00, 05 50 00, 05 70 00

## Scope Rule

Base bid is limited to CSI Division 05 - Metals work specifically assigned to the bidder: structural steel, joists, metal deck, cold-formed metal framing, metal fabrications, stairs, railings, and ornamental metals. Concrete, fireproofing, painting, doors/hardware, and delegated engineering must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- structural steel framing when assigned
- steel joists and metal deck when assigned
- cold-formed metal framing when assigned
- metal fabrications
- metal stairs and ladders
- handrails and guardrails
- ornamental metals when assigned

## Terms That Usually Identify This Scope

- metals
- structural steel
- steel joist
- metal deck
- cold-formed
- fabrication
- stair
- railing
- 05 00

## Adjacent Scope To Exclude By Default

- concrete
- fireproofing
- painting
- door hardware
- glazing

## Adjacent Scope To Flag Before Pricing

- shop drawings
- delegated design
- embed
- anchor bolt
- galvanizing

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile division-05-metals`.
3. Review `bid-package-working/takeoff/candidate-pages.md` and `triage-scope-signals.md`.
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile division-05-metals` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, reference index, workbook, proposal letter, alerts, and sendoff package.
