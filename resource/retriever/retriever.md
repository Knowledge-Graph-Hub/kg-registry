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
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache License 2.0
---

# BioPack Retriever

Retriever is a Translator infrastructure component providing efficient TRAPI access to multiple knowledge graph backends with query deduplication, caching, and centralized normalization.
