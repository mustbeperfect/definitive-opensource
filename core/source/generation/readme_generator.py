from contents_generator import generate_contents
from mainheader_generator import generate_mainheader
from tableofcontents_generator import generate_table_of_contents

platforms = ["all", "windows", "macos", "linux", "selfhost"]

# Platforms mapped to corresponding header files
header_files = {
    "all": "components/header.md",
    "windows": "components/windowsheader.md",
    "macos": "components/macosheader.md",
    "linux": "components/linuxheader.md",
    "selfhost": "components/selfhostheader.md",
}


def generate_readme_for_platform(platform):
    content = ""
    header_file = header_files.get(platform, "components/header.md")

    # Inject every component of the list from top to bottom
    if platform == "all":
        content += generate_mainheader()

    with open(header_file, "r", encoding="utf-8") as f:
        content += f.read() + "\n"

    with open("components/tags.md", "r", encoding="utf-8") as f:
        content += f.read() + "\n"

    toc_md = generate_table_of_contents()
    content += toc_md + "\n"

    contents_md = generate_contents(platform)
    content += contents_md + "\n"

    with open("components/footer.md", "r", encoding="utf-8") as f:
        content += f.read() + "\n"

    # Write output file
    output_filename = (
        "README.md" if platform == "all" else f"../resources/readmes/{platform}.md"
    )
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {output_filename}")


if __name__ == "__main__":
    for platform in platforms:
        generate_readme_for_platform(platform)
