---
layout: resource_detail
activity_status: active
id: neo
name: Noctua Entity Ontology
description: >-
  This repository contains classes required by Noctua/Minerva for representing entities that are object of 'enabled by' relations, and similar molecular relationships. This includes: genes, protein (gene-level generic proteins and isoforms), functional RNAs, and complexes. These are represented as ontology classes, although NEO is not really an ontology in a conventional sense: there is no hierarchy, it is organized as a largely flat list.
domain: biological systems
contacts:
- category: Individual
  orcid: 0000-0002-6601-2165
  github: cmungall
  email: cjmungall@lbl.gov
  label: Christopher J. Mungall
homepage_url: https://github.com/geneontology/neo/
repository: https://github.com/geneontology/neo/
products:
- id: neo.model
  name: neo OWL release
  description: OWL release of neo
  category: Product
  url: http://purl.obolibrary.org/obo/go/noctua/neo.owl
  format: owl
  secondary_source:
  - neo
  original_source:
  - neo
category: Resource

---

Noctua Entity Ontology. Conversion of gene and gene-centric entity IDs from uniprot and MODs.
