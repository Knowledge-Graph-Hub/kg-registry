---
id: ncipidkg
name: NCI-PID 2.0 KG
description: The NCI-PID 2.0 Knowledge Graph converts NCI Pathway Interaction Database
  version 2.0 networks into RDF, capturing protein interactions, signaling pathways,
  and post-translational modifications enriched with INDRA evidence metadata.
activity_status: active
homepage_url: https://www.ndexbio.org/index.html#/networkset/7bc65b82-2a2f-11ed-ac45-0ac135e8bacf
contacts:
- category: Individual
  label: Cytoscape and NDEx Team
  contact_details:
  - contact_type: email
    value: support@ndexbio.org
collection:
- okn
layout: resource_detail
category: KnowledgeGraph
creation_date: '2026-03-30T00:00:00Z'
last_modified_date: '2026-05-29T00:00:00Z'
products:
- id: ncipidkg.sparql
  name: NCI-PID 2.0 KG SPARQL
  description: SPARQL endpoint for NCI-PID 2.0 KG
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/ncipidkg/sparql
  original_source:
  - source: ncipidkg
    relation_type: prov:hadPrimarySource
- id: ncipidkg.tpf
  name: NCI-PID 2.0 KG TPF
  description: Triple Pattern Fragments endpoint for NCI-PID 2.0 KG
  category: ProgrammingInterface
  format: http
  product_url: https://apps.okn.us/ldf/ncipidkg
  original_source:
  - source: ncipidkg
    relation_type: prov:hadPrimarySource
domains:
- general
---
NCI-PID 2.0 KG

## Description

The NCI-PID 2.0 Knowledge Graph converts NCI Pathway Interaction Database version 2.0 networks into RDF, capturing protein interactions, signaling pathways, and post-translational modifications enriched with INDRA evidence metadata.

*This resource was automatically synchronized from the FRINK OKN registry.*
