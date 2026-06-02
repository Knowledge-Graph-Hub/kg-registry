---
activity_status: active
category: DataSource
creation_date: '2026-06-02T00:00:00Z'
description: Stub Resource page for harmonizome. This page was automatically generated
  because it was referenced by other resources.
domains:
- stub
id: harmonizome
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: Harmonizome
products:
- category: GraphicalInterface
  description: Interactive web interface for exploring the Harmonizome knowledge graph
    with gene-centric network visualization
  format: http
  id: harmonizome-kg.portal
  name: Harmonizome-KG Explorer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome-kg
  product_url: https://harmonizome-kg.maayanlab.cloud/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: harmonizome
- category: ProgrammingInterface
  connection_url: https://harmonizome-kg.maayanlab.cloud/api/knowledge_graph
  description: API endpoint for programmatic access to Harmonizome-KG neighborhoods,
    with filter parameters documented in the Harmonizome knowledge graph API guide
  format: json
  id: harmonizome-kg.api
  name: Harmonizome-KG API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome-kg
  product_url: https://maayanlab.cloud/Harmonizome/documentation#kg-api
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: harmonizome
- category: GraphProduct
  description: Neo4j knowledge graph serialization of Harmonizome processed datasets,
    including genes, attributes, resources, datasets, and gene-attribute associations
  dump_format: neo4j
  format: neo4j
  id: harmonizome-kg.graph
  latest_version: '3.0'
  name: Harmonizome-KG Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome-kg
  product_url: https://harmonizome-kg.maayanlab.cloud/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: harmonizome
warnings:
- This is an automatically generated stub page. Please replace with accurate information
  about this resource.
---
# Harmonizome

This is an automatically generated stub page for harmonizome. Please update with proper information.