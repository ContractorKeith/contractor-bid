import os
from contextlib import redirect_stdout
from datetime import date
from io import StringIO
from pathlib import Path
from typing import Annotated, Any, Literal

try:
    from pydantic import BaseModel, Field
    from mcp.server.fastmcp import FastMCP
    from mcp.types import ToolAnnotations
except ImportError as exc:  # pragma: no cover - exercised when the extra is absent.
    raise SystemExit(
        "contractor-bid MCP support requires the optional MCP extra. "
        'Install with: pipx install "contractor-bid[mcp]"'
    ) from exc

from .doctor import format_doctor, run_doctor
from .learning import record_feedback
from .packets import build_packets
from .profile import list_available_profiles, load_profile
from .project import create_project, ensure_workspace
from .sendoff import package_sendoff
from .tracker import (
    active_bids,
    add_or_update,
    archived_bids,
    change_summary,
    find_entry,
    load_tracker,
    move_entry,
    render_tracker,
    tracker_paths,
)
from .triage import triage_project
from .validate import validate_project
from .workbook import build_workbook


WORKSPACE_ENV = "CONTRACTOR_BID_WORKSPACE"

WorkspaceRoot = Annotated[
    str,
    Field(
        description=(
            "Optional workspace root containing profiles/, skills/, and bid projects. "
            f"Defaults to ${WORKSPACE_ENV}, then the current working directory."
        )
    ),
]
ProjectPath = Annotated[
    str,
    Field(description="Bid project path. Relative paths are resolved under the workspace root."),
]
ProfileId = Annotated[
    str,
    Field(description="Scope profile id, for example division-26-electrical or fences-gates."),
]


class ToolResponse(BaseModel):
    status: Literal["ok", "warning", "error"] = Field(
        description="Overall result status for the agent to surface to the user."
    )
    artifacts: list[str] = Field(
        default_factory=list,
        description="Files or folders produced or updated by this tool.",
    )
    summary: str = Field(description="Short human-readable result summary.")
    alerts: list[str] = Field(
        default_factory=list,
        description="Warnings, validation findings, or actionable error guidance.",
    )
    next_suggested_tool: str | None = Field(
        default=None,
        description="Next MCP tool the agent should usually call in this workflow.",
    )
    data: dict[str, Any] = Field(
        default_factory=dict,
        description="Structured result details for agents and tests.",
    )


def _dump(response: ToolResponse) -> dict[str, Any]:
    return response.model_dump(mode="json")


def _artifact(path: Path) -> str:
    return str(path.expanduser().resolve())


def _workspace_root(workspace_root: str | None = None) -> Path:
    raw = workspace_root or os.environ.get(WORKSPACE_ENV) or os.getcwd()
    return Path(raw).expanduser().resolve()


def _resolve_project(project: str, workspace_root: str | None = None) -> Path:
    raw = Path(project).expanduser()
    if raw.is_absolute():
        return raw.resolve()
    return (_workspace_root(workspace_root) / raw).resolve()


def _resolve_optional_path(path: str | None, base: Path) -> Path | None:
    if not path:
        return None
    raw = Path(path).expanduser()
    if raw.is_absolute():
        return raw.resolve()
    return (base / raw).resolve()


def _nearby_projects(root: Path) -> list[str]:
    if not root.is_dir():
        return []
    nearby: list[str] = []
    for path in sorted(root.iterdir()):
        if path.is_dir() and not path.name.startswith("."):
            nearby.append(path.name)
        if len(nearby) >= 10:
            break
    return nearby


def _profile_rows(root: Path) -> list[dict[str, str]]:
    return [
        {"profile_id": profile_id, "trade_name": trade_name, "source": source}
        for profile_id, trade_name, source in list_available_profiles(root)
    ]


def _load_profile(profile: str, root: Path) -> dict[str, Any]:
    try:
        return load_profile(profile, root)
    except FileNotFoundError as exc:
        valid = ", ".join(row["profile_id"] for row in _profile_rows(root)) or "none found"
        raise FileNotFoundError(f"{exc}. Valid profiles: {valid}") from exc


def _require_project(path: Path, root: Path) -> None:
    if path.exists():
        return
    nearby = ", ".join(_nearby_projects(root)) or "no nearby project folders found"
    raise FileNotFoundError(f"Project folder not found: {path}. Nearby folders: {nearby}")


