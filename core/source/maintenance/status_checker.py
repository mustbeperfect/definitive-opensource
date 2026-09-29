from __future__ import annotations

from datetime import datetime, timedelta
import json
from pathlib import Path
import sys

CORE_DIR = Path(__file__).resolve().parents[2]
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))

from source.utils.github_utils import extract_repo_path  # noqa: E402
from source.utils.path_utils import DYNAMIC_DATA_DIR, MAINTENANCE_DIR  # noqa: E402


def check_status(
    input_file: Path | str | None = None,
    output_file: Path | str | None = None,
) -> dict[str, list[str]]:
    """Inspect application metadata offline from applications_generated.json

    and generate the status maintenance markdown report.

    Checks for:
      - Potentially Abandoned (> 365 days since last commit)
      - Archived (repository archived on GitHub)
      - No Longer Exists (404 / repository unresolvable)
      - Rebranded / Moved (github_full_name differs from static repo_url path)
    """
    if input_file is None:
        input_path = Path("data/dynamic/applications_generated.json")
        if not input_path.exists():
            input_path = DYNAMIC_DATA_DIR / "applications_generated.json"
    else:
        input_path = Path(input_file)

    if output_file is None:
        output_path = Path("../resources/maintenance/status_maintenance.md")
        if not output_path.parent.exists():
            output_path = MAINTENANCE_DIR / "status_maintenance.md"
    else:
        output_path = Path(output_file)

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    potentially_abandoned: list[str] = []
    archived: list[str] = []
    no_longer_exists: list[str] = []
    rebranded: list[str] = []

    cutoff_date = datetime.now() - timedelta(days=365)

    for app in data.get("applications", []):
        app_name = app.get("name", "Unknown")
        repo_url = app.get("repo_url", "")
        if not repo_url or "github.com" not in repo_url:
            continue

        repo_path = extract_repo_path(repo_url)
        if not repo_path:
            continue

        # 1. Check if repository no longer exists (404 / unresolvable on GitHub)
        current_full_name = app.get("github_full_name", "")
        if app.get("not_found") or (
            "github_full_name" in app
            and not current_full_name
            and not app.get("last_commit")
            and app.get("stars", 0) == 0
        ):
            no_longer_exists.append(app_name)
            continue

        # 2. Check if repository was rebranded or moved
        if current_full_name and current_full_name.lower() != repo_path.lower():
            rebranded.append(
                f"{app_name} (Moved to: https://github.com/{current_full_name})"
            )

        # 3. Check if repository is archived
        if app.get("archived", False):
            archived.append(app_name)
            continue

        # 4. Check if repository is potentially abandoned (> 365 days since last commit)
        last_commit = app.get("last_commit", "")
        if last_commit:
            commit_date = None
            try:
                commit_date = datetime.strptime(last_commit, "%m/%d/%Y")
            except ValueError:
                try:
                    commit_date = datetime.fromisoformat(
                        last_commit.replace("Z", "+00:00")
                    )
                    if commit_date.tzinfo:
                        commit_date = commit_date.replace(tzinfo=None)
                except Exception:
                    commit_date = None

            if commit_date and commit_date < cutoff_date:
                potentially_abandoned.append(app_name)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Repository Activity Maintenance Report\n\n")

        f.write("## Potentially Abandoned:\n")
        if potentially_abandoned:
            for name in potentially_abandoned:
                f.write(f"- {name}\n")
        else:
            f.write("_None_\n")

        f.write("\n## Archived:\n")
        if archived:
            for name in archived:
                f.write(f"- {name}\n")
        else:
            f.write("_None_\n")

        f.write("\n## No Longer Exists (404):\n")
        if no_longer_exists:
            for name in no_longer_exists:
                f.write(f"- {name}\n")
        else:
            f.write("_None_\n")

        f.write("\n## Rebranded / Moved:\n")
        if rebranded:
            for item in rebranded:
                f.write(f"- {item}\n")
        else:
            f.write("_None_\n")

    print(f"{output_path} Complete")
    return {
        "potentially_abandoned": potentially_abandoned,
        "archived": archived,
        "no_longer_exists": no_longer_exists,
        "rebranded": rebranded,
    }


if __name__ == "__main__":
    check_status()
