---
category: GraphProduct
description: The SAWGraph Facilities and Industries Ontology (FIO) / Facility Registry
  Service (FRS) knowledge graph, an RDF (Turtle) graph representing US facilities
  from EPA's Facility Registry Service together with their NAICS and SIC industry
  classifications and spatial locations. It is served through the SAWGraph FRS SPARQL
  and Triple Pattern Fragments endpoints.
format: ttl
id: fiokg.graph
name: SAWGraph FRS Knowledge Graph
original_source:
- relation_type: prov:hadPrimarySource
  source: fiokg
- relation_type: prov:wasDerivedFrom
  source: sawgraph
- relation_type: prov:hadPrimarySource
  source: epa-frs
product_url: https://github.com/SAWGraph/fio
secondary_source:
- relation_type: prov:wasInfluencedBy
  source: naics
- relation_type: prov:wasInfluencedBy
  source: sic
layout: product_detail
---