def _known_error(exc: Exception) -> list[str]:
    text = str(exc)
    if "Poppler" in text or "pdftotext" in text or "pdftoppm" in text:
        return [
            text,
            "Run cb_doctor, then install Poppler if PDF text extraction or rendering is missing.",
        ]
    if "No PDFs found" in text:
        return [text, "Put source PDF files in bid-docs/ before running cb_triage."]
    if "Scope profile not found" in text:
        return [text, "Run cb_list_profiles to choose a built-in or workspace profile."]
    return [text]


def _error_response(exc: Exception) -> dict[str, Any]:
    return _dump(ToolResponse(status="error", summary=str(exc), alerts=_known_error(exc)))


def _tracker_artifacts(root: Path) -> list[str]:
    json_path, xlsx_path = tracker_paths(root)
    artifacts = [json_path]
    if xlsx_path.exists():
        artifacts.append(xlsx_path)
    return [_artifact(path) for path in artifacts]


def _proposal_response(summary: str, data: dict[str, Any]) -> dict[str, Any]:
    return _dump(
        ToolResponse(
            status="warning",
            summary=summary,
            alerts=[
                "This is a proposed tracker write only. Confirm with the user, then call "
                "the same tool with confirm=true to write it."
            ],
            data=data,
        )
    )


mcp = FastMCP(
    "contractor-bid",
    instructions=(
        "Use these tools to create and maintain source-backed commercial subcontractor "
        "bid workspaces. Triage output is a starting point, not a pricing decision."
    ),
)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Check contractor-bid environment",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
    )
)
def cb_doctor(workspace_root: WorkspaceRoot = "") -> dict[str, Any]:
    """Check Python, package, and PDF tool dependencies for contractor-bid."""
    root = _workspace_root(workspace_root)
    checks, exit_code = run_doctor()
    alerts = [f"{check.name}: {check.detail}" for check in checks if not check.ok]
    status: Literal["ok", "warning", "error"] = "error" if exit_code else ("warning" if alerts else "ok")
    return _dump(
        ToolResponse(
            status=status,
            summary="contractor-bid environment check complete.",
            alerts=alerts,
            data={
                "workspace_root": str(root),
                "formatted": format_doctor(checks),
                "checks": [check.__dict__ for check in checks],
            },
        )
    )


@mcp.tool(
    annotations=ToolAnnotations(
        title="List contractor-bid profiles",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
    )
)
def cb_list_profiles(workspace_root: WorkspaceRoot = "") -> dict[str, Any]:
    """List built-in and workspace scope profiles."""
    root = _workspace_root(workspace_root)
    rows = _profile_rows(root)
    if not rows:
        return _dump(
            ToolResponse(
                status="warning",
                summary="No scope profiles found.",
                alerts=["Run contractor-bid init to create a workspace profile."],
                data={"workspace_root": str(root), "profiles": []},
            )
        )
    return _dump(
        ToolResponse(
            status="ok",
            summary=f"Found {len(rows)} scope profile(s).",
            data={"workspace_root": str(root), "profiles": rows},
        )
    )


