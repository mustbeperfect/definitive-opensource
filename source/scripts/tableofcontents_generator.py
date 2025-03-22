import json

def slugify(name):
    #Create an anchor-friendly slug from a string.
    return name.lower().replace(" ", "-").replace("(", "").replace(")", "")

def generate_table_of_contents():
    # Load the categories JSON data
    with open("source/data/categories.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    categories = data.get("categories", [])
    subcategories = data.get("subcategories", [])
    
    # Build the alphabetical list (ignoring parent categories)
    subcat_names = [sub["Name"] for sub in subcategories]
    subcat_names.sort(key=lambda x: x.lower())
    alphabetical_md = ""
    for name in subcat_names:
        alphabetical_md += f"- [{name}](#{slugify(name)})\n"
    
    # Build the categorized list.
    # Create a mapping from parent id to parent name.
    parent_map = {cat["id"]: cat["Name"] for cat in categories}
    # Group subcategories by their parent id.
    grouped = {}
    for sub in subcategories:
        parent = sub.get("parent", "other")
        grouped.setdefault(parent, []).append(sub["Name"])
    # Sort each group's subcategories alphabetically.
    for key in grouped:
        grouped[key].sort(key=lambda x: x.lower())
    # Sort parent categories (exclude "other", which is appended at the end)
    parents = [(pid, parent_map.get(pid, "Other")) for pid in grouped if pid != "other"]
    parents.sort(key=lambda x: x[1].lower())
    if "other" in grouped:
        parents.append(("other", "Other"))
    
    categorized_md_lines = []
    for pid, pname in parents:
        categorized_md_lines.append(f"- {pname}")
        for subname in grouped[pid]:
            categorized_md_lines.append(f"    - [{subname}](#{slugify(subname)})")
    
    # Append fixed sections at the end of the categorized TOC.
    fixed_sections = ["Removed Projects", "FAQ", "Honorable Mentions of Closed-Source Software"]
    for item in fixed_sections:
        categorized_md_lines.append(f"- [{item}](#{slugify(item)})")
    
    categorized_md = "\n".join(categorized_md_lines)
    
    toc = f"""## Table of Contents

<details>
  <summary><b>Alphabetical</b></summary> <br />
{alphabetical_md}
</details>

<details open>
  <summary><b>Categorized</b></summary> <br />
{categorized_md}
</details>
"""
    return toc

if __name__ == "__main__":
    # For testing the TOC generator
    print(generate_table_of_contents())
