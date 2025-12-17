---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://openbiodiv.net/"
    id: "pensoft"
    label: Pensoft Publishers
creation_date: '2025-12-17T00:00:00Z'
description: OpenBiodiv is an open-access biodiversity knowledge graph that extracts, integrates, and provides semantic access to linked open biodiversity data from scientific literature and established taxonomic backbones. It converts narrative biodiversity information into computable semantic form and maintains a comprehensive knowledge management system for biodiversity science.
domains:
  - literature
homepage_url: https://openbiodiv.net/
id: "openbiodiv"
infores_id: "openbiodiv"
layout: resource_detail
license:
  id: "https://creativecommons.org/licenses/by/4.0/"
  label: CC BY 4.0
name: OpenBiodiv
products:
  - category: GraphicalInterface
    description: Interactive web portal for searching, exploring, and discovering biodiversity knowledge graph data including taxonomic treatments, species descriptions, and literature-extracted information
    format: http
    id: "openbiodiv.portal"
    is_public: true
    name: OpenBiodiv Web Portal
    product_url: https://openbiodiv.net/
  - category: ProgrammingInterface
    description: SPARQL endpoint for complex semantic queries across the biodiversity knowledge graph, enabling advanced queries combining taxonomic, literature, specimen, and ecological data
    format: http
    id: "openbiodiv.sparql"
    is_public: true
    name: OpenBiodiv SPARQL Endpoint
    product_url: "http://graph.openbiodiv.net/"
  - category: ProgrammingInterface
    description: RESTful API for programmatic access to OpenBiodiv biodiversity data with Swagger API documentation for easy integration
    format: http
    id: "openbiodiv.api"
    is_public: true
    name: OpenBiodiv REST API
    product_url: "https://graph.openbiodiv.net/webapi"
  - category: OntologyProduct
    description: OpenBioDiv-O, the OpenBiodiv Ontology
    id: "openbiodiv.ontology.ttl"
    is_public: true
    format: ttl
    name: OpenBioDiv-O
    product_url: "https://raw.githubusercontent.com/pensoft/OpenBiodiv/refs/heads/master/ontology/openbiodiv-ontology-latest.ttl"
    original_source:
    - skos
    - proton
    - fabio
    - doco
    - openbiodiv
    secondary_source:
    - openbiodiv
  - category: DocumentationProduct
    description: Guide to OpenBioDiv-O, the OpenBiodiv Ontology
    id: "openbiodiv.ontology.guide"
    is_public: true
    format: http
    name: OpenBioDiv-O Guide
    product_url: "https://openbiodiv.net/ontologies"
publications:
  - authors:
      - Penev L
      - Dimitrova M
      - Senderov V
      - Zhelezov G
      - Georgiev T
      - Stoev P
      - Simov K
    doi: "10.3390/publications7020038"
    id: "doi:10.3390/publications7020038"
    journal: Publications
    preferred: true
    title: "OpenBiodiv: A Knowledge Graph for Literature-Extracted Linked Open Data in Biodiversity Science"
    year: "2019"
  - authors:
      - Senderov V
      - Simov K
      - Georgiev T
      - Stoev P
      - Penev L
    doi: "10.1186/s13326-017-0174-5"
    id: "doi:10.1186/s13326-017-0174-5"
    journal: Journal of Biomedical Semantics
    title: "OpenBiodiv-O: ontology of the OpenBiodiv knowledge management system"
    year: "2018"
repository: https://github.com/pensoft/OpenBiodiv
taxon:
  - NCBITaxon:1
---

# OpenBiodiv

## Overview

OpenBiodiv is an Open Access Biodiversity Knowledge Management System (OBKMS) that creates and maintains a comprehensive biodiversity knowledge graph. It combines information extracted from scientific literature with established taxonomic backbones to create a semantic, linked-data repository of biodiversity knowledge.

The system transforms narrative biodiversity information from scholarly publications into computable semantic form, effectively "lifting" biodiversity knowledge into Linked Open Data (LOD) and making previously inaccessible information discoverable and machine-readable.

## Data Content and Coverage

### Scale and Scope

As of the latest updates, OpenBiodiv contains:
- **24,939 articles** - Scholarly publications analyzed for biodiversity information
- **167,471 treatments** - Taxonomic treatments and species descriptions
- **130,359 authors** - Contributing researchers and publication authors
- **736,809 taxon names** - Scientific names indexed and semantically linked
- **129,257 sequences** - Genetic and molecular sequences with taxonomic linkage
- **1,390 institutions and collections** - Museums and research institutions
- **117,854 figures** - Scientific illustrations and diagrams from publications
- **18,585 tables** - Research data tables extracted from literature
- **90,008 material examined sections** - Specimen and type material records

### Data Types and Coverage

