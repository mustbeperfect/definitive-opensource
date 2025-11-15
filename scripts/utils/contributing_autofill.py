import argparse
import base64
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Set, Tuple
import requests

ROOT = Path(__file__).resolve().parents[2]
TAGS_FILE = ROOT / "source" / "data" / "static" / "tags.json"
PLATFORMS_FILE = ROOT / "source" / "data" / "static" / "platforms.json"
CATEGORIES_FILE = ROOT / "source" / "data" / "static" / "categories.json"
APPLICATIONS_FILE = ROOT / "source" / "data" / "dynamic" / "applications.json"
USER_AGENT = "definitive-opensource-contributing-autofill"
GITHUB_API_VERSION = "2022-11-28"

REPO_PATTERN = re.compile(
    r"(?:github\.com[:/])?(?P<owner>[\w\-.]+)/(?P<repo>[\w\-.]+?)(?:\.git)?(?:[#?].*)?$",
    re.IGNORECASE,
)

PLATFORM_KEYWORDS: Dict[str, str] = {}

TAG_KEYWORDS: Dict[str, str] = {}

CATEGORY_KEYWORDS: Dict[str, str] = {}


@dataclass
class ReferenceData:
    tag_ids: Set[str]
    platform_ids: Set[str]
    category_ids: Set[str]
    tag_labels: Dict[str, str]
    platform_labels: Dict[str, str]
    category_labels: Dict[str, str]


class DuplicateRepositoryError(RuntimeError):
    """Raised when attempting to append an application that already exists."""


def load_reference_data() -> ReferenceData:
    with open(TAGS_FILE, "r", encoding="utf-8") as fh:
        tags_data = json.load(fh)
    tag_labels: Dict[str, str] = {}
    for entry in tags_data.get("attributes", []):
        label = entry.get("description") or entry.get("name") or entry["id"]
        emoji = entry.get("emoji")
        if emoji:
            label = f"{emoji} {label}"
        tag_labels[entry["id"]] = label
    for entry in tags_data.get("properties", []):
        label = entry.get("name") or entry.get("description") or entry["id"]
        tag_labels[entry["id"]] = label
    tag_ids = set(tag_labels.keys())

    with open(PLATFORMS_FILE, "r", encoding="utf-8") as fh:
        platforms_data = json.load(fh)
    platform_labels = {
        entry["id"]: entry.get("name") or entry["id"] for entry in platforms_data.get("platforms", [])
    }
    platform_ids = set(platform_labels.keys())

    with open(CATEGORIES_FILE, "r", encoding="utf-8") as fh:
        categories_data = json.load(fh)
    category_labels: Dict[str, str] = {
        entry["id"]: entry.get("name") or entry["id"] for entry in categories_data.get("categories", [])
    }
    for entry in categories_data.get("subcategories", []):
        parent = entry.get("parent")
        parent_label = category_labels.get(parent, parent) if parent else None
        name = entry.get("name") or entry["id"]
        label = f"{name} ({parent_label})" if parent_label else name
        category_labels[entry["id"]] = label
    category_ids = set(category_labels.keys())

    return ReferenceData(
        tag_ids=tag_ids,
        platform_ids=platform_ids,
        category_ids=category_ids,
        tag_labels=tag_labels,
        platform_labels=platform_labels,
        category_labels=category_labels,
    )


def render_options(options: Dict[str, str], indent: str = "  ") -> str:
    lines = []
    for key, label in sorted(options.items()):
        descriptor = f"{key}: {label}" if label and label != key else key
        lines.append(f"{indent}- {descriptor}")
    return "\n".join(lines)


def available_text(label: str, options: Dict[str, str]) -> str:
    if not options:
        return ""
    return f"Available {label} ids:\n{render_options(options)}"


def load_applications_data(path: Path) -> Dict:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def persist_applications_data(path: Path, data: Dict) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=4)
        fh.write("\n")


def append_application(entry: Dict, path: Path) -> None:
    data = load_applications_data(path)
    applications = data.setdefault("applications", [])
    new_url = (entry.get("repo_url") or "").rstrip("/")
    for existing in applications:
        if (existing.get("repo_url") or "").rstrip("/") == new_url:
            try:
                display_path = path.relative_to(ROOT)
            except ValueError:
                display_path = path
            raise DuplicateRepositoryError(
                f"Repository {entry['repo_url']} already exists in {display_path}."
            )
    applications.append(entry)
    persist_applications_data(path, data)


def parse_repo_identifier(value: str) -> Tuple[str, str]:
    value = value.strip()
    match = REPO_PATTERN.search(value)
    if match:
        return match.group("owner"), match.group("repo")
    if "/" in value:
        owner, repo = value.split("/", 1)
        return owner, repo
    raise ValueError(f"Could not parse repository from '{value}'.")


