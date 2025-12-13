---
activity_status: active
category: KnowledgeGraph
collection:
- ber
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: kristina.gruden@nib.si
  label: Kristina Gruden
- category: Individual
  contact_details:
  - contact_type: email
    value: carissa.bleker@nib.si
  label: Carissa Bleker
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.nib.si/
  label: National Institute of Biology Slovenia
description: A comprehensive knowledge graph resource for systems biology analysis
  of plant stress responses, containing mechanistic models and knowledge networks
  for plant stress signaling. It includes two knowledge graphs, the mechanistic Plant
  Stress Signalling model (PSS) and the Comprehensive Knowledge Network (CKN).
domains:
- plant science
- organisms
- systems biology
- pathways
homepage_url: https://skm.nib.si/
id: skm
language: en
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by-nc-sa/3.0/
  label: CC-BY-NC-SA-3.0
name: Stress Knowledge Map
products:
- category: GraphicalInterface
  description: Interactive search and visualization tool for the mechanistic Plant
    Stress Signalling model
  id: skm.pss.explorer
  name: PSS Explorer
  original_source:
  - skm
  product_url: https://skm.nib.si/pss
- category: GraphicalInterface
  description: Interactive search and visualization tool for the Comprehensive Knowledge
    Network
  id: skm.ckn.explorer
  name: CKN Explorer
  original_source:
  - skm
  product_url: https://skm.nib.si/ckn
- category: GraphProduct
  description: Current PSS model in Systems Biology Graphical Notation XML format
  format: sbgnml
  id: skm.pss.live.sbgn
  name: PSS Live Download (SBGN-ML)
  original_source:
  - skm
  product_file_size: 3204548
  product_url: https://skm.nib.si/downloads/pss/public/sbgn
- category: GraphProduct
  description: Current PSS model in Systems Biology Markup Language XML format
  format: sbml
  id: skm.pss.live.sbml
  name: PSS Live Download (SBML)
  original_source:
  - skm
  product_file_size: 548527
  product_url: https://skm.nib.si/downloads/pss/public/sbml
- category: GraphProduct
  description: Current PSS model in DOT Language format compatible with Graphviz
  format: dot
  id: skm.pss.live.dot
  name: PSS Live Download (DOT)
  original_source:
  - skm
  product_file_size: 595369
  product_url: https://skm.nib.si/downloads/pss/public/graphviz
- category: GraphProduct
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape.
    Reactions are represented as nodes (as in PSS Explorer and database schema).
  format: sif
  id: skm.pss.live.sif.original.graph
  name: PSS Live Download, original (SIF/LGL)
  original_source:
  - skm
  product_file_size: 161651
  product_url: https://skm.nib.si/downloads/pss/public/sif-edges
- category: GraphProduct
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape.
    Reactions are represented as nodes (as in PSS Explorer and database schema). This
    file contains the node annotations.
  format: sif
  id: skm.pss.live.sif.original.annotations
  name: PSS Live Download, original (SIF/LGL), node annotations
  original_source:
  - skm
  product_file_size: 401897
  product_url: https://skm.nib.si/downloads/pss/public/sif-nodes
- category: GraphProduct
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape.
    Reactions are collapsed to edges.
  format: sif
  id: skm.pss.live.sif.projection.graph
  name: PSS Live Download, projection (SIF/LGL)
  original_source:
  - skm
  product_file_size: 253631
  product_url: https://skm.nib.si/downloads/pss/public/rxn-edges
- category: GraphProduct
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape.
    Reactions are collapsed to edges. This file contains the node annotations.
  format: sif
  id: skm.pss.live.sif.projection.annotations
  name: PSS Live Download, projection (SIF/LGL), node annotations
  original_source:
  - skm
  product_file_size: 163587
  product_url: https://skm.nib.si/downloads/pss/public/rxn-nodes
- category: GraphProduct
  description: Current PSS model in Simple Interaction Format compatible with Cytoscape.
    Reactions are collapsed to edges, FunctionalClusters are expanded to arabidopsis
    identifiers.
  format: sif
  id: skm.pss.live.sif.dinar.graph
  name: PSS Live Download, DiNAR (SIF/LGL)
  original_source:
  - skm
  product_file_size: 361747
  product_url: https://skm.nib.si/downloads/pss/public/dinar-edges
- category: GraphProduct
  description: Current PSS model in Boolean network format compatible with BoolDog
    and BoolNet
  format: boolnet
  id: skm.pss.live.boolnet.graph
  name: PSS Live Downloads (BoolNet)
  original_source:
  - skm
  product_file_size: 53198
  product_url: https://skm.nib.si/downloads/pss/public/boolnet
- category: GraphProduct
  description: Current PSS model in Boolean network format compatible with BoolDog
    and BoolNet. This file contains the node annotations.
  format: boolnet
  id: skm.pss.live.boolnet.annotations
  name: PSS Live Downloads (BoolNet), node annotations
  original_source:
  - skm
  product_file_size: 70946
  product_url: https://skm.nib.si/downloads/pss/public/boolnet-annot
- category: GraphProduct
  description: Comprehensive Knowledge Network v2 in SIF/LGL format with 26,234 entities
    and ~500,000 interactions
  edge_count: 500000
  format: sif
  id: skm.ckn.v2.graph
  name: CKN v2 (June 2023)
  node_count: 26234
  original_source:
  - skm
  product_file_size: 2732107
  product_url: https://skm.nib.si/downloads/ckn/v2-2023.06
- category: GraphProduct
  description: Comprehensive Knowledge Network v2 in SIF/LGL format with 26,234 entities
    and ~500,000 interactions. This file contains the node annotations.
  format: sif
  id: skm.ckn.v2.annotations
  name: CKN v2 (June 2023), node annotations
  original_source:
  - skm
  product_file_size: 885747
  product_url: https://skm.nib.si/downloads/ckn-annot/v2-2023.06
- category: GraphProduct
  description: Comprehensive Knowledge Network v1 in SIF/LGL format
  format: sif
  id: skm.ckn.v1.graph
  name: CKN v1 (June 2018)
  original_source:
  - skm
  product_file_size: 318666
  product_url: https://skm.nib.si/downloads/ckn/v1-2018.06
- category: GraphProduct
  description: Comprehensive Knowledge Network v1 in SIF/LGL format. This file contains
    the node annotations.
  format: sif
  id: skm.ckn.v1.annotations
  name: CKN v1 (June 2018), node annotations
  original_source:
  - skm
  product_file_size: 702407
  product_url: https://skm.nib.si/downloads/ckn-annot/v1-2018.06
publications:
- authors:
  - Carissa Bleker
  - "\u017Diva Ram\u0161ak"
  - Andras Bittner
  - "Vid Podpe\u010Dan"
  - "Maja Zagor\u0161\u010Dak"
  - Bernhard Wurzinger
  - "\u0160pela Baebler"
  - Marko Petek
  - "Maja Kri\u017Enik"
  - Annelotte van Dieren
  - Juliane Gruber
  - Leila Afjehi-Sadat
  - Wolfram Weckwert
  - "An\u017Ee \u017Dupani\u010D"
  - Markus Teige
  - Ute C. Vothknecht
  - Kristina Gruden
  doi: doi:10.1016/j.xplc.2024.100920
  id: https://doi.org/10.1016/j.xplc.2024.100920
  journal: Plant Communications
  title: 'Stress Knowledge Map: A knowledge graph resource for systems biology analysis
    of plant stress responses'
  year: '2024'
repository: https://github.com/NIB-SI/skm-tools
version: '1.0'
taxon:
- NCBITaxon:33090
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