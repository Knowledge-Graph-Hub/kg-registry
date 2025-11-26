---
activity_status: active
category: DataSource
creation_date: '2025-10-30T00:00:00Z'
description: OmicsDI (Omics Discovery Index) is an integrated resource for omics datasets across multiple repositories, providing a unified search interface for genomics, proteomics, metabolomics, and transcriptomics data.
domains:
  - genomics
  - proteomics
id: "omicsdi"
infores_id: "omicsdi"
last_modified_date: '2025-11-25T00:00:00Z'
layout: resource_detail
name: OmicsDI
homepage_url: https://www.omicsdi.org/
synonyms:
  - OmicsDI
  - Omics Discovery Index
contacts:
  - category: Organization
    label: EMBL-EBI
    contact_details:
      - contact_type: url
        value: "https://www.ebi.ac.uk/"
---

# OmicsDI

## Overview

OmicsDI (Omics Discovery Index) is an integrated resource developed by EMBL-EBI that provides a unified search and discovery platform for omics datasets. It aggregates metadata from multiple public omics repositories, enabling researchers to find and access genomics, proteomics, metabolomics, transcriptomics, and multi-omics datasets through a single interface.

## Key Features

- **Multi-Repository Search**: Unified access to datasets from multiple omics databases
- **Cross-Omics Coverage**: Genomics, proteomics, metabolomics, transcriptomics, and multi-omics data
- **Standardized Metadata**: Harmonized dataset descriptions using controlled vocabularies
- **Advanced Search**: Faceted search across organisms, tissues, diseases, and data types
- **Dataset Discovery**: Browse and explore related datasets and studies
- **API Access**: Programmatic access to dataset metadata
- **Citation Tracking**: Links to publications and citation information

## Integrated Repositories

OmicsDI aggregates data from major omics repositories:

### Genomics and Transcriptomics
- ArrayExpress
- GEO (Gene Expression Omnibus)
- ENA (European Nucleotide Archive)
- dbGaP

### Proteomics
- PRIDE (Proteomics Identifications Database)
- PeptideAtlas
- MassIVE
- jPOST

### Metabolomics
- MetaboLights
- Metabolomics Workbench
- MetabolomeXchange

### Other Data Types
- Expression Atlas
- Genome-wide association studies (GWAS)
- Epigenomics datasets

## Data Content

### Dataset Metadata
- Dataset identifiers and accession numbers
- Study titles and descriptions
- Organism and tissue information
- Disease and phenotype annotations
- Experimental design details
- Technology and platform information
- Sample sizes and biological replicates
- Publication references
- Data availability and access information

### Standardization
- Ontology-based annotations (e.g., EFO, NCBI Taxonomy)
- Unified metadata schema across repositories
- Controlled vocabulary for data types and technologies
- Cross-references between related datasets

## Applications

- **Data Discovery**: Finding relevant omics datasets for research questions
- **Multi-Omics Integration**: Identifying complementary datasets across omics types
- **Meta-Analysis**: Discovering comparable datasets for large-scale analyses
- **Hypothesis Generation**: Exploring related studies and datasets
- **Data Reuse**: Accessing public omics data for secondary analyses
- **Literature Mining**: Connecting datasets to publications

## Search Capabilities

### Faceted Search
- Organism/species
- Tissue and cell type
- Disease and phenotype
- Omics type
- Technology platform
- Publication date
- Submitter institution

### Advanced Features
- Free-text search across metadata fields
- Boolean operators and filters
- Related dataset recommendations
- Export and download of search results
- Saved searches and alerts

## API and Programmatic Access

OmicsDI provides:
- RESTful API for dataset queries
- Bulk metadata download
- Integration with computational workflows
- R and Python client libraries

## Information Resource ID

This resource has the Information Resource identifier: `infores:omicsdi`

## Access

- **Web Interface**: https://www.omicsdi.org/
- **API Documentation**: https://www.omicsdi.org/api
- **Help and Tutorials**: https://www.omicsdi.org/about

## Governance

OmicsDI is maintained by the European Bioinformatics Institute (EMBL-EBI) as part of their data integration and discovery services.

For more information, visit https://www.omicsdi.org/ or contact EMBL-EBI at https://www.ebi.ac.uk/
