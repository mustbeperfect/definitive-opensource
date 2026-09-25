from datetime import datetime
import json
from pathlib import Path

CORE_DIR = Path(__file__).resolve().parent.parent.parent
REPO_ROOT = CORE_DIR.parent


def format_stars(stars: int | None) -> str:
    if stars is None:
        return "0"
    return f"{stars:,}"


def format_time_ago(commit_date_str: str) -> str:
    if not commit_date_str:
        return "N/A"
    try:
        commit_date = datetime.strptime(commit_date_str, "%m/%d/%Y").date()
    except Exception:
        return "Unknown"

    today = datetime.now().date()
    days = (today - commit_date).days

    if days < 0:
        return "Today"
    if days == 0:
        return "Today"
    if days == 1:
        return "Yesterday"
    if days < 7:
        return f"{days} days ago"
    if days < 30:
        weeks = days // 7
        return f"{weeks} week{'s' if weeks > 1 else ''} ago"
    if days < 365:
        months = days // 30
        return f"{months} month{'s' if months > 1 else ''} ago"

    years = days // 365
    remaining_months = (days % 365) // 30
    if remaining_months > 0:
        return (
            f"{years} yr{'s' if years > 1 else ''}, "
            f"{remaining_months} mo{'s' if remaining_months > 1 else ''} ago"
        )
    return f"{years} year{'s' if years > 1 else ''} ago"


def resolve_paths(
    input_file: Path | str | None = None,
    output_file: Path | str | None = None,
) -> tuple[Path, Path]:
    if input_file is None:
        if Path("data/dynamic/backlog_generated.json").exists():
            input_path = Path("data/dynamic/backlog_generated.json")
        elif Path("core/data/dynamic/backlog_generated.json").exists():
            input_path = Path("core/data/dynamic/backlog_generated.json")
        else:
            input_path = CORE_DIR / "data" / "dynamic" / "backlog_generated.json"
    else:
        input_path = Path(input_file)

    if output_file is None:
        if Path("resources/maintenance").exists():
            output_path = Path("resources/maintenance/backlog.md")
        elif Path("../resources/maintenance").exists():
            output_path = Path("../resources/maintenance/backlog.md")
        else:
            output_path = REPO_ROOT / "resources" / "maintenance" / "backlog.md"
    else:
        output_path = Path(output_file)

    return input_path, output_path


def generate_backlog_markdown(
    input_file: Path | str | None = None,
    output_file: Path | str | None = None,
) -> str:
    input_path, output_path = resolve_paths(input_file, output_file)

    print(f"Reading generated backlog from: {input_path}")
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    applications = data.get("applications", [])

    lines = [
        "# Backlog",
        "",
        "| Project | Stars | Last Commit | Time Since Last Commit | Note |",
        "| --- | --- | --- | --- | --- |",
    ]

    for app in applications:
        name = (app.get("name") or "Unknown Project").replace("|", "-").strip()
        repo_url = (app.get("repo_url") or "").strip()
        note = (app.get("note") or "").replace("|", "-").strip()
        last_commit = (app.get("last_commit") or "").strip()
        stars = app.get("stars", 0)

        project_link = f"[{name}]({repo_url})" if repo_url else name
        stars_formatted = format_stars(stars)
        last_commit_display = last_commit if last_commit else "N/A"
        time_ago_display = format_time_ago(last_commit)

        lines.append(
            f"| {project_link} | {stars_formatted} | {last_commit_display} | {time_ago_display} | {note} |"
        )

    lines.append("")
    content = "\n".join(lines)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(
        f"Successfully generated {output_path} with {len(applications)} applications."
    )
    return content


if __name__ == "__main__":
    generate_backlog_markdown()