**Primary Data Sources:**
- Pensoft-published articles (>5,000 biodiversity papers)
- Plazi TreatmentBank (taxonomic treatments)
- GBIF Backbone Taxonomy (established taxonomic frameworks)
- Biodiversity Literature Repository (Zenodo-hosted content)

**Content Categories:**
- Taxonomic treatments and species descriptions
- Scientific nomenclature and naming relationships
- Author and institutional information
- Specimen and type material data
- DNA and genetic sequences with taxonomic context
- Ecological data and species interactions
- Biogeographical distribution information
- Material examined sections from taxonomic literature
- Scientific figures and illustrations
- Research data tables

**Taxonomic Coverage:**
OpenBiodiv covers all kingdoms of life with particular strength in:
- **Insects** - Especially the "Big 4" insect orders (Coleoptera, Lepidoptera, Hymenoptera, Diptera)
- **Plants** - Extensive plant taxonomy coverage
- **Fungi** - Fungal taxonomy and ecology
- **Invertebrates** - Comprehensive non-insect invertebrate coverage
- **Vertebrates** - Vertebrate species and taxonomy

## Data Access and Formats

### Access Methods

**1. Web Portal**
- Interactive interface for searching and exploring biodiversity data
- User-friendly discovery of taxonomic treatments and species information
- Full-text search capabilities

**2. SPARQL Endpoint**
- Endpoint: http://graph.openbiodiv.net/
- Enable complex semantic queries across multiple data types
- Query combinations of literature, taxonomy, specimens, and sequences
- Adheres to W3C SPARQL standards

**3. REST API**
- Endpoint: https://graph.openbiodiv.net/webapi
- RESTful interface for programmatic access
- Swagger documentation for API methods
- Simple queries and data retrieval
- Integration with external systems and workflows

### Data Format

All data is maintained and distributed in **RDF (Resource Description Framework)** format, adhering to Linked Open Data (LOD) principles and stored in Ontotext GraphDB. Output formats include:
- RDF/XML
- RDF Linked Open Data format
- Query results through SPARQL
- JSON (via REST API)

### Data Updates

- Database is updated and indexed daily
- Apache Kafka event-streaming platform enables continuous workflow automation
- Ongoing integration of new content from source publishers
- Real-time incorporation of new taxonomic treatments and literature

## Key Features

### Semantic Integration

- Automatic entity linking and discovery across data sources
- Connection of taxon names to publication sections and context
- Linking of specimens to institutions and collectors
- Association of authors with their publications and taxonomic work
- Relationship extraction from natural language text

### Query Capabilities

- Complex queries spanning literature, taxonomy, specimens, and sequences
- Example: "Which taxa treatments mention both species X and species Y?"
- Example: "Find all specimens of species X from institution Y"
- Example: "Discover all ecological interactions mentioned for a given taxon"
- Advanced SPARQL queries for custom analyses

### Standards Compliance

- Full compliance with Linked Open Data principles
- Integration with Global Biodiversity Information Facility (GBIF)
- Compatible with Darwin Core standards and DarwinCore-based ontologies
- Support for SPAR Ontologies in scholarly publishing
- Connection to ENVO (Environment Ontology) for ecological data
- Integration with NOMEN ontology for nomenclature

## Use Cases and Applications

- **Taxonomic Research** - Discovering all published species descriptions for a taxon
- **Specimen Management** - Finding and linking type materials and specimen records
- **Literature Mining** - Extracting structured biodiversity information from publications
- **Cross-database Research** - Integrating data across literature, taxonomy, and specimens
- **Evolutionary Studies** - Connecting sequence data to taxonomic descriptions
- **Biogeographical Analysis** - Mapping species distributions from literature
- **Ecological Interaction Discovery** - Finding documented species interactions
- **Institutional Research** - Analyzing collections and museum holdings
- **Literature Integration** - Semantic linking of biodiversity research outputs

## Technical Infrastructure

### Technologies

- **Graph Database:** Ontotext GraphDB
- **Data Pipeline:** Apache Kafka for event streaming
- **Publishing Platform:** ARPHA (Advanced Research Publishing and Hosting Architecture)
- **Data Standards:** RDF, SPARQL, Darwin Core, Linked Open Data

### Ontologies

- **OpenBiodiv-O:** Custom ontology defining the semantic structure of the system
- Integration with multiple external ontologies for comprehensive coverage
- Semantic web standards for interoperability

## Citation and Usage

OpenBiodiv data is freely available under the Creative Commons Attribution 4.0 (CC BY 4.0) license. Users are encouraged to cite the appropriate OpenBiodiv publication(s) when using data from this resource in research or educational materials.

The system is operated by Pensoft Publishers in collaboration with major biodiversity institutions and the global biodiversity informatics community.
