---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://pax-db.org/
  label: PaxDb
creation_date: '2026-06-17T00:00:00Z'
description: PaxDb (Protein Abundance Database) is a database of whole-organism protein
  abundance information across organisms. It integrates and re-processes quantitative
  proteomics datasets to provide consistent, comparable protein abundance estimates
  for thousands of proteins in many species.
domains:
- proteomics
homepage_url: https://pax-db.org/
id: paxdb
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
name: PaxDb
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching protein abundance data across
    organisms.
  format: http
  id: paxdb.site
  is_public: true
  name: PaxDb Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: paxdb
  product_url: https://pax-db.org/
- category: Product
  description: Bulk downloads of protein abundance datasets by organism.
  format: mixed
  id: paxdb.downloads
  name: PaxDb Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: paxdb
  product_url: https://pax-db.org/downloads/latest/
publications:
- authors:
  - Qingyao Huang
  - Damian Szklarczyk
  - John Oehninger
  - Christian von Mering
  doi: 10.1093/nar/gkaf1066
  id: https://doi.org/10.1093/nar/gkaf1066
  journal: Nucleic Acids Research
  preferred: true
  title: 'PaxDb v6.0: reprocessed, LLM-selected, curated protein abundance data across organisms'
  year: '2026'
---
# PaxDb

PaxDb (Protein Abundance Database) is a resource of protein abundance data spanning many
organisms. It collects quantitative proteomics datasets, re-processes them through a
unified pipeline, and maps them to a common namespace so that abundance values can be
compared within and across species.

Content includes:

- Whole-organism protein abundance estimates derived from mass spectrometry datasets
- Integrated ("whole organism") and tissue/condition-specific datasets
- Consistent, comparable abundance values across thousands of proteins and many species
- Bulk downloads of abundance data

GeneCards integrates protein abundance data from PaxDb.
