---
activity_status: active
category: Aggregator
collection:
  - translator
contacts:
  - category: Organization
    contact_details:
      - contact_type: github
        value: "BioPack-team"
      - contact_type: url
        value: "https://github.com/BioPack-team/retriever"
    label: BioPack Team
  - category: Individual
    contact_details:
      - contact_type: email
        value: jcallaghan@scripps.edu
      - contact_type: github
        value: tokebe
    label: Willow Callaghan
creation_date: '2025-12-03T00:00:00Z'
description: 'Retriever is an NCATS Biomedical Data Translator Knowledge Provider (infores:retriever) from the DOGSURF team that answers TRAPI queries directly against two data tiers: a Tier 0 graph engine (Gandalf) and a Tier 1 Elasticsearch index built from the merged Translator KG. It serves as an intermediary for the Shepherd reasoning system, deduplicating subqueries, caching results and centralizing identifier normalization.'
domains:
  - biomedical
homepage_url: https://github.com/BioPack-team/retriever
id: "retriever"
infores_id: "retriever"
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
name: BioPack Retriever
repository: https://github.com/BioPack-team/retriever
synonyms:
  - Retriever
products:
  - category: ProgrammingInterface
    description: Production TRAPI 1.6 Knowledge Provider endpoint (/query, /asyncquery, /meta_knowledge_graph).
    format: http
    id: retriever.api
    is_public: true
    name: Retriever TRAPI API
    original_source:
      - source: retriever
        relation_type: prov:hadPrimarySource
      - source: translator
        relation_type: prov:hadPrimarySource
    product_url: https://retriever.transltr.io/
  - category: ProcessProduct
    description: Retriever source code implementing query deduplication, caching, and TRAPI aggregation workflows.
    format: http
    id: retriever.code
    name: Retriever Source Repository
    original_source:
      - source: retriever
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/BioPack-team/retriever
  - category: DocumentationProduct
    description: Project README with deployment and usage instructions for Retriever.
    format: http
    id: retriever.docs
    name: Retriever Documentation
    original_source:
      - source: retriever
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/BioPack-team/retriever#readme
  - category: ProgrammingInterface
    description: Production Shepherd service (TRAPI 1.5.0, version 1.1.7 when checked on 2026-10-04),
      with endpoints to check the status of asynchronous queries and fetch stored responses
      for all hosted ARAs.
    format: http
    id: shepherd.api
    name: Shepherd TRAPI API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: shepherd
      - relation_type: prov:wasDerivedFrom
        source: retriever
    product_url: https://shepherd.transltr.io/docs
  - category: ProgrammingInterface
    description: TRAPI query endpoint for the ARAGORN ARA implementation within Shepherd (/query
      and /asyncquery), which answers queries with lookup, Omnicorp literature co-occurrence
      support and scoring operations over knowledge from Retriever.
    format: http
    id: shepherd.aragorn.api
    infores_id: shepherd-aragorn
    name: Shepherd ARAGORN TRAPI API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: shepherd
      - relation_type: prov:wasInfluencedBy
        source: aragorn
      - relation_type: prov:wasDerivedFrom
        source: retriever
    product_url: https://shepherd.transltr.io/aragorn/docs
  - category: ProgrammingInterface
    description: TRAPI query endpoint for the ARAX ARA implementation within Shepherd (/query
      and /asyncquery), an in-process port of ARAX's expand, overlay, pathfinding and ranking
      steps over knowledge from Retriever.
    format: http
    id: shepherd.arax.api
    infores_id: shepherd-arax
    name: Shepherd ARAX TRAPI API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: shepherd
      - relation_type: prov:wasInfluencedBy
        source: arax
      - relation_type: prov:wasDerivedFrom
        source: retriever
    product_url: https://shepherd.transltr.io/arax/docs
  - category: ProgrammingInterface
    description: TRAPI query endpoint for the BioThings Explorer (BTE) ARA implementation within
      Shepherd (/query and /asyncquery), over knowledge from Retriever.
    format: http
    id: shepherd.bte.api
    infores_id: shepherd-bte
    name: Shepherd BTE TRAPI API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: shepherd
      - relation_type: prov:wasInfluencedBy
        source: biothings-explorer
      - relation_type: prov:wasDerivedFrom
        source: retriever
    product_url: https://shepherd.transltr.io/bte/docs
  - category: ProgrammingInterface
    description: TRAPI query endpoint for the SIPR ARA within Shepherd (/query and /asyncquery),
      which uses a PageRank algorithm to answer set input queries over knowledge from Retriever.
    format: http
    id: shepherd.sipr.api
    infores_id: shepherd-sipr
    name: Shepherd SIPR TRAPI API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: shepherd
      - relation_type: prov:wasDerivedFrom
        source: retriever
    product_url: https://shepherd.transltr.io/sipr/docs
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache License 2.0
---

# BioPack Retriever

Retriever is a Translator infrastructure component providing efficient TRAPI access to multiple knowledge graph backends with query deduplication, caching, and centralized normalization.
