from pathlib import Path
import sys

CORE_DIR = Path(__file__).resolve().parents[2]
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))

from source.generation.archive_generator import generate_archive_section  # noqa: E402
from source.generation.contents_generator import generate_contents  # noqa: E402
from source.generation.header_generator import generate_header  # noqa: E402
from source.generation.tableofcontents_generator import (  # noqa: E402
    generate_table_of_contents,
)
from source.utils.path_utils import COMPONENTS_DIR, READMES_DIR, REPO_ROOT  # noqa: E402

platforms = ["all", "windows", "macos", "linux", "selfhost"]


def generate_readme_for_platform(platform):
    content = ""

    # Inject every component of the list from top to bottom
    content += generate_header(platform) + "\n"

    with open(COMPONENTS_DIR / "tags.md", "r", encoding="utf-8") as f:
        content += f.read() + "\n"

    toc_md = generate_table_of_contents(platform)
    content += toc_md + "\n"

    contents_md = generate_contents(platform)
    content += contents_md + "\n"

    archive_md = generate_archive_section()
    content += archive_md + "\n"

    with open(COMPONENTS_DIR / "footer.md", "r", encoding="utf-8") as f:
        content += f.read() + "\n"

    # Write output file
    output_filename = (
        REPO_ROOT / "README.md"
        if platform == "all"
        else READMES_DIR / f"{platform}.md"
    )
    output_filename.parent.mkdir(parents=True, exist_ok=True)
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {output_filename}")


if __name__ == "__main__":
    for platform in platforms:
        generate_readme_for_platform(platform)
