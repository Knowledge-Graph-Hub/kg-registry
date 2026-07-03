---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: geo@ncbi.nlm.nih.gov
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/geo/
  label: NCBI Gene Expression Omnibus
creation_date: '2026-07-01T00:00:00Z'
description: The Gene Expression Omnibus (GEO) is a public functional genomics data
  repository maintained by the NCBI at the U.S. National Library of Medicine. It archives
  and freely distributes high-throughput gene expression and other functional genomics
  datasets, including the single-cell and single-nucleus studies of human pancreatic
  islets that PanKbase identified and reprocessed.
domains:
- biomedical
- genomics
homepage_url: https://www.ncbi.nlm.nih.gov/geo/
id: gene-expression-omnibus
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
name: Gene Expression Omnibus (GEO)
products:
- category: DataSource
  description: Web portal for searching, browsing, and downloading functional genomics
    datasets archived in the Gene Expression Omnibus.
  format: http
  id: gene-expression-omnibus.portal
  name: GEO Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  product_url: https://www.ncbi.nlm.nih.gov/geo/
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
- category: GraphProduct
  description: RDF (Turtle) knowledge graph of the NIAID Data Ecosystem, harmonizing
    dataset and computational-tool metadata harvested from NIAID-funded and globally-relevant
    infectious and immune-mediated disease repositories. Served through the Proto-OKN
    FRINK federated SPARQL platform.
  format: ttl
  id: nde.graph
  name: NIAID Data Ecosystem KG (graph)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nde
  - relation_type: prov:hadPrimarySource
    source: immport
  - relation_type: prov:hadPrimarySource
    source: vdjserver
  product_url: https://frink.apps.renci.org/nde
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: gene-expression-omnibus
  - relation_type: prov:wasInfluencedBy
    source: sra
  - relation_type: prov:wasInfluencedBy
    source: omicsdi
  - relation_type: prov:wasInfluencedBy
    source: hubmap
  - relation_type: prov:wasInfluencedBy
    source: massive
  - relation_type: prov:wasInfluencedBy
    source: pdb
  - relation_type: prov:wasInfluencedBy
    source: lincs
---
Gene Expression Omnibus (GEO)

## Description

The Gene Expression Omnibus (GEO) is a public functional genomics data repository operated by the NCBI. PanKbase used systematic searches of GEO to identify islet single-cell and single-nucleus studies (including those using IIDP- and Prodo-supplied islets), which were then reprocessed through a harmonized pipeline. GEO therefore acts as an aggregating upstream influence on PanKbase and PanKgraph.