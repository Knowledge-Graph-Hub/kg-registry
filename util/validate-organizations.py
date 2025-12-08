#!/usr/bin/env python3
"""
Validate Organization markdown files against the KG-Registry schema.

This script validates the YAML frontmatter in Organization markdown files
against the LinkML schema, ensuring they conform to the Organization class.
"""

import argparse
import sys
import pathlib

import frontmatter
from copy import deepcopy
from linkml.validator import validate
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO
from ruamel.yaml.scanner import ScannerError
from yaml.parser import ParserError
from frontmatter.util import u
from yamllint import config, linter

HERE = pathlib.Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
SOURCE_SCHEMA_PATH = ROOT.joinpath(
    "src", "kg_registry", "kg_registry_schema", "schema", "kg_registry_schema_all.yaml"
)


class CustomRuamelYAMLHandler(frontmatter.YAMLHandler):
    """Custom YAML handler using ruamel for better formatting preservation."""
    
    def __init__(self):
        self.myyaml = YAML()
        self.myyaml.default_flow_style = False
        self.myyaml.allow_duplicate_keys = True
        self.myyaml.indent(mapping=2, sequence=4, offset=2)
        self.myyaml.preserve_quotes = True
        self.myyaml.width = 1500
        super().__init__()

    def load(self, fm, **kwargs):
        return self.myyaml.load(fm, **kwargs)

    def export(self, metadata, **kwargs):
        stream = StringIO()
        self.myyaml.dump(data=metadata, stream=stream)
        metadata = stream.getvalue()
        metadata = metadata[:-1]
        return u(metadata)


def get_yaml_text(fn):
    """Extract YAML frontmatter text from a markdown file."""
    with open(fn, "r") as f:
        content = f.read()
    
    if not content.startswith("---"):
        return ""
    
    # Find the closing ---
    end_idx = content.find("---", 3)
    if end_idx == -1:
        return ""
    
    return content[3:end_idx].strip()


def validate_organizations(files):
    """
    Validate Organization markdown files against the schema.
    
    Args:
        files: List of file paths to validate
        
    Returns:
        Tuple of (errors, warnings)
    """
    errs = []
    warn = []
    
    for fn in files:
        # Check to see if we can parse the yaml frontmatter first
        if not frontmatter.check(fn):
            errs.append(f"{fn} does not contain frontmatter")
            continue

        # Load with ruamel handler so we can preserve/emit quotes
        handler = CustomRuamelYAMLHandler()
        try:
            post = frontmatter.load(fn, handler=handler)
        except (ScannerError, ParserError) as e:
            errs.append(f"Failed to parse YAML in {fn}: {e}")
            continue
        
        obj = deepcopy(post.metadata)
        
        # Check that this is an Organization
        if obj.get("category") != "Organization":
            errs.append(f"{fn}: category must be 'Organization', got '{obj.get('category')}'")
            continue
        
        # Check required fields for Organization
        if not obj.get("id"):
            errs.append(f"{fn}: missing required field 'id'")
        if not obj.get("label"):
            errs.append(f"{fn}: missing required field 'label'")
        if not obj.get("layout"):
            warn.append(f"{fn}: missing 'layout' field (should be 'organization_detail')")
        elif obj.get("layout") != "organization_detail":
            warn.append(f"{fn}: layout should be 'organization_detail', got '{obj.get('layout')}'")
        
        # Validate against the Organization class using LinkML
        report = validate(
            instance=obj, 
            schema=str(SOURCE_SCHEMA_PATH), 
            target_class="Organization"
        )
        if report.results:
            for result in report.results:
                if result.severity == "ERROR":
                    errs.append(f"{fn}: {result.message}")
                elif result.severity == "WARNING":
                    warn.append(f"{fn}: {result.message}")

        # Run yaml linter to check for basic syntax errors and formatting
        yamltext = get_yaml_text(fn)
        yaml_config_path = ROOT / "util" / "config.yamllint"
        if yaml_config_path.exists():
            yaml_config = config.YamlLintConfig(file=str(yaml_config_path))
            for p in linter.run("---\n" + yamltext, yaml_config):
                if p.level == "error":
                    errs.append(f"{fn}: {p}")
                elif p.level == "warning":
                    warn.append(f"{fn}: {p}")
    
    return errs, warn


def main():
    parser = argparse.ArgumentParser(
        description="Validate Organization markdown files against the KG-Registry schema"
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="Organization markdown files to validate"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show verbose output"
    )
    
    args = parser.parse_args()
    
    if not args.files:
        print("No files specified", file=sys.stderr)
        sys.exit(1)
    
    errs, warn = validate_organizations(args.files)
    
    if args.verbose or warn:
        if warn:
            print("WARNINGS:", file=sys.stderr)
            for w in warn:
                print(f"  WARN: {w}", file=sys.stderr)
    
    if errs:
        print("FAILURES:", file=sys.stderr)
        for e in errs:
            print(f"  ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"✅ Validated {len(args.files)} organization file(s) successfully")


if __name__ == "__main__":
    main()
