from __future__ import annotations

from typing import Any


RESERVED_CSI_DIVISIONS_03_33 = {
    "15": "Reserved for Future Expansion",
    "16": "Reserved for Future Expansion",
    "17": "Reserved for Future Expansion",
    "18": "Reserved for Future Expansion",
    "19": "Reserved for Future Expansion",
    "20": "Reserved for Future Expansion",
    "24": "Reserved for Future Expansion",
    "29": "Reserved for Future Expansion",
    "30": "Reserved for Future Expansion",
}


ACTIVE_CSI_DIVISIONS_03_33: tuple[dict[str, Any], ...] = (
    {
        "division": "03",
        "title": "Concrete",
        "profile_id": "division-03-concrete",
        "skill_description": (
            "Whole-division starter rules for CSI Division 03 - Concrete. Use when "
            "starting, triaging, validating, or packaging a commercial concrete bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 03 - Concrete work specifically assigned "
            "to the bidder: forming, reinforcing, cast-in-place, precast, finishes, and "
            "concrete repair. Earthwork, asphalt paving, utilities, landscaping, structural "
            "steel, waterproofing, and delegated design must be explicitly included, "
            "excluded, or flagged before pricing."
        ),
        "base_scope": [
            "concrete formwork",
            "reinforcing steel and accessories",
            "cast-in-place concrete",
            "concrete slabs and pads",
            "concrete finishing and curing",
            "precast concrete when assigned",
            "concrete repair and patching when assigned",
        ],
        "include_terms": [
            "concrete",
            "cast-in-place",
            "precast",
            "rebar",
            "reinforcing",
            "formwork",
            "slab",
            "footing",
            "curb",
            "03 00",
        ],
        "spec_sections": [
            "03 00 00",
            "03 10 00",
            "03 20 00",
            "03 30 00",
            "03 35 00",
            "03 40 00",
            "03 60 00",
        ],
        "quantity_units": ["CY", "SF", "LF", "EA", "TON"],
        "review_terms": ["sawcut", "demolition", "excavation", "vapor barrier", "waterproofing"],
        "exclude_terms": ["asphalt", "striping", "landscaping", "irrigation", "site utility"],
        "proposal_exclusions": [
            "unsuitable soils and subgrade correction unless listed",
            "survey/layout by others unless listed",
            "asphalt paving and striping unless listed",
            "dewatering and winter conditions unless listed",
        ],
    },
    {
        "division": "04",
        "title": "Masonry",
        "profile_id": "division-04-masonry",
        "skill_description": (
            "Whole-division starter rules for CSI Division 04 - Masonry. Use when "
            "starting, triaging, validating, or packaging a commercial masonry bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 04 - Masonry work specifically assigned "
            "to the bidder: unit masonry, stone, masonry accessories, reinforcement, "
            "grout, mortar, cleaning, and restoration. Structural steel, concrete, "
            "waterproofing, sealants, insulation, and delegated engineering must be "
            "explicitly included, excluded, or flagged before pricing."
        ),
        "base_scope": [
            "CMU and unit masonry",
            "brick masonry",
            "stone assemblies when assigned",
            "mortar and grout",
            "masonry reinforcement and ties",
            "lintels and masonry accessories when assigned",
            "masonry cleaning and restoration when assigned",
        ],
        "include_terms": [
            "masonry",
            "CMU",
            "concrete masonry unit",
            "brick",
            "block",
            "stone",
            "mortar",
            "grout",
            "04 00",
        ],
        "spec_sections": [
            "04 00 00",
            "04 05 00",
            "04 20 00",
            "04 22 00",
            "04 40 00",
            "04 70 00",
        ],
        "quantity_units": ["SF", "LF", "EA", "CY"],
        "review_terms": ["lintel", "flashing", "weep", "cavity insulation", "restoration"],
        "exclude_terms": ["structural steel", "cast-in-place concrete", "sealant", "waterproofing"],
        "proposal_exclusions": [
            "structural steel lintels unless listed",
            "waterproofing and air barriers unless listed",
            "sealants by others unless listed",
            "engineered shoring or bracing unless listed",
        ],
    },
    {
        "division": "05",
        "title": "Metals",
        "profile_id": "division-05-metals",
        "skill_description": (
            "Whole-division starter rules for CSI Division 05 - Metals. Use when "
            "starting, triaging, validating, or packaging a commercial metals bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 05 - Metals work specifically assigned "
            "to the bidder: structural steel, joists, metal deck, cold-formed metal "
            "framing, metal fabrications, stairs, railings, and ornamental metals. "
            "Concrete, fireproofing, painting, doors/hardware, and delegated engineering "
            "must be explicitly included, excluded, or flagged before pricing."
        ),
        "base_scope": [
            "structural steel framing when assigned",
            "steel joists and metal deck when assigned",
            "cold-formed metal framing when assigned",
            "metal fabrications",
            "metal stairs and ladders",
            "handrails and guardrails",
            "ornamental metals when assigned",
        ],
        "include_terms": [
            "metals",
            "structural steel",
            "steel joist",
            "metal deck",
            "cold-formed",
            "fabrication",
            "stair",
            "railing",
            "05 00",
        ],
        "spec_sections": [
            "05 00 00",
            "05 05 00",
            "05 12 00",
            "05 21 00",
            "05 31 00",
            "05 40 00",
            "05 50 00",
            "05 70 00",
        ],
        "quantity_units": ["TON", "LB", "LF", "EA", "SF"],
        "review_terms": ["shop drawings", "delegated design", "embed", "anchor bolt", "galvanizing"],
        "exclude_terms": ["concrete", "fireproofing", "painting", "door hardware", "glazing"],
        "proposal_exclusions": [
            "professional engineering unless listed",
            "field painting and touch-up beyond listed scope",
            "concrete embeds and anchor bolts unless listed",
            "fireproofing by others unless listed",
        ],
    },
    {
        "division": "06",
        "title": "Wood, Plastics, and Composites",
        "profile_id": "division-06-wood-plastics-composites",
        "skill_description": (
            "Whole-division starter rules for CSI Division 06 - Wood, Plastics, and "
            "Composites. Use when starting, triaging, validating, or packaging a "
            "commercial carpentry or millwork bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 06 - Wood, Plastics, and Composites "
            "work specifically assigned to the bidder: rough carpentry, sheathing, "
            "blocking, architectural woodwork, countertops, and plastic/composite "
            "fabrications. Framing in other divisions, casework in Division 12, "
            "waterproofing, hardware, and finishes must be explicitly included, "
            "excluded, or flagged before pricing."
        ),
        "base_scope": [
            "rough carpentry",
            "wood blocking and backing",
            "wood sheathing and panels",
            "architectural woodwork when assigned",
            "plastic laminate work when assigned",
            "countertops when assigned",
            "composite fabrications when assigned",
        ],
        "include_terms": [
            "rough carpentry",
            "wood",
            "blocking",
            "backing",
            "sheathing",
            "millwork",
            "casework",
            "plastic laminate",
            "countertop",
            "06 00",
        ],
        "spec_sections": [
            "06 00 00",
            "06 10 00",
            "06 16 00",
            "06 20 00",
            "06 40 00",
            "06 60 00",
        ],
        "quantity_units": ["LF", "SF", "EA", "BF"],
        "review_terms": ["casework", "countertop", "fire-retardant", "blocking by others"],
        "exclude_terms": ["metal framing", "finish painting", "door hardware", "waterproofing"],
        "proposal_exclusions": [
            "concealed blocking not shown on drawings unless listed",
            "field finishing by others unless listed",
            "door hardware and appliances unless listed",
            "solid surface or stone tops unless listed",
        ],
    },
    {
        "division": "07",
        "title": "Thermal and Moisture Protection",
        "profile_id": "division-07-thermal-moisture-protection",
        "skill_description": (
            "Whole-division starter rules for CSI Division 07 - Thermal and Moisture "
            "Protection. Use when starting, triaging, validating, or packaging a "
            "commercial roofing, waterproofing, insulation, firestopping, or sealants bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 07 - Thermal and Moisture Protection "
            "work specifically assigned to the bidder: waterproofing, insulation, air "
            "barriers, roofing, flashing, sheet metal, firestopping, joint protection, "
            "and sealants. Structural deck, framing, roof drains, interior finishes, and "
            "MEP penetrations must be explicitly included, excluded, or flagged before "
            "pricing."
        ),
        "base_scope": [
            "below-grade waterproofing when assigned",
            "thermal insulation",
            "air and vapor barriers",
            "roofing assemblies",
            "flashing and sheet metal",
            "firestopping",
            "joint sealants and expansion joints",
        ],
        "include_terms": [
            "roofing",
            "waterproofing",
            "insulation",
            "air barrier",
            "vapor barrier",
            "flashing",
            "sheet metal",
            "firestopping",
            "sealant",
            "07 00",
        ],
        "spec_sections": [
            "07 00 00",
            "07 10 00",
            "07 21 00",
            "07 24 00",
            "07 27 00",
            "07 50 00",
            "07 60 00",
            "07 84 00",
            "07 90 00",
        ],
        "quantity_units": ["SF", "LF", "EA", "ROLL"],
        "review_terms": ["wood blocking", "roof drain", "curb", "penetration", "warranty"],
        "exclude_terms": ["structural deck", "roof drain plumbing", "metal framing", "interior painting"],
        "proposal_exclusions": [
            "structural roof deck by others unless listed",
            "roof drains and overflow piping by others unless listed",
            "temporary dry-in unless listed",
            "manufacturer warranty fees unless listed",
        ],
    },
    {
        "division": "08",
        "title": "Openings",
        "profile_id": "division-08-openings",
        "skill_description": (
            "Whole-division starter rules for CSI Division 08 - Openings. Use when "
            "starting, triaging, validating, or packaging a commercial doors, frames, "
            "hardware, glazing, or storefront bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 08 - Openings work specifically assigned "
            "to the bidder: doors, frames, access panels, entrances, storefront, curtain "
            "wall, windows, hardware, glazing, and louvers. Structural steel, low-voltage "
            "wiring, access control, painting, and wall construction must be explicitly "
            "included, excluded, or flagged before pricing."
        ),
        "base_scope": [
            "hollow metal doors and frames",
            "wood doors when assigned",
            "access doors and panels",
            "aluminum entrances and storefront when assigned",
            "windows and curtain wall when assigned",
            "finish hardware",
            "glazing and louvers when assigned",
        ],
        "include_terms": [
            "door",
            "frame",
            "hardware",
            "storefront",
            "curtain wall",
            "window",
            "glazing",
            "louver",
            "access panel",
            "08 00",
        ],
        "spec_sections": [
            "08 00 00",
            "08 11 00",
            "08 14 00",
            "08 31 00",
            "08 41 00",
            "08 44 00",
            "08 71 00",
            "08 80 00",
        ],
        "quantity_units": ["EA", "SF", "LF", "SET"],
        "review_terms": ["access control", "electric strike", "panic", "closer", "fire rating"],
        "exclude_terms": ["low-voltage wiring", "card reader", "painting", "structural steel"],
        "proposal_exclusions": [
            "electrical and low-voltage wiring by others unless listed",
            "access control programming by others unless listed",
            "field painting by others unless listed",
            "structural supports by others unless listed",
        ],
    },
    {
        "division": "09",
        "title": "Finishes",
        "profile_id": "division-09-finishes",
        "skill_description": (
            "Whole-division starter rules for CSI Division 09 - Finishes. Use when "
            "starting, triaging, validating, or packaging a commercial finishes bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 09 - Finishes work specifically assigned "
            "to the bidder: gypsum assemblies, tile, ceilings, flooring, wall finishes, "
            "painting, coatings, and specialty finishes. Structural framing, MEP supports, "
            "waterproofing, Division 10 specialties, and furniture must be explicitly "
            "included, excluded, or flagged before pricing."
        ),
        "base_scope": [
            "metal studs and gypsum board when assigned",
            "tile and setting materials",
            "acoustical ceilings",
            "resilient flooring",
            "carpet and walk-off mats when assigned",
            "painting and coatings",
            "wall coverings and specialty finishes when assigned",
        ],
        "include_terms": [
            "finishes",
            "gypsum",
            "drywall",
            "tile",
            "ceiling",
            "flooring",
            "paint",
            "coating",
            "wall covering",
            "09 00",
        ],
        "spec_sections": [
            "09 00 00",
            "09 21 16",
            "09 29 00",
            "09 30 00",
            "09 51 00",
            "09 65 00",
            "09 68 00",
            "09 90 00",
        ],
        "quantity_units": ["SF", "LF", "EA", "SY"],
        "review_terms": ["level 5", "moisture mitigation", "floor prep", "fire-rated assembly"],
        "exclude_terms": ["structural steel", "waterproofing", "casework", "toilet accessories"],
        "proposal_exclusions": [
            "substrate correction beyond listed prep",
            "moisture mitigation unless listed",
            "temporary heat and humidity control by others",
            "after-hours phasing unless listed",
        ],
    },
    {
        "division": "10",
        "title": "Specialties",
        "profile_id": "division-10-specialties",
        "skill_description": (
            "Whole-division starter rules for CSI Division 10 - Specialties. Use when "
            "starting, triaging, validating, or packaging a commercial specialties bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 10 - Specialties work specifically "
            "assigned to the bidder: visual display units, signage, partitions, toilet "
            "accessories, fire protection specialties, lockers, louvers, postal "
            "specialties, and other specialty products. Blocking, backing, electrical, "
            "plumbing, structural supports, and installation by others must be explicitly "
            "included, excluded, or flagged before pricing."
        ),
        "base_scope": [
            "visual display units",
            "signage when assigned",
            "toilet compartments and accessories",
            "fire extinguisher cabinets",
            "lockers and storage specialties",
            "operable partitions when assigned",
            "miscellaneous specialty products",
        ],
        "include_terms": [
            "specialties",
            "signage",
            "toilet accessory",
            "toilet partition",
            "locker",
            "fire extinguisher cabinet",
            "markerboard",
            "corner guard",
            "10 00",
        ],
        "spec_sections": [
            "10 00 00",
            "10 14 00",
            "10 21 13",
            "10 22 00",
            "10 28 00",
            "10 44 00",
            "10 51 00",
        ],
        "quantity_units": ["EA", "LF", "SF", "SET"],
        "review_terms": ["blocking", "backing", "owner furnished", "sign permit", "electrical"],
        "exclude_terms": ["rough carpentry", "electrical wiring", "plumbing", "structural support"],
        "proposal_exclusions": [
            "blocking and backing by others unless listed",
            "electrical connections by others unless listed",
            "sign permits and fees unless listed",
            "owner-furnished items unless listed",
        ],
    },
    {
        "division": "11",
        "title": "Equipment",
        "profile_id": "division-11-equipment",
        "skill_description": (
            "Whole-division starter rules for CSI Division 11 - Equipment. Use when "
            "starting, triaging, validating, or packaging a commercial equipment bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 11 - Equipment work specifically assigned "
            "to the bidder: commercial, foodservice, loading dock, laboratory, athletic, "
            "and other facility equipment. Utility rough-ins, structural supports, "
            "controls, owner-furnished equipment, and commissioning must be explicitly "
            "included, excluded, or flagged before pricing."
        ),
        "base_scope": [
            "commercial equipment when assigned",
            "foodservice equipment when assigned",
            "loading dock equipment when assigned",
            "laboratory equipment when assigned",
            "athletic and recreational equipment when assigned",
            "equipment anchorage when assigned",
            "startup assistance when assigned",
        ],
        "include_terms": [
            "equipment",
            "foodservice",
            "appliance",
            "dock leveler",
            "laboratory equipment",
            "athletic equipment",
            "washer",
            "dryer",
            "11 00",
        ],
        "spec_sections": [
            "11 00 00",
            "11 10 00",
            "11 30 00",
            "11 40 00",
            "11 52 00",
            "11 53 00",
            "11 70 00",
        ],
        "quantity_units": ["EA", "SET", "LS"],
        "review_terms": ["owner furnished", "rough-in", "startup", "warranty", "anchorage"],
        "exclude_terms": ["electrical wiring", "plumbing piping", "gas piping", "structural steel"],
        "proposal_exclusions": [
            "utility rough-ins by others unless listed",
            "owner-furnished equipment unless listed",
            "structural supports and housekeeping pads unless listed",
            "final connections by others unless listed",
        ],
    },
    {
        "division": "12",
        "title": "Furnishings",
        "profile_id": "division-12-furnishings",
        "skill_description": (
            "Whole-division starter rules for CSI Division 12 - Furnishings. Use when "
            "starting, triaging, validating, or packaging a commercial furnishings bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 12 - Furnishings work specifically "
            "assigned to the bidder: window treatments, casework, countertops, entrance "
            "mats, furniture, seating, and systems furniture. Millwork in Division 06, "
            "appliances, electrical/data connections, blocking, and owner-furnished items "
            "must be explicitly included, excluded, or flagged before pricing."
        ),
        "base_scope": [
            "window treatments",
            "manufactured casework when assigned",
            "countertops when assigned",
            "entrance floor mats and frames",
            "furniture and seating when assigned",
            "systems furniture when assigned",
            "accessory furnishings when assigned",
        ],
        "include_terms": [
            "furnishings",
            "window treatment",
            "shade",
            "casework",
            "countertop",
            "furniture",
            "seating",
            "entrance mat",
            "12 00",
        ],
        "spec_sections": [
            "12 00 00",
            "12 21 00",
            "12 24 00",
            "12 32 00",
            "12 36 00",
            "12 48 00",
            "12 50 00",
        ],
        "quantity_units": ["EA", "LF", "SF", "SET"],
        "review_terms": ["blocking", "power/data", "owner furnished", "field measure"],
        "exclude_terms": ["rough carpentry", "electrical wiring", "plumbing fixtures", "appliances"],
        "proposal_exclusions": [
            "blocking and backing by others unless listed",
            "power and data connections by others unless listed",
            "field finishing by others unless listed",
            "owner-furnished items unless listed",
        ],
    },
    {
        "division": "13",
        "title": "Special Construction",
        "profile_id": "division-13-special-construction",
        "skill_description": (
            "Whole-division starter rules for CSI Division 13 - Special Construction. "
            "Use when starting, triaging, validating, or packaging a commercial special "
            "construction bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 13 - Special Construction work "
            "specifically assigned to the bidder: pre-engineered structures, pools, "
            "special-purpose rooms, controlled environments, sound/vibration assemblies, "
            "and other specialty systems. Foundations, utilities, MEP connections, "
            "controls, permits, and delegated design must be explicitly included, "
            "excluded, or flagged before pricing."
        ),
        "base_scope": [
            "pre-engineered structures when assigned",
            "special-purpose rooms",
            "controlled environment rooms when assigned",
            "aquatic and pool systems when assigned",
            "sound and vibration specialty systems when assigned",
            "radiation protection or shielded rooms when assigned",
            "special construction coordination items",
        ],
        "include_terms": [
            "special construction",
            "pre-engineered",
            "prefabricated",
            "pool",
            "controlled environment",
            "cleanroom",
            "radiation protection",
            "sound isolation",
            "13 00",
        ],
        "spec_sections": [
            "13 00 00",
            "13 11 00",
            "13 12 00",
            "13 18 00",
            "13 21 00",
            "13 34 00",
            "13 49 00",
        ],
        "quantity_units": ["LS", "EA", "SF", "LF"],
        "review_terms": ["delegated design", "permit", "foundation", "utility connection", "controls"],
        "exclude_terms": ["earthwork", "concrete foundation", "electrical feeder", "plumbing piping"],
        "proposal_exclusions": [
            "foundations by others unless listed",
            "utility connections by others unless listed",
            "permits and testing fees unless listed",
            "delegated design engineering unless listed",
        ],
    },
    {
        "division": "14",
        "title": "Conveying Equipment",
        "profile_id": "division-14-conveying-equipment",
        "skill_description": (
            "Whole-division starter rules for CSI Division 14 - Conveying Equipment. "
            "Use when starting, triaging, validating, or packaging a commercial elevator, "
            "lift, escalator, or conveying equipment bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 14 - Conveying Equipment work "
            "specifically assigned to the bidder: elevators, lifts, escalators, moving "
            "walks, hoists, and related conveying systems. Hoistway construction, "
            "structural supports, electrical feeders, fire alarm interfaces, pits, and "
            "permits must be explicitly included, excluded, or flagged before pricing."
        ),
        "base_scope": [
            "elevators when assigned",
            "wheelchair and platform lifts when assigned",
            "escalators and moving walks when assigned",
            "hoists and cranes when assigned",
            "conveyors when assigned",
            "controls furnished with conveying equipment",
            "startup and inspection support when assigned",
        ],
        "include_terms": [
            "conveying equipment",
            "elevator",
            "lift",
            "escalator",
            "moving walk",
            "hoist",
            "conveyor",
            "14 00",
        ],
        "spec_sections": [
            "14 00 00",
            "14 20 00",
            "14 21 00",
            "14 24 00",
            "14 30 00",
            "14 40 00",
            "14 90 00",
        ],
        "quantity_units": ["EA", "STOP", "LS"],
        "review_terms": ["hoistway", "pit", "machine room", "fire alarm", "inspection"],
        "exclude_terms": ["structural steel", "concrete pit", "electrical feeder", "fire alarm wiring"],
        "proposal_exclusions": [
            "hoistway and shaft construction by others unless listed",
            "power feeders and disconnects by others unless listed",
            "fire alarm interface by others unless listed",
            "inspection fees unless listed",
        ],
    },
    {
        "division": "21",
        "title": "Fire Suppression",
        "profile_id": "division-21-fire-suppression",
        "skill_description": (
            "Whole-division starter rules for CSI Division 21 - Fire Suppression. Use "
            "when starting, triaging, validating, or packaging a commercial fire "
            "suppression bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 21 - Fire Suppression work specifically "
            "assigned to the bidder: sprinkler, standpipe, fire pump, clean agent, and "
            "special fire suppression systems. Underground utilities, fire alarm, "
            "electrical power, structural supports, patching, and delegated design must "
            "be explicitly included, excluded, or flagged before pricing."
        ),
        "base_scope": [
            "wet and dry sprinkler systems",
            "standpipe systems when assigned",
            "fire pump systems when assigned",
            "clean agent or special suppression when assigned",
            "sprinkler piping and heads",
            "valves, trim, and specialties",
            "hydraulic calculations when assigned",
        ],
        "include_terms": [
            "fire suppression",
            "sprinkler",
            "standpipe",
            "fire pump",
            "clean agent",
            "deluge",
            "preaction",
            "21 00",
        ],
        "spec_sections": [
            "21 00 00",
            "21 05 00",
            "21 10 00",
            "21 13 00",
            "21 20 00",
            "21 30 00",
        ],
        "quantity_units": ["EA", "LF", "HEAD", "LS"],
        "review_terms": ["hydraulic calculation", "fire pump", "underground", "fire alarm", "permit"],
        "exclude_terms": ["fire alarm", "electrical feeder", "site water utility", "patching"],
        "proposal_exclusions": [
            "fire alarm wiring and monitoring by others unless listed",
            "underground fire service by others unless listed",
            "electrical power by others unless listed",
            "patching and painting by others unless listed",
        ],
    },
    {
        "division": "22",
        "title": "Plumbing",
        "profile_id": "division-22-plumbing",
        "skill_description": (
            "Whole-division starter rules for CSI Division 22 - Plumbing. Use when "
            "starting, triaging, validating, or packaging a commercial plumbing bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 22 - Plumbing work specifically assigned "
            "to the bidder: domestic water, sanitary waste and vent, storm drainage, "
            "fixtures, equipment, insulation, and plumbing specialties. Site utilities, "
            "fire suppression, HVAC piping, electrical power, controls, and owner-furnished "
            "equipment must be explicitly included, excluded, or flagged before pricing."
        ),
        "base_scope": [
            "domestic water piping",
            "sanitary waste and vent piping",
            "storm drainage piping when assigned",
            "plumbing fixtures and trim",
            "water heaters and plumbing equipment",
            "plumbing insulation when assigned",
            "floor drains, cleanouts, and specialties",
        ],
        "include_terms": [
            "plumbing",
            "domestic water",
            "sanitary",
            "waste and vent",
            "fixture",
            "water heater",
            "floor drain",
            "cleanout",
            "22 00",
        ],
        "spec_sections": [
            "22 00 00",
            "22 05 00",
            "22 07 00",
            "22 11 00",
            "22 13 00",
            "22 14 00",
            "22 40 00",
        ],
        "quantity_units": ["EA", "LF", "LS"],
        "review_terms": ["site utility", "gas piping", "grease interceptor", "storm drainage", "fixture by owner"],
        "exclude_terms": ["fire sprinkler", "HVAC piping", "electrical wiring", "site water utility"],
        "proposal_exclusions": [
            "site utilities beyond building connection unless listed",
            "fire suppression by others unless listed",
            "electrical power and controls by others unless listed",
            "owner-furnished fixtures unless listed",
        ],
    },
    {
        "division": "23",
        "title": "Heating, Ventilating, and Air Conditioning (HVAC)",
        "profile_id": "division-23-hvac",
        "skill_description": (
            "Whole-division starter rules for CSI Division 23 - Heating, Ventilating, and "
            "Air Conditioning (HVAC). Use when starting, triaging, validating, or "
            "packaging a commercial HVAC bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 23 - Heating, Ventilating, and Air "
            "Conditioning (HVAC) work specifically assigned to the bidder: HVAC piping, "
            "equipment, ductwork, air distribution, controls, insulation, testing, and "
            "balancing. Plumbing, fire suppression, electrical power, structural supports, "
            "roofing, and owner-furnished equipment must be explicitly included, excluded, "
            "or flagged before pricing."
        ),
        "base_scope": [
            "HVAC equipment",
            "ductwork and air distribution",
            "hydronic piping when assigned",
            "refrigerant piping when assigned",
            "mechanical insulation",
            "HVAC controls when assigned",
            "testing and balancing when assigned",
        ],
        "include_terms": [
            "HVAC",
            "mechanical",
            "ductwork",
            "air handler",
            "rooftop unit",
            "VAV",
            "diffuser",
            "hydronic",
            "refrigerant",
            "23 00",
        ],
        "spec_sections": [
            "23 00 00",
            "23 05 00",
            "23 07 00",
            "23 09 00",
            "23 21 00",
            "23 31 00",
            "23 34 00",
            "23 37 00",
            "23 74 00",
        ],
        "quantity_units": ["EA", "LF", "SF", "TON", "CFM"],
        "review_terms": ["controls", "test and balance", "roof curb", "gas piping", "structural support"],
        "exclude_terms": ["plumbing fixture", "fire sprinkler", "electrical feeder", "roofing patch"],
        "proposal_exclusions": [
            "electrical power wiring by others unless listed",
            "roof curbs and roof patching by others unless listed",
            "structural supports by others unless listed",
            "owner-furnished equipment unless listed",
        ],
    },
    {
        "division": "25",
        "title": "Integrated Automation",
        "profile_id": "division-25-integrated-automation",
        "skill_description": (
            "Whole-division starter rules for CSI Division 25 - Integrated Automation. "
            "Use when starting, triaging, validating, or packaging a commercial building "
            "automation or integration bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 25 - Integrated Automation work "
            "specifically assigned to the bidder: building automation integration, "
            "networking, controllers, programming, sequences, analytics, and system "
            "interfaces. Mechanical controls in Division 23, electrical power, low-voltage "
            "cabling, cybersecurity requirements, and owner platform work must be "
            "explicitly included, excluded, or flagged before pricing."
        ),
        "base_scope": [
            "integrated automation controllers",
            "building automation software when assigned",
            "integration gateways and interfaces",
            "sequences and programming",
            "automation network coordination",
            "graphics and trend setup when assigned",
            "commissioning support when assigned",
        ],
        "include_terms": [
            "integrated automation",
            "building automation",
            "BAS",
            "BMS",
            "DDC",
            "controls integration",
            "gateway",
            "sequence of operation",
            "25 00",
        ],
        "spec_sections": [
            "25 00 00",
            "25 05 00",
            "25 08 00",
            "25 10 00",
            "25 30 00",
            "25 50 00",
            "25 90 00",
        ],
        "quantity_units": ["EA", "POINT", "LS"],
        "review_terms": ["owner platform", "cybersecurity", "network", "commissioning", "training"],
        "exclude_terms": ["electrical power", "mechanical equipment", "low-voltage cabling", "fire alarm"],
        "proposal_exclusions": [
            "power wiring by others unless listed",
            "owner licensing and cloud subscriptions unless listed",
            "mechanical equipment controls by others unless listed",
            "third-party system access by owner/GC unless listed",
        ],
    },
    {
        "division": "26",
        "title": "Electrical",
        "profile_id": "division-26-electrical",
        "skill_description": (
            "Whole-division starter rules for CSI Division 26 - Electrical. Use when "
            "starting, triaging, validating, or packaging a commercial electrical bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 26 - Electrical work specifically "
            "assigned to the bidder: service, distribution, grounding, raceways, wiring, "
            "devices, lighting, controls, and electrical specialties. Communications, "
            "security, fire alarm, utility company work, HVAC controls, owner-furnished "
            "equipment, and commissioning must be explicitly included, excluded, or "
            "flagged before pricing."
        ),
        "base_scope": [
            "electrical service and distribution",
            "raceways and conductors",
            "grounding and bonding",
            "switchboards, panels, and transformers",
            "wiring devices",
            "lighting fixtures and controls",
            "equipment connections when assigned",
        ],
        "include_terms": [
            "electrical",
            "conduit",
            "feeder",
            "panel",
            "switchboard",
            "transformer",
            "lighting",
            "receptacle",
            "26 00",
        ],
        "spec_sections": [
            "26 00 00",
            "26 05 00",
            "26 20 00",
            "26 24 00",
            "26 27 00",
            "26 28 00",
            "26 51 00",
        ],
        "quantity_units": ["EA", "LF", "SF", "LS"],
        "review_terms": ["utility", "lighting controls", "fire alarm", "low voltage", "owner furnished"],
        "exclude_terms": ["data cabling", "security", "fire alarm", "HVAC controls", "utility company"],
        "proposal_exclusions": [
            "utility company fees and work by others unless listed",
            "low-voltage systems by others unless listed",
            "fire alarm by others unless listed",
            "owner-furnished equipment unless listed",
        ],
    },
    {
        "division": "27",
        "title": "Communications",
        "profile_id": "division-27-communications",
        "skill_description": (
            "Whole-division starter rules for CSI Division 27 - Communications. Use when "
            "starting, triaging, validating, or packaging a commercial communications or "
            "structured cabling bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 27 - Communications work specifically "
            "assigned to the bidder: pathways when assigned, structured cabling, racks, "
            "grounding, voice/data, AV, paging, intercom, and communications equipment. "
            "Electrical power, security, fire alarm, owner network equipment, service "
            "provider work, and programming must be explicitly included, excluded, or "
            "flagged before pricing."
        ),
        "base_scope": [
            "structured cabling",
            "communications pathways when assigned",
            "equipment racks and cable management",
            "telecommunications grounding when assigned",
            "voice/data outlets and patch panels",
            "audio-video systems when assigned",
            "paging and intercom when assigned",
        ],
        "include_terms": [
            "communications",
            "structured cabling",
            "data",
            "telecom",
            "fiber",
            "rack",
            "patch panel",
            "audio visual",
            "27 00",
        ],
        "spec_sections": [
            "27 00 00",
            "27 05 00",
            "27 10 00",
            "27 20 00",
            "27 30 00",
            "27 40 00",
            "27 50 00",
        ],
        "quantity_units": ["EA", "DROP", "LF", "LS"],
        "review_terms": ["owner equipment", "service provider", "pathway", "testing", "certification"],
        "exclude_terms": ["electrical power", "security", "fire alarm", "utility service provider"],
        "proposal_exclusions": [
            "active network equipment by owner unless listed",
            "service provider fees and work by others unless listed",
            "electrical power by others unless listed",
            "security and fire alarm systems by others unless listed",
        ],
    },
    {
        "division": "28",
        "title": "Electronic Safety and Security",
        "profile_id": "division-28-electronic-safety-security",
        "skill_description": (
            "Whole-division starter rules for CSI Division 28 - Electronic Safety and "
            "Security. Use when starting, triaging, validating, or packaging a commercial "
            "security, access control, CCTV, or fire alarm bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 28 - Electronic Safety and Security work "
            "specifically assigned to the bidder: access control, intrusion detection, "
            "video surveillance, electronic detection, fire alarm, and related safety "
            "systems. Door hardware, electrical power, network infrastructure, monitoring "
            "contracts, owner credentials, and fire protection must be explicitly included, "
            "excluded, or flagged before pricing."
        ),
        "base_scope": [
            "access control systems when assigned",
            "intrusion detection when assigned",
            "video surveillance when assigned",
            "fire alarm systems when assigned",
            "safety and security cabling when assigned",
            "head-end equipment and panels",
            "testing and certification when assigned",
        ],
        "include_terms": [
            "security",
            "access control",
            "card reader",
            "CCTV",
            "camera",
            "intrusion",
            "fire alarm",
            "detection",
            "28 00",
        ],
        "spec_sections": [
            "28 00 00",
            "28 05 00",
            "28 10 00",
            "28 13 00",
            "28 20 00",
            "28 31 00",
            "28 46 00",
        ],
        "quantity_units": ["EA", "LF", "DEVICE", "LS"],
        "review_terms": ["door hardware", "monitoring", "network", "permit", "programming"],
        "exclude_terms": ["electrical power", "door hardware", "locksmith", "sprinkler", "network switch"],
        "proposal_exclusions": [
            "door hardware by others unless listed",
            "electrical power by others unless listed",
            "monitoring contracts and fees unless listed",
            "owner network equipment unless listed",
        ],
    },
    {
        "division": "31",
        "title": "Earthwork",
        "profile_id": "division-31-earthwork",
        "skill_description": (
            "Whole-division starter rules for CSI Division 31 - Earthwork. Use when "
            "starting, triaging, validating, or packaging a commercial earthwork bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 31 - Earthwork work specifically assigned "
            "to the bidder: clearing, grading, excavation, fill, compaction, dewatering, "
            "earth retention, and subgrade preparation. Site utilities, paving, concrete, "
            "landscaping, contaminated soils, rock removal, and survey must be explicitly "
            "included, excluded, or flagged before pricing."
        ),
        "base_scope": [
            "site clearing when assigned",
            "mass excavation and grading",
            "trenching and backfill when assigned",
            "fill and compaction",
            "subgrade preparation",
            "dewatering when assigned",
            "earth retention when assigned",
        ],
        "include_terms": [
            "earthwork",
            "excavation",
            "grading",
            "fill",
            "backfill",
            "compaction",
            "subgrade",
            "dewatering",
            "31 00",
        ],
        "spec_sections": [
            "31 00 00",
            "31 10 00",
            "31 20 00",
            "31 23 00",
            "31 25 00",
            "31 31 00",
            "31 50 00",
        ],
        "quantity_units": ["CY", "SF", "LF", "TON", "ACRE"],
        "review_terms": ["rock", "unsuitable soils", "dewatering", "erosion control", "survey"],
        "exclude_terms": ["site utility", "asphalt paving", "concrete paving", "landscaping", "irrigation"],
        "proposal_exclusions": [
            "rock removal unless listed",
            "contaminated soils handling unless listed",
            "survey and staking by others unless listed",
            "import/export fees beyond listed quantities",
        ],
    },
    {
        "division": "32",
        "title": "Exterior Improvements",
        "profile_id": "division-32-exterior-improvements",
        "skill_description": (
            "Whole-division starter rules for CSI Division 32 - Exterior Improvements. "
            "Use when starting, triaging, validating, or packaging a commercial sitework, "
            "paving, landscaping, or fence bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 32 - Exterior Improvements work "
            "specifically assigned to the bidder: paving, pavement markings, site "
            "concrete when assigned, fences and gates, retaining walls, irrigation, "
            "planting, and exterior amenities. Earthwork, utilities, electrical power, "
            "structural concrete, and environmental work must be explicitly included, "
            "excluded, or flagged before pricing."
        ),
        "base_scope": [
            "asphalt and concrete paving when assigned",
            "pavement markings and signage when assigned",
            "fences and gates when assigned",
            "retaining walls when assigned",
            "irrigation when assigned",
            "planting and landscape restoration when assigned",
            "site furnishings and exterior amenities when assigned",
        ],
        "include_terms": [
            "exterior improvements",
            "paving",
            "asphalt",
            "pavement marking",
            "fence",
            "gate",
            "irrigation",
            "planting",
            "landscape",
            "32 00",
        ],
        "spec_sections": [
            "32 00 00",
            "32 01 00",
            "32 10 00",
            "32 12 00",
            "32 13 00",
            "32 17 00",
            "32 31 00",
            "32 80 00",
            "32 90 00",
        ],
        "quantity_units": ["SF", "SY", "LF", "EA", "TON"],
        "review_terms": ["earthwork", "electrical", "site utility", "tree protection", "maintenance"],
        "exclude_terms": ["storm drainage", "water utility", "electrical feeder", "building concrete"],
        "proposal_exclusions": [
            "earthwork and subgrade correction by others unless listed",
            "site utilities by others unless listed",
            "electrical power/control wiring by others unless listed",
            "landscape maintenance unless listed",
        ],
    },
    {
        "division": "33",
        "title": "Utilities",
        "profile_id": "division-33-utilities",
        "skill_description": (
            "Whole-division starter rules for CSI Division 33 - Utilities. Use when "
            "starting, triaging, validating, or packaging a commercial site utilities bid."
        ),
        "scope_rule": (
            "Base bid is limited to CSI Division 33 - Utilities work specifically assigned "
            "to the bidder: water, wells, sanitary sewerage, storm drainage, fuel, "
            "hydronic/steam energy, electrical utilities, and communications utilities. "
            "Building plumbing/electrical systems, earthwork beyond utility scope, paving "
            "restoration, permits, and utility company work must be explicitly included, "
            "excluded, or flagged before pricing."
        ),
        "base_scope": [
            "water utilities when assigned",
            "sanitary sewerage utilities when assigned",
            "storm drainage utilities when assigned",
            "fuel distribution utilities when assigned",
            "energy utilities when assigned",
            "electrical utilities when assigned",
            "communications utilities when assigned",
        ],
        "include_terms": [
            "utilities",
            "water utility",
            "sanitary sewer",
            "storm drainage",
            "fuel distribution",
            "electrical utility",
            "communications utility",
            "manhole",
            "33 00",
        ],
        "spec_sections": [
            "33 00 00",
            "33 05 00",
            "33 10 00",
            "33 20 00",
            "33 30 00",
            "33 40 00",
            "33 50 00",
            "33 70 00",
            "33 80 00",
        ],
        "quantity_units": ["LF", "EA", "CY", "TON", "LS"],
        "review_terms": ["utility company", "tap fee", "permit", "bypass pumping", "paving restoration"],
        "exclude_terms": ["building plumbing", "building electrical", "landscaping", "asphalt restoration"],
        "proposal_exclusions": [
            "utility company fees and work by others unless listed",
            "paving and landscape restoration unless listed",
            "rock removal and contaminated soils unless listed",
            "permits and inspection fees unless listed",
        ],
    },
)


def starter_profiles(*, company_name: str = "Your Company") -> list[dict[str, Any]]:
    profiles: list[dict[str, Any]] = []
    for seed in ACTIVE_CSI_DIVISIONS_03_33:
        division = seed["division"]
        title = seed["title"]
        profiles.append(
            {
                "schema_version": 1,
                "profile_id": seed["profile_id"],
                "company_name": company_name,
                "trade_name": f"Division {division} - {title}",
                "skill_description": seed["skill_description"],
                "csi_divisions": [division],
                "scope_rule": seed["scope_rule"],
                "base_scope": list(seed["base_scope"]),
                "include_terms": list(seed["include_terms"]),
                "spec_sections": list(seed["spec_sections"]),
                "quantity_units": list(seed["quantity_units"]),
                "review_terms": list(seed["review_terms"]),
                "exclude_terms": list(seed["exclude_terms"]),
                "proposal_exclusions": list(seed["proposal_exclusions"]),
            }
        )
    return profiles
