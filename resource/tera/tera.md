---
id: "tera"
category: 'KnowledgeGraph'
layout: 'resource_detail'
name: 'TERA: Toxicological Effect and Risk Assessment Knowledge Graph'
activity_status: 'active'
description: >
  The Toxicological Effect and Risk Assessment (TERA) Knowledge Graph is an integrated knowledge graph
  for ecological risk assessment based on chemical effect data from U.S. EPA ECOTOX. TERA aligns
  toxicological data to non-proprietary identifiers using ontology alignment tools and external sources
  such as Wikidata, enabling the use of external chemical knowledge graphs including ChEBI, PubChem,
  and MeSH. The knowledge graph also includes aggregated data from NCBI Taxonomy and Encyclopedia of
  Life (EOL) trait data. By linking ECOTOX to external sources, TERA enables the extrapolation of
  chemical effect data, extending the reach of ecological risk assessment while limiting the need for
  laboratory experiments. The knowledge graph has been applied to predict adverse biological effects
  of chemicals using knowledge graph embeddings and supports various applications in environmental
  toxicology and risk assessment.
homepage_url: 'https://niva-knowledge-graph.github.io/TERA/'
repository: 'https://github.com/NIVA-Knowledge-Graph/TERA'
license:
  id: "https://opensource.org/licenses/MIT"
  label: 'MIT License'
domains:
  - toxicology
  - environment
  - biological systems
creation_date: '2025-10-28T00:00:00Z'
last_modified_date: '2025-10-28T00:00:00Z'
contacts:
  - category: 'Individual'
    label: 'Erik B. Myklebust'
    contact_details:
      - contact_type: 'github'
        value: "Erik-BM"
publications:
  - id: "https://doi.org/10.48550/arXiv.1908.10128"
    category: 'Publication'
    preferred: true
    title: 'TERA: the Toxicological Effect and Risk Assessment Knowledge Graph'
    authors:
      - 'Erik Bryhn Myklebust'
      - 'Ernesto Jimenez-Ruiz'
      - 'Jiaoyan Chen'
      - 'Raoul Wolf'
      - 'Knut Erik Tollefsen'
    year: "2019"
    journal: 'arXiv:1908.10128'
  - id: "https://doi.org/10.3233/sw-222804"
    category: 'Publication'
    preferred: false
    title: 'Prediction of Adverse Biological Effects of Chemicals Using Knowledge Graph Embeddings'
    authors:
      - 'Erik B. Myklebust'
      - 'Ernesto Jimenez-Ruiz'
      - 'Jiaoyan Chen'
      - 'Raoul Wolf'
      - 'Knut Erik Tollefsen'
    year: "2022"
    journal: 'Semantic Web Journal'
products:
  - id: "tera.documentation"
    category: 'DocumentationProduct'
    name: 'TERA Documentation'
    description: 'API documentation for the TERA knowledge graph package'
    product_url: 'https://niva-knowledge-graph.github.io/TERA/'
    format: 'http'
  - id: "tera.zenodo-dataset"
    category: 'Product'
    name: 'TERA Knowledge Graph Dataset (Zenodo)'
    description: 'TERA knowledge graph dataset snapshot version 1.1.0 hosted on Zenodo, including NT files and CSV mappings'
    product_url: 'https://zenodo.org/records/4244313'
    format: 'http'
    product_file_size: 5905580032
    license:
      id: "https://creativecommons.org/licenses/by/4.0/"
      label: 'CC-BY 4.0'
  - id: "tera.ecotox-chemical-nt"
    category: 'Product'
    name: 'ECOTOX Chemical Data (N-Triples)'
    description: 'Chemical data from EPA ECOTOX in N-Triples RDF format'
    product_url: 'https://zenodo.org/records/4244313/files/ecotox_chemical.nt'
    format: 'ntriples'
    product_file_size: 680300
  - id: "tera.ecotox-taxonomy-nt"
    category: 'Product'
    name: 'ECOTOX Taxonomy Data (N-Triples)'
    description: 'Taxonomy data from EPA ECOTOX in N-Triples RDF format'
    product_url: 'https://zenodo.org/records/4244313/files/ecotox_taxonomy.nt'
    format: 'ntriples'
    product_file_size: 22800000
  - id: "tera.effects-nt"
    category: 'Product'
    name: 'Effects Data (N-Triples)'
    description: 'Chemical effects data in N-Triples RDF format'
    product_url: 'https://zenodo.org/records/4244313/files/effects.nt'
    format: 'ntriples'
    product_file_size: 1000000000
  - id: "tera.mesh-nt"
    category: 'Product'
    name: 'MeSH Data (N-Triples)'
    description: 'MeSH (Medical Subject Headings) data in N-Triples RDF format'
    product_url: 'https://zenodo.org/records/4244313/files/mesh.nt'
    format: 'ntriples'
    product_file_size: 2100000000
  - id: "tera.ncbi-nt"
    category: 'Product'
    name: 'NCBI Taxonomy Data (N-Triples)'
    description: 'NCBI Taxonomy data in N-Triples RDF format'
    product_url: 'https://zenodo.org/records/4244313/files/ncbi.nt'
    format: 'ntriples'
    product_file_size: 1400000000
  - id: "tera.traits-nt"
    category: 'Product'
    name: 'EOL Traits Data (N-Triples)'
    description: 'Encyclopedia of Life traits data in N-Triples RDF format'
    product_url: 'https://zenodo.org/records/4244313/files/traits.nt'
    format: 'ntriples'
    product_file_size: 968000000
  - id: "tera.cas-to-mesh-csv"
    category: 'MappingProduct'
    name: 'CAS to MeSH Mapping (CSV)'
    description: 'Mapping file linking CAS Registry Numbers to MeSH identifiers'
    product_url: 'https://zenodo.org/records/4244313/files/cas_to_mesh.csv'
    format: 'csv'
    product_file_size: 109400
  - id: "tera.chebi-to-mesh-csv"
    category: 'MappingProduct'
    name: 'ChEBI to MeSH Mapping (CSV)'
    description: 'Mapping file linking ChEBI identifiers to MeSH identifiers'
    product_url: 'https://zenodo.org/records/4244313/files/chebi_to_mesh.csv'
    format: 'csv'
    product_file_size: 78600
  - id: "tera.chembl-to-mesh-csv"
    category: 'MappingProduct'
    name: 'ChEMBL to MeSH Mapping (CSV)'
    description: 'Mapping file linking ChEMBL identifiers to MeSH identifiers'
    product_url: 'https://zenodo.org/records/4244313/files/chembl_to_mesh.csv'
    format: 'csv'
    product_file_size: 108500
  - id: "tera.cid-to-mesh-csv"
    category: 'MappingProduct'
    name: 'PubChem CID to MeSH Mapping (CSV)'
    description: 'Mapping file linking PubChem compound identifiers (CID) to MeSH identifiers'
    product_url: 'https://zenodo.org/records/4244313/files/cid_to_mesh.csv'
    format: 'csv'
    product_file_size: 108000
  - id: "tera.ncbi-to-eol-csv"
    category: 'MappingProduct'
    name: 'NCBI to EOL Mapping (CSV)'
    description: 'Mapping file linking NCBI Taxonomy identifiers to Encyclopedia of Life identifiers'
    product_url: 'https://zenodo.org/records/4244313/files/ncbi_to_eol.csv'
    format: 'csv'
    product_file_size: 3800000
  - id: "tera.python-package"
    category: 'ProgrammingInterface'
    name: 'TERA Python Package'
    description: 'Python package providing APIs for data aggregation, integration, and access of TERA knowledge graph'
    repository: 'https://github.com/NIVA-Knowledge-Graph/TERA'
    format: 'python'
