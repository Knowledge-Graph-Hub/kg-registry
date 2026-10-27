---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: kfecho@copperlineprofessionalsolutions.com
  label: Karamarie Fecho
creation_date: '2025-03-09T00:00:00Z'
description: ROBOKOP (Reasoning Over Biomedical Objects linked in Knowledge Oriented
  Pathways) is an open-source biomedical knowledge graph system that enables complex
  queries over a large-scale integrated knowledge graph.
domains:
- biomedical
homepage_url: http://robokop.renci.org
id: robokop
infores_id: robokop
last_modified_date: '2026-09-16T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: ROBOKOP
products:
- category: Product
  description: A biomedical knowledge graph containing ~10 million nodes and ~250
    million edges from ~30 biological data sources and bio-ontologies.
  format: neo4j
  id: robokop.graph
  name: ROBOKOP Knowledge Graph (KG)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: robokop
  product_file_size: 280
  product_url: http://robokopkg.renci.org
- category: GraphProduct
  description: Robokop KG (Automat)
  format: kgx-jsonl
  id: automat.robokopkg
  name: robokopkg
  original_source:
  - relation_type: prov:hadPrimarySource
    source: automat
  - relation_type: prov:hadPrimarySource
    source: robokop
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: drugmechdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: gtex
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/RobokopKG/4901b2bc764444ea/
- category: GraphProduct
  description: 'Robokop Plus: the ROBOKOP KG extended with CORD-19 and text-mined
    assertions (2023 data, Biolink 3.1.2; legacy).'
  format: kgx-jsonl
  id: automat.robokopplus
  name: robokopplus
  original_source:
  - relation_type: prov:hadPrimarySource
    source: automat
  - relation_type: prov:hadPrimarySource
    source: robokop
  - relation_type: prov:hadPrimarySource
    source: cord-19
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  product_url: https://stars.renci.org/var/plater/bl-3.1.2/RobokopPlus/ad8cb4d0a7ccc923/kgx_files/
- category: ProgrammingInterface
  description: RENCI-hosted TRAPI endpoint (/query, /asyncquery) for the ARAGORN ARA,
    with Swagger documentation. Queries are answered by Strider over the knowledge
    providers it has registered (here including the Automat ROBOKOP KG, CAM-KP, ICEES,
    Ubergraph, GeLiNEA, Genetics KP, MolePro, OpenPredict and Text Mining KP co-occurrence),
    plus direct ROBOKOP KG lookups for inferred queries, SRI Node Normalizer identifier
    normalization and OmniCorp literature co-occurrence overlays for scoring.
  format: http
  id: aragorn.api
  name: ARAGORN API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aragorn
  - relation_type: prov:hadPrimarySource
    source: robokop
  - relation_type: prov:hadPrimarySource
    source: automat
  - relation_type: prov:hadPrimarySource
    source: omnicorp
  - relation_type: prov:hadPrimarySource
    source: node-normalizer
  - relation_type: prov:hadPrimarySource
    source: cam-kp
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: genetics-kp
  - relation_type: prov:hadPrimarySource
    source: molepro
  - relation_type: prov:hadPrimarySource
    source: openpredict
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  product_url: https://aragorn.renci.org/docs
- category: ProgrammingInterface
  description: Production (NCATS ITRB) deployment of the ARAGORN TRAPI endpoint, with
    Swagger documentation. Like the RENCI deployment it queries knowledge providers
    through Strider, looks up the ROBOKOP KG via Automat, normalizes identifiers with
    the SRI Node Normalizer and scores answers with OmniCorp literature co-occurrence.
  format: http
  id: aragorn.api.itrb
  is_public: true
  name: ARAGORN Production API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aragorn
  - relation_type: prov:hadPrimarySource
    source: robokop
  - relation_type: prov:hadPrimarySource
    source: automat
  - relation_type: prov:hadPrimarySource
    source: omnicorp
  - relation_type: prov:hadPrimarySource
    source: node-normalizer
  - relation_type: prov:hadPrimarySource
    source: cam-kp
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  - relation_type: prov:hadPrimarySource
    source: genetics-kp
  - relation_type: prov:hadPrimarySource
    source: molepro
  - relation_type: prov:hadPrimarySource
    source: cohd
  - relation_type: prov:hadPrimarySource
    source: connections-hypothesis-kp
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: multiomics-kp
  - relation_type: prov:hadPrimarySource
    source: drug-approvals-kp
  - relation_type: prov:hadPrimarySource
    source: microbiomekg
  - relation_type: prov:hadPrimarySource
    source: service-kp
  product_url: https://aragorn.transltr.io/aragorn/docs
repository: https://github.com/NCATS-Gamma/robokop
rrid: SCR_023437
---
### ROBOKOP: A Knowledge Graph System for Biomedical Question Answering

ROBOKOP (Reasoning Over Biomedical Objects linked in Knowledge Oriented Pathways) is an **open-source**, modular **biomedical knowledge graph system** that includes:
- The **ROBOKOP Knowledge Graph (KG)**
- A **user interface** for building and exploring queries
- Supporting tools and APIs for programmatic access

## Evaluation

- View the evaluation: [robokop evaluation](robokop_eval.html)