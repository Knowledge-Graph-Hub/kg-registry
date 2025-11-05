---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: depmap@broadinstitute.org
  label: DepMap Team, Broad Institute
creation_date: '2025-11-05T00:00:00Z'
description: PRISM (Profiling Relative Inhibition Simultaneously in Mixtures) is a
  high-throughput drug screening technology developed by the Broad Institute that
  measures the sensitivity of cancer cell lines to therapeutic compounds. PRISM uses
  DNA barcoding to pool hundreds of cell lines together, enabling massively parallel
  drug screening at unprecedented scale. The platform is integrated into the Cancer
  Dependency Map (DepMap) project and provides comprehensive dose-response data for
  drug-cancer cell line interactions.
domains:
- drug discovery
- pharmacology
- biomedical
- precision medicine
- health
homepage_url: https://depmap.org/portal/prism/
id: prism
infores_id: prism
last_modified_date: '2025-11-05T00:00:00Z'
layout: resource_detail
name: PRISM
products:
- category: GraphicalInterface
  description: Web interface for exploring PRISM drug screening data through DepMap
  format: http
  id: prism.portal
  name: PRISM Data Portal
  original_source:
  - prism
  product_url: https://depmap.org/portal/prism/
- category: Product
  description: Downloadable drug sensitivity screening data from PRISM assays
  format: csv
  id: prism.datasets
  name: PRISM Drug Sensitivity Datasets
  original_source:
  - prism
  product_url: https://depmap.org/portal/data_page/
- category: ProgrammingInterface
  description: API access to PRISM drug screening data
  format: http
  id: prism.api
  name: DepMap API (PRISM data)
  original_source:
  - prism
  product_url: https://depmap.org/portal/api/
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - chebi
  - cosmic
  - achilles
  - depmap
  - ccle
  - gdsc
  - cellosaurus
  - clue
  - ctd
  - pharmacodb
  - prism
  - drugbank
  - lincs
  - compartments
  - offsides
  - sider
  - drugcentral
  - repohub
  - chemicalchecker
  - repodb
  - disgenet
  - opentargets
  - creeds
  - interpro
  - reactome
  - tissues
  - dorothea
  - progeny
  - gtex
  - hpa
  - go
  - corum
  - huri
  - intact
  - omnipath
  - string
  - bto
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
  secondary_source:
  - bioteque
publications:
- id: https://doi.org/10.1038/s43018-019-0018-6
repository: https://github.com/broadinstitute/depmap_omics
synonyms:
- PRISM
- Profiling Relative Inhibition Simultaneously in Mixtures
taxon:
- NCBITaxon:9606
---
# PRISM

## Overview

PRISM (Profiling Relative Inhibition Simultaneously in Mixtures) is a revolutionary high-throughput drug screening technology developed at the Broad Institute that enables massively parallel testing of therapeutic compounds against hundreds of cancer cell lines simultaneously. By leveraging DNA barcoding technology, PRISM can screen compounds at a scale and cost efficiency previously impossible, generating comprehensive drug sensitivity profiles across diverse cancer types.

## Technology Platform

### DNA Barcoding Approach
- Each cell line is labeled with a unique DNA barcode
- Cell lines are pooled together in a single well
- After drug treatment, cell viability is measured by quantifying barcode abundance
- Enables testing of 100+ cell lines per compound simultaneously

### Screening Scale
- **Cell Lines**: 500+ cancer cell lines representing diverse lineages
- **Compounds**: Thousands of compounds including FDA-approved drugs and experimental molecules
- **Dose-Response**: 8-point dose-response curves for accurate IC50 determination
- **Throughput**: 10-100x more efficient than traditional one-cell-line-per-well approaches

## Data Content

### Drug Sensitivity Profiles
- Comprehensive dose-response measurements
- IC50 and AUC (Area Under Curve) values
- Viability measurements across concentration ranges
- Quality control metrics for each experiment

### Cell Line Characterization
- Genomic profiles (mutations, copy number)
- Transcriptomic data (gene expression)
- Lineage and subtype annotations
- Integration with DepMap omics data

### Compound Information
- Chemical structures and properties
- MOA (Mechanism of Action) annotations
- Target information
- Clinical trial status

## Integration with DepMap

PRISM data is fully integrated into the Cancer Dependency Map project, enabling:
- Correlation with CRISPR dependency data
- Multi-omic biomarker discovery
- Prediction of drug response
- Identification of combination therapy opportunities

## Applications

- **Drug Repurposing**: Identifying new indications for approved drugs
- **Precision Medicine**: Matching patients to therapies based on molecular features
- **Target Validation**: Linking genetic dependencies to drug sensitivity
- **Biomarker Discovery**: Identifying predictive markers of drug response
- **Combination Strategies**: Finding synergistic drug combinations

## Data Access

All PRISM data is freely available through:
- DepMap Data Portal for bulk downloads
- Interactive web interface for exploration and visualization
- API access for programmatic queries
- Regular quarterly data releases

## Information Resource ID

This resource has the Information Resource identifier: `infores:prism`

## License and Reuse

PRISM data is made available by the Broad Institute for research use through the DepMap portal, supporting open science and drug discovery efforts worldwide.