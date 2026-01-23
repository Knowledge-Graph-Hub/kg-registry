This repository contains the source code for the Knowledge Graph Registry, which is a collection of resources and tools for managing and sharing metadata about knowledge graphs and their relationships.

## General Guidelines for Adding Resources and Products
When adding new resources, always follow the schema in `src/kg_registry/kg_registry_schema/schema/kg_registry_schema.yaml`.

Follow the schema, including all enums (for fields using enums, do not create values not present in the acceptable values for the enum).

Do not create new categories. Use the classes defined in the schema.

Do not change any contents of the `registry` directory, as these are automatically generated from Makefile targets.

Do not create new files for Product entries, as these are automatically generated based on their corresponding Resource entries.

Use the contents of the `resource` directory for examples of Resource entries.

When creating new Resource entries or updating stub entries, ensure that you include at least one entry for the Products field.

If a Product mentions another Resource in its description, find the ID of that Resource and include it in the Product's `original_source` field. For example, if a product is described as "A mapping file to WikiPathways", then the `original_source` list for this Product should include `wikipathways`.

For new products, if you cannot identify an appropriate category, use "Product". There is no such category as "DataProduct".

The `creation_date` field refers to the date our metadata page was created, not the date of creation of the described resource.

The `last_modified_date` field refers to today's date, not any date corresponding to the described resource.

New date fields should be set to today's date.

Don't fill out the `curators` field as this is specific to the KG-Registry team.

You can use the existing uv-managed environment to validate Resource or Product pages (precede any `make` command with `uv run`).

Note that ToolResource is not a valid category.

## How to Do a Quick Curation

1. Find all stub Resource pages (they'll have `stub` in their `domains` list).

2. Select one of these stub pages at random. If it is already mentioned in the curation problems log (see `reports/curation_problems.tsv`), skip it and select another.

3. Find information about the Resource. There may already be a `homepage_url`, which is a good place to start, but a literature search may also be helpful. 

4. Expand the Resource page. Consult the schema and other pages as examples. Remember to include products, but you don't need to create the individual Product pages - those get generated later. You don't need to remove Products already on the page, as they may be present if another Resource references this one. If you encounter enough problems during curation to prevent you from completing the curation, log them in `reports/curation_problems.tsv` and move on to another Resource.

5. Validate the new page (with the makefile target `validate-file`). Correct any validity issues before continuing.

6. Repeat (return to step 2) until you have curated at least 5 Resources.
