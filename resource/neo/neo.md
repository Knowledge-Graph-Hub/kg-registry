---
layout: resource_detail
activity_status: active
id: neo
name: Noctua Entity Ontology
description: 'This repository contains classes required by Noctua/Minerva for representing
  entities that are object of ''enabled by'' relations, and similar molecular relationships.
  This includes: genes, protein (gene-level generic proteins and isoforms), functional
  RNAs, and complexes. These are represented as ontology classes, although NEO is
  not really an ontology in a conventional sense: there is no hierarchy, it is organized
  as a largely flat list.'
domains:
- biological systems
contacts:
- category: Individual
  label: Christopher J. Mungall
  orcid: 0000-0002-6601-2165
  contact_details:
  - contact_type: email
    value: cjmungall@lbl.gov
  - contact_type: github
    value: cmungall
homepage_url: https://github.com/geneontology/neo/
repository: https://github.com/geneontology/neo/
products:
- id: neo.model
  name: neo OWL release
  description: OWL release of neo
  category: Product
  product_url: http://purl.obolibrary.org/obo/go/noctua/neo.owl
  format: owl
  secondary_source:
  - neo
  original_source:
  - neo
category: Resource
---

Noctua Entity Ontology. Conversion of gene and gene-centric entity IDs from uniprot and MODs.
