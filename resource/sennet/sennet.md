---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://sennetconsortium.org/
  label: SenNet Consortium
creation_date: '2025-11-05T00:00:00Z'
description: The Cellular Senescence Network (SenNet) is an NIH Common Fund program
  that aims to comprehensively identify and characterize senescent cells across the
  human lifespan and in various disease states. SenNet provides spatial molecular
  maps of senescent cells in tissues, developing and applying cutting-edge technologies
  for detecting cellular senescence. The consortium generates multi-omics data, imaging
  data, and develops computational tools to advance understanding of how senescent
  cells contribute to aging and age-related diseases.
domains:
- health
- biomedical
- anatomy and development
- genomics
- precision medicine
homepage_url: https://sennetconsortium.org/
id: sennet
last_modified_date: '2025-11-05T00:00:00Z'
layout: resource_detail
name: SenNet
products:
- category: GraphicalInterface
  description: Data portal for browsing and accessing SenNet datasets
  format: http
  id: sennet.portal
  name: SenNet Data Portal
  original_source:
  - sennet
  product_url: https://data.sennetconsortium.org/
- category: Product
  description: Multi-omics datasets of senescent cells
  format: mixed
  id: sennet.data
  name: SenNet Multi-Omics Data
  original_source:
  - sennet
  product_url: https://data.sennetconsortium.org/
- category: ProgrammingInterface
  description: API for programmatic access to SenNet data
  format: http
  id: sennet.api
  name: SenNet API
  original_source:
  - sennet
  product_url: https://sennetconsortium.org/
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
synonyms:
- SenNet
- Cellular Senescence Network
taxon:
- NCBITaxon:9606
---
# SenNet - Cellular Senescence Network

## Overview

The Cellular Senescence Network (SenNet) is an NIH Common Fund program that aims to comprehensively identify and characterize senescent cells across the human lifespan and in various disease states.

Launched in 2021, SenNet develops and applies cutting-edge technologies to create spatial molecular maps of senescent cells in human tissues, advancing understanding of how these cells contribute to aging and age-related diseases.

## Key Features

- **Senescence Biomarkers**: Development and validation of markers for detecting senescent cells
- **Multi-Omics Profiling**: Genomics, transcriptomics, proteomics, and metabolomics of senescent cells
- **Spatial Mapping**: Tissue-level spatial distribution of senescent cells
- **Technology Development**: Novel methods for senescence detection and characterization
- **Public Data**: Open access to datasets, protocols, and analysis tools
- **Cross-Tissue Studies**: Comprehensive mapping across multiple human tissues

## Research Applications

- Aging biology research
- Age-related disease mechanisms
- Therapeutic target identification
- Senolytic drug development
- Biomarker discovery
- Understanding tissue-specific aging

## Products

### SenNet Data Portal
Web-based portal for exploring, visualizing, and downloading SenNet datasets including imaging, omics, and metadata.

### SenNet Multi-Omics Data
Comprehensive molecular datasets characterizing senescent cells across tissues and conditions, including transcriptomics, proteomics, and metabolomics.

### SenNet API
Programmatic interface for accessing SenNet data and integrating with computational workflows.

## Information Resource ID

This resource has the Information Resource identifier: `infores:sennet`

## Domains

- Health
- Biomedical
- Anatomy and Development
- Genomics
- Precision Medicine

## Taxon Coverage

Human (NCBITaxon:9606)