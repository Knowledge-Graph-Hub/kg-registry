---
activity_status: active
category: DataSource
collection:
- ber
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.dsmz.de/
  label: DSMZ (Leibniz Institute DSMZ-German Collection of Microorganisms and Cell
    Cultures)
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
homepage_url: https://mediadive.dsmz.de/
id: mediadive
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: MediaDive
products:
- category: GraphicalInterface
  description: MediaDive web portal for browsing, searching, comparing, and building
    microbial cultivation media recipes.
  format: http
  id: mediadive.portal
  name: MediaDive Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mediadive
  product_url: https://mediadive.dsmz.de/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: bacdive
  - relation_type: prov:used
    source: chebi
  - relation_type: prov:used
    source: ncbitaxon
- category: ProgrammingInterface
  description: MediaDive REST API documentation for programmatic retrieval of media,
    solutions, ingredients, strains, and related records.
  format: http
  id: mediadive.rest_api
  name: MediaDive REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mediadive
  product_url: https://mediadive.dsmz.de/doc/index.html
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: bacdive
  - relation_type: prov:used
    source: chebi
  - relation_type: prov:used
    source: ncbitaxon
- category: ProgrammingInterface
  description: MediaDive SPARQL endpoint for querying the DSMZ Digital Diversity RDF
    representation of MediaDive data.
  format: http
  id: mediadive.sparql
  name: MediaDive SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mediadive
  product_url: https://sparql.dsmz.de/mediadive
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: bacdive
  - relation_type: prov:used
    source: chebi
  - relation_type: prov:used
    source: ncbitaxon
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
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
- category: GraphProduct
  compression: targz
  description: The core KG KG-Microbe-Core with ontologies, organismal traits, and
    growth preferences.
  format: kgx
  id: kg-microbe.graph.core
  name: KG-Microbe KGX Graph - Core
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
- category: GraphProduct
  compression: targz
  description: Core plus human biomedical data (ontologies, CTD, Wallen et al)
  format: kgx
  id: kg-microbe.graph.biomedical
  name: KG-Microbe KGX Graph - Biomedical
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
- category: GraphProduct
  compression: targz
  description: Core plus Uniprot genome annotations
  format: kgx
  id: kg-microbe.graph.function
  name: KG-Microbe KGX Graph - Function
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
- category: GraphProduct
  compression: targz
  description: Biomedical plus Uniprot genome annotations
  format: kgx
  id: kg-microbe.graph.biomedical-function
  name: KG-Microbe KGX Graph - Biomedical-Function
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_file_size: 4640682152
  product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-biomedical-function-20250222.tar.gz
publications:
- authors:
  - Julia Koblitz
  - Philipp Halama
  - Stefan Spring
  - Vera Thiel
  - Christiane Baschien
  - Richard L. Hahnke
  - Michael Pester
  - Joerg Overmann
  - Lorenz Christian Reimer
  doi: 10.1093/nar/gkac803
  id: doi:10.1093/nar/gkac803
  journal: Nucleic Acids Research
  preferred: true
  title: 'MediaDive: the expert-curated cultivation media database'
  year: '2023'
synonyms:
- MediaDive
- Media Diversity
- DSMZ MediaDive
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