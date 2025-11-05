---
activity_status: active
category: Aggregator
creation_date: '2025-11-05T00:00:00Z'
description: The KinAce web portal aggregates and visualizes the network of interactions between protein kinases and their substrates in the human genome. KinAce integrates data from multiple sources including PhosphoSitePlus, iPTMnet, EPSD, KinHub, CORAL, Dark Kinase Knowledgebase, UniProt, HGNC, KEGG, and InterPro, providing comprehensive phosphorylation site data and kinase-substrate relationships.
domains:
  - proteomics
  - systems biology
  - biomedical
  - biological systems
homepage_url: https://kinace.kinametrix.com/
id: "kinace"
infores_id: "kinace"
last_modified_date: '2025-11-05T00:00:00Z'
layout: resource_detail
name: KinAce
products:
  - id: kinace.portal
    category: GraphicalInterface
    name: KinAce Web Portal
    description: Interactive web interface for exploring and visualizing kinase-substrate interactions
    product_url: https://kinace.kinametrix.com/
    format: http
    original_source:
      - phosphositeplus
      - iptmnet
      - uniprot
      - epsd
      - kinhub
      - coralkinome
      - darkkinasekb
      - hgnc
      - kegg
      - interpro
    secondary_source:
      - kinace
synonyms:
  - KinAce
taxon:
  - NCBITaxon:9606
---

# KinAce

## Overview

KinAce is a web portal that aggregates and visualizes the network of interactions between protein kinases and their substrates in the human genome. The platform provides multiple ways to select and explore sets of proteins, displaying known kinase-substrate interactions with comprehensive phosphorylation site data.

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
