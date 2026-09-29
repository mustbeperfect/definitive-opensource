from __future__ import annotations

import json
from pathlib import Path
import sys

CORE_DIR = Path(__file__).resolve().parents[2]
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))

from source.utils.path_utils import DYNAMIC_DATA_DIR, MAINTENANCE_DIR, STATIC_DATA_DIR  # noqa: E402

VALID_FLAGS = {"custom-description", "custom-license", "custom-homepage"}
VALID_ARCHIVE_REASONS = {
    "closed-source",
    "closed source",
    "abandoned",
    "archived",
    "deleted",
}


def validate_categories(
    categories_path: Path,
) -> tuple[list[dict], set[str], set[str]]:
    """Validate categories.json for missing fields, duplicate IDs, and relationships."""
    issues: list[dict] = []
    valid_subcategories: set[str] = set()
    valid_categories: set[str] = set()

    if not categories_path.exists():
        return (
            [{"name": categories_path.name, "issues": ["File not found"]}],
            valid_subcategories,
            valid_categories,
        )

    with open(categories_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    categories = data.get("categories", [])
    subcategories = data.get("subcategories", [])

    seen_cat_ids: set[str] = set()
    for cat in categories:
        cat_issues: list[str] = []
        cat_id = cat.get("id", "").strip().lower()
        cat_name = cat.get("name", "").strip() or cat_id or "Unnamed Category"

        if not cat_id:
            cat_issues.append("Missing category ID")
        elif cat_id in seen_cat_ids:
            cat_issues.append(f"Duplicate category ID '{cat_id}'")
        else:
            seen_cat_ids.add(cat_id)
            valid_categories.add(cat_id)

        if not cat.get("name", "").strip():
            cat_issues.append("Missing category name")

        if cat_issues:
            issues.append({"name": cat_name, "issues": cat_issues})

    seen_subcat_ids: set[str] = set()
    for subcat in subcategories:
        subcat_issues: list[str] = []
        subcat_id = subcat.get("id", "").strip().lower()
        subcat_name = (
            subcat.get("name", "").strip() or subcat_id or "Unnamed Subcategory"
        )

        if not subcat_id:
            subcat_issues.append("Missing subcategory ID")
        elif subcat_id in seen_subcat_ids:
            subcat_issues.append(f"Duplicate subcategory ID '{subcat_id}'")
        else:
            seen_subcat_ids.add(subcat_id)
            valid_subcategories.add(subcat_id)

        if subcat_id and subcat_id in seen_cat_ids:
            subcat_issues.append(
                f"Subcategory ID '{subcat_id}' conflicts with category ID"
            )

        if not subcat.get("name", "").strip():
            subcat_issues.append("Missing subcategory name")

        parent = subcat.get("parent", "").strip().lower()
        valid_parent_ids = seen_cat_ids | {"other"}
        if not parent:
            subcat_issues.append("Missing parent category")
        elif seen_cat_ids and parent not in valid_parent_ids:
            subcat_issues.append(f"Invalid parent category '{parent}'")

        if subcat_issues:
            issues.append({"name": subcat_name, "issues": subcat_issues})

    return issues, valid_subcategories, valid_categories


def validate_platforms(platforms_path: Path) -> tuple[list[dict], set[str]]:
    """Validate platforms.json for missing fields and duplicate IDs."""
    issues: list[dict] = []
    valid_platforms: set[str] = set()

    if not platforms_path.exists():
        return (
            [{"name": platforms_path.name, "issues": ["File not found"]}],
            valid_platforms,
        )

    with open(platforms_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    platforms = data.get("platforms", [])
    seen_platforms: set[str] = set()

    for platform in platforms:
        plat_issues: list[str] = []
        p_id = platform.get("id", "").strip().lower()
        p_name = platform.get("name", "").strip() or p_id or "Unnamed Platform"

        if not p_id:
            plat_issues.append("Missing platform ID")
        elif p_id in seen_platforms:
            plat_issues.append(f"Duplicate platform ID '{p_id}'")
        else:
            seen_platforms.add(p_id)
            valid_platforms.add(p_id)

        if not platform.get("name", "").strip():
            plat_issues.append("Missing platform name")

        if plat_issues:
            issues.append({"name": p_name, "issues": plat_issues})

    return issues, valid_platforms


def validate_tags(tags_path: Path) -> tuple[list[dict], set[str]]:
    """Validate tags.json for missing fields and duplicate IDs."""
    issues: list[dict] = []
    valid_tags: set[str] = set()

    if not tags_path.exists():
        return [{"name": tags_path.name, "issues": ["File not found"]}], valid_tags

    with open(tags_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    attributes = data.get("attributes", [])
    properties = data.get("properties", [])
    all_tags = attributes + properties

    seen_tags: set[str] = set()
    for tag in all_tags:
        tag_issues: list[str] = []
        t_id = tag.get("id", "").strip().lower()
        t_name = tag.get("description", tag.get("name", t_id)) or "Unnamed Tag"

        if not t_id:
            tag_issues.append("Missing tag ID")
        elif t_id in seen_tags:
            tag_issues.append(f"Duplicate tag ID '{t_id}'")
        else:
            seen_tags.add(t_id)
            valid_tags.add(t_id)

        if tag_issues:
            issues.append({"name": t_name, "issues": tag_issues})

    return issues, valid_tags


def validate_applications(
    applications_path: Path,
    valid_categories: set[str],
    valid_platforms: set[str],
    valid_tags: set[str],
    valid_flags: set[str],
) -> tuple[list[dict], set[str], set[str]]:
    """Validate applications.json for required fields, valid relationships, and duplicates."""
    issues: list[dict] = []
    seen_github: set[str] = set()
    seen_names: set[str] = set()

    if not applications_path.exists():
        return (
            [{"name": applications_path.name, "issues": ["File not found"]}],
            seen_github,
            seen_names,
        )

    with open(applications_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    applications = data.get("applications", [])

    for app in applications:
        app_issues: list[str] = []
        name = app.get("name", "").strip()

        if not name:
            app_issues.append("Missing application name")
        elif name.lower() in seen_names:
            app_issues.append("Duplicate application name")
        else:
            seen_names.add(name.lower())

        github_url = app.get("repo_url", "").strip()
        if not github_url:
            app_issues.append("Missing GitHub URL")
        elif github_url.lower() in seen_github:
            app_issues.append("Duplicate GitHub URL")
        else:
            seen_github.add(github_url.lower())

        category = app.get("category", "").strip().lower()
        if not category:
            app_issues.append("Missing category")
        elif category not in valid_categories:
            app_issues.append(f"Invalid category '{category}'")

        platforms = [str(p).strip().lower() for p in app.get("platforms", [])]
        if not platforms:
            app_issues.append("Missing platform")
        else:
            invalid_platforms = [p for p in platforms if p not in valid_platforms]
            if invalid_platforms:
                app_issues.append(f"Invalid platforms: {', '.join(invalid_platforms)}")
            seen_p: set[str] = set()
            dup_p: list[str] = []
            for p in platforms:
                if p in seen_p and p not in dup_p:
                    dup_p.append(p)
                seen_p.add(p)
            if dup_p:
                app_issues.append(f"Duplicate platforms: {', '.join(dup_p)}")

        tags = [str(t).strip().lower() for t in app.get("tags", [])]
        if tags:
            invalid_tags = [t for t in tags if t not in valid_tags]
            if invalid_tags:
                app_issues.append(f"Invalid tags: {', '.join(invalid_tags)}")
            seen_t: set[str] = set()
            dup_t: list[str] = []
            for t in tags:
                if t in seen_t and t not in dup_t:
                    dup_t.append(t)
                seen_t.add(t)
            if dup_t:
                app_issues.append(f"Duplicate tags: {', '.join(dup_t)}")

        flags = [str(f).strip().lower() for f in app.get("flags", [])]
        if flags:
            invalid_flags = [f for f in flags if f not in valid_flags]
            if invalid_flags:
                app_issues.append(f"Invalid flags: {', '.join(invalid_flags)}")
            seen_f: set[str] = set()
            dup_f: list[str] = []
            for f in flags:
                if f in seen_f and f not in dup_f:
                    dup_f.append(f)
                seen_f.add(f)
            if dup_f:
                app_issues.append(f"Duplicate flags: {', '.join(dup_f)}")

        if app_issues:
            issues.append(
                {"name": name or "Unnamed Project", "issues": app_issues}
            )

    return issues, seen_github, seen_names


def validate_backlog(backlog_path: Path) -> list[dict]:
    """Validate backlog.json for missing fields and duplicates."""
    issues: list[dict] = []
    seen_github: set[str] = set()
    seen_names: set[str] = set()

    if not backlog_path.exists():
        return [{"name": backlog_path.name, "issues": ["File not found"]}]

    with open(backlog_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    applications = data.get("applications", [])

    for app in applications:
        app_issues: list[str] = []
        name = app.get("name", "").strip()

        if not name:
            app_issues.append("Missing application name")
        elif name.lower() in seen_names:
            app_issues.append("Duplicate application name")
        else:
            seen_names.add(name.lower())

        github_url = app.get("repo_url", "").strip()
        if not github_url:
            app_issues.append("Missing GitHub URL")
        elif github_url.lower() in seen_github:
            app_issues.append("Duplicate GitHub URL")
        else:
            seen_github.add(github_url.lower())

        if app_issues:
            issues.append(
                {"name": name or "Unnamed Project", "issues": app_issues}
            )

    return issues


def validate_archive(
    archive_path: Path,
    valid_reasons: set[str],
    active_app_urls: set[str],
) -> list[dict]:
    """Validate archive.json for missing fields, invalid reasons, and duplicates."""
    issues: list[dict] = []
    seen_github: set[str] = set()
    seen_names: set[str] = set()

    if not archive_path.exists():
        return [{"name": archive_path.name, "issues": ["File not found"]}]

    with open(archive_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    applications = data.get("applications", [])

    for app in applications:
        app_issues: list[str] = []
        name = app.get("name", "").strip()

        if not name:
            app_issues.append("Missing application name")
        elif name.lower() in seen_names:
            app_issues.append("Duplicate application name")
        else:
            seen_names.add(name.lower())

        github_url = app.get("repo_url", "").strip()
        if not github_url:
            app_issues.append("Missing GitHub URL")
        elif github_url.lower() in seen_github:
            app_issues.append("Duplicate GitHub URL")
        else:
            seen_github.add(github_url.lower())

        reason = app.get("reason", "").strip().lower()
        if not reason:
            app_issues.append("Missing archive reason")
        elif reason not in valid_reasons:
            app_issues.append(f"Invalid archive reason '{reason}'")

        if github_url and github_url.lower() in active_app_urls:
            app_issues.append("Archived project still present in applications.json")

        if app_issues:
            issues.append(
                {"name": name or "Unnamed Project", "issues": app_issues}
            )

    return issues


def generate_report(
    output_path: Path,
    report_data: dict[str, list[dict]],
) -> int:
    """Write the markdown report and return the total number of issues found."""
    total_issues = sum(
        len(entry["issues"])
        for entries in report_data.values()
        for entry in entries
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Format Maintenance Report\n\n")
        if total_issues == 0:
            f.write("No issues found. All data files are properly formatted.\n")
        else:
            for file_name, entries in report_data.items():
                if not entries:
                    continue
                f.write(f"## {file_name}\n\n")
                for entry in entries:
                    f.write(f"### {entry['name']}\n")
                    for issue in entry["issues"]:
                        f.write(f"- {issue}\n")
                    f.write("\n")

    return total_issues


def run_format_checks(
    static_data_dir: Path | str | None = None,
    dynamic_data_dir: Path | str | None = None,
    report_output_file: Path | str | None = None,
) -> tuple[dict[str, list[dict]], int, Path]:
    """Execute all formatting and consistency checks across data files."""
    if static_data_dir is None:
        static_dir = Path("data/static")
        if not static_dir.exists():
            static_dir = STATIC_DATA_DIR
    else:
        static_dir = Path(static_data_dir)

    if dynamic_data_dir is None:
        dynamic_dir = Path("data/dynamic")
        if not dynamic_dir.exists():
            dynamic_dir = DYNAMIC_DATA_DIR
    else:
        dynamic_dir = Path(dynamic_data_dir)

    if report_output_file is None:
        report_path = Path("../resources/maintenance/format_maintenance.md")
        if not report_path.parent.exists():
            report_path = MAINTENANCE_DIR / "format_maintenance.md"
    else:
        report_path = Path(report_output_file)

    cat_issues, valid_subcats, _ = validate_categories(
        static_dir / "categories.json"
    )
    plat_issues, valid_plats = validate_platforms(static_dir / "platforms.json")
    tag_issues, valid_tags = validate_tags(static_dir / "tags.json")

    app_issues, seen_app_urls, _ = validate_applications(
        applications_path=static_dir / "applications.json",
        valid_categories=valid_subcats,
        valid_platforms=valid_plats,
        valid_tags=valid_tags,
        valid_flags=VALID_FLAGS,
    )

    backlog_issues = validate_backlog(static_dir / "backlog.json")
    archive_issues = validate_archive(
        archive_path=dynamic_dir / "archive.json",
        valid_reasons=VALID_ARCHIVE_REASONS,
        active_app_urls=seen_app_urls,
    )

    report_data = {
        "applications.json": app_issues,
        "categories.json": cat_issues,
        "platforms.json": plat_issues,
        "tags.json": tag_issues,
        "backlog.json": backlog_issues,
        "archive.json": archive_issues,
    }

    total_issues = generate_report(report_path, report_data)
    return report_data, total_issues, report_path


def main() -> None:
    _, total_issues, _ = run_format_checks()
    print("Maintenance report generated: format_maintenance.md")
    if total_issues > 0:
        print(f"Validation failed: {total_issues} issue(s) found.")
        sys.exit(1)
    print("Validation passed: No issues found.")
    sys.exit(0)


if __name__ == "__main__":
    main()

