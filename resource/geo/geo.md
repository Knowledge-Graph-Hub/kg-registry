---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: hoganwr@gmail.com
  - contact_type: github
    value: hoganwr
  label: Bill Hogan
  orcid: 0000-0002-9881-1017
creation_date: '2025-09-29T00:00:00Z'
description: An ontology of geographical entities
domains:
- environment
- geographic information systems
homepage_url: https://github.com/ufbmi/geographical-entity-ontology/wiki
id: geo
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Geographical Entity Ontology
products:
- category: OntologyProduct
  description: Geographical Entity Ontology in OWL format
  format: owl
  id: geo.owl
  name: geo.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geo
  product_file_size: 17397
  product_url: http://purl.obolibrary.org/obo/geo.owl
- category: DocumentationProduct
  description: GEO project wiki describing the ontology rationale, modular architecture,
    and release locations.
  format: http
  id: geo.docs
  name: GEO Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geo
  product_url: https://github.com/ufbmi/geographical-entity-ontology/wiki
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Geographical Entity Ontology (GEO), produced by
    KG-Bioportal from the BioPortal submission. The archive contains GEO_nodes.tsv
    and GEO_edges.tsv.
  edge_count: 0
  format: kgx
  id: geo.kg-bioportal
  latest_version: production version 2018-02-23
  name: GEO KGX graph (KG-Bioportal)
  node_count: 3
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geo
  product_file_size: 390
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.08/GEO.tar.gz
publications: []
repository: https://github.com/ufbmi/geographical-entity-ontology
---
## Description

The Geographical Entity Ontology (GEO) models geographical entities in a way
that cleanly separates geopolitical organizations from the territories or regions
over which they have jurisdiction. Its rationale explicitly addresses cases such
as the United States, where the governing nation and the geographical region it
governs should not be treated as the same thing.

The current GEO release is modular: the main `geo.owl` file provides the core
ontology, while many individuals and specialized geography modules are published
as separate OWL files. The project wiki documents that modular architecture and
the ontology's distinction among geographical regions, land masses, bodies of
water, governmental organizations, and related entities.

## Contacts

- Bill Hogan (hoganwr@gmail.com) [ORCID: 0000-0002-9881-1017](https://orcid.org/0000-0002-9881-1017)

## Products

### geo.owl

Geographical Entity Ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/geo.owl](http://purl.obolibrary.org/obo/geo.owl)

**Format**: owl

**Domains**: environment

---

*This resource was automatically synchronized from the OBO Foundry registry.*