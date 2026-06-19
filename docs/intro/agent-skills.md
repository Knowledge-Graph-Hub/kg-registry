---
layout: intro_doc
title: Agent Skills
---

# Agent Skills

KG-Registry includes a small set of local agent skills to support curation and maintenance workflows in this repository, plus a set of read-only discovery skills for exploring what the registry knows about a resource or domain.

The curation and maintenance skills are designed for curators working in a checked-out copy of the repository. The discovery skills are different: they need no local clone and query the published Parquet files over HTTP, so anyone with network access can use them.

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

## Discovery and exploration

These skills are read-only and need no local clone. They answer questions about what the registry already records by querying the published Parquet files over HTTP at `https://kghub.org/kg-registry/registry/parquet/` (`resources.parquet`, `resource_domains.parquet`, `resource_products.parquet`, `resource_taxa.parquet`). They run DuckDB with the `httpfs` extension — for example via `uv run --with duckdb --no-project python` — and do not edit resource pages. Provenance, usages, and publications live inside the `raw_data` JSON column of `resources.parquet`.

### Search the registry by topic or domain

Use the `search-resources` skill.

This workflow finds resources covering a subject area (for example, "everything about RNA interactions"). It maps the free-text topic to the controlled domain vocabulary, runs a keyword search over names and descriptions, sweeps the source files for matches the structured query misses, and returns a ranked, de-duplicated list noting each resource's category and activity status.

### Trace a resource's upstream sources

Use the `trace-upstream-sources` skill.

This workflow determines the upstream data sources a resource (usually a knowledge graph) is built from, by walking each product's `original_source` and `secondary_source`, resolving the referenced KG-Registry identifiers, and optionally recursing to build the full provenance tree back to primary sources.

### Find where a resource is used

Use the `find-downstream-usages` skill.

This workflow determines everywhere a resource is used downstream. It combines a reverse-provenance sweep (other resources whose products name the target as a source) with the target's own curator-recorded `usages` field.

### Find resources similar to a given one

Use the `find-similar-resources` skill.

This workflow finds alternatives and near-duplicates of a resource by combining structured signals KG-Registry records (shared domains, taxa, category, graph scale, shared upstream sources) with heuristics such as description similarity and overlapping publication authors, then ranks the results with an explanation of why each is similar.

## Installing and discovering these skills

The skills are exposed through two complementary, independent standards. Either can be used on its own; supporting both costs nothing extra.

### Install as a plugin (Claude Code marketplace)

`/.claude-plugin/marketplace.json` defines a Claude Code plugin marketplace with two plugins:

- `kg-registry-discovery` — the four read-only discovery skills (no local clone needed).
- `kg-registry-curation` — the four curation and maintenance skills (require a local clone).

Add the marketplace and install a plugin from a Claude Code session:

```
/plugin marketplace add Knowledge-Graph-Hub/kg-registry
/plugin install kg-registry-discovery
```

This resolves against the repository's default branch, so the plugins become installable once these files are merged to `main`.

### Discover via Agentic Resource Discovery (ARD)

`/.well-known/ai-catalog.json` is an [Agentic Resource Discovery](https://github.com/ards-project/ard-spec) manifest (the `ai-catalog` format ARD builds on). It lists every skill as a catalog entry with a domain-anchored URN identifier, a short description, `capabilities`, and `representativeQueries` that registries use for semantic matching. Each entry's `url` points at the raw `SKILL.md`, and its `metadata` links back to the marketplace plugin that installs it.

Because the site is served under the `/kg-registry` base path, the manifest is published at `https://kghub.org/kg-registry/.well-known/ai-catalog.json` rather than the bare domain root. An ARD registry can be pointed at that URL directly; placing or linking a copy at the `kghub.org` domain root is a separate hosting step outside this repository.

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