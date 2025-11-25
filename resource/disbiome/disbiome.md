---
activity_status: active
category: Database
creation_date: '2025-11-25T00:00:00Z'
description: Database of microbiome-disease associations, cataloging relationships between microbial taxa and human diseases based on experimental and clinical evidence.
domains:
- microbiology
- biomedical
- clinical
- health
id: disbiome
homepage_url: https://disbiome.ugent.be/
last_modified_date: '2025-11-25T00:00:00Z'
layout: resource_detail
name: Disbiome
synonyms:
- Disbiome
- Disbiome Database
products:
- category: GraphProduct
  compression: targz
  description: Raw source files for all KG-Microbe framework transforms (all 4 KGs)
  format: kgx
  id: kg-microbe.graph.raw
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: KG-Microbe KGX Graph - Raw
  original_source:
  - envo
  - ncbitaxon
  - chebi
  - go
  - mondo
  - hp
  - bacdive
  - mediadive
  - uniprot
  - rhea
  - ec
  - bactotraits
  - ctd
  - disbiome
  - metpo
  product_file_size: 12464495186
  product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-raw-20250222.tar.gz
  secondary_source:
  - kg-microbe
- category: GraphProduct
  compression: targz
  description: The core KG KG-Microbe-Core with ontologies, organismal traits, and
    growth preferences.
  format: kgx
  id: kg-microbe.graph.core
  name: KG-Microbe KGX Graph - Core
  original_source:
  - envo
  - ncbitaxon
  - chebi
  - go
  - mondo
  - hp
  - bacdive
  - mediadive
  - uniprot
  - rhea
  - ec
  - bactotraits
  - ctd
  - disbiome
  - metpo
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
  secondary_source:
  - kg-microbe
- category: GraphProduct
  compression: targz
  description: Core plus human biomedical data (ontologies, CTD, Wallen et al)
  format: kgx
  id: kg-microbe.graph.biomedical
  name: KG-Microbe KGX Graph - Biomedical
  original_source:
  - envo
  - ncbitaxon
  - chebi
  - go
  - mondo
  - hp
  - bacdive
  - mediadive
  - uniprot
  - rhea
  - ec
  - bactotraits
  - ctd
  - disbiome
  - metpo
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
  secondary_source:
  - kg-microbe
- category: GraphProduct
  compression: targz
  description: Core plus Uniprot genome annotations
  format: kgx
  id: kg-microbe.graph.function
  name: KG-Microbe KGX Graph - Function
  original_source:
  - envo
  - ncbitaxon
  - chebi
  - go
  - mondo
  - hp
  - bacdive
  - mediadive
  - uniprot
  - rhea
  - ec
  - bactotraits
  - ctd
  - disbiome
  - metpo
  product_file_size: 4623010863
  product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-function-20250222.tar.gz
  secondary_source:
  - kg-microbe
- category: GraphProduct
  compression: targz
  description: Biomedical plus Uniprot genome annotations
  format: kgx
  id: kg-microbe.graph.biomedical-function
  name: KG-Microbe KGX Graph - Biomedical-Function
  original_source:
  - envo
  - ncbitaxon
  - chebi
  - go
  - mondo
  - hp
  - bacdive
  - mediadive
  - uniprot
  - rhea
  - ec
  - bactotraits
  - ctd
  - disbiome
  - metpo
  product_file_size: 4640682152
  product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-biomedical-function-20250222.tar.gz
  secondary_source:
  - kg-microbe
warnings:
- This is an automatically generated stub page. Please replace with accurate information
  about this resource.
---
# Disbiome

## Overview

Disbiome is a comprehensive database that catalogs associations between human microbiome composition and diseases. It integrates experimental and clinical evidence linking specific microbial taxa to various disease states, providing a resource for understanding the role of microbiota in human health and disease.

## Key Features

- **Disease-Microbe Associations**: Curated relationships between microbial taxa and human diseases
- **Evidence-Based Annotations**: Links to supporting literature and experimental data
- **Taxonomic Coverage**: Associations at multiple taxonomic levels (phylum to species)
- **Disease Categories**: Coverage of diverse disease types including metabolic, inflammatory, infectious, and neurological disorders
- **Effect Direction**: Annotation of increased or decreased abundance in disease states
- **Body Site Information**: Specification of relevant body sites or microbiome niches

## Applications

- **Disease Research**: Understanding microbial contributions to disease etiology
- **Biomarker Discovery**: Identifying microbial signatures for disease diagnosis or prognosis
- **Therapeutic Development**: Targeting microbiome modulation for treatment strategies
- **Microbiome Studies**: Hypothesis generation for microbiome-disease research
- **Systems Medicine**: Integrating microbiome data with other biomedical knowledge

## Data Content

Disbiome includes associations for:
- Gastrointestinal diseases (IBD, IBS, colorectal cancer)
- Metabolic disorders (obesity, diabetes, NAFLD)
- Neurological conditions (autism, depression, Alzheimer's)
- Infectious diseases
- Autoimmune conditions
- Respiratory diseases
- Dermatological conditions

## Integration

Disbiome data is integrated into:
- KG-Microbe knowledge graph (linking microbiome with human health)
- Disease ontologies (Mondo, Human Phenotype Ontology)
- Microbial taxonomy databases (NCBITaxon)
- Comparative Toxicogenomics Database (CTD)

## Access

Disbiome is accessible through:
- Web interface: https://disbiome.ugent.be/
- Downloadable datasets
- Integration in knowledge graph frameworks

For more information about Disbiome integration in knowledge graphs, see the [KG-Microbe project](https://github.com/Knowledge-Graph-Hub/kg-microbe).