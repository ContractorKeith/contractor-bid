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

## Install

### macOS / Linux

From a checkout:

```bash
git clone https://github.com/ContractorKeith/contractor-bid.git
cd contractor-bid
scripts/install.sh --install-poppler
```

When the repo is public, this can also be installed with:

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/ContractorKeith/contractor-bid/main/scripts/install.sh)"
```

### Windows PowerShell

```powershell
git clone https://github.com/ContractorKeith/contractor-bid.git
cd contractor-bid
.\scripts\install.ps1 -InstallPoppler
```

The installer creates an isolated virtualenv under `~/.contractor-bid`, installs the CLI there, and writes a launcher to `~/.local/bin/contractor-bid`.

### Developer Install

Use this only if you are editing the source code:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -e .
```

## Prerequisites

Required:

- Python 3.11 or newer
- Git, for the installer and updates

Installed automatically into the virtualenv:

- `openpyxl`, for `.xlsx` takeoff workbooks
- `pypdf`, for page packet PDFs and PDF fallback parsing

Recommended system dependency:

- Poppler: `pdfinfo`, `pdftotext`, and `pdftoppm`

Poppler gives faster PDF text extraction and page-image rendering. Without Poppler, basic PDF handling can fall back to `pypdf`, but rendered candidate page images are unavailable. This project does not do OCR yet; scanned image-only plans will need OCR before triage works well.

Check a machine:

```bash
contractor-bid doctor
```

No GitHub CLI is required for normal use.

## Quick Start

Start with a built-in scope profile:

- `fences-gates`
- `concrete-flatwork`
- `drywall-framing`
- `electrical`

Start a bid project:

```bash
mkdir contractor-bid-workspace
cd contractor-bid-workspace

contractor-bid new bids/070126-example-project \
  --profile fences-gates \
  --project-name "Example Project" \
  --bid-due "2026-07-01 14:00"
```

Add source PDFs to `bids/070126-example-project/bid-docs/`, then run:

```bash
contractor-bid triage bids/070126-example-project --profile fences-gates --render
contractor-bid build-packets bids/070126-example-project
contractor-bid build-workbook bids/070126-example-project --profile fences-gates
contractor-bid check bids/070126-example-project --profile fences-gates
contractor-bid package-sendoff bids/070126-example-project
```

Create a custom scope profile when the built-ins are not close enough:

```bash
contractor-bid init
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

Starter profiles and skills are included in the installed package and in the repo:

- `profiles/<profile>.json` - deterministic scope profile used by scripts.
- `skills/<profile>-bid-scope/SKILL.md` - model-readable instructions for Claude/Codex-style agents.

`contractor-bid init` writes or overwrites a custom profile and matching skill in the current workspace.

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
contractor-bid learn \
  --profile fences-gates \
  --project bids/070126-example-project \
  --note "Flag motor operators separately when electrical power/control responsibility is unclear."
```

The command appends to `.contractor-bid/feedback.jsonl` and `.contractor-bid/LESSONS.md`. Agents should review those files before similar bids. When a correction becomes a durable rule, update the profile, regenerate the skill, and adjust scripts/templates if needed.

## Repository Status

This repository is private while it is being built. It includes an MIT license so it can be opened later when the project is ready for public use.
