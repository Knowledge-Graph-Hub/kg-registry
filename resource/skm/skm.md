---
layout: resource_detail
activity_status: active
id: skm
name: Stress Knowledge Map
description: A comprehensive knowledge graph resource for systems biology analysis of plant stress responses, containing mechanistic models and knowledge networks for plant stress signaling. It includes two knowledge graphs, the mechanistic Plant Stress Signalling model (PSS) and the Comprehensive Knowledge Network (CKN).
domains:
- plant science
- organisms
- systems biology
- pathways
contacts:
- category: Individual
  label: Kristina Gruden
  contact_details:
  - contact_type: email
    value: kristina.gruden@nib.si
- category: Individual
  label: Carissa Bleker
  contact_details:
  - contact_type: email
    value: carissa.bleker@nib.si
- category: Organization
  label: National Institute of Biology Slovenia
  contact_details:
  - contact_type: url
    value: https://www.nib.si/
homepage_url: https://skm.nib.si/
repository: https://github.com/NIB-SI/skm-tools
category: KnowledgeGraph
license:
  label: CC-BY-NC-SA-3.0
  id: http://creativecommons.org/licenses/by-nc-sa/3.0/
version: "1.0"
language: en
publications:
- id: https://doi.org/10.1016/j.xplc.2024.100920
  title: "Stress Knowledge Map: A knowledge graph resource for systems biology analysis of plant stress responses"
  authors:
  - Carissa Bleker
  - Živa Ramšak
  - Andras Bittner
  - Vid Podpečan
  - Maja Zagorščak
  - Bernhard Wurzinger
  - Špela Baebler
  - Marko Petek
  - Maja Križnik
  - Annelotte van Dieren
  - Juliane Gruber
  - Leila Afjehi-Sadat
  - Wolfram Weckwert
  - Anže Županič
  - Markus Teige
  - Ute C. Vothknecht
  - Kristina Gruden
  journal: Plant Communications
  year: "2024"
  doi: doi:10.1016/j.xplc.2024.100920
products:
- id: skm.pss.explorer
  name: PSS Explorer
  description: Interactive search and visualization tool for the mechanistic Plant Stress Signalling model
  product_url: https://skm.nib.si/pss
  category: GraphicalInterface
  original_source:
  - skm
- id: skm.ckn.explorer
  name: CKN Explorer
  description: Interactive search and visualization tool for the Comprehensive Knowledge Network
  product_url: https://skm.nib.si/ckn
  category: GraphicalInterface
  original_source:
  - skm
- id: skm.pss.live.sbgn
  name: PSS Live Download (SBGN-ML)
  description: Current PSS model in Systems Biology Graphical Notation XML format
  product_url: https://skm.nib.si/downloads/pss/public/sbgn
  category: GraphProduct
  original_source:
  - skm
  format: sbgnml
- id: skm.pss.live.sbml
  name: PSS Live Download (SBML)
  description: Current PSS model in Systems Biology Markup Language XML format
  product_url: https://skm.nib.si/downloads/pss/public/sbml
  category: GraphProduct
  original_source:
  - skm
  format: sbml
- id: skm.pss.live.dot
  name: PSS Live Download (DOT)
  description: Current PSS model in DOT Language format compatible with Graphviz
  product_url: https://skm.nib.si/downloads/pss/public/graphviz
  category: GraphProduct
  original_source:
  - skm
  format: dot
- id: skm.pss.live.sif.original.graph
  name: PSS Live Download, original (SIF/LGL)
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape. Reactions are represented as nodes (as in PSS Explorer and database schema).
  product_url: https://skm.nib.si/downloads/pss/public/sif-edges
  category: GraphProduct
  original_source:
  - skm
  format: sif
- id: skm.pss.live.sif.original.annotations
  name: PSS Live Download, original (SIF/LGL), node annotations
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape. Reactions are represented as nodes (as in PSS Explorer and database schema). This file contains the node annotations.
  product_url: https://skm.nib.si/downloads/pss/public/sif-nodes
  category: GraphProduct
  original_source:
  - skm
  format: sif
- id: skm.pss.live.sif.projection.graph
  name: PSS Live Download, projection (SIF/LGL)
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape. Reactions are collapsed to edges.
  product_url: https://skm.nib.si/downloads/pss/public/rxn-edges
  category: GraphProduct
  original_source:
  - skm
  format: sif
