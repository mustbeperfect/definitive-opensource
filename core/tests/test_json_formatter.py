from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest

CORE_DIR = Path(__file__).resolve().parents[1]
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))

from source.maintenance.json_formatter import (  # noqa: E402
    VALID_ARCHIVE_REASONS,
    VALID_FLAGS,
    generate_report,
    run_format_checks,
    validate_applications,
    validate_archive,
    validate_backlog,
    validate_categories,
    validate_platforms,
    validate_tags,
)


class TestJsonFormatter(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_validate_categories_duplicates_and_parents(self):
        cat_file = self.temp_path / "categories.json"
        cat_file.write_text(
            json.dumps(
                {
                    "categories": [
                        {"name": "Dev", "id": "dev"},
                        {"name": "Dev Dup", "id": "dev"},
                    ],
                    "subcategories": [
                        {"name": "Editor", "id": "editor", "parent": "dev"},
                        {"name": "Editor Dup", "id": "editor", "parent": "dev"},
                        {"name": "Conflict", "id": "dev", "parent": "dev"},
                        {"name": "Invalid Parent", "id": "term", "parent": "nonexistent"},
                    ],
                }
            ),
            encoding="utf-8",
        )

        issues, valid_subcats, valid_cats = validate_categories(cat_file)
        issues_flat = [issue for entry in issues for issue in entry["issues"]]

        self.assertIn("Duplicate category ID 'dev'", issues_flat)
        self.assertIn("Duplicate subcategory ID 'editor'", issues_flat)
        self.assertIn("Subcategory ID 'dev' conflicts with category ID", issues_flat)
        self.assertIn("Invalid parent category 'nonexistent'", issues_flat)
        self.assertIn("editor", valid_subcats)
        self.assertIn("dev", valid_cats)

    def test_validate_platforms(self):
        plat_file = self.temp_path / "platforms.json"
        plat_file.write_text(
            json.dumps(
                {
                    "platforms": [
                        {"name": "Cross", "id": "cross"},
                        {"name": "Cross Dup", "id": "cross"},
                    ]
                }
            ),
            encoding="utf-8",
        )

        issues, valid_platforms = validate_platforms(plat_file)
        issues_flat = [issue for entry in issues for issue in entry["issues"]]

        self.assertIn("Duplicate platform ID 'cross'", issues_flat)
        self.assertEqual(valid_platforms, {"cross"})

    def test_validate_tags(self):
        tag_file = self.temp_path / "tags.json"
        tag_file.write_text(
            json.dumps(
                {
                    "attributes": [
                        {"id": "ai", "description": "AI Usage"},
                        {"id": "ai", "description": "Duplicate AI"},
                    ],
                    "properties": [
                        {"id": "cli", "name": "CLI"},
                    ],
                }
            ),
            encoding="utf-8",
        )

        issues, valid_tags = validate_tags(tag_file)
        issues_flat = [issue for entry in issues for issue in entry["issues"]]

        self.assertIn("Duplicate tag ID 'ai'", issues_flat)
        self.assertEqual(valid_tags, {"ai", "cli"})

    def test_validate_flags_and_tags_in_applications(self):
        app_file = self.temp_path / "applications.json"
        app_file.write_text(
            json.dumps(
                {
                    "applications": [
                        {
                            "name": "App 1",
                            "repo_url": "https://github.com/org/app1",
                            "category": "editor",
                            "platforms": ["cross"],
                            "tags": ["ai", "unknown-tag"],
                            "flags": ["custom-homepage", "invalid-flag"],
                        },
                        {
                            "name": "App 1",  # duplicate name
                            "repo_url": "https://github.com/org/app2",
                            "category": "editor",
                            "platforms": ["cross"],
                            "tags": ["cli"],
                            "flags": ["custom-license"],
                        },
                        {
                            "name": "App 3",
                            "repo_url": "https://github.com/org/app1",  # duplicate repo_url
                            "category": "invalid-cat",
                            "platforms": ["invalid-plat"],
                            "tags": [],
                            "flags": [],
                        },
                    ]
                }
            ),
            encoding="utf-8",
        )

        issues, seen_urls, seen_names = validate_applications(
            applications_path=app_file,
            valid_categories={"editor"},
            valid_platforms={"cross"},
            valid_tags={"ai", "cli"},
            valid_flags=VALID_FLAGS,
        )

        first_app_issues = issues[0]["issues"]
        second_app_issues = issues[1]["issues"]
        third_app_issues = issues[2]["issues"]

        self.assertEqual(issues[0]["name"], "App 1")
        self.assertIn("Invalid tags: unknown-tag", first_app_issues)
        self.assertIn("Invalid flags: invalid-flag", first_app_issues)

        # Second App 1 has duplicate name
        self.assertEqual(issues[1]["name"], "App 1")
        self.assertIn("Duplicate application name", second_app_issues)

        # App 3 has duplicate url, invalid category, invalid platform
        self.assertEqual(issues[2]["name"], "App 3")
        self.assertIn("Duplicate GitHub URL", third_app_issues)
        self.assertIn("Invalid category 'invalid-cat'", third_app_issues)
        self.assertIn("Invalid platforms: invalid-plat", third_app_issues)

    def test_validate_backlog(self):
        backlog_file = self.temp_path / "backlog.json"
        backlog_file.write_text(
            json.dumps(
                {
                    "applications": [
                        {"name": "Backlog 1", "repo_url": "https://github.com/org/b1"},
                        {"name": "Backlog 1", "repo_url": "https://github.com/org/b2"},
                        {"name": "Backlog 2", "repo_url": "https://github.com/org/b1"},
                    ]
                }
            ),
            encoding="utf-8",
        )

        issues = validate_backlog(backlog_file)
        issues_flat = [issue for entry in issues for issue in entry["issues"]]

        self.assertIn("Duplicate application name", issues_flat)
        self.assertIn("Duplicate GitHub URL", issues_flat)

    def test_validate_archive(self):
        archive_file = self.temp_path / "archive.json"
        archive_file.write_text(
            json.dumps(
                {
                    "applications": [
                        {
                            "name": "Archive 1",
                            "repo_url": "https://github.com/org/a1",
                            "reason": "abandoned",
                        },
                        {
                            "name": "Archive 1",
                            "repo_url": "https://github.com/org/a2",
                            "reason": "invalid-reason",
                        },
                        {
                            "name": "Active in Apps",
                            "repo_url": "https://github.com/org/active",
                            "reason": "closed-source",
                        },
                    ]
                }
            ),
            encoding="utf-8",
        )

        issues = validate_archive(
            archive_path=archive_file,
            valid_reasons=VALID_ARCHIVE_REASONS,
            active_app_urls={"https://github.com/org/active"},
        )
        issues_flat = [issue for entry in issues for issue in entry["issues"]]

        self.assertIn("Duplicate application name", issues_flat)
        self.assertIn("Invalid archive reason 'invalid-reason'", issues_flat)
        self.assertIn(
            "Archived project still present in applications.json", issues_flat
        )

    def test_generate_report_clean_and_with_issues(self):
        report_file = self.temp_path / "report.md"

        # Clean report
        total = generate_report(report_file, {"applications.json": []})
        self.assertEqual(total, 0)
        content = report_file.read_text(encoding="utf-8")
        self.assertIn("No issues found. All data files are properly formatted.", content)

        # Report with issues
        total = generate_report(
            report_file,
            {
                "applications.json": [
                    {"name": "App 1", "issues": ["Duplicate application name"]}
                ]
            },
        )
        self.assertEqual(total, 1)
        content = report_file.read_text(encoding="utf-8")
        self.assertIn("## applications.json", content)
        self.assertIn("### App 1", content)
        self.assertIn("- Duplicate application name", content)

    def test_run_format_checks_integration(self):
        static_dir = self.temp_path / "static"
        dynamic_dir = self.temp_path / "dynamic"
        static_dir.mkdir()
        dynamic_dir.mkdir()

        (static_dir / "categories.json").write_text(
            json.dumps({"categories": [{"id": "c1", "name": "C1"}], "subcategories": [{"id": "s1", "name": "S1", "parent": "c1"}]}),
            encoding="utf-8",
        )
        (static_dir / "platforms.json").write_text(
            json.dumps({"platforms": [{"id": "p1", "name": "P1"}]}),
            encoding="utf-8",
        )
        (static_dir / "tags.json").write_text(
            json.dumps({"attributes": [{"id": "t1"}], "properties": []}),
            encoding="utf-8",
        )
        (static_dir / "applications.json").write_text(
            json.dumps({
                "applications": [
                    {
                        "name": "App Clean",
                        "repo_url": "https://github.com/org/clean",
                        "category": "s1",
                        "platforms": ["p1"],
                        "tags": ["t1"],
                        "flags": ["custom-description"],
                    }
                ]
            }),
            encoding="utf-8",
        )
        (static_dir / "backlog.json").write_text(
            json.dumps({"applications": []}),
            encoding="utf-8",
        )
        (dynamic_dir / "archive.json").write_text(
            json.dumps({"applications": []}),
            encoding="utf-8",
        )

        report_file = self.temp_path / "format_maintenance.md"
        report_data, total_issues, out_path = run_format_checks(
            static_data_dir=static_dir,
            dynamic_data_dir=dynamic_dir,
            report_output_file=report_file,
        )

        self.assertEqual(total_issues, 0)
        self.assertEqual(out_path, report_file)
        self.assertIn("No issues found", report_file.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
