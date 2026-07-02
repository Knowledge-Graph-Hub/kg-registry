---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://prodolabs.com/
  label: Prodo Laboratories, Inc.
creation_date: '2026-07-01T00:00:00Z'
description: Prodo Laboratories, Inc. is a commercial supplier of human pancreatic
  islets, exocrine tissue, and related reagents for diabetes and pancreas research.
  Islets supplied by Prodo are used in numerous published studies whose omic data
  are deposited in public repositories, and Prodo is one of the islet sources integrated
  by PanKbase.
domains:
- biomedical
- genomics
homepage_url: https://prodolabs.com/
id: prodo
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
name: Prodo Laboratories
products:
- category: DataSource
  description: Product catalog and ordering site for Prodo Laboratories human islet
    and pancreatic tissue products.
  format: http
  id: prodo.site
  name: Prodo Laboratories Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prodo
  product_url: https://prodolabs.com/
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
taxon:
- NCBITaxon:9606
---
Prodo Laboratories

## Description

Prodo Laboratories, Inc. is a commercial provider of human pancreatic islets and related tissue products used widely in diabetes and islet biology research. Islets supplied by Prodo are a source of single-cell datasets integrated by PanKbase.