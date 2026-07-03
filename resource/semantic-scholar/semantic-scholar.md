---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.semanticscholar.org/
  label: Allen Institute for AI (Semantic Scholar)
creation_date: '2026-07-02T00:00:00Z'
description: Semantic Scholar is a free, AI-powered research tool and scholarly literature
  database from the Allen Institute for AI, providing a corpus of paper metadata,
  abstracts, authors, citations, and the Semantic Scholar Academic Graph (S2AG).
domains:
- literature
- information technology
homepage_url: https://www.semanticscholar.org/
id: semantic-scholar
last_modified_date: '2026-07-02T00:00:00Z'
layout: resource_detail
name: Semantic Scholar
products:
- category: GraphicalInterface
  description: Web interface for searching and browsing the Semantic Scholar corpus
    of papers, authors, and citations.
  format: http
  id: semantic-scholar.website
  name: Semantic Scholar Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: semantic-scholar
  product_url: https://www.semanticscholar.org/
- category: ProgrammingInterface
  description: Public API providing programmatic access to the Semantic Scholar Academic
    Graph (S2AG), including paper, author, and citation records.
  format: http
  id: semantic-scholar.api
  is_public: true
  name: Semantic Scholar Academic Graph API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: semantic-scholar
  product_url: https://www.semanticscholar.org/product/api
- category: GraphProduct
  description: The CM4AI Talent Knowledge Graph connecting Bridge2AI and CM4AI researchers,
    projects, publications, datasets, and bio-entities.
  format: ttl
  id: cm4ai_talent_kg.graph
  name: CM4AI Talent Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cm4ai_talent_kg
  - relation_type: prov:hadPrimarySource
    source: pubmed-knowledge-graph
  - relation_type: prov:hadPrimarySource
    source: semantic-scholar
  product_url: https://cm4aikg.vercel.app/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: orcid
  - relation_type: prov:wasInfluencedBy
    source: bridge2ai
---
Semantic Scholar is a free, AI-powered research tool for scientific
literature, developed at the Allen Institute for AI. It provides a large
corpus of scholarly records with paper metadata, abstracts, author
profiles, and citation relationships.

The Semantic Scholar Academic Graph (S2AG) exposes this corpus through a
public API and bulk datasets, supporting author disambiguation, citation
analysis, and downstream knowledge graph construction across the
biomedical and broader research literature.