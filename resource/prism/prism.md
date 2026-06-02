---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: depmap@broadinstitute.org
  id: broad
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
homepage_url: https://depmap.org/repurposing/
id: prism
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: PRISM
products:
- category: GraphicalInterface
  description: Web interface for exploring the PRISM Repurposing drug-screening resource
    through DepMap
  format: http
  id: prism.portal
  name: PRISM Repurposing Resource
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prism
  product_url: https://depmap.org/repurposing/
- category: Product
  description: DepMap downloads page for PRISM Repurposing primary and secondary screen
    data
  format: csv
  id: prism.datasets
  name: PRISM Drug Sensitivity Dataset Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prism
  product_url: https://depmap.org/portal/data_page/?tab=allData
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: depmap
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-02: HTTP 403 error
    when accessing file'
- category: Product
  description: Replicate-collapsed log-fold-change matrix from the primary PRISM Repurposing
    screen of pooled-cell line chemical-perturbation viability measurements
  format: csv
  id: prism.primary_screen_lfc
  name: PRISM Repurposing Primary Screen Log-Fold Change
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prism
  product_url: https://ndownloader.figshare.com/files/20237709
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: depmap
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-02: HTTP 403 error
    when accessing file'
- category: Product
  description: Dose-response curve parameter matrix from the secondary PRISM Repurposing
    screen of 1,448 compounds across cancer cell lines
  format: csv
  id: prism.secondary_screen_dose_response
  name: PRISM Repurposing Secondary Screen Dose Response
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prism
  product_url: https://ndownloader.figshare.com/files/20237739
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: depmap
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-02: HTTP 403 error
    when accessing file'
- category: ProgrammingInterface
  description: API access to PRISM drug screening data
  format: http
  id: prism.api
  name: DepMap API (PRISM data)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prism
  product_url: https://depmap.org/portal/api/
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: bioteque
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chemicalchecker
  - relation_type: prov:hadPrimarySource
    source: clue
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: creeds
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: huri
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: offsides
  - relation_type: prov:hadPrimarySource
    source: omnipath
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  - relation_type: prov:hadPrimarySource
    source: prism
  - relation_type: prov:hadPrimarySource
    source: progeny
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
- category: Product
  description: Drug screening data from various platforms including GDSC, PRISM, and
    CTD2
  format: csv
  id: depmap.drug_sensitivity
  name: DepMap Drug Sensitivity Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_url: https://depmap.org/portal/data_page/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: prism
  - relation_type: prov:wasDerivedFrom
    source: ctd2
publications:
- authors:
  - Steven M Corsello
  - Rohith T Nagari
  - Ryan D Spangler
  - Jordan Rossen
  - Mustafa Kocak
  - Todd R Golub
  doi: 10.1038/s43018-019-0018-6
  id: doi:10.1038/s43018-019-0018-6
  journal: Nature Cancer
  preferred: true
  title: Discovering the anticancer potential of non-oncology drugs by systematic
    viability profiling
  year: '2020'
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

No exact PRISM entry was found in the INFORES catalog during the 2026-06-02 curation pass.

## License and Reuse

PRISM data is made available by the Broad Institute for research use through the DepMap portal, supporting open science and drug discovery efforts worldwide.