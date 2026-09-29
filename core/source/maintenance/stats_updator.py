from __future__ import annotations

import json
from pathlib import Path
import sys

CORE_DIR = Path(__file__).resolve().parents[2]
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))

from source.utils.github_utils import (  # noqa: E402
    extract_repo_path,
    fetch_repo_data,
    fetch_repos_batch,
    format_commit_date,
    get_github_headers,
    get_github_token,
)


def update_application_data(
    app: dict,
    headers: dict | None = None,
    repo_data: dict | None = None,
    fallback_app: dict | None = None,
) -> dict:
    repo_url = app.get("repo_url", "")
    repo_name = extract_repo_path(repo_url)
    if not repo_name:
        print(f"Skipping {app.get('name', 'Unknown')}: Invalid GitHub URL ({repo_url})")
        return app

    if repo_data is None and headers is not None:
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
        # If fetch failed but fallback_app exists, preserve previous dynamic values
        if fallback_app:
            for field in [
                "stars",
                "language",
                "homepage_url",
                "description",
                "license",
                "last_commit",
            ]:
                if (field not in app or not app.get(field)) and fallback_app.get(field):
                    app[field] = fallback_app[field]
        return app


def update_all_applications(
    input_file: Path | str | None = None,
    output_file: Path | str | None = None,
    batch_size: int = 100,
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

    # Load fallback cache from existing generated file to avoid data loss on failures
    existing_lookup: dict[str, dict] = {}
    if output_path.exists():
        try:
            with open(output_path, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
                for existing_app in existing_data.get("applications", []):
                    if existing_app.get("repo_url"):
                        existing_lookup[existing_app["repo_url"]] = existing_app
                    if existing_app.get("name"):
                        existing_lookup[existing_app["name"]] = existing_app
        except Exception as e:
            print(f"Notice: Could not load existing generated data for fallback: {e}")

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    applications = data.get("applications", [])
    repo_paths: list[str] = []
    for app in applications:
        repo_path = extract_repo_path(app.get("repo_url", ""))
        if repo_path:
            repo_paths.append(repo_path)

    # Batch fetch all repositories via GraphQL (or threaded REST fallback)
    batch_results = fetch_repos_batch(
        repo_paths,
        token=token,
        headers=headers,
        batch_size=batch_size,
    )

    generated_apps = []
    for app in applications:
        repo_path = extract_repo_path(app.get("repo_url", ""))
        repo_data = batch_results.get(repo_path) if repo_path else None
        fallback_app = (
            existing_lookup.get(app.get("repo_url", ""))
            or existing_lookup.get(app.get("name", ""))
        )
        updated_app = update_application_data(
            app.copy(),
            headers=headers,
            repo_data=repo_data,
            fallback_app=fallback_app,
        )
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

