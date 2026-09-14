import json
import os
from datetime import datetime
import requests

with open("data/static/applications.json", "r") as f:
    data = json.load(f)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if GITHUB_TOKEN is None:
    print("Error: GITHUB_TOKEN environment variable is not set.")
    exit(1)

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

def update_application_data(app):
    repo_name = app["repo_url"].split("github.com/")[1]
    repo_url = f"https://api.github.com/repos/{repo_name}"

    print(f"Updating: {repo_name}")
    print(f"API URL: {repo_url}")

    response = requests.get(repo_url, headers=headers)

    if response.status_code == 200:
        repo_data = response.json()

        app["stars"] = repo_data.get("stargazers_count", app.get("stars", 0))
        app["language"] = repo_data.get("language", app.get("language", ""))

        # Flags
        if "custom-homepage" not in app.get("flags", []):
            app["homepage_url"] = repo_data.get("homepage", app.get("homepage_url", ""))

        if "custom-description" not in app.get("flags", []):
            app["description"] = repo_data.get("description", app.get("description", ""))

        if "custom-license" not in app.get("flags", []):
            license_data = repo_data.get("license")
            if license_data is not None:
                app["license"] = license_data.get("spdx_id", app.get("license", ""))
            else:
                app["license"] = app.get("license", "")

        # Check
        if "pushed_at" in repo_data and repo_data["pushed_at"]:
            app["last_commit"] = datetime.strptime(
                repo_data["pushed_at"], "%Y-%m-%dT%H:%M:%SZ"
            ).strftime("%m/%d/%Y")
        else:
            app["last_commit"] = app.get("last_commit", "")

        return app
    else:
        print(
            f"Error: Unable to fetch data for {repo_name}. Status Code: {response.status_code}"
        )
        print(f"Response: {response.text}")
        return app

generated_apps = []
for app in data["applications"]:
    updated_app = update_application_data(app.copy())
    generated_apps.append(updated_app)

generated_data = {"applications": generated_apps}

with open("data/dynamic/applications_generated.json", "w") as f:
    json.dump(generated_data, f, indent=4)

print("Updated application data successfully! Output written to applications_generated.json.")
