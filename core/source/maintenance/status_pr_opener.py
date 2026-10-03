from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Any

import requests

CORE_DIR = Path(__file__).resolve().parents[2]
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))

from source.maintenance.json_formatter import run_format_checks  # noqa: E402
from source.maintenance.status_checker import get_status_candidates  # noqa: E402
from source.utils.github_utils import get_github_headers, get_github_token  # noqa: E402
from source.utils.path_utils import DYNAMIC_DATA_DIR, STATIC_DATA_DIR  # noqa: E402


def slugify(text: str) -> str:
    """Normalize text into a lowercase, hyphen-separated slug suitable for branch names."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")


def get_repo_slug() -> str:
    """Retrieve owner/repo from GITHUB_REPOSITORY or git remote origin."""
    repo = os.getenv("GITHUB_REPOSITORY")
    if repo and "/" in repo:
        return repo.strip()

    try:
        res = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            capture_output=True,
            text=True,
            check=True,
        )
        url = res.stdout.strip()
        if "github.com" in url:
            if url.endswith(".git"):
                url = url[:-4]
            if "github.com/" in url:
                return url.split("github.com/")[1]
            elif "github.com:" in url:
                return url.split("github.com:")[1]
    except Exception:
        pass

    return "mustbeperfect/definitive-opensource"


def get_open_pull_requests(
    repo_slug: str, token: str | None = None
) -> list[dict[str, Any]]:
    """Retrieve list of currently open pull requests for the repository."""
    # 1. Attempt using gh CLI if available
    try:
        res = subprocess.run(
            [
                "gh",
                "pr",
                "list",
                "--repo",
                repo_slug,
                "--state",
                "open",
                "--json",
                "headRefName,title,number,url",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        if res.returncode == 0 and res.stdout.strip():
            raw_prs = json.loads(res.stdout)
            return [
                {
                    "head_ref": pr.get("headRefName", ""),
                    "title": pr.get("title", ""),
                    "number": pr.get("number"),
                    "url": pr.get("url", ""),
                }
                for pr in raw_prs
            ]
    except Exception:
        pass

    # 2. Fallback: GitHub REST API
    headers = get_github_headers(token)
    api_url = f"https://api.github.com/repos/{repo_slug}/pulls?state=open&per_page=100"
    try:
        response = requests.get(api_url, headers=headers, timeout=15)
        if response.status_code == 200:
            raw_prs = response.json()
            return [
                {
                    "head_ref": pr.get("head", {}).get("ref", ""),
                    "title": pr.get("title", ""),
                    "number": pr.get("number"),
                    "url": pr.get("html_url", ""),
                }
                for pr in raw_prs
            ]
    except Exception as e:
        print(f"Notice: Failed to fetch open pull requests via REST API: {e}")

    return []


def find_existing_pr(
    branch_name: str,
    title: str,
    open_prs: list[dict[str, Any]],
) -> dict[str, Any] | None:
    """Check if a PR is already open for this branch or exact title."""
    for pr in open_prs:
        if pr.get("head_ref") == branch_name or pr.get("title") == title:
            return pr
    return None


def apply_archive_change(
    applications_file: Path,
    archive_file: Path,
    app_name: str,
    repo_url: str,
    reason: str = "archived",
) -> bool:
    """Move an application from applications.json to archive.json."""
    if not applications_file.exists() or not archive_file.exists():
        return False

    with open(applications_file, "r", encoding="utf-8") as f:
        apps_data = json.load(f)

    with open(archive_file, "r", encoding="utf-8") as f:
        archive_data = json.load(f)

    clean_target_url = repo_url.strip().lower().rstrip("/")
    if clean_target_url.endswith(".git"):
        clean_target_url = clean_target_url[:-4]

    target_name_lower = app_name.strip().lower()

    matching_apps = []
    remaining_apps = []
    for app in apps_data.get("applications", []):
        cur_url = app.get("repo_url", "").strip().lower().rstrip("/")
        if cur_url.endswith(".git"):
            cur_url = cur_url[:-4]
        cur_name = app.get("name", "").strip().lower()

        if cur_url == clean_target_url or cur_name == target_name_lower:
            matching_apps.append(app)
        else:
            remaining_apps.append(app)

    if not matching_apps:
        print(f"Notice: '{app_name}' not found in applications.json (already removed).")
        return False

    apps_data["applications"] = remaining_apps

    existing_archive_urls = {
        a.get("repo_url", "").strip().lower().rstrip("/")
        for a in archive_data.get("applications", [])
    }
    if clean_target_url not in existing_archive_urls:
        archive_data.setdefault("applications", []).append(
            {
                "name": app_name,
                "repo_url": repo_url.strip(),
                "reason": reason,
            }
        )

    with open(applications_file, "w", encoding="utf-8") as f:
        json.dump(apps_data, f, indent=4)
        f.write("\n")

    with open(archive_file, "w", encoding="utf-8") as f:
        json.dump(archive_data, f, indent=2)
        f.write("\n")

    return True


def apply_rebrand_change(
    applications_file: Path,
    app_name: str,
    old_repo_url: str,
    new_repo_url: str,
) -> bool:
    """Update repo_url of an application in applications.json."""
    if not applications_file.exists():
        return False

    with open(applications_file, "r", encoding="utf-8") as f:
        apps_data = json.load(f)

    clean_old_url = old_repo_url.strip().lower().rstrip("/")
    if clean_old_url.endswith(".git"):
        clean_old_url = clean_old_url[:-4]

    target_name_lower = app_name.strip().lower()

    updated = False
    for app in apps_data.get("applications", []):
        cur_url = app.get("repo_url", "").strip().lower().rstrip("/")
        if cur_url.endswith(".git"):
            cur_url = cur_url[:-4]
        cur_name = app.get("name", "").strip().lower()

        if cur_url == clean_old_url or cur_name == target_name_lower:
            if app.get("repo_url") != new_repo_url.strip():
                app["repo_url"] = new_repo_url.strip()
                updated = True
            break

    if not updated:
        return False

    with open(applications_file, "w", encoding="utf-8") as f:
        json.dump(apps_data, f, indent=4)
        f.write("\n")

    return True


def build_pr_content(candidate: dict[str, Any]) -> tuple[str, str, str]:
    """Generate (branch_name, title, body) for a given candidate."""
    name = candidate["name"]
    action_type = candidate.get("type", "archive")
    slug = slugify(name)

    if action_type == "archive":
        reason = candidate.get("reason", "archived")
        repo_url = candidate["repo_url"]
        branch_name = f"maintenance/archive-{slug}"

        if reason == "deleted":
            title = f"chore(archive): move {name} to archive (deleted)"
            body = (
                f"### 📦 Move to Archive: {name}\n\n"
                f"The repository for **{name}** no longer exists (404 / unresolvable) on GitHub.\n\n"
                f"- **Project**: {name}\n"
                f"- **GitHub URL**: {repo_url}\n"
                f"- **Archive Reason**: `deleted`\n\n"
                f"#### Changes\n"
                f"- Removed `{name}` from `core/data/static/applications.json`\n"
                f"- Added `{name}` to `core/data/static/archive.json` with reason `deleted`\n\n"
                f"---\n"
                f"*Automated pull request opened by Definitive OpenSource status maintenance.*"
            )
        else:
            title = f"chore(archive): move {name} to archive"
            body = (
                f"### 📦 Move to Archive: {name}\n\n"
                f"The repository for **{name}** has been archived on GitHub.\n\n"
                f"- **Project**: {name}\n"
                f"- **GitHub URL**: {repo_url}\n"
                f"- **Archive Reason**: `archived`\n\n"
                f"#### Changes\n"
                f"- Removed `{name}` from `core/data/static/applications.json`\n"
                f"- Added `{name}` to `core/data/static/archive.json` with reason `archived`\n\n"
                f"---\n"
                f"*Automated pull request opened by Definitive OpenSource status maintenance.*"
            )
        return branch_name, title, body

    elif action_type == "rebrand":
        old_url = candidate["repo_url"]
        new_url = candidate["new_repo_url"]
        branch_name = f"maintenance/rebrand-{slug}"
        title = f"chore(url): update {name} repository URL"
        body = (
            f"### 🔄 Rebrand / Move: {name}\n\n"
            f"The repository for **{name}** has moved or rebranded on GitHub.\n\n"
            f"- **Project**: {name}\n"
            f"- **New GitHub URL**: {new_url}\n"
            f"- **Previous URL**: {old_url}\n\n"
            f"#### Changes\n"
            f"- Updated `repo_url` in `core/data/static/applications.json` to `{new_url}`\n\n"
            f"---\n"
            f"*Automated pull request opened by Definitive OpenSource status maintenance.*"
        )
        return branch_name, title, body

    raise ValueError(f"Unknown candidate action type: {action_type}")


def create_pull_request(
    repo_slug: str,
    branch_name: str,
    title: str,
    body: str,
    base: str = "main",
    token: str | None = None,
) -> str | None:
    """Create a pull request using gh CLI or GitHub REST API."""
    # 1. Try gh CLI
    try:
        res = subprocess.run(
            [
                "gh",
                "pr",
                "create",
                "--repo",
                repo_slug,
                "--title",
                title,
                "--body",
                body,
                "--head",
                branch_name,
                "--base",
                base,
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        if res.returncode == 0:
            pr_url = res.stdout.strip()
            print(f"Created PR via gh CLI: {pr_url}")
            return pr_url
        else:
            print(f"gh pr create notice: {res.stderr.strip()}")
    except Exception as e:
        print(f"gh CLI error: {e}")

    # 2. Fallback: GitHub REST API
    headers = get_github_headers(token)
    api_url = f"https://api.github.com/repos/{repo_slug}/pulls"
    payload = {
        "title": title,
        "body": body,
        "head": branch_name,
        "base": base,
    }
    try:
        response = requests.post(api_url, headers=headers, json=payload, timeout=20)
        if response.status_code == 201:
            pr_data = response.json()
            pr_url = pr_data.get("html_url", "")
            print(f"Created PR via GitHub REST API: {pr_url}")
            return pr_url
        else:
            print(
                f"Failed to create PR via API ({response.status_code}): {response.text[:300]}"
            )
            return None
    except Exception as e:
        print(f"Error creating PR via API: {e}")
        return None


def process_single_candidate(
    candidate: dict[str, Any],
    repo_slug: str,
    static_dir: Path,
    open_prs: list[dict[str, Any]],
    base_branch: str = "main",
    dry_run: bool = False,
    token: str | None = None,
) -> str:
    """Process a single candidate and create PR if needed.

    Returns status: 'created', 'dry_run', 'already_open', 'not_modified', 'failed'
    """
    branch_name, title, body = build_pr_content(candidate)
    name = candidate["name"]

    # Check if PR is already open
    existing = find_existing_pr(branch_name, title, open_prs)
    if existing:
        print(
            f"Skipping {name}: PR #{existing.get('number')} already open ({existing.get('url')})"
        )
        return "already_open"

    apps_file = static_dir / "applications.json"
    archive_file = static_dir / "archive.json"

    if dry_run:
        print(f"[DRY RUN] Would create PR for '{name}':")
        print(f"  Branch: {branch_name}")
        print(f"  Title:  {title}")
        print(f"  Action: {candidate.get('type')}")
        if candidate.get("type") == "archive":
            print(
                f"  Target: Move {name} ({candidate['repo_url']}) to archive.json ({candidate.get('reason')})"
            )
        elif candidate.get("type") == "rebrand":
            print(f"  Target: Update URL to {candidate['new_repo_url']}")
        return "dry_run"

    # Save starting branch
    try:
        res = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        starting_branch = res.stdout.strip()
    except Exception:
        starting_branch = base_branch

    try:
        base_ref = f"origin/{base_branch}"
        fetch_res = subprocess.run(
            ["git", "rev-parse", "--verify", base_ref],
            capture_output=True,
            text=True,
            check=False,
        )
        start_point = base_ref if fetch_res.returncode == 0 else base_branch

        subprocess.run(
            ["git", "checkout", "-B", branch_name, start_point],
            check=True,
            capture_output=True,
        )

        if candidate.get("type") == "archive":
            modified = apply_archive_change(
                applications_file=apps_file,
                archive_file=archive_file,
                app_name=name,
                repo_url=candidate["repo_url"],
                reason=candidate.get("reason", "archived"),
            )
            files_to_add = [str(apps_file), str(archive_file)]
        elif candidate.get("type") == "rebrand":
            modified = apply_rebrand_change(
                applications_file=apps_file,
                app_name=name,
                old_repo_url=candidate["repo_url"],
                new_repo_url=candidate["new_repo_url"],
            )
            files_to_add = [str(apps_file)]
        else:
            modified = False
            files_to_add = []

        if not modified:
            print(f"Skipping {name}: No changes needed in data files.")
            return "not_modified"

        # Validate JSON integrity
        report_data, total_issues, _ = run_format_checks(
            static_data_dir=static_dir,
            report_output_file=Path("/dev/null"),
        )
        if total_issues > 0:
            print(
                f"Warning: Format checks failed for {name} ({total_issues} issues). Aborting PR."
            )
            return "failed"

        subprocess.run(["git", "add"] + files_to_add, check=True)
        diff_res = subprocess.run(
            ["git", "diff", "--staged", "--quiet"],
            check=False,
        )
        if diff_res.returncode == 0:
            print(f"Notice: git diff was empty for {name}. Skipping.")
            return "not_modified"

        subprocess.run(["git", "commit", "-m", title], check=True, capture_output=True)

        push_res = subprocess.run(
            ["git", "push", "-u", "origin", branch_name, "--force"],
            capture_output=True,
            text=True,
            check=False,
        )
        if push_res.returncode != 0:
            print(f"Error pushing branch {branch_name}: {push_res.stderr.strip()}")
            return "failed"

        pr_url = create_pull_request(
            repo_slug=repo_slug,
            branch_name=branch_name,
            title=title,
            body=body,
            base=base_branch,
            token=token,
        )
        if pr_url:
            return "created"
        return "failed"

    except Exception as e:
        print(f"Error processing {name}: {e}")
        return "failed"
    finally:
        subprocess.run(
            ["git", "checkout", starting_branch], capture_output=True, check=False
        )
        subprocess.run(
            ["git", "checkout", "--", "."], capture_output=True, check=False
        )


def run_status_pr_opener(
    dynamic_file: Path | str | None = None,
    static_dir: Path | str | None = None,
    dry_run: bool = False,
    max_prs: int = 10,
    token: str | None = None,
    repo_slug: str | None = None,
    base_branch: str = "main",
) -> dict[str, list[str]]:
    """Scan candidate applications and open pull requests for archived, deleted, or rebranded projects."""
    if dynamic_file is None:
        dynamic_path = DYNAMIC_DATA_DIR / "applications_generated.json"
    else:
        dynamic_path = Path(dynamic_file)

    if static_dir is None:
        static_path = STATIC_DATA_DIR
    else:
        static_path = Path(static_dir)

    if token is None:
        token = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN") or get_github_token()

    if repo_slug is None:
        repo_slug = get_repo_slug()

    print(
        f"Scanning {dynamic_path} for status changes (dry_run={dry_run}, max_prs={max_prs})..."
    )
    candidates = get_status_candidates(input_file=dynamic_path)

    to_process: list[dict[str, Any]] = []
    to_process.extend(candidates.get("archived", []))
    to_process.extend(candidates.get("no_longer_exists", []))
    to_process.extend(candidates.get("rebranded", []))

    if not to_process:
        print("No archived, deleted, or rebranded projects detected.")
        return {"created": [], "already_open": [], "skipped": []}

    print(f"Found {len(to_process)} candidate action(s). Fetching open PRs...")
    open_prs = get_open_pull_requests(repo_slug, token=token) if not dry_run else []

    results: dict[str, list[str]] = {
        "created": [],
        "already_open": [],
        "skipped": [],
    }

    created_count = 0
    for cand in to_process:
        if created_count >= max_prs:
            print(f"Reached maximum PR limit of {max_prs}. Stopping.")
            break

        status = process_single_candidate(
            candidate=cand,
            repo_slug=repo_slug,
            static_dir=static_path,
            open_prs=open_prs,
            base_branch=base_branch,
            dry_run=dry_run,
            token=token,
        )

        name = cand["name"]
        if status in ("created", "dry_run"):
            results["created"].append(name)
            created_count += 1
        elif status == "already_open":
            results["already_open"].append(name)
        else:
            results["skipped"].append(name)

    print("\n=== Status PR Opener Summary ===")
    print(f"Created:      {len(results['created'])} ({', '.join(results['created']) or 'None'})")
    print(
        f"Already Open: {len(results['already_open'])} ({', '.join(results['already_open']) or 'None'})"
    )
    print(f"Skipped:      {len(results['skipped'])} ({', '.join(results['skipped']) or 'None'})")

    return results


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Auto-open PRs for archived, deleted, or rebranded projects."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate PR creation without touching git branches or remote.",
    )
    parser.add_argument(
        "--max-prs",
        type=int,
        default=10,
        help="Maximum number of PRs to open in one run (default: 10).",
    )
    parser.add_argument(
        "--token",
        type=str,
        default=None,
        help="GitHub personal access token or actions token.",
    )
    parser.add_argument(
        "--repo",
        type=str,
        default=None,
        help="Target GitHub repository (owner/repo).",
    )
    parser.add_argument(
        "--dynamic-file",
        type=str,
        default=None,
        help="Path to applications_generated.json.",
    )
    parser.add_argument(
        "--static-dir",
        type=str,
        default=None,
        help="Path to static data directory.",
    )
    args = parser.parse_args()

    run_status_pr_opener(
        dynamic_file=args.dynamic_file,
        static_dir=args.static_dir,
        dry_run=args.dry_run,
        max_prs=args.max_prs,
        token=args.token,
        repo_slug=args.repo,
    )


if __name__ == "__main__":
    main()
