---
activity_status: active
category: DataModel
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: cjmungall@lbl.gov
  - contact_type: github
    value: cmungall
  label: Christopher J. Mungall
  orcid: 0000-0002-6601-2165
description: A data model for describing change operations at a high level on an ontology
  or ontology-like artefact, such as a Knowledge Graph. KGCL enables standardized
  representation of changes in ontologies and knowledge graphs for tracking, auditing,
  and reproducibility. It provides a formal language for representing and documenting
  changes in knowledge graphs, facilitating version control, change history, and collaboration.
domains:
- information technology
homepage_url: https://incatools.github.io/kgcl/
id: kgcl
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: Knowledge Graph Change Language
products:
- category: DataModelProduct
  description: OWL release of Knowledge Graph Change Language, provides a formal semantic
    model for representing change operations in ontologies and knowledge graphs.
  format: owl
  id: kgcl.model.owl
  name: Knowledge Graph Change Language OWL release
  original_source:
  - kgcl
  product_file_size: 11700
  product_url: https://w3id.org/kgcl/kgcl.owl.ttl
  secondary_source:
  - kgcl
- category: ProcessProduct
  description: Python implementation of the Knowledge Graph Change Language standard,
    including a LinkML model and LARK grammar for parsing and generating KGCL statements.
  id: kgcl.python
  name: KGCL Python Implementation
  original_source:
  - kgcl
  product_url: https://github.com/INCATools/kgcl/
  secondary_source:
  - kgcl
- category: DataModelProduct
  description: JSON-LD context for the Knowledge Graph Change Language model, enabling
    semantic interoperability for KGCL data.
  format: jsonld
  id: kgcl.model.jsonld
  name: Knowledge Graph Change Language JSON-LD Context
  original_source:
  - kgcl
  product_file_size: 2161
  product_url: https://w3id.org/kgcl/kgcl.context.jsonld
  secondary_source:
  - kgcl
- category: DataModelProduct
  description: SHACL shapes for validating Knowledge Graph Change Language instances.
  format: shacl
  id: kgcl.model.shacl
  name: Knowledge Graph Change Language SHACL Shapes
  original_source:
  - kgcl
  product_file_size: 15868
  product_url: https://w3id.org/kgcl/kgcl.shacl.ttl
  secondary_source:
  - kgcl
- category: DataModelProduct
  description: YAML schema representation of the Knowledge Graph Change Language model.
  format: yaml
  id: kgcl.model.yaml
  name: Knowledge Graph Change Language YAML Schema
  original_source:
  - kgcl
  product_file_size: 7492
  product_url: https://w3id.org/kgcl/kgcl.yaml
  secondary_source:
  - kgcl
publications:
- authors:
  - Hegde H
  - Vendetti J
  - Goutte-Gattat D
  - Caufield JH
  - Graybeal JB
  - Harris NL
  - Karam N
  - Kindermann C
  - Matentzoglu N
  - Overton JA
  - Mungall CJ
  id: doi:10.1093/database/baae133
  journal: Database
  preferred: true
  title: A change language for ontologies and knowledge graphs
  year: '2025'
repository: https://github.com/INCATools/kgcl/
version: 0.7.0
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