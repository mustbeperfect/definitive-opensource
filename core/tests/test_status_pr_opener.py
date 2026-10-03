from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

CORE_DIR = Path(__file__).resolve().parents[1]
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))

from source.maintenance.status_pr_opener import (  # noqa: E402
    apply_archive_change,
    apply_rebrand_change,
    build_pr_content,
    find_existing_pr,
    get_open_pull_requests,
    get_repo_slug,
    run_status_pr_opener,
    slugify,
)


class TestStatusPROpener(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.temp_dir.name)

        self.sample_apps = {
            "applications": [
                {
                    "name": "Active App",
                    "description": "An active app",
                    "repo_url": "https://github.com/owner/active",
                    "tags": [],
                    "platforms": ["cross"],
                    "category": "agent",
                    "flags": [],
                    "license": "MIT",
                },
                {
                    "name": "Archived App",
                    "description": "An archived app",
                    "repo_url": "https://github.com/owner/archived-repo",
                    "tags": [],
                    "platforms": ["cross"],
                    "category": "agent",
                    "flags": [],
                    "license": "MIT",
                },
                {
                    "name": "Rebranded App",
                    "description": "A rebranded app",
                    "repo_url": "https://github.com/old-org/rebranded",
                    "tags": ["cli"],
                    "platforms": ["macos"],
                    "category": "ide",
                    "flags": ["custom-license"],
                    "license": "Apache-2.0",
                },
            ]
        }

        self.sample_archive = {
            "applications": [
                {
                    "name": "Old Project",
                    "repo_url": "https://github.com/old/project",
                    "reason": "abandoned",
                }
            ]
        }

        self.apps_file = self.temp_path / "applications.json"
        with open(self.apps_file, "w", encoding="utf-8") as f:
            json.dump(self.sample_apps, f, indent=4)

        self.archive_file = self.temp_path / "archive.json"
        with open(self.archive_file, "w", encoding="utf-8") as f:
            json.dump(self.sample_archive, f, indent=2)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_slugify(self):
        self.assertEqual(slugify("Atuin Desktop"), "atuin-desktop")
        self.assertEqual(slugify("Quill Transcription"), "quill-transcription")
        self.assertEqual(slugify("WSL Manager (Moved)"), "wsl-manager-moved")
        self.assertEqual(slugify("  Special   Characters! 123 "), "special-characters-123")

    def test_build_pr_content_archive(self):
        cand = {
            "name": "Atuin Desktop",
            "repo_url": "https://github.com/atuinsh/desktop",
            "reason": "archived",
            "type": "archive",
        }
        branch, title, body = build_pr_content(cand)
        self.assertEqual(branch, "maintenance/archive-atuin-desktop")
        self.assertEqual(title, "chore(archive): move Atuin Desktop to archive")
        # Must contain GitHub link
        self.assertIn("https://github.com/atuinsh/desktop", body)
        self.assertIn("`archived`", body)

    def test_build_pr_content_deleted(self):
        cand = {
            "name": "Dead App",
            "repo_url": "https://github.com/dead/app",
            "reason": "deleted",
            "type": "archive",
        }
        branch, title, body = build_pr_content(cand)
        self.assertEqual(branch, "maintenance/archive-dead-app")
        self.assertEqual(title, "chore(archive): move Dead App to archive (deleted)")
        # Must contain GitHub link
        self.assertIn("https://github.com/dead/app", body)
        self.assertIn("`deleted`", body)

    def test_build_pr_content_rebrand(self):
        cand = {
            "name": "LibreChat",
            "repo_url": "https://github.com/danny-avila/LibreChat",
            "new_repo_url": "https://github.com/LibreChat-AI/LibreChat",
            "current_full_name": "LibreChat-AI/LibreChat",
            "type": "rebrand",
        }
        branch, title, body = build_pr_content(cand)
        self.assertEqual(branch, "maintenance/rebrand-librechat")
        self.assertEqual(title, "chore(url): update LibreChat repository URL")
        # Must contain GitHub link
        self.assertIn("https://github.com/LibreChat-AI/LibreChat", body)
        self.assertIn("https://github.com/danny-avila/LibreChat", body)

    def test_apply_archive_change(self):
        result = apply_archive_change(
            applications_file=self.apps_file,
            archive_file=self.archive_file,
            app_name="Archived App",
            repo_url="https://github.com/owner/archived-repo",
            reason="archived",
        )
        self.assertTrue(result)

        with open(self.apps_file, "r", encoding="utf-8") as f:
            updated_apps = json.load(f)
        names = [a["name"] for a in updated_apps["applications"]]
        self.assertNotIn("Archived App", names)
        self.assertIn("Active App", names)
        self.assertIn("Rebranded App", names)

        with open(self.archive_file, "r", encoding="utf-8") as f:
            updated_archive = json.load(f)
        archive_names = [a["name"] for a in updated_archive["applications"]]
        self.assertIn("Archived App", archive_names)
        archived_entry = next(
            a for a in updated_archive["applications"] if a["name"] == "Archived App"
        )
        self.assertEqual(archived_entry["reason"], "archived")
        self.assertEqual(
            archived_entry["repo_url"], "https://github.com/owner/archived-repo"
        )

        # Applying again should return False (already removed)
        result2 = apply_archive_change(
            applications_file=self.apps_file,
            archive_file=self.archive_file,
            app_name="Archived App",
            repo_url="https://github.com/owner/archived-repo",
            reason="archived",
        )
        self.assertFalse(result2)

    def test_apply_rebrand_change(self):
        result = apply_rebrand_change(
            applications_file=self.apps_file,
            app_name="Rebranded App",
            old_repo_url="https://github.com/old-org/rebranded",
            new_repo_url="https://github.com/new-org/rebranded",
        )
        self.assertTrue(result)

        with open(self.apps_file, "r", encoding="utf-8") as f:
            updated_apps = json.load(f)
        app = next(
            a for a in updated_apps["applications"] if a["name"] == "Rebranded App"
        )
        self.assertEqual(app["repo_url"], "https://github.com/new-org/rebranded")
        # Ensure other fields were not lost
        self.assertEqual(app["license"], "Apache-2.0")
        self.assertEqual(app["flags"], ["custom-license"])
        self.assertEqual(app["platforms"], ["macos"])
        self.assertEqual(app["category"], "ide")

        # Applying again with same new url should return False (no changes needed)
        result2 = apply_rebrand_change(
            applications_file=self.apps_file,
            app_name="Rebranded App",
            old_repo_url="https://github.com/new-org/rebranded",
            new_repo_url="https://github.com/new-org/rebranded",
        )
        self.assertFalse(result2)

    def test_find_existing_pr(self):
        open_prs = [
            {
                "head_ref": "maintenance/archive-atuin-desktop",
                "title": "chore(archive): move Atuin Desktop to archive",
                "number": 12,
                "url": "https://github.com/owner/repo/pull/12",
            }
        ]

        found_by_branch = find_existing_pr(
            "maintenance/archive-atuin-desktop", "Random Title", open_prs
        )
        self.assertIsNotNone(found_by_branch)
        self.assertEqual(found_by_branch["number"], 12)

        found_by_title = find_existing_pr(
            "other-branch", "chore(archive): move Atuin Desktop to archive", open_prs
        )
        self.assertIsNotNone(found_by_title)
        self.assertEqual(found_by_title["number"], 12)

        not_found = find_existing_pr(
            "maintenance/rebrand-librechat", "Different title", open_prs
        )
        self.assertIsNone(not_found)

    @patch("source.maintenance.status_pr_opener.subprocess.run")
    def test_get_open_pull_requests_gh(self, mock_run):
        mock_res = MagicMock()
        mock_res.returncode = 0
        mock_res.stdout = json.dumps(
            [
                {
                    "headRefName": "maintenance/rebrand-librechat",
                    "title": "chore(url): update LibreChat repository URL",
                    "number": 42,
                    "url": "https://github.com/mustbeperfect/definitive-opensource/pull/42",
                }
            ]
        )
        mock_run.return_value = mock_res

        prs = get_open_pull_requests("mustbeperfect/definitive-opensource")
        self.assertEqual(len(prs), 1)
        self.assertEqual(prs[0]["head_ref"], "maintenance/rebrand-librechat")
        self.assertEqual(prs[0]["number"], 42)

    @patch.dict("os.environ", {"GITHUB_REPOSITORY": "testowner/testrepo"})
    def test_get_repo_slug_from_env(self):
        self.assertEqual(get_repo_slug(), "testowner/testrepo")

    def test_run_status_pr_opener_dry_run(self):
        dynamic_file = self.temp_path / "applications_generated.json"
        sample_dynamic = {
            "applications": [
                {
                    "name": "Archived App",
                    "repo_url": "https://github.com/owner/archived-repo",
                    "github_full_name": "owner/archived-repo",
                    "archived": True,
                    "last_commit": "01/01/2023",
                    "stars": 10,
                },
                {
                    "name": "Rebranded App",
                    "repo_url": "https://github.com/old-org/rebranded",
                    "github_full_name": "new-org/rebranded",
                    "archived": False,
                    "last_commit": "09/01/2026",
                    "stars": 50,
                },
            ]
        }
        with open(dynamic_file, "w", encoding="utf-8") as f:
            json.dump(sample_dynamic, f)

        res = run_status_pr_opener(
            dynamic_file=dynamic_file,
            static_dir=self.temp_path,
            dry_run=True,
            max_prs=5,
        )

        self.assertIn("Archived App", res["created"])
        self.assertIn("Rebranded App", res["created"])
        self.assertEqual(len(res["created"]), 2)


if __name__ == "__main__":
    unittest.main()
