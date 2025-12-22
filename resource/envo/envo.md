---
activity_status: active
category: Ontology
collection:
  - obo-foundry
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: pier.buttigieg@awi.de
      - contact_type: github
        value: pbuttigieg
    label: Pier Luigi Buttigieg
    orcid: 0000-0002-4366-3088
description: ENVO is a domain ontology for the standardized representation and interoperability of environmental systems, components, and processes across multiple scales. A community-driven, OWL-based ontology with over 6,000 terms covering environments from microscopic to planetary scales, supporting FAIR data practices and semantic interoperability across diverse research domains including microbiology, ecology, genomics, and environmental health research.
creation_date: '2025-06-10T00:00:00Z'
last_modified_date: '2025-12-20T00:00:00Z'
domains:
  - environment
homepage_url: http://environmentontology.org/
id: envo
layout: resource_detail
license:
  id: http://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png
name: Environment Ontology
products:
  - category: OntologyProduct
    description: main ENVO OWL release
    format: owl
    id: envo.owl
    name: main ENVO OWL release
    product_file_size: 819909
    product_url: http://purl.obolibrary.org/obo/envo.owl
  - category: OntologyProduct
    description: ENVO in obographs JSON format
    format: json
    id: envo.json
    name: ENVO in obographs JSON format
    product_file_size: 653600
    product_url: http://purl.obolibrary.org/obo/envo.json
  - category: OntologyProduct
    description: ENVO in OBO Format. May be lossy
    format: obo
    id: envo.obo
    name: ENVO in OBO Format. May be lossy
    product_file_size: 595276
    product_url: http://purl.obolibrary.org/obo/envo.obo
  - category: OntologyProduct
    description: OBO-Basic edition of ENVO
    format: obo
    id: envo.subsets.envo-basic.obo
    name: OBO-Basic edition of ENVO
    product_file_size: 422465
    product_url: http://purl.obolibrary.org/obo/envo/subsets/envo-basic.obo
  - category: OntologyProduct
    description: Earth Microbiome Project subset
    format: owl
    id: envo.subsets.envoEmpo.owl
    name: Earth Microbiome Project subset
    product_file_size: 19016
    product_url: http://purl.obolibrary.org/obo/envo/subsets/envoEmpo.owl
  - category: OntologyProduct
    description: GSC Lite subset of ENVO
    format: obo
    id: envo.subsets.EnvO-Lite-GSC.obo
    name: GSC Lite subset of ENVO
    product_file_size: 12912
    product_url: http://purl.obolibrary.org/obo/envo/subsets/EnvO-Lite-GSC.obo
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
    description: The core KG KG-Microbe-Core with ontologies, organismal traits, and growth preferences.
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
repository: https://github.com/EnvironmentOntology/envo
---

## Overview

ENVO (Environment Ontology) is a community-driven domain ontology that provides a standardized vocabulary for describing environmental systems, components, and processes. Designed to promote semantic interoperability and support FAIR (Findable, Accessible, Interoperable, Reusable) data practices, ENVO enables diverse research communities to describe environmental entities using consistent, controlled terminology across multiple scales—from microscopic (cellular environments) to planetary scales (global biomes).

The ontology plays a critical role in bridging disciplinary gaps, allowing researchers in microbiology, ecology, environmental health, genomics, and related fields to integrate and reason over heterogeneous environmental data through shared semantic understanding.

## Scope and Coverage

### Scales and Domains

ENVO covers environmental entities and processes across multiple orders of magnitude:
- **Microscopic environments**: Cellular and microbial habitats
- **Organismal scale**: Host organisms and their associated environmental niches
- **Ecosystem scale**: Communities, habitats, and biomes
- **Regional scale**: Geographical and geopolitical entities
- **Global scale**: Planetary systems and global biomes

### Core Concepts

ENVO represents:
- **Environmental systems**: Distinct environmental units (e.g., soil, ocean, atmosphere, host organisms)
- **Environmental components**: Physical, chemical, and biological entities found in environments (e.g., minerals, chemical compounds, organisms)
- **Environmental processes**: Biological, chemical, and physical processes occurring in environments (e.g., decomposition, photosynthesis, weather systems)
- **Environmental properties**: Measurable characteristics of environments (e.g., temperature, pH, salinity)

### Disciplinary Applications