---

The Toxicological Effect and Risk Assessment (TERA) Knowledge Graph provides an integrated semantic infrastructure for ecological risk assessment. TERA addresses the challenge of integrating diverse toxicological data sources to enable comprehensive chemical effect prediction while reducing the need for animal testing.

## Overview

TERA is built on chemical effect data from the U.S. EPA's ECOTOX database and integrates multiple external knowledge sources including NCBI Taxonomy, PubChem, ChEMBL, Encyclopedia of Life (EOL), Wikidata, MeSH, and ChEBI. The knowledge graph uses ontology alignment tools to link toxicological data to non-proprietary identifiers, creating a unified semantic framework for environmental risk assessment.

## Data Integration

The knowledge graph employs sophisticated data integration techniques to align chemical identifiers across multiple databases. TERA provides mapping files linking CAS Registry Numbers, ChEBI identifiers, ChEMBL identifiers, and PubChem compound identifiers to MeSH terms, as well as mappings between NCBI Taxonomy and Encyclopedia of Life. These mappings enable seamless integration of chemical and biological data from diverse sources.

## Applications

TERA has been successfully applied to predict adverse biological effects of chemicals using knowledge graph embeddings. The integration of ECOTOX data with external chemical knowledge graphs enables data extrapolation, allowing researchers to make predictions about chemical effects on species and endpoints not directly tested in laboratory experiments. This capability extends the reach of ecological risk assessment while addressing animal welfare concerns.

## Technical Architecture

The TERA system consists of three main modules:

- **DataAggregation**: Classes for aggregating data from multiple sources into common formats
- **DataIntegration**: Tools for aligning and integrating aggregated data using ontology alignment
- **DataAccess**: APIs providing programmatic access to the integrated knowledge graph

## Data Availability

The TERA knowledge graph is available as a comprehensive dataset on Zenodo (version 1.1.0, approximately 5.5 GB), containing:
- Chemical data (680 KB)
- Taxonomy data (22.8 MB)
- Effects data (1.0 GB)
- MeSH data (2.1 GB)
- NCBI Taxonomy data (1.4 GB)
- EOL Traits data (968 MB)
- Multiple identifier mapping files (CSV format)

All data files are provided in N-Triples RDF format, enabling semantic web applications and SPARQL queries.

## Development and Community

TERA is developed by the Norwegian Institute for Water Research (NIVA) Knowledge Graph team. The project has been featured in multiple peer-reviewed publications, including the International Semantic Web Conference (ISWC 2019, Best Student Paper in the In-Use track) and the Semantic Web Journal. The codebase is written in Python and is available under the MIT License.

## License Information

The TERA dataset is released under CC-BY 4.0. Component data sources maintain their original licenses:
- EOL: Various Creative Commons licenses
- NCBI: CC0 1.0 Universal
- ECOTOX: No restrictions
- PubChem: Open Data Commons Open Database License
- ChEMBL: CC Attribution
- MeSH: Open, Courtesy of U.S. National Library of Medicine
- Wikidata: CC0 1.0

The TERA software package is released under the MIT License.
