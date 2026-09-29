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
    fetch_repo_summary,
    fetch_repos_batch,
    format_commit_date,
    get_github_headers,
    get_github_token,
)


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

    # Load fallback cache from existing generated backlog to avoid data loss on failures
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
            print(f"Notice: Could not load existing backlog data for fallback: {e}")

    applications = data.get("applications", [])
    if not applications and output_path.exists():
        print(
            f"Warning: No applications found in {input_path}. Preserving existing {output_path} to prevent data loss."
        )
        return {"applications": []}

    total = len(applications)

    repo_paths = [
        extract_repo_path(app.get("repo_url", ""))
        for app in applications
        if extract_repo_path(app.get("repo_url", ""))
    ]
    batch_results = fetch_repos_batch(repo_paths, token=token, headers=headers)

    generated_apps = []

    for idx, app in enumerate(applications, 1):
        name = app.get("name", "")
        repo_url = app.get("repo_url", "")
        note = app.get("note", "")

        last_commit = ""
        stars = 0

        repo_path = extract_repo_path(repo_url)

        # Look up fallback from cache
        fallback_app = None
        if repo_path:
            fallback_app = existing_lookup.get(repo_path.lower())
        if not fallback_app and repo_url:
            fallback_app = existing_lookup.get(repo_url.strip()) or existing_lookup.get(
                repo_url.strip().lower()
            )
        if not fallback_app and name:
            fallback_app = existing_lookup.get(name.strip().lower())

        if repo_path and repo_path in batch_results and batch_results[repo_path]:
            repo_data = batch_results[repo_path]
            stars = repo_data.get("stargazers_count", 0)
            last_commit = format_commit_date(repo_data.get("pushed_at"))
        elif repo_path:
            # Batch didn't return data; if fallback cache exists, use it to avoid data loss
            if fallback_app and fallback_app.get("last_commit"):
                last_commit = fallback_app.get("last_commit", "")
                stars = fallback_app.get("stars", 0)
            else:
                last_commit, stars = fetch_repo_summary(repo_path, headers)
        else:
            if fallback_app:
                last_commit = fallback_app.get("last_commit", "")
                stars = fallback_app.get("stars", 0)
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

    print(
        f"Successfully generated {output_path} with {len(generated_apps)} applications."
    )
    return generated_data


if __name__ == "__main__":
    generate_backlog()
