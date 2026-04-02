---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: balhoff@renci.org
  - contact_type: github
    value: balhoff
  label: Jim Balhoff
- category: Individual
  contact_details:
  - contact_type: email
    value: balhoff@renci.org
  - contact_type: github
    value: balhoff
  label: James P. Balhoff
  orcid: 0000-0002-8688-6599
creation_date: '2025-03-09T00:00:00Z'
description: Integrated suite of OBO ontologies with precomputed inferred relationships
domains:
- other
homepage_url: https://github.com/INCATools/ubergraph/
id: ubergraph
infores_id: ubergraph
last_modified_date: '2026-03-30T00:00:00Z'
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
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for Ubergraph distributed via the NCATS Translator
    release site (release 2026_03_27; build ubergraph_2026-03-08_0fef3756_2025sep1_4.3.6;
    source version 2026-03-08; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 9937241
  format: kgx-jsonl
  id: translator.ubergraph.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Ubergraph KGX Graph
  node_count: 580326
  original_source:
  - ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/ubergraph/latest/
  secondary_source:
  - translator
  versions:
  - '2026_03_27'
  - ubergraph_2026-03-08_0fef3756_2025sep1_4.3.6
- category: ProgrammingInterface
  description: SPARQL endpoint for Ubergraph
  id: ubergraph.sparql
  name: Ubergraph SPARQL
  original_source:
  - ubergraph
  product_url: https://frink.apps.renci.org/ubergraph/sparql
- category: ProgrammingInterface
  description: Triple Pattern Fragments endpoint for Ubergraph
  id: ubergraph.tpf
  name: Ubergraph TPF
  original_source:
  - ubergraph
  product_url: https://frink.apps.renci.org/ldf/ubergraph
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: Aggregated KGX JSONL graph package combining 29 Translator release
    sources (release 2026_03_27; build 423af7989cac; Biolink 4.3.6; Node Normalizer
    2025sep1).
  edge_count: 29243943
  format: kgx-jsonl
  id: translator.translator_kg.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Aggregate KGX Graph
  node_count: 1696790
  original_source:
  - alliance
  - bgee
  - bindingdb
  - chembl
  - cohd
  - ctd
  - ctkp
  - drug-approvals-kp
  - dgidb
  - diseases
  - drugrephub
  - drugcentral
  - gtopdb
  - gene2phenotype
  - geneticskp
  - go-cam
  - goa
  - hp
  - icees-kg
  - intact
  - ncbigene
  - panther
  - pathbank
  - semmeddb
  - sider
  - signor
  - text-mining-kp
  - ttd
  - ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
  secondary_source:
  - translator
  versions:
  - '2026_03_27'
  - 423af7989cac
repository: https://github.com/INCATools/ubergraph
---
### Ubergraph: A Unified Semantic Knowledge Graph for OBO Ontologies

Ubergraph is an RDF triplestore and public SPARQL query endpoint that integrates a suite of **39 OBO ontologies**, precomputing OWL inferences into a traversable **knowledge graph**. This enables efficient semantic reasoning over multiple ontologies, without requiring extensive local computation.

## Automated Evaluation

- View the automated evaluation: [ubergraph automated evaluation](ubergraph_eval_automated.html)