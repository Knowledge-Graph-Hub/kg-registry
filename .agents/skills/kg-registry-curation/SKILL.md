---
name: kg-registry-curation
description: Use when curating or expanding a KG-Registry resource page. Applies to stub resources and incomplete existing pages stored as Markdown with YAML front matter under resource/.
---

# kg-registry-curation

Curate a single KG-Registry resource page end to end.

## Prerequisite

- Run this skill only from a local clone of the KG-Registry repository.
- The workflow depends on reading and editing files under `resource/`, consulting local repository context, and running local validation commands.
- If the repository is not cloned locally, stop and clone it before attempting curation.

## When to use

- The user names a specific resource to curate.
- The user asks to expand a stub entry in `resource/`.
- The user asks to improve metadata completeness for one existing resource page.
- A batch workflow has already selected a specific target file and now needs the single-resource curation procedure.

Skip when:

- The task is about generated outputs under `registry/`.
- The task is about schema code changes rather than resource metadata.
- The task is about creating standalone Product pages. KG-Registry product pages are generated automatically from the parent Resource entry.

## Inputs

- Required: a resource identifier, resource name, or direct resource file path.
- Preferred final target: exactly one file under `resource/<id>/<id>.md`.

If the input is ambiguous, resolve it before editing. Do not guess between multiple candidate resources.

## Workflow

1. Resolve the target file.
   - If the user gave a path, use it directly.
   - If the user gave an ID or name, find the matching file under `resource/`.
   - Read the current file first and confirm whether it is a stub or an incomplete curated page.

2. Confirm the governing constraints before editing.
   - Follow the LinkML schema in `src/kg_registry/kg_registry_schema/schema/kg_registry_schema.yaml`.
   - Do not invent enum values, categories, or product types not present in the schema.
   - Do not edit anything under `registry/`; those files are generated.
   - Do not create standalone Product files.
   - Ensure the resource retains at least one `products` entry.
   - Do not fill in the `curators` field.
   - Treat `creation_date` as the date the KG-Registry metadata page was created.
   - Set `last_modified_date` to today when making updates.

3. Gather only the minimum evidence needed for this resource.
   - Start from the page's existing metadata, especially `homepage_url`, `repository`, existing products, publications, and warnings.
   - Use similar curated files in `resource/` as structural examples.
   - Prefer the resource homepage, project documentation, repository, and authoritative download/API pages over broad research.
   - Expect web search to be necessary for many stubs and incomplete pages. Use it early when the current page does not already provide enough authoritative information.
   - When you use web search, prefer authoritative sources first: the project homepage, official documentation, maintained repository, release pages, papers, and organizational pages that directly own the resource.

4. Expand or correct the YAML front matter.
   - Keep the file as Markdown with YAML front matter; do not convert it to `.yaml`.
   - Replace stub text and warnings with real metadata when possible.
   - Keep `layout: resource_detail` unless the file already uses a different valid resource layout.
   - Use an existing schema class for `category`.
   - Add or improve fields such as `description`, `homepage_url`, `repository`, `license`, `contacts`, `publications`, `domains`, `tags`, `taxon`, and `products` when supported by evidence.
   - Preserve useful existing products. Do not remove valid products just because the page began as a stub.
   - Fill `original_source` and `secondary_source` as lists of `SourceAssociation` objects with both `source` and `relation_type`.
   - Use KG-Registry identifiers in `source`, not homepage URLs, INFORES IDs, free text labels, or citations.
   - When the source is another resource already present in KG-Registry, use that resource's KG-Registry ID.
   - When the source is a specific product rather than the whole resource, use the KG-Registry product ID if it already exists.
   - If a referenced source does not already exist in KG-Registry, you may mint a new KG-Registry resource ID as long as it is unique, stable, and filename-safe. The build tooling can generate a new stub page for that referenced ID later.
   - Prefer lowercase identifiers using the repository's existing conventions. Avoid spaces and punctuation other than hyphen or underscore unless an established local pattern already exists.
   - `original_source` is for the direct primary source or sources of the product. The default relation type is `prov:hadPrimarySource`.
   - `secondary_source` is for additional upstream influences, aggregators, or contextual sources that affected the product without being the primary source. The default relation type is `prov:wasInfluencedBy`.
   - Use a more specific allowed PROV-O relation when the provenance is clear. In practice, `prov:wasDerivedFrom` fits transformed or re-packaged products and `prov:wasInformedBy` fits informative but indirect inputs.
   - Keep the parent resource itself in `original_source` for products that are owned directly by that resource.
   - Do not place the parent resource in `secondary_source` when it is the direct owner of the product.
   - If a product description mentions another Resource as an upstream input, represent that relationship in provenance rather than burying it only in prose.
   - If no specialized product category is clearly appropriate, use `Product`.

5. Update the Markdown body only as needed.
   - Replace placeholder stub prose with a concise human-readable summary.
   - Keep any hand-written sections that remain accurate.
   - Avoid duplicating every field from front matter in prose.

6. Prettify and validate the file.
   - Consult the `kg-registry-validation` skill for validation and quality checks.
   - Run `uv run make prettify-file FILE=<target-file>` after editing when formatting needs normalization.
   - Run `uv run make validate-file FILE=<target-file>` before finishing.
   - Fix validation errors in the same file before stopping.

7. If curation is blocked, handle it explicitly.
   - If you cannot complete the page because the resource lacks a resolvable homepage, has insufficient public documentation, or cannot be confidently identified, add an entry to `reports/curation_problems.tsv`.
   - Use the columns `resource_id`, `reason`, `details`, and `date_attempted`.
   - Keep the reason short and concrete, such as `no_homepage`, `insufficient_info`, or `page_unresolvable`.
   - Do not fabricate metadata just to satisfy validation.

## Quick reference

| Task | Command |
|------|---------|
| Validate one file | `uv run make validate-file FILE=resource/<id>/<id>.md` |
| Prettify one file | `uv run make prettify-file FILE=resource/<id>/<id>.md` |
| Find stub files | `rg -l '^\s*-\s*stub\s*$' resource` |
| Check prior curation failures | `cut -f1 reports/curation_problems.tsv` |

## Common mistakes

- Editing `registry/` outputs directly instead of the source file under `resource/`.
- Converting a resource page from Markdown front matter to a standalone YAML file.
- Inventing a new resource or product category not defined by the schema.
- Creating a separate Product page file.
- Removing all existing products from a resource.
- Using free-text source names, URLs, or INFORES IDs directly in `original_source` or `secondary_source` instead of KG-Registry identifiers.
- Forgetting that missing source IDs can be intentionally minted as new unique KG-Registry IDs so later tooling can create stub pages for them.
- Using `secondary_source` where `original_source` is appropriate, or omitting the parent resource from a directly owned product's primary provenance.
- Filling in `curators` even though that field is reserved for the KG-Registry team.
- Reusing dates from the external resource for `creation_date` or `last_modified_date`.
- Leaving `domains: [stub]` in place after a successful curation.
- Skipping `uv run make validate-file FILE=...` before finishing.

## Relationship to other skills

- `curate-next` selects the next stub resources and dispatches this single-resource workflow.
- `kg-registry-validation` covers per-file validation, provenance checks, and quality-review steps after editing.
- `kg-registry-curation` is the core per-resource curation procedure.
