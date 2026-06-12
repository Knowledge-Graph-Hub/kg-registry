# kg-registry

A registry for knowledge graphs and their components.

🔗 [Visit the KG Registry](https://kghub.org/kg-registry/)

## Features

- Registry of knowledge graphs and related resources
- YAML-based data format for easy editing and collaboration
- Web interface for browsing resources
- Advanced search using SQL queries via DuckDB
- Parquet file support for efficient storage and querying
- CLI tools for data management and export

## Documentation

**[KG-Registry Documentation](https://kghub.org/kg-registry/docs/intro/)**: Start here to learn about the purpose of KG-Registry and how it works.

Entries in KG-Registry are either *Resources* or *Products*. Resources represent top-level entries for knowledge graph and data sources. Products are specific representations or interfaces for a resource (e.g., graph dumps, APIs, or visualizations). This also includes associated software and documentation sets.

For more detail:
- [Resources](https://kghub.org/kg-registry/docs/intro/resources.html)
- [Products](https://kghub.org/kg-registry/docs/intro/products.html)
- [Agent-Assisted Curation](https://kghub.org/kg-registry/docs/intro/agent-skills.html)
- [Parquet Backend & Advanced Search](docs/parquet_backend.md)

## Site Development

For developers working on the KG-Registry website and backend:
- [Site Development Guide](README-sitedev.md) - Setup, deployment, and troubleshooting
- [Agent Skills Guide](docs/intro/agent-skills.md) - Local agent-assisted curation workflows in `.agents/`
- [Parquet Backend Documentation](docs/parquet_backend.md) - Database schema and querying
- [Advanced Search Feature](advanced-search.html) - SQL-based resource discovery interface

## Reference Validation

Resource publication metadata is validated against cache files produced by
[`linkml-reference-validator`](https://github.com/linkml/linkml-reference-validator).
Cached title, year, DOI, and first-author mismatches are validation errors;
missing cache files are warnings during ordinary validation.

```bash
uv run make validate-file FILE=resource/<resource>/<resource>.md
uv run make cache-publication-references
uv run make validate-publication-reference-cache
```

See [Reference Validation](docs/reference-validation.md) for the full procedure.