@mcp.tool(
    annotations=ToolAnnotations(
        title="Create bid project",
        readOnlyHint=False,
        destructiveHint=False,
        idempotentHint=False,
    )
)
def cb_new_project(
    project: ProjectPath,
    profile: ProfileId,
    workspace_root: WorkspaceRoot = "",
    project_name: Annotated[str, Field(description="Display name for the bid project.")] = "",
    bid_due: Annotated[str, Field(description="Bid due date/time, if known.")] = "",
    gc: Annotated[str, Field(description="General contractor or client contact.")] = "",
    address: Annotated[str, Field(description="Project address or location.")] = "",
) -> dict[str, Any]:
    """Scaffold a bid project folder from a scope profile."""
    try:
        root = _workspace_root(workspace_root)
        ensure_workspace(root)
        profile_data = _load_profile(profile, root)
        project_path = _resolve_project(project, workspace_root)
        created = create_project(
            project_dir=project_path,
            profile=profile_data,
            project_name=project_name,
            bid_due=bid_due,
            gc=gc,
            address=address,
        )
        return _dump(
            ToolResponse(
                status="ok",
                artifacts=[_artifact(path) for path in created],
                summary=f"Created bid project: {project_path}",
                next_suggested_tool="cb_triage",
                data={"project": str(project_path), "profile": profile_data["profile_id"]},
            )
        )
    except Exception as exc:
        return _error_response(exc)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Triage bid documents",
        readOnlyHint=False,
        destructiveHint=False,
        idempotentHint=True,
    )
)
def cb_triage(
    project: ProjectPath,
    profile: ProfileId,
    workspace_root: WorkspaceRoot = "",
    render: Annotated[
        bool,
        Field(description="Render top candidate pages as PNGs when pdftoppm is installed."),
    ] = False,
    max_render: Annotated[
        int,
        Field(ge=0, le=200, description="Maximum number of candidate pages to render."),
    ] = 20,
    write_sources: Annotated[
        bool,
        Field(
            description=(
                "Copy suggested scope pages into scope-pages-sources.json only when the "
                "canonical file is empty."
            )
        ),
    ] = False,
) -> dict[str, Any]:
    """Extract PDF text and score likely scope/spec pages for review."""
    try:
        root = _workspace_root(workspace_root)
        project_path = _resolve_project(project, workspace_root)
        _require_project(project_path, root)
        profile_data = _load_profile(profile, root)
        stdout = StringIO()
        with redirect_stdout(stdout):
            hits = triage_project(
                project_path,
                profile_data,
                render=render,
                max_render=max_render,
                write_sources=write_sources,
            )
        work = project_path / "bid-package-working"
        artifacts = [
            work / "text-extracts" / "page-hits.json",
            work / "text-extracts" / "page-hits.csv",
            work / "text-extracts" / "scope-signals.json",
            work / "takeoff" / "candidate-pages.md",
            work / "takeoff" / "triage-scope-signals.md",
            work / "takeoff" / "scope-pages-sources.suggested.json",
        ]
        if write_sources:
            artifacts.append(work / "takeoff" / "scope-pages-sources.json")
        output_lines = [line for line in stdout.getvalue().splitlines() if line.strip()]
        alerts = [line for line in output_lines if "WARNING:" in line or "Skipped" in line]
        status: Literal["ok", "warning", "error"] = "ok"
        summary = f"Triage complete: {len(hits)} candidate page(s)."
        if not hits:
            status = "warning"
            alerts.append(
                "No candidate pages found. The plan set may be image-only/OCR is not yet "
                "supported, or the selected profile terms did not match these PDFs."
            )
        return _dump(
            ToolResponse(
                status=status,
                artifacts=[_artifact(path) for path in artifacts if path.exists()],
                summary=summary,
                alerts=alerts,
                next_suggested_tool="cb_build_packets",
                data={
                    "project": str(project_path),
                    "profile": profile_data["profile_id"],
                    "candidate_pages": len(hits),
                    "hits": [hit.__dict__ for hit in hits],
                    "stdout": output_lines,
                },
            )
        )
    except Exception as exc:
        return _error_response(exc)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Build page packets",
        readOnlyHint=False,
        destructiveHint=False,
        idempotentHint=True,
    )
)
def cb_build_packets(
    project: ProjectPath,
    workspace_root: WorkspaceRoot = "",
    sources: Annotated[
        str,
        Field(
            description=(
                "Optional sources JSON path. Relative paths resolve under the bid project folder."
            )
        ),
    ] = "",
) -> dict[str, Any]:
    """Build scope/spec packet PDFs and the bid scope summary."""
    try:
        root = _workspace_root(workspace_root)
        project_path = _resolve_project(project, workspace_root)
        _require_project(project_path, root)
        sources_path = _resolve_optional_path(sources, project_path)
        result = build_packets(project_path, sources=sources_path)
        work = project_path / "bid-package-working"
        artifacts = [
            Path(result["summary"]),
            work / "scope-pages.pdf",
            work / "scope-pages-index.md",
            work / "spec-pages.pdf",
            work / "spec-pages-index.md",
            work / "scope-and-spec-pages.pdf",
        ]
        status: Literal["ok", "warning", "error"] = "ok"
        alerts: list[str] = []
        if not result["scope_pages"] and not result["spec_pages"]:
            status = "warning"
            alerts.append(
                "No scope_pages[] or spec_pages[] were approved yet. Review triage suggestions "
                "and fill bid-package-working/takeoff/scope-pages-sources.json."
            )
        return _dump(
            ToolResponse(
                status=status,
                artifacts=[_artifact(path) for path in artifacts if path.exists()],
                summary=(
                    f"Built page-packet artifacts: {result['scope_pages']} scope page(s), "
                    f"{result['spec_pages']} spec page(s)."
                ),
                alerts=alerts,
                next_suggested_tool="cb_build_workbook",
                data=result,
            )
        )
    except Exception as exc:
        return _error_response(exc)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Build takeoff workbook",
        readOnlyHint=False,
        destructiveHint=False,
        idempotentHint=True,
    )
)
def cb_build_workbook(
    project: ProjectPath,
    workspace_root: WorkspaceRoot = "",
    profile: Annotated[
        str,
        Field(description="Optional scope profile id used for scope guard checks."),
    ] = "",
    config: Annotated[
        str,
        Field(description="Optional takeoff JSON path. Relative paths resolve under the project."),
    ] = "",
    out: Annotated[
        str,
        Field(description="Optional output workbook path. Relative paths resolve under the project."),
    ] = "",
) -> dict[str, Any]:
    """Build the takeoff/BOM workbook from the project takeoff JSON."""
    try:
        root = _workspace_root(workspace_root)
        project_path = _resolve_project(project, workspace_root)
        _require_project(project_path, root)
        profile_data = _load_profile(profile, root) if profile else None
        config_path = _resolve_optional_path(config, project_path)
        out_path = _resolve_optional_path(out, project_path)
        workbook = build_workbook(project_path, profile=profile_data, config=config_path, out=out_path)
        return _dump(
            ToolResponse(
                status="ok",
                artifacts=[_artifact(workbook)],
                summary=f"Built workbook: {workbook}",
                next_suggested_tool="cb_check",
                data={"project": str(project_path), "workbook": str(workbook)},
            )
        )
    except Exception as exc:
        return _error_response(exc)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Check bid package",
        readOnlyHint=False,
        destructiveHint=False,
        idempotentHint=True,
    )
)
def cb_check(
    project: ProjectPath,
    profile: ProfileId,
    workspace_root: WorkspaceRoot = "",
    today: Annotated[
        str,
        Field(description="Optional date override for due-date math, formatted YYYY-MM-DD."),
    ] = "",
    write_alerts: Annotated[
        bool,
        Field(description="Write ALERTS.md. Set false for status-only validation."),
    ] = True,
) -> dict[str, Any]:
    """Validate required artifacts and scope guardrails for a bid package."""
    try:
        root = _workspace_root(workspace_root)
        project_path = _resolve_project(project, workspace_root)
        _require_project(project_path, root)
        profile_data = _load_profile(profile, root)
        today_value = date.fromisoformat(today) if today else None
        out, exit_code, warnings, errors = validate_project(
            project_path,
            profile_data,
            today=today_value,
            write=write_alerts,
        )
        status: Literal["ok", "warning", "error"] = "error" if exit_code else "ok"
        if warnings and status == "ok":
            status = "warning"
        artifacts = [_artifact(out)] if write_alerts and out.exists() else []
        return _dump(
            ToolResponse(
                status=status,
                artifacts=artifacts,
                summary=f"Validation complete: {len(warnings)} warning(s), {len(errors)} hard error(s).",
                alerts=[*warnings, *errors],
                next_suggested_tool=None if errors else "cb_package_sendoff",
                data={
                    "project": str(project_path),
                    "alerts_path": str(out),
                    "warnings": warnings,
                    "errors": errors,
                    "exit_code": exit_code,
                },
            )
        )
    except Exception as exc:
        return _error_response(exc)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Package supplier sendoff",
        readOnlyHint=False,
        destructiveHint=False,
        idempotentHint=True,
    )
)
def cb_package_sendoff(
    project: ProjectPath,
    workspace_root: WorkspaceRoot = "",
    name: Annotated[str, Field(description="Optional sendoff package folder/zip name.")] = "",
) -> dict[str, Any]:
    """Build the supplier/internal-review sendoff folder and zip."""
    try:
        root = _workspace_root(workspace_root)
        project_path = _resolve_project(project, workspace_root)
        _require_project(project_path, root)
        out_dir, zip_path = package_sendoff(project_path, name=name)
        return _dump(
            ToolResponse(
                status="ok",
                artifacts=[_artifact(out_dir), _artifact(zip_path)],
                summary=f"Built sendoff package: {zip_path}",
                data={"project": str(project_path), "sendoff_dir": str(out_dir), "zip": str(zip_path)},
            )
        )
    except Exception as exc:
        return _error_response(exc)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Record bid workflow lesson",
        readOnlyHint=False,
        destructiveHint=False,
        idempotentHint=False,
    )
)
def cb_learn(
    note: Annotated[str, Field(description="Correction or lesson to append to feedback.jsonl.")],
    workspace_root: WorkspaceRoot = "",
    project: Annotated[
        str,
        Field(description="Optional related bid project path."),
    ] = "",
    profile: Annotated[str, Field(description="Optional related profile id.")] = "",
    category: Annotated[str, Field(description="Feedback category label.")] = "correction",
) -> dict[str, Any]:
    """Append a correction or reusable lesson to the workspace feedback log."""
    try:
        root = _workspace_root(workspace_root)
        project_ref = str(_resolve_project(project, workspace_root)) if project else None
        path = record_feedback(root, note=note, project=project_ref, profile_id=profile, category=category)
        return _dump(
            ToolResponse(
                status="ok",
                artifacts=[_artifact(path)],
                summary=f"Recorded feedback: {path}",
                data={"feedback_log": str(path), "category": category},
            )
        )
    except Exception as exc:
        return _error_response(exc)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Propose or add tracker bid",
        readOnlyHint=False,
        destructiveHint=False,
        idempotentHint=False,
    )
)
def cb_track_add(
    workspace_root: WorkspaceRoot = "",
    project: Annotated[
        str | None,
        Field(description="Optional bid project folder to pull project.json fields from."),
    ] = None,
    id: Annotated[str | None, Field(description="Optional explicit bid id/slug.")] = None,
    name: Annotated[str | None, Field(description="Project name when not using a project folder.")] = None,
    location: Annotated[str | None, Field(description="Project location/address.")] = None,
    due: Annotated[str | None, Field(description="Bid due date or date/time.")] = None,
    progress: Annotated[str | None, Field(description="Tracker progress stage.")] = None,
    next_action: Annotated[str | None, Field(description="Next action to take.")] = None,
    gc: Annotated[str | None, Field(description="Client / GC contact.")] = None,
    profile: Annotated[str | None, Field(description="Scope profile id.")] = None,
    note: Annotated[str | None, Field(description="Optional dated note to append.")] = None,
    confirm: Annotated[
        bool,
        Field(description="Must be true after user confirmation before this tool writes."),
    ] = False,
) -> dict[str, Any]:
    """Add a bid to the workspace tracker after explicit confirmation."""
    try:
        root = _workspace_root(workspace_root)
        project_path = _resolve_project(project, workspace_root) if project else None
        proposed = {
            "project": str(project_path) if project_path else name,
            "id": id,
            "location": location,
            "due": due,
            "progress": progress,
            "next_action": next_action,
            "gc": gc,
            "profile": profile,
            "note": note,
        }
        if not confirm:
            label = name or (project_path.name if project_path else id) or "new bid"
            return _proposal_response(f"Proposed tracker add/update for '{label}'.", proposed)
        ensure_workspace(root)
        entry, created, changed = add_or_update(
            root,
            project_path=project_path,
            id=id,
            name=name,
            location=location,
            due_date=due,
            progress=progress,
            next_action=next_action,
            client_gc=gc,
            profile=profile,
            note=note,
        )
        render_tracker(root)
        return _dump(
            ToolResponse(
                status="ok",
                artifacts=_tracker_artifacts(root),
                summary=change_summary(entry, created, changed),
                data={"entry": entry, "created": created, "changed": changed},
            )
        )
    except Exception as exc:
        return _error_response(exc)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Propose or update tracker bid",
        readOnlyHint=False,
        destructiveHint=False,
        idempotentHint=True,
    )
)
def cb_track_update(
    bid: Annotated[str, Field(description="Bid id or exact project name to update.")],
    workspace_root: WorkspaceRoot = "",
    location: Annotated[str | None, Field(description="Project location/address.")] = None,
    due: Annotated[str | None, Field(description="Bid due date or date/time.")] = None,
    progress: Annotated[str | None, Field(description="Tracker progress stage.")] = None,
    next_action: Annotated[str | None, Field(description="Next action to take.")] = None,
    gc: Annotated[str | None, Field(description="Client / GC contact.")] = None,
    note: Annotated[str | None, Field(description="Optional dated note to append.")] = None,
    confirm: Annotated[
        bool,
        Field(description="Must be true after user confirmation before this tool writes."),
    ] = False,
) -> dict[str, Any]:
    """Update an existing tracker bid after explicit confirmation."""
    try:
        root = _workspace_root(workspace_root)
        data = load_tracker(root)
        existing = find_entry(data, bid)
        if existing is None:
            raise ValueError(f"No bid found matching: {bid}")
        proposed = {
            "bid": bid,
            "location": location,
            "due": due,
            "progress": progress,
            "next_action": next_action,
            "gc": gc,
            "note": note,
        }
        if not confirm:
            return _proposal_response(
                f"Proposed tracker update for '{existing.get('project', bid)}'.",
                proposed,
            )
        ensure_workspace(root)
        entry, created, changed = add_or_update(
            root,
            id=bid,
            location=location,
            due_date=due,
            progress=progress,
            next_action=next_action,
            client_gc=gc,
            note=note,
        )
        render_tracker(root)
        return _dump(
            ToolResponse(
                status="ok",
                artifacts=_tracker_artifacts(root),
                summary=change_summary(entry, created, changed),
                data={"entry": entry, "created": created, "changed": changed},
            )
        )
    except Exception as exc:
        return _error_response(exc)


