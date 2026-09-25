from datetime import datetime
import os
import subprocess
import requests


def get_github_token() -> str | None:
    token = os.getenv("GITHUB_TOKEN")
    if token:
        return token
    try:
        res = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True,
            text=True,
            check=True,
        )
        gh_token = res.stdout.strip()
        if gh_token:
            return gh_token
    except Exception:
        pass
    return None


def get_github_headers(token: str | None = None) -> dict[str, str]:
    if token is None:
        token = get_github_token()
    headers = {
        "Accept": "application/vnd.github.v3+json",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def extract_repo_path(repo_url: str) -> str | None:
    if not repo_url:
        return None
    clean_url = repo_url.strip().rstrip("/")
    if clean_url.endswith(".git"):
        clean_url = clean_url[:-4]
    if "github.com/" in clean_url:
        path = clean_url.split("github.com/")[1]
        parts = [p for p in path.split("/") if p]
        if len(parts) >= 2:
            return f"{parts[0]}/{parts[1]}"
    return None


def format_commit_date(pushed_at: str | None) -> str:
    if not pushed_at:
        return ""
    try:
        return datetime.strptime(pushed_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%m/%d/%Y")
    except ValueError:
        try:
            return datetime.fromisoformat(pushed_at.replace("Z", "+00:00")).strftime(
                "%m/%d/%Y"
            )
        except Exception:
            return str(pushed_at)


def fetch_repo_data(
    repo_path: str,
    headers: dict | None = None,
    timeout: int = 15,
) -> dict | None:
    if headers is None:
        headers = get_github_headers()
    api_url = f"https://api.github.com/repos/{repo_path}"
    try:
        response = requests.get(api_url, headers=headers, timeout=timeout)
        if response.status_code == 200:
            return response.json()
        else:
            print(
                f"Warning: Failed to fetch {repo_path} (Status Code: {response.status_code})"
            )
            return None
    except Exception as e:
        print(f"Error fetching {repo_path}: {e}")
        return None


def fetch_repo_summary(
    repo_path: str,
    headers: dict | None = None,
    timeout: int = 15,
) -> tuple[str, int]:
    repo_data = fetch_repo_data(repo_path, headers=headers, timeout=timeout)
    if not repo_data:
        return "", 0
    stars = repo_data.get("stargazers_count", 0)
    last_commit = format_commit_date(repo_data.get("pushed_at"))
    return last_commit, stars
