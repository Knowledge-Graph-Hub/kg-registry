---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://proteininformationresource.org/pirsf/
  label: Protein Information Resource (PIR)
creation_date: '2026-06-17T00:00:00Z'
description: PIRSF (Protein Information Resource SuperFamily) is a network classification
  system of proteins based on their evolutionary relationships of whole proteins.
  It provides a hierarchical classification reflecting both functional and evolutionary
  relationships among protein families.
domains:
- proteomics
homepage_url: https://proteininformationresource.org/pirsf/
id: pirsf
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
name: PIRSF
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching the PIRSF protein family
    classification.
  format: http
  id: pirsf.site
  is_public: true
  name: PIRSF Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pirsf
  product_url: https://proteininformationresource.org/pirsf/
- category: Product
  description: Bulk downloads of PIRSF family classification data files.
  format: mixed
  id: pirsf.downloads
  name: PIRSF Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pirsf
  product_url: https://ftp.proteininformationresource.org/pir_databases/pirsf/
publications:
- authors:
  - C. H. Wu
  doi: 10.1093/nar/gkh097
  id: https://doi.org/10.1093/nar/gkh097
  journal: Nucleic Acids Research
  preferred: true
  title: 'PIRSF: family classification system at the Protein Information Resource'
  year: '2004'
---
# PIRSF

PIRSF (Protein Information Resource SuperFamily) is a protein classification system
developed at the Protein Information Resource (PIR). It organizes proteins into a network
structure of families based on full-length protein similarity, capturing both functional
and evolutionary relationships.

Content includes:

- Hierarchical protein family classification (homeomorphic families and superfamilies)
- Family-level functional and evolutionary annotations
- Downloadable classification data

GeneCards integrates protein family classifications from PIRSF.
