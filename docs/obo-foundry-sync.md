# OBO Foundry Synchronization

This document describes the OBO Foundry synchronization functionality added to the KG-Registry.

## Overview

The OBO Foundry sync feature automatically creates and updates KG-Registry resources for ontologies from the OBO Foundry registry (https://obofoundry.org/). This ensures that the KG-Registry stays up-to-date with the latest ontologies from this important biomedical ontology resource.

## Files Added

- `util/sync_obo_foundry.py` - Main synchronization script
- Updated `Makefile` with new sync targets
- Updated schema to include `obo-foundry` collection

## Usage

### Command Line

```bash
# Sync all active OBO Foundry ontologies
poetry run python util/sync_obo_foundry.py --verbose

# Test sync with limited number of ontologies
poetry run python util/sync_obo_foundry.py --limit 5 --verbose

# Dry run to see what would be synced
poetry run python util/sync_obo_foundry.py --dry-run --verbose
```

### Make Targets

```bash
# Sync all active OBO Foundry ontologies
make sync-obo-foundry

# Test sync with 5 ontologies
make sync-obo-test

# Dry run to see what would be synced
make sync-obo-dry-run
```

## Integration with Build Process

The OBO Foundry sync is integrated into the main build process via the `all` target in the Makefile. This means that every time the full build is run, the OBO Foundry ontologies will be synchronized.

## What Gets Synced

The sync process:

1. Fetches the OBO Foundry registry from https://obofoundry.org/registry/ontologies.yml
2. Filters out inactive, orphaned, or obsolete ontologies
3. Transforms the metadata to match the KG-Registry schema
4. Creates/updates resource files in the `resource/` directory
5. Adds all synced ontologies to the `obo-foundry` collection

## Metadata Transformation

The sync script transforms OBO Foundry metadata to KG-Registry format:

- **License**: Converts OBO license objects to KG-Registry License format
- **Domain**: Maps OBO domains to valid KG-Registry DomainEnum values
- **Contacts**: Extracts email, GitHub, and ORCID information
- **Products**: Creates product entries for each ontology file format
- **Publications**: Includes associated publications
- **Collections**: Adds to `obo-foundry` collection

## Domain Mapping

OBO Foundry domains are mapped to KG-Registry domains as follows:

- `anatomy and development` → `anatomy and development`
- `biological systems` → `biological systems`
- `chemistry and biochemistry` → `chemistry and biochemistry`
- `diet, metabolomics, and nutrition` → `chemistry and biochemistry`
- `health` → `biomedical`
- `information` → `biomedical`
- `information technology` → `biomedical`
- `investigations` → `biomedical`
- `organisms` → `biological systems`
- `phenotype` → `biological systems`
- `simulation` → `biological systems`
- `upper` → `biological systems`
- `environment` → `environment`
- `agriculture` → `agriculture`

Unknown domains default to `biological systems`.

## Statistics

As of the last sync, the OBO Foundry contains approximately:
- 263 total ontologies
- 185 active ontologies (that would be synced)
- 78 inactive/orphaned/obsolete ontologies (skipped)

## Schema Changes

Added the `obo-foundry` collection to `CollectionEnum` in the schema:

```yaml
obo-foundry:
  description: >-
    This entity is an ontology from the OBO Foundry,
    a collaborative effort to create reference ontologies
    in the biomedical domain.
  meaning: https://obofoundry.org/
```

## Error Handling

The sync script includes comprehensive error handling:

- Network errors when fetching the registry
- YAML parsing errors
- Individual ontology processing errors
- Schema validation errors

Failed ontologies are logged but don't stop the overall sync process.

## Logging

The script provides detailed logging at INFO and DEBUG levels:
- Fetching registry data
- Processing individual ontologies
- Creating/updating resources
- Final statistics

## Future Enhancements

Potential future improvements:
- Incremental sync based on modification dates
- Configurable domain mappings
- Support for additional OBO Foundry metadata fields
- Integration with automated PR creation for updates