- id: skm.pss.live.sif.projection.annotations
  name: PSS Live Download, projection (SIF/LGL), node annotations
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape. Reactions are collapsed to edges. This file contains the node annotations.
  product_url: https://skm.nib.si/downloads/pss/public/rxn-nodes
  category: GraphProduct
  original_source:
  - skm
  format: sif
- id: skm.pss.live.sif.dinar.graph
  name: PSS Live Download, DiNAR (SIF/LGL)
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape. Reactions are collapsed to edges, FunctionalClusters are expanded to arabidopsis identifiers.
  product_url: https://skm.nib.si/downloads/pss/public/dinar-edges
  category: GraphProduct
  original_source:
  - skm
  format: sif
- id: skm.pss.live.boolnet.graph
  name: PSS Live Downloads (BoolNet)
  description: Current PSS model in Boolean network format compatible with BoolDog and BoolNet
  product_url: https://skm.nib.si/downloads/pss/public/boolnet
  category: GraphProduct
  original_source:
  - skm
  format: boolnet
- id: skm.pss.live.boolnet.annotations
  name: PSS Live Downloads (BoolNet), node annotations
  description: Current PSS model in Boolean network format compatible with BoolDog and BoolNet. This file contains the node annotations.
  product_url: https://skm.nib.si/downloads/pss/public/boolnet-annot
  category: GraphProduct
  original_source:
  - skm
  format: boolnet
- id: skm.ckn.v2.graph
  name: CKN v2 (June 2023)
  description: Comprehensive Knowledge Network v2 in SIF/LGL format with 26,234 entities and ~500,000 interactions
  product_url: https://skm.nib.si/downloads/ckn/v2-2023.06
  category: GraphProduct
  original_source:
  - skm
  format: sif
  edge_count: 500000
  node_count: 26234
- id: skm.ckn.v2.annotations
  name: CKN v2 (June 2023), node annotations
  description: Comprehensive Knowledge Network v2 in SIF/LGL format with 26,234 entities and ~500,000 interactions. This file contains the node annotations.
  product_url: https://skm.nib.si/downloads/ckn-annot/v2-2023.06
  category: GraphProduct
  original_source:
  - skm
  format: sif
- id: skm.ckn.v1.graph
  name: CKN v1 (June 2018)
  description: Comprehensive Knowledge Network v1 in SIF/LGL format
  product_url: https://skm.nib.si/downloads/ckn/v1-2018.06
  category: GraphProduct
  original_source:
  - skm
  format: sif
- id: skm.ckn.v1.annotations
  name: CKN v1 (June 2018), node annotations
  description: Comprehensive Knowledge Network v1 in SIF/LGL format. This file contains the node annotations.
  product_url: https://skm.nib.si/downloads/ckn-annot/v1-2018.06
  category: GraphProduct
  original_source:
  - skm
  format: sif
---

# Stress Knowledge Map

The Stress Knowledge Map (SKM) is a comprehensive knowledge graph resource for systems biology analysis of plant stress responses. It provides two complementary knowledge graphs:

## PSS - Plant Stress Signalling Model

PSS is a mechanistic model of plant stress signalling that assembles validated molecular interactions from published resources. It includes the complete stress response cascade within plant cells, covering:

- Stress perception through receptors
- Ca²⁺, reactive oxygen species (ROS), and MAPK signalling cascades  
- Phytohormone biosynthesis and signaling pathways (ABA, JA, SA, ET, IAA, GA, CK)
- Transcriptional and post-transcriptional regulation
- Intersections with growth and development

The model contains genes, gene products, complexes, metabolites, and stress triggers, with interactions including protein-DNA, non-coding RNA-transcript, protein-protein interactions, enzymatic catalysis, and transport reactions.

## CKN - Comprehensive Knowledge Network

CKN is a large-scale, condition-agnostic assembly of experimentally observed physical interactions in Arabidopsis thaliana. It contains:

- 26,234 entities (24,829 genes in Araport)  
- Almost 500,000 interactions
- Protein-DNA interactions, non-coding RNA-transcript interactions, post-translational modifications, and protein-protein interactions
- Reliability ranking system based on experimental approaches

## Key Features

- Interactive visualization tools for both knowledge graphs
- Downloadable data in multiple formats
- Python toolkit for computational analysis
- Focus on Arabidopsis thaliana, potato, tomato, and poplar
- Supports Boolean to ODE modeling approaches
- Community contribution system for new interactions

The resource enables researchers to explore plant stress signaling mechanisms, generate hypotheses, and perform systems-level analysis of plant responses to environmental stresses.
