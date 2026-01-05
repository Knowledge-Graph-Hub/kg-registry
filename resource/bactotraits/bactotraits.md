---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://www.univ-lorraine.fr/"
    id: univ-lorraine
    label: Université de Lorraine
creation_date: '2025-11-25T00:00:00Z'
description: A comprehensive database of bacterial phenotypic traits including morphology,
  physiology, ecology, and growth characteristics for thousands of bacterial species.
  BactoTraits provides standardized trait annotations for comparative microbiology
  and systems biology applications.
domains:
- microbiology
- biological systems
- systems biology
homepage_url: https://ordar.otelo.univ-lorraine.fr/record?id=10.24396/ORDAR-53
id: bactotraits
last_modified_date: '2026-01-05T00:00:00Z'
layout: resource_detail
license:
  id: "https://creativecommons.org/licenses/by/4.0/"
  label: CC BY 4.0
name: BactoTraits
synonyms:
- BactoTraits
- Bacterial Traits Database
products:
- category: Product
  description: BactoTraits database with downloadable trait datasets
  format: http
  id: bactotraits.database
  is_public: true
  name: BactoTraits Database and Downloads
  product_url: https://ordar.otelo.univ-lorraine.fr/record?id=10.24396/ORDAR-53
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
taxon:
- NCBITaxon:2
---

# BactoTraits

## Overview

BactoTraits is a comprehensive database that catalogs phenotypic traits of bacterial species. It provides standardized information about bacterial morphology, physiology, ecology, metabolism, and growth characteristics, enabling comparative analyses across thousands of bacterial taxa.

## Key Features

- **Comprehensive Trait Coverage**: Morphological, physiological, metabolic, and ecological characteristics
- **Standardized Annotations**: Controlled vocabularies and ontology terms for trait descriptions
- **Taxonomic Breadth**: Coverage of diverse bacterial phyla and species
- **Growth Parameters**: Temperature ranges, pH preferences, oxygen requirements, salinity tolerance
- **Morphological Data**: Cell shape, size, arrangement, motility, and structural features
- **Metabolic Capabilities**: Substrate utilization, fermentation products, enzymatic activities
- **Ecological Context**: Habitat preferences, pathogenicity, biogeographic distribution

## Trait Categories

### Morphological Traits
- Cell shape (cocci, bacilli, spirilla, etc.)
- Cell size and dimensions
- Gram staining properties
- Spore formation
- Flagella and motility
- Capsule formation

### Physiological Traits
- Temperature optima and ranges (psychrophile, mesophile, thermophile)
- pH preferences (acidophile, neutrophile, alkaliphile)
- Oxygen requirements (aerobe, anaerobe, facultative)
- Salinity tolerance (halophile, halotolerant)
- Pressure tolerance (barophile)

### Metabolic Traits
- Carbon source utilization
- Nitrogen fixation capability
- Fermentation types
- Respiration modes
- Photosynthesis capability

### Ecological Traits
- Habitat types (soil, aquatic, host-associated)
- Pathogenicity and virulence
- Symbiotic relationships
- Biogeochemical cycling roles

## Applications

- **Comparative Microbiology**: Analyzing trait evolution and diversity across bacterial lineages
- **Ecological Modeling**: Predicting microbial distributions and community composition
- **Biotechnology**: Identifying bacteria with desired traits for industrial applications
- **Systems Biology**: Integrating phenotypes with genomic and metabolic data
- **Machine Learning**: Training models for trait prediction from genomic data
- **Microbiome Research**: Understanding functional diversity in microbial communities

## Data Sources

BactoTraits integrates information from:
- Bergey's Manual of Systematic Bacteriology
- Scientific literature
- Culture collection databases
- BacDive (Bacterial Diversity Metadatabase)
- Experimental studies

## Integration

BactoTraits data is integrated into:
- KG-Microbe knowledge graph (linking traits with taxonomy, metabolism, and ecology)
- NCBITaxon (taxonomic classifications)
- Environmental ontologies (ENVO)
- Gene Ontology (GO)

For more information about BactoTraits integration in knowledge graphs, see the [KG-Microbe project](https://github.com/Knowledge-Graph-Hub/kg-microbe).
