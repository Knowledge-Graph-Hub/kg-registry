---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: http://www.licpathway.net/ENdb/Contact.php
  - contact_type: email
    value: lcqbio@163.com
  label: School of Medical Informatics, Daqing Campus, Harbin Medical University
creation_date: '2026-06-18T00:00:00Z'
description: ENdb is a manually curated database of experimentally validated enhancers
  for human and mouse, compiled from published literature. Each entry links an enhancer
  to its experimentally supported target gene(s) and includes detailed regulatory
  annotations such as the validation experiment type, associated transcription factors,
  disease and tissue/cell-line context, and references to the supporting publications.
  The database provides browse, search, genome browser, and bulk download interfaces,
  and serves as an upstream primary source for integrated resources including GenomicKB.
domains:
- genomics
- systems biology
- biomedical
homepage_url: http://www.licpathway.net/ENdb/
id: endb
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: ENdb
products:
- category: GraphicalInterface
  description: Web interface for browsing manually curated, experimentally validated
    enhancers and their target genes and regulatory annotations in ENdb.
  id: endb.browse
  name: ENdb Browse
  original_source:
  - relation_type: prov:hadPrimarySource
    source: endb
  product_url: http://www.licpathway.net/ENdb/Browse.php
- category: Product
  description: Bulk download of the ENdb dataset of experimentally supported enhancer-target
    gene records and associated regulatory metadata.
  id: endb.download
  name: ENdb Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: endb
  product_url: http://www.licpathway.net/ENdb/Download.php
- category: GraphProduct
  description: GenomicKB 1.0 Neo4j Database Dump (Requires license)
  dump_format: neo4j
  id: genomickb.graph
  name: GenomicKB Graph Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genomickb
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: dbvar
  - relation_type: prov:hadPrimarySource
    source: endb
  - relation_type: prov:hadPrimarySource
    source: enhanceratlas
  - relation_type: prov:hadPrimarySource
    source: ccre
  - relation_type: prov:hadPrimarySource
    source: fire
  - relation_type: prov:hadPrimarySource
    source: motifmap
  product_url: https://available-inventions.umich.edu/product/genomickb-a-knowledgebase-for-the-human-genome
publications:
- authors:
  - Xuefeng Bai
  - Shanshan Shi
  - Bo Ai
  - Yong Jiang
  - Yuejuan Liu
  - Xiaole Han
  - Mingcong Xu
  - Qi Pan
  - Fan Wang
  - Qiuyu Wang
  - Jian Zhang
  - Xuecang Li
  - Chenchen Feng
  - Yanyu Li
  - Yuezhu Wang
  - Yiwei Song
  - Ke Feng
  - Chunquan Li
  doi: 10.1093/nar/gkz973
  id: https://pubmed.ncbi.nlm.nih.gov/31665430
  journal: Nucleic Acids Res
  preferred: true
  title: 'ENdb: a manually curated database of experimentally supported enhancers
    for human and mouse'
  year: '2020'
---
# ENdb

ENdb is a manually curated database of experimentally validated enhancers for
human and mouse. Drawing on published literature, it records enhancer-to-target
gene relationships together with detailed regulatory context, including the
experimental validation method, associated transcription factors, and disease
and tissue/cell-line annotations. ENdb offers browse, search, genome browser,
and download interfaces, and acts as an upstream primary source for integrated
knowledge graphs such as GenomicKB.