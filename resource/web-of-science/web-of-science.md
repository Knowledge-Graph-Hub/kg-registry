---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://clarivate.com/
  label: Clarivate
creation_date: '2026-06-02T00:00:00Z'
description: Web of Science Core Collection is a multidisciplinary citation database
  from Clarivate that indexes peer-reviewed journals, conference proceedings, books,
  and cited references across sciences, social sciences, arts, and humanities.
domains:
- literature
- information technology
- general
homepage_url: https://clarivate.com/academia-government/scientific-and-academic-research/research-discovery-and-referencing/web-of-science/
id: web-of-science
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: Web of Science
products:
- category: GraphicalInterface
  description: Web of Science research discovery and citation-index platform.
  format: http
  id: web-of-science.platform
  name: Web of Science Platform
  original_source:
  - relation_type: prov:hadPrimarySource
    source: web-of-science
  product_url: https://www.webofscience.com/
  warnings:
  - Web of Science access is subscription-dependent.
- category: DocumentationProduct
  description: Clarivate documentation for Web of Science Core Collection content,
    indexes, records, and search features.
  format: http
  id: web-of-science.core_collection_docs
  name: Web of Science Core Collection Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: web-of-science
  product_url: https://webofscience.help.clarivate.com/Content/wos-core-collection/wos-core-collection.htm
  warnings: []
- category: GraphProduct
  description: Neo4j framework-materials knowledge graph constructed from Web of Science
    abstracts and publication metadata with LLM-assisted information extraction. The
    paper reports 2.53 million nodes and 4.01 million relationships covering materials,
    properties, structures, applications, and related literature.
  edge_count: 4010000
  id: kg-fm.graph
  name: KG-FM Neo4j Knowledge Graph
  node_count: 2530000
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-fm
  - relation_type: prov:hadPrimarySource
    source: web-of-science
  product_url: https://github.com/MontageBai/KGFM
  warnings:
  - No standalone Neo4j database dump, public graph endpoint, or versioned graph release
    was identified in the GitHub repository when curated on 2026-06-02; the repository
    provides source text, JSON extraction files, and Python scripts for constructing
    and using the graph.
- category: Product
  compression: zip
  description: Zipped abstract-text corpora for COF, HOF, and MOF literature used
    as input to KG-FM extraction and graph construction.
  id: kg-fm.abstract_text
  name: KG-FM Abstract Text Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-fm
  - relation_type: prov:hadPrimarySource
    source: web-of-science
  product_url: https://github.com/MontageBai/KGFM/tree/main/Abstract%20Text
- category: Product
  compression: zip
  description: Zipped JSON extraction files for COF, HOF, and MOF literature, produced
    from framework-material abstracts and used to import KG-FM nodes and relationships.
  id: kg-fm.json_extractions
  name: KG-FM JSON Extraction Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-fm
  - relation_type: prov:hadPrimarySource
    source: web-of-science
  product_url: https://github.com/MontageBai/KGFM/tree/main/Json%20File
synonyms:
- WoS
- Web of Science Core Collection
- WOSCC
warnings:
- Web of Science is a proprietary Clarivate resource and institutional subscription
  depth can affect available coverage.
---
# Web of Science

Web of Science is a Clarivate research discovery and citation-index platform. KG-FM used Web of Science records for framework-material literature retrieval, abstracts, DOI metadata, author information, publication dates, and journal information.