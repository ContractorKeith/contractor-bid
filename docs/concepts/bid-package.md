# What A Bid Project Produces

`contractor-bid` is useful because it gives the model and the estimator the same working surface. The model does not just chat about a bid. It creates files that can be checked, edited, rebuilt, and reused.

## The Output Package

| Artifact | Why it matters |
|---|---|
| `00-Bid-Scope-Summary.md` | The fast read: what appears in scope, what to open first, what still needs measurement, and what is excluded. |
| `00-Scope-Reference-Index.md` | A drawing/spec/RFI index that keeps source references visible. |
| `scope-pages.pdf` | A short PDF packet of only the pages relevant to the subcontractor's scope. |
| `spec-pages.pdf` | A short PDF packet of relevant spec pages when specs are found. |
| `scope-and-spec-pages.pdf` | One combined packet for review or supplier handoff. |
| `01-Takeoff-Worksheet-REV1.xlsx` | A workbook with BOM rows, supplier quote columns, alerts, RFIs, and source references. |
| `02 - Proposal Letter.md` | A proposal draft that carries inclusions, exclusions, alternates, and clarifications. |
| `ALERTS.md` | A validation report for missing artifacts, due date urgency, addenda, and scope-drift terms. |
| `supplier-sendoff/*.zip` | A clean handoff package for suppliers, vendors, or internal review. |

## Based On A Real Working Pattern

The first version came from active fence/gate bid workflows. In those projects, the useful package was not "one model answer." It was a folder with:

- a quick-read summary,
- a page-source JSON,
- isolated scope/spec PDF packets,
- a workbook generated from JSON,
- a reference index,
- a proposal draft,
- a review log,
- alerts for adjacent-scope drift,
- and a sendoff zip.

One real package ended with a 15-page scope packet, an 11-page spec packet, a 26-page combined packet, a workbook, and a supplier sendoff zip. Another smaller package had a 6-page scope packet and no separate spec packet. That difference is the point: the tool should adapt to the bid set while keeping the same reviewable structure.

## What It Does Not Do

- It does not replace manual takeoff.
- It does not guarantee final quantities.
- It does not create final pricing on its own.
- It does not replace contract review or trade judgment.
- It does not handle scanned image-only drawings well unless OCR has been done first.

The goal is narrower and more useful: get from messy bid docs to a source-backed bid workspace that a subcontractor can actually review before pricing.
