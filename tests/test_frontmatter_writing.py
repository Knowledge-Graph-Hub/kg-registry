"""Tests for writing YAML frontmatter back to disk.

python-frontmatter 1.1.0 encoded in `dump` and wrote bytes, so callers opened
files in binary mode. 1.2.0 changed `dump` to write `str`, which raises
``TypeError: a bytes-like object is required, not 'str'`` against a binary
handle -- every write-back path in the repo broke when the lockfile moved to
1.3.0. These tests pin the behaviour the code now relies on.
"""

from pathlib import Path

import frontmatter
import pytest

from util.common import CustomRuamelYAMLHandler, dump_frontmatter_text, save_frontmatter_file

POST_TEXT = "---\nid: demo.product\nname: Demo\n---\n\nBody text.\n"


@pytest.mark.parametrize("use_handler", [False, True])
def test_dump_frontmatter_text_returns_str(use_handler):
    post = frontmatter.loads(POST_TEXT)
    handler = CustomRuamelYAMLHandler() if use_handler else None

    text = dump_frontmatter_text(post, handler)

    assert isinstance(text, str)
    # No trailing newline, matching what frontmatter.dump used to write; callers
    # append one themselves.
    assert not text.endswith("\n")
    assert frontmatter.loads(text).metadata["id"] == "demo.product"


@pytest.mark.parametrize("use_ruamel", [False, True])
def test_save_frontmatter_file_round_trips(tmp_path: Path, use_ruamel: bool):
    target = tmp_path / "demo.md"

    save_frontmatter_file(
        target,
        {"id": "demo.product", "name": "Demo", "tags": ["a", "b"]},
        content="\nBody text.\n",
        use_ruamel=use_ruamel,
    )

    reloaded = frontmatter.load(target)
    assert reloaded.metadata["id"] == "demo.product"
    assert reloaded.metadata["tags"] == ["a", "b"]
    assert "Body text." in reloaded.content
    # Written as text, not bytes: readable without an explicit decode.
    assert target.read_text(encoding="utf-8").startswith("---")


def test_save_frontmatter_file_handles_non_ascii(tmp_path: Path):
    """UTF-8 is explicit, so the write does not depend on the locale encoding."""
    target = tmp_path / "demo.md"

    save_frontmatter_file(target, {"id": "demo.product", "name": "Ontología — José"}, content="")

    assert frontmatter.load(target).metadata["name"] == "Ontología — José"
