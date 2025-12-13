---
activity_status: active
category: DataSource
creation_date: '2025-11-25T00:00:00Z'
description: Database of metabolic potential predictions for microbial organisms,
  providing computational inferences about metabolic capabilities based on genomic
  and metagenomic data.
domains:
- microbiology
- systems biology
- genomics
id: metpo
last_modified_date: '2025-11-25T00:00:00Z'
layout: resource_detail
name: MetPo
synonyms:
- MetPo
- Metabolic Potential
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
taxon:
- NCBITaxon:2
---

# MetPo

## Overview

MetPo (Metabolic Potential) is a computational resource that provides predictions of metabolic capabilities for microbial organisms. It integrates genomic and metagenomic data to infer the metabolic potential of microorganisms, including their ability to utilize various substrates, produce specific metabolites, and participate in biogeochemical cycles.

## Key Features

- **Metabolic Predictions**: Computational inference of metabolic pathways and capabilities from sequence data
- **Substrate Utilization**: Predictions of carbon source utilization and nutrient requirements
- **Pathway Completeness**: Assessment of complete vs. incomplete metabolic pathways
- **Functional Annotations**: Links to enzyme classifications and biochemical reactions
- **Taxonomic Coverage**: Predictions across diverse microbial taxa

## Applications

- **Microbial Ecology**: Understanding metabolic roles in microbial communities
- **Metagenomics**: Predicting metabolic functions from environmental sequences
- **Biotechnology**: Identifying organisms for specific metabolic applications
- **Systems Biology**: Integrating metabolic predictions with growth conditions and traits
- **Comparative Genomics**: Analyzing metabolic diversity across microbial lineages

## Methodology

Metabolic potential predictions typically combine:
- Genome or metagenome sequence analysis
- Enzyme and pathway annotation
- Metabolic network reconstruction
- Comparative genomics approaches
- Machine learning models for function prediction

## Integration

MetPo data is integrated into the KG-Microbe knowledge graph framework, connecting metabolic predictions with:
- Microbial taxonomy (NCBITaxon)
- Enzyme classifications (EC numbers)
- Biochemical reactions (Rhea)
- Phenotypic traits (BactoTraits)
- Growth conditions (MediaDive)

For more information about metabolic potential integration in knowledge graphs, see the [KG-Microbe project](https://github.com/Knowledge-Graph-Hub/kg-microbe).
