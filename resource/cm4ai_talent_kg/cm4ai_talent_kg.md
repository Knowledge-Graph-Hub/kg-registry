---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://cm4ai.org/
    label: Bridge2AI CM4AI
description: A knowledge graph containing connections between researchers, projects, and publications centering on members of the Bridge2AI Consortium and the Cell Maps for AI (CM4AI) project.
domains:
  - literature
homepage_url: https://cm4aikg.vercel.app/
id: cm4ai_talent_kg
layout: resource_detail
name: CM4AI Talent KG
products:
  - category: GraphicalInterface
    description: Web-based interface for browsing and exploring the CM4AI Talent Knowledge Graph
    format: http
    id: cm4ai_talent_kg.web_interface
    name: CM4AI Talent KG Web Interface
    original_source:
      - source: cm4ai_talent_kg
        relation_type: prov:hadPrimarySource
    product_url: https://cm4aikg.vercel.app/
  - category: GraphProduct
    description: The CM4AI Talent Knowledge Graph connecting Bridge2AI and CM4AI
      researchers, projects, publications, datasets, and bio-entities.
    format: ttl
    id: cm4ai_talent_kg.graph
    name: CM4AI Talent Knowledge Graph
    original_source:
      - source: cm4ai_talent_kg
        relation_type: prov:hadPrimarySource
      - source: pubmed-knowledge-graph
        relation_type: prov:hadPrimarySource
      - source: semantic-scholar
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: orcid
        relation_type: prov:wasInfluencedBy
      - source: bridge2ai
        relation_type: prov:wasInfluencedBy
    product_url: https://cm4aikg.vercel.app/
creation_date: '2025-07-16T00:00:00Z'
last_modified_date: '2026-07-02T00:00:00Z'
---

A knowledge graph containing connections between researchers, projects, and publications centering on members of the Bridge2AI Consortium and the Cell Maps for AI (CM4AI) project.

## Automated Evaluation

- View the automated evaluation: [cm4ai_talent_kg automated evaluation](cm4ai_talent_kg_eval_automated.html)
