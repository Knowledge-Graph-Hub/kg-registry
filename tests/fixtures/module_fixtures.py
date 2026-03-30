import importlib.util
import sys
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


@pytest.fixture(scope="session")
def util_dir(repo_root: Path) -> Path:
    return repo_root / "util"


def _load_module(module_name: str, script_path: Path, extra_sys_path: Path | None = None):
    added_path = False
    if extra_sys_path is not None:
        extra_path_str = str(extra_sys_path)
        if extra_path_str not in sys.path:
            sys.path.insert(0, extra_path_str)
            added_path = True

    try:
        spec = importlib.util.spec_from_file_location(module_name, str(script_path))
        assert spec is not None and spec.loader is not None, f"Could not load {script_path.name}"
        mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
        sys.modules[module_name] = mod
        spec.loader.exec_module(mod)  # type: ignore[attr-defined]
        return mod
    finally:
        if added_path:
            sys.path.pop(0)


@pytest.fixture(scope="session")
def extract_metadata_module(repo_root: Path):
    return _load_module("extract_metadata", repo_root / "util" / "extract-metadata.py")


@pytest.fixture(scope="session")
def quality_dashboard_module(repo_root: Path, util_dir: Path):
    return _load_module(
        "quality_dashboard",
        repo_root / "util" / "generate-quality-dashboard.py",
        extra_sys_path=util_dir,
    )


@pytest.fixture(scope="session")
def kg_monarch_ingest_module(repo_root: Path):
    return _load_module(
        "kg_monarch_ingest",
        repo_root / "src" / "kg_registry" / "ingests" / "kg-monarch" / "kg-monarch.py",
    )


@pytest.fixture(scope="session")
def parallel_validator_module(repo_root: Path, util_dir: Path):
    return _load_module(
        "parallel_validator",
        repo_root / "util" / "parallel_validator.py",
        extra_sys_path=util_dir,
    )
