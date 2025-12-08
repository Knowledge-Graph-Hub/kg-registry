#!/usr/bin/env python3
"""
Validation utilities for KG-Registry.

This module provides validation functions for both Resource and Organization
files against the KG-Registry schema.
"""

import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from copy import deepcopy
from typing import Any, Callable, Dict, List, Optional, Tuple

import jsonschema
from linkml.validator import validate as linkml_validate
from yamllint import config, linter

from common import (
    INACTIVE_STATUSES,
    SCHEMA_PATH,
    SOURCE_SCHEMA_PATH,
    YAMLLINT_CONFIG_PATH,
    CustomRuamelYAMLHandler,
    get_separator_for_file,
    get_yaml_text,
    load_frontmatter_file,
)

__all__ = [
    # Resource validation
    "validate_resource",
    "validate_resources_parallel",
    "load_json_schema",
    # Organization validation
    "validate_organization",
    "validate_organizations",
    # Results handling
    "ValidationResults",
    "print_results",
    "save_results",
]


# =============================================================================
# Validation Results Class
# =============================================================================


class ValidationResults:
    """Container for validation results with error, warning, and info levels."""

    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.infos: List[str] = []

    def add_error(self, message: str) -> None:
        self.errors.append(message)

    def add_warning(self, message: str) -> None:
        self.warnings.append(message)

    def add_info(self, message: str) -> None:
        self.infos.append(message)

    def merge(self, other: "ValidationResults") -> None:
        """Merge results from another ValidationResults instance."""
        self.errors.extend(other.errors)
        self.warnings.extend(other.warnings)
        self.infos.extend(other.infos)

    def has_errors(self) -> bool:
        return len(self.errors) > 0

    def has_warnings(self) -> bool:
        return len(self.warnings) > 0

    def to_dict(self) -> Dict[str, List[str]]:
        return {
            "error": self.errors,
            "warn": self.warnings,
            "info": self.infos,
        }

    @classmethod
    def from_dict(cls, d: Dict[str, List[str]]) -> "ValidationResults":
        result = cls()
        result.errors = d.get("error", [])
        result.warnings = d.get("warn", [])
        result.infos = d.get("info", [])
        return result


# =============================================================================
# Schema Loading
# =============================================================================


def load_json_schema(schema_path: str = None) -> Optional[Dict[str, Any]]:
    """
    Load the JSON schema for resource validation.

    Args:
        schema_path: Optional path to schema file (defaults to SCHEMA_PATH)

    Returns:
        The loaded JSON schema dictionary, or None if loading fails
    """
    path = schema_path or SCHEMA_PATH
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Unable to load schema {path}: {e}")
        return None


# =============================================================================
# Resource Validation
# =============================================================================


def validate_resource(
    item: Dict[str, Any],
    schema: Dict[str, Any],
    metadata_grid: Dict[str, Dict] = None
) -> ValidationResults:
    """
    Validate a single resource against the JSON schema.

    Args:
        item: Resource metadata dictionary
        schema: JSON schema to validate against
        metadata_grid: Optional grid to track validation results

    Returns:
        ValidationResults containing any errors, warnings, or infos
    """
    results = ValidationResults()
    resource_id = item.get("id", "unknown")

    # Track grid results
    grid_entry = {}
    grid_entry["inactive"] = item.get("activity_status") in INACTIVE_STATUSES
    grid_entry["resource_status"] = item.get("activity_status", "inactive")

    has_error = False
    has_warn = False
    has_info = False

    try:
        jsonschema.validate(item, schema)
    except jsonschema.exceptions.ValidationError as ve:
        # Extract the field name from the error
        title = list(ve.absolute_schema_path)[0]
        if title == "required":
            field_names = re.findall(r"\'(.*?)\'", ve.message)
            if field_names:
                title = field_names[0]
        if title == "properties":
            title = list(ve.absolute_schema_path)[1]

        # Get the schema "level" for this field
        level = _get_schema_level(title, ve, schema)
        if level is None:
            level = "error"  # Default to error if level not found

        grid_entry[title] = level

        # Set flags
        if level == "error":
            has_error = True
        elif level == "warning":
            has_warn = True
        elif level == "info":
            has_info = True

        # Skip logging for inactive resources on certain fields
        if not (
            item.get("activity_status") in INACTIVE_STATUSES
            and title in ["contact", "license", "repository"]
        ):
            # Format message
            msg = _format_validation_message(ve, title, resource_id)

            if level == "error":
                results.add_error(msg)
            elif level == "warning":
                if "required" in msg:
                    msg = msg.replace("required", "recommended")
                results.add_warning(msg)
            elif level == "info":
                results.add_info(msg)

    # Set overall validation status
    if has_error:
        grid_entry["validation_status"] = "FAIL"
    elif has_warn:
        grid_entry["validation_status"] = "WARN"
    elif has_info:
        grid_entry["validation_status"] = "INFO"
    else:
        grid_entry["validation_status"] = "PASS"

    if metadata_grid is not None:
        metadata_grid[resource_id] = grid_entry

    return results


