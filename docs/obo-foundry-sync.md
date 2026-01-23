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
uv run python util/sync_obo_foundry.py --verbose

# Test sync with limited number of ontologies
uv run python util/sync_obo_foundry.py --limit 5 --verbose

# Dry run to see what would be synced
uv run python util/sync_obo_foundry.py --dry-run --verbose
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

## Features

- **Automatic Synchronization**: Fetches the latest ontology metadata from the OBO Foundry registry
- **Enhanced Metadata Transformation**: Converts OBO Foundry metadata to KG-Registry schema format with four key improvements:
  - **Contact Objects**: Transforms contact details to proper Contact class objects with category, label, contact_details, and ORCID
  - **Product Objects**: Creates proper Product objects with name, description, and product_url fields
  - **DataModel Category**: Sets ontology category to 'DataModel' instead of generic 'Resource'
  - **Inactive Ontology Inclusion**: Includes inactive and obsolete ontologies (previously filtered out)
- **Domain Mapping**: Maps OBO domains to KG-Registry domain categories
- **License Handling**: Properly formats license information as License objects
- **Publication Links**: Includes associated publications when available
- **Tag Filtering**: Only includes valid tags that match the KG-Registry schema
- **Collection Tagging**: All synced ontologies are tagged with 'obo-foundry' collection
- **Update Detection**: Identifies new vs. existing resources for proper logging
- **Error Handling**: Robust error handling with detailed logging
- **Dry Run Support**: Test mode to preview changes without making modifications

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

## Recent Enhancements (September 2024)

The OBO Foundry sync has been enhanced with four key improvements to better align with the KG-Registry schema:

### 1. Enhanced Contact Transformation
- **Before**: Simple contact strings like "Email: user@example.com"  
- **After**: Proper Contact objects with structured fields:
  ```yaml
  contacts:
  - category: Individual
    label: "Jane Doe"
    contact_details: "jane.doe@example.com"
    orcid: "0000-0000-0000-0000"
  ```

### 2. Structured Product Objects
- **Before**: Simple URL lists in download_url fields
- **After**: Proper Product objects following the schema:
  ```yaml
  products:
  - name: "ontology.owl"
    description: "Primary OWL file for Ontology"
    product_url: "http://purl.obolibrary.org/obo/ontology.owl"
  ```

### 3. DataModel Category Assignment  
- **Before**: Generic 'Resource' category
- **After**: Specific 'DataModel' category for all ontologies

### 4. Inactive Ontology Inclusion
- **Before**: Inactive and obsolete ontologies were filtered out
- **After**: All ontologies included with proper activity_status preservation

## Ontology Statistics

Based on the most recent sync (September 2024):

- **Total Ontologies in OBO Foundry**: 263
- **Active Ontologies**: 185  
- **Inactive/Obsolete Ontologies**: 78 (now included in sync)
- **Successfully Mapped**: ~95% of all ontologies
- **Common Issues**: Invalid tags, missing contact information, complex license structures

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