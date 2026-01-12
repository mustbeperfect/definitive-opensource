from tableofcontents_generator import generate_table_of_contents
from contents_generator import generate_contents
from mainheader_generator import generate_mainheader

# List of target platforms
platforms = ["all", "windows", "macos", "linux", "selfhost"]

# Platforms mapped to corresponding header files
header_files = {
    "all": "core/components/header.md",
    "windows": "core/components/windowsheader.md",
    "macos": "core/components/macosheader.md",
    "linux": "core/components/linuxheader.md",
    "selfhost": "core/components/selfhostheader.md"
}

def generate_readme_for_platform(platform):
    content = ""
    header_file = header_files.get(platform, "core/components/header.md")

    # Inject mainheader with dynamic project count
    if platform == "all":
        content += generate_mainheader()
    
    # Inject header
    with open(header_file, "r", encoding="utf-8") as f:
        content += f.read() + "\n"
    
    # Inject tags.md
    with open("core/components/tags.md", "r", encoding="utf-8") as f:
        content += f.read() + "\n"
    
    # Generate Table of Contents
    toc_md = generate_table_of_contents()
    content += toc_md + "\n"
    
    # Generate the actual markdown list of contents for the given platform
    contents_md = generate_contents(platform)
    content += contents_md + "\n"
    
    # Inject footer.md
    with open("core/components/footer.md", "r", encoding="utf-8") as f:
        content += f.read() + "\n"
    
    # Write output file
    output_filename = "README.md" if platform == "all" else f"resources/readmes/{platform}.md"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {output_filename}")

if __name__ == "__main__":
    for platform in platforms:
        generate_readme_for_platform(platform)
