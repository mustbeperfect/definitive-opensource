import os
import json
import requests
from urllib.parse import urlparse

JSON_FILE = "applications.json"

# Get GitHub token from environment variable.
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise EnvironmentError("Please set your GITHUB_TOKEN environment variable.")

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

def format_stars(stars):

    # Star count format
    if stars < 1000:
        return str(stars)
    else:
        # Check if the number is evenly divisible by 1000.
        if stars % 1000 == 0:
            return f"{stars // 1000}k"
        else:
            # Format to one decimal place.
            return f"{stars / 1000:.1f}k"

def extract_owner_repo(url):

    # Extract URL
    parsed = urlparse(url)
    path_parts = parsed.path.strip("/").split("/")
    if len(path_parts) >= 2:
        return path_parts[0], path_parts[1]
    else:
        raise ValueError(f"URL {url} is not a valid GitHub repository URL.")

def update_star_count(application):
    repo_url = application.get("link", "")
    try:
        owner, repo = extract_owner_repo(repo_url)
    except ValueError as e:
        print(e)
        return

    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(api_url, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        stars = data.get("stargazers_count", 0)
        application["stars"] = format_stars(stars)
        print(f"Updated {owner}/{repo} with {application['stars']} stars.")
    else:
        print(f"Failed to fetch data for {owner}/{repo}: {response.status_code} {response.text}")

def main():
    # Load the JSON file
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    applications = data.get("applications", [])
    for app in applications:
        update_star_count(app)

    # Save updated JSON back to file
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("Updated JSON file.")

if __name__ == "__main__":
    main()
