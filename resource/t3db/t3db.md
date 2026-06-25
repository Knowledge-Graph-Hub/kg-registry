---
activity_status: active
category: DataSource
creation_date: '2026-06-18T00:00:00Z'
description: The Toxin and Toxin Target Database (T3DB), also known as the Toxic Exposome
  Database, is a bioinformatics resource from the Wishart lab that combines detailed
  toxin data with comprehensive toxin target information. It covers thousands of toxins,
  including pollutants, pesticides, drugs, and food toxins, annotated with chemical,
  toxicological, mechanistic, and target details across more than 90 data fields per
  record. Each toxin is linked to its corresponding protein, gene, or other molecular
  targets along with the associated mechanisms of toxicity. T3DB is an upstream
  primary source for PharmDB.
domains:
- toxicology
- chemistry and biochemistry
- pharmacology
homepage_url: http://www.t3db.ca/
id: t3db
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: "Toxin and Toxin Target Database"
products:
- category: GraphicalInterface
  description: Web portal for browsing and searching T3DB toxins, their targets, and
    mechanisms of toxicity, with detailed annotation pages for each toxin record.
  format: http
  id: t3db.portal
  name: T3DB Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: t3db
  product_url: http://www.t3db.ca/
- category: DataSource
  description: Bulk downloads of the full T3DB dataset, including toxin records, toxin
    target records, and toxin-target associations in formats such as XML and SDF.
    Use is governed by the T3DB terms of use.
  format: xml
  id: t3db.downloads
  name: T3DB Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: t3db
  product_url: http://www.t3db.ca/downloads
  warnings:
  - URL returned HTTP 403 when checked on 2026-06-18 because the site is served behind
    a Cloudflare bot challenge (Cf-Mitigated_ challenge)_ the server is responding
    and the site is reachable in a standard browser.
publications:
- authors:
  - Wishart D
  - Arndt D
  - Pon A
  - Sajed T
  - Guo AC
  - Djoumbou Y
  - Knox C
  - Wilson M
  - Liang Y
  - Grant J
  - Liu Y
  - Goldansaz SA
  - Rappaport SM
  doi: 10.1093/nar/gku1004
  id: https://pubmed.ncbi.nlm.nih.gov/25378312/
  journal: Nucleic Acids Res
  preferred: true
  title: 'T3DB: the toxic exposome database'
  year: '2015'
---
# Toxin and Toxin Target Database (T3DB)

## Overview

The Toxin and Toxin Target Database (T3DB), also called the Toxic Exposome Database, is a curated bioinformatics resource developed by the Wishart lab that pairs detailed toxin records with comprehensive information about their molecular targets. Each toxin is described across more than 90 data fields and linked to the proteins, genes, or other targets it acts upon, together with the mechanisms by which it exerts its toxic effects.

## Scope & Content

- Thousands of toxins, including environmental pollutants, pesticides, drugs, and food toxins
- Chemical, physical, and toxicological property annotations for each toxin
- Toxin target records (proteins, genes, and other molecular targets)
- Toxin-target associations describing mechanisms of toxicity
- Cross-references to external chemical and biomedical resources

## Use Cases

- Computational and mechanistic toxicology research
- Linking chemical exposures to molecular targets and adverse effects
- Building integrated knowledge graphs of toxins, targets, and mechanisms
- Serving as an upstream primary source for downstream resources such as PharmDB

## Access

T3DB is available through its public web portal at http://www.t3db.ca/, which supports browsing and searching of toxin and target records. Bulk data downloads (e.g., XML and SDF) are provided via the downloads page; use is subject to the T3DB terms of use.

## Citation & Attribution

When using T3DB, cite Wishart D et al., "T3DB: the toxic exposome database," Nucleic Acids Research, 2015 (doi:10.1093/nar/gku1004).
