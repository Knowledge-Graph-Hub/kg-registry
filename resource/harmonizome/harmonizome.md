---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: avi.maayan@mssm.edu
      - contact_type: url
        value: https://labs.icahn.mssm.edu/maayanlab/
    label: Ma'ayan Laboratory
creation_date: '2026-06-02T00:00:00Z'
description: Harmonizome is a collection of processed datasets gathered from diverse online resources to serve and mine knowledge about genes and proteins across many functional genomics, proteomics, disease, drug, and pathway domains.
domains:
  - biomedical
  - genomics
  - systems biology
  - proteomics
homepage_url: https://maayanlab.cloud/Harmonizome/
id: harmonizome
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Harmonizome
products:
  - category: GraphicalInterface
    description: Harmonizome 3.0 web portal for searching and exploring processed gene and protein datasets, resources, genes, attributes, and associations.
    id: harmonizome.portal
    name: Harmonizome Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: harmonizome
    product_url: https://maayanlab.cloud/Harmonizome/
  - category: Product
    description: Harmonizome 3.0 processed dataset downloads, including dataset-specific association files and knowledge graph serialization downloads.
    format: mixed
    id: harmonizome.downloads
    name: Harmonizome Downloads
    original_source:
      - relation_type: prov:hadPrimarySource
        source: harmonizome
    product_url: https://maayanlab.cloud/Harmonizome/download
  - category: DocumentationProduct
    description: Harmonizome documentation describing dataset pages, API access, downloads, and the Harmonizome-KG API and graph serialization.
    id: harmonizome.documentation
    name: Harmonizome Documentation
    original_source:
      - relation_type: prov:hadPrimarySource
        source: harmonizome
    product_url: https://maayanlab.cloud/Harmonizome/documentation
  - category: GraphicalInterface
    description: Interactive web interface for exploring the Harmonizome knowledge graph with gene-centric network visualization
    format: http
    id: harmonizome-kg.portal
    name: Harmonizome-KG Explorer
    original_source:
      - relation_type: prov:hadPrimarySource
        source: harmonizome-kg
    product_url: https://harmonizome-kg.maayanlab.cloud/
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: harmonizome
  - category: ProgrammingInterface
    connection_url: https://harmonizome-kg.maayanlab.cloud/api/knowledge_graph
    description: API endpoint for programmatic access to Harmonizome-KG neighborhoods, with filter parameters documented in the Harmonizome knowledge graph API guide
    format: json
    id: harmonizome-kg.api
    name: Harmonizome-KG API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: harmonizome-kg
    product_url: https://maayanlab.cloud/Harmonizome/documentation#kg-api
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: harmonizome
  - category: GraphProduct
    description: Neo4j knowledge graph serialization of Harmonizome processed datasets, including genes, attributes, resources, datasets, and gene-attribute associations
    dump_format: neo4j
    format: neo4j
    id: harmonizome-kg.graph
    latest_version: '3.0'
    name: Harmonizome-KG Neo4j Database
    original_source:
      - relation_type: prov:hadPrimarySource
        source: harmonizome-kg
    product_url: https://harmonizome-kg.maayanlab.cloud/
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: harmonizome
publications:
  - authors:
      - Ido Diamant
      - Daniel J B Clarke
      - John Erol Evangelista
      - Nathania Lingam
      - Avi Ma'ayan
    doi: 10.1093/nar/gkae1080
    id: doi:10.1093/nar/gkae1080
    journal: Nucleic Acids Research
    preferred: true
    title: 'Harmonizome 3.0: integrated knowledge about genes and proteins from diverse multi-omics resources'
    year: '2025'
  - authors:
      - Rouillard AD
      - Gundersen GW
      - Fernandez NF
      - Wang Z
      - Monteiro CD
      - McDermott MG
      - Ma'ayan A
    doi: 10.1093/database/baw100
    id: doi:10.1093/database/baw100
    journal: Database
    preferred: false
    title: 'The harmonizome: a collection of processed datasets gathered to serve and mine knowledge about genes and proteins'
    year: '2016'
repository: https://github.com/MaayanLab/HarmonizomePythonScripts
taxon:
  - NCBITaxon:9606
---

# Harmonizome

Harmonizome integrates processed datasets about genes and proteins from many
online biological resources. Harmonizome 3.0 adds updated dataset pages,
downloadable association files, and knowledge graph serializations used by
Harmonizome-KG.
