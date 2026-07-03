---
layout: resource_detail
activity_status: active
id: pubmed-knowledge-graph
name: PubMed Knowledge Graph
description: >-
  The PubMed Knowledge Graph (PKG) is a biomedical knowledge graph built
  from PubMed that connects papers, authors, bio-entities, affiliations,
  citations, and research projects, with author name disambiguation and
  entity linking. PKG 2.0 additionally connects patents and clinical
  trials.
domains:
  - literature
  - biomedical
contacts:
  - category: Organization
    label: PubMed Knowledge Graph (PKG)
    contact_details:
      - contact_type: url
        value: https://pubmedkg.github.io/
homepage_url: https://pubmedkg.github.io/
category: KnowledgeGraph
last_modified_date: '2026-07-02T00:00:00Z'
publications:
  - authors:
      - Jian XU
      - Sunkyu KIM
      - Min SONG
      - et al.
    doi: 10.1038/s41597-020-0543-2
    id: doi:10.1038/s41597-020-0543-2
    journal: Scientific Data
    preferred: true
    title: Building a PubMed knowledge graph
    year: '2020'
products:
  - category: GraphicalInterface
    description: Project homepage for the PubMed Knowledge Graph, providing
      dataset documentation and download access.
    format: http
    id: pubmed-knowledge-graph.website
    name: PubMed Knowledge Graph Homepage
    original_source:
      - source: pubmed-knowledge-graph
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
    product_url: https://pubmedkg.github.io/
creation_date: '2026-07-02T00:00:00Z'
---

The PubMed Knowledge Graph (PKG) is a large-scale biomedical knowledge
graph derived from PubMed. It links papers to disambiguated authors,
bio-entities, affiliations, citation relationships, and research
projects, enabling bibliometric and scientometric analyses across the
biomedical literature.

PKG 2.0 extends the graph by connecting papers with patents and clinical
trials, integrating previously dispersed biomedical resources through
biomedical entity links, author networks, citation relationships, and
research project connections. The dataset is freely available for
download from the project homepage.
