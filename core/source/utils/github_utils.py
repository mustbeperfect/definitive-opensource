from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import json
import os
import subprocess
from typing import Any

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


def format_time_ago(commit_date_str: str) -> str:
    """Format an %m/%d/%Y commit date string as a relative human-readable time."""
    if not commit_date_str:
        return "N/A"
    try:
        commit_date = datetime.strptime(commit_date_str, "%m/%d/%Y").date()
    except Exception:
        return "Unknown"

    today = datetime.now().date()
    days = (today - commit_date).days

    if days <= 0:
        return "Today"
    if days == 1:
        return "Yesterday"
    if days < 7:
        return f"{days} days ago"
    if days < 30:
        weeks = days // 7
        return f"{weeks} week{'s' if weeks > 1 else ''} ago"
    if days < 365:
        months = days // 30
        return f"{months} month{'s' if months > 1 else ''} ago"

    years = days // 365
    remaining_months = (days % 365) // 30
    if remaining_months > 0:
        return (
            f"{years} yr{'s' if years > 1 else ''}, "
            f"{remaining_months} mo{'s' if remaining_months > 1 else ''} ago"
        )
    return f"{years} year{'s' if years > 1 else ''} ago"


def fetch_repo_data(
    repo_path: str,
    headers: dict | None = None,
    timeout: int = 15,
    session: requests.Session | None = None,
) -> dict | None:
    if headers is None:
        headers = get_github_headers()
    api_url = f"https://api.github.com/repos/{repo_path}"
    client = session or requests
    try:
        response = client.get(api_url, headers=headers, timeout=timeout)
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


def build_graphql_repos_query(repo_pairs: list[tuple[str, str]]) -> str:
    """Construct a GraphQL query batching multiple repository lookups using aliases."""
    fields = """
        nameWithOwner
        description
        homepageUrl
        stargazerCount
        pushedAt
        isArchived
        primaryLanguage {
            name
        }
        licenseInfo {
            spdxId
        }
    """
    query_parts = ["query {"]
    for i, (owner, name) in enumerate(repo_pairs):
        owner_json = json.dumps(owner)
        name_json = json.dumps(name)
        query_parts.append(
            f"  repo_{i}: repository(owner: {owner_json}, name: {name_json}) {{{fields}}}"
        )
    query_parts.append("}")
    return "\n".join(query_parts)


def normalize_graphql_repo(raw_node: dict[str, Any] | None) -> dict[str, Any] | None:
    """Normalize a GitHub GraphQL Repository node to match REST API schema expectations."""
    if not raw_node:
        return None
    license_info = raw_node.get("licenseInfo")
    primary_language = raw_node.get("primaryLanguage")
    return {
        "stargazers_count": raw_node.get("stargazerCount", 0),
        "language": primary_language.get("name") if primary_language else None,
        "homepage": raw_node.get("homepageUrl") or "",
        "description": raw_node.get("description") or "",
        "license": (
            {"spdx_id": license_info.get("spdxId") or ""}
            if license_info and license_info.get("spdxId")
            else None
        ),
        "pushed_at": raw_node.get("pushedAt"),
        "archived": raw_node.get("isArchived", False),
        "full_name": raw_node.get("nameWithOwner", ""),
    }


