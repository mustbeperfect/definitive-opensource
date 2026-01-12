import json


# Utils
def slugify(name):
    return name.lower().replace(" ", "-").replace("(", "").replace(")", "")


def extract_repo_path(link):
    parts = link.rstrip("/").split("/")
    if len(parts) >= 5:
        return f"{parts[-2]}/{parts[-1]}"
    return ""


def format_stars(n):
    if n >= 1_000_000:
        formatted = f"{n / 1_000_000:.1f}M"
        return formatted.replace(".0M", "M")
    elif n >= 1_000:
        formatted = f"{n / 1_000:.1f}k"
        return formatted.replace(".0k", "k")
    else:
        return str(n)


# Generates actual list contents in markdown (categories and projects within)
def generate_contents(platform="all"):
    with open("core/data/static/categories.json", "r", encoding="utf-8") as f:
        cat_data = json.load(f)
    with open("core/data/dynamic/applications.json", "r", encoding="utf-8") as f:
        app_data = json.load(f)
    with open("core/data/static/tags.json", "r", encoding="utf-8") as f:
        tags_data = json.load(f)
    with open("core/data/static/platforms.json", "r", encoding="utf-8") as f:
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
    for sub in subcategories:
        parent = sub.get("parent", "other")
        subcat_by_parent.setdefault(parent, []).append(
            {"Name": sub["name"], "id": sub["id"]}
        )

    for key in subcat_by_parent:
        subcat_by_parent[key].sort(key=lambda x: x["Name"].lower())

    # Include projects relative to type of list being gneerated (all or platform specific)
    apps_by_subcat = {}
    for app in applications:
        include = False
        if platform == "all":
            include = True
        else:
            app_platforms = [p.lower() for p in app.get("platforms", [])]
            target = platform.lower()
            if target in app_platforms:
                include = True

            if target in ["macos", "linux", "windows"] and "cross" in app_platforms:
                include = True
        if not include:
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
        md_output += f"# {pname} - [Go to top](#table-of-contents)\n\n"

        for sub in subcat_by_parent.get(pid, []):
            subname = sub["Name"]
            md_output += f"### {subname}\n\n"
            md_output += "| Name | Description | Platform(s) | Stars |\n"
            md_output += "| --- | --- | --- | --- |\n"

            apps = apps_by_subcat.get(sub["id"], [])
            for app in apps:
                name = app.get("name", "")
                description = app.get("description", "").replace("|", "-")
                link = app.get("repo_url", "#")
                attribute_tags = ""
                property_tags = ""
                """
                if app.get("tags"):
                    tags += " " + " ".join(app["tags"])
                """
                if app.get("tags"):
                    # attribute_tags = " " + " ".join(attribute_map.get(tag, tag) for tag in app.get("tags", []))
                    attribute_tags = " " + " ".join(
                        attribute_map[tag]
                        for tag in app["tags"]
                        if tag in attribute_map
                    )
                    property_tags = " ".join(
                        f"`{property_map[tag]}`"
                        for tag in app["tags"]
                        if tag in property_map
                    )

                # app_platforms = " ".join(f"`{p}`" for p in app.get("platforms", []))
                app_platforms = " ".join(
                    f"`{platform_map.get(p, p)}`" for p in app.get("platforms", [])
                )
                stars = app.get("stars")
                stars_formatted = (
                    f"**{format_stars(stars)}**" if stars is not None else ""
                )
                # repo_path = extract_repo_path(link)
                md_output += f"| [{name}]({link}){attribute_tags}{property_tags} | {description} | {app_platforms} | {stars_formatted} |\n"
            md_output += "\n"
    return md_output


if __name__ == "__main__":
    # For testing, default to all platforms
    print(generate_contents("all"))
