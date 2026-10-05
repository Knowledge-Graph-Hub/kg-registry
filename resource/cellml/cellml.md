---
activity_status: active
category: DataModel
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: editors@cellml.org
  - contact_type: url
    value: https://www.cellml.org/community/specification_custodians
  label: CellML Specification Custodian Board
- category: Organization
  contact_details:
  - contact_type: github
    value: cellml
  label: CellML
creation_date: '2026-10-05T00:00:00Z'
description: CellML is an open XML-based language for describing and exchanging mathematical
  models of biological processes, such as cellular electrophysiology, signaling and
  metabolism. Models are built from reusable components containing variables, units
  and equations written in MathML, connected through variable mappings and able to
  import other models. The standard has three versioned specifications (1.0, 1.1 and
  2.0), developed at the Auckland Bioengineering Institute and governed since May
  2026 by the CellML Specification Custodian Board. The libCellML library provides
  a reference implementation for reading, validating, analysing and generating code
  from CellML 2.0 models.
domains:
- systems biology
- biological systems
homepage_url: https://www.cellml.org/
id: cellml
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
name: CellML
products:
- category: DocumentationProduct
  description: Normative CellML 2.0 specification, the formal set of rules defining
    a valid CellML 2.0 model encoding, provided as a PDF. Previous release 2.0.0 and
    the 2017 drafts are linked from the CellML 2.0 specification page.
  format: pdf
  id: cellml.spec-2.0
  name: CellML 2.0 Normative Specification
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellml
  product_file_size: 191957
  product_url: https://www.cellml.org/specifications/cellml_2.0/cellml_2_0_normative_specification.pdf
- category: DocumentationProduct
  description: Informative rendering of the CellML 2.0 specification, which extends
    the normative rules with explanations, examples and notes on how each rule maps
    to the libCellML data model and API.
  format: http
  id: cellml.spec-2.0-informative
  name: CellML 2.0 Informative Specification
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellml
  product_url: https://cellml-specification.readthedocs.io/
- category: DocumentationProduct
  description: CellML 1.1 specification (6 November 2002, frozen 28 February 2006),
    which added model imports to CellML 1.0, with its errata.
  format: http
  id: cellml.spec-1.1
  name: CellML 1.1 Specification
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellml
  product_url: https://www.cellml.org/specifications/cellml_1.1
- category: DataModelProduct
  description: Document type definition (DTD) corresponding to the syntax rules of
    the CellML 1.1 specification.
  format: txt
  id: cellml.dtd-1.1
  name: CellML 1.1 DTD
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellml
  product_file_size: 4147
  product_url: https://www.cellml.org/cellml/cellml_1_1.dtd
- category: DocumentationProduct
  description: CellML 1.0 specification, the original recommendation of 10 August
    2001.
  format: http
  id: cellml.spec-1.0
  name: CellML 1.0 Specification
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellml
  product_url: https://www.cellml.org/specifications/cellml_1.0
- category: DataModelProduct
  description: Document type definition (DTD) corresponding to the syntax rules of
    the 10 August 2001 CellML 1.0 specification.
  format: txt
  id: cellml.dtd-1.0
  name: CellML 1.0 DTD
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellml
  product_file_size: 3830
  product_url: https://www.cellml.org/cellml/cellml_1_0.dtd
- category: ProcessProduct
  description: libCellML, a C++ library with Python bindings for creating, parsing,
    validating, analysing and printing CellML 2.0 models and for generating C and
    Python code from them. Licensed under Apache 2.0.
  format: http
  id: cellml.libcellml
  latest_version: v0.7.1
  license:
    id: https://www.apache.org/licenses/LICENSE-2.0
    label: Apache-2.0
  name: libCellML
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellml
  product_url: https://github.com/cellml/libcellml
- category: DocumentationProduct
  description: libCellML website with user documentation, tutorials, API reference
    and installation instructions.
  format: http
  id: cellml.libcellml-docs
  name: libCellML Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellml
  product_url: https://libcellml.org/
- category: DocumentationProduct
  description: CellML website pages listing the CellML specifications and software
    tools that support CellML.
  format: http
  id: cellml.specifications
  name: CellML Specifications Index
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellml
  product_url: https://www.cellml.org/specifications
publications:
- authors:
  - Michael Clerx
  - Michael T. Cooling
  - Jonathan Cooper
  - Alan Garny
  - Keri Moyle
  - David P. Nickerson
  - Poul M. F. Nielsen
  - Hugh Sorby
  doi: 10.1515/jib-2020-0021
  id: doi:10.1515/jib-2020-0021
  journal: Journal of Integrative Bioinformatics
  preferred: true
  title: CellML 2.0
  year: '2020'
- authors:
  - Michael Clerx
  - Michael T. Cooling
  - Jonathan Cooper
  - Alan Garny
  - Keri Moyle
  - David P. Nickerson
  - Poul M. F. Nielsen
  - Hugh Sorby
  doi: 10.1515/jib-2023-0003
  id: doi:10.1515/jib-2023-0003
  journal: Journal of Integrative Bioinformatics
  title: CellML 2.0.1
  year: '2023'
- authors:
  - Autumn A. Cuellar
  - Catherine M. Lloyd
  - Poul F. Nielsen
  - David P. Bullivant
  - David P. Nickerson
  - Peter J. Hunter
  doi: 10.1177/0037549703040939
  id: doi:10.1177/0037549703040939
  journal: SIMULATION
  title: An Overview of CellML 1.1, a Biological Model Description Language
  year: '2003'
- authors:
  - Catherine M. Lloyd
  - Matt D.B. Halstead
  - Poul F. Nielsen
  doi: 10.1016/j.pbiomolbio.2004.01.004
  id: doi:10.1016/j.pbiomolbio.2004.01.004
  journal: Progress in Biophysics and Molecular Biology
  title: 'CellML: its future, present and past'
  year: '2004'
repository: https://github.com/cellml
---
# CellML

CellML is an open, XML-based standard for encoding mathematical models of biological processes so that they can be stored, exchanged, reused and simulated by different software tools. It is most widely used for models of cellular electrophysiology, such as cardiac myocyte action potential models, but it applies to any system of ordinary differential and algebraic equations.

A CellML model is made of components. Each component declares variables with physical units and holds equations written in MathML. Variables in different components are linked through connections, and models can import components and units from other CellML documents. This makes it possible to assemble larger models from smaller ones.

## Specifications

- **CellML 1.0** (10 August 2001): the original recommendation, with a DTD.
- **CellML 1.1** (2002, frozen in 2006): added model imports; it also has a DTD.
- **CellML 2.0** (2020, with a 2.0.1 update published in 2023): a simplified and stricter revision. It has a normative specification and an informative version that explains the rules with examples.

## Software

[libCellML](https://libcellml.org/) is the reference library for CellML 2.0. It parses, validates, analyses and serializes models and generates C or Python code. It is developed on GitHub under the Apache 2.0 license. Many other tools read CellML, including OpenCOR and Myokit.

## Governance

The Auckland Bioengineering Institute developed CellML, and an elected CellML Editorial Board governed it. On 16 May 2026 governance passed to a self-sustaining CellML Specification Custodian Board, which can be contacted at editors@cellml.org.
