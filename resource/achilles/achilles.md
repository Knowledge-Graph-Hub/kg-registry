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
creation_date: '2025-07-08T00:00:00Z'
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
last_modified_date: '2025-12-13T00:00:00Z'
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
taxon:
- NCBITaxon:9606
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