def github_request(path: str, token: Optional[str], params: Optional[Dict[str, str]] = None) -> requests.Response:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": USER_AGENT,
        "X-GitHub-Api-Version": GITHUB_API_VERSION,
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    url = f"https://api.github.com/{path.lstrip('/')}"
    response = requests.get(url, headers=headers, params=params or {})
    if response.status_code == 401:
        raise RuntimeError("GitHub authentication failed. Set the GITHUB_TOKEN environment variable.")
    if response.status_code == 403 and "rate limit" in response.text.lower():
        raise RuntimeError("GitHub rate limit exceeded. Provide a token to continue.")
    return response


def fetch_repo(owner: str, repo: str, token: Optional[str]) -> Dict:
    response = github_request(f"repos/{owner}/{repo}", token, params={"per_page": 1})
    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch repo metadata ({response.status_code}): {response.text}")
    return response.json()


def fetch_readme_excerpt(owner: str, repo: str, token: Optional[str]) -> Optional[str]:
    response = github_request(f"repos/{owner}/{repo}/readme", token)
    if response.status_code != 200:
        return None
    payload = response.json()
    content = payload.get("content")
    if not content:
        return None
    try:
        decoded = base64.b64decode(content).decode("utf-8", errors="replace")
    except (ValueError, UnicodeDecodeError):
        return None
    for line in decoded.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            stripped = stripped.lstrip("#").strip()
        stripped = stripped.rstrip(".")
        if stripped:
            return stripped
    return None


def normalize_project_name(repo_name: str) -> str:
    if not repo_name:
        return ""
    if any(ch.isupper() for ch in repo_name if ch.isalpha()):
        return repo_name
    tokens = [token for token in re.split(r"[-_]", repo_name) if token]
    if tokens:
        return " ".join(token.capitalize() for token in tokens)
    return repo_name.capitalize()


def iso_to_mmddyyyy(value: Optional[str]) -> str:
    if not value:
        return ""
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").strftime("%m/%d/%Y")
    except ValueError:
        return ""


def keyword_hits(keywords: Dict[str, str], sources: Sequence[str]) -> Set[str]:
    if not sources:
        return set()
    haystack = " ".join(filter(None, sources)).lower()
    matches: Set[str] = set()
    for needle, mapped in keywords.items():
        if re.search(rf"\b{re.escape(needle)}\b", haystack):
            matches.add(mapped)
    return matches


def infer_platforms(repo: Dict, ref: ReferenceData) -> Tuple[Set[str], List[str]]:
    notes: List[str] = []
    notes.append(
        "Platforms were not inferred automatically.\n"
        f"{available_text('platform', ref.platform_labels)}"
    )
    return set(), notes


def infer_tags(repo: Dict, ref: ReferenceData) -> Tuple[Set[str], List[str]]:
    return set(), []


def infer_category(repo: Dict, ref: ReferenceData) -> Tuple[str, List[str]]:
    return "", [
        "Category must be specified manually.\n"
        f"{available_text('category', ref.category_labels)}"
    ]


def prompt_list(field_label: str, options: Dict[str, str], allow_empty: bool = False) -> List[str]:
    valid_values = set(options.keys())
    print(f"\n{available_text(field_label, options)}")
    skip_hint = " (press Enter to skip)" if allow_empty else ""
    prompt = f"Enter {field_label} ids (comma separated){skip_hint}:\n> "
    while True:
        raw = input(prompt).strip()
        if not raw and allow_empty:
            return []
        values = [val.strip() for val in raw.split(",") if val.strip()]
        invalid = [val for val in values if val not in valid_values]
        if invalid:
            print(f"Invalid values: {', '.join(invalid)}. Please try again.")
            continue
        if not values:
            print("At least one value is required. Press Ctrl+C to abort.")
            continue
        return values


def prompt_value(field_label: str, options: Dict[str, str]) -> str:
    valid_values = set(options.keys())
    print(f"\n{available_text(field_label, options)}")
    prompt = f"Enter {field_label} id:\n> "
    while True:
        raw = input(prompt).strip()
        if raw in valid_values:
            return raw
        print(f"{raw} is not a valid value. Please try again.")


def fill_missing_with_input(entry: Dict, ref: ReferenceData) -> Dict:
    if not sys.stdin.isatty():
        return entry

    updated = entry.copy()
    if not updated.get("platforms"):
        updated["platforms"] = prompt_list("platform", ref.platform_labels)
    if not updated.get("tags"):
        updated["tags"] = prompt_list("tag", ref.tag_labels, allow_empty=True)
    if not updated.get("category"):
        updated["category"] = prompt_value("category", ref.category_labels)
    return updated