@mcp.tool(
    annotations=ToolAnnotations(
        title="Propose or archive tracker bid",
        readOnlyHint=False,
        destructiveHint=False,
        idempotentHint=True,
    )
)
def cb_track_move(
    bid: Annotated[str, Field(description="Bid id or exact project name to archive.")],
    outcome: Annotated[str, Field(description="Archive outcome: completed, won, lost, or no-bid.")] = "completed",
    workspace_root: WorkspaceRoot = "",
    confirm: Annotated[
        bool,
        Field(description="Must be true after user confirmation before this tool writes."),
    ] = False,
) -> dict[str, Any]:
    """Move a tracker bid to archived/completed after explicit confirmation."""
    try:
        root = _workspace_root(workspace_root)
        data = load_tracker(root)
        existing = find_entry(data, bid)
        if existing is None:
            raise ValueError(f"No bid found matching: {bid}")
        if outcome not in {"completed", "won", "lost", "no-bid"}:
            raise ValueError("outcome must be one of: completed, won, lost, no-bid")
        if not confirm:
            return _proposal_response(
                f"Proposed moving '{existing.get('project', bid)}' to archive as {outcome}.",
                {"bid": bid, "outcome": outcome},
            )
        ensure_workspace(root)
        entry = move_entry(root, bid, outcome=outcome)
        render_tracker(root)
        return _dump(
            ToolResponse(
                status="ok",
                artifacts=_tracker_artifacts(root),
                summary=(
                    f"Moved '{entry.get('project')}' to Archived/Completed "
                    f"(outcome={entry.get('outcome')})."
                ),
                data={"entry": entry},
            )
        )
    except Exception as exc:
        return _error_response(exc)


@mcp.tool(
    annotations=ToolAnnotations(
        title="List tracker bids",
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
    )
)
def cb_track_list(
    workspace_root: WorkspaceRoot = "",
    include_archived: Annotated[
        bool,
        Field(description="Include archived/completed bids in the response."),
    ] = False,
) -> dict[str, Any]:
    """List active and optionally archived tracker bids."""
    try:
        root = _workspace_root(workspace_root)
        data = load_tracker(root)
        active = active_bids(data)
        archived = archived_bids(data) if include_archived else []
        return _dump(
            ToolResponse(
                status="ok",
                summary=f"Tracker has {len(active)} active bid(s) and {len(archived)} archived bid(s).",
                data={
                    "active": active,
                    "archived": archived,
                    "include_archived": include_archived,
                },
            )
        )
    except Exception as exc:
        return _error_response(exc)


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
