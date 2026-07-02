---
layout: resource_detail
activity_status: active
id: gene-expression-omnibus
name: Gene Expression Omnibus (GEO)
description: The Gene Expression Omnibus (GEO) is a public functional genomics data repository maintained by the NCBI at the U.S. National Library of Medicine. It archives and freely distributes high-throughput gene expression and other functional genomics datasets, including the single-cell and single-nucleus studies of human pancreatic islets that PanKbase identified and reprocessed.
domains:
- biomedical
- genomics
contacts:
- category: Organization
  label: NCBI Gene Expression Omnibus
  contact_details:
  - contact_type: email
    value: geo@ncbi.nlm.nih.gov
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/geo/
homepage_url: https://www.ncbi.nlm.nih.gov/geo/
category: Aggregator
products:
- id: gene-expression-omnibus.portal
  name: GEO Portal
  description: Web portal for searching, browsing, and downloading functional genomics datasets archived in the Gene Expression Omnibus.
  category: DataSource
  product_url: https://www.ncbi.nlm.nih.gov/geo/
  format: http
  original_source:
  - source: gene-expression-omnibus
    relation_type: prov:hadPrimarySource
creation_date: '2026-07-01T00:00:00Z'
last_modified_date: '2026-07-01T00:00:00Z'
---

Gene Expression Omnibus (GEO)

## Description

The Gene Expression Omnibus (GEO) is a public functional genomics data repository operated by the NCBI. PanKbase used systematic searches of GEO to identify islet single-cell and single-nucleus studies (including those using IIDP- and Prodo-supplied islets), which were then reprocessed through a harmonized pipeline. GEO therefore acts as an aggregating upstream influence on PanKbase and PanKgraph.
