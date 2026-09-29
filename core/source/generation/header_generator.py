import json
from pathlib import Path
import re
import sys

CORE_DIR = Path(__file__).resolve().parents[2]
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))

from source.generation.contents_generator import app_matches_platform  # noqa: E402
from source.utils.path_utils import COMPONENTS_DIR, DYNAMIC_DATA_DIR  # noqa: E402

PLATFORM_HEADERS = {
    "all": {
        "title": "definitive-opensource",
        "description": "The definitive list of the best of everything open source",
    },
    "windows": {
        "title": "Windows",
        "description": "Filtered for Windows and cross-platform apps",
    },
    "macos": {
        "title": "MacOS",
        "description": "Filtered for MacOS and cross-platform apps",
    },
    "linux": {
        "title": "Linux",
        "description": "Filtered for Linux and cross-platform apps",
    },
    "selfhost": {
        "title": "SelfHosted",
        "description": "Filtered for selfhosted apps",
    },
}

NAV_ITEMS = [
    {
        "id": "all",
        "name": "Main / All",
        "url": "https://github.com/mustbeperfect/definitive-opensource/blob/main/README.md",
    },
    {
        "id": "windows",
        "name": "Windows",
        "url": "https://github.com/mustbeperfect/definitive-opensource/blob/main/resources/readmes/windows.md",
    },
    {
        "id": "macos",
        "name": "MacOS",
        "url": "https://github.com/mustbeperfect/definitive-opensource/blob/main/resources/readmes/macos.md",
    },
    {
        "id": "linux",
        "name": "Linux",
        "url": "https://github.com/mustbeperfect/definitive-opensource/blob/main/resources/readmes/linux.md",
    },
    {
        "id": "selfhost",
        "name": "SelfHosted",
        "url": "https://github.com/mustbeperfect/definitive-opensource/blob/main/resources/readmes/selfhost.md",
    },
]


def normalize_platform(platform: str) -> str:
    p = platform.lower()
    if p in ("main", "readme"):
        return "all"
    if p == "selfhosted":
        return "selfhost"
    return p


def generate_top_header(platform: str = "all") -> str:
    norm_platform = normalize_platform(platform)
    with open(
        DYNAMIC_DATA_DIR / "applications_generated.json", "r", encoding="utf-8"
    ) as f:
        data = json.load(f)

    applications = data.get("applications", [])
    if norm_platform == "all":
        project_count = len(applications)
    else:
        project_count = len(
            [app for app in applications if app_matches_platform(app, norm_platform)]
        )

    info = PLATFORM_HEADERS.get(
        norm_platform,
        {
            "title": platform.capitalize(),
            "description": f"Filtered for {platform} apps",
        },
    )

    header_content = f"""
<table align="center">
    <tr>
    <td>🌍 v0.8.5-beta</td>
    </tr>
</table>

<h1 align="center">[ {info['title']} ] </h1>
<p align="center">{info['description']}</p>

<p align="center"><code>Status: Active</code> - <code>Projects: {project_count}</code></p>
"""
    return header_content


def generate_navbar(platform: str = "all") -> str:
    norm_platform = normalize_platform(platform)
    items_html = []
    for item in NAV_ITEMS:
        if item["id"] == norm_platform:
            items_html.append(f"<b>[ {item['name']} ]</b>")
        else:
            items_html.append(f'<a href="{item["url"]}">{item["name"]}</a>')

    joined = "\n  <span> · </span>\n  ".join(items_html)
    return f"""<h4 align="center">
  {joined}
</h4>"""


def generate_header(platform: str = "all") -> str:
    top_header = generate_top_header(platform)
    navbar = generate_navbar(platform)

    with open(COMPONENTS_DIR / "header.md", "r", encoding="utf-8") as f:
        header_template = f.read()

    if "<!-- NAVBAR -->" in header_template:
        body = header_template.replace("<!-- NAVBAR -->", navbar)
    else:
        body = re.sub(
            r'<h4 align="center">[\s\S]*?</h4>', navbar, header_template
        )

    return f"\n{top_header.strip()}\n\n{body.strip()}\n"


if __name__ == "__main__":
    print(generate_header("all"))
