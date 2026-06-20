---
name: fences-gates-bid-scope
description: Bid-project scope rules for fences and gates. Use when starting, triaging, validating, or packaging a commercial fence/gate bid.
---

# Fences and Gates Bid Scope

Company: Your Company
CSI division(s): 32
Spec section hints: 32 31 13, 32 31 19

## Scope Rule

Base bid is limited to permanent fences, gates, gate hardware, and fence/gate-specific accessories. Adjacent scopes must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- fence runs
- gate openings
- gate hardware
- operators
- posts
- rails
- panels
- fabric

## Terms That Usually Identify This Scope

- fence
- gate
- chain link
- ornamental
- access control
- operator
- 32 31

## Adjacent Scope To Exclude By Default

- bollard
- temporary fence
- silt fence
- tree protection fence
- concrete
- paving

## Adjacent Scope To Flag Before Pricing

- railing
- handrail
- guardrail

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile fences-gates`.
3. Review `bid-package-working/takeoff/candidate-pages.md` and `triage-scope-signals.md`.
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile fences-gates` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, reference index, workbook, proposal letter, alerts, and sendoff package.
