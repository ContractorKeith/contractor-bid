# contractor-bid Docs

`contractor-bid` helps commercial subcontractors turn messy bid documents into a
reviewable, source-backed bid workspace.

It is a Python CLI plus optional agent integrations. The tool creates a consistent project
folder, finds likely scope/spec pages, builds review packets, generates a workbook from JSON,
checks for missing artifacts and scope drift, and packages supplier or internal-review
sendoffs.

## What To Read First

If you are new, follow these pages in order:

1. [Install](install.md) - get the CLI and optional PDF tools installed.
2. [Quick Start](quickstart.md) - run the fictional proof-of-life sample or create a project.
3. [First Bid Walkthrough](first-bid-walkthrough.md) - understand the full review loop.
4. [Bid Package Outputs](concepts/bid-package.md) - learn what files the tool produces.

If you are connecting an agent, start with [MCP And Agent Plugin Setup](guides/mcp-plugin-setup.md)
after the CLI works locally.

## The Core Promise

The tool does not price the job for you. It gives you a workspace an estimator and an AI agent
can both inspect:

- source PDFs stay in `bid-docs/`
- generated artifacts stay in `bid-package-working/`
- approved source pages are tracked in `takeoff/scope-pages-sources.json`
- takeoff and workbook generation come from JSON that can be reviewed
- excluded or review-only scope terms are checked before pricing

The source checkout includes `examples/fictional-fences-gates-demo/`, a sanitized fences/gates
bid with fake PDFs and fake quantities that can be copied to `/tmp` and run through the full
pipeline before using any customer documents.

## Standard Pipeline

```bash
contractor-bid doctor
contractor-bid new bids/070126-example --profile division-32-exterior-improvements
contractor-bid triage bids/070126-example --profile division-32-exterior-improvements --render
contractor-bid build-packets bids/070126-example
contractor-bid build-workbook bids/070126-example --profile division-32-exterior-improvements
contractor-bid check bids/070126-example --profile division-32-exterior-improvements
contractor-bid package-sendoff bids/070126-example
```

There are two human review points in that pipeline:

- approve candidate pages before building page packets
- fill source-backed takeoff JSON before building the workbook

Those review points are intentional. They keep PDF text hits from turning into unverified
pricing assumptions.
