---
activity_status: active
category: DataSource
creation_date: '2025-07-17T00:00:00Z'
description: Stub Resource page for pubmed. This page was automatically generated
  because it was referenced by other resources.
domains:
- stub
id: pubmed
last_modified_date: '2025-07-17T00:00:00Z'
layout: resource_detail
name: Pubmed
products:
- category: MappingProduct
  compression: gzip
  description: Gene to PubMed mapping data providing literature references associated
    with genes
  format: tsv
  id: ncbigene.gene2pubmed
  name: Gene to PubMed Mapping
  original_source:
  - pubmed
  - ncbigene
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/gene2pubmed.gz
- category: ProcessProduct
  description: INDRA CoGEx is a graph database integrating causal relations, ontological
    relations, properties, and data, assembled at scale automatically from the scientific
    literature and structured sources. This is the code to build the graph.
  id: indra.cogex.code
  name: INDRA CoGEx Build Code
  original_source:
  - chembl
  - sider
  - reactome
  - wikipathways
  - hp
  - nihreporter
  - disgenet
  - pubmed
  - gwascatalog
  - cellmarker
  - go
  - bgee
  - ccle
  - clinicaltrialsgov
  - indra
  product_url: https://github.com/gyorilab/indra_cogex
  secondary_source:
  - indra
warnings:
- This is an automatically generated stub page. Please replace with accurate information
  about this resource.
---
# Pubmed

This is an automatically generated stub page for pubmed. Please update with proper information.