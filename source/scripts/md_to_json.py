import json
import re


def parse_readme(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    applications = []
    category = None

    for line in lines:
        line = line.strip()

        # Match category headers
        category_match = re.match(r"^### (.+)", line)
        if category_match:
            category = category_match.group(1).lower().replace(" ", "-")
            continue

        # Match application entries with optional tag
        app_match = re.match(r"\| \[(.+)\]\((https://github.com/[^)]+)\)(?: `([^`]+)`)? \| (.+?) \| (.+?) \|", line)
        if app_match and category:
            name, link, tag, description, platforms = app_match.groups()
            applications.append({
                "name": name,
                "description": description,
                "link": link,
                "tags": [tag] if tag else [],
                "platforms": platforms.split(),
                "category": category
            })

    return applications


def save_to_json(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    readme_path = "README.md"  # Update with actual path
    output_path = "applications.json"

    parsed_data = parse_readme(readme_path)
    save_to_json(parsed_data, output_path)
    print(f"Converted README to {output_path}")
