---
activity_status: active
category: Aggregator
creation_date: '2025-08-20T00:00:00Z'
description: BioPortal is a comprehensive open repository and portal for biomedical
  ontologies and terminologies, providing search, browsing, mappings, versioned downloads,
  REST APIs, widgets, and analytics to support data integration, annotation, and semantic
  interoperability in the life and health sciences.
domains:
- biomedical
- clinical
- information technology
- upper
id: bioportal
last_modified_date: '2025-09-16T00:00:00Z'
layout: resource_detail
license:
  id: https://www.bioontology.org/terms/
  label: BioPortal Terms of Use (includes attribution & reuse conditions)
name: BioPortal
products:
- category: GraphicalInterface
  description: Web portal for searching, browsing, and visualizing biomedical ontologies
    and mappings
  format: http
  id: bioportal.portal
  name: BioPortal Portal
  product_url: https://bioportal.bioontology.org/
- category: ProgrammingInterface
  description: REST API for ontology concepts, search, mappings, metrics, and downloads
  format: http
  id: bioportal.api
  name: BioPortal REST API
  product_url: http://data.bioontology.org/
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
- doi: 10.1093/nar/gkaf402
  id: doi:10.1093/nar/gkaf402
  journal: Nucleic Acids Research
  title: 'BioPortal: an open community resource for sharing, searching, and utilizing
    biomedical ontologies'
  year: '2025'
warnings:
- Some ontologies have distinct licenses; review individual ontology license metadata
  before reuse.
---
# BioPortal

BioPortal hosts over a thousand biomedical ontologies with search, mappings, visualization, downloads, and programmatic access.