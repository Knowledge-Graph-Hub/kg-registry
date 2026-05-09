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
infores_id: bioportal
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
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioportal
  product_url: https://bioportal.bioontology.org/
- category: ProgrammingInterface
  description: REST API for ontology concepts, search, mappings, metrics, and downloads
  format: http
  id: bioportal.api
  name: BioPortal REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioportal
  product_url: http://data.bioontology.org/
- category: GraphProduct
  description: PheKnowLator graph files, including subsets with and without inverse
    relations.
  format: owl
  id: pheknowlator.graph
  latest_version: current_build
  name: PheKnowLator graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioportal
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: genemania
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pheknowlator
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vo
  product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
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
taxon:
- NCBITaxon:9606
warnings:
- Some ontologies have distinct licenses; review individual ontology license metadata
  before reuse.
---
# BioPortal

BioPortal hosts over a thousand biomedical ontologies with search, mappings, visualization, downloads, and programmatic access.