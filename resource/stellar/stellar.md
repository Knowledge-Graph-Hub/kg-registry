---
activity_status: active
category: Resource
description: STELLAR is a geometric deep learning method for cell type discovery and identification
  in spatially resolved single-cell datasets. It automatically assigns cells to known
  cell types and discovers novel cell types by transferring annotations across different
  dissection regions, tissues, and donors.
domains:
- biomedical
- genomics
- biology
- machine learning
homepage_url: https://snap.stanford.edu/stellar/
id: stellar
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: STELLAR
repository: https://github.com/snap-stanford/stellar
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
  label: Maria Brbić
publications:
- authors:
  - Brbić M
  - Cao K
  - Hickey JW
  - Tan Y
  - Snyder MP
  - Nolan GP
  - Leskovec J
  doi: https://doi.org/10.1038/s41592-022-01651-8
  journal: Nature Methods
  preferred: true
  title: Annotation of spatially resolved single-cell data with STELLAR
  year: "2022"
products:
- category: ProcessProduct
  description: PyTorch implementation of the STELLAR algorithm for cell-type discovery and identification
  id: stellar.code
  name: STELLAR Code
  product_url: https://github.com/snap-stanford/stellar
- category: GraphicalInterface
  description: Demo Jupyter notebook showing example usage of STELLAR on downsampled datasets
  id: stellar.demo
  name: STELLAR Demo Notebook
  product_url: https://github.com/snap-stanford/stellar/blob/main/demo.ipynb
- category: Product
  description: CODEX multiplexed imaging datasets used in STELLAR research
  id: stellar.datasets
  name: STELLAR Datasets
  product_url: https://datadryad.org/stash/share/1OQtxew0Unh3iAdP-ELew-ctwuPTBz6Oy8uuyxqliZk
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
  - do
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
  - cmap
  - hp
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
  - nposckan
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
  - do
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
  - cmap
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
  - nposckan
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
  - do
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
  - cmap
  - hp
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
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
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