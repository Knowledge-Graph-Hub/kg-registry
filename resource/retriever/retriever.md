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
creation_date: '2025-12-03T00:00:00Z'
description: Retriever is an NCATS Translator component that serves as a TRAPI (Translator Reasoner API) access layer and intermediary between Knowledge Providers and the Shepherd ARA. Retriever deduplicates subquery operations, provides a cache layer, and centralizes normalization calls for improved efficiency in querying multiple knowledge graph backends. It aggregates TRAPI query responses from DogPark Knowledge Providers, using external database backends to serve integrated biomedical knowledge.
domains:
  - translational
  - biomedical
homepage_url: https://github.com/BioPack-team/retriever
id: "retriever"
infores_id: "retriever"
last_modified_date: '2026-02-20T00:00:00Z'
layout: resource_detail
name: BioPack Retriever
repository: https://github.com/BioPack-team/retriever
synonyms:
  - Retriever
products:
  - category: ProcessProduct
    description: Retriever source code implementing query deduplication, caching, and
      TRAPI aggregation workflows.
    format: http
    id: retriever.code
    name: Retriever Source Repository
    original_source:
      - retriever
    product_url: https://github.com/BioPack-team/retriever
  - category: DocumentationProduct
    description: Project README with deployment and usage instructions for Retriever.
    format: http
    id: retriever.docs
    name: Retriever Documentation
    original_source:
      - retriever
    product_url: https://github.com/BioPack-team/retriever#readme
---

# BioPack Retriever

Retriever is a Translator infrastructure component providing efficient TRAPI access to multiple knowledge graph backends with query deduplication, caching, and centralized normalization.
