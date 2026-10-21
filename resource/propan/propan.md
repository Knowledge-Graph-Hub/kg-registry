---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://ngdc.cncb.ac.cn/propan/home
  - contact_type: email
    value: propan@big.ac.cn
  label: National Genomics Data Center, CNCB
creation_date: '2026-10-21T00:00:00Z'
description: ProPan is a comprehensive database for profiling the pan-genome dynamics of prokaryotes,
  hosted by the China National Center for Bioinformation (CNCB) / National Genomics Data Center.
  It provides post-processed gene-content data, functional annotation, and multi-dimensional
  analyses across bacterial and archaeal species, including orthologous gene clustering, nucleotide
  diversity, COG enrichment, metabolism analyses, antibiotic-resistance gene prediction, and
  KEGG and PPI mapping. It covers 1,504 species (1,481 bacterial and 23 archaeal) spanning
  51,882 strain genomes sourced from NCBI.
domains:
- microbiology
- genomics
homepage_url: https://ngdc.cncb.ac.cn/propan/home
id: propan
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
name: ProPan
products:
- category: GraphicalInterface
  description: Web portal to browse, search, and view prokaryotic pan-genome profiles, functional
    annotations, and analyses by species.
  format: http
  id: propan.portal
  name: ProPan Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: propan
  product_url: https://ngdc.cncb.ac.cn/propan/home
- category: Product
  description: Bulk download of ProPan post-processed pan-genome datasets (gene clusters,
    annotations) by species.
  format: http
  id: propan.downloads
  name: ProPan Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: propan
  product_url: https://ngdc.cncb.ac.cn/propan/downloads
publications:
- authors:
  - Yadong Zhang
  - Hao Zhang
  - Zaichao Zhang
  - Qiheng Qian
  - Zhewen Zhang
  - Jingfa Xiao
  doi: 10.1093/nar/gkac832
  id: doi:10.1093/nar/gkac832
  journal: Nucleic Acids Research
  preferred: true
  title: 'ProPan: a comprehensive database for profiling prokaryotic pan-genome dynamics'
  year: '2023'
---

# ProPan

## Overview

ProPan is a database for profiling prokaryotic pan-genome dynamics, hosted by the China National Center for Bioinformation (CNCB). It gives gene content and functional annotation across 1,504 bacterial and archaeal species, with analyses of gene clustering, diversity, metabolism, and antibiotic resistance.

## Access

- ProPan browser: view pan-genome profiles and analyses by species.
- Downloads: post-processed pan-genome datasets.

## Citation

Please cite: Zhang Y, Zhang H, Zhang Z, Qian Q, Zhang Z, Xiao J. ProPan: a comprehensive database for profiling prokaryotic pan-genome dynamics. Nucleic Acids Res. 2023;51(D1):D767–D776. doi:10.1093/nar/gkac832
