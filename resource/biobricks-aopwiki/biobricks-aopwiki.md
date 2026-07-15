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
description: BioBricks AOP-Wiki is an open knowledge graph for Adverse Outcome Pathways
  from the AOP-Wiki.
domains:
- toxicology
- biological systems
homepage_url: https://github.com/biobricks-ai/aopwikirdf-kg
id: biobricks-aopwiki
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
name: BioBricks AOP-Wiki
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for BioBricks AOP-Wiki
  format: http
  id: biobricks-aopwiki.sparql
  name: BioBricks AOP-Wiki SPARQL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobricks-aopwiki
  product_url: https://apps.okn.us/biobricks-aopwiki/sparql
- category: ProgrammingInterface
  description: Triple Pattern Fragments endpoint for BioBricks AOP-Wiki
  id: biobricks-aopwiki.tpf
  name: BioBricks AOP-Wiki TPF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobricks-aopwiki
  product_url: https://apps.okn.us/ldf/biobricks-aopwiki
- category: GraphProduct
  description: RDF knowledge graph (Turtle) repackaging AOP-Wiki data as an open knowledge
    graph
  format: ttl
  id: biobricks-aopwiki.graph
  name: BioBricks AOP-Wiki Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobricks-aopwiki
  - relation_type: prov:wasDerivedFrom
    source: aop-wiki
  product_url: https://github.com/biobricks-ai/aopwikirdf-kg
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-10: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-07-15: HTTP 404 error
    when accessing file'
repository: https://github.com/biobricks-ai/aopwikirdf-kg
---
BioBricks AOP-Wiki

## Automated Evaluation

- View the automated evaluation: [biobricks-aopwiki automated evaluation](biobricks-aopwiki_eval_automated.html)