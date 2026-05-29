---
activity_status: active
category: KnowledgeGraph
creation_date: '2026-04-06T00:00:00Z'
description: PharMeBINet is a heterogeneous pharmacological medical biochemical network that integrates biomedical data sources into a graph for studying drugs, adverse drug reactions, genes, proteins, variants, diseases, and their relationships.
domains:
  - pharmacology
  - drug discovery
  - biomedical
  - health
homepage_url: https://pharmebi.net/
id: pharmebinet
last_modified_date: '2026-05-29T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: PharMeBINet
products:
  - category: GraphicalInterface
    description: Web application for browsing and querying PharMeBINet.
    format: http
    id: pharmebinet.browser
    name: PharMeBINet Web Application
    original_source:
      - source: pharmebinet
        relation_type: prov:hadPrimarySource
    product_url: https://pharmebi.net/
  - category: GraphProduct
    compression: gzip
    description: PharMeBINet V2 JSON release published on February 6, 2024.
    format: json
    id: pharmebinet.json
    latest_version: v2
    name: PharMeBINet JSON Release
    original_source:
      - source: pharmebinet
        relation_type: prov:hadPrimarySource
    product_file_size: 1942958027
    product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_24_02_06.json.gz/content
  - category: GraphProduct
    compression: zip
    description: PharMeBINet V2 TSV release published on February 6, 2024.
    format: tsv
    id: pharmebinet.tsv
    latest_version: v2
    name: PharMeBINet TSV Release
    original_source:
      - source: pharmebinet
        relation_type: prov:hadPrimarySource
    product_file_size: 1922614551
    product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_tsv_24_02_06.zip/content
  - category: GraphProduct
    compression: zip
    description: PharMeBINet V2 GraphML release published on February 6, 2024.
    format: mixed
    id: pharmebinet.graphml
    latest_version: v2
    name: PharMeBINet GraphML Release
    original_source:
      - source: pharmebinet
        relation_type: prov:hadPrimarySource
    product_file_size: 2027519087
    product_url: https://zenodo.org/api/records/17814889/files/PharMeBiNet_graphml_24_02_06.zip/content
  - category: GraphProduct
    compression: zip
    description: PharMeBINet V2 Neo4j database release published on February 6, 2024.
    format: neo4j
    id: pharmebinet.neo4j
    latest_version: v2
    name: PharMeBINet Neo4j Database
    original_source:
      - source: pharmebinet
        relation_type: prov:hadPrimarySource
    product_file_size: 3847978577
    product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_24_02_06.zip/content
  - category: GraphProduct
    compression: zip
    description: PharMeBINet V2 Neo4j dump release published on February 6, 2024.
    dump_format: neo4j
    format: neo4j
    id: pharmebinet.neo4j.dump
    latest_version: v2
    name: PharMeBINet Neo4j Dump
    original_source:
      - source: pharmebinet
        relation_type: prov:hadPrimarySource
    product_file_size: 3598325722
    product_url: https://zenodo.org/api/records/17814889/files/pharmebinet_dump_24_02_06.zip/content
  - category: DocumentationProduct
    description: Data sources documentation page describing the upstream resources integrated into PharMeBINet.
    format: http
    id: pharmebinet.data-sources
    name: PharMeBINet Data Sources
    original_source:
      - source: pharmebinet
        relation_type: prov:hadPrimarySource
    product_url: https://pharmebi.net/#/datasources
publications:
  - doi: doi:10.1038/s41597-022-01510-3
    id: https://doi.org/10.1038/s41597-022-01510-3
    journal: Scientific Data
    preferred: true
    title: The heterogeneous pharmacological medical biochemical network PharMeBINet
    year: '2022'
repository: https://github.com/ckoenigs/PharMeBINet
---

# PharMeBINet

PharMeBINet is a large heterogeneous biomedical knowledge graph centered on pharmacology and adverse drug reaction analysis. The project integrates many biomedical resources into a graph database and provides both a public web interface and versioned releases in JSON, TSV, GraphML, and Neo4j formats for downstream analysis.
