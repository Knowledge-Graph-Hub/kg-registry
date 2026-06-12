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

By default, missing cache files are warnings. Cached references are compared to
the Resource page publication fields, and mismatches in title, year, DOI, or
first author are validation errors. Journal mismatches are warnings because
journal names often differ between abbreviated and full forms.

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

For one-off validation, use the underlying script options:

```bash
uv run ./util/extract-metadata.py validate \
  --fetch-publication-references \
  resource/<resource>/<resource>.md
```

`linkml-reference-validator` currently requires Python 3.10 or newer, so the
dependency is marked with a Python-version guard. On Python 3.9, KG-Registry can
still compare existing cache files but cannot fetch missing cache entries.
