---
layout: ontology_detail
activity_status: active
id: ubergraph
title: Ubergraph
description: Ubergraph is an RDF triplestore integrating OBO ontologies into a unified semantic graph
domain: information
restype: "knowledge graph"
contact:
  - orcid: 0000-0003-1319-7955
    github: balhoff
    email: balhoff@renci.org
    label: James P. Balhoff
homepage: https://ubergraph.apps.renci.org/sparql
tracker: https://github.com/INCATools/ubergraph/issues
repository: https://github.com/INCATools/ubergraph
products:
- id: ubergraph
  title: Ubergraph Blazegraph Database
  description: A Blazegraph RDF database containing precomputed OWL inferences for OBO ontologies
  ontology_purl: https://ubergraph.apps.renci.org/sparql
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
---

### Ubergraph: A Unified Semantic Knowledge Graph for OBO Ontologies

Ubergraph is an RDF triplestore and public SPARQL query endpoint that integrates a suite of **39 OBO ontologies**, precomputing OWL inferences into a traversable **knowledge graph**. This enables efficient semantic reasoning over multiple ontologies, without requiring extensive local computation.

### Features
- **SPARQL Query Interface:** Provides a web-based endpoint for querying OBO ontologies.
- **Precomputed OWL Inferences:** Stores OWL-based logical inferences as RDF triples for fast access.
- **Relation Graphs:** Simplifies ontology access by storing subclass and existential relations as standard RDF triples.
- **Ontology Classification:** Uses the **ELK reasoner** to compute class hierarchies.
- **Biolink Model Integration:** Connects OBO terms to Biolink categories.

