---
layout: ontology_detail
activity_status: active
id: ubergraph
title: Ubergraph
description: Ubergraph is an RDF triplestore integrating OBO ontologies into a unified semantic graph
domain: information
restype: "knowledge graph"
contact:
  orcid: 0000-0002-8688-6599
  github: balhoff
  email: balhoff@renci.org
  label: James P. Balhoff
homepage: https://ubergraph.apps.renci.org/sparql
tracker: https://github.com/INCATools/ubergraph/issues
repository: https://github.com/INCATools/ubergraph
products:
- id: ubergraph.rdf
  title: Ubergraph RDF
  description: RDF of Ubergraph
  ontology_purl: https://ubergraph.apps.renci.org/sparql
- id: ubergraph.blazegraph.jnl
  title: Ubergraph blazegraph journal
  description: Blazegraph journal of Ubergraph
  ontology_purl: https://ubergraph.apps.renci.org/downloads/current/ubergraph.jnl.gz
- id: ubergraph.nquads
  title: Ubergraph n-quads
  description: Ubergraph n-quads
  ontology_purl:  https://ubergraph.apps.renci.org/downloads/current/ubergraph.nq.gz  
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
---

### Ubergraph: A Unified Semantic Knowledge Graph for OBO Ontologies

Ubergraph is an RDF triplestore and public SPARQL query endpoint that integrates a suite of **39 OBO ontologies**, precomputing OWL inferences into a traversable **knowledge graph**. This enables efficient semantic reasoning over multiple ontologies, without requiring extensive local computation.

### Features
- **SP
