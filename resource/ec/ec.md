---
activity_status: active
category: Ontology
creation_date: '2025-11-25T00:00:00Z'
description: The Enzyme Commission classification system provides a hierarchical numbering scheme for enzymes based on the chemical reactions they catalyze, maintained by the IUBMB.
domains:
  - systems biology
id: "ec"
homepage_url: https://www.enzyme-database.org/
last_modified_date: '2025-11-25T00:00:00Z'
layout: resource_detail
name: Enzyme Commission
synonyms:
  - EC
  - EC Numbers
  - Enzyme Commission Numbers
  - IUBMB Enzyme Nomenclature
products:
  - category: GraphProduct
    compression: targz
    description: Raw source files for all KG-Microbe framework transforms (all 4 KGs)
    format: kgx
    id: "kg-microbe.graph.raw"
    license:
      id: "https://creativecommons.org/publicdomain/zero/1.0/"
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
    description: The core KG KG-Microbe-Core with ontologies, organismal traits, and growth preferences.
    format: kgx
    id: "kg-microbe.graph.core"
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
    id: "kg-microbe.graph.biomedical"
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
    id: "kg-microbe.graph.function"
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
    id: "kg-microbe.graph.biomedical-function"
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
  - This is an automatically generated stub page. Please replace with accurate information about this resource.
---

# Enzyme Commission

## Overview

The Enzyme Commission (EC) classification system is a hierarchical numerical classification scheme for enzymes based on the chemical reactions they catalyze. Maintained by the International Union of Biochemistry and Molecular Biology (IUBMB), EC numbers provide a standardized nomenclature used universally in biochemistry and molecular biology.

## Classification Structure

EC numbers consist of four hierarchical levels:
1. **First digit**: Main enzyme class (1-7)
   - EC 1: Oxidoreductases
   - EC 2: Transferases
   - EC 3: Hydrolases
   - EC 4: Lyases
   - EC 5: Isomerases
   - EC 6: Ligases
   - EC 7: Translocases
2. **Second digit**: Subclass (type of substrate or chemical group)
3. **Third digit**: Sub-subclass (further specificity)
4. **Fourth digit**: Serial number (specific enzyme)

Example: EC 3.2.1.1 represents α-amylase (a hydrolase acting on glycosidic bonds)

## Key Features

- **Hierarchical Classification**: Organized by reaction type and substrate specificity
- **Universal Standard**: Widely adopted across biological databases and publications
- **Systematic Naming**: Each enzyme receives a unique EC number and systematic name
- **Reaction Specificity**: Classification based on catalyzed reaction, not protein structure
- **Regular Updates**: Continuously maintained with new enzyme discoveries

## Applications

- **Functional Annotation**: Classifying gene products by enzymatic function
- **Metabolic Pathway Analysis**: Mapping enzymes to biochemical pathways
- **Comparative Genomics**: Analyzing enzyme distributions across organisms
- **Drug Discovery**: Identifying enzyme targets for therapeutic intervention
- **Systems Biology**: Integrating enzymatic functions in metabolic models

## Integration

EC classifications are integrated into numerous biological databases including:
- UniProt (protein functional annotations)
- KEGG (metabolic pathway mapping)
- BRENDA (enzyme information)
- Rhea (biochemical reactions)
- KG-Microbe (microbial functional genomics)

## Data Access

EC numbers and enzyme information are freely available through:
- IUBMB Enzyme Nomenclature Committee: https://www.enzyme-database.org/
- ExPASy Enzyme Database: https://enzyme.expasy.org/
- BRENDA Enzyme Database: https://www.brenda-enzymes.org/

For more information about how EC classifications are used in knowledge graphs, see the [KG-Microbe project](https://github.com/Knowledge-Graph-Hub/kg-microbe).
