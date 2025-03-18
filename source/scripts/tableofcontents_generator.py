import json

def load_categories():
    with open("categories.json", "r", encoding="utf-8") as f:
        return json.load(f)

def generate_table_of_contents():
    data = load_categories()
    categories = sorted(data["categories"], key=lambda x: x["Name"].lower())
    subcategories = sorted(data["subcategories"], key=lambda x: x["Name"].lower())
    
    toc = ["## Contents\n"]
    
    # Alphabetical section
    toc.append("<details>\n  <summary><b>Alphabetical</b></summary> <br />\n")
    for sub in subcategories:
        toc.append(f"  - [{sub['Name']}](#{sub['id']})")
    toc.append("</details>\n")
    
    # Categorized section
    toc.append("<details open>\n  <summary><b>Categorized</b></summary> <br />\n")
    
    category_map = {cat["id"]: cat["Name"] for cat in categories}
    organized_subcategories = {}
    
    for sub in subcategories:
        parent = sub["parent"]
        if parent not in organized_subcategories:
            organized_subcategories[parent] = []
        organized_subcategories[parent].append(sub)
    
    for cat in categories:
        cat_id = cat["id"]
        toc.append(f"  - {cat['Name']}")
        if cat_id in organized_subcategories:
            for sub in organized_subcategories[cat_id]:
                toc.append(f"      - [{sub['Name']}](#{sub['id']})")
    
    # Other category at the end
    if "other" in organized_subcategories:
        toc.append("  - [Other](#other)")
    
    toc.append("</details>\n")
    return "\n".join(toc)

if __name__ == "__main__":
    toc_content = generate_table_of_contents()
    with open("tableofcontents.md", "w", encoding="utf-8") as f:
        f.write(toc_content)
    print("Generated tableofcontents.md")
