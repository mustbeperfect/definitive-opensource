import json
from pathlib import Path
import sys

CORE_DIR = Path(__file__).resolve().parents[2]
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))

from source.utils.path_utils import DYNAMIC_DATA_DIR  # noqa: E402

REASON_LABELS = {
    "closed-source": "Closed Source",
    "closed source": "Closed Source",
    "abandoned": "Abandoned",
    "archived": "Archived",
    "deleted": "Deleted",
}


def format_reason(reason):
    if not reason:
        return "Unknown"

    normalized = reason.strip().lower()
    if normalized in REASON_LABELS:
        return REASON_LABELS[normalized]

    return reason.strip().title()


def generate_archive_section():
    with open(DYNAMIC_DATA_DIR / "archive.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    applications = data.get("applications", [])

    lines = [
        "## Removed Projects",
        "Projects that were once on this list but removed, usually due to abandonment or going closed source.",
        "",
        "<details>",
        "  <summary><b>Archive</b></summary> <br />",
        "",
    ]

    for app in applications:
        name = app.get("name", "Unknown Project")
        repo_url = app.get("repo_url", "").strip()
        reason = format_reason(app.get("reason", "Unknown"))

        if repo_url:
            lines.append(f"  - [{name}]({repo_url}) - `{reason}`")
        else:
            lines.append(f"  - {name} - `{reason}`")

    lines.extend(["</details>", ""])
    return "\n".join(lines)


if __name__ == "__main__":
    print(generate_archive_section())
