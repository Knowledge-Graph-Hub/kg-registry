---
activity_status: active
category: DataModel
creation_date: '2025-08-20T00:00:00Z'
description: The Vaccine Ontology (VO) is a community ontology that represents vaccines,
  vaccine components, vaccine administration, host responses, pathogens, and related
  concepts. VO supports standardized representation, data integration, and analysis
  of vaccine-related knowledge across resources.
domains:
- immunology
- health
- organisms
homepage_url: https://obofoundry.org/ontology/vo.html
id: vo
last_modified_date: '2025-08-20T00:00:00Z'
layout: resource_detail
name: Vaccine Ontology
products:
- category: DataModelProduct
  description: OWL release of VO
  format: owl
  id: vo.owl
  name: Vaccine Ontology OWL release
  original_source:
  - bfo
  - iao
  - chebi
  - ncbitaxon
  - vo
  product_file_size: 1466262
  product_url: http://purl.obolibrary.org/obo/vo.owl
  secondary_source:
  - vo
- category: DataModelProduct
  description: OBO release of VO
  format: obo
  id: vo.obo
  name: Vaccine Ontology OBO release
  original_source:
  - bfo
  - iao
  - chebi
  - ncbitaxon
  - vo
  product_url: http://purl.obolibrary.org/obo/vo.obo
  secondary_source:
  - vo
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-20: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-21: HTTP 404 error
    when accessing file'
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
---
VO provides a standardized vocabulary for vaccines and related entities, facilitating interoperability
among vaccine data resources and supporting computational analysis.