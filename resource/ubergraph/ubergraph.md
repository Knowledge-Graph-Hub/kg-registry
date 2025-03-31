---
layout: resource_detail
activity_status: active
id: ubergraph
name: Ubergraph
description: Ubergraph is an RDF triplestore integrating OBO ontologies into a unified semantic graph
domains:
- other
category: KnowledgeGraph
contacts:
- category: Individual
  orcid: 0000-0002-8688-6599
  github: balhoff
  email: balhoff@renci.org
  label: James P. Balhoff
homepage_url: https://ubergraph.apps.renci.org/sparql
repository: https://github.com/INCATools/ubergraph
products:
- id: ubergraph.rdf
  name: Ubergraph RDF
  description: RDF of Ubergraph
  product_url: https://ubergraph.apps.renci.org/sparql
  category: Product
  original_source:
  - ubergraph
  secondary_source:
  - ubergraph
- id: ubergraph.blazegraph.jnl
  name: Ubergraph blazegraph journal
  description: Blazegraph journal of Ubergraph
  product_url: https://ubergraph.apps.renci.org/downloads/current/ubergraph.jnl.gz
  category: Product
  original_source:
  - ubergraph
  secondary_source:
  - ubergraph
- id: ubergraph.nquads
  name: Ubergraph n-quads
  description: Ubergraph n-quads
  product_url: https://ubergraph.apps.renci.org/downloads/current/ubergraph.nq.gz
  category: Product
  original_source:
  - ubergraph
  secondary_source:
  - ubergraph
  format: nquads
license:
  label: CC BY 4.0
  id: https://creativecommons.org/licenses/by/4.0/
---

### Ubergraph: A Unified Semantic Knowledge Graph for OBO Ontologies

Ubergraph is an RDF triplestore and public SPARQL query endpoint that integrates a suite of **39 OBO ontologies**, precomputing OWL inferences into a traversable **knowledge graph**. This enables efficient semantic reasoning over multiple ontologies, without requiring extensive local computation.
