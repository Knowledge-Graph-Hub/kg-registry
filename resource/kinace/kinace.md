---
activity_status: active
category: Aggregator
creation_date: '2025-11-05T00:00:00Z'
description: KiNet is a web portal and dataset, originally deposited as KinAce, for aggregating and visualizing kinase-substrate interactions in the human genome. KiNet integrates interaction data from PhosphoSitePlus, iPTMnet, and EPSD with kinase group, protein, gene, pathway, and domain annotations from KinHub, CORAL, the Dark Kinase Knowledgebase, UniProt, HGNC, KEGG, and InterPro.
domains:
  - proteomics
  - systems biology
  - biomedical
  - biological systems
homepage_url: https://kinet.kinametrix.com/
id: "kinace"
infores_id: "kinace"
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: KiNet
products:
  - id: kinace.portal
    category: GraphicalInterface
    name: KiNet Web Portal
    description: Interactive Shiny web interface for exploring and visualizing human kinase-substrate interactions
    product_url: https://kinet.kinametrix.com/
    format: http
    original_source:
      - source: kinace
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: coralkinome
        relation_type: prov:wasDerivedFrom
      - source: darkkinasekb
        relation_type: prov:wasDerivedFrom
      - source: epsd
        relation_type: prov:wasDerivedFrom
      - source: hgnc
        relation_type: prov:wasDerivedFrom
      - source: interpro
        relation_type: prov:wasDerivedFrom
      - source: iptmnet
        relation_type: prov:wasDerivedFrom
      - source: kegg
        relation_type: prov:wasDerivedFrom
      - source: kinhub
        relation_type: prov:wasDerivedFrom
      - source: phosphositeplus
        relation_type: prov:wasDerivedFrom
      - source: uniprot
        relation_type: prov:wasDerivedFrom
  - id: kinace.interactions
    category: GraphProduct
    name: KiNet Full Interaction Dataset
    description: CSV download of the full KiNet human kinase-substrate interaction dataset with source database, evidence, and PMID reference fields
    product_url: https://raw.githubusercontent.com/GauravPandeyLab/KiNet/master/data/ksi_source_full_dataset.csv
    format: csv
    product_file_size: 5180792
    original_source:
      - source: kinace
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: epsd
        relation_type: prov:wasDerivedFrom
      - source: iptmnet
        relation_type: prov:wasDerivedFrom
      - source: phosphositeplus
        relation_type: prov:wasDerivedFrom
  - id: kinace.github_archive
    category: Product
    name: KiNet GitHub Dataset Archive
    description: Zipped GitHub data archive for the KiNet/KinAce web portal and kinase-substrate interaction dataset
    product_url: https://raw.githubusercontent.com/GauravPandeyLab/KiNet/master/data/2023-10-30-kinace-dataset.zip
    compression: zip
    product_file_size: 381292
    original_source:
      - source: kinace
        relation_type: prov:hadPrimarySource
  - id: kinace.zenodo_archive
    category: Product
    name: KinAce Zenodo Archive
    description: Zenodo archive for the KinAce web portal and kinase-substrate interaction dataset
    product_url: https://zenodo.org/api/records/10212986/files/KinAce.zip/content
    compression: zip
    product_file_size: 816896
    original_source:
      - source: kinace
        relation_type: prov:hadPrimarySource
  - id: kinace.code
    category: ProcessProduct
    name: KiNet Source Code
    description: GitHub repository containing the R/Shiny source code and data files for the KiNet web portal
    product_url: https://github.com/GauravPandeyLab/KiNet
    format: http
    original_source:
      - source: kinace
        relation_type: prov:hadPrimarySource
publications:
  - authors:
      - John A. P. Sekar
      - Yan Chak Li
      - Avner Schlessinger
      - Gaurav Pandey
    doi: 10.1038/s41540-024-00442-5
    id: doi:10.1038/s41540-024-00442-5
    journal: npj Systems Biology and Applications
    preferred: true
    title: A web portal for exploring kinase-substrate interactions
    year: '2024'
repository: https://github.com/GauravPandeyLab/KiNet
synonyms:
  - KiNet
  - KinAce
taxon:
  - NCBITaxon:9606
---

# KiNet

## Overview

KiNet is a web portal that aggregates and visualizes the network of interactions between protein kinases and their substrates in the human genome. The platform provides multiple ways to select and explore sets of proteins, displaying known kinase-substrate interactions with phosphorylation site, evidence, and source database details. The archived Zenodo dataset was deposited under the KinAce name.

## Data Sources

KinAce integrates data from multiple authoritative sources:

- **Interactions**: PhosphoSitePlus, iPTMnet, EPSD
- **Kinase groups**: KinHub, CORAL, Dark Kinase Knowledgebase
- **Protein names**: UniProt
- **Gene symbols**: HGNC
- **Pathways**: KEGG
- **Protein domains**: InterPro

## Key Features

### Multiple Access Points
- Search by protein
- Browse by pathway
- Filter by domain
- Create custom protein sets

### Visualization Capabilities
- Network views of kinase-substrate relationships
- Phosphorylation site mapping
- Kinase family groupings
- Interactive exploration tools

### Data Types
- **Proteins**: Human proteome coverage
- **Pathways**: KEGG pathway integration
- **Domains**: InterPro domain annotations
- **Interactions**: Experimentally validated phosphorylation events

## Scope and Coverage

- **Species**: Human (Homo sapiens, NCBITaxon:9606)
- **Focus**: Protein kinases and their substrates
- **Data types**: Phosphorylation sites, kinase-substrate interactions
- **Integration**: Multiple complementary data sources

## Use Cases

- Identifying kinase substrates for target proteins
- Exploring kinase signaling networks
- Studying phosphorylation cascades
- Drug target identification
- Systems biology analysis of phosphorylation networks

## Information Resource ID

This resource has the Information Resource identifier: `infores:kinace`
