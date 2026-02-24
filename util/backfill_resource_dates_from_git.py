#!/usr/bin/env python3

"""
Backfill missing resource date fields from git history.

This script updates only root Resource pages at:
  resource/<resource_id>/<resource_id>.md

It fills missing `creation_date` and/or `last_modified_date` by using:
  - earliest commit date for `creation_date`
  - latest commit date for `last_modified_date`

Dates are normalized to `YYYY-MM-DDT00:00:00Z`.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import yaml


ROOT = Path(__file__).resolve().parent.parent
RESOURCE_DIR = ROOT / "resource"


@dataclass
class UpdateResult:
    path: Path
    added_creation: bool = False
    added_modified: bool = False
    skipped_missing_git_history: bool = False
    skipped_parse_error: bool = False


def iter_root_resource_files() -> Iterable[Path]:
    """Yield root resource pages in `resource/<id>/<id>.md` format."""
    for path in sorted(RESOURCE_DIR.glob("*/*.md")):
        if path.stem == path.parent.name:
            yield path


def _to_normalized_date(iso_dt: str) -> str | None:
    iso_dt = iso_dt.strip()
    if len(iso_dt) < 10:
        return None
    date_part = iso_dt[:10]
    if date_part.count("-") != 2:
        return None
    return f"{date_part}T00:00:00Z"


def git_commit_date(path: Path, earliest: bool) -> str | None:
    """Get earliest/latest commit date for a file as `YYYY-MM-DDT00:00:00Z`."""
    rel_path = path.relative_to(ROOT).as_posix()
    cmd = ["git", "log", "--follow", "--format=%cI", "--", rel_path]
    if earliest:
        cmd.insert(4, "--reverse")

    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        return None
    lines = [line.strip() for line in proc.stdout.splitlines() if line.strip()]
    if not lines:
        return None
    raw = lines[0]
    return _to_normalized_date(raw)


def _load_source_text(path: Path, source: str) -> str | None:
    if source == "worktree":
        return path.read_text(encoding="utf-8")

    rel_path = path.relative_to(ROOT).as_posix()
    proc = subprocess.run(
        ["git", "show", f"HEAD:{rel_path}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        return None
    return proc.stdout


def _split_frontmatter(text: str) -> tuple[list[str], int] | tuple[None, None]:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None, None

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return None, None
    return lines, end_idx


def _parse_metadata(lines: list[str], end_idx: int) -> dict | None:
    fm_text = "".join(lines[1:end_idx])
    try:
        obj = yaml.safe_load(fm_text)
    except yaml.YAMLError:
        return None
    if obj is None:
        return {}
    if not isinstance(obj, dict):
        return None
    return obj


def update_file(path: Path, dry_run: bool, source: str) -> UpdateResult:
    source_text = _load_source_text(path, source=source)
    if source_text is None:
        return UpdateResult(path=path, skipped_parse_error=True)

    lines, end_idx = _split_frontmatter(source_text)
    if lines is None:
        return UpdateResult(path=path, skipped_parse_error=True)

    meta = _parse_metadata(lines, end_idx)
    if meta is None:
        return UpdateResult(path=path, skipped_parse_error=True)

    # Safety: this should only be Resource pages.
    if meta.get("category") == "Product":
        return UpdateResult(path=path)

    needs_creation = not bool(meta.get("creation_date"))
    needs_modified = not bool(meta.get("last_modified_date"))
    if not (needs_creation or needs_modified):
        return UpdateResult(path=path)

    creation = None
    modified = None
    if needs_creation:
        creation = git_commit_date(path, earliest=True)
        if creation is None:
            return UpdateResult(path=path, skipped_missing_git_history=True)
    if needs_modified:
        modified = git_commit_date(path, earliest=False)
        if modified is None:
            return UpdateResult(path=path, skipped_missing_git_history=True)

    if dry_run:
        return UpdateResult(
            path=path,
            added_creation=bool(creation),
            added_modified=bool(modified),
        )

    new_lines = list(lines)
    insert_lines = []
    if creation:
        insert_lines.append(f"creation_date: '{creation}'\n")
    if modified:
        insert_lines.append(f"last_modified_date: '{modified}'\n")
    new_lines[end_idx:end_idx] = insert_lines

    path.write_text("".join(new_lines), encoding="utf-8")
    return UpdateResult(
        path=path,
        added_creation=bool(creation),
        added_modified=bool(modified),
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Backfill missing Resource date fields from git history.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned updates without writing files.",
    )
    parser.add_argument(
        "--source",
        choices=("worktree", "head"),
        default="worktree",
        help="Read file content from worktree or HEAD before patching (default: worktree).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional limit on number of files to process.",
    )
    args = parser.parse_args()

    files = list(iter_root_resource_files())
    if args.limit is not None:
        files = files[: args.limit]

    updated_files = 0
    added_creation = 0
    added_modified = 0
    skipped_no_history = 0
    skipped_parse_error = 0

    for path in files:
        result = update_file(path, dry_run=args.dry_run, source=args.source)
        if result.skipped_missing_git_history:
            skipped_no_history += 1
            print(f"SKIP(no git history): {path.relative_to(ROOT)}")
            continue
        if result.skipped_parse_error:
            skipped_parse_error += 1
            print(f"SKIP(parse error): {path.relative_to(ROOT)}")
            continue

        if result.added_creation or result.added_modified:
            updated_files += 1
            if result.added_creation:
                added_creation += 1
            if result.added_modified:
                added_modified += 1

            if args.dry_run:
                parts = []
                if result.added_creation:
                    parts.append("creation_date")
                if result.added_modified:
                    parts.append("last_modified_date")
                print(f"WOULD UPDATE({', '.join(parts)}): {path.relative_to(ROOT)}")

    mode = "DRY-RUN" if args.dry_run else "UPDATED"
    print(
        f"{mode}: files={updated_files} "
        f"creation_date_added={added_creation} "
        f"last_modified_date_added={added_modified} "
        f"skipped_no_history={skipped_no_history} "
        f"skipped_parse_error={skipped_parse_error}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