def _get_schema_level(
    title: str,
    ve: jsonschema.exceptions.ValidationError,
    schema: Dict[str, Any]
) -> Optional[str]:
    """Extract the validation level from the schema for a field."""
    if title not in list(ve.absolute_schema_path) and title not in schema.get("properties", {}):
        return None

    if title in list(ve.absolute_schema_path):
        title_index = list(ve.absolute_schema_path).index(title)
        path = list(ve.absolute_schema_path)[0:(title_index + 1)]
    else:
        path = ["properties", title]

    abs_schema = schema
    level = None
    try:
        for schema_item in path:
            if schema_item in abs_schema:
                if "level" in abs_schema[schema_item]:
                    level = abs_schema[schema_item]["level"]
                abs_schema = abs_schema[schema_item]
    except (TypeError, KeyError):
        pass

    return level


def _format_validation_message(
    ve: jsonschema.exceptions.ValidationError,
    title: str,
    resource_id: str
) -> str:
    """Format a validation error message."""
    msg = ve.message

    # Special handling for license messages
    if title == "license":
        search = re.search("'(.+?)' is not one of", msg)
        if search:
            msg = f"'{search.group(1)}' is not a recommended license"
        else:
            search = re.search(r"(\{'label'.+?'url'.+?\}) is not valid", msg)
            if not search:
                search = re.search(r"(\{'url'.+?'label'.+?\}) is not valid", msg)
            if search:
                try:
                    d = json.loads(search.group(1).replace("'", '"'))
                    msg = f"'{d.get('label')}' <{d.get('url')}> is not a recommended license"
                except (json.JSONDecodeError, KeyError):
                    pass

    return f"{resource_id.upper()} {title}: {msg}"


def validate_resources_parallel(
    resources: List[Dict[str, Any]],
    schema: Dict[str, Any],
    max_workers: int = 10,
    metadata_grid: Dict[str, Dict] = None
) -> ValidationResults:
    """
    Validate multiple resources in parallel.

    Args:
        resources: List of resource metadata dictionaries
        schema: JSON schema to validate against
        max_workers: Number of worker threads
        metadata_grid: Optional grid to track validation results

    Returns:
        Combined ValidationResults for all resources
    """
    if len(resources) < 50:
        # Use sequential validation for small sets
        combined = ValidationResults()
        for item in resources:
            result = validate_resource(item, schema, metadata_grid)
            combined.merge(result)
        return combined

    print(f"Validating {len(resources)} resources with {max_workers} workers...")
    combined = ValidationResults()

    def validate_single(item):
        return (item.get("id", "unknown"), validate_resource(item, schema, metadata_grid))

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(validate_single, item): item for item in resources}

        completed = 0
        for future in as_completed(futures):
            resource_id, result = future.result()
            combined.merge(result)
            completed += 1
            if completed % 100 == 0:
                print(f"  Progress: {completed}/{len(resources)} resources validated")

    print(f"  ✅ Completed validation of {len(resources)} resources")
    return combined


# =============================================================================
# Organization Validation
# =============================================================================


def validate_organization(
    filepath: str,
    verbose: bool = False
) -> ValidationResults:
    """
    Validate a single Organization file against the schema.

    Args:
        filepath: Path to the organization markdown file
        verbose: Whether to print verbose output

    Returns:
        ValidationResults containing any errors or warnings
    """
    import pathlib
    results = ValidationResults()
    fp = pathlib.Path(filepath)

    # Check frontmatter exists
    import frontmatter as fm
    if not fm.check(filepath):
        results.add_error(f"{filepath} does not contain frontmatter")
        return results

    # Load the file
    metadata, _, error = load_frontmatter_file(fp, use_ruamel=True)
    if error:
        results.add_error(f"Failed to parse YAML in {filepath}: {error}")
        return results

    # Check category
    if metadata.get("category") != "Organization":
        results.add_error(
            f"{filepath}: category must be 'Organization', got '{metadata.get('category')}'"
        )
        return results

    # Check required fields
    if not metadata.get("id"):
        results.add_error(f"{filepath}: missing required field 'id'")
    if not metadata.get("label"):
        results.add_error(f"{filepath}: missing required field 'label'")
    if not metadata.get("layout"):
        results.add_warning(f"{filepath}: missing 'layout' field (should be 'organization_detail')")
    elif metadata.get("layout") != "organization_detail":
        results.add_warning(
            f"{filepath}: layout should be 'organization_detail', got '{metadata.get('layout')}'"
        )

    # Validate against LinkML schema
    report = linkml_validate(
        instance=metadata,
        schema=str(SOURCE_SCHEMA_PATH),
        target_class="Organization"
    )
    if report.results:
        for r in report.results:
            if r.severity == "ERROR":
                results.add_error(f"{filepath}: {r.message}")
            elif r.severity == "WARNING":
                results.add_warning(f"{filepath}: {r.message}")

    # Run yamllint
    if YAMLLINT_CONFIG_PATH.exists():
        yaml_text = get_yaml_text(fp)
        yaml_config = config.YamlLintConfig(file=str(YAMLLINT_CONFIG_PATH))
        for problem in linter.run("---\n" + yaml_text, yaml_config):
            if problem.level == "error":
                results.add_error(f"{filepath}: {problem}")
            elif problem.level == "warning":
                results.add_warning(f"{filepath}: {problem}")

    return results


