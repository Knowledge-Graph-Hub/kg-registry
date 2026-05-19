---
layout: intro_doc
title: Agent Skills
---

# Agent Skills

KG-Registry includes a small set of local agent skills to support curation and maintenance workflows in this repository.

These skills are designed for curators working in a checked-out copy of the repository, not for editing generated site output or for use against the public website alone.

## Prerequisite

Before using any of these skills, clone the KG-Registry repository locally.

The skills rely on:

- reading and editing source files under `resource/`
- checking nearby repository context such as `reports/curation_problems.tsv`
- running local validation commands such as `uv run make validate-file FILE=...`

If you are not working in a local clone of the repository, stop and clone it first.

## Where the skills live

The current agent workflows are defined in the repository's `.agents/` directory.

That directory includes:

- command entry points for common tasks
- skill definitions for curation and validation workflows
- local permission settings used by the agent when running repository-specific commands

## Available workflows

### Curate a specific resource

Use the `kg-registry-curation` skill, or the matching `curate` command entry point when your agent environment supports commands.

This workflow is for expanding a stub resource or improving a specific existing resource page. It focuses on the source page under `resource/<id>/<id>.md`, expects web search when the current page is incomplete, and finishes with local validation.

### Curate the next batch of stubs

Use the `curate-next` skill, or the matching `curate-next` command entry point when available.

This workflow selects the next stub resources from the local repository, skips resources already listed in `reports/curation_problems.tsv`, and dispatches per-resource curation.

### Validate a curated resource page

Use the `kg-registry-validation` skill.

This workflow checks a curated file for schema validity and curation-specific quality issues such as placeholder stub content, missing provenance structure, missing products, or incorrect source associations.

### Update a product URL

Use the `kg-registry-product-url-update` skill.

This workflow is for replacing a stale `product_url` with the best current live URL for the same product. It is especially useful when an old version-specific URL has disappeared and the best replacement is a newer canonical page, release page, or current download endpoint.

## What these workflows assume

The agent skills are written around a few KG-Registry-specific rules:

- edit source files in `resource/`, not generated output in `registry/`
- keep resource pages as Markdown files with YAML front matter
- use the LinkML schema in `src/kg_registry/kg_registry_schema/schema/kg_registry_schema.yaml`
- validate local edits with repository commands rather than ad hoc checks
- use KG-Registry identifiers, not free text or raw URLs, in provenance slots such as `original_source` and `secondary_source`

## Typical curation loop

1. Choose a resource or product task.
2. Use the appropriate skill from the local repository clone.
3. Search authoritative web sources when the current metadata is incomplete or stale.
4. Update the source page under `resource/`.
5. Run local validation before finishing.

## When not to use these skills

These skills are not a substitute for broader project setup or site deployment instructions.

For repository setup, development, and troubleshooting, see the root-level development documentation such as `README-sitedev.md`.