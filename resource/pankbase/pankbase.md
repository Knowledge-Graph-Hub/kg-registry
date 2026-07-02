---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: help@pankbase.org
  label: PanKBase
- category: Organization
  contact_details:
  - contact_type: email
    value: hirncc@coh.org
  - contact_type: url
    value: https://hirnetwork.org/
  label: NIDDK Human Islet Research Network (HIRN)
creation_date: '2025-03-17T00:00:00Z'
description: PanKbase is a comprehensive, centralized resource for the study of the
  human pancreas and diabetes. The PanKbase collective aims to integrate diverse type
  1 diabetes (T1D) datasets with expert-curated knowledge in a centralized, open-source
  data hub. Part of the NIH/NIDDK Human Islet Research Network (HIRN).
domains:
- biomedical
- biological systems
- genomics
- clinical
- precision medicine
homepage_url: https://pankbase.org/
id: pankbase
last_modified_date: '2026-06-27T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: PanKBase
products:
- category: GraphProduct
  description: Knowledge graph representation of human pancreas and diabetes data
  id: pankbase.graph
  name: PanKGraph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pankbase
- category: GraphicalInterface
  description: Graphical interface for exploring the PanKGraph
  format: http
  id: pankbase.graph.site
  is_public: true
  name: PanKGraph Site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pankbase
  product_url: https://pankgraph.org/
- category: ProgrammingInterface
  description: Programming interface for exploring the PanKGraph
  format: http
  id: pankbase.graph.api
  is_neo4j: true
  is_public: true
  name: PanKGraph API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pankbase
  product_url: https://pankgraph.org/api
- category: ProgrammingInterface
  description: Programming interface for accessing contents of the PanKbase Data Portal
  format: http
  id: pankbase.api
  is_public: true
  name: PanKBase Data Library API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pankbase
  product_url: https://pankbase.github.io/pankbase-client-openapi-spec/
- category: GraphProduct
  description: Pancreas-focused knowledge graph integrating genes, SNPs, pancreatic
    expression QTLs, and donor-derived islet datasets harmonized within PanKbase.
  format: http
  id: pankgraph.graph
  name: PanKgraph Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pankgraph
  - relation_type: prov:wasDerivedFrom
    source: pankbase
  - relation_type: prov:hadPrimarySource
    source: hpap
  - relation_type: prov:hadPrimarySource
    source: iidp
  - relation_type: prov:hadPrimarySource
    source: prodo
  product_url: https://pankgraph.org/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: gene-expression-omnibus
repository: https://github.com/PanKbase-DB
taxon:
- NCBITaxon:9606
---
PanKBase