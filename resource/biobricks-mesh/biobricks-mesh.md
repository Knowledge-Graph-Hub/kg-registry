---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: tom@insilica.co
  - contact_type: github
    value: tomlue
  label: Tom Luechtefeld
- category: Individual
  contact_details:
  - contact_type: email
    value: tom@insilica.co
  label: Tom Luechtefeld
creation_date: '2025-12-08T00:00:00Z'
description: BioBricks MeSH is an open knowledge graph of Medical Subject Headings
  (MeSH) biomedical vocabulary.
domains:
- biomedical
homepage_url: https://github.com/biobricks-ai/mesh-kg
id: biobricks-mesh
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
name: BioBricks MeSH
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for BioBricks MeSH
  format: http
  id: biobricks-mesh.sparql
  name: BioBricks MeSH SPARQL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobricks-mesh
  product_url: https://apps.okn.us/biobricks-mesh/sparql
- category: ProgrammingInterface
  description: Triple Pattern Fragments endpoint for BioBricks MeSH
  id: biobricks-mesh.tpf
  name: BioBricks MeSH TPF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobricks-mesh
  product_url: https://apps.okn.us/ldf/biobricks-mesh
- category: GraphProduct
  description: RDF knowledge graph (Turtle) repackaging the MeSH biomedical vocabulary
    as an open knowledge graph
  format: ttl
  id: biobricks-mesh.graph
  name: BioBricks MeSH Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobricks-mesh
  - relation_type: prov:wasDerivedFrom
    source: mesh
  product_url: https://github.com/biobricks-ai/mesh-kg
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-10: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-07-15: HTTP 404 error
    when accessing file'
repository: https://github.com/biobricks-ai/mesh-kg
---
BioBricks MeSH

## Automated Evaluation

- View the automated evaluation: [biobricks-mesh automated evaluation](biobricks-mesh_eval_automated.html)