import json

def load_data():
    with open("categories.json", "r", encoding="utf-8") as f:
        categories_data = json.load(f)
    with open("applications.json", "r", encoding="utf-8") as f:
        applications_data = json.load(f)
    return categories_data, applications_data

def generate_markdown(platform_filter=None):
    categories_data, applications_data = load_data()
    categories = sorted(categories_data["categories"], key=lambda x: x["Name"].lower())
    subcategories = sorted(categories_data["subcategories"], key=lambda x: x["Name"].lower())
    applications = sorted(applications_data["applications"], key=lambda x: x["name"].lower())
    
    markdown_content = []
    markdown_content.append("## Contents\n")
    
    category_map = {cat["id"]: cat["Name"] for cat in categories}
    subcategory_map = {sub["id"]: sub for sub in subcategories}
    
    categorized_apps = {sub["id"]: [] for sub in subcategories}
    for app in applications:
        if app["category"] in categorized_apps:
            if platform_filter:
                if platform_filter in [p.strip('`').lower() for p in app["platforms"]]:
                    categorized_apps[app["category"]].append(app)
            else:
                categorized_apps[app["category"]].append(app)
    
    for cat in categories:
        cat_id = cat["id"]
        markdown_content.append(f"# {cat['Name']} - [Go to top](#contents)\n")
        for sub in subcategories:
            if sub["parent"] == cat_id and categorized_apps[sub["id"]]:
                markdown_content.append(f"### {sub['Name']}\n")
                markdown_content.append("| Name | Description | Platform | Stars |\n| --- | --- | --- | --- |")
                for app in categorized_apps[sub["id"]]:
                    platforms = " ".join(app["platforms"])
                    stars_badge = f"![GitHub Repo stars](https://img.shields.io/github/stars/{app['link'].split('/')[-2]}/{app['link'].split('/')[-1]}?style=for-the-badge&label=%20&color=white)"
                    tags = " ".join(app["tags"])
                    markdown_content.append(f"| [{app['name']}]({app['link']}) {tags} | {app['description']} | {platforms} | {stars_badge} |")
                markdown_content.append("")
    
    return "\n".join(markdown_content)

if __name__ == "__main__":
    markdown_output = generate_markdown()
    with open("contents.md", "w", encoding="utf-8") as f:
        f.write(markdown_output)
    print("Generated contents.md")