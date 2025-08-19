#!/usr/bin/env python3

import argparse
import csv
import sys
import pathlib
import datetime
import json

import frontmatter
import yaml
from copy import deepcopy
from frontmatter.util import u
from linkml.validator import validate
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO
from ruamel.yaml.scalarstring import DoubleQuotedScalarString as DQ
from yamllint import config, linter

__author__ = "cjm"
HERE = pathlib.Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
SOURCE_SCHEMA_PATH = ROOT.joinpath(
    "src", "kg_registry", "kg_registry_schema", "schema", "kg_registry_schema_all.yaml")
SCHEMA_PATH = ROOT.joinpath("src", "kg_registry", "kg_registry_schema", "kg_registry_schema.json")

# Ensure local src is importable for generated datamodel imports
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))


def main():
    parser = argparse.ArgumentParser(
        description="Helper utils for KG-Registry",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="subcommand", help="sub-command help")

    # SUBCOMMAND
    parser_n = subparsers.add_parser("validate", help="validate yaml inside md")
    parser_n.set_defaults(function=validate_markdown)
    parser_n.add_argument("files", nargs="*")
    parser_n = subparsers.add_parser(
        "prettify", help="prettify YAML block in registry Markdown files"
    )
    parser_n.set_defaults(function=prettify)
    parser_n.add_argument("files", nargs="*")
    # SUBCOMMAND
    parser_n = subparsers.add_parser("concat", help="concat resource yamls")
    parser_n.add_argument("-i", "--include", help="yaml file to include for header")
    parser_n.add_argument("-o", "--output", help="output yaml file")
    parser_n.set_defaults(function=concat_resource_yaml)
    parser_n.add_argument("files", nargs="*")

    args = parser.parse_args()

    func = args.function
    func(args)


class CustomRuamelYAMLHandler(frontmatter.YAMLHandler):
    def __init__(self):
        self.myyaml = YAML()
        self.myyaml.default_flow_style = False
        self.myyaml.allow_duplicate_keys = True
        self.myyaml.indent(mapping=2, sequence=4, offset=2)
        self.myyaml.preserve_quotes = True
        self.myyaml.width = 1500
        # self.myyaml.explicit_start = True
        super().__init__()

    def load(self, fm, **kwargs):
        return self.myyaml.load(fm, **kwargs)

    def export(self, metadata, **kwargs):
        stream = StringIO()
        self.myyaml.dump(data=metadata, stream=stream)
        metadata = stream.getvalue()
        metadata = metadata[:-1]
        return u(metadata)


def prettify(args):
    for file in args.files:
        handler = CustomRuamelYAMLHandler()
        text = frontmatter.load(file, handler=handler)
        file_obj = open(file, "wb")
        frontmatter.dump(text, fd=file_obj, handler=handler)
        file_obj = open(file, "a")
        file_obj.write("\n")
        file_obj.close()


def validate_markdown(args):
    """
    Ensure the yaml encoded inside a YAML file is syntactically valid.

    First attempt to strip the yaml from the .md file, second use the standard python yaml parser
    to parse the embedded yaml. If it can't be passed then an error will be thrown and a stack
    trace shown.

    This also uses the LinkML schema to validate the yaml.
    """

    errs = []
    warn = []
    for fn in args.files:
        # Check to see if we can parse the yaml frontmatter first
        if not frontmatter.check(fn):
            errs.append("%s does not contain frontmatter" % (fn))

        # Load with ruamel handler so we can preserve/emit quotes
        handler = CustomRuamelYAMLHandler()
        post = frontmatter.load(fn, handler=handler)
        obj = deepcopy(post.metadata)
        md_content = post.content

        # Coerce certain scalar fields to quoted strings, normalize dates, and sanitize domains
        original_obj = deepcopy(obj)
        obj = coerce_string_like_fields(obj)
        obj = normalize_date_fields(obj)
        obj = sanitize_domains(obj)

        # If modified, write back in-place using ruamel to preserve formatting and quotes
        if obj != original_obj:
            post.metadata = obj
            with open(fn, "wb") as fwb:
                frontmatter.dump(post, fd=fwb, handler=handler)
            # Ensure trailing newline after frontmatter/content
            with open(fn, "a") as fa:
                fa.write("\n")

        # If this is the root of the resource, validate against the Resource class
        # These pages will already contain child classes, so other
        # pages don't need their own validation (it would be redundant)
        if obj.get("id") == pathlib.Path(fn).parent.name:
            target_class = "Resource"
        else:
            continue

        report = validate(instance=obj, schema=str(SOURCE_SCHEMA_PATH), target_class=target_class)
        if report.results:
            for result in report.results:
                if result.severity == "ERROR":
                    errs.append(f"{fn}: {result.message}")

        # Now run yaml linter to check for basic syntax errors and formatting
        yamltext = get_YAML_text(fn)
        yaml_config = config.YamlLintConfig(file="util/config.yamllint")
        for p in linter.run("---\n" + yamltext, yaml_config):
            if p.level == "error":
                errs.append(f"%s: {p}" % (fn))
            elif p.level == "warning":
                warn.append(f"%s: {p}" % (fn))

    if len(warn) > 0:
        print("WARNINGS:", file=sys.stderr)
        for w in warn:
            print("WARN: " + w, file=sys.stderr)
    if len(errs) > 0:
        print("FAILURES:", file=sys.stderr)
        for e in errs:
            print("ERROR:" + e, file=sys.stderr)
        sys.exit(1)


