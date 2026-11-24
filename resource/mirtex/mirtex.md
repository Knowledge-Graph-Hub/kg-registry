---
activity_status: unknown
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: pirmail@georgetown.edu
  - contact_type: url
    value: https://proteininformationresource.org/
  label: Protein Information Resource
creation_date: '2026-11-24T00:00:00Z'
description: miRTex is a text mining system for microRNA relations in the literature, extracting
  microRNA-target relations along with microRNA-gene and gene-microRNA regulation relations.
  Results for Medline abstracts were made available for query and download through the Protein
  Information Resource.
domains:
- genomics
- literature
- natural language processing
- non-coding RNA
- gene regulation
funding:
- National Institute of General Medical Sciences (P20GM103446)
homepage_url: https://proteininformationresource.org/mirtex/
id: mirtex
last_modified_date: '2026-11-24T00:00:00Z'
layout: resource_detail
name: miRTex
products:
- category: GraphicalInterface
  description: Web interface for querying and downloading microRNA relations mined from Medline
    abstracts.
  format: http
  id: mirtex.portal
  name: miRTex Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mirtex
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://proteininformationresource.org/mirtex/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: pir
  warnings:
  - The site returned HTTP 503 when checked on 2026-11-24.
publications:
- authors:
  - Gang Li
  - Karen E. Ross
  - Cecilia N. Arighi
  - Yifan Peng
  - Cathy H. Wu
  - K. Vijay-Shanker
  doi: 10.1371/journal.pcbi.1004391
  id: doi:10.1371/journal.pcbi.1004391
  journal: PLOS Computational Biology
  preferred: true
  title: 'miRTex: A Text Mining System for miRNA-Gene Relation Extraction'
  year: '2015'
warnings:
- The miRTex site returned HTTP 503 (temporarily unavailable) on every check on 2026-11-24.
  The PIR home page still lists miRTex.
---

# miRTex

miRTex is a text mining system for microRNA-gene relations, offered through the `pir` site alongside
`rlims-p` and `iptmnet`. Its published evaluation gives F-scores close to 0.90 on three relation types
over 150 abstracts.
