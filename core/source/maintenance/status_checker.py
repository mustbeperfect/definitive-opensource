import json
import os
from datetime import datetime, timedelta

import requests

INPUT_FILE = "data/dynamic/applications.json"
OUTPUT_FILE = "../resources/maintenance/status_maintenance.md"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {"Accept": "application/vnd.github+json"}
if GITHUB_TOKEN:
    headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

with open(INPUT_FILE, "r") as f:
    data = json.load(f)

potentially_abandoned = []
archived = []
no_longer_exists = []
rebranded = []

# Check if projects are abandoned, archived, or no longer exist
for app in data.get("applications", []):
    repo_url = app.get("repo_url")
    if not repo_url or "github.com" not in repo_url:
        continue

    try:
        parts = repo_url.rstrip("/").split("/")
        owner, repo = parts[-2], parts[-1]
    except Exception:
        continue

    api_url = f"https://api.github.com/repos/{owner}/{repo}"

    try:
        r = requests.get(api_url, headers=headers)
        if r.status_code == 404:
            no_longer_exists.append(app["name"])
            continue
        elif r.status_code != 200:
            print(f"Warning: failed to fetch {repo_url} ({r.status_code})")
            continue

        repo_data = r.json()

        current_full_name = repo_data.get("full_name", "")
        expected_full_name = f"{owner}/{repo}"

        if current_full_name.lower() != expected_full_name.lower():
            new_url = repo_data.get("html_url", "Unknown URL")
            rebranded.append(f"{app['name']} (Moved to: {new_url})")

        if repo_data.get("archived"):
            archived.append(app["name"])
            continue

        pushed_at = repo_data.get("pushed_at")
        if pushed_at:
            last_commit_date = datetime.strptime(pushed_at, "%Y-%m-%dT%H:%M:%SZ")
            if last_commit_date < datetime.utcnow() - timedelta(days=365):
                potentially_abandoned.append(app["name"])

    except Exception as e:
        print(f"Error processing {repo_url}: {e}")

with open(OUTPUT_FILE, "w") as f:
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

print(f"{OUTPUT_FILE} Complete")
