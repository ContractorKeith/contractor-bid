# Profiles

Built-in starter profiles live here and can be used immediately.

The canonical set is CSI-first: one whole-division starter for each active MasterFormat division from 03 through 33. Profile ids use `division-XX-*`, for example:

- `division-03-concrete`
- `division-04-masonry`
- `division-07-thermal-moisture-protection`
- `division-22-plumbing`
- `division-26-electrical`
- `division-32-exterior-improvements`
- `division-33-utilities`

See `docs/CSI_DIVISIONS.md` for the full active/reserved division table and the generator command.

The older trade-specific starters are still kept as narrower examples:

- `fences-gates` (Division 32)
- `concrete-flatwork` (Division 03)
- `drywall-framing` (Division 09)
- `electrical` (Divisions 26/27/28)
- `plumbing` (Division 22)
- `hvac` (Division 23)
- `roofing` (Division 07)

Profiles are deterministic JSON rules used by the scripts. Run `contractor-bid init` to create or overwrite a custom profile for your own company and scope.
