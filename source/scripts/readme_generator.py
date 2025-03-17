import json
import re


def generate_markdown(applications, categories, subcategories):
    # Organize categories and subcategories
    category_map = {cat["id"]: cat["Name"] for cat in categories}
    subcategory_map = {sub["id"]: (sub["Name"], sub["parent"]) for sub in subcategories}

    # Organize applications into subcategories
    subcategory_apps = {}
    for app in applications:
        subcategory = app.get("category", "")
        if subcategory not in subcategory_apps:
            subcategory_apps[subcategory] = []
        subcategory_apps[subcategory].append(app)

    # Sort subcategories alphabetically
    sorted_subcategories = sorted(subcategory_map.items(), key=lambda x: x[1][0].lower())

    # Sort applications within subcategories
    for subcategory in subcategory_apps:
        subcategory_apps[subcategory] = sorted(subcategory_apps[subcategory], key=lambda x: x["name"].lower())

    # Build markdown
    markdown = "# Contents\n\n"

    # Sort categories alphabetically
    sorted_categories = sorted(category_map.items(), key=lambda x: x[1].lower())

    for cat_id, cat_name in sorted_categories:
        markdown += f"# {cat_name} - [Go to top](#contents)\n\n"

        for sub_id, (sub_name, parent_id) in sorted_subcategories:
            if parent_id == cat_id:
                markdown += f"### {sub_name}\n\n"
                markdown += "| Name | Description | Platform | Stars |\n"
                markdown += "| --- | --- | --- | --- |\n"

                if sub_id in subcategory_apps:
                    for app in subcategory_apps[sub_id]:
                        tags = " ".join([f"`{tag}`" for tag in app.get("tags", [])]) if app.get("tags") else ""
                        platforms = " ".join(app.get("platforms", []))
                        repo_owner, repo_name = app["link"].split("/")[-2:]
                        stars = f"![GitHub Repo stars](https://img.shields.io/github/stars/{repo_owner}/{repo_name}?style=for-the-badge&label=%20&color=white)"
                        markdown += f"| [{app['name']}]({app['link']}) {tags} | {app['description']} | {platforms} | {stars} |\n"

                markdown += "\n"

    return markdown


def save_markdown(content, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == "__main__":
    applications_path = "applications.json"  # Update with actual path
    categories_path = "categories.json"  # Update with actual path
    output_path = "source/testing/test.md"

    try:
        with open(applications_path, 'r', encoding='utf-8') as file:
            applications_data = json.load(file)
            if isinstance(applications_data, list):
                applications_data = {"applications": applications_data}
    except json.JSONDecodeError as e:
        print(f"Error reading {applications_path}: {e}")
        applications_data = {"applications": []}

    try:
        with open(categories_path, 'r', encoding='utf-8') as file:
            categories_data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error reading {categories_path}: {e}")
        categories_data = {"categories": [], "subcategories": []}

    markdown_content = generate_markdown(applications_data.get("applications", []),
                                         categories_data.get("categories", []),
                                         categories_data.get("subcategories", []))
    save_markdown(markdown_content, output_path)
    print(f"Generated {output_path}")