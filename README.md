# contractor-bid

`contractor-bid` is a starter kit for commercial subcontractors who want an AI-ready bid project folder for any CSI division.

The workflow is designed for Claude, Codex, or another model to operate inside a repeatable folder structure:

1. Initialize a subcontractor scope profile.
2. Start a new bid project.
3. Drop the bid documents into `bid-docs/`.
4. Triage PDFs into candidate scope/spec pages.
5. Build a quick-read summary, page packets, takeoff workbook, proposal draft, alerts, and sendoff zip.
6. Record corrections and promote durable lessons into the profile, skill, templates, or scripts.

The original pattern comes from real fence/gate bid-package work, but the names and guardrails are generic so concrete, millwork, electrical, drywall, roofing, sitework, and other trades can define their own scope boundaries.

## Install For Local Development

```bash
cd /Users/keithbloemendaal/Documents/github.nosync/projects/contractor-bid
python3 -m venv .venv
. .venv/bin/activate
pip install -e .
```

For PDF text and page images, install Poppler if it is not already available:

```bash
brew install poppler
```

## Quick Start

Create a scope profile:

```bash
python -m contractor_bid init \
  --profile fences-gates \
  --company "Complete Custom Fence" \
  --trade "Fences and Gates" \
  --divisions "32" \
  --base-scope "fence runs,gate openings,gate hardware,operators,posts,rails,panels,fabric" \
  --include-terms "fence,gate,chain link,ornamental,operator,access control,32 31" \
  --review-terms "railing,handrail,guardrail" \
  --exclude-terms "bollard,temporary fence,silt fence,tree protection fence,concrete,paving" \
  --non-interactive
```

Start a bid project:

```bash
python -m contractor_bid new bids/070126-example-project \
  --profile fences-gates \
  --project-name "Example Project" \
  --bid-due "2026-07-01 14:00"
```

Add source PDFs to `bids/070126-example-project/bid-docs/`, then run:

```bash
python -m contractor_bid triage bids/070126-example-project --profile fences-gates --render
python -m contractor_bid build-packets bids/070126-example-project
python -m contractor_bid build-workbook bids/070126-example-project --profile fences-gates
python -m contractor_bid check bids/070126-example-project --profile fences-gates
python -m contractor_bid package-sendoff bids/070126-example-project
```

## Generated Bid Artifacts

Each bid project gets the same basic working set:

- `bid-docs/` for source PDFs, bid forms, addenda, and spreadsheets.
- `bid-package-working/takeoff/candidate-pages.md` from triage.
- `bid-package-working/takeoff/triage-scope-signals.md` from triage.
- `bid-package-working/takeoff/scope-pages-sources.json` as the source map for extracted PDFs.
- `bid-package-working/00-Bid-Scope-Summary.md` as the first file to read.
- `bid-package-working/00-Scope-Reference-Index.md` as the drawing/spec/RFI index.
- `bid-package-working/01-Takeoff-Worksheet-REV1.xlsx` as the supplier-input workbook.
- `bid-package-working/02 - Proposal Letter.md` as the GC-facing proposal draft.
- `bid-package-working/scope-pages.pdf`, `spec-pages.pdf`, and `scope-and-spec-pages.pdf` when page sources are filled.
- `bid-package-working/ALERTS.md` from the validator.
- `bid-package-working/supplier-sendoff/*.zip` for supplier or partner handoff.

## Scope Profiles And Skills

`contractor-bid init` writes:

- `profiles/<profile>.json` - deterministic scope profile used by scripts.
- `skills/<profile>-bid-scope/SKILL.md` - model-readable instructions for Claude/Codex-style agents.

The profile is where each contractor defines:

- CSI division and spec section hints.
- Work carried in base bid.
- Search terms that identify the scope.
- Adjacent scope to exclude by default.
- Adjacent scope to flag before pricing.
- Standard proposal exclusions.

## Learning Loop

Record corrections:

```bash
python -m contractor_bid learn \
  --profile fences-gates \
  --project bids/070126-example-project \
  --note "Flag motor operators separately when electrical power/control responsibility is unclear."
```

The command appends to `.contractor-bid/feedback.jsonl` and `.contractor-bid/LESSONS.md`. Agents should review those files before similar bids. When a correction becomes a durable rule, update the profile, regenerate the skill, and adjust scripts/templates if needed.

## Repository Status

This repository is private while it is being built. It includes an MIT license so it can be opened later when the project is ready for public use.
