# CSI Division Starters

`contractor-bid` includes whole-division starter profiles for the active CSI MasterFormat divisions from 03 through 33. These are broad bid-starting rules, not final estimating decisions. A subcontractor should copy or customize the closest starter when their company carries a narrower trade package.

Division names follow CSI MasterFormat naming. Public references: [CSI MasterFormat](https://www.csiresources.org/standards/masterformat) and [ABC MasterFormat CSI Codes](https://www.abc.org/Membership/MasterFormat-CSI-Codes-NAICS-Codes/CSI-Codes).

Each active division starter includes:

- `profiles/division-XX-*.json`
- `examples/profiles/division-XX-*.json`
- `skills/division-XX-*-bid-scope/SKILL.md`

Regenerate or check the committed files with:

```bash
python3 scripts/generate-csi-starters.py
python3 scripts/generate-csi-starters.py --check
```

## Active Division Starters

| Division | CSI name | Profile |
|---|---|---|
| 03 | Concrete | `division-03-concrete` |
| 04 | Masonry | `division-04-masonry` |
| 05 | Metals | `division-05-metals` |
| 06 | Wood, Plastics, and Composites | `division-06-wood-plastics-composites` |
| 07 | Thermal and Moisture Protection | `division-07-thermal-moisture-protection` |
| 08 | Openings | `division-08-openings` |
| 09 | Finishes | `division-09-finishes` |
| 10 | Specialties | `division-10-specialties` |
| 11 | Equipment | `division-11-equipment` |
| 12 | Furnishings | `division-12-furnishings` |
| 13 | Special Construction | `division-13-special-construction` |
| 14 | Conveying Equipment | `division-14-conveying-equipment` |
| 21 | Fire Suppression | `division-21-fire-suppression` |
| 22 | Plumbing | `division-22-plumbing` |
| 23 | Heating, Ventilating, and Air Conditioning (HVAC) | `division-23-hvac` |
| 25 | Integrated Automation | `division-25-integrated-automation` |
| 26 | Electrical | `division-26-electrical` |
| 27 | Communications | `division-27-communications` |
| 28 | Electronic Safety and Security | `division-28-electronic-safety-security` |
| 31 | Earthwork | `division-31-earthwork` |
| 32 | Exterior Improvements | `division-32-exterior-improvements` |
| 33 | Utilities | `division-33-utilities` |

## Reserved Gaps

The current starter set intentionally skips reserved MasterFormat numbers in this range:

| Division | Status |
|---|---|
| 15 | Reserved for Future Expansion |
| 16 | Reserved for Future Expansion |
| 17 | Reserved for Future Expansion |
| 18 | Reserved for Future Expansion |
| 19 | Reserved for Future Expansion |
| 20 | Reserved for Future Expansion |
| 24 | Reserved for Future Expansion |
| 29 | Reserved for Future Expansion |
| 30 | Reserved for Future Expansion |

## Trade-Specific Starters

The repo also keeps narrower trade-specific starters such as `fences-gates`, `concrete-flatwork`, `drywall-framing`, `electrical`, `plumbing`, `hvac`, and `roofing`. Those are useful examples of how a subcontractor can narrow a whole CSI division into the scope they actually bid.
