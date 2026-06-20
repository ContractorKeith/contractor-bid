from __future__ import annotations

import argparse
import sys
from datetime import date
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from . import __version__
from .doctor import format_doctor, run_doctor
from .learning import record_feedback
from .packets import build_packets
from .profile import build_profile, list_available_profiles, load_profile, parse_csv, write_profile
from .project import create_project, ensure_workspace
from .sendoff import package_sendoff
from .triage import triage_project
from .util import markdown_table
from .validate import deliverable_checklist, validate_project
from .workbook import build_workbook


def package_version() -> str:
    try:
        return version("contractor-bid")
    except PackageNotFoundError:
        return __version__


def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{prompt}{suffix}: ").strip()
    return value or default


def ask_list(prompt: str, default: list[str] | None = None) -> list[str]:
    default = default or []
    rendered = ", ".join(default)
    value = ask(prompt, rendered)
    return parse_csv(value)


def command_init(args: argparse.Namespace) -> int:
    root = args.root.resolve()
    ensure_workspace(root)
    if args.non_interactive:
        company = args.company or "Your Company"
        trade = args.trade or "Your Scope"
        scope_rule = args.scope_rule
        divisions = parse_csv(args.divisions)
        base_scope = parse_csv(args.base_scope)
        include_terms = parse_csv(args.include_terms)
        spec_sections = parse_csv(args.spec_sections)
        quantity_units = parse_csv(args.quantity_units)
        review_terms = parse_csv(args.review_terms)
        exclude_terms = parse_csv(args.exclude_terms)
        proposal_exclusions = parse_csv(args.proposal_exclusions)
    else:
        print("Create a reusable scope profile for your commercial bid workflow.\n")
        company = ask("Company name", args.company or "Your Company")
        trade = ask("Trade / scope name", args.trade or "Fences and Gates")
        scope_rule = ask(
            "Scope rule",
            args.scope_rule
            or (
                f"Base bid is limited to {trade}. Adjacent scopes must be explicitly "
                "included, excluded, or flagged before pricing."
            ),
        )
        divisions = ask_list("CSI division(s), comma-separated", parse_csv(args.divisions) or ["32"])
        base_scope = ask_list("Work you usually carry in base bid")
        include_terms = ask_list("Keywords/spec terms that identify your scope")
        spec_sections = ask_list("CSI spec section hints")
        quantity_units = ask_list("Quantity units you measure", ["EA", "LF", "SF", "CY"])
        review_terms = ask_list("Adjacent scope terms to flag before pricing")
        exclude_terms = ask_list("Adjacent scope terms to exclude by default")
        proposal_exclusions = ask_list("Standard proposal exclusions")

    profile = build_profile(
        company_name=company,
        trade_name=trade,
        profile_id=args.profile,
        scope_rule=scope_rule,
        divisions=divisions,
        base_scope=base_scope,
        include_terms=include_terms,
        spec_sections=spec_sections,
        quantity_units=quantity_units,
        review_terms=review_terms,
        exclude_terms=exclude_terms,
        proposal_exclusions=proposal_exclusions,
    )
    profile_file, skill_file = write_profile(root, profile)
    print(f"Wrote profile: {profile_file}")
    print(f"Wrote skill:   {skill_file}")
    return 0


def command_new(args: argparse.Namespace) -> int:
    root = args.root.resolve()
    ensure_workspace(root)
    profile = load_profile(args.profile, root)
    created = create_project(
        project_dir=args.project.resolve(),
        profile=profile,
        project_name=args.project_name,
        bid_due=args.bid_due,
        gc=args.gc,
        address=args.address,
    )
    print(f"Created bid project: {args.project.resolve()}")
    for path in created:
        print(f"- {path}")
    return 0


def command_triage(args: argparse.Namespace) -> int:
    root = args.root.resolve()
    profile = load_profile(args.profile, root)
    hits = triage_project(
        args.project.resolve(),
        profile,
        render=args.render,
        max_render=args.max_render,
        write_sources=args.write_sources,
    )
    print(f"Triage complete: {len(hits)} candidate page(s)")
    print(f"- {args.project.resolve() / 'bid-package-working' / 'takeoff' / 'candidate-pages.md'}")
    print(f"- {args.project.resolve() / 'bid-package-working' / 'takeoff' / 'triage-scope-signals.md'}")
    return 0


