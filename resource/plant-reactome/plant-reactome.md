---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://plantreactome.gramene.org/
  id: gramene
  label: Gramene Project
creation_date: '2025-12-17T00:00:00Z'
description: Plant Reactome is a freely-accessible, open-source pathway knowledgebase
  for comparative pathway analysis and systems biology in plants. It provides manually
  curated pathways in rice with gene-orthology based projections across 129 plant
  species.
domains:
- plant biology
- pathways
- systems biology
funding:
- Gramene
homepage_url: https://plantreactome.gramene.org/
id: plant-reactome
infores_id: plant-reactome
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Plant Reactome
products:
- category: GraphicalInterface
  description: Web portal for browsing, searching, and visualizing plant pathway data
    with interactive pathway diagrams and comparative analysis tools
  format: http
  id: plant-reactome.portal
  is_public: true
  name: Plant Reactome Web Portal
  product_url: https://plantreactome.gramene.org/
- category: ProgrammingInterface
  description: RESTful Content Service API for programmatic access to pathway data,
    entities, and structures in JSON format
  format: http
  id: plant-reactome.api
  is_public: true
  name: Plant Reactome REST API
  product_url: https://plantreactome.gramene.org/index.php?option=com_content&view=article&id=217&Itemid=255
- category: Product
  compression: zip
  description: BioPAX3 format pathway data downloads organized by plant species
  format: biopax
  id: plant-reactome.biopax
  name: Plant Reactome BioPAX3 Data
  product_url: https://plantreactome.gramene.org/download/current/biopax3.zip
- category: Product
  compression: zip
  description: SBGN format pathway diagrams and pathway descriptions for plant pathway
    visualization
  format: sbgnml
  id: plant-reactome.sbgn
  name: Plant Reactome SBGN Diagrams
  product_url: https://plantreactome.gramene.org/download/current/
- category: Product
  description: Scalable Vector Graphics (SVG) format pathway diagrams for interactive
    and high-quality pathway visualization
  format: svg
  id: plant-reactome.svg
  name: Plant Reactome SVG Diagrams
  product_url: https://plantreactome.gramene.org/download/current/
- category: Product
  description: PNG raster image format pathway diagrams for static pathway visualization
  format: png
  id: plant-reactome.png
  name: Plant Reactome PNG Diagrams
  product_url: https://plantreactome.gramene.org/download/current/
- category: MappingProduct
  description: Identifier mapping files linking stable pathway identifiers with associated
    genes, reactions, and pathways across plant species
  format: csv
  id: plant-reactome.mappings
  name: Plant Reactome Identifier Mappings
  product_url: https://plantreactome.gramene.org/index.php?option=com_content&view=article&id=18&Itemid=242&lang=en
publications:
- authors:
  - Gupta P
  - Elser J
  - Hooks E
  - D'Eustachio P
  - Jaiswal P
  - Naithani S
  doi: 10.1093/nar/gkad1052
  id: doi:10.1093/nar/gkad1052
  journal: Nucleic Acids Research
  preferred: true
  title: 'Plant Reactome Knowledgebase: empowering plant pathway exploration and OMICS
    data analysis'
  year: '2024'
- authors:
  - Naithani S
  - Preece J
  - D'Eustachio P
  - Gupta P
  - Amarasinghe V
  - Dharmawardhana PD
  - Wu G
  - Fabregat A
  - Elser JL
  - Weiser J
  - Keays M
  - Fuentes AM
  - Petryszak R
  - Stein LD
  - Ware D
  - Jaiswal P
  doi: 10.1093/nar/gkw932
  id: doi:10.1093/nar/gkw932
  journal: Nucleic Acids Research
  title: 'Plant Reactome: a knowledgebase and resource for comparative pathway analysis'
  year: '2017'
- authors:
  - Naithani S
  - Gupta P
  - Preece J
  - D'Eustachio P
  - Elser JL
  - Garg P
  - Dikeman DA
  - Kiff J
  - Cook J
  - Olson A
  - Wei S
  - Tello-Ruiz MK
  - Mundo AF
  - Munoz-Pomer A
  - Mohammed S
  - Cheng T
  - Bolton E
  - Papatheodorou I
  - Stein L
  - Ware D
  - Jaiswal P
  doi: 10.1093/nar/gkz996
  id: doi:10.1093/nar/gkz996
  journal: Nucleic Acids Research
  title: 'Plant Reactome: a knowledgebase and resource for comparative pathway analysis'
  year: '2020'
repository: https://github.com/Gramene/gramene-docs
taxon:
- NCBITaxon:3055
- NCBITaxon:2763
- NCBITaxon:3218
- NCBITaxon:3702
- NCBITaxon:3711
- NCBITaxon:3694
- NCBITaxon:4513
- NCBITaxon:4530
- NCBITaxon:4555
- NCBITaxon:4558
- NCBITaxon:4577
- NCBITaxon:4641
- NCBITaxon:3847
- NCBITaxon:3880
- NCBITaxon:4081
- NCBITaxon:4113
- NCBITaxon:15368
- NCBITaxon:88036
---
# Plant Reactome

## Overview

Plant Reactome is a freely-accessible, open-source pathway knowledgebase developed by the Gramene project. It provides researchers with intuitive bioinformatics tools for visualization, interpretation, and analysis of plant pathway knowledge to support basic research, genome analysis, modeling, systems biology, and education.

