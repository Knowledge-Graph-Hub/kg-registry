---
activity_status: unknown
category: KnowledgeGraph
contacts:
- category: Individual
  label: Tong Wang
- category: Individual
  label: Lijun Duan
- category: Individual
  label: Chunxia He
- category: Individual
  label: Gengchen Deng
- category: Individual
  label: Rong Qin
- category: Individual
  label: Yanchun Zhang
creation_date: '2025-11-22T00:00:00Z'
description: ATOM (Anti-tumor Biomaterial Knowledge Graph) is a knowledge graph construction
  approach that extracts structured relationships about anti-tumor biomaterials from
  unstructured biomedicine literature, enabling researchers to efficiently access
  information about tumor treatment materials and their relationships.
domains:
- biomedical
- clinical
- health
homepage_url: https://doi.org/10.1109/BIBM47256.2019.8983062
id: atom
last_modified_date: '2025-11-22T00:00:00Z'
layout: resource_detail
name: ATOM
products:
- category: GraphProduct
  description: Anti-tumor biomaterial knowledge graph constructed from biomedicine
    literature, containing structured relationships among anti-tumor entities extracted
    through entity recognition, sentence simplification, triple extraction, and predicate
    mapping.
  id: atom.kg
  name: ATOM Knowledge Graph
  original_source:
  - pubmed
  product_url: https://doi.org/10.1109/BIBM47256.2019.8983062
  warnings:
  - File was not able to be retrieved when checked on 2025-11-22_ HTTP 418 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-11-25: HTTP 418 error
    when accessing file'
- category: ProcessProduct
  description: Natural language processing pipeline for constructing anti-tumor biomaterial
    knowledge graphs from unstructured biomedicine literature, implementing entity
    recognition, sentence simplification, triple extraction, and predicate mapping
    processes.
  id: atom.pipeline
  name: ATOM Construction Pipeline
  original_source:
  - atom
  product_url: https://doi.org/10.1109/BIBM47256.2019.8983062
  warnings:
  - File was not able to be retrieved when checked on 2025-11-22_ HTTP 418 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-11-25: HTTP 418 error
    when accessing file'
publications:
- authors:
  - Tong Wang
  - Lijun Duan
  - Chunxia He
  - Gengchen Deng
  - Rong Qin
  - Yanchun Zhang
  doi: 10.1109/BIBM47256.2019.8983062
  id: doi:10.1109/BIBM47256.2019.8983062
  journal: 2019 IEEE International Conference on Bioinformatics and Biomedicine (BIBM)
  title: 'ATOM: Construction of Anti-tumor Biomaterial Knowledge Graph by Biomedicine
    Literature'
  year: '2019'
---
# ATOM

## Overview

ATOM (Anti-tumor Biomaterial Knowledge Graph) is a knowledge graph construction approach developed to address the challenge of extracting structured information from the rapidly growing body of unstructured biomedicine literature on anti-tumor biomaterials. As anti-tumor biomaterials research has expanded, the volume of literature has made it increasingly difficult for researchers to efficiently obtain relevant information about tumor treatment materials and their relationships.

The ATOM approach transforms unstructured text from biomedicine literature into a structured knowledge graph that explicitly represents entities and their relationships, making it easier for researchers to navigate and query information about anti-tumor biomaterials.

## Key Features

### Knowledge Graph Construction Pipeline

ATOM implements a comprehensive four-stage pipeline for knowledge graph construction:

1. **Entity Recognition**: Identifies anti-tumor biomaterial entities and related biomedical concepts within literature text
2. **Sentence Simplification**: Processes complex sentences to facilitate relationship extraction
3. **Triple Extraction**: Extracts subject-predicate-object triples representing relationships between entities
4. **Predicate Mapping**: Maps extracted predicates to standardized relationship types for consistency

### Literature-Driven Approach

ATOM specifically targets biomedicine literature as its primary data source, focusing on extracting information relevant to anti-tumor biomaterial applications. This literature-driven approach enables the system to:

- Capture the latest research findings on anti-tumor biomaterials
- Represent diverse types of relationships (e.g., material properties, therapeutic mechanisms, clinical applications)
- Integrate information across multiple publications

### Structured Knowledge Representation

The resulting knowledge graph provides structured relationships among anti-tumor entities, enabling:

- Efficient querying of material properties and relationships
- Discovery of connections between biomaterials and tumor treatments
- Support for computational analysis and reasoning about anti-tumor therapies

## Applications

### Information Retrieval

ATOM addresses the fundamental challenge of information retrieval from unstructured biomedicine literature, allowing researchers to:

- Quickly locate relevant information about specific anti-tumor biomaterials
- Understand relationships between materials and their therapeutic effects
- Navigate complex networks of biomaterial interactions

### Research Support

The knowledge graph supports biomedical research by:

- Providing structured access to anti-tumor biomaterial knowledge
- Facilitating hypothesis generation about material combinations or applications
- Enabling systematic analysis of material properties and therapeutic outcomes

### Knowledge Integration

ATOM contributes to the broader biomedical knowledge infrastructure by:

- Standardizing representation of anti-tumor biomaterial relationships
- Integrating information across disparate literature sources
- Supporting interoperability with other biomedical knowledge resources

## Technical Implementation

### Natural Language Processing

ATOM employs natural language processing techniques to:

- Parse unstructured text from biomedicine publications
- Identify named entities related to anti-tumor biomaterials
- Extract meaningful relationships expressed in natural language

### Knowledge Graph Architecture

The system constructs a graph-based representation where:

- Nodes represent anti-tumor biomaterial entities and related concepts
- Edges represent relationships between entities (mapped predicates)
- The structure supports graph-based queries and reasoning

## Validation

Experimental evaluation demonstrated that ATOM effectively:

- Expresses extracted anti-tumor entities and their relationships
- Constructs meaningful knowledge graphs from biomedicine literature
- Addresses the gap in tools for anti-tumor biomaterial knowledge graph construction

## Significance

ATOM represents a specialized solution for the anti-tumor biomaterials domain, filling a previously identified gap in knowledge graph construction tools. By providing structured access to information from biomedicine literature, ATOM supports researchers in navigating the growing body of knowledge about anti-tumor biomaterials and accelerates research in tumor treatment development.

The approach demonstrates the value of domain-specific knowledge graph construction methods that address the unique characteristics and requirements of specialized biomedical fields.

---

*This resource page was created based on the conference paper published at IEEE BIBM 2019. Limited information is available about ongoing development or public availability of the ATOM system.*