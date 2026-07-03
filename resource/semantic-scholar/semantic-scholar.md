---
layout: resource_detail
activity_status: active
id: semantic-scholar
name: Semantic Scholar
description: >-
  Semantic Scholar is a free, AI-powered research tool and scholarly
  literature database from the Allen Institute for AI, providing a
  corpus of paper metadata, abstracts, authors, citations, and the
  Semantic Scholar Academic Graph (S2AG).
domains:
  - literature
  - information technology
contacts:
  - category: Organization
    label: Allen Institute for AI (Semantic Scholar)
    contact_details:
      - contact_type: url
        value: https://www.semanticscholar.org/
homepage_url: https://www.semanticscholar.org/
category: DataSource
last_modified_date: '2026-07-02T00:00:00Z'
products:
  - category: GraphicalInterface
    description: Web interface for searching and browsing the Semantic Scholar
      corpus of papers, authors, and citations.
    format: http
    id: semantic-scholar.website
    name: Semantic Scholar Search
    original_source:
      - source: semantic-scholar
        relation_type: prov:hadPrimarySource
    product_url: https://www.semanticscholar.org/
  - category: ProgrammingInterface
    description: Public API providing programmatic access to the Semantic Scholar
      Academic Graph (S2AG), including paper, author, and citation records.
    format: http
    id: semantic-scholar.api
    is_public: true
    name: Semantic Scholar Academic Graph API
    original_source:
      - source: semantic-scholar
        relation_type: prov:hadPrimarySource
    product_url: https://www.semanticscholar.org/product/api
creation_date: '2026-07-02T00:00:00Z'
---

Semantic Scholar is a free, AI-powered research tool for scientific
literature, developed at the Allen Institute for AI. It provides a large
corpus of scholarly records with paper metadata, abstracts, author
profiles, and citation relationships.

The Semantic Scholar Academic Graph (S2AG) exposes this corpus through a
public API and bulk datasets, supporting author disambiguation, citation
analysis, and downstream knowledge graph construction across the
biomedical and broader research literature.
