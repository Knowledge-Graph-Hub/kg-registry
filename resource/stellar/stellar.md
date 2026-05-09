---
activity_status: active
category: Resource
contacts:
- category: Individual
  contact_details:
  - contact_type: url
    value: https://cs.stanford.edu/~jure/
  label: Jure Leskovec
- category: Individual
  contact_details:
  - contact_type: url
    value: https://cs.stanford.edu/~mbrbic/
  label: "Maria Brbi\u0107"
creation_date: '2025-06-04T00:00:00Z'
description: STELLAR is a geometric deep learning method for cell type discovery and
  identification in spatially resolved single-cell datasets. It automatically assigns
  cells to known cell types and discovers novel cell types by transferring annotations
  across different dissection regions, tissues, and donors.
domains:
- biomedical
- genomics
homepage_url: https://snap.stanford.edu/stellar/
id: stellar
last_modified_date: '2025-10-15T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: STELLAR
products:
- category: ProcessProduct
  description: PyTorch implementation of the STELLAR algorithm for cell-type discovery
    and identification
  id: stellar.code
  name: STELLAR Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: stellar
  product_url: https://github.com/snap-stanford/stellar
- category: GraphicalInterface
  description: Demo Jupyter notebook showing example usage of STELLAR on downsampled
    datasets
  id: stellar.demo
  name: STELLAR Demo Notebook
  original_source:
  - relation_type: prov:hadPrimarySource
    source: stellar
  product_url: https://github.com/snap-stanford/stellar/blob/main/demo.ipynb
- category: Product
  description: CODEX multiplexed imaging datasets used in STELLAR research
  id: stellar.datasets
  name: STELLAR Datasets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: stellar
  product_url: https://datadryad.org/stash/share/1OQtxew0Unh3iAdP-ELew-ctwuPTBz6Oy8uuyxqliZk
  warnings: []
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
publications:
- authors:
  - "Brbi\u0107 M"
  - Cao K
  - Hickey JW
  - Tan Y
  - Snyder MP
  - Nolan GP
  - Leskovec J
  doi: doi:10.1038/s41592-022-01651-8
  id: https://doi.org/10.1038/s41592-022-01651-8
  journal: Nature Methods
  preferred: true
  title: Annotation of spatially resolved single-cell data with STELLAR
  year: '2022'
repository: https://github.com/snap-stanford/stellar
---
# STELLAR - Spatially Resolved Single-Cell Data Analysis

STELLAR (SpaTial cELl LeARning) is a geometric deep learning tool for cell-type discovery and identification in spatially resolved single-cell datasets. Developed at Stanford University, it uses graph convolutional neural networks to analyze spatial relationships between cells in tissue samples.

## Overview

STELLAR addresses the challenge of annotating cells in spatial single-cell datasets by combining molecular features with spatial organization. The method takes two inputs:

1. A reference dataset of annotated spatially resolved single-cell data
2. An unannotated dataset with unknown cell types

Using these inputs, STELLAR:
- Learns low-dimensional cell embeddings using graph convolutional networks
- Assigns cells to known cell types from the reference dataset
- Identifies novel cell types not present in the reference dataset
- Preserves spatial information about cell neighborhoods

## Applications

STELLAR has been successfully applied to:

- **CODEX multiplexed imaging data**: Used for analysis of Barrett's esophagus and tonsil tissue
- **HuBMAP datasets**: Applied to healthy intestine tissues across 8 donors, 64 tissues, and 2.6 million cells
- **Higher-order tissue structure analysis**: Capturing multicellular structural features within tissues

## Implementation

STELLAR is implemented in PyTorch and leverages PyTorch Geometric for graph neural network operations. The codebase includes:

- Core STELLAR algorithm for cell annotation
- Demo notebooks for example usage
- Utilities for dataset processing
- Pre-trained models

## Citation

When using STELLAR, please cite:
```
@article{stellar2022,
  title={Annotation of spatially resolved single-cell data with STELLAR},
  author={Brbić, Maria and Cao, Kaidi and Hickey, John W and Tan, Yuqi and Snyder, Michael P and Nolan, Garry P and Leskovec, Jure},
  journal={Nature Methods},
  volume={19},
  number={11},
  pages={1411--1418},
  year={2022},
  publisher={Nature Publishing Group}
}
```