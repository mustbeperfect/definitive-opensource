import json
from pathlib import Path

try:
    from source.utils.github_utils import (
        extract_repo_path,
        fetch_repo_summary,
        get_github_headers,
        get_github_token,
    )
except ImportError:
    from source.utils.github_utils import (
        extract_repo_path,
        fetch_repo_summary,
        get_github_headers,
        get_github_token,
    )

CORE_DIR = Path(__file__).resolve().parent.parent.parent


def generate_backlog(
    input_file: Path | str | None = None,
    output_file: Path | str | None = None,
) -> dict:
    if input_file is None:
        input_path = Path("data/static/backlog.json")
        if not input_path.exists():
            input_path = CORE_DIR / "data" / "static" / "backlog.json"
    else:
        input_path = Path(input_file)

    if output_file is None:
        if Path("data/dynamic").exists():
            output_path = Path("data/dynamic/backlog_generated.json")
        else:
            output_path = CORE_DIR / "data" / "dynamic" / "backlog_generated.json"
    else:
        output_path = Path(output_file)

    print(f"Reading backlog from: {input_path}")
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    token = get_github_token()
    if not token:
        print("Warning: GITHUB_TOKEN not found. Requests may be rate-limited.")
    headers = get_github_headers(token)

    applications = data.get("applications", [])
    total = len(applications)
    generated_apps = []

    for idx, app in enumerate(applications, 1):
        name = app.get("name", "")
        repo_url = app.get("repo_url", "")
        note = app.get("note", "")

        last_commit = ""
        stars = 0

        repo_path = extract_repo_path(repo_url)
        if repo_path:
            print(f"[{idx}/{total}] Fetching {name} ({repo_path})...")
            last_commit, stars = fetch_repo_summary(repo_path, headers)
        else:
            print(
                f"[{idx}/{total}] Skipping {name}: Invalid or non-GitHub URL ({repo_url})"
            )

        generated_apps.append(
            {
                "name": name,
                "repo_url": repo_url,
                "note": note,
                "last_commit": last_commit,
                "stars": stars,
            }
        )

    generated_data = {"applications": generated_apps}

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(generated_data, f, indent=4)
        f.write("\n")

    print(
        f"Successfully generated {output_path} with {len(generated_apps)} applications."
    )
    return generated_data


if __name__ == "__main__":
    generate_backlog()
