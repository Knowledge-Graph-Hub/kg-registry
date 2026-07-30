"""Tests for the generated-artifact sync check.

These exercise the checker against synthetic trees rather than the real
repository. The repo's own committed summary is expected to be stale between
registry updates -- it is the update-registry workflow, not CI, that regenerates
it -- so asserting on the real files here would fail every resource-addition PR.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import yaml

from util.check_generated_artifacts import REQUIRED_ARTIFACTS, check


def _write_tree(root: Path, registry_ids, summary_ids, omit=()):
    """Lay out a minimal repo with the given resource ids in each artifact."""
    for artifact in REQUIRED_ARTIFACTS:
        if artifact in omit:
            continue
        path = root / artifact
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("placeholder\n")

    if Path("registry/kgs.yml") not in omit:
        (root / "registry/kgs.yml").write_text(
            yaml.safe_dump({"resources": [{"id": i, "name": i} for i in registry_ids]})
        )
    if Path("registry/kgs-summary.json") not in omit:
        (root / "registry/kgs-summary.json").write_text(
            json.dumps({"resources": [{"id": i, "name": i} for i in summary_ids]})
        )


class TestCheckGeneratedArtifacts(unittest.TestCase):
    def test_in_sync_tree_has_no_problems(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_tree(root, ["kg-a", "kg-b"], ["kg-a", "kg-b"])
            self.assertEqual(check(root), [])

    def test_resource_missing_from_summary_is_reported(self):
        """The exact failure that froze the resource browser."""
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_tree(root, ["kg-a", "imo-knowledge-graph"], ["kg-a"])
            problems = check(root)
            self.assertTrue(problems)
            joined = "\n".join(problems)
            self.assertIn("out of sync", joined)
            self.assertIn("imo-knowledge-graph", joined)

    def test_extra_resource_in_summary_is_reported(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_tree(root, ["kg-a"], ["kg-a", "kg-removed"])
            joined = "\n".join(check(root))
            self.assertIn("kg-removed", joined)

    def test_missing_artifact_is_reported(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            omit = [Path("registry/kgs.ttl")]
            _write_tree(root, ["kg-a"], ["kg-a"], omit=omit)
            joined = "\n".join(check(root))
            self.assertIn("registry/kgs.ttl is missing", joined)

    def test_missing_registry_yaml_stops_before_comparison(self):
        """No spurious sync error when there is nothing to compare against."""
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            omit = [Path("registry/kgs.yml")]
            _write_tree(root, [], ["kg-a"], omit=omit)
            problems = check(root)
            self.assertEqual(len(problems), 1)
            self.assertIn("registry/kgs.yml is missing", problems[0])

    def test_empty_registry_is_reported(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_tree(root, [], [])
            joined = "\n".join(check(root))
            self.assertIn("never be empty", joined)

    def test_long_id_lists_are_truncated(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            ids = [f"kg-{n:03d}" for n in range(30)]
            _write_tree(root, ids, [])
            joined = "\n".join(check(root))
            self.assertIn("...and 10 more", joined)


if __name__ == "__main__":
    unittest.main()
