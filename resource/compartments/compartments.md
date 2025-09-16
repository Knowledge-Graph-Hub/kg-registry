---
activity_status: active
category: DataSource
description: COMPARTMENTS is an evidence-weighted subcellular localization knowledge resource that integrates experimental data, manual curation, high-throughput localization screens, automatic text mining, and sequence-based predictions to assign proteins to cellular compartments with confidence scores.
domains:
  - proteomics
  - systems biology
  - biological systems
id: compartments
layout: resource_detail
name: COMPARTMENTS
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
products:
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - chebi
  - cosmic
  - achilles
  - depmap
  - ccle
  - gdsc
  - cellosaurus
  - clue
  - ctd
  - pharmacodb
  - prism
  - drugbank
  - lincs
  - compartments
  - offsides
  - sider
  - drugcentral
  - repohub
  - chemicalchecker
  - repodb
  - disgenet
  - opentargets
  - creeds
  - interpro
  - reactome
  - tissues
  - dorothea
  - progeny
  - gtex
  - hpa
  - go
  - corum
  - huri
  - intact
  - omnipath
  - string
  - bto
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
  secondary_source:
  - bioteque
- id: compartments.portal
  name: COMPARTMENTS Portal
  description: Web interface for exploring protein subcellular localization evidence across integrated sources.
  category: GraphicalInterface
  product_url: https://compartments.jensenlab.org/
- id: compartments.downloads
  name: COMPARTMENTS Bulk Downloads
  description: Bulk data downloads of localization scores and evidence files.
  category: Product
  product_url: https://compartments.jensenlab.org/Downloads
---
# COMPARTMENTS
