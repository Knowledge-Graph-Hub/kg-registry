---
name: kg-registry-validation
description: Use when validating or quality-checking KG-Registry resource pages after curation, especially for schema compliance, provenance slot correctness, and stub-cleanup issues.
---

# kg-registry-validation

Validate a KG-Registry resource page after editing, with extra attention to provenance and curation-specific quality issues.

## When to use

- After curating or expanding a resource page.
- When a resource file fails `validate-file`.
- When reviewing whether `original_source` and `secondary_source` were filled correctly.
- When checking that a stub was fully converted into a curated page.

Skip when:

- The task is general application testing unrelated to resource metadata.
- The task is schema authoring or code changes outside `resource/`.

## Inputs

- Required: a specific resource file path such as `resource/<id>/<id>.md`.
- Optional: a related concern to emphasize, such as provenance, dates, products, or stub cleanup.

## Workflow

1. Validate the file structurally.
   - Run:
     ```bash
     uv run make validate-file FILE=resource/<id>/<id>.md
     ```
   - If the file needs formatting cleanup, run:
     ```bash
     uv run make prettify-file FILE=resource/<id>/<id>.md
     uv run make validate-file FILE=resource/<id>/<id>.md
     ```

2. Check curation-specific quality rules that matter even when schema validation passes.
   - Confirm the file remains under `resource/` and not `registry/`.
   - Confirm the page still has at least one `products` entry.
   - Confirm `last_modified_date` reflects today for the curation edit.
   - Confirm `curators` was not filled in.
   - If the page was formerly a stub, confirm `domains: [stub]`, placeholder warnings, and stub prose were removed or replaced appropriately.

3. Check provenance fields carefully.
   - Inspect each product's `original_source` and `secondary_source`.
   - Each provenance entry must be a `SourceAssociation` object with both:
     - `source`
     - `relation_type`
   - `source` must be a KG-Registry resource ID or product ID, not a URL, INFORES ID, or descriptive label.
   - Use `prov:hadPrimarySource` as the default relation for `original_source`.
   - Use `prov:wasInfluencedBy` as the default relation for `secondary_source` when no more specific PROV-O relation is known.
   - Use `prov:wasDerivedFrom` when the product is transformed or repackaged from another source.
   - Use `prov:wasInformedBy` when another source influenced curation without being a direct derivation input.
   - Confirm directly owned products include the parent resource in `original_source`.
   - Confirm the parent resource is not redundantly listed in `secondary_source` for its own direct products.

4. Check referenced IDs for resolvability and intent.
   - When a provenance `source` references an existing KG-Registry resource, verify that the identifier matches the real registry ID.
   - When a provenance `source` references a not-yet-existing upstream resource, confirm the newly minted ID is unique, stable, and filename-safe.
   - A missing referenced ID can be acceptable during curation if it is an intentional new KG-Registry identifier. The tooling can later generate a stub page for it.
   - Do not silently replace a valid missing intended source ID with a raw URL or free-text label just to avoid creating a new identifier.

5. If validation fails, repair locally and rerun.
   - Fix the same file first.
   - Rerun `uv run make validate-file FILE=...` after each substantive fix.

## Quick reference

| Task | Command |
|------|---------|
| Validate one file | `uv run make validate-file FILE=resource/<id>/<id>.md` |
| Prettify then validate | `uv run make prettify-file FILE=resource/<id>/<id>.md && uv run make validate-file FILE=resource/<id>/<id>.md` |
| Find provenance slots in a file | `rg -n 'original_source|secondary_source|relation_type' resource/<id>/<id>.md` |

## Common mistakes

- Treating schema validation success as sufficient even when stub warnings or placeholder prose remain.
- Writing provenance as strings or labels instead of `SourceAssociation` objects.
- Using URLs or INFORES IDs in `source` instead of KG-Registry IDs.
- Forgetting that directly owned products should name their parent resource in `original_source`.
- Deleting a legitimate newly minted source ID because it does not yet have a page.

## Relationship to other skills

- `kg-registry-curation` is the editing workflow.
- `curate-next` dispatches batches of curation tasks that should finish with this validation workflow.