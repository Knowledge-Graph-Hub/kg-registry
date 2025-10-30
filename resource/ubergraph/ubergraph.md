---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: balhoff@renci.org
      - contact_type: github
        value: balhoff
    label: James P. Balhoff
    orcid: 0000-0002-8688-6599
description: Ubergraph is an RDF triplestore integrating OBO ontologies into a unified semantic graph
domains:
  - other
homepage_url: https://ubergraph.apps.renci.org/sparql
id: ubergraph
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Ubergraph
products:
  - category: Product
    description: RDF of Ubergraph
    id: ubergraph.rdf
    name: Ubergraph RDF
    original_source:
      - ubergraph
    product_file_size: 6866918
    product_url: https://ubergraph.apps.renci.org/sparql
    secondary_source:
      - ubergraph
  - category: Product
    description: Blazegraph journal of Ubergraph
    id: ubergraph.blazegraph.jnl
    name: Ubergraph blazegraph journal
    original_source:
      - ubergraph
    product_file_size: 9157530809
    product_url: https://ubergraph.apps.renci.org/downloads/current/ubergraph.jnl.gz
    secondary_source:
      - ubergraph
  - category: Product
    description: Ubergraph n-quads
    format: nquads
    id: ubergraph.nquads
    name: Ubergraph n-quads
    original_source:
      - ubergraph
    product_file_size: 3718641146
    product_url: https://ubergraph.apps.renci.org/downloads/current/ubergraph.nq.gz
    secondary_source:
      - ubergraph
  - category: GraphProduct
    description: UberGraph Automat
    format: kgx-jsonl
    id: automat.ubergraph
    name: ubergraph_automat
    original_source:
      - ubergraph
    product_url: https://stars.renci.org/var/plater/bl-4.2.1/UbergraphRedundant_Automat/e6b3204fd3a04413/
    secondary_source:
      - automat
repository: https://github.com/INCATools/ubergraph
infores_id: ubergraph
---

### Ubergraph: A Unified Semantic Knowledge Graph for OBO Ontologies

Ubergraph is an RDF triplestore and public SPARQL query endpoint that integrates a suite of **39 OBO ontologies**, precomputing OWL inferences into a traversable **knowledge graph**. This enables efficient semantic reasoning over multiple ontologies, without requiring extensive local computation.
