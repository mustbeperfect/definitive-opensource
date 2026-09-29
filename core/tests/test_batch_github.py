from __future__ import annotations

import json
from pathlib import Path
import sys
import unittest
from unittest.mock import MagicMock, patch

# Ensure core is on sys.path
CORE_DIR = Path(__file__).resolve().parents[1]
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))

from source.maintenance.backlog_updator import generate_backlog  # noqa: E402
from source.maintenance.stats_updator import (  # noqa: E402
    update_all_applications,
    update_application_data,
)
from source.utils.github_utils import (  # noqa: E402
    build_graphql_repos_query,
    extract_repo_path,
    fetch_repos_batch,
    fetch_repos_batch_graphql,
    fetch_repos_batch_rest,
    normalize_graphql_repo,
)


class TestBatchGitHubUtils(unittest.TestCase):
    def test_extract_repo_path(self):
        self.assertEqual(
            extract_repo_path("https://github.com/openinterpreter/openinterpreter"),
            "openinterpreter/openinterpreter",
        )
        self.assertEqual(
            extract_repo_path("https://github.com/screenpipe/screenpipe.git"),
            "screenpipe/screenpipe",
        )
        self.assertEqual(
            extract_repo_path("https://github.com/owner/repo/"),
            "owner/repo",
        )
        self.assertIsNone(extract_repo_path("https://gitlab.com/owner/repo"))
        self.assertIsNone(extract_repo_path(""))

    def test_build_graphql_repos_query(self):
        pairs = [("owner1", "repo1"), ("owner2", 'repo"with"quote')]
        query = build_graphql_repos_query(pairs)
        self.assertIn('repo_0: repository(owner: "owner1", name: "repo1")', query)
        self.assertIn(
            'repo_1: repository(owner: "owner2", name: "repo\\"with\\"quote")', query
        )
        self.assertIn("stargazerCount", query)
        self.assertIn("primaryLanguage", query)
        self.assertIn("licenseInfo", query)

    def test_normalize_graphql_repo(self):
        raw_node = {
            "nameWithOwner": "foo/bar",
            "stargazerCount": 1234,
            "description": "A cool repo",
            "homepageUrl": "https://foo.bar",
            "pushedAt": "2026-09-27T10:00:00Z",
            "isArchived": False,
            "primaryLanguage": {"name": "Rust"},
            "licenseInfo": {"spdxId": "MIT"},
        }
        normalized = normalize_graphql_repo(raw_node)
        self.assertEqual(normalized["stargazers_count"], 1234)
        self.assertEqual(normalized["language"], "Rust")
        self.assertEqual(normalized["homepage"], "https://foo.bar")
        self.assertEqual(normalized["description"], "A cool repo")
        self.assertEqual(normalized["license"], {"spdx_id": "MIT"})
        self.assertEqual(normalized["pushed_at"], "2026-09-27T10:00:00Z")
        self.assertFalse(normalized["archived"])
        self.assertEqual(normalized["full_name"], "foo/bar")

    def test_normalize_graphql_repo_null_license_and_language(self):
        raw_node = {
            "nameWithOwner": "foo/bar",
            "stargazerCount": 0,
            "description": None,
            "homepageUrl": None,
            "pushedAt": None,
            "isArchived": True,
            "primaryLanguage": None,
            "licenseInfo": None,
        }
        normalized = normalize_graphql_repo(raw_node)
        self.assertEqual(normalized["stargazers_count"], 0)
        self.assertIsNone(normalized["language"])
        self.assertEqual(normalized["homepage"], "")
        self.assertEqual(normalized["description"], "")
        self.assertIsNone(normalized["license"])
        self.assertTrue(normalized["archived"])

    @patch("source.utils.github_utils.requests.post")
    def test_fetch_repos_batch_graphql_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": {
                "repo_0": {
                    "nameWithOwner": "owner1/repo1",
                    "stargazerCount": 100,
                    "description": "Desc 1",
                    "homepageUrl": "https://example.com",
                    "pushedAt": "2026-09-01T00:00:00Z",
                    "isArchived": False,
                    "primaryLanguage": {"name": "Python"},
                    "licenseInfo": {"spdxId": "Apache-2.0"},
                },
                "repo_1": None,  # Not found
            }
        }
        mock_post.return_value = mock_response

        results = fetch_repos_batch_graphql(
            ["owner1/repo1", "owner2/notfound"],
            token="fake-token",
            batch_size=10,
        )

        self.assertEqual(len(results), 2)
        self.assertEqual(results["owner1/repo1"]["stargazers_count"], 100)
        self.assertEqual(results["owner1/repo1"]["language"], "Python")
        self.assertIsNone(results["owner2/notfound"])

    @patch("source.utils.github_utils.fetch_repo_data")
    def test_fetch_repos_batch_rest(self, mock_fetch_repo_data):
        mock_fetch_repo_data.side_effect = lambda path, **kwargs: {
            "stargazers_count": 50,
            "language": "Go",
            "full_name": path,
        }

        results = fetch_repos_batch_rest(["owner/repoA", "owner/repoB"], max_workers=2)
        self.assertEqual(len(results), 2)
        self.assertEqual(results["owner/repoA"]["stargazers_count"], 50)
        self.assertEqual(results["owner/repoB"]["language"], "Go")

    @patch("source.utils.github_utils.fetch_repos_batch_graphql")
    @patch("source.utils.github_utils.fetch_repos_batch_rest")
    def test_fetch_repos_batch_with_token_and_partial_fallback(
        self, mock_rest, mock_graphql
    ):
        mock_graphql.return_value = {
            "owner/good": {"stargazers_count": 200},
            "owner/renamed": None,
        }
        mock_rest.return_value = {
            "owner/renamed": {"stargazers_count": 300, "full_name": "owner/newname"},
        }

        results = fetch_repos_batch(
            ["owner/good", "owner/renamed"],
            token="token123",
        )

        mock_graphql.assert_called_once()
        mock_rest.assert_called_once_with(
            ["owner/renamed"],
            headers=mock_rest.call_args[1]["headers"],
            max_workers=8,
            timeout=30,
        )
        self.assertEqual(results["owner/good"]["stargazers_count"], 200)
        self.assertEqual(results["owner/renamed"]["stargazers_count"], 300)

    @patch("source.utils.github_utils.fetch_repos_batch_rest")
    @patch("source.utils.github_utils.get_github_token", return_value=None)
    def test_fetch_repos_batch_without_token_falls_back_to_rest(
        self, mock_token, mock_rest
    ):
        mock_rest.return_value = {"owner/repo": {"stargazers_count": 10}}
        results = fetch_repos_batch(["owner/repo"], token=None)
        mock_rest.assert_called_once()
        self.assertEqual(results["owner/repo"]["stargazers_count"], 10)


