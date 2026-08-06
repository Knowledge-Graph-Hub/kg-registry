---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  label: Martin Ramirez
  orcid: 0000-0002-0358-0130
  contact_details:
  - contact_type: email
    value: ramirez@macn.gov.ar
  - contact_type: github
    value: martinjramirez
creation_date: '2025-09-29T00:00:00Z'
description: An ontology for spider comparative biology including anatomical parts
  (e.g. leg, claw), behavior (e.g. courtship, combing) and products (i.g. silk, web,
  borrow).
domains:
- anatomy and development
homepage_url: http://research.amnh.org/atol/files/
id: spd
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Spider Ontology
products:
- category: OntologyProduct
  description: Spider Ontology in OWL format
  format: owl
  id: spd.owl
  name: spd.owl
  product_file_size: 69679
  product_url: http://purl.obolibrary.org/obo/spd.owl
  original_source:
  - source: spd
    relation_type: prov:hadPrimarySource
- id: spd.kg-bioportal
  name: SPD KGX graph (KG-Bioportal)
  category: GraphProduct
  description: KGX TSV transform of Spider Anatomy Ontology (SPD), produced by KG-Bioportal
    from the BioPortal submission. The archive contains SPD_nodes.tsv and SPD_edges.tsv.
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/SPD.tar.gz
  format: kgx
  compression: targz
  original_source:
  - source: spd
    relation_type: prov:hadPrimarySource
  node_count: 853
  edge_count: 1214
  latest_version: '1.1'
repository: https://github.com/obophenotype/spider-ontology
taxon:
- NCBITaxon:6893
publications:
- authors:
  - Martín J. Ramírez
  - Peter Michalik
  doi: 10.3390/d11100202
  id: https://doi.org/10.3390/d11100202
  journal: Diversity
  title: The Spider Anatomy Ontology (SPD) A Versatile Tool to Link Anatomy with Cross-Disciplinary
    Data
  year: '2019'
---
## Description

An ontology for spider comparative biology including anatomical parts (e.g. leg, claw), behavior (e.g. courtship, combing) and products (i.g. silk, web, borrow).

## Contacts

- Martin Ramirez (ramirez@macn.gov.ar) [ORCID: 0000-0002-0358-0130](https://orcid.org/0000-0002-0358-0130)

## Products

### spd.owl

Spider Ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/spd.owl](http://purl.obolibrary.org/obo/spd.owl)

**Format**: owl

## Publications

- [The Spider Anatomy Ontology (SPD) A Versatile Tool to Link Anatomy with Cross-Disciplinary Data](https://doi.org/10.3390/d11100202)

**Domains**: anatomy and development

**Taxon**: NCBITaxon:6893

---

*This resource was automatically synchronized from the OBO Foundry registry.*
