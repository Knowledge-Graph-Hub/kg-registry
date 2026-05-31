---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: cellxgene@chanzuckerberg.com
  - contact_type: url
    value: https://cellxgene.cziscience.com/
  label: Chan Zuckerberg Initiative
creation_date: '2026-05-28T00:00:00Z'
description: CZ CELLxGENE is a platform for finding, downloading, exploring, and analyzing
  single-cell datasets through a public data portal, integrated analysis interfaces,
  and the CELLxGENE Census programmatic access layer.
domains:
- biomedical
- genomics
- health
homepage_url: https://cellxgene.cziscience.com/
id: cellxgene
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
name: CZ CELLxGENE
products:
- category: GraphicalInterface
  description: Main CZ CELLxGENE Discover portal for browsing public single-cell collections,
    datasets, gene expression views, and analysis tools.
  format: http
  id: cellxgene.portal
  name: CZ CELLxGENE Discover
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  product_url: https://cellxgene.cziscience.com/
- category: GraphicalInterface
  description: Search and download interface for public curated collections and datasets
    available through CZ CELLxGENE Discover.
  format: http
  id: cellxgene.datasets
  name: CZ CELLxGENE Datasets Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  product_url: https://cellxgene.cziscience.com/datasets
- category: ProgrammingInterface
  description: Documentation and entry point for the CELLxGENE Census API and data
    object used to query standardized single-cell expression data in R and Python.
  format: http
  id: cellxgene.census
  is_public: true
  name: CZ CELLxGENE Census
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  product_url: https://chanzuckerberg.github.io/cellxgene-census/
- category: DocumentationProduct
  description: Official documentation for CZ CELLxGENE Discover, Explorer, Gene Expression,
    and Annotate workflows.
  format: http
  id: cellxgene.docs
  name: CZ CELLxGENE Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  product_url: https://cellxgene.cziscience.com/docs
- category: ProgrammingInterface
  connection_url: cl-kg-neo4j-db.cellgeni.sanger.ac.uk:443
  description: Publicly available Neo4j instance for CL-KG.
  id: cl-kg.api.neo4j
  is_neo4j: true
  is_public: true
  name: CL-KG Neo4j graph instance
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cl-kg
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  product_url: https://cellular-semantics.sanger.ac.uk/browser/
---
# CZ CELLxGENE

CZ CELLxGENE is a single-cell data platform from the Chan Zuckerberg Initiative
that supports public data discovery, interactive exploration, and programmatic
access to a large harmonized corpus of single-cell expression datasets.