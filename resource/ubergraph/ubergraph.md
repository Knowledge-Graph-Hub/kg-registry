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
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  product_file_size: 6866918
  product_url: https://ubergraph.apps.renci.org/sparql
- category: Product
  description: Blazegraph journal of Ubergraph
  id: ubergraph.blazegraph.jnl
  name: Ubergraph blazegraph journal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  product_file_size: 9157530809
  product_url: https://ubergraph.apps.renci.org/downloads/current/ubergraph.jnl.gz
- category: Product
  description: Ubergraph n-quads
  format: nquads
  id: ubergraph.nquads
  name: Ubergraph n-quads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  product_file_size: 3718641146
  product_url: https://ubergraph.apps.renci.org/downloads/current/ubergraph.nq.gz
- category: GraphProduct
  description: UberGraph Automat
  format: kgx-jsonl
  id: automat.ubergraph
  name: ubergraph_automat
  original_source:
  - relation_type: prov:hadPrimarySource
    source: automat
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/UbergraphRedundant_Automat/e6b3204fd3a04413/
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
  - relation_type: prov:hadPrimarySource
    source: translator
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/ubergraph/latest/
  versions:
  - '2026_03_27'
  - ubergraph_2026-03-08_0fef3756_2025sep1_4.3.6
- category: ProgrammingInterface
  description: SPARQL endpoint for Ubergraph
  id: ubergraph.sparql
  name: Ubergraph SPARQL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  product_url: https://frink.apps.renci.org/ubergraph/sparql
- category: ProgrammingInterface
  description: Triple Pattern Fragments endpoint for Ubergraph
  id: ubergraph.tpf
  name: Ubergraph TPF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ubergraph
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
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cohd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: drug-approvals-kp
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: geneticskp
  - relation_type: prov:hadPrimarySource
    source: go-cam
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathbank
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: translator
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
  versions:
  - '2026_03_27'
  - 423af7989cac
repository: https://github.com/INCATools/ubergraph
---
### Ubergraph: A Unified Semantic Knowledge Graph for OBO Ontologies

Ubergraph is an RDF triplestore and public SPARQL query endpoint that integrates a suite of **39 OBO ontologies**, precomputing OWL inferences into a traversable **knowledge graph**. This enables efficient semantic reasoning over multiple ontologies, without requiring extensive local computation.

## Automated Evaluation

- View the automated evaluation: [ubergraph automated evaluation](ubergraph_eval_automated.html)