The database uses **Oryza sativa** (rice) as the primary reference organism for manual pathway curation, with curated pathways extended via gene-orthology projection to 129 additional plant species, creating a comprehensive resource for comparative plant pathway analysis.

## Data Content and Scale

Plant Reactome houses a comprehensive collection of pathway knowledge across 130 plant species:

### Reference Pathways (Rice)
- **339 Reference Pathways** - Manually curated for rice
- **1,953 Reactions** - Detailed biochemical reactions
- **2,129 Gene Products** - Proteins and gene products
- **1,299 Small Molecules** - Metabolites and chemical entities

### Total Coverage Across All Species
- **Over 34,000 Pathways** - Including orthology-based projections
- **Over 102,000 Reactions** - Across all projected species
- **Over 223,000 Gene Products** - Total unique proteins/genes
- **129 Projected Species** - Beyond the primary reference

### Pathway Categories

The database encompasses a diverse range of biological processes:

- **Metabolic and Transport Pathways** - Energy metabolism, nutrient transport, biosynthesis
- **Hormone Signaling Pathways** - Auxin, gibberellin, ethylene, jasmonate, salicylate signaling
- **Genetic Regulation** - Developmental processes and transcriptional networks
- **Cell Cycle Pathways** - Cell division and cycle control
- **Plant Defense and Stress Response** - Biotic and abiotic stress responses
- **Developmental Processes** - Organ differentiation and morphogenesis
- **Signaling Cascades** - Multi-level regulatory networks

## Species Coverage

Plant Reactome covers diverse plant organisms spanning multiple taxonomic groups:

### Model Organisms
- **Arabidopsis thaliana** (3702) - Well-characterized flowering plant
- **Oryza sativa** (4530) - Rice (primary reference)
- **Zea mays** (4577) - Maize/Corn
- **Hordeum vulgare** (4513) - Barley
- **Sorghum bicolor** (4558) - Sorghum

### Legumes and Pulses
- **Glycine max** (3847) - Soybean
- **Medicago truncatula** (3880) - Medicago

### Fruits and Vegetables
- **Solanum lycopersicum** (4081) - Tomato
- **Solanum tuberosum** (4113) - Potato
- **Musa acuminata** (4641) - Banana

### Trees and Perennials
- **Populus trichocarpa** (3694) - Poplar

### Non-Seed Plants
- **Physcomitrella patens** (3218) - Moss (non-vascular)
- **Selaginella moellendorffii** (88036) - Lycophyte (vascular non-seed)

### Photosynthetic Protists
- **Chlamydomonas reinhardtii** (3055) - Green algae
- **Cyanidioschyzon merolae** (2763) - Red algae

### Additional Species
Additional species coverage extends through orthology-based projections to include relatives of the species listed above, totaling 129 species beyond the primary reference.

## Data Access and Formats

Plant Reactome provides multiple access modes and standardized data formats for integration and analysis:

### Web Interface
- Interactive pathway browser and search functionality
- Pathway visualization tools with subcellular localization
- Comparative pathway views across species
- Expression data integration and analysis
- Embeddable pathway diagram widgets

### REST API
- JSON-formatted responses
- Programmatic access to pathways, reactions, and entities
- Hierarchical querying capabilities

### Data Downloads
- **BioPAX3** - Standard pathway exchange format
- **SBGN** - Systems Biology Graphical Notation for visualizations
- **SVG/PNG** - Pathway diagrams in vector and raster formats
- **CSV** - Identifier mappings and analysis files

### Data Integration
- Gene identifiers linked to Gramene-Ensembl Plants
- Protein cross-references to UniProt
- Small molecule/metabolite references to ChEBI and PubChem

## Key Features

### Pathway Analysis Tools
- **Gene Expression Summary Analysis (GSA)** - Identify differentially expressed pathways
- **Pathway Enrichment Analysis** - Statistical analysis of OMICS data
- **Comparative Pathway Analysis** - Cross-species pathway comparison

### OMICS Data Integration
- Transcriptomics baseline expression visualization
- Support for high-throughput gene expression data analysis
- Proteomics data integration capabilities

### Data Accessibility
- Multiple query modes and search functionality
- Hierarchical pathway organization
- Cross-species navigation and comparison

## Use Cases

Plant Reactome serves diverse research and educational applications:

- **Plant Systems Biology** - Understanding regulatory networks and systems-level biology
- **Functional Genomics** - Annotation and characterization of gene function
- **Genome Analysis** - Integration of genomic data with pathway knowledge
- **Comparative Genomics** - Understanding functional evolution across plant species
- **Agricultural Research** - Crop improvement and trait optimization
- **Environmental Stress Biology** - Plant responses to drought, temperature, pathogens
- **Developmental Biology** - Understanding plant growth and morphogenesis
- **Education** - Teaching plant biology and systems biology concepts

## Citation and Usage

Plant Reactome data is freely available under the Creative Commons Attribution 4.0 International (CC BY 4.0) license. Users are encouraged to cite the appropriate Plant Reactome publication(s) when using data from this resource in research or educational materials.

## Community and Support

Plant Reactome is maintained by the Gramene project and welcomes community feedback on:
- Database content and data quality
- Website functionality and user experience
- Documentation and tutorials
- Feature requests and suggestions

Support and information are available through the Plant Reactome website and the broader Gramene community.
