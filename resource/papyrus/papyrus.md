---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: OlivierBeq
  label: Olivier J. M. Béquignon
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.universiteitleiden.nl/en/science/drug-research
  label: Computational Drug Discovery, Leiden Academic Centre for Drug Research, Leiden
    University
creation_date: '2026-10-28T00:00:00Z'
description: Papyrus is a large-scale, standardized and curated dataset of small-molecule
  bioactivity data aimed at machine learning applications such as QSAR and proteochemometric
  modeling. It aggregates and normalizes ligand-protein bioactivity measurements (with
  standardized compound structures, UniProt protein targets, and precomputed molecular
  and protein descriptors) into quality-graded records, and is distributed as versioned
  releases. The original release compiled about 60 million data points from ChEMBL and
  ExCAPE-DB; later versions add further sources and grow the dataset. A high-confidence
  subset, Papyrus++, is provided alongside the full all-quality dataset. The data are
  hosted on 4TU.ResearchData and Zenodo, and the companion papyrus-scripts Python package
  and command-line tool handle downloading, versioning, filtering, searching, and export.
domains:
- cheminformatics
- drug discovery
- chemistry and biochemistry
- machine learning
- information technology
homepage_url: https://github.com/OlivierBeq/Papyrus-scripts
id: papyrus
last_modified_date: '2026-10-28T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC BY-SA 4.0
name: Papyrus
products:
- category: Product
  description: The Papyrus bioactivity dataset, distributed as versioned releases on
    4TU.ResearchData (and mirrored on Zenodo). Each release provides standardized ligand-protein
    bioactivity records, compound structures, UniProt protein targets, and precomputed
    molecular and protein descriptors, in tab-delimited and Parquet formats (LZMA/Gzip
    compressed), with a high-confidence Papyrus++ subset alongside the full all-quality
    dataset.
  format: mixed
  id: papyrus.dataset
  name: Papyrus Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: papyrus
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: excape-db
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://doi.org/10.4121/16896406
- category: ProcessProduct
  description: papyrus-scripts, a Python library and command-line tool for working with
    the Papyrus dataset. It downloads, versions, and caches releases from 4TU or Zenodo,
    provides a lazy filtering and search API over the data (quality, source, organism,
    protein class, and molecular filters), builds similarity and substructure search
    indexes, and exports selected subsets.
  format: python
  id: papyrus.scripts
  name: papyrus-scripts
  license:
    id: https://opensource.org/licenses/MIT
    label: MIT License
  original_source:
  - relation_type: prov:hadPrimarySource
    source: papyrus
  product_url: https://github.com/OlivierBeq/Papyrus-scripts
publications:
- authors:
  - Olivier J. M. Béquignon
  - Brandon J. Bongers
  - Willem Jespers
  - Adriaan P. IJzerman
  - Bob van der Water
  - Gerard J. P. van Westen
  doi: 10.1186/s13321-022-00672-x
  id: doi:10.1186/s13321-022-00672-x
  journal: Journal of Cheminformatics
  preferred: true
  title: 'Papyrus: a large-scale curated dataset aimed at bioactivity predictions'
  year: '2023'
version: 2024.09.2
---
# Papyrus

## Overview

Papyrus is a large-scale, standardized and curated dataset of small-molecule bioactivity data, built for machine learning uses such as QSAR and proteochemometric modeling. It normalizes ligand-protein bioactivity measurements into quality-graded records, with standardized compound structures, UniProt protein targets, and precomputed molecular and protein descriptors, and ships as versioned releases.

The original release compiled roughly 60 million data points from ChEMBL and ExCAPE-DB; later versions add more sources and continue to grow. A high-confidence subset, Papyrus++, is provided alongside the full all-quality dataset.

## Access

- The dataset is hosted on 4TU.ResearchData (DOI 10.4121/16896406, CC BY-SA 4.0) and mirrored on Zenodo, as versioned releases.
- The `papyrus-scripts` Python package and CLI (MIT, on PyPI and GitHub) download, filter, search, and export the data without loading the full dataset into memory.

There is no interactive web frontend; access is through the dataset files and the scripts.

## Upstream sources

ChEMBL and ExCAPE-DB are the core bioactivity sources, and protein targets are mapped to UniProt. ExCAPE-DB itself aggregates ChEMBL and PubChem bioassay data, so PubChem-origin activities enter Papyrus through it.

## Citation

Béquignon OJM, Bongers BJ, Jespers W, IJzerman AP, van der Water B, van Westen GJP. Papyrus: a large-scale curated dataset aimed at bioactivity predictions. J Cheminform. 2023;15:3. doi:10.1186/s13321-022-00672-x
