---
activity_status: active
category: DataSource
creation_date: '2025-11-25T00:00:00Z'
description: MediaDive is the world's largest collection of microbial cultivation
  media, maintained by DSMZ (German Collection of Microorganisms and Cell Cultures).
  It provides comprehensive information about media compositions, solutions, ingredients,
  and growth conditions for over 47,000 microbial strains including bacteria, archaea,
  fungi, protists, and algae.
domains:
- microbiology
- biological systems
- systems biology
id: mediadive
homepage_url: https://mediadive.dsmz.de/
last_modified_date: '2025-11-25T00:00:00Z'
layout: resource_detail
name: MediaDive
synonyms:
- MediaDive
- Media Diversity
- DSMZ MediaDive
contacts:
- category: Organization
  label: DSMZ (Leibniz Institute DSMZ-German Collection of Microorganisms and Cell
    Cultures)
  contact_details:
  - contact_type: url
    value: https://www.dsmz.de/
publications:
- id: https://doi.org/10.1093/nar/gkac803
  title: 'MediaDive: the expert-curated cultivation media database'
  year: '2022'
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
taxon:
- NCBITaxon:2
- NCBITaxon:2157
---

# MediaDive

## Overview

MediaDive is the world's largest expert-curated collection of microbial cultivation media, developed and maintained by DSMZ (Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures) in Germany. As part of the DSMZ Digital Diversity initiative, MediaDive provides comprehensive, standardized information about media compositions, solutions, ingredients, and growth conditions for cultivating diverse microorganisms.

## Database Content

MediaDive contains extensive cultivation data:

- **3,326 Media**: Complete cultivation media recipes with detailed formulations
- **5,839 Solutions**: Stock solutions and preparation instructions
- **1,235 Ingredients**: Individual media components with specifications
- **47,546 Strains**: Microbial strains with associated cultivation protocols

### Organism Coverage

- Bacteria (Gram-positive and Gram-negative)
- Archaea
- Fungi (yeasts and filamentous fungi)
- Protists
- Algae
- Over 40,000 strains with documented cultivation media

## Key Features

### Data Organization

- **Detailed Media Formulations**: Precise ingredient quantities, concentrations, and preparation steps
- **Hierarchical Solutions**: Stock solutions with component breakdowns
- **Ingredient Specifications**: Chemical properties, sources, and preparation methods
- **Preparation Steps**: Sequential instructions for media and solution preparation
- **Gas Atmospheres**: Anaerobic and microaerophilic growth conditions

### Growth Parameters

- Temperature ranges and optima
- pH requirements and adjustments
- Oxygen requirements (aerobic, anaerobic, microaerophilic)
- Pressure conditions
- Light requirements (for phototrophs)
- Incubation times

### Standardized Annotations

- Controlled vocabularies for media components
- Taxonomic classifications (linked to NCBI Taxonomy)
- Isolation source information
- Growth characteristics
- Media types (liquid, solid, semi-solid)

## Search and Discovery Tools

### Search Features

- **Medium Finder**: Search and filter cultivation media by various criteria
- **Solution Finder**: Locate specific stock solutions and preparations
- **Taxonomy Search**: Find media by organism taxonomy
- **Isolation Sources**: Search by environmental origin of strains

### Interactive Tools

- **Medium Builder**: Create custom media formulations from available components
- **Compare Media**: Side-by-side comparison of different media compositions
- **Compare Solutions**: Analyze differences between stock solutions
- **Unit Converter**: Convert between different concentration units
- **SPARQL Endpoint**: Semantic query interface for advanced data access (https://sparql.dsmz.de/mediadive)

### Prediction Tools (Coming Soon)

- Machine learning-based prediction of suitable media for new isolates

## Data Structure and Interoperability

### Semantic Web Integration

- RDF-based data representation
- SPARQL query interface for programmatic access
- Linked data principles for interoperability
- Integration with external taxonomic and chemical databases

### API Access

- RESTful API for programmatic data retrieval
- Comprehensive API documentation available at https://mediadive.dsmz.de/doc/index.html
- Batch queries for large-scale data integration

## Applications

### Research and Development

- **Microbiology Research**: Evidence-based media selection for cultivation experiments
- **Culture Collection Management**: Standardized protocols for strain maintenance
- **Biotechnology**: Optimizing growth conditions for industrial microorganisms
- **Novel Strain Isolation**: Reference media for cultivating previously uncultured organisms

### Comparative and Systems Biology

- **Growth Preference Analysis**: Comparing nutritional requirements across taxa
- **Metabolic Inference**: Linking media composition to metabolic capabilities
- **Ecological Modeling**: Understanding niche requirements from cultivation data
- **Phylogenetic Studies**: Analyzing growth trait evolution

### Education and Training

- Teaching resource for microbiology courses
- Reference for laboratory protocols
- Best practices in microbial cultivation

## Integration with External Resources

### Partner Databases

MediaDive collaborates with international culture collections:
- **JCM** (Japan Collection of Microorganisms)
- **CCAP** (Culture Collection of Algae and Protozoa, UK)
- **NBRC** (NITE Biological Resource Center, Japan)

### Knowledge Graph Integration

MediaDive data is integrated into:
- **KG-Microbe**: Knowledge graph framework connecting media with microbial taxonomy, traits, and functional annotations
- **DSMZ Digital Diversity**: Unified access to all DSMZ biological resources
- Links to chemical ontologies (ChEBI) for ingredient standardization
- Connections to environmental ontologies (ENVO) for isolation source context
- Integration with Gene Ontology (GO) for functional associations

## Publication and Citation

MediaDive is described in:
- **Publication**: "MediaDive: the expert-curated cultivation media database" (2022)
- **DOI**: https://doi.org/10.1093/nar/gkac803
- **Citation**: Available at https://mediadive.dsmz.de/cite

## Access and Documentation

- **Homepage**: https://mediadive.dsmz.de/
- **Documentation**: https://mediadive.dsmz.de/docs/website
- **Medium Builder Guide**: https://mediadive.dsmz.de/docs/medium-builder
- **API Reference**: https://mediadive.dsmz.de/doc/index.html
- **Statistics**: https://mediadive.dsmz.de/stats
- **Contact**: https://mediadive.dsmz.de/contact

## Funding and Support

MediaDive is supported by:
- DSMZ (Leibniz Institute)
- de.NBI (German Network for Bioinformatics Infrastructure)

For more information about how MediaDive data is used in knowledge graph construction, see the [KG-Microbe project](https://github.com/Knowledge-Graph-Hub/kg-microbe).
