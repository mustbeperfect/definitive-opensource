import json

with open("data/dynamic/applications.json") as f:
    applications = json.load(f)["applications"]

with open("data/static/categories.json") as f:
    categories_data = json.load(f)["subcategories"]
    valid_categories = {c["id"].lower() for c in categories_data}

with open("data/static/platforms.json") as f:
    platforms_data = json.load(f)["platforms"]
    valid_platforms = {p["id"].lower() for p in platforms_data}

seen_github = set()
issues_report = []

# Check for formatting issues inside of all data files (static and dynamic)
for app in applications:
    app_issues = []

    github_url = app.get("repo_url", "").strip()
    if not github_url:
        app_issues.append("Missing GitHub URL")
    elif github_url in seen_github:
        app_issues.append("Duplicate GitHub URL")
    else:
        seen_github.add(github_url)

    category = app.get("category", "").lower()
    if not category:
        app_issues.append("Missing category")
    elif category not in valid_categories:
        app_issues.append(f"Invalid category '{category}'")

    platforms = [p.lower() for p in app.get("platforms", [])]
    if not platforms:
        app_issues.append("Missing platform")
    else:
        invalid_platforms = [p for p in platforms if p not in valid_platforms]
        if invalid_platforms:
            app_issues.append(f"Invalid platforms: {', '.join(invalid_platforms)}")

    if app_issues:
        issues_report.append(
            {"name": app.get("name", "Unnamed Project"), "issues": app_issues}
        )

with open("../resources/maintenance/format_maintenance.md", "w") as f:
    f.write("# Format Maintenance Report\n\n")
    if not issues_report:
        f.write("No issues found. All applications are properly formatted.\n")
    else:
        for entry in issues_report:
            f.write(f"## {entry['name']}\n")
            for issue in entry["issues"]:
                f.write(f"- {issue}\n")
            f.write("\n")

print("Maintenance report generated: format_maintenance.md")