def command_build_packets(args: argparse.Namespace) -> int:
    result = build_packets(args.project.resolve(), sources=args.sources)
    print("Built page-packet artifacts")
    print(f"- Summary: {result['summary']}")
    print(f"- Scope pages: {result['scope_pages']}")
    print(f"- Spec pages: {result['spec_pages']}")
    return 0


def command_build_workbook(args: argparse.Namespace) -> int:
    profile = load_profile(args.profile, args.root.resolve()) if args.profile else None
    out = build_workbook(args.project.resolve(), profile=profile, config=args.config, out=args.out)
    print(f"Built workbook: {out}")
    return 0


def command_check(args: argparse.Namespace) -> int:
    profile = load_profile(args.profile, args.root.resolve())
    today = date.fromisoformat(args.today) if args.today else None
    out, exit_code, warnings, errors = validate_project(
        args.project.resolve(),
        profile,
        today=today,
        write=not args.no_write,
    )
    print(f"Wrote alerts: {out}")
    print(f"Warnings: {len(warnings)}")
    print(f"Hard errors: {len(errors)}")
    return exit_code


def command_status(args: argparse.Namespace) -> int:
    profile = load_profile(args.profile, args.root.resolve())
    today = date.fromisoformat(args.today) if args.today else None
    project = args.project.resolve()
    rows, _alerts, _errors = deliverable_checklist(project / "bid-package-working")
    _out, exit_code, warnings, errors = validate_project(
        project,
        profile,
        today=today,
        write=False,
    )
    print(f"Status for: {project}")
    print("")
    print("\n".join(markdown_table(["Status", "Deliverable", "Path"], rows)))
    print("")
    print(f"Warnings: {len(warnings)}")
    print(f"Hard errors: {len(errors)}")
    return exit_code


def command_package(args: argparse.Namespace) -> int:
    out_dir, zip_path = package_sendoff(args.project.resolve(), name=args.name)
    print(f"Built sendoff folder: {out_dir}")
    print(f"Built sendoff zip:    {zip_path}")
    return 0


def command_learn(args: argparse.Namespace) -> int:
    path = record_feedback(
        args.root.resolve(),
        note=args.note,
        project=str(args.project) if args.project else None,
        profile_id=args.profile,
        category=args.category,
    )
    print(f"Recorded feedback: {path}")
    return 0


def command_doctor(args: argparse.Namespace) -> int:
    checks, exit_code = run_doctor()
    print(format_doctor(checks))
    return exit_code


def command_list_profiles(args: argparse.Namespace) -> int:
    rows = list_available_profiles(args.root.resolve())
    if not rows:
        print("No profiles found.")
        return 1
    for profile_id, trade_name, source in rows:
        print(f"{profile_id} - {trade_name} ({source})")
    return 0


