---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: achilles@broadinstitute.org
  - contact_type: url
    value: https://depmap.org/portal/achilles/
  id: broad
  label: Project Achilles, Broad Institute
curators:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://depmap.org/
  label: DepMap
description: Project Achilles is a systematic effort aimed at identifying and cataloging
  gene essentiality across hundreds of genomically characterized cancer cell lines.
  Achilles uses genome-scale RNAi and CRISPR-Cas9 genetic perturbation reagents to
  silence or knockout individual genes and identify those genes that affect cell survival.
domains:
- biomedical
- genomics
- health
homepage_url: https://depmap.org/portal/achilles/
id: achilles
layout: resource_detail
license:
  id: https://depmap.org/portal/terms/
  label: DepMap Terms of Use
name: Project Achilles
products:
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
- authors:
  - Tsherniak A
  - Vazquez F
  - Montgomery PG
  - Weir BA
  - Kryukov G
  - Cowley GS
  doi: 10.1016/j.cell.2017.06.010
  id: doi:10.1016/j.cell.2017.06.010
  journal: Cell
  title: Defining a Cancer Dependency Map
  year: '2017'
---

# Project Achilles

Project Achilles is a systematic effort aimed at identifying and cataloging gene essentiality across hundreds of genomically characterized cancer cell lines. It is part of the broader Cancer Dependency Map (DepMap) initiative at the Broad Institute.

## About Project Achilles

Achilles uses genome-scale RNAi and CRISPR-Cas9 genetic perturbation reagents to silence or knockout individual genes and identify those genes that affect cell survival. By linking these dependencies to the genetic or molecular features of the tumors, this project is providing the foundation for the Cancer Dependency Map.

The project utilizes lentiviral-based pooled RNAi or CRISPR/Cas9 libraries in genome-scaled pooled loss-of-function (LOF) screening. This allows for the stable suppression of each gene individually in a subset of cells within a pooled format, enabling cost-effective genome-scale interrogation of gene essentiality.

## Methodology

Achilles has developed a highly standardized parallel screening workflow able to handle a large number of screens and ensure that the data across cell lines are comparable. Rigorous quality controls, including multiple cell line fingerprinting steps and monitoring of cell/reagent representation throughout the screening process, are performed to ensure the quality of the data.

The project has also developed computational methods to improve accuracy:
- **DEMETER** for RNAi screening
- **CERES** for CRISPR screening

These methods computationally infer and subtract seed effects that arise for each shRNA, resulting in more reliable datasets.

## Data Releases

Project Achilles is an ongoing effort aimed at screening more than 2000 cell lines of a variety of lineages, including cell lines derived from both solid and hematopoietic tumors of pediatric and adult lineages. The data is released on a quarterly basis pre-publication, with each release expanding the cell lines and genes covered.

## Applications

The Achilles dataset enables researchers to:
- Identify cancer vulnerabilities that can be exploited therapeutically
- Understand genetic dependencies in specific cancer types
- Discover context-specific essential genes
- Identify novel targets for cancer drug development
- Validate potential drug targets

The comprehensive nature of the dataset, covering hundreds of cell lines across diverse cancer types, makes it a valuable resource for cancer research and precision medicine.