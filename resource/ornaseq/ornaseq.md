---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  label: Stephen Fisher
  orcid: 0000-0001-8034-7685
  contact_details:
  - contact_type: email
    value: safisher@upenn.edu
  - contact_type: github
    value: safisher
creation_date: '2025-09-29T00:00:00Z'
description: An application ontology designed to annotate next-generation sequencing
  experiments performed on RNA.
domains:
- biomedical
- general
homepage_url: http://kim.bio.upenn.edu/software/ornaseq.shtml
id: ornaseq
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Ontology of RNA Sequencing
products:
- category: OntologyProduct
  description: Ontology of RNA Sequencing in OWL format
  format: owl
  id: ornaseq.owl
  name: ornaseq.owl
  product_file_size: 27418
  product_url: http://purl.obolibrary.org/obo/ornaseq.owl
  original_source:
  - source: ornaseq
    relation_type: prov:hadPrimarySource
- id: ornaseq.kg-bioportal
  name: ORNASEQ KGX graph (KG-Bioportal)
  category: GraphProduct
  description: KGX TSV transform of Ontology of RNA Sequencing (ORNASEQ), produced
    by KG-Bioportal from the BioPortal submission. The archive contains ORNASEQ_nodes.tsv
    and ORNASEQ_edges.tsv.
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/ORNASEQ.tar.gz
  format: kgx
  compression: targz
  original_source:
  - source: ornaseq
    relation_type: prov:hadPrimarySource
  node_count: 203
  edge_count: 332
repository: https://github.com/safisher/ornaseq
publications: []
---
## Description

An application ontology designed to annotate next-generation sequencing experiments performed on RNA.

## Contacts

- Stephen Fisher (safisher@upenn.edu) [ORCID: 0000-0001-8034-7685](https://orcid.org/0000-0001-8034-7685)

## Products

### ornaseq.owl

Ontology of RNA Sequencing in OWL format

**URL**: [http://purl.obolibrary.org/obo/ornaseq.owl](http://purl.obolibrary.org/obo/ornaseq.owl)

**Format**: owl

**Domains**: biomedical

---

*This resource was automatically synchronized from the OBO Foundry registry.*
