---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://asntech.org/dbsuper/
  label: dbSUPER
creation_date: '2026-06-17T00:00:00Z'
description: dbSUPER is an integrated and interactive database of super-enhancers in
  mouse and human genomes. It provides a centralized resource of super-enhancer
  regions with associated genes, cell and tissue types, and supporting genomic data
  to assist studies of transcriptional control of cell identity and disease.
domains:
- genomics
- systems biology
homepage_url: https://asntech.org/dbsuper/
id: dbsuper
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
name: dbSUPER
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching super-enhancers across cell
    and tissue types.
  format: http
  id: dbsuper.site
  is_public: true
  name: dbSUPER Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  product_url: https://asntech.org/dbsuper/
- category: Product
  description: Downloadable super-enhancer datasets in BED and other formats.
  format: mixed
  id: dbsuper.downloads
  name: dbSUPER Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  product_url: https://asntech.org/dbsuper/download.php
publications:
- authors:
  - Aziz Khan
  - Xuegong Zhang
  doi: 10.1093/nar/gkv1002
  id: https://doi.org/10.1093/nar/gkv1002
  journal: Nucleic Acids Research
  preferred: true
  title: 'dbSUPER: a database of super-enhancers in mouse and human genome'
  year: '2016'
---
# dbSUPER

dbSUPER is a database of super-enhancers in the mouse and human genomes. Super-enhancers
are large clusters of transcriptional enhancers that drive expression of genes defining
cell identity, and dbSUPER provides a centralized, interactive resource for exploring
them.

Content includes:

- Super-enhancer regions identified across many cell and tissue types
- Associated genes and overlapping genomic features
- Downloadable datasets for further analysis

GeneCards integrates super-enhancer annotations from dbSUPER.
