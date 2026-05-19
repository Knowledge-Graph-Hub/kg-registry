---
name: curate-next
description: Use when asked to curate the next N KG-Registry stub resources. Selects uncatalogued stub pages not already listed in reports/curation_problems.tsv and dispatches single-resource curation in parallel.
---

# curate-next

Curate the next N stub resources in KG-Registry.

## Prerequisite

- Run this skill only from a local clone of the KG-Registry repository.
- The workflow depends on scanning local files under `resource/`, reading `reports/curation_problems.tsv`, editing checked-out pages, and running local validation commands.
- If the repository is not cloned locally, stop and clone it before attempting batch curation.

## When to use

- "Curate the next 3 stub resources"
- "/curate-next 5"
- "Work through a batch of KG-Registry stubs"

Skip when:

- The user names a specific resource. Use the single-resource curation workflow instead.
- The task is to generate new stub pages. That is a separate maintenance flow.
- The task is purely about reviewing `reports/curation_problems.tsv` without curating pages.

## Inputs

- Required positional argument `N`: number of resources to curate.
- `N` must be a positive integer between 1 and 5 inclusive.
- If `N` is missing, non-integer, `<= 0`, or `> 5`, ask the user to clarify rather than guessing.

The cap keeps the batch small enough to curate, validate, and summarize cleanly.

## Workflow

1. Validate `N`.
   - Never default to a value the user did not provide.

2. Build the candidate stub list.
   - Find stub pages from `resource/` by looking for `stub` in the `domains` list.
   - Prefer a command such as:
     ```bash
     rg -l '^\s*-\s*stub\s*$' resource
     ```
   - Sort the results for deterministic selection.

3. Exclude resources already logged as blocked.
   - Read `reports/curation_problems.tsv` and collect the `resource_id` values from the first column.
   - Drop any candidate whose directory or file stem matches an existing blocked `resource_id`.

4. Select the next `N` candidates.
   - Use the first `N` survivors after sorting.
   - If fewer than `N` candidates remain, do not pad with blocked or non-stub files. Report the shortfall.

5. Dispatch single-resource curation.
   - For each selected resource, invoke the `kg-registry-curation` workflow.
   - If the environment supports parallel sub-agents safely, dispatch the selected resources in parallel.
   - If parallel execution is used, isolate each worker from the others before editing. Separate git worktrees are preferred for true parallel edits.
   - Keep each worker focused on one resource file and its direct validation.
   - Make it explicit in each dispatched prompt that web search will likely be necessary for stub expansion and provenance resolution.
   - Make it explicit in each dispatched prompt that `original_source` and `secondary_source` must use KG-Registry identifiers, minting a new unique KG-Registry ID when an upstream resource is referenced but not yet present in the registry.

6. Validate each curated file.
   - Each resource must pass `uv run make validate-file FILE=<target-file>` before being reported complete.
   - If prettification changes the file, validate again afterward.
   - Use the `kg-registry-validation` skill for the post-edit validation workflow when additional checking is needed.

7. Report outcomes.
   - List curated resources and whether each completed successfully.
   - List blocked resources and whether they were logged to `reports/curation_problems.tsv`.
   - State any shortfall if fewer than `N` resources were actually curated.

## Quick reference

| Task | Command |
|------|---------|
| List stub files | `rg -l '^\s*-\s*stub\s*$' resource | sort` |
| View blocked resource IDs | `cut -f1 reports/curation_problems.tsv` |
| Validate one curated file | `uv run make validate-file FILE=resource/<id>/<id>.md` |

## Common mistakes

- Treating every incomplete page as a stub. This workflow is driven specifically by `domains` containing `stub`.
- Re-curating resources already documented in `reports/curation_problems.tsv`.
- Padding the batch with arbitrary resources when fewer than `N` valid stub candidates remain.
- Dispatching multiple curations into one shared working tree without isolation.
- Dispatching workers without telling them to use web search when the stub itself lacks enough evidence.
- Letting workers write provenance with raw labels or URLs instead of KG-Registry IDs.
- Reporting success before each file has passed validation.

## Relationship to other skills

- `kg-registry-curation` performs the actual per-resource edit and validation steps.
- `kg-registry-validation` performs the focused validation and quality checks for curated files.
- `curate-next` is the batch selector and dispatcher.