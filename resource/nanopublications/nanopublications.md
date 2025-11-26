---
activity_status: active
category: DataModel
creation_date: '2025-10-30T00:00:00Z'
description: Nanopublications are a format for publishing scientific claims as small, machine-readable, FAIR digital objects using RDF semantic web technology. Each nanopublication consists of three parts - an assertion, provenance metadata, and publication info - forming minimal publishable information units that can be cited, queried, and reused.
domains: []
id: "nanopublications"
infores_id: "nanopublications"
homepage_url: http://nanopub.net/
last_modified_date: '2025-11-26T00:00:00Z'
layout: resource_detail
name: Nanopublications Network
synonyms:
  - Nanopublications
  - Nanopubs
repository: https://github.com/Nanopublication
products:
  - category: GraphicalInterface
    description: Web interface for browsing and searching nanopublications
    format: http
    id: "nanopublications.portal"
    name: Nanopublications Browser
    product_url: http://nanopub.net/
    original_source:
      - nanopublications
  - category: ProgrammingInterface
    description: Decentralized server network for storing and retrieving nanopublications
    format: http
    id: "nanopublications.servers"
    name: Nanopublication Server Network
    product_url: http://nanopub.net/
    original_source:
      - nanopublications
publications:
  - id: "https://doi.org/10.7717/peerj-cs.387"
    title: "Genuine semantic publishing"
    journal: PeerJ Computer Science
    year: "2021"
---

# Nanopublications Network

## Overview

Nanopublications provide a format for publishing the smallest unit of publishable information: an assertion about anything that can be uniquely identified. Each nanopublication uses RDF (Resource Description Framework) to represent assertions with their provenance and publication metadata as machine-readable FAIR (Findable, Accessible, Interoperable, Reusable) digital objects.

## Key Features

- **Three-Part Structure**: Each nanopublication consists of Assertion, Provenance, and Publication Info graphs
- **RDF-Based**: Uses semantic web standards for maximum interoperability
- **FAIR Principles**: Designed to make scientific claims truly FAIR
- **Decentralized**: Distributed server network with no single point of failure
- **Citable**: Each nanopublication has a unique identifier and can be cited
- **Immutable**: Once published, nanopublications cannot be changed (only retracted or superseded)

## Nanopublication Structure

### Three Named Graphs

1. **Assertion Graph**: The actual scientific claim or statement
2. **Provenance Graph**: Metadata about how the assertion was derived (methods, sources, authors)
3. **Publication Info Graph**: Metadata about the nanopublication itself (creation date, license, etc.)

### Format
- Uses RDF for semantic representation
- Serializable in multiple formats (Turtle, RDF/XML, JSON-LD, etc.)
- Employs trusty URIs for content-based identification
- Cryptographically signed for integrity verification

## Applications

- **Scientific Publishing**: Publishing small, reusable units of scientific knowledge
- **Data Integration**: Linking heterogeneous data sources semantically
- **Knowledge Graphs**: Building machine-readable knowledge representations
- **Provenance Tracking**: Recording detailed lineage of scientific claims
- **Hypothesis Publishing**: Making testable hypotheses explicitly citable
- **Review & Commentary**: Publishing responses and annotations to other work

## Network Infrastructure

### Server Network
- Decentralized network of nanopublication servers
- Each server can replicate content from others
- No central authority required
- Automatic discovery and synchronization
- Multiple access protocols supported

### Query & Access
- SPARQL endpoints for semantic queries
- REST APIs for programmatic access
- Web interfaces for browsing
- Bulk downloads available
- Federated queries across servers

## Tools & Libraries

- **nanopub-java**: Java library for creating and handling nanopublications
- **nanopub Python package**: Python tools for nanopublications
- **Nanobench**: Desktop application for creating nanopublications
- **nanopub-server**: Server software for hosting nanopublications
- Various validators and converters

## Community & Development

- Open community of researchers and developers
- Specifications developed through collaborative process
- Multiple implementations and tools available
- Used by various research projects and initiatives
- Growing adoption in life sciences and beyond

## Data Licensing

Nanopublications themselves use CC0 (public domain dedication) or CC-BY licenses, though individual assertions may reference data with different licenses.

## Information Resource ID

This resource has the Information Resource identifier: `infores:nanopublications`
