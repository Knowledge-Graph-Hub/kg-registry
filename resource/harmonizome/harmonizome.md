---
activity_status: active
category: Aggregator
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: avi.maayan@mssm.edu
      - contact_type: url
        value: https://labs.icahn.mssm.edu/maayanlab/
    label: Ma'ayan Laboratory
creation_date: '2026-06-02T00:00:00Z'
description: Harmonizome is an aggregator of processed gene and protein datasets from diverse online biomedical resources. Harmonizome 3.0 reports 114,997,358 associations among 58,935 genes and 518,340 attributes from 172 datasets provided by 87 resources.
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
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: achilles
      - relation_type: prov:wasDerivedFrom
        source: biogps
      - relation_type: prov:wasDerivedFrom
        source: ccle
      - relation_type: prov:wasDerivedFrom
        source: cellmarker
      - relation_type: prov:wasDerivedFrom
        source: chea
      - relation_type: prov:wasDerivedFrom
        source: clinvar
      - relation_type: prov:wasDerivedFrom
        source: cmap
      - relation_type: prov:wasDerivedFrom
        source: compartments
      - relation_type: prov:wasDerivedFrom
        source: corum
      - relation_type: prov:wasDerivedFrom
        source: cosmic
      - relation_type: prov:wasDerivedFrom
        source: ctd
      - relation_type: prov:wasDerivedFrom
        source: depmap
      - relation_type: prov:wasDerivedFrom
        source: diseases
      - relation_type: prov:wasDerivedFrom
        source: disgenet
      - relation_type: prov:wasDerivedFrom
        source: drugbank
      - relation_type: prov:wasDerivedFrom
        source: encode
      - relation_type: prov:wasDerivedFrom
        source: gdsc
      - relation_type: prov:wasDerivedFrom
        source: geo
      - relation_type: prov:wasDerivedFrom
        source: glygen
      - relation_type: prov:wasDerivedFrom
        source: go
      - relation_type: prov:wasDerivedFrom
        source: gtex
      - relation_type: prov:wasDerivedFrom
        source: gwascatalog
      - relation_type: prov:wasDerivedFrom
        source: hmdb
      - relation_type: prov:wasDerivedFrom
        source: hp
      - relation_type: prov:wasDerivedFrom
        source: hpa
      - relation_type: prov:wasDerivedFrom
        source: hubmap
      - relation_type: prov:wasDerivedFrom
        source: impc
      - relation_type: prov:wasDerivedFrom
        source: interpro
      - relation_type: prov:wasDerivedFrom
        source: kegg
      - relation_type: prov:wasDerivedFrom
        source: lincs-l1000
      - relation_type: prov:wasDerivedFrom
        source: mirtarbase
      - relation_type: prov:wasDerivedFrom
        source: motrpac
      - relation_type: prov:wasDerivedFrom
        source: mp
      - relation_type: prov:wasDerivedFrom
        source: msigdb
      - relation_type: prov:wasDerivedFrom
        source: omim
      - relation_type: prov:wasDerivedFrom
        source: panther
      - relation_type: prov:wasDerivedFrom
        source: pathwaycommons
      - relation_type: prov:wasDerivedFrom
        source: pfocr
      - relation_type: prov:wasDerivedFrom
        source: phosphositeplus
      - relation_type: prov:wasDerivedFrom
        source: pid
      - relation_type: prov:wasDerivedFrom
        source: reactome
      - relation_type: prov:wasDerivedFrom
        source: tcga
      - relation_type: prov:wasDerivedFrom
        source: tissues
      - relation_type: prov:wasDerivedFrom
        source: wikipathways
  - category: DocumentationProduct
    description: Harmonizome documentation describing dataset pages, API access, downloads, and the Harmonizome knowledge graph API and graph serialization.
    id: harmonizome.documentation
    name: Harmonizome Documentation
    original_source:
      - relation_type: prov:hadPrimarySource
        source: harmonizome
    product_url: https://maayanlab.cloud/Harmonizome/documentation
  - category: GraphicalInterface
    description: Interactive web interface for exploring the Harmonizome knowledge graph with gene-centric network visualization.
    format: http
    id: harmonizome.kg-portal
    name: Harmonizome Knowledge Graph Explorer
    original_source:
      - relation_type: prov:hadPrimarySource
        source: harmonizome
    product_url: https://harmonizome-kg.maayanlab.cloud/
  - category: ProgrammingInterface
    connection_url: https://harmonizome-kg.maayanlab.cloud/api/knowledge_graph
    description: API endpoint for programmatic access to Harmonizome knowledge graph neighborhoods, with filter parameters documented in the Harmonizome knowledge graph API guide.
    format: json
    id: harmonizome.kg-api
    name: Harmonizome Knowledge Graph API
    original_source:
      - relation_type: prov:hadPrimarySource
        source: harmonizome
    product_url: https://maayanlab.cloud/Harmonizome/documentation#kg-api
  - category: GraphProduct
    description: Neo4j knowledge graph serialization of Harmonizome processed datasets, including genes, attributes, resources, datasets, and gene-attribute associations.
    dump_format: neo4j
    format: neo4j
    id: harmonizome.kg-neo4j
    latest_version: '3.0'
    name: Harmonizome Knowledge Graph Neo4j Database
    original_source:
      - relation_type: prov:hadPrimarySource
        source: harmonizome
    product_url: https://harmonizome-kg.maayanlab.cloud/
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: achilles
      - relation_type: prov:wasDerivedFrom
        source: biogps
      - relation_type: prov:wasDerivedFrom
        source: ccle
      - relation_type: prov:wasDerivedFrom
        source: cellmarker
      - relation_type: prov:wasDerivedFrom
        source: chea
      - relation_type: prov:wasDerivedFrom
        source: clinvar
      - relation_type: prov:wasDerivedFrom
        source: cmap
      - relation_type: prov:wasDerivedFrom
        source: compartments
      - relation_type: prov:wasDerivedFrom
        source: corum
      - relation_type: prov:wasDerivedFrom
        source: cosmic
      - relation_type: prov:wasDerivedFrom
        source: ctd
      - relation_type: prov:wasDerivedFrom
        source: depmap
      - relation_type: prov:wasDerivedFrom
        source: diseases
      - relation_type: prov:wasDerivedFrom
        source: disgenet
      - relation_type: prov:wasDerivedFrom
        source: drugbank
      - relation_type: prov:wasDerivedFrom
        source: encode
      - relation_type: prov:wasDerivedFrom
        source: gdsc
      - relation_type: prov:wasDerivedFrom
        source: geo
      - relation_type: prov:wasDerivedFrom
        source: glygen
      - relation_type: prov:wasDerivedFrom
        source: go
      - relation_type: prov:wasDerivedFrom
        source: gtex
      - relation_type: prov:wasDerivedFrom
        source: gwascatalog
      - relation_type: prov:wasDerivedFrom
        source: hmdb
      - relation_type: prov:wasDerivedFrom
        source: hp
      - relation_type: prov:wasDerivedFrom
        source: hpa
      - relation_type: prov:wasDerivedFrom
        source: hubmap
      - relation_type: prov:wasDerivedFrom
        source: impc
      - relation_type: prov:wasDerivedFrom
        source: interpro
      - relation_type: prov:wasDerivedFrom
        source: kegg
      - relation_type: prov:wasDerivedFrom
        source: lincs-l1000
      - relation_type: prov:wasDerivedFrom
        source: mirtarbase
      - relation_type: prov:wasDerivedFrom
        source: motrpac
      - relation_type: prov:wasDerivedFrom
        source: mp
      - relation_type: prov:wasDerivedFrom
        source: msigdb
      - relation_type: prov:wasDerivedFrom
        source: omim
      - relation_type: prov:wasDerivedFrom
        source: panther
      - relation_type: prov:wasDerivedFrom
        source: pathwaycommons
      - relation_type: prov:wasDerivedFrom
        source: pfocr
      - relation_type: prov:wasDerivedFrom
        source: phosphositeplus
      - relation_type: prov:wasDerivedFrom
        source: pid
      - relation_type: prov:wasDerivedFrom
        source: reactome
      - relation_type: prov:wasDerivedFrom
        source: tcga
      - relation_type: prov:wasDerivedFrom
        source: tissues
      - relation_type: prov:wasDerivedFrom
        source: wikipathways
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
online biological resources. Harmonizome 3.0 reports 172 datasets from 87
resources; the current download table displays source labels including Achilles,
Allen Brain Atlas, BioGPS, CCLE, ChEA, ClinVar, CTD, DepMap, DisGeNET, DrugBank,
ENCODE, GEO, GO, GTEx, GWAS Catalog, HPA, KEGG, MSigDB, Pathway Commons,
PhosphoSitePlus, Reactome, TCGA, HuBMAP, WikiPathways, and many additional
experimental, literature-derived, and pathway resources.

The Harmonizome knowledge graph portal, API, and Neo4j serialization are treated
as products of this Harmonizome resource rather than as a separate
`harmonizome-kg` resource.
