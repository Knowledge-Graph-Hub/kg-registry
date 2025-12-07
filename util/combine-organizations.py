#!/usr/bin/env python3
"""
Combine all Organization YAML frontmatter files into a single YAML file.

This script reads all .md files from the org/ directory,
extracts their YAML frontmatter, and combines them into a single
organizations.yml file for use by the site.
"""

import argparse
import pathlib
import sys

import frontmatter
import yaml

HERE = pathlib.Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
ORG_DIR = ROOT / "org"
OUTPUT_FILE = ROOT / "registry" / "organizations.yml"


def combine_organizations(output_path: pathlib.Path = OUTPUT_FILE) -> None:
    """
    Read all organization .md files and combine their frontmatter into a single YAML file.
    
    Args:
        output_path: Path to write the combined YAML output
    """
    organizations = []
    
    # Find all organization directories
    if not ORG_DIR.exists():
        print(f"Warning: Organization directory {ORG_DIR} does not exist")
        return
    
    for org_subdir in sorted(ORG_DIR.iterdir()):
        if not org_subdir.is_dir():
            continue
        
        # Look for .md files in each organization subdirectory
        for md_file in org_subdir.glob("*.md"):
            try:
                post = frontmatter.load(md_file)
                metadata = dict(post.metadata)
                
                # Ensure it's actually an Organization
                if metadata.get("category") != "Organization":
                    print(f"Warning: Skipping {md_file} - not an Organization (category: {metadata.get('category')})")
                    continue
                
                organizations.append(metadata)
                print(f"Loaded organization: {metadata.get('id', 'unknown')}")
                
            except Exception as e:
                print(f"Error loading {md_file}: {e}", file=sys.stderr)
                continue
    
    # Sort by ID
    organizations.sort(key=lambda x: x.get("id", ""))
    
    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w") as f:
        f.write("# Combined Organization metadata\n")
        f.write("# Auto-generated - do not edit directly\n")
        f.write("# Edit the individual files in org/ instead\n\n")
        f.write("organizations:\n")
        yaml.dump(organizations, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    print(f"\n✅ Combined {len(organizations)} organization(s) into {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Combine Organization YAML files into a single file"
    )
    parser.add_argument(
        "-o", "--output",
        type=pathlib.Path,
        default=OUTPUT_FILE,
        help=f"Output file path (default: {OUTPUT_FILE})"
    )
    
    args = parser.parse_args()
    combine_organizations(args.output)


if __name__ == "__main__":
    main()
