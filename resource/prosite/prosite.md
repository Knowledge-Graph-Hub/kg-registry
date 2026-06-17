---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://prosite.expasy.org/
  label: PROSITE Group - SIB Swiss Institute of Bioinformatics
creation_date: '2026-06-17T00:00:00Z'
description: PROSITE is a database of protein families and domains. It consists of
  documentation entries describing protein domains, families and functional sites,
  as well as associated patterns and profiles used to identify them, hosted at the
  SIB Swiss Institute of Bioinformatics.
domains:
- proteomics
- chemistry and biochemistry
homepage_url: https://prosite.expasy.org/
id: prosite
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc-nd/4.0/
  label: CC-BY-NC-ND-4.0
name: PROSITE
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching PROSITE documentation entries,
    patterns, and profiles.
  format: http
  id: prosite.site
  is_public: true
  name: PROSITE Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prosite
  product_url: https://prosite.expasy.org/
- category: GraphicalInterface
  description: Tool for scanning protein sequences against PROSITE patterns and profiles.
  format: http
  id: prosite.scanprosite
  is_public: true
  name: ScanProsite
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prosite
  product_url: https://prosite.expasy.org/scanprosite/
- category: Product
  description: Bulk downloads of PROSITE data files (patterns, profiles, and documentation).
  format: mixed
  id: prosite.downloads
  name: PROSITE Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prosite
  product_url: https://ftp.expasy.org/databases/prosite/
publications:
- authors:
  - Christian J. A. Sigrist
  - Edouard de Castro
  - Lorenzo Cerutti
  - Béatrice A. Cuche
  - Nicolas Hulo
  - Alan Bridge
  - Lydie Bougueleret
  - Ioannis Xenarios
  doi: 10.1093/nar/gks1067
  id: https://doi.org/10.1093/nar/gks1067
  journal: Nucleic Acids Research
  preferred: true
  title: New and continuing developments at PROSITE
  year: '2012'
---
# PROSITE

PROSITE is a protein domain and family database hosted at the SIB Swiss Institute of
Bioinformatics as part of the ExPASy resource portal. It provides documentation entries
that describe protein domains, families and functional sites, together with the patterns
(regular-expression-like signatures) and generalized profiles used to detect them in
protein sequences.

Key components include:

- Curated documentation entries describing protein families and domains
- PROSITE patterns and profiles for sequence-based detection
- The ScanProsite tool for matching sequences against PROSITE signatures
- Integration with the ProRule annotation rules

GeneCards integrates protein domain and family annotations from PROSITE.
