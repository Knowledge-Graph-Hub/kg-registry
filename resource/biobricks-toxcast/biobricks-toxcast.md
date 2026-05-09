---
activity_status: active
category: KnowledgeGraph
collection:
  - okn
contacts:
  - category: Individual
    label: Tom Luechtefeld
    contact_details:
      - contact_type: email
        value: tom@insilica.co
      - contact_type: github
        value: tomlue
  - category: Individual
    contact_details:
      - contact_type: email
        value: tom@insilica.co
    label: Tom Luechtefeld
description: BioBricks ToxCast is an open knowledge graph for EPA ToxCast high-throughput screening data.
domains:
  - toxicology
homepage_url: https://github.com/biobricks-ai/biobricks-okg
id: biobricks-toxcast
layout: resource_detail
name: BioBricks ToxCast
products:
  - category: ProgrammingInterface
    description: SPARQL endpoint for BioBricks ToxCast
    id: biobricks-toxcast.sparql
    name: BioBricks ToxCast SPARQL
    original_source:
      - source: biobricks-toxcast
        relation_type: prov:hadPrimarySource
    product_url: https://frink.apps.renci.org/biobricks-toxcast/sparql
  - id: biobricks-toxcast.tpf
    name: BioBricks ToxCast TPF
    description: Triple Pattern Fragments endpoint for BioBricks ToxCast
    category: ProgrammingInterface
    product_url: https://frink.apps.renci.org/ldf/biobricks-toxcast
    original_source:
      - source: biobricks-toxcast
        relation_type: prov:hadPrimarySource
repository: https://github.com/biobricks-ai/biobricks-okg
creation_date: '2025-12-08T00:00:00Z'
last_modified_date: '2026-03-30T00:00:00Z'
---

BioBricks ToxCast

## Automated Evaluation

- View the automated evaluation: [biobricks-toxcast automated evaluation](biobricks-toxcast_eval_automated.html)