class TestStatsUpdator(unittest.TestCase):
    def test_update_application_data_with_batch_result(self):
        app = {
            "name": "Test App",
            "repo_url": "https://github.com/foo/bar",
            "category": "ai",
            "flags": [],
        }
        repo_data = {
            "stargazers_count": 4200,
            "language": "TypeScript",
            "homepage": "https://testapp.dev",
            "description": "Batch updated description",
            "license": {"spdx_id": "MIT"},
            "pushed_at": "2026-09-28T12:00:00Z",
        }

        updated = update_application_data(app.copy(), repo_data=repo_data)
        self.assertEqual(updated["stars"], 4200)
        self.assertEqual(updated["language"], "TypeScript")
        self.assertEqual(updated["homepage_url"], "https://testapp.dev")
        self.assertEqual(updated["description"], "Batch updated description")
        self.assertEqual(updated["license"], "MIT")
        self.assertEqual(updated["last_commit"], "09/28/2026")

    def test_update_application_data_respects_custom_flags(self):
        app = {
            "name": "Custom App",
            "repo_url": "https://github.com/foo/bar",
            "category": "ai",
            "flags": ["custom-homepage", "custom-description", "custom-license"],
            "homepage_url": "https://custom.org",
            "description": "Custom curated description",
            "license": "Custom Commercial",
        }
        repo_data = {
            "stargazers_count": 999,
            "language": "Python",
            "homepage": "https://overwritten.org",
            "description": "Overwritten description",
            "license": {"spdx_id": "GPL-3.0"},
            "pushed_at": "2026-09-28T12:00:00Z",
        }

        updated = update_application_data(app.copy(), repo_data=repo_data)
        self.assertEqual(updated["stars"], 999)
        self.assertEqual(updated["language"], "Python")
        self.assertEqual(updated["homepage_url"], "https://custom.org")
        self.assertEqual(updated["description"], "Custom curated description")
        self.assertEqual(updated["license"], "Custom Commercial")

    def test_update_application_data_uses_fallback_cache_on_fetch_failure(self):
        app = {
            "name": "Failing App",
            "repo_url": "https://github.com/broken/repo",
            "category": "ai",
            "flags": [],
        }
        fallback_app = {
            "name": "Failing App",
            "repo_url": "https://github.com/broken/repo",
            "stars": 1500,
            "language": "Rust",
            "homepage_url": "https://cached.org",
            "description": "Cached description",
            "license": "MIT",
            "last_commit": "09/20/2026",
        }

        # repo_data is None (fetch failed)
        updated = update_application_data(
            app.copy(),
            repo_data=None,
            fallback_app=fallback_app,
        )
        self.assertEqual(updated["stars"], 1500)
        self.assertEqual(updated["language"], "Rust")
        self.assertEqual(updated["homepage_url"], "https://cached.org")
        self.assertEqual(updated["description"], "Cached description")
        self.assertEqual(updated["license"], "MIT")
        self.assertEqual(updated["last_commit"], "09/20/2026")

    def test_update_application_data_preserves_zero_stars_from_fallback(self):
        app = {
            "name": "Zero Star App",
            "repo_url": "https://github.com/foo/zero",
            "category": "ai",
            "flags": [],
        }
        fallback_app = {
            "name": "Zero Star App",
            "repo_url": "https://github.com/foo/zero",
            "stars": 0,
            "language": "Python",
            "homepage_url": "",
            "description": "Zero stars repo",
            "license": "MIT",
            "last_commit": "09/01/2026",
        }

        updated = update_application_data(
            app.copy(),
            repo_data=None,
            fallback_app=fallback_app,
        )
        self.assertIn("stars", updated)
        self.assertEqual(updated["stars"], 0)
        self.assertEqual(updated["language"], "Python")
        self.assertEqual(updated["description"], "Zero stars repo")
        self.assertEqual(updated["license"], "MIT")
        self.assertEqual(updated["last_commit"], "09/01/2026")

    def test_update_application_data_populates_safe_defaults_when_no_fallback(self):
        app = {
            "name": "Brand New App",
            "repo_url": "https://github.com/new/app",
            "category": "ai",
            "flags": [],
        }

        # Both repo_data and fallback_app are None
        updated = update_application_data(
            app.copy(),
            repo_data=None,
            fallback_app=None,
        )
        self.assertEqual(updated["stars"], 0)
        self.assertEqual(updated["language"], "")
        self.assertEqual(updated["homepage_url"], "")
        self.assertEqual(updated["description"], "")
        self.assertEqual(updated["license"], "")
        self.assertEqual(updated["last_commit"], "")

    def test_update_application_data_preserves_custom_flags_on_fetch_failure(self):
        app = {
            "name": "Custom Flags App",
            "repo_url": "https://github.com/foo/flags",
            "category": "ai",
            "flags": ["custom-description", "custom-license", "custom-homepage"],
            "description": "Curated description",
            "license": "Proprietary",
            "homepage_url": "https://custom.site",
        }
        fallback_app = {
            "name": "Custom Flags App",
            "repo_url": "https://github.com/foo/flags",
            "stars": 42,
            "language": "Go",
            "description": "Old stale description",
            "license": "Old License",
            "homepage_url": "https://old.site",
            "last_commit": "08/15/2026",
        }

        updated = update_application_data(
            app.copy(),
            repo_data=None,
            fallback_app=fallback_app,
        )
        self.assertEqual(updated["description"], "Curated description")
        self.assertEqual(updated["license"], "Proprietary")
        self.assertEqual(updated["homepage_url"], "https://custom.site")
        self.assertEqual(updated["stars"], 42)
        self.assertEqual(updated["language"], "Go")
        self.assertEqual(updated["last_commit"], "08/15/2026")

    @patch("source.maintenance.stats_updator.fetch_repos_batch")
    def test_update_all_applications_flow(self, mock_batch):
        mock_batch.return_value = {
            "foo/bar": {
                "stargazers_count": 888,
                "language": "C++",
                "homepage": "https://foo.bar",
                "description": "Great C++ repo",
                "license": {"spdx_id": "Apache-2.0"},
                "pushed_at": "2026-09-25T00:00:00Z",
            }
        }

        test_input = CORE_DIR / "tests" / "test_input.json"
        test_output = CORE_DIR / "tests" / "test_output.json"

        input_data = {
            "applications": [
                {
                    "name": "FooBar",
                    "repo_url": "https://github.com/foo/bar",
                    "category": "tools",
                    "flags": [],
                }
            ]
        }
        with open(test_input, "w", encoding="utf-8") as f:
            json.dump(input_data, f)

        try:
            result = update_all_applications(
                input_file=test_input,
                output_file=test_output,
                batch_size=50,
            )
            mock_batch.assert_called_once_with(
                ["foo/bar"],
                token=mock_batch.call_args[1]["token"],
                headers=mock_batch.call_args[1]["headers"],
                batch_size=50,
            )
            self.assertEqual(len(result["applications"]), 1)
            app = result["applications"][0]
            self.assertEqual(app["stars"], 888)
            self.assertEqual(app["language"], "C++")
            self.assertEqual(app["license"], "Apache-2.0")

            # Check that file was written
            self.assertTrue(test_output.exists())
            with open(test_output, "r", encoding="utf-8") as f:
                saved = json.load(f)
            self.assertEqual(saved["applications"][0]["stars"], 888)
        finally:
            if test_input.exists():
                test_input.unlink()
            if test_output.exists():
                test_output.unlink()

    @patch("source.maintenance.stats_updator.fetch_repos_batch")
    def test_update_all_applications_preserves_fallback_cache_on_batch_failure(
        self, mock_batch
    ):
        # Simulate complete batch fetch failure (e.g. rate limit)
        mock_batch.return_value = {"foo/bar": None}

        test_input = CORE_DIR / "tests" / "test_input_failure.json"
        test_output = CORE_DIR / "tests" / "test_output_failure.json"

        input_data = {
            "applications": [
                {
                    "name": "FooBar",
                    "repo_url": "https://github.com/foo/bar/",  # Note trailing slash
                    "category": "tools",
                    "flags": [],
                }
            ]
        }
        existing_data = {
            "applications": [
                {
                    "name": "FooBar",
                    "repo_url": "https://github.com/foo/bar",
                    "stars": 9999,
                    "language": "Rust",
                    "homepage_url": "https://foobar.rs",
                    "description": "Previously cached description",
                    "license": "MIT",
                    "last_commit": "09/10/2026",
                }
            ]
        }
        with open(test_input, "w", encoding="utf-8") as f:
            json.dump(input_data, f)
        with open(test_output, "w", encoding="utf-8") as f:
            json.dump(existing_data, f)

        try:
            result = update_all_applications(
                input_file=test_input,
                output_file=test_output,
                batch_size=50,
            )
            self.assertEqual(len(result["applications"]), 1)
            app = result["applications"][0]
            # Verify cached metadata was preserved and not stripped
            self.assertEqual(app["stars"], 9999)
            self.assertEqual(app["language"], "Rust")
            self.assertEqual(app["homepage_url"], "https://foobar.rs")
            self.assertEqual(app["description"], "Previously cached description")
            self.assertEqual(app["license"], "MIT")
            self.assertEqual(app["last_commit"], "09/10/2026")
        finally:
            if test_input.exists():
                test_input.unlink()
            if test_output.exists():
                test_output.unlink()


