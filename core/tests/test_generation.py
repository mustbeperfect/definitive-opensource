from __future__ import annotations

from pathlib import Path
import re
import sys
import unittest

# Ensure core is on sys.path
CORE_DIR = Path(__file__).resolve().parents[1]
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))

from source.generation.contents_generator import (  # noqa: E402
    app_matches_platform,
    generate_contents,
)
from source.generation.tableofcontents_generator import (  # noqa: E402
    generate_table_of_contents,
)
from source.utils.markdown_utils import slugify  # noqa: E402


class TestGeneration(unittest.TestCase):
    def test_app_matches_platform(self):
        cross_app = {"platforms": ["Cross"]}
        mac_app = {"platforms": ["MacOS"]}
        self_app = {"platforms": ["SelfHost"]}

        self.assertTrue(app_matches_platform(cross_app, "all"))
        self.assertTrue(app_matches_platform(cross_app, "windows"))
        self.assertTrue(app_matches_platform(cross_app, "macos"))
        self.assertTrue(app_matches_platform(cross_app, "linux"))
        self.assertFalse(app_matches_platform(cross_app, "selfhost"))

        self.assertTrue(app_matches_platform(mac_app, "macos"))
        self.assertFalse(app_matches_platform(mac_app, "windows"))
        self.assertFalse(app_matches_platform(mac_app, "selfhost"))

        self.assertTrue(app_matches_platform(self_app, "selfhost"))
        self.assertFalse(app_matches_platform(self_app, "macos"))

    def test_no_empty_tables_or_empty_parents(self):
        platforms = ["all", "windows", "macos", "linux", "selfhost"]
        empty_table_regex = re.compile(
            r"(### [^\n]+)\n\n\| Name \| Description \| Platform\(s\) \| Stars \|\n\| --- \| --- \| --- \| --- \|\n\s*(?=\n|#|\Z)"
        )
        empty_parent_regex = re.compile(
            r"(# [^\n]+ - \[Go to top\]\(#table-of-contents\))\n\n(?=# [^#]|\Z)"
        )

        for platform in platforms:
            contents = generate_contents(platform)
            empty_tables = empty_table_regex.findall(contents)
            empty_parents = empty_parent_regex.findall(contents)

            self.assertEqual(
                empty_tables,
                [],
                f"Found empty tables in platform '{platform}': {empty_tables}",
            )
            self.assertEqual(
                empty_parents,
                [],
                f"Found empty parent categories in platform '{platform}': {empty_parents}",
            )

    def test_table_of_contents_synchronized_with_contents(self):
        platforms = ["all", "windows", "macos", "linux", "selfhost"]

        for platform in platforms:
            toc = generate_table_of_contents(platform)
            contents = generate_contents(platform)

            # Subcategory headings in contents
            subcat_headings = set(re.findall(r"^###\s+([^\n]+)", contents, re.MULTILINE))
            content_slugs = {slugify(name) for name in subcat_headings}

            # TOC subcategory links
            toc_links = re.findall(r"\[([^\]]+)\]\(#([^\)]+)\)", toc)
            # Exclude fixed footer sections
            fixed_slugs = {
                slugify("Removed Projects"),
                slugify("FAQ"),
                slugify("Honorable Mentions of Closed-Source Software"),
            }

            for name, anchor in toc_links:
                if anchor in fixed_slugs:
                    continue
                self.assertIn(
                    anchor,
                    content_slugs,
                    f"Platform '{platform}': TOC link '{name}' (#{anchor}) does not exist in content",
                )

    def test_specific_known_empty_categories_omitted(self):
        # selfhost should omit EMACS Packages, Operating System, etc.
        selfhost_toc = generate_table_of_contents("selfhost")
        selfhost_contents = generate_contents("selfhost")
        self.assertNotIn("EMACS Packages", selfhost_toc)
        self.assertNotIn("EMACS Packages", selfhost_contents)
        self.assertNotIn("# Operating System - [Go to top]", selfhost_contents)
        self.assertNotIn("# Extensions - [Go to top]", selfhost_contents)

        # README.md (all) should omit EMACS Packages
        all_toc = generate_table_of_contents("all")
        all_contents = generate_contents("all")
        self.assertNotIn("EMACS Packages", all_toc)
        self.assertNotIn("### EMACS Packages", all_contents)


if __name__ == "__main__":
    unittest.main()
