---
activity_status: active
category: KnowledgeGraph
creation_date: '2026-04-06T00:00:00Z'
description: HALD (Human Aging and Longevity Database) is a human aging and longevity knowledge graph generated from text-mined PubMed literature and organized around entities, relations, and biomarkers relevant to aging and longevity research.
domains:
  - biomedical
  - literature
  - precision medicine
homepage_url: https://bis.zju.edu.cn/hald
id: hald
last_modified_date: '2026-05-28T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Human Aging and Longevity Database
products:
  - category: Product
    description: Version 6 JSON file containing literature metadata for the HALD corpus.
    format: json
    id: hald.literature-info.json
    latest_version: v6
    name: HALD Literature Info
    original_source:
      - source: hald
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
    product_file_size: 854292307
    product_url: https://ndownloader.figshare.com/files/43612512
  - category: Product
    description: Version 6 JSON file containing entity-level metadata extracted for HALD.
    format: json
    id: hald.entity-info.json
    latest_version: v6
    name: HALD Entity Info
    original_source:
      - source: hald
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
    product_file_size: 296732271
    product_url: https://ndownloader.figshare.com/files/43612509
  - category: GraphProduct
    description: Version 6 JSON file containing relation triples extracted for HALD.
    format: json
    id: hald.relation-info.json
    latest_version: v6
    name: HALD Relation Info
    original_source:
      - source: hald
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
    product_file_size: 98203237
    product_url: https://ndownloader.figshare.com/files/43612506
  - category: Product
    description: Version 6 JSON file containing aging biomarker records from HALD.
    format: json
    id: hald.aging-biomarkers.json
    latest_version: v6
    name: HALD Aging Biomarkers
    original_source:
      - source: hald
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
    product_file_size: 1199321
    product_url: https://ndownloader.figshare.com/files/43612503
  - category: Product
    description: Version 6 JSON file containing longevity biomarker records from HALD.
    format: json
    id: hald.longevity-biomarkers.json
    latest_version: v6
    name: HALD Longevity Biomarkers
    original_source:
      - source: hald
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
    product_file_size: 339386
    product_url: https://ndownloader.figshare.com/files/43612497
  - category: Product
    description: Version 6 CSV file containing entity rows for loading HALD into Neo4j.
    format: csv
    id: hald.entities.csv
    latest_version: v6
    name: HALD Neo4j Entities
    original_source:
      - source: hald
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
    product_file_size: 239792
    product_url: https://ndownloader.figshare.com/files/43612494
  - category: Product
    description: Version 6 CSV file containing relationship rows for loading HALD into Neo4j.
    format: csv
    id: hald.roles.csv
    latest_version: v6
    name: HALD Neo4j Roles
    original_source:
      - source: hald
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
    product_file_size: 5077672
    product_url: https://ndownloader.figshare.com/files/43612500
  - category: GraphicalInterface
    description: Interactive web interface for searching, browsing, and exploring HALD.
    format: http
    id: hald.browser
    name: HALD Web Interface
    original_source:
      - source: hald
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
    product_url: https://bis.zju.edu.cn/hald
publications:
  - doi: doi:10.1038/s41597-023-02781-0
    id: https://doi.org/10.1038/s41597-023-02781-0
    journal: Scientific Data
    preferred: true
    title: HALD, a human aging and longevity knowledge graph for precision gerontology and geroscience analyses
    year: '2023'
repository: https://github.com/zexuwu/hald
taxon:
  - NCBITaxon:9606
---

# HALD

HALD is a literature-derived knowledge graph focused on human aging and longevity. It supports exploration of entities, relationships, and biomarkers identified from PubMed abstracts, and it exposes version 6 downloadable JSON and CSV files alongside an interactive browser for searching and network inspection.
