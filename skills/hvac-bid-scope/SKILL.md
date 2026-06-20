---
name: hvac-bid-scope
description: Bid-project scope rules for HVAC and mechanical work. Use when starting, triaging, validating, or packaging a commercial HVAC/mechanical bid.
---

# HVAC and Mechanical Bid Scope

Company: Your Company
CSI division(s): 23
Spec section hints: 23 05 00, 23 07 00, 23 31 13, 23 74 00

## Scope Rule

Base bid is limited to HVAC and mechanical systems defined by the profile: equipment, ductwork, hydronic and refrigerant piping, and air distribution. Test and balance, building automation/controls, plumbing, electrical power connections, and owner-furnished equipment must be explicitly included, excluded, or flagged before pricing.

## Base Scope

- rooftop units
- split systems
- air handlers
- ductwork
- grilles registers diffusers
- hydronic piping
- refrigerant piping
- exhaust fans
- VAV boxes

## Terms That Usually Identify This Scope

- hvac
- mechanical
- ductwork
- rooftop unit
- air handler
- VAV
- diffuser
- refrigerant
- 23 05
- 23 31

## Adjacent Scope To Exclude By Default

- fire sprinkler
- electrical wiring
- plumbing fixtures
- structural steel
- owner furnished

## Adjacent Scope To Flag Before Pricing

- test and balance
- controls
- building automation
- natural gas
- louvers
- fire damper
- smoke damper
- roof curbs

## Bid Package Workflow

1. Put source PDFs, spreadsheets, and addenda in `bid-docs/`.
2. Run `contractor-bid triage <project> --profile hvac`.
3. Review `bid-package-working/takeoff/candidate-pages.md` and `triage-scope-signals.md`.
4. Fill `takeoff/scope-pages-sources.json`, then run `contractor-bid build-packets <project>`.
5. Fill the takeoff JSON, then run `contractor-bid build-workbook <project>`.
6. Run `contractor-bid check <project> --profile hvac` before sending anything out.
7. Record user corrections with `contractor-bid learn` and update this skill/profile when the correction should become a durable rule.

## Guardrail

Do not silently price excluded or flagged adjacent scopes. Carry the scope boundary through the summary, reference index, workbook, proposal letter, alerts, and sendoff package.
