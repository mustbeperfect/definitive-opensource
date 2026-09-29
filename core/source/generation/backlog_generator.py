import json
from pathlib import Path
import sys

CORE_DIR = Path(__file__).resolve().parents[2]
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))

from source.utils.github_utils import format_time_ago  # noqa: E402
from source.utils.markdown_utils import format_stars, sanitize_table_cell  # noqa: E402
from source.utils.path_utils import DYNAMIC_DATA_DIR, MAINTENANCE_DIR  # noqa: E402


def resolve_paths(
    input_file: Path | str | None = None,
    output_file: Path | str | None = None,
) -> tuple[Path, Path]:
    if input_file is None:
        input_path = DYNAMIC_DATA_DIR / "backlog_generated.json"
    else:
        input_path = Path(input_file)

    if output_file is None:
        output_path = MAINTENANCE_DIR / "backlog.md"
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
        name = sanitize_table_cell(app.get("name") or "Unknown Project")
        repo_url = (app.get("repo_url") or "").strip()
        note = sanitize_table_cell(app.get("note"))
        last_commit = (app.get("last_commit") or "").strip()
        stars = app.get("stars", 0)

        project_link = f"[{name}]({repo_url})" if repo_url else name
        stars_formatted = format_stars(stars, compact=False)
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
