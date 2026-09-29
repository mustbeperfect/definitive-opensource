import json
from pathlib import Path
import sys

CORE_DIR = Path(__file__).resolve().parents[2]
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))

from source.utils.markdown_utils import format_stars, sanitize_table_cell  # noqa: E402
from source.utils.path_utils import DYNAMIC_DATA_DIR, STATIC_DATA_DIR  # noqa: E402


def app_matches_platform(app, platform="all"):
    """Check if an application matches the target platform."""
    if platform == "all":
        return True
    app_platforms = [p.lower() for p in app.get("platforms", [])]
    target = platform.lower()
    if target in app_platforms:
        return True
    if target in ["macos", "linux", "windows"] and "cross" in app_platforms:
        return True
    return False


# Generates actual list contents in markdown (categories and projects within)
def generate_contents(platform="all"):
    with open(STATIC_DATA_DIR / "categories.json", "r", encoding="utf-8") as f:
        cat_data = json.load(f)
    with open(
        DYNAMIC_DATA_DIR / "applications_generated.json", "r", encoding="utf-8"
    ) as f:
        app_data = json.load(f)
    with open(STATIC_DATA_DIR / "tags.json", "r", encoding="utf-8") as f:
        tags_data = json.load(f)
    with open(STATIC_DATA_DIR / "platforms.json", "r", encoding="utf-8") as f:
        platforms_data = json.load(f)

    categories = cat_data.get("categories", [])
    subcategories = cat_data.get("subcategories", [])
    applications = app_data.get("applications", [])

    # Map id's to corresponding names
    parent_map = {cat["id"]: cat["name"] for cat in categories}
    attribute_map = {
        attribute["id"]: attribute["emoji"] for attribute in tags_data["attributes"]
    }
    property_map = {
        property["id"]: property["name"] for property in tags_data["properties"]
    }
    platform_map = {p["id"]: p["name"] for p in platforms_data["platforms"]}

    subcat_by_parent = {}
    seen_subcat_ids = set()
    for sub in subcategories:
        if sub["id"] in seen_subcat_ids:
            continue
        seen_subcat_ids.add(sub["id"])
        parent = sub.get("parent", "other")
        subcat_by_parent.setdefault(parent, []).append(
            {"Name": sub["name"], "id": sub["id"]}
        )

    for key in subcat_by_parent:
        subcat_by_parent[key].sort(key=lambda x: x["Name"].lower())

    # Include projects relative to type of list being generated (all or platform specific)
    apps_by_subcat = {}
    for app in applications:
        if not app_matches_platform(app, platform):
            continue

        cat_id = app.get("category", "uncategorized")
        apps_by_subcat.setdefault(cat_id, []).append(app)

    for key in apps_by_subcat:
        apps_by_subcat[key].sort(key=lambda x: x["name"].lower())

    md_output = ""

    parent_items = [
        (pid, parent_map.get(pid, pid)) for pid in subcat_by_parent if pid != "other"
    ]
    parent_items.sort(key=lambda x: x[1].lower())
    if "other" in subcat_by_parent:
        parent_items.append(("other", "Other"))

    for pid, pname in parent_items:
        # Check if this parent category has any subcategories with matching apps
        subs_with_apps = [
            sub
            for sub in subcat_by_parent.get(pid, [])
            if apps_by_subcat.get(sub["id"])
        ]
        if not subs_with_apps:
            continue

        md_output += f"# {pname} - [Go to top](#table-of-contents)\n\n"

        for sub in subs_with_apps:
            subname = sub["Name"]
            md_output += f"### {subname}\n\n"
            md_output += "| Name | Description | Platform(s) | Stars |\n"
            md_output += "| --- | --- | --- | --- |\n"

            apps = apps_by_subcat.get(sub["id"], [])
            for app in apps:
                name = app.get("name", "")
                description = sanitize_table_cell(app.get("description"))
                link = app.get("repo_url", "#")
                attribute_tags = ""
                property_tags = ""
                if app.get("tags"):
                    attribute_tags = " ".join(
                        attribute_map[tag]
                        for tag in app["tags"]
                        if tag in attribute_map
                    )
                    property_tags = " ".join(
                        f"`{property_map[tag]}`"
                        for tag in app["tags"]
                        if tag in property_map
                    )

                tags_display = " ".join(
                    [t for t in [attribute_tags, property_tags] if t]
                )
                tags_formatted = f" {tags_display}" if tags_display else ""

                # app_platforms = " ".join(f"`{p}`" for p in app.get("platforms", []))
                app_platforms = " ".join(
                    f"`{platform_map.get(p, p)}`" for p in app.get("platforms", [])
                )
                stars = app.get("stars")
                stars_formatted = (
                    f"**{format_stars(stars)}**" if stars is not None else ""
                )
                md_output += f"| [{name}]({link}){tags_formatted} | {description} | {app_platforms} | {stars_formatted} |\n"
            md_output += "\n"
    return md_output


if __name__ == "__main__":
    # For testing, default to all platforms
    print(generate_contents("all"))