def concat_resource_yaml(args):
    """
    Given arguments with files and ouput,
    read YAML files into an array and write an output YAML file.
    Output will be concatenated list of all resource metadata.
    Assumes that args.files is already sorted alphabetically.

    This function also:
    * Creates sub-pages for products as needed
    * Propagates derived products to the source Resource pages
    * Adds a logo to the license metadata if it exists
    * Creates stub Resource pages for sources mentioned in products but don't have a page yet
    """

    def decorate_metadata(objs):
        """
        Add the logo corresponding to the given object's license (if it has one).
        """

        for obj in objs:
            if "license" in obj:
                # https://creativecommons.org/about/downloads
                license = obj["license"]
                try:
                    lurl = license["id"]  # This should be a URL
                except KeyError:
                    print(f"ERROR: Could not find id for license in {obj['id']}")
                    sys.exit(1)
                logo = ""
                if lurl.find("creativecommons.org/licenses/by-sa") > 0:
                    logo = (
                        "https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png"
                    )
                elif lurl.find("creativecommons.org/licenses/by/") > 0:
                    logo = "http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png"
                elif lurl.find("creativecommons.org/publicdomain/zero/") > 0:
                    logo = (
                        "http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png"
                    )
                if logo:
                    license["logo"] = logo

    def generate_product_pages(objs):
        layout_string = "layout: product_detail"
        for obj in objs:
            if "products" in obj:
                for product in obj["products"]:
                    # Only create pages for products with IDs that start with the resource ID
                    if "id" in product and (product["id"]).startswith(obj["id"]):
                        fn = f"resource/{obj['id']}/{product['id']}.md"
                        file_path = pathlib.Path(fn)

                        # Create a copy of the product to add layout
                        product_with_layout = deepcopy(product)

                        # Check if file exists
                        if file_path.exists():
                            try:
                                # Load existing product data
                                existing_product = frontmatter.load(fn).metadata

                                # Remove layout from comparison if it exists
                                existing_product_copy = deepcopy(existing_product)
                                if "layout" in existing_product_copy:
                                    del existing_product_copy["layout"]

                                # Compare content (ignoring order)
                                if yaml.dump(sorted(product.items())) == yaml.dump(sorted(existing_product_copy.items())):
                                    continue
                                else:
                                    print(
                                        f"Updating page for product {product['id']} - content changed")
                                    # Show what's different
                                    product_keys = set(product.keys())
                                    existing_keys = set(existing_product_copy.keys())

                                    # Show added or removed keys
                                    added_keys = product_keys - existing_keys
                                    removed_keys = existing_keys - product_keys
                                    if added_keys:
                                        print(f"  Added fields: {', '.join(added_keys)}")
                                    if removed_keys:
                                        print(f"  Removed fields: {', '.join(removed_keys)}")

                                    # Show changed values for common keys
                                    common_keys = product_keys.intersection(existing_keys)
                                    for key in common_keys:
                                        if product[key] != existing_product_copy.get(key):
                                            print(f"  Changed '{key}'")
                            except Exception as e:
                                print(
                                    f"Error reading existing product file {fn}, will recreate: {str(e)}")
                        else:
                            print(f"Creating new page for product {product['id']}")

                        # Write the product to its own page
                        with open(fn, "w") as f:
                            f.write("---\n" + yaml.dump(product) + layout_string + "\n---\n")

    def _normalize_warning_msg(msg: str) -> str:
        """Return a normalized warning string with dates and extra whitespace removed for similarity grouping."""
        import re
        if not isinstance(msg, str):
            return ''
        s = msg
        # Remove ISO and YYYY-MM-DD date patterns and nearby prepositions
        s = re.sub(
            r"\b(on|as of|checked on|at)\s+\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}:\d{2}Z)?", "", s, flags=re.IGNORECASE)
        s = re.sub(r"\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}:\d{2}Z)?", "", s)
        # Collapse whitespace and punctuation spaces
        s = re.sub(r"\s+", " ", s).strip().lower()
        return s

    def _date_from_warning(msg: str):
        """Extract a date object from a warning message if present (YYYY-MM-DD or ISO with Z)."""
        import re
        import datetime as _dt
        if not isinstance(msg, str):
            return None
        m = re.search(r"(\d{4}-\d{2}-\d{2})(?:T\d{2}:\d{2}:\d{2}Z)?", msg)
        if not m:
            return None
        try:
            return _dt.datetime.strptime(m.group(1), "%Y-%m-%d").date()
        except Exception:
            return None

    def dedupe_product_warnings(objs):
        """Deduplicate very similar warnings per product, keeping the most recent dated entry.
        Updates both in-memory objects and resource markdown files when changes occur."""
        updated_resources = 0
        for obj in objs:
            if "id" not in obj:
                continue
            changed = False
            if "products" in obj and isinstance(obj["products"], list):
                for p in obj["products"]:
                    warns = p.get("warnings")
                    if not warns or not isinstance(warns, list):
                        continue
                    groups = {}
                    for w in warns:
                        key = _normalize_warning_msg(w)
                        d = _date_from_warning(w)
                        if key not in groups:
                            groups[key] = (w, d)
                        else:
                            # Keep the one with the latest date (or keep existing if no date comparison possible)
                            _, existing_date = groups[key]
                            if d and ((existing_date is None) or (d > existing_date)):
                                groups[key] = (w, d)
                    # Rebuild list: choose the kept warning per group; stable order by descending date then text
                    new_warns = [wd[0] for wd in sorted(
                        groups.values(), key=lambda wd: (wd[1] is not None, wd[1]), reverse=True)]
                    if new_warns != warns:
                        p["warnings"] = new_warns
                        changed = True
            if changed:
                # Persist back to the resource markdown file
                fn = f"resource/{obj['id']}/{obj['id']}.md"
                try:
                    (metadata, md) = load_md(fn)
                    if "products" in metadata and isinstance(metadata["products"], list):
                        # Align warnings from in-memory obj to file metadata
                        # Build a map from product id to warnings
                        id_to_warns = {}
                        for p in obj["products"]:
                            if isinstance(p, dict) and "id" in p and "warnings" in p:
                                id_to_warns[p["id"]] = p["warnings"]
                        for idx, prod in enumerate(metadata["products"]):
                            if isinstance(prod, dict) and "id" in prod and prod["id"] in id_to_warns:
                                if id_to_warns[prod["id"]] != prod.get("warnings"):
                                    metadata["products"][idx]["warnings"] = id_to_warns[prod["id"]]
                                    updated_resources += 1
                    with open(fn, "w") as f:
                        f.write("---\n" + yaml.dump(metadata) + "---\n" + md)
                except Exception as e:
                    print(f"Error updating warnings for resource {obj['id']}: {str(e)}")
        if updated_resources:
            print(f"Deduplicated warnings for {updated_resources} product entries across resources")

    def create_stub_resource_pages(objs):
        """
        Create stub Resource pages for sources mentioned in products but don't have a page yet.
        For example, if a product references 'disgenet' as an original_source but there's no
        resource/disgenet/disgenet.md file, create one with minimal information.

        A product could also reference another product, in which case we also create a stub page
        for that product if it doesn't exist. References can be in the format:
        - 'resource_id' for a simple resource reference
        - 'resource_id.product_id' for a specific product reference
        """
        # First collect all resource IDs mentioned in products and their related product IDs
        referenced_resources = set()
        resource_product_map = {}  # Maps resource_id to set of product_ids that should be added

        for obj in objs:
            if "products" in obj:
                for product in obj["products"]:
                    # Check original_source and secondary_source fields
                    for field_name in ["original_source", "secondary_source"]:
                        if field_name in product and isinstance(product[field_name], list):
                            for resource_ref in product[field_name]:
                                if not resource_ref or not isinstance(resource_ref, str):
                                    continue

                                # Handle resource.product format
                                if '.' in resource_ref:
                                    parts = resource_ref.split('.', 1)
                                    resource_id = parts[0]
                                    product_id = parts[1]

                                    # Add resource to referenced_resources
                                    referenced_resources.add(resource_id)

                                    # Add product to resource_product_map
                                    if resource_id not in resource_product_map:
                                        resource_product_map[resource_id] = set()
                                    resource_product_map[resource_id].add(product_id)
                                else:
                                    # Simple resource reference
                                    referenced_resources.add(resource_ref)

        # Get the list of existing resource directories
        existing_resources = set()
        resource_dir = pathlib.Path(ROOT / "resource")
        if resource_dir.exists() and resource_dir.is_dir():
            for path in resource_dir.iterdir():
                if path.is_dir():
                    existing_resources.add(path.name)

        # Find resources mentioned but don't have a directory
        missing_resources = referenced_resources - existing_resources
        if missing_resources:
            print(
                f"Found {len(missing_resources)} resources mentioned but missing pages: {', '.join(missing_resources)}")
        else:
            print("No missing resource pages detected.")
            return

        # Create stub pages for missing resources
        stubs_created = 0
        for resource_id in missing_resources:
            # Skip resources with invalid characters (only allow alphanumeric, hyphen, and underscore)
            # Note: We now handle dots separately to support resource.product format
            if not all(c.isalnum() or c in '-_' for c in resource_id):
                print(
                    f"Skipping creation of stub for resource '{resource_id}' due to invalid characters")
                continue

            # Create the directory if it doesn't exist
            resource_dir = ROOT / "resource" / resource_id
            resource_dir.mkdir(parents=True, exist_ok=True)

            # Check if the main resource file already exists
            resource_file = resource_dir / f"{resource_id}.md"
            if resource_file.exists():
                print(
                    f"Resource file {resource_file} already exists, checking for missing products")

                # If this resource has associated products, make sure they exist
                if resource_id in resource_product_map:
                    try:
                        # Load existing resource metadata
                        (metadata, md) = load_md(resource_file)
                        if "products" not in metadata:
                            metadata["products"] = []
                        elif not isinstance(metadata["products"], list):
                            # Convert to list if it's not already
                            metadata["products"] = [metadata["products"]
                                                    ] if metadata["products"] else []

                        # Make sure dates are in the correct format
                        if "creation_date" not in metadata:
                            metadata["creation_date"] = datetime.datetime.now().strftime(
                                "%Y-%m-%dT00:00:00Z")
                        if "last_modified_date" not in metadata:
                            metadata["last_modified_date"] = datetime.datetime.now().strftime(
                                "%Y-%m-%dT00:00:00Z")

                        # Normalize dates
                        metadata = normalize_date_fields(metadata)

                        # Get existing product IDs
                        existing_product_ids = set()
                        for prod in metadata["products"]:
                            if isinstance(prod, dict) and "id" in prod:
                                existing_product_ids.add(prod["id"])

                        # Add missing stub products
                        added_products = 0
                        for product_id in resource_product_map[resource_id]:
                            if product_id not in existing_product_ids:
                                # Create a stub product
                                stub_product = {
                                    "id": product_id,
                                    "name": f"{product_id.capitalize()} (Stub)",
                                    "description": f"Automatically generated stub product. Please update with accurate information.",
                                    "category": "DataModelProduct"  # Default category, can be updated later
                                }
                                metadata["products"].append(stub_product)
                                added_products += 1

                        if added_products > 0:
                            print(f"Added {added_products} stub products to {resource_id}")
                            # Write updated metadata back to file
                            with open(resource_file, "w") as f:
                                f.write("---\n")
                                yaml.dump(metadata, f)
                                f.write("---\n")
                                f.write(md)
                    except Exception as e:
                        print(f"Error updating products for {resource_id}: {str(e)}")

                continue

            print(f"Creating stub Resource page for {resource_id}")

            # Create a minimal resource stub
            stub_content = {
                "layout": "resource_detail",
                "activity_status": "active",
                "id": resource_id,
                "name": resource_id.capitalize(),
                "description": f"Stub Resource page for {resource_id}. This page was automatically generated because it was referenced by other resources.",
                "domains": ["stub"],  # Use 'stub' domain to identify auto-generated pages
                "category": "DataSource",  # Default category
                "warnings": [
                    "This is an automatically generated stub page. Please replace with accurate information about this resource."
                ],
                "creation_date": datetime.datetime.now().strftime("%Y-%m-%dT00:00:00Z"),
                "last_modified_date": datetime.datetime.now().strftime("%Y-%m-%dT00:00:00Z")
            }

            # Add any referenced products as stubs
            if resource_id in resource_product_map:
                stub_content["products"] = []
                for product_id in resource_product_map[resource_id]:
                    stub_product = {
                        "id": product_id,
                        "name": f"{product_id.capitalize()} (Stub)",
                        "description": f"Automatically generated stub product. Please update with accurate information.",
                        "category": "DataModelProduct"  # Default category, can be updated later
                    }
                    stub_content["products"].append(stub_product)
                print(
                    f"Added {len(resource_product_map[resource_id])} stub products to new resource {resource_id}")

            # Write the stub page using the same YAML handler for consistency
            try:
                with open(resource_file, "w") as f:
                    f.write("---\n")
                    yaml.dump(stub_content, f)
                    f.write("---\n")
                    f.write(
                        f"\n# {resource_id.capitalize()}\n\nThis is an automatically generated stub page for {resource_id}. Please update with proper information.\n")
                stubs_created += 1
            except Exception as e:
                print(f"Error creating stub page for {resource_id}: {str(e)}")

        print(f"Created {stubs_created} stub resource pages")

    def update_stub_domains(objs):
        """
        Update the domains of existing stub resource pages from 'other' to 'stub'.
        This helps identify automatically generated pages vs. manually created ones.
        """
        updated_count = 0
        for obj in objs:
            # Check if this is likely a stub page
            if "domains" in obj and "warnings" in obj:
                is_stub = False
                # Check if warnings contains the stub warning message
                for warning in obj["warnings"]:
                    if "automatically generated stub page" in warning:
                        is_stub = True
                        break

                # If it's a stub and using 'other' domain, update it to 'stub'
                if is_stub and "domains" in obj and obj["domains"] == ["other"]:
                    # Update the domain in the in-memory object
                    obj["domains"] = ["stub"]

                    # Update the resource page file
                    fn = f"resource/{obj['id']}/{obj['id']}.md"
                    try:
                        (metadata, md) = load_md(fn)
                        if "domains" in metadata and metadata["domains"] == ["other"]:
                            metadata["domains"] = ["stub"]
                            with open(fn, "w") as f:
                                f.write("---\n" + yaml.dump(metadata) + "---\n" + md)
                            updated_count += 1
                            print(
                                f"Updated domain for stub resource {obj['id']} from 'other' to 'stub'")
                    except Exception as e:
                        print(f"Error updating domain for resource {obj['id']}: {str(e)}")

        if updated_count > 0:
            print(f"Updated domains for {updated_count} stub resources from 'other' to 'stub'")
        else:
            print("No stub resources needed domain updates")

    def propagate_products(objs):
        """
        Propagates derived products to their source Resource pages.
        For example, if the page for Aggregator A lists a product from Source S,
        then the page for Source S should list Aggregator A's version of it as a derived product.
        Also removes duplicate products (with the same ID) from Resource pages.
        """

        to_be_propagated = {}

        # Search for applicable derived products first
        for obj in objs:
            if "products" in obj:
                for product in obj["products"]:
                    for field_name in ["original_source", "secondary_source"]:
                        if field_name in product:
                            for resource_id in product[field_name]:
                                if resource_id != obj["id"]:
                                    if resource_id not in to_be_propagated:
                                        to_be_propagated[resource_id] = []
                                    to_be_propagated[resource_id].append(deepcopy(product))
        print(
            f"Found {len(to_be_propagated)} resources with products to propagate: {', '.join(to_be_propagated.keys())}")

        # Remove duplicate products from all resources first
        for obj in objs:
            if "products" in obj and len(obj["products"]) > 0:
                # Deduplicate products based on ID
                unique_products = []
                product_ids = set()

                for product in obj["products"]:
                    if "id" in product:
                        product_id = product["id"]
                        if product_id not in product_ids:
                            product_ids.add(product_id)
                            unique_products.append(product)
                    else:
                        # For products without ID, keep them all
                        unique_products.append(product)

                # If we removed any duplicates, update the products list
                if len(unique_products) < len(obj["products"]):
                    print(
                        f"Removed {len(obj['products']) - len(unique_products)} duplicate products from {obj['id']}")
                    obj["products"] = unique_products

                    # Update the resource page file
                    fn = f"resource/{obj['id']}/{obj['id']}.md"
                    try:
                        (metadata, md) = load_md(fn)
                        if "products" in metadata:
                            # Ensure products is a list
                            if not isinstance(metadata["products"], list):
                                metadata["products"] = [metadata["products"]
                                                        ] if metadata["products"] else []

                            # Deduplicate the products in the metadata
                            unique_metadata_products = []
                            metadata_product_ids = set()

                            for product in metadata["products"]:
                                if isinstance(product, dict) and "id" in product:
                                    product_id = product["id"]
                                    if product_id not in metadata_product_ids:
                                        metadata_product_ids.add(product_id)
                                        unique_metadata_products.append(product)
                                else:
                                    # For products without ID, keep them all
                                    unique_metadata_products.append(product)

                            if len(unique_metadata_products) < len(metadata["products"]):
                                metadata["products"] = unique_metadata_products
                                with open(fn, "w") as f:
                                    f.write("---\n" + yaml.dump(metadata) + "---\n" + md)
                    except Exception as e:
                        print(f"Error updating resource file {fn}: {str(e)}")

        # Now update the concatenated list of resources
        # And write newly added products to their respective Resource pages
        print("Cross-resource references:")
        print("Resource Name\tCount of products referencing")
        for obj in objs:
            if obj["id"] in to_be_propagated:
                print(f"{obj['id']}\t{len(to_be_propagated[obj['id']])}")

                total_written = 0

                if "products" not in obj:
                    obj["products"] = []

                # Do the writing here
                for product in to_be_propagated[obj["id"]]:
                    # Check if a product with the same ID already exists
                    product_exists = False
                    if "id" in product:
                        product_id = product["id"]
                        # Check in the concatenated list of resources
                        for existing_product in obj["products"]:
                            if "id" in existing_product and existing_product["id"] == product_id:
                                product_exists = True
                                break

                        if not product_exists:
                            obj["products"].append(product)
                            total_written += 1
                    else:
                        # Fall back to full object comparison if no ID exists
                        if product not in obj["products"]:
                            obj["products"].append(product)
                            total_written += 1

                    # Write to the respective Resource page
                    fn = f"resource/{obj['id']}/{obj['id']}.md"
                    (metadata, md) = load_md(fn)
                    if "products" not in metadata:
                        metadata["products"] = []
                    elif not isinstance(metadata["products"], list):
                        metadata["products"] = [metadata["products"]
                                                ] if metadata["products"] else []

                    # Check if a product with the same ID already exists in the Resource page
                    metadata_product_exists = False
                    if "id" in product:
                        product_id = product["id"]
                        for existing_product in metadata["products"]:
                            if isinstance(existing_product, dict) and "id" in existing_product and existing_product["id"] == product_id:
                                metadata_product_exists = True
                                break

                        if not metadata_product_exists:
                            metadata["products"].append(product)
                            with open(fn, "w") as f:
                                f.write("---\n" + yaml.dump(metadata) + "---\n" + md)
                    else:
                        # Fall back to full object comparison if no ID exists
                        if product not in metadata["products"]:
                            metadata["products"].append(product)
                            with open(fn, "w") as f:
                                f.write("---\n" + yaml.dump(metadata) + "---\n" + md)

                if total_written > 0:
                    print(f" Wrote {str(total_written)} product(s) to {obj['id']} entry")

    def create_evaluation_pages(objs):
        """
        Read evals/evals.tsv and, for each resource ID in the first column, create an
                evaluation markdown page at resource/<id>/<id>_eval.md with layout eval_detail.
                Expected format:
                    - Row 1: grouping categories for questions (columns 2..N)
                    - Row 2: individual question headers (columns 2..N)
                    - Rows 3..: data rows where column 1 is the resource ID and columns 2..N are answers

                Behavior:
                    - Group questions by their category and render a separate table per category
                    - Color cells with answers that begin with 'Y'/'Yes' green and 'N'/'No' red
                    - Annotate the in-memory resource object with an 'evaluation_page' field
                    - Insert a small markdown link to the evaluation page into the resource markdown if missing
        """
        evals_path = ROOT / 'evals' / 'evals.tsv'
        if not evals_path.exists():
            print("No evals/evals.tsv found; skipping evaluation page generation")
            return

        # Build a quick index of resources by id
        resources_by_id = {obj.get('id'): obj for obj in objs if obj.get('id')}

        created = 0
        updated_links = 0
        with open(evals_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='\t')
            rows = list(reader)
            if not rows:
                print("evals.tsv is empty; nothing to do")
                return
            if len(rows) == 1:
                print("evals.tsv has only one row; need at least two header rows and one data row")
                return

            group_headers = rows[0]
            question_headers = rows[1]

            # Load human-readable question titles mapping from eval_descriptions.tsv (if present)
            descriptions = {}
            desc_path = ROOT / 'evals' / 'eval_descriptions.tsv'
            if desc_path.exists():
                try:
                    with open(desc_path, 'r', newline='', encoding='utf-8') as df:
                        d_reader = csv.reader(df, delimiter='\t')
                        for d_row in d_reader:
                            if not d_row or len(d_row) < 2:
                                continue
                            k = (d_row[0] or '').strip()
                            v = (d_row[1] or '').strip()
                            if not k or not v:
                                continue
                            # Skip header-like rows
                            kl = k.lower()
                            vl = v.lower()
                            if kl in ('id', 'key', 'question', 'field') and vl in ('description', 'label', 'title'):
                                continue
                            descriptions[k] = v
                except Exception as e:
                    print(f"WARN: could not read eval_descriptions.tsv: {e}")

            def humanize_identifier(s: str) -> str:
                t = (s or '').strip()
                if not t:
                    return ''
                t = t.replace('_', ' ')
                t = t.title()
                # Fix common acronyms
                t = t.replace('Kg', 'KG').replace('Api', 'API').replace(
                    'Id', 'ID').replace('Ids', 'IDs')
                return t

            def display_title(key: str) -> str:
                return descriptions.get(key, humanize_identifier(key))

            # Forward-fill empty group headers so blanks inherit the previous non-empty category
            filled_group_headers = list(group_headers)
            last = ''
            for i in range(len(filled_group_headers)):
                current = (filled_group_headers[i] or '').strip()
                if current:
                    last = current
                else:
                    filled_group_headers[i] = last

            # Helper to compute style for a given answer value
            def style_for_value(val: str) -> str:
                v = (val or '').strip().lower()
                if v.startswith('y') or v.startswith('yes'):
                    return 'background-color:#d4edda;'
                if v.startswith('n') or v.startswith('no'):
                    return 'background-color:#f8d7da;'
                return ''

            # Helper to escape HTML and linkify URLs
            def linkify_and_escape(s: str) -> str:
                import re
                import html
                if not s:
                    return ''
                pattern = re.compile(r'(https?://[^\s<>\"]+)')
                parts = []
                last = 0
                for m in pattern.finditer(s):
                    parts.append(html.escape(s[last:m.start()]))
                    url = m.group(1)
                    url_esc = html.escape(url)
                    parts.append(f'<a href="{url_esc}">{url_esc}</a>')
                    last = m.end()
                parts.append(html.escape(s[last:]))
                return ''.join(parts)

            # Clean comment: drop leading boolean marker and surrounding parentheses
            def clean_comment(c: str) -> str:
                import re
                if not c:
                    return ''
                txt = c.strip()
                # Remove leading boolean answer tokens (Y/N/Yes/No) with optional punctuation and spaces
                txt = re.sub(r'^\s*(yes|y|no|n)\b[\s:;\-–—]*', '', txt, flags=re.IGNORECASE)
                # Remove leading single letter (Y/N), comma, and space (e.g., "Y, foo")
                txt = re.sub(r'^[YyNn],\s+', '', txt)
                # Remove any leading commas and spaces (e.g., ", foo" or ",,  foo")
                txt = re.sub(r'^[,\s]+', '', txt)
                txt = txt.strip()
                # If wrapped in a single pair of parentheses, remove them
                if len(txt) >= 2 and txt[0] == '(' and txt[-1] == ')':
                    txt = txt[1:-1].strip()
                # Capitalize first letter if not empty
                if txt:
                    txt = txt[0].upper() + txt[1:]
                return txt

            # Ensure first column is ID; iterate over data rows
            for row in rows[2:]:
                if not row or len(row) == 0:
                    continue
                rid = (row[0] or '').strip()
                if not rid:
                    continue
                # Only proceed if this resource exists
                res_dir = ROOT / 'resource' / rid
                res_file = res_dir / f"{rid}.md"
                if not res_file.exists():
                    print(
                        f"WARN: evaluation provided for '{rid}' but no resource page found; skipping")
                    continue

                # Group questions by category, collapsing paired *_text comment columns with their boolean
                from collections import OrderedDict
                # cat -> OrderedDict[base_question] -> {question, answer, comment}
                grouped = OrderedDict()
                col_limit = min(len(filled_group_headers), len(question_headers), len(row))
                # Optional per-row metadata
                evaluator_val = ''
                evaluation_date_val = ''
                for i in range(1, col_limit):  # skip ID column
                    cat = (filled_group_headers[i] or '').strip()
                    q = (question_headers[i] or '').strip()
                    v = (row[i] or '').strip()
                    if not q and not v:
                        continue
                    # Special-case metadata fields that should not appear in grouped tables
                    q_norm = (q or '').strip().lower()
                    if q_norm == 'evaluator':
                        evaluator_val = v
                        continue
                    if q_norm in ('evaluation_date', 'evaluation date', 'date'):
                        evaluation_date_val = v
                        continue
                    # Determine base question id and if this is a comment column
                    is_comment = False
                    base_q = q
                    if q.endswith('_text'):
                        is_comment = True
                        base_q = q[:-5]

                    if cat not in grouped:
                        grouped[cat] = OrderedDict()
                    if base_q not in grouped[cat]:
                        grouped[cat][base_q] = {
                            'question': base_q,
                            'answer': '',
                            'comment': ''
                        }
                    if is_comment:
                        grouped[cat][base_q]['comment'] = v
                    else:
                        grouped[cat][base_q]['answer'] = v

                # Default evaluation date to today if not supplied
                if not evaluation_date_val:
                    evaluation_date_val = datetime.date.today().isoformat()
                if not evaluator_val:
                    evaluator_val = 'Not specified'

                # Build HTML content (layout will render title and metadata)
                html_lines = []
                for cat, qmap in grouped.items():
                    if cat:
                        html_lines.append(f"## {cat}")
                    html_lines.append("<div class=\"table-responsive\">")
                    html_lines.append("<table class=\"table table-striped\">")
                    html_lines.append(
                        "<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>")
                    yes_count = 0
                    answered_count = 0
                    for base_q, entry in qmap.items():
                        q_val = display_title(entry.get('question', ''))
                        a_val = entry.get('answer', '')
                        c_val = clean_comment(entry.get('comment', ''))
                        # Escape and linkify
                        q_esc = linkify_and_escape(q_val or '')
                        a_esc = linkify_and_escape(a_val or '')
                        c_esc = linkify_and_escape(c_val or '')
                        style = style_for_value(a_val)
                        style_attr = f" style=\"{style}\"" if style else ""
                        v_norm = (a_val or '').strip().lower()
                        if v_norm:
                            answered_count += 1
                            if v_norm.startswith('y') or v_norm.startswith('yes'):
                                yes_count += 1
                        html_lines.append(
                            f"<tr><td>{q_esc}</td><td{style_attr}>{a_esc}</td><td>{c_esc}</td></tr>")
                    html_lines.append("</tbody></table></div>")
                    # Section score (skip for License Information)
                    if (cat or '').strip().lower() != 'license information':
                        html_lines.append(
                            f"<p><strong>Section Score:</strong> {yes_count}/{answered_count}</p>")
                    html_lines.append("")
                content = "\n".join(html_lines) + "\n"

                # Write the evaluation page
                eval_md_path = res_dir / f"{rid}_eval.md"
                with open(eval_md_path, 'w', encoding='utf-8') as ef:
                    # Include evaluator and evaluation_date in front matter for downstream use
                    fm = {
                        'layout': 'eval_detail',
                        'evaluator': evaluator_val or None,
                        'evaluation_date': evaluation_date_val,
                    }
                    # Remove None fields to keep front matter clean
                    fm = {k: v for k, v in fm.items() if v is not None}
                    ef.write("---\n")
                    yaml.dump(fm, ef)
                    ef.write("---\n\n")
                    ef.write(content)
                created += 1

                # Annotate the in-memory object so the table can render an icon/link
                if rid in resources_by_id:
                    resources_by_id[rid]['evaluation_page'] = f"resource/{rid}/{rid}_eval.html"

                # Insert a link into the resource markdown content if missing
                try:
                    (metadata, md) = load_md(res_file)
                    link_snippet = f"[{rid} evaluation]({rid}_eval.html)"
                    if link_snippet not in md:
                        md_update = md.rstrip() + "\n\n## Evaluation\n\n- View the evaluation: " + link_snippet + "\n"
                        with open(res_file, 'w', encoding='utf-8') as rf:
                            rf.write("---\n")
                            yaml.dump(metadata, rf)
                            rf.write("---\n")
                            rf.write(md_update)
                        updated_links += 1
                except Exception as e:
                    print(
                        f"WARN: could not update resource page for {rid} with evaluation link: {e}")

        print(f"Created {created} evaluation page(s); updated {updated_links} resource page link(s)")

    objs = []
    foundry = []
    library = []
    obsolete = []
    cfg = {}
    if args.include:
        with open(args.include, "r") as f:
            cfg = yaml.load(f.read(), Loader=yaml.SafeLoader)
    for fn in args.files:
        (obj, md) = load_md(fn)
        # Normalize date fields to ISO 8601 format
        obj = normalize_date_fields(obj)
        # Check if the object is actually a product
        if obj.get("id") == pathlib.Path(fn).parent.name:
            library.append(obj)
    objs = foundry + library + obsolete
    cfg["resources"] = objs

    # Deduplicate similar product warnings (keep most recent)
    dedupe_product_warnings(objs)

    # Generate product pages
    generate_product_pages(objs)

    # Create stub pages for resources mentioned in products but don't have a page yet
    create_stub_resource_pages(objs)

    # Propagate derived products to the source Resource pages
    propagate_products(objs)

    # Add logos to licenses
    decorate_metadata(objs)

    # Update domains of existing stub resources
    update_stub_domains(objs)

    # Generate evaluation pages from evals/evals.tsv and annotate resources
    create_evaluation_pages(objs)

    with open(args.output, "w") as f:
        f.write(yaml.dump(cfg))
    return cfg


