import json
import os

from tableofcontents_generator import generate_tableofcontents
from contents_generator import generate_markdown

def load_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def generate_readme(platform="all"):
    header_map = {
        "cross": "source/lib/crossheader.md",
        "macos": "source/lib/macosheader.md",
        "windows": "source/lib/windowsheader.md",
        "selfhost": "source/lib/selfhostheader.md",
    }
    
    header_file = header_map.get(platform, "source/lib/header.md")
    header = load_file(header_file)
    tags = load_file("source/lib/tags.md")
    footer = load_file("source/lib/footer.md")
    
    toc = generate_tableofcontents()
    content = generate_markdown(platform)
    
    readme_content = "\n".join([header, tags, toc, content, footer])
    
    output_file = f"readmes/{platform}.md" if platform != "all" else "source/testing/test.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"Generated {output_file}")

if __name__ == "__main__":
    for platform in ["all", "cross", "macos", "windows", "selfhost"]:
        generate_readme(platform)
