---
activity_status: active
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ontotext.com/
  id: ontotext
  label: Ontotext Lab, Sirma Group
creation_date: '2025-12-17T00:00:00Z'
description: PROTON (PROTo ONtology) is a lightweight upper-level ontology serving
  as a foundational modeling basis for semantic web applications. It provides a modular
  framework with approximately 542 entity classes and 183 properties, covering named
  entities, temporal concepts, quantitative domains, and abstract concepts. Designed
  for information extraction, semantic annotation, knowledge management, and linked
  data integration.
domains: []
homepage_url: https://www.ontotext.com/products/proton/
id: proton
infores_id: proton
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
name: PROTON (PROTo ONtology)
products:
- category: OntologyProduct
  description: Complete PROTON 3.0 Beta ontology specification in OWL Lite/RDF-XML
    format, including all four modules (System, Top, Extent, KM) with comprehensive
    entity class definitions and properties
  format: owl
  id: proton.ontology
  is_public: true
  name: PROTON Ontology OWL Distribution
  product_file_size: 725192
  product_url: https://ontotext.com/documents/proton/Proton-Ver3.0B.pdf
- category: OntologyProduct
  description: PROTON Top Module - the primary upper-level ontology module containing
    core entity types (Person, Location, Organization), temporal concepts, quantitative
    domains, and abstract concepts
  format: owl
  id: proton.top
  is_public: true
  name: PROTON Top Module
  product_url: http://www.ontotext.com/proton/protontop
  warnings:
  - File was not able to be retrieved when checked on 2026-02-18_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-02-20_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-02-20: HTTP 403 error
    when accessing file'
- category: DocumentationProduct
  description: Comprehensive technical documentation and class reference for PROTON
    ontology covering all modules, properties, and usage guidelines
  format: http
  id: proton.documentation
  is_public: true
  name: PROTON Documentation
  product_url: https://www.ontotext.com/documents/proton/proton-doc.htm
- category: GraphicalInterface
  description: Interactive browser for exploring and navigating PROTON ontology structure,
    classes, and relationships on TriplyDB platform
  format: http
  id: proton.browser
  is_public: true
  name: PROTON Browser on TriplyDB
  product_url: https://triplydb.com/ontotext/proton/browser
- category: OntologyProduct
  description: OpenBioDiv-O, the OpenBiodiv Ontology
  format: ttl
  id: openbiodiv.ontology.ttl
  is_public: true
  name: OpenBioDiv-O
  original_source:
  - skos
  - proton
  - fabio
  - doco
  - openbiodiv
  product_file_size: 8176
  product_url: https://raw.githubusercontent.com/pensoft/OpenBiodiv/refs/heads/master/ontology/openbiodiv-ontology-latest.ttl
  secondary_source:
  - openbiodiv
repository: https://github.com/Ontotext-AD/proton
synonyms:
- PROTo ONtology
- PROTON 3.0
- PROTON Top
version: 3.0 Beta
---
# PROTON (PROTo ONtology)

## Overview

PROTON (PROTo ONtology) is a lightweight, modular upper-level ontology developed by Ontotext Lab as part of the EU-funded SEKT (Semantically Enabled Knowledge Technologies) project. It serves as a foundational modeling basis for semantic web applications, knowledge management systems, and linked data integration across multiple domains.

The ontology is designed to enable automatic entity recognition, information extraction from text, semantic annotation of documents, and alignment of domain-specific ontologies with a common upper-level framework.

## Ontology Structure

### Modular Architecture

PROTON is organized into four complementary modules:

1. **System Module** (base layer)
   - Technical and auxiliary classes for ontology management
   - Contains: LexicalResource, EntitySource, Entity
   - Supports system-level operations

2. **Top Module** (primary layer)
   - Core upper-level concepts and entity types
   - Named entities: Person, Location, Organization, Agent
   - Temporal concepts: Date, TimeInterval, Event, Happening
   - Quantitative/Concrete domains: Money, Number, Address, Measurement
   - Abstract concepts: Topic, GeneralTerm, InformationResource

3. **Extent Module**
   - Extended entity types and domain-specific extensions

4. **KM Module** (Knowledge Management)
   - Knowledge management specific concepts and properties

### Scale

- **542 entity classes** - Comprehensive coverage of named entity types and conceptual domains
- **183 properties** - Relational definitions for connecting and describing entities
- **OWL Lite formalism** - Ensures computational tractability while maintaining semantic expressiveness

## Technical Specifications

### Format and Representation

- **Standard format:** OWL Lite (W3C Web Ontology Language Lite dialect)
- **Serialization:** RDF/XML (Resource Description Framework XML)
- **Conformance:** Follows W3C semantic web standards

