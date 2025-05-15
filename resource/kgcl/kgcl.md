---
layout: resource_detail
activity_status: active
id: kgcl
name: Knowledge Graph Change Language
description: A data model for describing change operations at a high level on an ontology
  or ontology-like artefact, such as a Knowledge Graph. KGCL enables standardized representation
  of changes in ontologies and knowledge graphs for tracking, auditing, and reproducibility.
  It provides a formal language for representing and documenting changes in knowledge graphs,
  facilitating version control, change history, and collaboration.
domains:
- information technology
version: 0.7.0
contacts:
- category: Individual
  label: Christopher J. Mungall
  orcid: 0000-0002-6601-2165
  contact_details:
  - contact_type: email
    value: cjmungall@lbl.gov
  - contact_type: github
    value: cmungall
homepage_url: https://incatools.github.io/kgcl/
repository: https://github.com/INCATools/kgcl/
products:
- id: kgcl.model.owl
  name: Knowledge Graph Change Language OWL release
  description: OWL release of Knowledge Graph Change Language, provides a formal semantic model for representing change operations in ontologies and knowledge graphs.
  category: DataModelProduct
  format: owl
  product_url: https://w3id.org/kgcl/kgcl.owl.ttl
  secondary_source:
  - kgcl
  original_source:
  - kgcl
- id: kgcl.python
  name: KGCL Python Implementation
  description: Python implementation of the Knowledge Graph Change Language standard, including a LinkML model and LARK grammar for parsing and generating KGCL statements.
  category: ProcessProduct
  product_url: https://github.com/INCATools/kgcl/
  secondary_source:
  - kgcl
  original_source:
  - kgcl
- id: kgcl.model.jsonld
  name: Knowledge Graph Change Language JSON-LD Context
  description: JSON-LD context for the Knowledge Graph Change Language model, enabling semantic interoperability for KGCL data.
  category: DataModelProduct
  format: jsonld
  product_url: https://w3id.org/kgcl/kgcl.context.jsonld
  secondary_source:
  - kgcl
  original_source:
  - kgcl
- id: kgcl.model.shacl
  name: Knowledge Graph Change Language SHACL Shapes
  description: SHACL shapes for validating Knowledge Graph Change Language instances.
  category: DataModelProduct
  format: shacl
  product_url: https://w3id.org/kgcl/kgcl.shacl.ttl
  secondary_source:
  - kgcl
  original_source:
  - kgcl
- id: kgcl.model.yaml
  name: Knowledge Graph Change Language YAML Schema
  description: YAML schema representation of the Knowledge Graph Change Language model.
  category: DataModelProduct
  format: yaml
  product_url: https://w3id.org/kgcl/kgcl.yaml
  secondary_source:
  - kgcl
  original_source:
  - kgcl
license:
  label: MIT License
  id: https://opensource.org/licenses/MIT
category: DataModel
publications:
- id: doi:10.1093/database/baae133
  title: "A change language for ontologies and knowledge graphs"
  authors:
    - "Hegde H"
    - "Vendetti J"
    - "Goutte-Gattat D"
    - "Caufield JH"
    - "Graybeal JB"
    - "Harris NL"
    - "Karam N"
    - "Kindermann C"
    - "Matentzoglu N"
    - "Overton JA"
    - "Mungall CJ"
  journal: Database
  year: "2025"
  preferred: true
---

## Overview

KGCL (Knowledge Graph Change Language) is a standard datamodel for representing changes in ontologies and knowledge graphs. It provides a formal way to describe operations such as node creation, edge modification, and entity obsolescence while preserving the history and intent behind each change.

## Purpose

The primary purposes of KGCL are:

1. **Tracking Changes**: Enables detailed tracking of every modification made to knowledge resources
2. **Reproducibility**: Ensures reproducible workflows for ontology and knowledge graph maintenance
3. **Auditability**: Provides mechanisms for auditing changes over time
4. **Collaboration**: Facilitates coordination among multiple editors working on shared knowledge resources
5. **Tools Integration**: Creates a standardized language that various tools can implement for consistent change management

## Components

KGCL consists of:
- A formal schema defining change operations
- Various serializations including OWL, OBO, SHACL, and YAML
- A Python implementation with a LinkML model and LARK grammar parser
- JSON-LD contexts for semantic web integration

## Usage

KGCL can be used for:
- Maintaining ontologies with complex editing workflows
- Documenting changes in versioned knowledge graphs
- Enabling programmatic applications to generate and interpret change operations
- Creating human-readable reports of modifications to knowledge resources
- Supporting quality control processes in collaborative ontology development

## Resources

* [Official Documentation](https://incatools.github.io/kgcl/)
* [GitHub Repository](https://github.com/INCATools/kgcl/)
* [W3ID Permanent Identifier](https://w3id.org/kgcl/)
