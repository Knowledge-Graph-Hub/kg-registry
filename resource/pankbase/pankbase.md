---
layout: resource_detail
activity_status: active
id: pankbase
name: PanKBase
description: PanKbase is a comprehensive, centralized resource for the study of the
  human pancreas and diabetes. The PanKbase collective aims to integrate diverse type
  1 diabetes (T1D) datasets with expert-curated knowledge in a centralized, open-source
  data hub. Part of the NIH/NIDDK Human Islet Research Network (HIRN).
domains:
- health
- biological systems
- genomics
- clinical
- precision medicine
contacts:
- category: Organization
  label: PanKBase
  contact_details:
  - contact_type: email
    value: help@pankbase.org
- category: Organization
  label: NIDDK Human Islet Research Network (HIRN)
  contact_details:
  - contact_type: email
    value: hirncc@coh.org
  - contact_type: url
    value: https://hirnetwork.org/
homepage_url: https://pankbase.org/
repository: https://github.com/PanKbase-DB
funding:
- id: niddk
  label: National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK)
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
category: DataSource
products:
- id: pankbase.graph
  name: PanKGraph
  description: Knowledge graph representation of human pancreas and diabetes data
  category: GraphProduct
  secondary_source:
  - pankbase
  original_source:
  - pankbase
  format: neo4j
  node_categories:
  - gene
  - protein
  - pathway
  - diabetes marker
  - pancreatic cell
- id: pankbase.graph.site
  name: PanKGraph Site
  description: Graphical interface for exploring the PanKGraph
  category: GraphicalInterface
  product_url: https://pankgraph.org/
  secondary_source:
  - pankbase
  original_source:
  - pankbase
  format: http
  is_public: true
- id: pankbase.graph.api
  name: PanKGraph API
  description: Programming interface for exploring the PanKGraph
  category: ProgrammingInterface
  product_url: https://pankgraph.org/api
  secondary_source:
  - pankbase
  original_source:
  - pankbase
  format: http
  is_public: true
  is_neo4j: true
- id: pankbase.api
  name: PanKBase Data Library API
  description: Programming interface for accessing contents of the PanKbase Data Portal
  category: ProgrammingInterface
  product_url: https://pankbase-db.github.io/pankbase-client-openapi-spec/
  secondary_source:
  - pankbase
  original_source:
  - pankbase
  format: http
  is_public: true
---

PanKBase