def validate_organizations(
    files: List[str],
    verbose: bool = False
) -> ValidationResults:
    """
    Validate multiple Organization files.

    Args:
        files: List of file paths to validate
        verbose: Whether to print verbose output

    Returns:
        Combined ValidationResults for all files
    """
    combined = ValidationResults()
    for filepath in files:
        result = validate_organization(filepath, verbose)
        combined.merge(result)
    return combined


# =============================================================================
# Results Output
# =============================================================================


def print_results(results: ValidationResults) -> None:
    """Print validation results to the console."""
    for msg in results.errors:
        print(f"ERROR\t{msg}")
    for msg in results.warnings:
        print(f"WARN\t{msg}")
    for msg in results.infos:
        print(f"INFO\t{msg}")


def save_results(
    results: ValidationResults,
    outfile: str
) -> None:
    """
    Save validation results to a file.

    Args:
        results: ValidationResults to save
        outfile: Path to output file (CSV, TSV, or TXT)
    """
    separator = get_separator_for_file(outfile)

    with open(outfile, "w") as f:
        f.write(f"Level{separator}Message\n")
        for msg in results.errors:
            f.write(f"ERROR{separator}{msg}\n")
        for msg in results.warnings:
            f.write(f"WARN{separator}{msg}\n")
        for msg in results.infos:
            f.write(f"INFO{separator}{msg}\n")


def sort_metadata_grid(
    metadata_grid: Dict[str, Dict]
) -> List[str]:
    """
    Sort the metadata grid based on status and validation results.

    Args:
        metadata_grid: Dictionary mapping resource IDs to their validation results

    Returns:
        Sorted list of resource IDs
    """
    active = {"PASS": [], "INFO": [], "WARN": [], "FAIL": []}
    inactive = {"PASS": [], "INFO": [], "WARN": [], "FAIL": []}

    for resource_id, results in metadata_grid.items():
        resource_status = results.get("resource_status", "inactive")
        validation_status = results.get("validation_status", "FAIL")

        if results.get("inactive", True):
            inactive[validation_status].append(resource_id)
        elif resource_status == "active":
            active[validation_status].append(resource_id)
        else:
            inactive[validation_status].append(resource_id)

    sorted_ids = []
    for status_group in [active, inactive]:
        for v_status in ["PASS", "INFO", "WARN", "FAIL"]:
            sorted_list = sorted(status_group[v_status], key=str.lower)
            sorted_ids.extend(sorted_list)

    return sorted_ids


def save_metadata_grid(
    metadata_grid: Dict[str, Dict],
    headers: List[str],
    outfile: str
) -> None:
    """
    Save the metadata validation grid to a file.

    Args:
        metadata_grid: Dictionary of validation results per resource
        headers: List of additional column headers
        outfile: Path to output file
    """
    separator = get_separator_for_file(outfile)
    sort_order = sort_metadata_grid(metadata_grid)

    header = f"Resource{separator}Activity Status{separator}Validation Status"
    for h in headers:
        header += separator + h
    header += "\n"

    with open(outfile, "w") as f:
        f.write(header)
        for resource_id in sort_order:
            results = metadata_grid.get(resource_id, {})
            line = f"{resource_id}{separator}{results.get('resource_status', '')}{separator}{results.get('validation_status', '')}"
            for h in headers:
                value = results.get(h, "")
                if h == "license":
                    # License has two checks - use more severe
                    all_res = [results.get("license", ""), results.get("license-lite", "")]
                    if "error" in all_res:
                        value = "error"
                    elif "warning" in all_res:
                        value = "warning"
                    elif "info" in all_res:
                        value = "info"
                    else:
                        value = "pass"
                line += separator + str(value)
            f.write(line + "\n")

    print(f"Full validation results written to {outfile}")
