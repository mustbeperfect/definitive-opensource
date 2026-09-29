from __future__ import annotations

import json
import os
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
    flags = app.get("flags", [])

    if not repo_name:
        print(f"Skipping {app.get('name', 'Unknown')}: Invalid GitHub URL ({repo_url})")
        if fallback_app:
            if "stars" in fallback_app and fallback_app["stars"] is not None:
                app["stars"] = fallback_app["stars"]
            elif "stars" not in app or app["stars"] is None:
                app["stars"] = 0
            if "language" in fallback_app and fallback_app["language"] is not None:
                app["language"] = fallback_app["language"]
            elif "language" not in app or app["language"] is None:
                app["language"] = ""
            if (
                "homepage_url" in fallback_app
                and fallback_app["homepage_url"] is not None
            ):
                app["homepage_url"] = fallback_app["homepage_url"]
            elif "homepage_url" not in app or app["homepage_url"] is None:
                app["homepage_url"] = ""
            if (
                "last_commit" in fallback_app
                and fallback_app["last_commit"] is not None
            ):
                app["last_commit"] = fallback_app["last_commit"]
            elif "last_commit" not in app or app["last_commit"] is None:
                app["last_commit"] = ""
        else:
            if "stars" not in app or app["stars"] is None:
                app["stars"] = 0
            if "language" not in app or app["language"] is None:
                app["language"] = ""
            if "homepage_url" not in app or app["homepage_url"] is None:
                app["homepage_url"] = ""
            if "last_commit" not in app or app["last_commit"] is None:
                app["last_commit"] = ""
        if "description" not in app or app["description"] is None:
            app["description"] = ""
        if "license" not in app or app["license"] is None:
            app["license"] = ""
        return app

    if repo_data is None and headers is not None:
        print(f"Updating: {repo_name}")
        repo_data = fetch_repo_data(repo_name, headers=headers)

    if repo_data is not None:
        app["stars"] = repo_data.get("stargazers_count", app.get("stars", 0))
        app["language"] = repo_data.get("language") or app.get("language", "") or ""

        # Flags
        if "custom-homepage" not in flags:
            app["homepage_url"] = (
                repo_data.get("homepage") or app.get("homepage_url", "") or ""
            )
        elif "homepage_url" not in app or app["homepage_url"] is None:
            app["homepage_url"] = ""

        if "custom-description" not in flags:
            app["description"] = (
                repo_data.get("description", app.get("description", "")) or ""
            )
        elif "description" not in app or app["description"] is None:
            app["description"] = ""

        if "custom-license" not in flags:
            license_data = repo_data.get("license")
            if isinstance(license_data, dict):
                app["license"] = (
                    license_data.get("spdx_id") or app.get("license", "") or ""
                )
            elif isinstance(license_data, str):
                app["license"] = license_data
            else:
                app["license"] = app.get("license", "") or ""
        elif "license" not in app or app["license"] is None:
            app["license"] = ""

        # Check
        pushed_at = repo_data.get("pushed_at")
        if pushed_at:
            app["last_commit"] = format_commit_date(pushed_at)
        else:
            app["last_commit"] = app.get("last_commit", "") or ""

        # Ensure all dynamic keys exist and are not None
        if "stars" not in app or app["stars"] is None:
            app["stars"] = 0
        if "language" not in app or app["language"] is None:
            app["language"] = ""
        if "homepage_url" not in app or app["homepage_url"] is None:
            app["homepage_url"] = ""
        if "last_commit" not in app or app["last_commit"] is None:
            app["last_commit"] = ""
        if "description" not in app or app["description"] is None:
            app["description"] = ""
        if "license" not in app or app["license"] is None:
            app["license"] = ""

        return app
    else:
        # If fetch failed but fallback_app exists, preserve previous dynamic values without wiping
        if fallback_app:
            # 1. stars
            if "stars" in fallback_app and fallback_app["stars"] is not None:
                app["stars"] = fallback_app["stars"]
            elif "stars" not in app or app["stars"] is None:
                app["stars"] = 0

            # 2. language
            if "language" in fallback_app and fallback_app["language"] is not None:
                app["language"] = fallback_app["language"]
            elif "language" not in app or app["language"] is None:
                app["language"] = ""

            # 3. homepage_url
            if "custom-homepage" not in flags:
                if (
                    "homepage_url" in fallback_app
                    and fallback_app["homepage_url"] is not None
                ):
                    app["homepage_url"] = fallback_app["homepage_url"]
                elif "homepage_url" not in app or app["homepage_url"] is None:
                    app["homepage_url"] = ""
            elif "homepage_url" not in app or app["homepage_url"] is None:
                app["homepage_url"] = ""

            # 4. description
            if "custom-description" not in flags:
                if (
                    "description" in fallback_app
                    and fallback_app["description"] is not None
                ):
                    app["description"] = fallback_app["description"]
                elif "description" not in app or app["description"] is None:
                    app["description"] = ""
            elif "description" not in app or app["description"] is None:
                app["description"] = ""

            # 5. license
            if "custom-license" not in flags:
                if "license" in fallback_app and fallback_app["license"] is not None:
                    app["license"] = fallback_app["license"]
                elif "license" not in app or app["license"] is None:
                    app["license"] = ""
            elif "license" not in app or app["license"] is None:
                app["license"] = ""

            # 6. last_commit
            if (
                "last_commit" in fallback_app
                and fallback_app["last_commit"] is not None
            ):
                app["last_commit"] = fallback_app["last_commit"]
            elif "last_commit" not in app or app["last_commit"] is None:
                app["last_commit"] = ""
        else:
            # No fallback available, ensure valid schema defaults so entries are not stripped
            if "stars" not in app or app["stars"] is None:
                app["stars"] = 0
            if "language" not in app or app["language"] is None:
                app["language"] = ""
            if "homepage_url" not in app or app["homepage_url"] is None:
                app["homepage_url"] = ""
            if "description" not in app or app["description"] is None:
                app["description"] = ""
            if "license" not in app or app["license"] is None:
                app["license"] = ""
            if "last_commit" not in app or app["last_commit"] is None:
                app["last_commit"] = ""

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
                    raw_url = existing_app.get("repo_url", "")
                    if raw_url:
                        existing_lookup[raw_url.strip()] = existing_app
                        existing_lookup[raw_url.strip().lower()] = existing_app
                        path = extract_repo_path(raw_url)
                        if path:
                            existing_lookup[path.lower()] = existing_app
                    name = existing_app.get("name", "")
                    if name:
                        existing_lookup[name.strip().lower()] = existing_app
        except Exception as e:
            print(f"Notice: Could not load existing generated data for fallback: {e}")

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    applications = data.get("applications", [])
    if not applications and output_path.exists():
        print(
            f"Warning: No applications found in {input_path}. Preserving existing {output_path} to prevent data loss."
        )
        return {"applications": []}

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
        raw_url = app.get("repo_url", "")
        repo_path = extract_repo_path(raw_url)
        repo_data = batch_results.get(repo_path) if repo_path else None

        # Look up fallback cache by normalized repo path, exact URL, or normalized name
        fallback_app = None
        if repo_path:
            fallback_app = existing_lookup.get(repo_path.lower())
        if not fallback_app and raw_url:
            fallback_app = existing_lookup.get(raw_url.strip()) or existing_lookup.get(
                raw_url.strip().lower()
            )
        if not fallback_app and app.get("name"):
            fallback_app = existing_lookup.get(app["name"].strip().lower())

        # Do not pass headers=headers here because batch fetch was already performed;
        # this avoids blocking on hundreds of synchronous individual requests if batch failed.
        updated_app = update_application_data(
            app.copy(),
            headers=None,
            repo_data=repo_data,
            fallback_app=fallback_app,
        )
        generated_apps.append(updated_app)

    generated_data = {"applications": generated_apps}

    # Atomic write to prevent file corruption or destructive 0-byte truncation on crash
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = output_path.with_name(f"{output_path.name}.tmp.{os.getpid()}")
    try:
        with open(temp_path, "w", encoding="utf-8") as f:
            json.dump(generated_data, f, indent=4)
            f.write("\n")
        temp_path.replace(output_path)
    except Exception:
        if temp_path.exists():
            temp_path.unlink()
        raise

    print(f"Updated application data successfully. Output written to {output_path}.")
    return generated_data


if __name__ == "__main__":
    update_all_applications()
