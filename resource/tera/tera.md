---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: Erik-BM
  label: Erik B. Myklebust
creation_date: '2025-10-28T00:00:00Z'
description: 'The Toxicological Effect and Risk Assessment (TERA) Knowledge Graph
  is an integrated knowledge graph for ecological risk assessment based on chemical
  effect data from U.S. EPA ECOTOX. TERA aligns toxicological data to non-proprietary
  identifiers using ontology alignment tools and external sources such as Wikidata,
  enabling the use of external chemical knowledge graphs including ChEBI, PubChem,
  and MeSH. The knowledge graph also includes aggregated data from NCBI Taxonomy and
  Encyclopedia of Life (EOL) trait data. By linking ECOTOX to external sources, TERA
  enables the extrapolation of chemical effect data, extending the reach of ecological
  risk assessment while limiting the need for laboratory experiments. The knowledge
  graph has been applied to predict adverse biological effects of chemicals using
  knowledge graph embeddings and supports various applications in environmental toxicology
  and risk assessment.

  '
domains:
- toxicology
- environment
- biological systems
homepage_url: https://niva-knowledge-graph.github.io/TERA/
id: tera
last_modified_date: '2025-10-28T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: 'TERA: Toxicological Effect and Risk Assessment Knowledge Graph'
products:
- category: DocumentationProduct
  description: API documentation for the TERA knowledge graph package
  format: http
  id: tera.documentation
  name: TERA Documentation
  product_url: https://niva-knowledge-graph.github.io/TERA/
- category: Product
  description: TERA knowledge graph dataset snapshot version 1.1.0 hosted on Zenodo,
    including NT files and CSV mappings
  format: http
  id: tera.zenodo-dataset
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY 4.0
  name: TERA Knowledge Graph Dataset (Zenodo)
  product_file_size: 5905580032
  product_url: https://zenodo.org/records/4244313
- category: Product
  description: Chemical data from EPA ECOTOX in N-Triples RDF format
  format: ntriples
  id: tera.ecotox-chemical-nt
  name: ECOTOX Chemical Data (N-Triples)
  product_file_size: 680300
  product_url: https://zenodo.org/records/4244313/files/ecotox_chemical.nt
- category: Product
  description: Taxonomy data from EPA ECOTOX in N-Triples RDF format
  format: ntriples
  id: tera.ecotox-taxonomy-nt
  name: ECOTOX Taxonomy Data (N-Triples)
  product_file_size: 22800000
  product_url: https://zenodo.org/records/4244313/files/ecotox_taxonomy.nt
- category: Product
  description: Chemical effects data in N-Triples RDF format
  format: ntriples
  id: tera.effects-nt
  name: Effects Data (N-Triples)
  product_file_size: 1000000000
  product_url: https://zenodo.org/records/4244313/files/effects.nt
- category: Product
  description: MeSH (Medical Subject Headings) data in N-Triples RDF format
  format: ntriples
  id: tera.mesh-nt
  name: MeSH Data (N-Triples)
  product_file_size: 2100000000
  product_url: https://zenodo.org/records/4244313/files/mesh.nt
- category: Product
  description: NCBI Taxonomy data in N-Triples RDF format
  format: ntriples
  id: tera.ncbi-nt
  name: NCBI Taxonomy Data (N-Triples)
  product_file_size: 1400000000
  product_url: https://zenodo.org/records/4244313/files/ncbi.nt
- category: Product
  description: Encyclopedia of Life traits data in N-Triples RDF format
  format: ntriples
  id: tera.traits-nt
  name: EOL Traits Data (N-Triples)
  product_file_size: 968000000
  product_url: https://zenodo.org/records/4244313/files/traits.nt
- category: MappingProduct
  description: Mapping file linking CAS Registry Numbers to MeSH identifiers
  format: csv
  id: tera.cas-to-mesh-csv
  name: CAS to MeSH Mapping (CSV)
  product_file_size: 109400
  product_url: https://zenodo.org/records/4244313/files/cas_to_mesh.csv
- category: MappingProduct
  description: Mapping file linking ChEBI identifiers to MeSH identifiers
  format: csv
  id: tera.chebi-to-mesh-csv
  name: ChEBI to MeSH Mapping (CSV)
  product_file_size: 78600
  product_url: https://zenodo.org/records/4244313/files/chebi_to_mesh.csv
- category: MappingProduct
  description: Mapping file linking ChEMBL identifiers to MeSH identifiers
  format: csv
  id: tera.chembl-to-mesh-csv
  name: ChEMBL to MeSH Mapping (CSV)
  product_file_size: 108500
  product_url: https://zenodo.org/records/4244313/files/chembl_to_mesh.csv
- category: MappingProduct
  description: Mapping file linking PubChem compound identifiers (CID) to MeSH identifiers
  format: csv
  id: tera.cid-to-mesh-csv
  name: PubChem CID to MeSH Mapping (CSV)
  product_file_size: 108000
  product_url: https://zenodo.org/records/4244313/files/cid_to_mesh.csv
- category: MappingProduct
  description: Mapping file linking NCBI Taxonomy identifiers to Encyclopedia of Life
    identifiers
  format: csv
  id: tera.ncbi-to-eol-csv
  name: NCBI to EOL Mapping (CSV)
  product_file_size: 3800000
  product_url: https://zenodo.org/records/4244313/files/ncbi_to_eol.csv
- category: ProgrammingInterface
  description: Python package providing APIs for data aggregation, integration, and
    access of TERA knowledge graph
  format: python
  id: tera.python-package
  name: TERA Python Package
  repository: https://github.com/NIVA-Knowledge-Graph/TERA
publications:
- authors:
  - Erik Bryhn Myklebust
  - Ernesto Jimenez-Ruiz
  - Jiaoyan Chen
  - Raoul Wolf
  - Knut Erik Tollefsen
  category: Publication
  id: https://doi.org/10.48550/arXiv.1908.10128
  journal: arXiv:1908.10128
  preferred: true
  title: 'TERA: the Toxicological Effect and Risk Assessment Knowledge Graph'
  year: '2019'
- authors:
  - Erik B. Myklebust
  - Ernesto Jimenez-Ruiz
  - Jiaoyan Chen
  - Raoul Wolf
  - Knut Erik Tollefsen
  category: Publication
  id: https://doi.org/10.3233/sw-222804
  journal: Semantic Web Journal
  preferred: false
  title: Prediction of Adverse Biological Effects of Chemicals Using Knowledge Graph
    Embeddings
  year: '2022'
repository: https://github.com/NIVA-Knowledge-Graph/TERA
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

## Automated Evaluation

- View the automated evaluation: [tera automated evaluation](tera_eval_automated.html)
