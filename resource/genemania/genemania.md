---
activity_status: active
category: DataSource
creation_date: '2025-08-20T00:00:00Z'
description: GeneMANIA is a gene function prediction resource that integrates many
  types of functional association networks (co-expression, protein and genetic interactions,
  pathways, co-localization, and shared protein domains) and uses adaptive network
  weighting with label propagation to prioritize related genes and expand gene lists.
domains:
- genomics
- biomedical
- proteomics
homepage_url: https://genemania.org/
id: genemania
last_modified_date: '2025-08-20T00:00:00Z'
layout: resource_detail
name: GeneMANIA
products:
- category: GraphicalInterface
  description: Web interface for searching, visualizing, and analyzing functional
    association networks
  id: genemania.web
  name: GeneMANIA Web Interface
  product_url: https://genemania.org/
- category: GraphProduct
  description: PheKnowLator graph files, including subsets with and without inverse
    relations.
  format: owl
  id: pheknowlator.graph
  latest_version: current_build
  name: PheKnowLator graph
  original_source:
  - cl
  - clo
  - chebi
  - go
  - hp
  - mondo
  - pw
  - pr
  - ro
  - so
  - uberon
  - vo
  - bioportal
  - clinvar
  - ctd
  - disgenet
  - ensembl
  - genemania
  - hgnc
  - hpa
  - ncbigene
  - medgen
  - reactome
  - string
  - uniprot
  product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
  secondary_source:
  - pheknowlator
  versions:
  - v1.0.0
  - v2.0.0
  - v2.1.0
  - v3.0.2
  - v4.0.0
  - current_build
publications:
- authors:
  - Warde-Farley D
  - Donaldson SL
  - Comes O
  - Zuberi K
  - Badrawi R
  - et al.
  doi: 10.1093/nar/gkq537
  id: doi:10.1093/nar/gkq537
  journal: Nucleic Acids Research
  preferred: true
  title: 'The GeneMANIA prediction server: biological network integration for gene
    prioritization and predicting gene function'
  year: '2010'
usages:
- description: The PheKnowLator knowledge graph ingests GeneMANIA functional association
    networks to construct gene-to-gene associations (e.g., co-expression and interaction
    edges) during its build.
  id: pheknowlator-gene-gene-edges
  label: "PheKnowLator gene\u2013gene edges"
  type: actual
  url: https://github.com/callahantiff/PheKnowLator/wiki
---
GeneMANIA helps predict the function of genes and gene sets by integrating heterogeneous
functional genomics data across organisms and returning an interactive network with
ranked related genes and per-dataset contribution weights.