class TestBacklogUpdator(unittest.TestCase):
    @patch("source.maintenance.backlog_updator.fetch_repos_batch")
    def test_generate_backlog_preserves_fallback_cache_on_failure(self, mock_batch):
        mock_batch.return_value = {"old/project": None}

        test_input = CORE_DIR / "tests" / "test_backlog_input.json"
        test_output = CORE_DIR / "tests" / "test_backlog_output.json"

        input_data = {
            "applications": [
                {
                    "name": "Old Project",
                    "repo_url": "https://github.com/old/project/",
                    "note": "Potentially abandoned",
                }
            ]
        }
        existing_data = {
            "applications": [
                {
                    "name": "Old Project",
                    "repo_url": "https://github.com/old/project",
                    "note": "Potentially abandoned",
                    "last_commit": "05/10/2025",
                    "stars": 321,
                }
            ]
        }
        with open(test_input, "w", encoding="utf-8") as f:
            json.dump(input_data, f)
        with open(test_output, "w", encoding="utf-8") as f:
            json.dump(existing_data, f)

        try:
            result = generate_backlog(
                input_file=test_input,
                output_file=test_output,
            )
            self.assertEqual(len(result["applications"]), 1)
            app = result["applications"][0]
            self.assertEqual(app["name"], "Old Project")
            self.assertEqual(app["stars"], 321)
            self.assertEqual(app["last_commit"], "05/10/2025")
        finally:
            if test_input.exists():
                test_input.unlink()
            if test_output.exists():
                test_output.unlink()


if __name__ == "__main__":
    unittest.main()
