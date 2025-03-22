import json

def slugify(name):
    """
    Convert a string to an anchor-friendly slug.
    """
    return name.lower().replace(" ", "-").replace("(", "").replace(")", "")

def extract_repo_path(link):
    """
    Extract the GitHub repository path from the URL.
    Expects links of the form: https://github.com/username/repo
    """
    parts = link.rstrip("/").split("/")
    if len(parts) >= 5:
        return f"{parts[-2]}/{parts[-1]}"
    return ""

def generate_contents(platform="all"):
    # Load categories and applications JSON data.
    with open("source/data/categories.json", "r", encoding="utf-8") as f:
        cat_data = json.load(f)
    with open("source/data/applications.json", "r", encoding="utf-8") as f:
        app_data = json.load(f)
    
    categories = cat_data.get("categories", [])
    subcategories = cat_data.get("subcategories", [])
    applications = app_data.get("applications", [])
    
    # Build a mapping of parent category id to parent category name.
    parent_map = {cat["id"]: cat["Name"] for cat in categories}
    
    # Group subcategories by their parent.
    subcat_by_parent = {}
    for sub in subcategories:
        parent = sub.get("parent", "other")
        subcat_by_parent.setdefault(parent, []).append({
            "Name": sub["Name"],
            "id": sub["id"]
        })
    # Sort subcategories alphabetically in each parent group.
    for key in subcat_by_parent:
        subcat_by_parent[key].sort(key=lambda x: x["Name"].lower())
    
    # Filter and group applications by their subcategory (identified by the app's "category" field).
    apps_by_subcat = {}
    for app in applications:
        include = False
        if platform == "all":
            include = True
        else:
            # Normalize platform tags by stripping backticks and comparing in lower-case.
            app_platforms = [p.strip("`").lower() for p in app.get("platforms", [])]
            target = platform.lower()
            if target in app_platforms:
                include = True
            # For macos, linux, and windows, also include if "cross" is present.
            if target in ["macos", "linux", "windows"] and "cross" in app_platforms:
                include = True
        if not include:
            continue
        
        cat_id = app.get("category", "uncategorized")
        apps_by_subcat.setdefault(cat_id, []).append(app)
    
    # Sort applications within each subcategory alphabetically by name.
    for key in apps_by_subcat:
        apps_by_subcat[key].sort(key=lambda x: x["name"].lower())
    
    # Build Markdown output.
    md_output = ""
    # Process parent categories: sort alphabetically (excluding "other", which is added last).
    parent_items = [(pid, parent_map.get(pid, pid)) for pid in subcat_by_parent if pid != "other"]
    parent_items.sort(key=lambda x: x[1].lower())
    if "other" in subcat_by_parent:
        parent_items.append(("other", "Other"))
    
    for pid, pname in parent_items:
        md_output += f"# {pname} - [Go to top](#contents)\n\n"
        # For each subcategory under the parent category.
        for sub in subcat_by_parent.get(pid, []):
            subname = sub["Name"]
            md_output += f"### {subname}\n\n"
            md_output += "| Name | Description | Platform | Stars |\n"
            md_output += "| --- | --- | --- | --- |\n"
            # List all apps for the given subcategory.
            apps = apps_by_subcat.get(sub["id"], [])
            for app in apps:
                name = app.get("name", "")
                description = app.get("description", "")
                link = app.get("link", "#")
                # Join the platform tags as provided.
                app_platforms = " ".join(app.get("platforms", []))
                repo_path = extract_repo_path(link)
                stars_badge = f"![GitHub Repo stars](https://img.shields.io/github/stars/{repo_path}?style=for-the-badge&label=%20&color=white)" if repo_path else ""
                md_output += f"| [{name}]({link}) | {description} | {app_platforms} | {stars_badge} |\n"
            md_output += "\n"
    return md_output

if __name__ == "__main__":
    # For testing, default to 'all' platforms.
    print(generate_contents("all"))