def load_md(fn):
    """
    Load a yaml text blob from a markdown file and parse the blob.

    Returns a tuple (yaml_obj, markdown_text)
    """
    onto_stuff = frontmatter.load(fn)
    return (onto_stuff.metadata, onto_stuff.content)


def get_YAML_text(fn):
    with open(fn, "r") as f:
        text = f.read()
        chunks = text.split("---")
        yamltext = chunks[1].strip()
        return yamltext


def normalize_date_fields(obj):
    """
    Normalize date fields to ISO 8601 format with time and timezone.

    This function ensures that date fields like creation_date and last_modified_date
    are in the format expected by the schema (e.g., '2024-02-12T00:00:00Z').
    If a date is just a date string (e.g., '2024-02-12'), it adds time and timezone.
    """
    date_fields = ['creation_date', 'last_modified_date']

    for field in date_fields:
        if field in obj and obj[field]:
            date_value = obj[field]
            # If it's already in the correct format (contains T and Z), leave it as is
            if isinstance(date_value, str) and 'T' in date_value and date_value.endswith('Z'):
                continue

            # If it's a date string without time, add time and timezone
            if isinstance(date_value, str) and len(date_value) >= 10:
                # Extract just the date part in case there are quotes or other characters
                date_part = date_value.strip('"\'')
                if len(date_part) >= 10:  # At least YYYY-MM-DD
                    date_part = date_part[:10]  # Just take YYYY-MM-DD part
                    obj[field] = f"{date_part}T00:00:00Z"

    # Recursively process nested objects
    for key, value in obj.items():
        if isinstance(value, dict):
            normalize_date_fields(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    normalize_date_fields(item)

    return obj


def _load_allowed_domains_from_schema() -> set[str]:
    """Load DomainEnum permissible values from the generated JSON schema.

    Falls back to empty set if the schema file is missing or malformed.
    """
    try:
        with open(SCHEMA_PATH, "r") as f:
            schema = json.load(f)
        defs = schema.get("$defs") or schema.get("definitions") or {}
        domain_def = defs.get("DomainEnum", {})
        # LinkML JSON Schema encodes enums as oneOf with const per value
        allowed = set()
        if "enum" in domain_def:
            allowed = set(domain_def["enum"])  # rare, but support if present
        else:
            for item in domain_def.get("oneOf", []):
                const = item.get("const")
                if isinstance(const, str):
                    allowed.add(const)
        return allowed
    except Exception:
        return set()


def sanitize_domains(obj):
    """Remove any domain entries not present in DomainEnum.

    - Expects obj to be a dict with optional 'domains': list[str]
    - Returns the same dict instance after in-place filtering.
    """
    allowed = _load_allowed_domains_from_schema()
    if not allowed:
        return obj

    def _filter_in_place(d):
        if isinstance(d, dict):
            # Only filter top-level 'domains' on Resource objects; avoid altering nested keys with same name
            if d is obj and isinstance(d.get("domains"), list):
                d["domains"] = [x for x in d["domains"] if isinstance(x, str) and x in allowed]
            # Recurse to children but do not filter nested 'domains' occurrences to keep scope tight
            for v in d.values():
                if isinstance(v, dict):
                    _filter_in_place(v)
                elif isinstance(v, list):
                    for it in v:
                        if isinstance(it, dict):
                            _filter_in_place(it)

    _filter_in_place(obj)
    return obj


def coerce_string_like_fields(obj):
    """
    Coerce certain scalar fields to be serialized as double-quoted strings.

    This is primarily to ensure YAML numeric-looking values (e.g., 1990) intended
    to be strings are quoted (e.g., "1990") so they validate correctly and remain
    strings on subsequent parses.

    Fields coerced (by key name, anywhere in the object):
      - year
      - version
      - latest_version
      - versions (list: each item coerced)
    """
    # Keys that should always be treated as strings (force quoted)
    scalar_keys_force_quote = {
        "year",
        "version",
        "latest_version",
        "id",
        "fairsharing_id",
        "infores_id",
        "doi",
        "value",
    }
    list_keys_force_quote = {"versions"}

    def _coerce_in_place(d):
        if isinstance(d, dict):
            for k, v in list(d.items()):
                # Recurse first into nested structures
                if isinstance(v, dict):
                    _coerce_in_place(v)
                elif isinstance(v, list):
                    if k in list_keys_force_quote:
                        new_list = []
                        for item in v:
                            if isinstance(item, (int, float)):
                                new_list.append(DQ(str(item)))
                            elif isinstance(item, str):
                                # Force quotes even if already string
                                new_list.append(DQ(item))
                            else:
                                new_list.append(item)
                        d[k] = new_list
                    else:
                        for item in v:
                            _coerce_in_place(item)
                else:
                    if k in scalar_keys_force_quote and v is not None:
                        if isinstance(v, (int, float)):
                            d[k] = DQ(str(v))
                        elif isinstance(v, str):
                            # Force quotes even if already string
                            d[k] = DQ(v)
        elif isinstance(d, list):
            for item in d:
                _coerce_in_place(item)

    _coerce_in_place(obj)
    return obj


if __name__ == "__main__":
    main()