def command_run(args: argparse.Namespace) -> int:
    profile = load_profile(args.profile, args.root.resolve())
    project = args.project.resolve()

    packets = build_packets(project)
    print(f"Built page-packet artifacts: {packets['summary']}")

    workbook = build_workbook(project, profile=profile)
    print(f"Built workbook: {workbook}")

    today = date.fromisoformat(args.today) if args.today else None
    alerts, exit_code, warnings, errors = validate_project(project, profile, today=today)
    print(f"Wrote alerts: {alerts}")
    print(f"Warnings: {len(warnings)}")
    print(f"Hard errors: {len(errors)}")

    out_dir, zip_path = package_sendoff(project, name=args.name)
    print(f"Built sendoff folder: {out_dir}")
    print(f"Built sendoff zip:    {zip_path}")
    return exit_code


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="contractor-bid",
        description="Create and maintain AI-ready commercial subcontractor bid projects.",
    )
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Workspace root containing profiles/ and skills/.")
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {package_version()}",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    list_profiles = sub.add_parser("list-profiles", help="List built-in and workspace profiles.")
    list_profiles.set_defaults(func=command_list_profiles)

    init = sub.add_parser("init", help="Create a reusable scope profile and generated agent skill.")
    init.add_argument("--profile", default=None, help="Profile id, e.g. fences-gates or concrete.")
    init.add_argument("--company", default=None)
    init.add_argument("--trade", default=None)
    init.add_argument("--divisions", default="")
    init.add_argument("--base-scope", default="")
    init.add_argument("--include-terms", default="")
    init.add_argument("--spec-sections", default="")
    init.add_argument("--quantity-units", default="")
    init.add_argument("--review-terms", default="")
    init.add_argument("--exclude-terms", default="")
    init.add_argument("--proposal-exclusions", default="")
    init.add_argument("--scope-rule", default=None)
    init.add_argument("--non-interactive", action="store_true")
    init.set_defaults(func=command_init)

    new = sub.add_parser("new", help="Create a bid project folder from a scope profile.")
    new.add_argument("project", type=Path)
    new.add_argument("--profile", required=True, help="Profile id or path to profile JSON.")
    new.add_argument("--project-name", default=None)
    new.add_argument("--bid-due", default=None)
    new.add_argument("--gc", default=None)
    new.add_argument("--address", default=None)
    new.set_defaults(func=command_new)

    triage = sub.add_parser("triage", help="Extract PDF text and score candidate scope pages.")
    triage.add_argument("project", type=Path)
    triage.add_argument("--profile", required=True)
    triage.add_argument("--render", action="store_true", help="Render top candidate pages with pdftoppm when available.")
    triage.add_argument("--max-render", type=int, default=20)
    triage.add_argument(
        "--write-sources",
        action="store_true",
        help="Copy suggested scope pages into the canonical sources JSON only if it is empty.",
    )
    triage.set_defaults(func=command_triage)

    packets = sub.add_parser("build-packets", help="Build scope/spec page PDFs and quick-read summary.")
    packets.add_argument("project", type=Path)
    packets.add_argument("--sources", type=Path, default=None)
    packets.set_defaults(func=command_build_packets)

    workbook = sub.add_parser("build-workbook", help="Build takeoff/BOM workbook from JSON.")
    workbook.add_argument("project", type=Path)
    workbook.add_argument("--profile", default=None)
    workbook.add_argument("--config", type=Path, default=None)
    workbook.add_argument("--out", type=Path, default=None)
    workbook.set_defaults(func=command_build_workbook)

    check = sub.add_parser("check", help="Validate required bid package artifacts and scope guardrails.")
    check.add_argument("project", type=Path)
    check.add_argument("--profile", required=True)
    check.add_argument("--today", default=None, help="Override date for due-date math, YYYY-MM-DD.")
    check.add_argument("--no-write", action="store_true")
    check.set_defaults(func=command_check)

    status = sub.add_parser("status", help="Show bid package status without writing ALERTS.md.")
    status.add_argument("project", type=Path)
    status.add_argument("--profile", required=True)
    status.add_argument("--today", default=None, help="Override date for due-date math, YYYY-MM-DD.")
    status.set_defaults(func=command_status)

    package = sub.add_parser("package-sendoff", help="Create supplier/partner sendoff folder and zip.")
    package.add_argument("project", type=Path)
    package.add_argument("--name", default=None)
    package.set_defaults(func=command_package)

    run = sub.add_parser("run", help="Run packets, workbook, validation, and sendoff packaging.")
    run.add_argument("project", type=Path)
    run.add_argument("--profile", required=True)
    run.add_argument("--today", default=None, help="Override date for due-date math, YYYY-MM-DD.")
    run.add_argument("--name", default=None, help="Optional sendoff package name.")
    run.set_defaults(func=command_run)

    learn = sub.add_parser("learn", help="Record a correction or reusable lesson for future bids.")
    learn.add_argument("--note", required=True)
    learn.add_argument("--project", type=Path, default=None)
    learn.add_argument("--profile", default=None)
    learn.add_argument("--category", default="correction")
    learn.set_defaults(func=command_learn)

    doctor = sub.add_parser("doctor", help="Check local dependencies and optional PDF tools.")
    doctor.set_defaults(func=command_doctor)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except KeyboardInterrupt:
        return 130
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
