---
layout: intro_doc
title: Reference Validation
---

# Reference Validation

KG-Registry validates publication metadata against cache files produced by
[`linkml-reference-validator`](https://github.com/linkml/linkml-reference-validator).
The validation runs as part of the existing resource metadata validation path:

```bash
uv run make validate-file FILE=resource/<resource>/<resource>.md
uv run make extract-metadata
```

The full `extract-metadata` build target reports publication reference findings
as warnings so citation metadata issues do not block unrelated registry builds.
Single-file validation and explicit citation validation commands remain stricter
and can fail on hard citation metadata errors.

By default, missing cache files are warnings. Cached references are compared to
the Resource page publication fields, and mismatches in title, year, DOI, or
first author are validation errors. Journal mismatches are warnings because
journal names often differ between abbreviated and full forms.

Validation results are cached in `cache/publication_reference_validation.yml`.
The cache key includes the Resource page publication entry and the cached
reference metadata, so unchanged citations can be reused on subsequent builds.
If either the Resource page publication metadata or the cached reference changes,
the citation is checked again.

## Cache Location

The default cache directory is `references_cache`, configured in
`.linkml-reference-validator.yaml`. This follows the same Markdown plus YAML
front matter cache format used by `linkml-reference-validator`.

To populate missing cache entries for all resource pages:

```bash
uv run make cache-publication-references
```

To require cache coverage for all publication references:

```bash
uv run make validate-publication-reference-cache
```

To remove publication entries with hard metadata mismatches from Resource pages:

```bash
uv run ./util/extract-metadata.py validate \
  --remove-invalid-publications \
  resource/<resource>/<resource>.md
```

This repair mode removes only entries with hard comparison errors, such as a
complete title, DOI, or first-author mismatch. Missing cache files remain
warnings because they do not prove that the Resource page citation is invalid.

For one-off validation, use the underlying script options:

```bash
uv run ./util/extract-metadata.py validate \
  --fetch-publication-references \
  resource/<resource>/<resource>.md
```

`linkml-reference-validator` currently requires Python 3.10 or newer, so the
dependency is marked with a Python-version guard. On Python 3.9, KG-Registry can
still compare existing cache files but cannot fetch missing cache entries.

## Dashboard Metrics

The quality dashboard includes citation coverage and citation validation issues.
Resources with no `publications` entry are listed as missing publications.
Resources with cached validation errors, warnings, or missing reference cache
entries are listed as having publication citation metadata issues.