- **Microbiology & Microbial Ecology**: Describing microbial habitats and niches
- **Environmental Health**: Linking environmental exposures to health outcomes
- **Metagenomics & Genomics**: Contextualizing genomic samples with environmental metadata
- **Ecology & Conservation**: Characterizing natural and managed ecosystems
- **Environmental Science**: Standardizing environmental observations and monitoring
- **Oceanography & Limnology**: Aquatic environment description
- **Soil Science**: Soil environment characterization

## Technical Development

### Ontology Language and Structure

- **Primary Format**: Web Ontology Language (OWL 2)
- **Reasoning Support**: Full semantic reasoning capabilities
- **Class-Based Architecture**: Hierarchical class organization with multiple inheritance
- **Templating Methodology**: Accelerated class creation using systematic templates for consistency

### Community Development Model

- **Community-Driven**: Maintained through community contributions and collaboration
- **OBO Foundry Member**: Recognized as a top-tier OBO ontology with stringent quality standards
- **Version Control**: Active development on GitHub with transparent versioning
- **Regular Releases**: Periodic updates maintaining stability and adding new terminology
- **Cross-Ontology Coordination**: Integration with other OBO ontologies for semantic consistency

## Data Access and Products

### Download Formats

ENVO is available in multiple standard formats to support diverse use cases:

1. **Main OWL Release** - Complete Web Ontology Language format
   - Includes all ENVO classes and properties
   - Imported classes from referenced ontologies
   - Full reasoning capabilities
   - Format: OWL 2

2. **OBO Format Release** - Legacy OBO-style format
   - Standard format for biological ontologies
   - May lose some OWL expressiveness in conversion
   - Supports legacy tools and systems

3. **JSON Obographs Format** - Modern JSON serialization
   - Programmatic access and web applications
   - Machine-readable graph structure
   - Compatible with graph visualization tools

4. **Subset Versions** - Trimmed ontologies for specific use cases:
   - **ENVO-Basic**: OBO Basic subset for users needing core environmental terms
   - **ENVO-Lite-GSC**: Genomics Standards Consortium lite version optimized for metagenomic studies
   - **EnvO-EMPO**: Earth Microbiome Project subset tailored for microbiome research

### Access Methods

- **OBO Foundry Repository**: Stable URLs via `purl.obolibrary.org`
- **GitHub Repository**: Source code and development versions
- **BioPortal**: Browser and web services API
- **Ontobee**: Web interface for exploring classes and relationships
- **Bioregistry**: Machine-readable registry with standard identifiers

## Integration and Interoperability

### Standards Compliance

- **W3C Standards**: RDF, OWL, SPARQL compatibility
- **OBO Standards**: Adherence to OBO Foundry principles
- **Semantic Web**: Linked Data principles and URI-based identification
- **FAIR Principles**: Designed to support FAIR data practices

### Cross-Ontology Integration

ENVO integrates with numerous OBO ontologies:
- **Gene Ontology (GO)**: Linking biological processes to environmental contexts
- **CHEBI**: Chemical entities and compounds in environments
- **UBERON**: Organismal anatomy for host-associated environments
- **Mondo**: Disease relationships with environmental factors
- **NCBITaxon**: Organism classification within environments
- **PATO**: Phenotypes and properties in environmental contexts

### Collaborative Partnerships

- **ESIP Federation**: Earth Science Information Partners for standardization
- **UN Environment Programme**: Supporting global environmental monitoring
- **IOC-UNESCO**: Ocean Commission collaboration for marine environment standards
- **International Metagenomics and Microbiomes Association**: Microbiome research standardization

## Leadership and Community

### Primary Contact

