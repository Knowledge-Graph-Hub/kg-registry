---
activity_status: active
category: DataModel
contacts:
- category: Individual
  label: "Katy B\xF6rner"
  orcid: 0000-0002-3321-6137
creation_date: '2025-11-05T00:00:00Z'
description: The Human Reference Atlas (HRA) is a comprehensive 3D spatial framework
  and data model for mapping the healthy human body at single-cell resolution. The
  HRA provides reference anatomical structures, cell types, biomarkers, and standardized
  spatial coordinates to enable integration and analysis of diverse biological data
  types across multiple scales from organs to cells.
domains:
- anatomy and development
- health
- biological systems
- biomedical
- precision medicine
homepage_url: https://humanatlas.io/
id: hra
infores_id: hra
last_modified_date: '2025-11-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Human Reference Atlas
products:
- category: GraphicalInterface
  description: Web portal for exploring and visualizing the Human Reference Atlas
  format: http
  id: hra.portal
  name: Human Reference Atlas Portal
  original_source:
  - hra
  product_url: https://humanatlas.io/
- category: ProgrammingInterface
  description: API endpoints for programmatic access to HRA data
  format: http
  id: hra.api
  name: HRA API
  original_source:
  - hra
  product_url: https://apps.humanatlas.io/api
- category: Product
  description: Downloadable data files including anatomical structures, cell types,
    and biomarkers
  format: mixed
  id: hra.data
  name: HRA Data Downloads
  original_source:
  - hra
  product_url: https://humanatlas.io/data
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - doid
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - connectivitymap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - sckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - doid
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - connectivitymap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - sckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
publications:
- id: https://doi.org/10.1038/s41556-021-00788-6
repository: https://github.com/hubmapconsortium/ccf-ui
synonyms:
- HRA
taxon:
- NCBITaxon:9606
---
# Human Reference Atlas

## Overview

The Human Reference Atlas (HRA) is a comprehensive 3D spatial framework for mapping the healthy human body at single-cell resolution. Developed by the HuBMAP consortium and collaborators, the HRA provides standardized reference anatomical structures, cell type information, biomarkers, and spatial coordinates that enable integration and analysis of diverse biological data types.

## Key Components

### 3D Reference Organs
- High-resolution 3D models of 11 organs
- Standardized anatomical structures and regions
- Common Coordinate Framework (CCF) for spatial registration

### Cell Type Annotations
- Comprehensive cell type taxonomies
- Cell type biomarkers and signatures
- Linkages to molecular data

### Biomarker Information
- Protein, gene, and lipid biomarkers
- Cell type-specific markers
- Spatial expression patterns

## Data Model Features

- **Common Coordinate Framework (CCF)**: 3D reference coordinate system for spatial data integration
- **Anatomical Structures, Cell Types, and Biomarkers (ASCT+B)**: Structured tables linking anatomy, cell types, and biomarkers
- **3D Reference Object Library**: Collection of validated 3D organ models
- **Crosswalks**: Mappings to standard ontologies (Uberon, CL, HGNC, etc.)

## Scope and Coverage

- **Organs**: 11 major organs with 3D reference models
- **Cell Types**: Comprehensive coverage of human cell types
- **Biomarkers**: Thousands of molecular biomarkers
- **Species**: Human (Homo sapiens, NCBITaxon:9606)
- **Resolution**: Single-cell to organ level

## Use Cases

- Spatially registering experimental datasets
- Cell type identification and validation
- Cross-dataset integration and comparison
- Atlas construction for healthy and diseased tissues
- Multi-omics data integration
- Precision medicine applications

## Integration with HuBMAP

The HRA serves as the spatial reference framework for the Human BioMolecular Atlas Program (HuBMAP), enabling:
- Registration of tissue samples to standard anatomical locations
- Integration of multi-modal imaging and omics data
- Cross-consortium data sharing and comparison
- Reproducible analysis workflows

## Information Resource ID

This resource has the Information Resource identifier: `infores:hra`

## License and Reuse

HRA data and resources are released under CC BY 4.0 license, allowing free use with appropriate attribution.