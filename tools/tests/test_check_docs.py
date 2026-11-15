"""Behavioural tests for the T.O.O.N. documentation checker."""

import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from check_docs import anchors, check, documents  # noqa: E402


class DocumentationLinksTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "docs").mkdir()

    def write(self, name, data):
        target = self.root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(data, encoding="utf-8")
        return target

    def test_valid_relative_links_headings_and_unicode(self):
        self.write("README.md", "# Hello world\n\n[Read](docs/README.md#ação-e-dados)\n")
        d = self.write("docs/README.md", "# Ação e dados\n\n[Back](../README.md#hello-world)\n")
        self.assertEqual([], check(self.root))
        self.assertIn("ação-e-dados", anchors(d))

    def test_missing_file_and_missing_heading_report_both(self):
        self.write("README.md", "# Home\n[Bad](docs/missing.md)\n[Anchor](docs/README.md#absent)\n")
        self.write("docs/README.md", "# Actual heading\n")
        errors = check(self.root)
        self.assertEqual(2, len(errors))
        self.assertTrue(any("missing target" in e for e in errors))
        self.assertTrue(any("missing heading anchor" in e for e in errors))

    def test_fenced_code_and_external_links_are_ignored(self):
        self.write(
            "README.md",
            "# Home\n[Web](https://example.com/a)\n"
            "```md\n[Example](not-a-file.md)\n```\n",
        )
        self.assertEqual([], check(self.root))

    def test_duplicate_heading_ids_match_github(self):
        d = self.write("docs/a.md", "# Hello\n## Hello\n## Hello\n")
        self.assertEqual({"hello", "hello-1", "hello-2"}, anchors(d))
        self.write("README.md", "[Third](docs/a.md#hello-2)")
        self.assertEqual([], check(self.root))

    def test_cannot_link_outside_repo(self):
        self.write("README.md", "[Escape](../secret.md)")
        errors = check(self.root)
        self.assertEqual(1, len(errors))
        self.assertIn("escapes repository", errors[0])

    def test_does_not_scan_vendor_markdown(self):
        self.write("README.md", "# Home")
        self.write("Assets/Vendor/README.md", "[Bad](not-here.md)")
        self.assertEqual(1, len(documents(self.root)))
        self.assertEqual([], check(self.root))


if __name__ == "__main__":
    unittest.main()
