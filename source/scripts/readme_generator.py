import json
import os

from tableofcontents_generator import generate_tableofcontents
from contents_generator import generate_markdown

def load_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def generate_readme(platform="all"):
    header_map = {
        "macos": "source/components/macosheader.md",
        "windows": "source/components/windowsheader.md",
        "selfhost": "source/components/selfhostheader.md",
    }
    
    header_file = header_map.get(platform, "source/components/header.md")
    header = load_file(header_file)
    tags = load_file("source/components/tags.md")
    footer = load_file("source/components/footer.md")
    
    toc = generate_tableofcontents()
    content = generate_markdown(platform)
    
    readme_content = "\n".join([header, tags, toc, content, footer])
    
    output_file = f"readmes/{platform}.md" if platform != "all" else "source/testing/test.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"Generated {output_file}")

if __name__ == "__main__":
    for platform in ["all", "windows", "macos", "linux", "selfhost"]:
        generate_readme(platform)
