import json

def slugify(name):

    return name.lower().replace(" ", "-").replace("(", "").replace(")", "")

def extract_repo_path(link):

    parts = link.rstrip("/").split("/")
    if len(parts) >= 5:
        return f"{parts[-2]}/{parts[-1]}"
    return ""

def format_stars(n):
    if n >= 1_000_000:
        formatted = f"{n/1_000_000:.1f}M"
        return formatted.replace('.0M', 'M')
    elif n >= 1_000:
        formatted = f"{n/1_000:.1f}k"
        return formatted.replace('.0k', 'k')
    else:
        return str(n)

def generate_contents(platform="all"):

    with open("source/data/categories.json", "r", encoding="utf-8") as f:
        cat_data = json.load(f)
    with open("source/data/applications.json", "r", encoding="utf-8") as f:
        app_data = json.load(f)
    with open("source/data/tags.json", "r", encoding="utf-8") as f:
        tags_data = json.load(f)    
    
    categories = cat_data.get("categories", [])
    subcategories = cat_data.get("subcategories", [])
    applications = app_data.get("applications", [])
    

    parent_map = {cat["id"]: cat["name"] for cat in categories}


    tag_map = {tag["id"]: tag["emoji"] for tag in tags_data["tags"]}
    

    subcat_by_parent = {}
    for sub in subcategories:
        parent = sub.get("parent", "other")
        subcat_by_parent.setdefault(parent, []).append({
            "Name": sub["name"],
            "id": sub["id"]
        })

    for key in subcat_by_parent:
        subcat_by_parent[key].sort(key=lambda x: x["Name"].lower())
    

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

    parent_items = [(pid, parent_map.get(pid, pid)) for pid in subcat_by_parent if pid != "other"]
    parent_items.sort(key=lambda x: x[1].lower())
    if "other" in subcat_by_parent:
        parent_items.append(("other", "Other"))
    
    for pid, pname in parent_items:
        md_output += f"# {pname} - [Go to top](#contents)\n\n"

        for sub in subcat_by_parent.get(pid, []):
            subname = sub["Name"]
            md_output += f"### {subname}\n\n"
            md_output += "| Name | Description | Platform | Stars |\n"
            md_output += "| --- | --- | --- | --- |\n"

            apps = apps_by_subcat.get(sub["id"], [])
            for app in apps:
                name = app.get("name", "")
                description = app.get("description", "").replace("|", "-")
                link = app.get("repo_url", "#")
                tags = ""
                """
                if app.get("tags"):
                    tags += " " + " ".join(app["tags"])
                """        
                if app.get("tags"):
                    tags = " " + " ".join(tag_map.get(tag, tag) for tag in app.get("tags", []))

                app_platforms = " ".join(f"`{p}`" for p in app.get("platforms", []))
                stars = app.get("stars")
                stars_formatted = f"**{format_stars(stars)}**" if stars is not None else ""
                # repo_path = extract_repo_path(link)
                # stars_badge = f"![GitHub Repo stars](https://img.shields.io/github/stars/{repo_path}?style=for-the-badge&label=%20&color=white)" if repo_path else ""
                md_output += f"| [{name}]({link}){tags} | {description} | {app_platforms} | {stars_formatted} |\n"
            md_output += "\n"
    return md_output

if __name__ == "__main__":
    # For testing, default to 'all' platforms
    print(generate_contents("all"))
