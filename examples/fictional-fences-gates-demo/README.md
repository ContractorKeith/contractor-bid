# Fictional Fences And Gates Demo Bid

This is a sanitized proof-of-life sample for the `fences-gates` profile. All source PDFs,
quantities, project names, and contacts are fictional.

The sample is intentionally input-only. It includes fake source PDFs in `bid-docs/` and the
two reviewed inputs that normally require human judgment:

- `bid-package-working/takeoff/scope-pages-sources.json`
- `bid-package-working/takeoff/fictional-cedar-park-fence.json`

It demonstrates:

- triage finds permanent fence and gate scope
- excluded adjacent terms such as bollards, concrete, paving, temporary fence, silt fence,
  and tree protection fence stay out of base bid
- review-only terms such as handrail and guardrail stay flagged
- approved pages build scope/spec packets
- takeoff JSON builds the workbook
- `check` flags the due date and addendum basis
- `package-sendoff` creates a clean supplier/internal-review zip

## Run It From A Source Checkout

From the repository root:

```bash
mkdir -p /tmp/contractor-bid-demo/bids
cp -R examples/fictional-fences-gates-demo \
  /tmp/contractor-bid-demo/bids/070126-fictional-cedar-park-fence

PYTHONPATH=src python3 -m contractor_bid triage \
  /tmp/contractor-bid-demo/bids/070126-fictional-cedar-park-fence \
  --profile fences-gates
PYTHONPATH=src python3 -m contractor_bid build-packets \
  /tmp/contractor-bid-demo/bids/070126-fictional-cedar-park-fence
PYTHONPATH=src python3 -m contractor_bid build-workbook \
  /tmp/contractor-bid-demo/bids/070126-fictional-cedar-park-fence \
  --profile fences-gates
PYTHONPATH=src python3 -m contractor_bid check \
  /tmp/contractor-bid-demo/bids/070126-fictional-cedar-park-fence \
  --profile fences-gates \
  --today 2026-06-30
PYTHONPATH=src python3 -m contractor_bid package-sendoff \
  /tmp/contractor-bid-demo/bids/070126-fictional-cedar-park-fence
```

After the run, inspect:

```text
/tmp/contractor-bid-demo/bids/070126-fictional-cedar-park-fence/bid-package-working/
```