def fetch_repos_batch_graphql(
    repo_paths: list[str],
    token: str | None = None,
    batch_size: int = 100,
    timeout: int = 30,
) -> dict[str, dict[str, Any] | None]:
    """
    Fetch repository data in bulk using the GitHub GraphQL API in batches.
    Batches lookups using aliases (up to batch_size repos per HTTP request).
    """
    if token is None:
        token = get_github_token()
    if not token:
        raise ValueError("GitHub token required for GraphQL API batch requests.")

    results: dict[str, dict[str, Any] | None] = {}
    graphql_url = "https://api.github.com/graphql"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v4+json",
        "User-Agent": "definitive-opensource",
    }

    for i in range(0, len(repo_paths), batch_size):
        batch = repo_paths[i : i + batch_size]
        batch_pairs: list[tuple[str, str]] = []
        valid_indices: list[int] = []

        for idx, path in enumerate(batch):
            parts = path.split("/")
            if len(parts) == 2 and parts[0] and parts[1]:
                batch_pairs.append((parts[0], parts[1]))
                valid_indices.append(idx)
            else:
                results[path] = None

        if not batch_pairs:
            continue

        query = build_graphql_repos_query(batch_pairs)
        batch_num = (i // batch_size) + 1
        total_batches = (len(repo_paths) + batch_size - 1) // batch_size
        print(
            f"Fetching GraphQL batch {batch_num}/{total_batches} ({len(batch_pairs)} repos)..."
        )

        try:
            response = requests.post(
                graphql_url,
                json={"query": query},
                headers=headers,
                timeout=timeout,
            )
            if response.status_code != 200:
                print(
                    f"Warning: GraphQL request failed (Status {response.status_code}): {response.text[:200]}"
                )
                for path in batch:
                    if path not in results:
                        results[path] = None
                continue

            res_json = response.json()
            data = res_json.get("data") or {}

            for query_idx, orig_idx in enumerate(valid_indices):
                orig_path = batch[orig_idx]
                raw_node = data.get(f"repo_{query_idx}")
                results[orig_path] = normalize_graphql_repo(raw_node)

        except Exception as e:
            print(f"Error executing GraphQL query for batch {batch_num}: {e}")
            for path in batch:
                if path not in results:
                    results[path] = None

    return results


def fetch_repos_batch_rest(
    repo_paths: list[str],
    headers: dict | None = None,
    max_workers: int = 8,
    timeout: int = 15,
) -> dict[str, dict[str, Any] | None]:
    """Fetch repository data concurrently using ThreadPoolExecutor and GitHub REST API."""
    if headers is None:
        headers = get_github_headers()

    results: dict[str, dict[str, Any] | None] = {}
    total = len(repo_paths)
    if total == 0:
        return results

    print(
        f"Fetching {total} repos concurrently via REST (max_workers={max_workers})..."
    )

    with requests.Session() as session:
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=max_workers,
            pool_maxsize=max_workers,
            max_retries=2,
        )
        session.mount("https://", adapter)
        session.mount("http://", adapter)

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_repo = {
                executor.submit(
                    fetch_repo_data,
                    path,
                    headers=headers,
                    timeout=timeout,
                    session=session,
                ): path
                for path in repo_paths
            }
            completed = 0
            for future in as_completed(future_to_repo):
                repo_path = future_to_repo[future]
                completed += 1
                try:
                    results[repo_path] = future.result()
                except Exception as e:
                    print(f"Error fetching {repo_path} via REST: {e}")
                    results[repo_path] = None

                if completed % 100 == 0 or completed == total:
                    print(f"REST progress: {completed}/{total} completed.")

    return results


def fetch_repos_batch(
    repo_paths: list[str],
    token: str | None = None,
    headers: dict | None = None,
    batch_size: int = 100,
    max_workers: int = 8,
    timeout: int = 30,
) -> dict[str, dict[str, Any] | None]:
    """
    Fetch repository metadata in bulk.
    Uses GitHub GraphQL API (batched in chunks of batch_size) if a token is available.
    Falls back to REST for any unresolvable repos (e.g. renamed repos following redirects)
    or falls back to concurrent REST if GraphQL is unavailable or unauthenticated.
    """
    unique_paths = list(dict.fromkeys(repo_paths))
    if not unique_paths:
        return {}

    if token is None:
        token = get_github_token()

    if headers is None:
        headers = get_github_headers(token)

    results: dict[str, dict[str, Any] | None] = {}

    if token:
        try:
            print(
                f"Batch fetching metadata for {len(unique_paths)} repositories via GitHub GraphQL API..."
            )
            results = fetch_repos_batch_graphql(
                unique_paths, token=token, batch_size=batch_size, timeout=timeout
            )
        except Exception as e:
            print(
                f"GraphQL batch fetch failed ({e}). Falling back to threaded REST API..."
            )
            results = {}

        # Check for repositories that were not resolved via GraphQL (e.g. renamed or moved repos)
        unresolved = [p for p in unique_paths if results.get(p) is None]
        if unresolved and len(unresolved) < len(unique_paths):
            print(
                f"{len(unresolved)} repos not resolved via GraphQL. Falling back to REST for these repos..."
            )
            rest_fallback = fetch_repos_batch_rest(
                unresolved, headers=headers, max_workers=max_workers, timeout=timeout
            )
            results.update(rest_fallback)
        elif unresolved and len(unresolved) == len(unique_paths):
            # All repos failed via GraphQL; retry via REST
            print("All repos unresolved via GraphQL. Retrying via threaded REST API...")
            results = fetch_repos_batch_rest(
                unique_paths, headers=headers, max_workers=max_workers, timeout=timeout
            )
    else:
        print(
            "Warning: GITHUB_TOKEN not found. GraphQL batching requires authentication. "
            "Falling back to threaded REST API (requests may be rate-limited)."
        )
        results = fetch_repos_batch_rest(
            unique_paths, headers=headers, max_workers=max_workers, timeout=timeout
        )

    return results

