---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://scop.mrc-lmb.cam.ac.uk/
  label: MRC Laboratory of Molecular Biology
creation_date: '2026-06-17T00:00:00Z'
description: SCOP (Structural Classification of Proteins) is a classification of
  protein domains based on their structural and evolutionary relationships. It
  organizes domains of known three-dimensional structure into a hierarchy that
  reflects both structural similarity and evolutionary origin.
domains:
- proteomics
homepage_url: https://scop.mrc-lmb.cam.ac.uk/
id: scop
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
name: SCOP
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching the structural classification
    of protein domains.
  format: http
  id: scop.site
  is_public: true
  name: SCOP Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: scop
  product_url: https://scop.mrc-lmb.cam.ac.uk/
publications:
- authors:
  - Antonina Andreeva
  - Eugene Kulesha
  - Julian Gough
  - Alexey G Murzin
  doi: 10.1093/nar/gkz1064
  id: https://doi.org/10.1093/nar/gkz1064
  journal: Nucleic Acids Research
  preferred: true
  title: 'The SCOP database in 2020: expanded classification of representative family and superfamily domains of known protein structures'
  year: '2020'
---
# SCOP

SCOP (Structural Classification of Proteins) provides a comprehensive, largely manual
classification of protein domains of known three-dimensional structure. Domains are
grouped into a hierarchy of types, classes, folds, superfamilies, and families that
captures both structural similarity and inferred evolutionary relationships.

Content includes:

- Hierarchical classification of protein structural domains
- Family- and superfamily-level evolutionary relationships
- Representative domains linked to entries in the Protein Data Bank

GeneCards integrates protein structural classification data from SCOP.
