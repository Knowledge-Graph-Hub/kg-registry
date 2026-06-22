---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.icgc-argo.org/
  label: International Cancer Genome Consortium (ICGC)
creation_date: '2026-06-03T00:00:00Z'
description: The International Cancer Genome Consortium (ICGC) is a global initiative
  to characterize the genomic, transcriptomic, and epigenomic changes in 50 different
  tumor types and subtypes. It generates comprehensive catalogues of somatic mutations
  and other cancer genomics data, made available to the research community. The original
  ICGC Data Portal (dcc.icgc.org) was retired in June 2024, with ICGC 25K data and
  the successor ICGC ARGO project continuing to provide access to cancer genomics
  datasets.
domains:
- genomics
- clinical
- biomedical
homepage_url: https://www.icgc-argo.org/
id: icgc
last_modified_date: '2026-06-05T00:00:00Z'
layout: resource_detail
license:
  id: https://platform.icgc-argo.org/
  label: Controlled access (ICGC DACO)
name: ICGC
products:
- category: GraphicalInterface
  description: ICGC ARGO data platform for browsing, querying, and accessing uniformly
    analyzed cancer genomics and clinical data aligned to GRCh38.
  format: http
  id: icgc.platform
  name: ICGC ARGO Data Platform
  original_source:
  - relation_type: prov:hadPrimarySource
    source: icgc
  product_url: https://platform.icgc-argo.org/
- category: Product
  description: Controlled-access cancer genomics data downloads, including the ICGC
    25K release and PCAWG data, obtained through the ICGC DACO application process
    and Score download client.
  format: mixed
  id: icgc.downloads
  name: ICGC 25K Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: icgc
  product_url: https://docs.icgc-argo.org/
- category: Product
  description: Unified BioMuta cancer mutation dataset produced by combining mutation
    records from TCGA, ICGC, CIViC, and COSMIC into a common field structure.
  format: csv
  id: biomuta.dataset
  name: BioMuta Cancer Mutation Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomuta
  product_url: https://biomuta.readthedocs.io/en/latest/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: civic
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: icgc
  - relation_type: prov:wasDerivedFrom
    source: tcga
publications:
- doi: 10.1038/nature08987
  id: https://doi.org/10.1038/nature08987
  journal: Nature
  title: International network of cancer genome projects
  year: '2010'
synonyms:
- International Cancer Genome Consortium
- ICGC ARGO
---
# ICGC

## Overview

The International Cancer Genome Consortium (ICGC) is a global research effort to
characterize the genomic, transcriptomic, and epigenomic changes across dozens of
cancer types and subtypes. ICGC produced comprehensive catalogues of somatic mutations
and associated molecular and clinical data, shared with the research community to
accelerate cancer research.

## Status and Access

The original ICGC Data Portal at dcc.icgc.org was officially retired in June 2024. The
most recent ICGC 25K release and PCAWG data remain available to authorized users, and
the consortium's work continues through the Accelerating Research in Genomic Oncology
(ICGC ARGO) project. Data is uniformly analyzed against the GRCh38 human reference genome
and accessed through controlled-access procedures managed by the ICGC Data Access
Compliance Office (DACO).

## Key Features

- **Large-scale cancer genomics**: Somatic mutation catalogues across many tumor types.
- **Multi-omics data**: Genomic, transcriptomic, and epigenomic profiles plus clinical data.
- **Uniform analysis**: Data harmonized against GRCh38 in the ICGC ARGO platform.
- **Controlled access**: Sensitive datasets available via the ICGC DACO application process.

## Access

- ICGC ARGO data platform at [platform.icgc-argo.org](https://platform.icgc-argo.org/)
- ICGC 25K data access documentation at [docs.icgc-argo.org](https://docs.icgc-argo.org/)

## Citation

The International Cancer Genome Consortium. International network of cancer genome
projects. Nature (2010) 464:993-998. doi:10.1038/nature08987