def filter_resolved_notes(notes: List[str], entry: Dict) -> List[str]:
    filtered: List[str] = []
    for note in notes:
        lowered = note.lower()
        if "platform" in lowered and entry.get("platforms"):
            continue
        if "tag" in lowered and entry.get("tags"):
            continue
        if "category" in lowered and entry.get("category"):
            continue
        filtered.append(note)
    return filtered


def build_entry(
    repo_url: str,
    repo_data: Dict,
    ref: ReferenceData,
    owner: str,
    repo: str,
    full_details: bool,
    token: Optional[str],
) -> Tuple[Dict, List[str]]:
    notes: List[str] = []
    flags: Set[str] = set()

    repo_description = repo_data.get("description") or ""
    readme_description: Optional[str] = None
    if full_details and not repo_description:
        readme_description = fetch_readme_excerpt(owner, repo, token)

    name = normalize_project_name(repo_data.get("name", ""))
    platforms, platform_notes = infer_platforms(repo_data, ref)
    notes.extend(platform_notes)
    tags, tag_notes = infer_tags(repo_data, ref)
    notes.extend(tag_notes)
    category, category_notes = infer_category(repo_data, ref)
    notes.extend(category_notes)

    entry = {
        "name": name,
        "description": "",
        "repo_url": repo_url,
        "tags": sorted(tags),
        "platforms": sorted(platforms),
        "category": category,
        "stars": 0,
        "flags": sorted(flags),
        "last_commit": "",
        "language": "",
        "license": "",
        "homepage_url": "",
    }

    if full_details:
        description_value = repo_description or readme_description or ""
        entry["description"] = description_value
        if readme_description and not repo_description:
            flags.add("custom-description")
            notes.append("Description pulled from README (custom-description flag added).")
        elif not description_value:
            notes.append("Repository has no description; field left blank.")

        entry["stars"] = repo_data.get("stargazers_count", 0)
        entry["last_commit"] = iso_to_mmddyyyy(repo_data.get("pushed_at"))
        entry["language"] = repo_data.get("language") or ""
        license_data = repo_data.get("license") or {}
        entry["license"] = license_data.get("spdx_id") or license_data.get("name") or ""
        entry["homepage_url"] = repo_data.get("homepage") or ""

    entry["flags"] = sorted(flags)

    invalid_tags = [tag for tag in entry["tags"] if tag not in ref.tag_ids]
    if invalid_tags:
        raise ValueError(f"Invalid tag ids supplied: {', '.join(invalid_tags)}")

    invalid_platforms = [platform for platform in entry["platforms"] if platform not in ref.platform_ids]
    if invalid_platforms:
        raise ValueError(f"Invalid platform ids supplied: {', '.join(invalid_platforms)}")

    if entry["category"] and entry["category"] not in ref.category_ids:
        raise ValueError(f"Invalid category id supplied: {entry['category']}")

    if not entry["platforms"]:
        notes.append(
            "No platforms detected; please review `platforms`.\n"
            f"{available_text('platform', ref.platform_labels)}"
        )
    if not entry["category"]:
        notes.append(
            "Category missing; update `category` manually.\n"
            f"{available_text('category', ref.category_labels)}"
        )

    return entry, notes


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate an applications.json entry from a GitHub repository URL."
    )
    parser.add_argument("repo", help="GitHub repository URL or owner/repo slug.")
    parser.add_argument(
        "--applications-file",
        default=str(APPLICATIONS_FILE),
        help="Path to applications.json (default: source/data/dynamic/applications.json).",
    )
    parser.add_argument(
        "--full-details",
        action="store_true",
        help="Populate optional fields (description, stats, license, homepage) using GitHub data.",
    )

    args = parser.parse_args()
    owner, repo_name = parse_repo_identifier(args.repo)
    repo_url = f"https://github.com/{owner}/{repo_name}"

    token = os.getenv("GITHUB_TOKEN")

    repo_data = fetch_repo(owner, repo_name, token)
    ref = load_reference_data()
    entry, notes = build_entry(repo_url, repo_data, ref, owner, repo_name, args.full_details, token)
    entry = fill_missing_with_input(entry, ref)
    notes = filter_resolved_notes(notes, entry)

    applications_path = Path(args.applications_file).resolve()

    print(json.dumps(entry, indent=4))
    if notes:
        print("\nNotes:")
        for note in notes:
            print(f"- {note}")

    try:
        append_application(entry, applications_path)
    except DuplicateRepositoryError as exc:
        print(f"\nEntry skipped: {exc}")
        print("Hint: If you meant to update that entry, edit applications.json directly.")
        return

    print(f"\nAdded entry to {applications_path}")


if __name__ == "__main__":
    main()
