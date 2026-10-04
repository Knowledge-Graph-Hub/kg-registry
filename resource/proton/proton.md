---
activity_status: inactive
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ontotext.com/
  id: ontotext
  label: Ontotext Lab, Sirma Group
creation_date: '2025-12-17T00:00:00Z'
description: PROTON (PROTo ONtology) is a lightweight upper-level ontology developed
  by Ontotext in the EU SEKT project. It is split into System, Top, Extent and Knowledge
  Management modules, covering named entities such as people, organizations and locations,
  temporal and quantitative concepts, and information resources, and was used for
  information extraction, semantic annotation and linked data integration. Version
  3.0 (Beta) added a Linked Open Data extension mapped to DBpedia, Freebase and GeoNames.
  It has not been updated since about 2012, and the Ontotext homepage now redirects
  to a missing page on graphwise.ai.
domains:
- general
homepage_url: https://www.ontotext.com/products/proton/
id: proton
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
name: PROTON (PROTo ONtology)
products:
- category: DocumentationProduct
  description: PDF specification of PROTON 3.0 Beta, describing the System, Top, Extent
    and Knowledge Management modules and their classes and properties.
  format: pdf
  id: proton.ontology
  is_public: true
  name: PROTON 3.0 Beta Specification
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proton
  - relation_type: prov:wasInfluencedBy
    source: geonames
  product_file_size: 725192
  product_url: https://ontotext.com/documents/proton/Proton-Ver3.0B.pdf
  warnings:
  - Could not be retrieved when checked on 2026-10-04 because the Ontotext site served
    a CAPTCHA page instead of the file.
- category: OntologyProduct
  compression: gzip
  description: PROTON Top module (version 3.0) in Turtle, as mirrored on TriplyDB,
    with core entity types such as Person, Location and Organization plus temporal,
    quantitative and abstract concepts.
  format: ttl
  id: proton.top
  is_public: true
  name: PROTON Top Module
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proton
  - relation_type: prov:wasInfluencedBy
    source: geonames
  product_file_size: 12036
  product_url: https://api.triplydb.com/datasets/ontotext/proton/download.ttl.gz
- category: DocumentationProduct
  description: Comprehensive technical documentation and class reference for PROTON
    ontology covering all modules, properties, and usage guidelines
  format: http
  id: proton.documentation
  is_public: true
  name: PROTON Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proton
  product_url: https://www.ontotext.com/documents/proton/proton-doc.htm
  warnings:
  - Could not be retrieved when checked on 2026-10-04 because the Ontotext site served
    a CAPTCHA page instead of the file.
- category: GraphicalInterface
  description: Interactive browser for exploring and navigating PROTON ontology structure,
    classes, and relationships on TriplyDB platform
  format: http
  id: proton.browser
  is_public: true
  name: PROTON Browser on TriplyDB
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proton
  product_url: https://triplydb.com/ontotext/proton/browser
- category: OntologyProduct
  description: OpenBioDiv-O, the OpenBiodiv Ontology
  format: ttl
  id: openbiodiv.ontology.ttl
  is_public: true
  name: OpenBioDiv-O
  original_source:
  - relation_type: prov:hadPrimarySource
    source: skos
  - relation_type: prov:hadPrimarySource
    source: proton
  - relation_type: prov:hadPrimarySource
    source: fabio
  - relation_type: prov:hadPrimarySource
    source: doco
  - relation_type: prov:hadPrimarySource
    source: openbiodiv
  product_file_size: 8176
  product_url: https://raw.githubusercontent.com/pensoft/OpenBiodiv/refs/heads/master/ontology/openbiodiv-ontology-latest.ttl
publications:
- authors:
  - Mariana Damova
  - Svetoslav Petrov
  - Kiril Simov
  doi: 10.1007/978-3-642-15431-7_31
  id: doi:10.1007/978-3-642-15431-7_31
  journal: Lecture Notes in Computer Science
  title: Mapping Data Driven and Upper Level Ontology
  year: '2010'
synonyms:
- PROTo ONtology
- PROTON 3.0
- PROTON Top
version: 3.0 Beta
warnings:
- The homepage redirected to a missing page on graphwise.ai (HTTP 404) when checked
  on 2026-10-04, after Ontotext became Graphwise.
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
- Historical namespace: http://proton.semanticweb.org/2005/04/protons (no longer resolves)

**Interactive Browsing:**
- TriplyDB Browser: https://triplydb.com/ontotext/proton/browser
- Provides interactive visualization and exploration of ontology structure

**Documentation:**
- Technical documentation: https://www.ontotext.com/documents/proton/proton-doc.htm
- Official specification: https://ontotext.com/documents/proton/Proton-Ver3.0B.pdf

### Integration Frameworks

PROTON integrates seamlessly with:

- **Semantic Publishing:** SPAR (Semantic Publishing and Referencing) Ontologies
- **Biodiversity:** reused by the OpenBiodiv-O ontology
- **Linked Open Data:** the PROTON 3.0 extension was mapped to DBpedia, Freebase and GeoNames
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
- **Interoperability:** aligned with UMBEL; its top-level split follows DOLCE
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

PROTON has not been updated since version 3.0 Beta (about 2012). The Ontotext pages are no longer reliably reachable, but the Top module remains available on TriplyDB.

## Citation and Usage

PROTON is freely available under the Creative Commons Attribution 3.0 Unported (CC-BY 3.0) license. Users are required to provide appropriate attribution to the original creators and maintainers when using this ontology in research or applications.

Recommended attribution: "This work is based on Proton ontology, developed by Ontotext" with reference to http://www.ontotext.com/proton-ontology