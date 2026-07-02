# Why contractor-bid

Every AI construction tool chases takeoff measurement or the GC-side invite
blast. Nobody owns the specialty subcontractor's receiving side: the hours of
PDF shuffling between "you're invited to bid" and "I can actually price this."

contractor-bid owns that gap. It is the bid-setup tool for commercial
subcontractors. It gets you from bid invite to a reviewable, source-backed
package in under an hour, on your own machine, without uploading a single plan
sheet to anyone's cloud.

## The problem it solves

A commercial bid invite arrives with hundreds of plan pages, a project manual,
addenda, and a due date. Before you can price a single unit of work, someone
has to figure out which pages are yours, pull the relevant spec sections,
scaffold a takeoff, and watch for scope that drifted in from adjacent trades.
That is an afternoon gone, per bid, before estimating even starts.

contractor-bid turns that messy bid folder into a source-backed package:

- Your scope pages isolated into a bookmarked packet
- Spec sections pulled and packaged
- A takeoff workbook scaffolded from JSON you approve
- Scope-drift and missed-addenda alerts raised in `ALERTS.md`
- A supplier sendoff zipped and ready

## What makes it different

**Your plans never leave your machine.** contractor-bid is a local-first CLI
and optional stdio MCP server. There is no hosted service, no telemetry, and
no upload step. The core is MIT-licensed, so your IT department can read every
line. See [Security](reference/security.md).

**AI that cannot invent your numbers.** The model reads, classifies,
summarizes, and drafts. Deterministic code writes every quantity, from JSON
you approved, tied to a source page. Two human review gates are built into the
pipeline on purpose. If a number is in the workbook, you can prove where it
came from.

**Built by a working estimator.** 37 years in construction: master plumber,
journeyman electrician, founded and sold a homebuilding company, currently
estimating commercial fence. The tool runs on real bids before any release.

**Works with what you already run.** Bluebeam, Excel, email. contractor-bid
handles the hours before takeoff and the hour after: triage, scope, alerts,
sendoff. It feeds your measurement workflow instead of replacing it.

## What it will not do

- It will not price the job. Pricing is your judgment.
- It will not measure drawings. Use your existing takeoff workflow for that.
- It will not guess quantities. It refuses to, by design.

## Who it is for

- Specialty subcontractors in any CSI division (starter profiles cover
  Divisions 03 through 33)
- Estimators who want AI help but need every number to trace to a source page
- Anyone who cannot, or should not, upload GC documents to a cloud AI tool

Ready to try it? Start with [Install](install.md) and the
[Quick Start](quickstart.md).
