---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Organization
    contact_details:
      - contact_type: github
        value: "KChen-lab"
      - contact_type: url
        value: "https://github.com/KChen-lab"
    label: KChen Lab
creation_date: '2026-06-12T00:00:00Z'
description: Immune Cell Knowledge Graph (ICKG) is a set of immune cell type-specific knowledge graphs built from cancer immunotherapy-focused PubMed abstracts using large language models and human-verifiable validation. The graphs capture directed, literature-supported relationships among genes, pathways, immune functions, and related biomedical entities to support immune program interpretation and gene set annotation.
domains:
  - biomedical
  - immunology
homepage_url: https://kchen-lab.github.io/immune-knowledgegraph.github.io/
id: "ickg"
last_modified_date: '2026-06-12T00:00:00Z'
layout: resource_detail
name: Immune Cell Knowledge Graph
products:
  - category: GraphProduct
    description: Immune cell type-specific node and relationship CSV files for ICKG, including T cell, NK cell, and B cell graph exports.
    format: csv
    id: "ickg.graph-data"
    name: ICKG graph data
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ickg
      - relation_type: prov:hadPrimarySource
        source: pubmed
    product_url: https://github.com/KChen-lab/immune-knowledgegraph.github.io/tree/main/data
  - category: GraphicalInterface
    description: Web application for ICKG-based immune cell type-specific gene set annotation and pathway relationship analysis.
    format: http
    id: "ickg.portal"
    name: Immune Cell Knowledge Graph portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ickg
    product_url: https://kchen-lab.github.io/immune-knowledgegraph.github.io/
  - category: ProcessProduct
    description: Source code and models used for constructing and using Immune Cell Knowledge Graphs.
    id: "ickg.code"
    name: ICKG code repository
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ickg
    product_url: https://github.com/KChen-lab/ICKG
publications:
  - authors:
      - Shan He
      - Yukun Tan
      - Qing Ye
      - Matthew M. Gubin
      - Merve Dede
      - Hind Rafei
      - Weiyi Peng
      - Katayoun Rezvani
    doi: "10.1038/s44387-025-00060-4"
    id: "doi:10.1038/s44387-025-00060-4"
    journal: npj Artificial Intelligence
    title: AI-powered Immune Cell Knowledge Graph (ICKG) with granular immune contexts enables immune program interpretation
    year: "2026"
repository: https://github.com/KChen-lab/ICKG
taxon:
  - NCBITaxon:9606
---

Immune Cell Knowledge Graph (ICKG) provides immune cell type-specific, literature-derived
knowledge graphs and an interactive portal for interpreting immune gene sets in
context.