### Design Principles

PROTON's architecture is based on stratification principles derived from DOLCE (Descriptive Ontology for Linguistic and Cognitive Engineering):

- **Objects (Endurants)** - Entities that exist and persist
- **Happenings (Perdurants)** - Events, processes, and situations
- **Abstracts** - Abstract concepts and generalizations

## Content Coverage

### Named Entity Types

- **Persons** - Individual humans with associated properties
- **Organizations** - Companies, institutions, governmental bodies
- **Locations** - Geographic places, regions, countries, administrative divisions
- **Agents** - Generic agent entities (persons, organizations, or other actors)

### Temporal Concepts

- **Dates and time intervals** - Temporal anchoring and duration specification
- **Events and situations** - Temporal occurrences and their properties
- **Temporal relationships** - Sequencing and temporal ordering

### Quantitative and Concrete Domains

- **Monetary values** - Currency and financial amounts
- **Numerical data** - Quantities and measurements
- **Spatial information** - Addresses and geographic coordinates
- **Physical measurements** - Units and quantitative specifications

### Abstract Concepts

- **Topics and subjects** - Subject matter and thematic areas
- **General terms** - Generalized concepts and abstractions
- **Information resources** - Documents, publications, and information entities

## Access and Integration

### Available Endpoints

**RDF/Semantic Web Access:**
- Direct RDF: http://www.ontotext.com/proton/protontop
- Alternative RDF endpoints: http://proton.semanticweb.org/2005/04/protons and protonext

**Interactive Browsing:**
- TriplyDB Browser: https://triplydb.com/ontotext/proton/browser
- Provides interactive visualization and exploration of ontology structure

**Documentation:**
- Technical documentation: https://www.ontotext.com/documents/proton/proton-doc.htm
- Official specification: https://ontotext.com/documents/proton/Proton-Ver3.0B.pdf

### Integration Frameworks

PROTON integrates seamlessly with:

- **Semantic Publishing:** SPAR (Semantic Publishing and Referencing) Ontologies
- **Biodiversity Standards:** Darwin Core, OpenBiodiv-O, NOMEN, TaxPub
- **Linked Open Data:** DBPedia, GeoNames, Wikidata, and other major LOD datasets
- **Knowledge Management Systems:** GraphDB and OWLIM semantic repositories
- **Information Extraction:** Text analysis and Natural Language Processing pipelines

## Use Cases and Applications

### Information Extraction and NLP

- Semantic annotation of textual documents
- Automatic named entity recognition and classification
- Ontology population from unstructured text
- Enhancement of natural language processing systems

### Semantic Web Applications

- Knowledge management and organization
- Question answering systems
- Semantic search and information retrieval
- Semantic desktop environments
- Linked data integration and querying

### Domain-Specific Applications

- **Biodiversity Informatics** - Via OpenBiodiv-O integration for scientific literature and taxonomic data
- **Legal and Juridical Domain** - Integration with legal ontologies for domain modeling
- **Scientific Publishing** - Semantic annotation of research documents
- **Data Integration** - Schema mapping and heterogeneous data source alignment

### Knowledge Graph Construction

- Ontology alignment and mapping
- Upper-level framework for domain-specific ontology development
- Linked Open Data harmonization
- Cross-domain knowledge integration

## Standards Compliance

PROTON adheres to and integrates with:

- **W3C Standards:** OWL, RDF, SPARQL
- **Semantic Web:** Linked Data principles (5-star open data)
- **Interoperability:** Compatible with major semantic frameworks (UMBEL, DOLCE, SUMO)
- **Biodiversity Standards:** Darwin Core, GBIF requirements
- **Domain Standards:** Specialized alignments with discipline-specific ontologies

## Historical Context

PROTON was developed as a deliverable of the EU-IST SEKT Project (IST-2003-506826) between 2003-2006. It represents a collaborative effort to establish a lightweight yet comprehensive upper-level ontology suitable for knowledge management and semantic web applications.

Original creators:
- Kiril Simov
- Atanas Kiryakov
- Ivan Terziev
- Dimitar Manov
- Mariana Damova
- Svetoslav Petrov

## Maintenance and Support

**Current Maintainer:** Ontotext Lab, Sirma Group

The ontology continues to be maintained and extended through integration with modern linked data ecosystems and semantic web applications. It remains a reference upper-level ontology in the semantic web community.

## Citation and Usage

PROTON is freely available under the Creative Commons Attribution 3.0 Unported (CC-BY 3.0) license. Users are required to provide appropriate attribution to the original creators and maintainers when using this ontology in research or applications.

Recommended attribution: "This work is based on Proton ontology, developed by Ontotext" with reference to http://www.ontotext.com/proton-ontology