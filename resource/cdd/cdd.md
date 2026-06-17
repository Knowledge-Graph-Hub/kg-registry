---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/Structure/cdd/cdd.shtml
  label: NCBI - National Center for Biotechnology Information
creation_date: '2026-06-17T00:00:00Z'
description: The Conserved Domain Database (CDD) is a resource for the annotation of
  functional units in proteins. It provides a collection of well-annotated multiple
  sequence alignment models for ancient domains and full-length proteins, available
  as position-specific score matrices for fast identification of conserved domains
  in protein sequences.
domains:
- proteomics
- genomics
homepage_url: https://www.ncbi.nlm.nih.gov/Structure/cdd/cdd.shtml
id: cdd
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
name: Conserved Domain Database
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching conserved protein domain
    models.
  format: http
  id: cdd.site
  is_public: true
  name: CDD Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cdd
  product_url: https://www.ncbi.nlm.nih.gov/Structure/cdd/cdd.shtml
- category: GraphicalInterface
  description: CD-Search tool for identifying conserved domains in a protein query
    sequence.
  format: http
  id: cdd.cdsearch
  is_public: true
  name: CD-Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cdd
  product_url: https://www.ncbi.nlm.nih.gov/Structure/cdd/wrpsb.cgi
- category: Product
  description: FTP archive of CDD domain models, alignments, and annotation data.
  format: mixed
  id: cdd.downloads
  name: CDD Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cdd
  product_url: https://ftp.ncbi.nih.gov/pub/mmdb/cdd/
publications:
- authors:
  - Jiyao Wang
  - Farideh Chitsaz
  - Myra K Derbyshire
  - Noreen R Gonzales
  - Marc Gwadz
  - Shennan Lu
  - Gabriele H Marchler
  - James S Song
  - Narmada Thanki
  - Roxanne A Yamashita
  - Mingzhang Yang
  - Dachuan Zhang
  - Chanjuan Zheng
  - Christopher J Lanczycki
  - Aron Marchler-Bauer
  doi: 10.1093/nar/gkac1096
  id: https://doi.org/10.1093/nar/gkac1096
  journal: Nucleic Acids Research
  preferred: true
  title: The conserved domain database in 2023
  year: '2023'
---
# Conserved Domain Database

The Conserved Domain Database (CDD), part of NCBI's Entrez system, is a resource for the
annotation of functional units (conserved domains) in proteins. It curates multiple
sequence alignment models for ancient domains and full-length proteins, and imports
domain models from external collections such as Pfam, SMART, COG, PRK, and TIGRFAMs.

Content and tools include:

- Curated and imported conserved domain models stored as position-specific score matrices
- The CD-Search and Batch CD-Search tools for domain annotation of query proteins
- SPARCLE functional classification of protein sequences
- FTP downloads of domain models and annotation data

GeneCards integrates conserved protein domain annotations from CDD.