**Pier Luigi Buttigieg** (pbuttigieg@awi.de)
- Lead ontologist and primary curator
- ORCID: [0000-0002-4366-3088](https://orcid.org/0000-0002-4366-3088)
- Affiliation: Alfred Wegener Institute

### Host Institution

- **OBO Foundry**: Recognized member ontology
- **GitHub Organization**: EnvironmentOntology
- **Community Contributors**: Open contribution model with community review

## Use Cases and Applications

### Research Applications

- **Metagenomic Studies**: Contextualizing genomic sequences with standardized environmental metadata
- **Microbiome Research**: Describing host-associated and environmental microbiota habitats
- **Environmental Health Research**: Linking exposures and outcomes through standardized environmental terminology
- **Ecological Surveys**: Consistent description of habitats and ecosystems across studies
- **Climate and Environmental Monitoring**: Standardized reporting of environmental observations
- **Hypothesis Generation**: Discovering environmental factors associated with biological phenomena

### Data Integration

- **Sample Metadata**: Standardizing environmental context in genomic data repositories
- **Ecosystem Databases**: Organizing and querying environmental monitoring data
- **Multi-Study Analyses**: Enabling meta-analysis through consistent terminology
- **Ontology-Based Annotation**: Enriching research data with semantic environmental context

### Downstream Tools and Systems

ENVO is integrated into:
- **KG-Microbe**: Microbiome knowledge graphs using ENVO for environmental contextualization
- **Metagenomics Analysis Pipelines**: Environmental metadata standardization
- **Genomic Sequence Archives**: Sample annotation with ENVO terms
- **Bioinformatics Workflows**: Environmental factor integration in analysis pipelines

## Standards Compliance and Interoperability

- **OBO Foundry Standards**: Member ontology meeting strict quality requirements
- **Semantic Web Standards**: Full RDF/OWL/SPARQL compliance
- **FAIR Data Principles**: Machine-readable, accessible, and interoperable
- **Open Access**: CC0 public domain licensing
- **Version Control**: Transparent development history and provenance

## Citation and Usage

ENVO data and ontology files are freely available under CC0 (public domain) licensing, allowing unrestricted use for any purpose.

### Recommended Citations

For ENVO general use:
"ENVO (Environment Ontology). Available at: http://environmentontology.org/"

For research using ENVO:
"Buttigieg PL, et al. The environment ontology: contextualising biological and biomedical entities. Journal of Biomedical Semantics. 2013;4:43. https://doi.org/10.1186/2041-1480-4-43"

For recent updates:
"Buttigieg PL, et al. The environment ontology in 2016: bridging domains with increased scope, semantic density, and interoperation. Journal of Biomedical Semantics. 2016;7:57. https://doi.org/10.1186/s13326-016-0097-6"

### Key Resources

- **Website**: http://environmentontology.org/
- **GitHub Repository**: https://github.com/EnvironmentOntology/envo
- **OBO Foundry Page**: http://obofoundry.org/ontology/envo.html
- **BioPortal**: https://bioportal.bioontology.org/ontologies/ENVO
- **Ontobee Browser**: https://ontobee.org/ontology/ENVO
- **Bioregistry**: https://bioregistry.io/envo

## Contacts

- **Pier Luigi Buttigieg** (pier.buttigieg@awi.de) [ORCID: 0000-0002-4366-3088](https://orcid.org/0000-0002-4366-3088)

## Products

### main ENVO OWL release

main ENVO OWL release

**URL**: [http://purl.obolibrary.org/obo/envo.owl](http://purl.obolibrary.org/obo/envo.owl)

**Format**: owl

### ENVO in obographs JSON format

ENVO in obographs JSON format

**URL**: [http://purl.obolibrary.org/obo/envo.json](http://purl.obolibrary.org/obo/envo.json)

**Format**: json

### ENVO in OBO Format. May be lossy

ENVO in OBO Format. May be lossy

**URL**: [http://purl.obolibrary.org/obo/envo.obo](http://purl.obolibrary.org/obo/envo.obo)

**Format**: obo

### OBO-Basic edition of ENVO

OBO-Basic edition of ENVO

**URL**: [http://purl.obolibrary.org/obo/envo/subsets/envo-basic.obo](http://purl.obolibrary.org/obo/envo/subsets/envo-basic.obo)

**Format**: obo

### Earth Microbiome Project subset

Earth Microbiome Project subset

**URL**: [http://purl.obolibrary.org/obo/envo/subsets/envoEmpo.owl](http://purl.obolibrary.org/obo/envo/subsets/envoEmpo.owl)

**Format**: owl

### GSC Lite subset of ENVO

GSC Lite subset of ENVO

**URL**: [http://purl.obolibrary.org/obo/envo/subsets/EnvO-Lite-GSC.obo](http://purl.obolibrary.org/obo/envo/subsets/EnvO-Lite-GSC.obo)

**Format**: obo

## Publications

- [The environment ontology: contextualising biological and biomedical entities](https://doi.org/10.1186/2041-1480-4-43)
- [The environment ontology in 2016: bridging domains with increased scope, semantic density, and interoperation](https://doi.org/10.1186/s13326-016-0097-6)

**Domains**: environment

---

*This resource was automatically synchronized from the OBO Foundry registry.*
