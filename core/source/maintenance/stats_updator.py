import json
from pathlib import Path

try:
    from source.utils.github_utils import (
        extract_repo_path,
        fetch_repo_data,
        format_commit_date,
        get_github_headers,
        get_github_token,
    )
except ImportError:
    from source.utils.github_utils import (
        extract_repo_path,
        fetch_repo_data,
        format_commit_date,
        get_github_headers,
        get_github_token,
    )

CORE_DIR = Path(__file__).resolve().parent.parent.parent


def update_application_data(app: dict, headers: dict) -> dict:
    repo_url = app.get("repo_url", "")
    repo_name = extract_repo_path(repo_url)
    if not repo_name:
        print(f"Skipping {app.get('name', 'Unknown')}: Invalid GitHub URL ({repo_url})")
        return app

    print(f"Updating: {repo_name}")
    repo_data = fetch_repo_data(repo_name, headers=headers)

    if repo_data is not None:
        app["stars"] = repo_data.get("stargazers_count", app.get("stars", 0))
        app["language"] = repo_data.get("language", app.get("language", ""))

        # Flags
        if "custom-homepage" not in app.get("flags", []):
            app["homepage_url"] = repo_data.get("homepage", app.get("homepage_url", ""))

        if "custom-description" not in app.get("flags", []):
            app["description"] = repo_data.get(
                "description", app.get("description", "")
            )

        if "custom-license" not in app.get("flags", []):
            license_data = repo_data.get("license")
            if license_data is not None:
                app["license"] = license_data.get("spdx_id", app.get("license", ""))
            else:
                app["license"] = app.get("license", "")

        # Check
        pushed_at = repo_data.get("pushed_at")
        if pushed_at:
            app["last_commit"] = format_commit_date(pushed_at)
        else:
            app["last_commit"] = app.get("last_commit", "")

        return app
    else:
        return app


def update_all_applications(
    input_file: Path | str | None = None,
    output_file: Path | str | None = None,
) -> dict:
    if input_file is None:
        input_path = Path("data/static/applications.json")
        if not input_path.exists():
            input_path = CORE_DIR / "data" / "static" / "applications.json"
    else:
        input_path = Path(input_file)

    if output_file is None:
        if Path("data/dynamic").exists():
            output_path = Path("data/dynamic/applications_generated.json")
        else:
            output_path = CORE_DIR / "data" / "dynamic" / "applications_generated.json"
    else:
        output_path = Path(output_file)

    token = get_github_token()
    if not token:
        print(
            "Warning: GITHUB_TOKEN environment variable is not set. Requests may be rate-limited."
        )
    headers = get_github_headers(token)

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    generated_apps = []
    for app in data.get("applications", []):
        updated_app = update_application_data(app.copy(), headers)
        generated_apps.append(updated_app)

    generated_data = {"applications": generated_apps}

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(generated_data, f, indent=4)
        f.write("\n")

    print(f"Updated application data successfully. Output written to {output_path}.")
    return generated_data


if __name__ == "__main__":
    update_all_applications()
