---
activity_status: inactive
category: Aggregator
contacts:
- category: Individual
  contact_details:
  - contact_type: url
    value: https://www.maastrichtuniversity.nl/
  label: Michel Dumontier
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.maastrichtuniversity.nl/research/institutes/institute-data-science
  id: maastricht-ids
  label: Maastricht University Institute of Data Science
creation_date: '2025-12-18T00:00:00Z'
description: Bio2RDF (Linked Biomedical RDF Network) is a large-scale open-source
  semantic web integration project that converts over 35 diverse biological and biomedical
  databases into standardized RDF (Resource Description Framework) linked data, providing
  11 billion RDF triples accessible through SPARQL endpoints and REST APIs. It enables
  federated queries across heterogeneous data sources using W3C standards and the
  Semanticscience Integrated Ontology (SIO).
domains:
- biomedical
- genomics
homepage_url: https://bio2rdf.org
id: bio2rdf
infores_id: bio2rdf
last_modified_date: '2025-12-20T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
name: Bio2RDF (Linked Biomedical RDF Network)
products:
- category: ProgrammingInterface
  description: SPARQL 1.1 endpoint powered by OpenLink Virtuoso for querying Bio2RDF
    linked data across 35+ integrated biomedical databases with federated query support
  format: http
  id: bio2rdf.sparql
  is_public: true
  name: Bio2RDF SPARQL Endpoint
  product_url: https://bio2rdf.org/sparql
- category: ProgrammingInterface
  description: REST API for programmatic access to Bio2RDF linked data with support
    for SPARQL queries and multiple result formats
  format: http
  id: bio2rdf.api
  is_public: true
  name: Bio2RDF REST API
  product_url: https://github.com/bio2rdf/bio2rdf-api
- category: Product
  description: Downloadable RDF triple stores and datasets in multiple serialization
    formats (Turtle, N-Triples, RDF/XML, N3) from 35+ integrated biological databases
  id: bio2rdf.dumps
  name: Bio2RDF RDF Dumps and Downloads
  product_url: https://download.bio2rdf.org/
- category: GraphicalInterface
  description: Web-based interface for browsing and exploring Bio2RDF resources and
    linked data across biological databases
  format: http
  id: bio2rdf.web
  is_public: true
  name: Bio2RDF Web Interface
  product_url: https://bio2rdf.org
- category: Product
  description: BioSearch semantic search engine for Bio2RDF providing full-text and
    semantic search across integrated biological databases
  id: bio2rdf.biosearch
  name: BioSearch Semantic Search Engine
  product_url: https://biosemantics.org/biosearch
  warnings:
  - File was not able to be retrieved when checked on 2026-01-06_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2026-01-06: Timeout connecting
    to URL'
publications:
- authors:
  - Belleau F
  - Dumontier M
  doi: 10.1186/2041-1480-2-S1-S1
  id: doi:10.1186/2041-1480-2-S1-S1
  journal: Journal of Biomedical Semantics
  preferred: true
  title: 'Bio2RDF: towards a mashup to build bioinformatics knowledge systems'
  year: '2011'
- authors:
  - Callahan A
  - Cruz-Toledo J
  - Ansell P
  - Dumontier M
  doi: 10.1186/2041-1480-4-S1-S1
  id: doi:10.1186/2041-1480-4-S1-S1
  journal: Journal of Biomedical Semantics
  title: 'Bio2RDF Release 2: Improved Coverage, Interoperability and Provenance of
    Life Science Linked Data'
  year: '2013'
- authors:
  - Dumontier M
  - Callahan A
  - Cruz-Toledo J
  - et al.
  doi: 10.1186/2041-1480-5-14
  id: doi:10.1186/2041-1480-5-14
  journal: Journal of Biomedical Semantics
  title: The Semanticscience Integrated Ontology (SIO) for biomedical research and
    knowledge discovery
  year: '2014'
- authors:
  - Hu W
  - Qiu H
  - Huang J
  - et al.
  doi: 10.1093/database/bax059
  id: doi:10.1093/database/bax059
  journal: Database
  title: 'BioSearch: a semantic search engine for Bio2RDF'
  year: '2017'
- authors:
  - Balaur I
  - Dumontier M
  doi: 10.1186/1471-2105-12-358
  id: doi:10.1186/1471-2105-12-358
  journal: BMC Bioinformatics
  title: 'Chem2Bio2RDF: a semantic framework for linking and data mining chemogenomic
    and systems chemical biology data'
  year: '2011'
repository: https://github.com/MaastrichtU-IDS/bio2rdf
synonyms:
- Bio2RDF
- Linked Biomedical RDF Network
taxon:
- NCBITaxon:1
---
# Bio2RDF (Linked Biomedical RDF Network)

## Overview

Bio2RDF is an open-source, large-scale semantic web integration project that provides the largest network of Linked Data for the life sciences. The project addresses a critical challenge in biomedical research: life scientists need to search for and integrate biological data from a multitude of independent databases with non-standard web and database interfaces and heterogeneous data formats.

Bio2RDF creates a network of coherent linked data by converting over 35 biomedical and life sciences databases into standardized RDF (Resource Description Framework) format, making them accessible through SPARQL endpoints and REST APIs. The project is maintained by Maastricht University's Institute of Data Science and continues to serve as critical infrastructure for biomedical research and knowledge discovery.

## Data Content and Scale

### Database Coverage

Bio2RDF Release 3 (July 2014) encompasses approximately **11 billion RDF triples** across **35+ integrated datasets**, representing one of the largest networks of linked data for life sciences.

**Core Integrated Databases (Full Content):**
- **MGI** (Mouse Genome Informatics) - Mouse genetic data and annotations
- **HGNC** (Human Gene Nomenclature Committee) - Human gene names and symbols
- **KEGG** (Kyoto Encyclopedia of Genes and Genomes) - Pathways and biological processes
- **Entrez Gene/NCBI Gene** - Comprehensive gene information
- **OMIM** (Online Mendelian Inheritance in Man) - Genetic disorders and inheritance
- **Gene Ontology (GO)** - Biological process, cellular component, molecular function annotations
- **OBO** (Open Biomedical Ontologies) - 39+ integrated biomedical ontologies
- **PDB** (Protein Data Bank) - 3D protein structures
- **ChEBI** (Chemical Entities of Biological Interest) - Chemical compound data

**On-Demand Linked Sources:**
- UniProt (protein sequences and annotations)
- Reactome (biochemical pathways)
- Prosite (protein domains and patterns)
- PubMed (biomedical literature abstracts)
- GenBank (nucleotide sequences)
- PubChem (chemical compounds)

**Release 3 Additions (Expanded Coverage):**
- ClinicalTrials.gov (clinical trial information)
- dbSNP (single nucleotide polymorphisms)
- GenAge (aging-related genes)
- GenDR (dietary restriction genes)
- LSR (Life Span Database)
- OrphaNet (orphan diseases)
- SIDER (drug side effects)
- WormBase (C. elegans genomics)
- And 27+ additional linked sources via PharmGKB

### Data Types Covered

Bio2RDF integrates diverse biomedical data types:
- **Genes and Proteins**: Gene sequences, protein structures, functional annotations
- **Chemical Compounds**: Drug information, chemical properties, molecular structures
- **Diseases**: Disease associations, genetic origins, clinical manifestations
- **Pathways**: Metabolic and signaling pathways, biological processes
- **Literature**: PubMed abstracts, citations, publication metadata
- **Genomics**: SNPs, mutations, genomic variations
- **Protein Structures**: 3D coordinates, structural classifications
- **Protein-Protein Interactions**: Interaction networks and relationships
- **Gene-Disease Associations**: Links between genes and clinical phenotypes
- **Drug-Target Interactions**: Pharmacological relationships

## Data Access Methods

### SPARQL Endpoint

**Main SPARQL Endpoint**: https://bio2rdf.org/sparql
- Powered by **OpenLink Virtuoso 7.2.0** (version 07.20.3236)
- Full W3C SPARQL 1.1 protocol support
- CORS-enabled for cross-origin requests
- Text-indexed for full-text search capabilities
- Supports federated queries using SPARQL 1.1 SERVICE keyword

**Query Example:**
```sparql
curl -H "Accept: text/plain" --data-urlencode query@query.sparql https://bio2rdf.org/sparql
```

### REST API

**REST API Endpoint**: Available through dedicated repository
- RESTful interface to Bio2RDF network of data
- Database available at http://dataset.bio2rdf.org/
- Beta version at http://beta.dataset.bio2rdf.org/
- GitHub repository: https://github.com/bio2rdf/bio2rdf-api
- Support for batch operations and on-demand queries

### Data Downloads

**Download Service**: https://download.bio2rdf.org/
- Complete RDF files in multiple serialization formats
- Compressed files for efficient transfer
- Text-indexed Virtuoso triple stores for download and local deployment
- Version-controlled releases with metadata

### Result Formats Supported

Bio2RDF supports multiple output formats for flexibility in data consumption:
- **SPARQL_Results_CSV** - CSV format for spreadsheet applications
- **SPARQL_Results_JSON** - JSON for programmatic access
- **N-Triples** - Line-based RDF format
- **Turtle** - Human-readable RDF syntax
- **N3** (Notation 3) - Extended RDF notation
- **RDF/XML** - XML serialization of RDF

## Data Standards and Technical Architecture

### Semantic Web Technologies

**RDF (Resource Description Framework)**
- Triple-based knowledge representation (Subject-Predicate-Object)
- URI-based entity identification using International Resource Identifiers (IRI)
- Standard format: `http://bio2rdf.org/namespace:id`
- Normalized URIs for consistent entity linking across datasets

**OWL (Web Ontology Language)**
- Dataset types and predicates declared as OWL classes and object properties
- Enables semantic reasoning over implicit knowledge
- Support for subclass relations (rdfs:subClassOf), property equivalence (owl:equivalentProperty)
- Consistency checking and data quality validation

**SPARQL (SPARQL Protocol and RDF Query Language)**
- W3C standard for querying RDF data
- Complex graph pattern matching across linked datasets
- Federated query support across multiple endpoints
- Full-text search integration

### Semanticscience Integrated Ontology (SIO)

Bio2RDF uses the **Semanticscience Integrated Ontology (SIO)** as its primary semantic framework:
- Upper-level ontology providing consistent types and relations
- Provides vocabulary for linked data projects across biological domains
- Covers physical entities, processes, and informational entities
- Includes extensions for chemistry, biology, biochemistry, and bioinformatics
- Freely available under Creative Commons Attribution license

### Data Integration Pipeline

Bio2RDF's ETL (Extract-Transform-Load) process:
1. **Data Extraction**: Download from source databases or APIs
2. **Format Conversion**: Transform from diverse formats (CSV, TSV, RDB, XML, JSON) to RDF
3. **URI Normalization**: Generate consistent IRIs using centralized dataset registry
4. **Semantic Mapping**: Map to SIO ontology and OBO ontologies
5. **RDF Generation**: Produce RDF in multiple serialization formats
6. **Triplestore Loading**: Index and store in OpenLink Virtuoso
7. **Quality Assurance**: Consistency checking and validation

**Transformation Framework**: Modern approach using Common Workflow Language (CWL) for reproducible, scalable data transformation workflows

## Technical Infrastructure

### Core Technologies

- **Triple Store**: OpenLink Virtuoso Open Source Community Edition
- **Scripting Languages**: PHP, Perl, Ruby
- **Containerization**: Docker for deployment and scaling
- **Version Control**: GitHub for code and configuration management
- **Text Indexing**: Full-text search capabilities in Virtuoso

### Architecture Components

**Data Conversion Pipeline**
- Central GitHub repository consolidating ~30 PHP scripts, 1 Java program, 1 Ruby gem
- Common API for IRI generation using centralized dataset registry
- Community contribution model with code review

**SPARQL Endpoint Infrastructure**
- Each dataset has its own SPARQL endpoint powered by Virtuoso
- Federated query support for cross-dataset queries
- Text-indexed for efficient full-text search

**API and Interface Layer**
- REST API for programmatic access
- Web-based browsing and discovery interface
- OpenLink Virtuoso SPARQL Query Editor for interactive queries
- BioSearch semantic search engine for user-friendly discovery

## Use Cases and Applications

### Drug Discovery and Repurposing

- **Drug Repurposing**: Identify existing drugs with new therapeutic applications
- **Target Identification**: Find novel therapeutic targets for diseases
- **Polypharmacology Analysis**: Understand multi-target drug effects
- **Adverse Reaction Mapping**: Identify potential drug side effects through cross-database analysis

### Disease Research and Mechanistic Understanding

- **Disease-Gene-Protein Networks**: Map relationships between genes, proteins, and diseases
- **Pathway Analysis**: Understand biological mechanisms underlying diseases
- **Comorbidity Discovery**: Identify disease associations and relationships
- **Genetic Disorder Understanding**: Link molecular mechanisms to clinical phenotypes

### Complex Biological Queries

**Example Use Cases:**
- Identifying chemicals participating in specific biological processes with protein-encoding interactions
- Exploring implications of transcription factor genes in disease pathways
- Determining protein interaction networks from time-course genomic data
- Mining relational paths in integrated biomedical data for knowledge discovery

### Chemical-Biological Integration

- **Chemical Biology**: Integration of small molecule, target, gene, and pathway information (via Chem2Bio2RDF)
- **Structure-Activity Relationships**: Link chemical properties to biological activities
- **Chemical Genetics**: Connect chemical perturbations to genetic effects

### Research Support

- **Hypothesis Generation**: Generate testable hypotheses through integrated data mining
- **Data Mashups**: Create custom knowledge graphs from Bio2RDF data
- **Knowledge Discovery**: Novel association discovery through linked data exploration
- **Reproducible Research**: Standardized RDF representation supports reproducibility

## Organizational Structure

### Leadership and Affiliations

**Michel Dumontier**
- Scientific Director and Distinguished Professor of Data Science
- Maastricht University Institute of Data Science
- Primary developer and maintainer of Bio2RDF
- Expertise in semantic web, biomedical ontologies, data integration

**François Belleau**
- Founder of the Bio2RDF project
- Original architect of the linked data framework

**Community Contributors**
- Alison Callahan, José Cruz-Toledo, Philippe Rigault (Bio2RDF Release 2)
- Vincent Emonet (Recent contributions)
- Active community of developers and researchers

### Host Institution

**Maastricht University Institute of Data Science (IDS)**
- Primary institutional base for Bio2RDF maintenance and development
- Provides infrastructure and funding support
- Leads ongoing improvements and dataset updates
- GitHub organization: MaastrichtU-IDS

### Community Model

- Open-source, community-driven project
- Distributed development model with contribution mechanisms
- Code review and quality assurance processes
- Welcome to external contributions and dataset additions

## Funding and Support

**Primary Support**: Maastricht University Institute of Data Science

**Development Model**: Supported through:
- University research funding
- Open-source community contributions
- Academic partnerships
- Grant-supported research projects

**Status**: Actively maintained with ongoing updates to datasets, infrastructure improvements, and feature enhancements

## Standards Compliance and Interoperability

- **W3C Standards**: RDF, OWL, SPARQL, HTTP/REST
- **Semantic Web Technologies**: Linked data principles, URI-based identification
- **Biomedical Standards**: Integration with OBO Foundry ontologies
- **Open Science**: CC-BY 3.0 licensed, freely accessible data and code
- **Interoperability**: Support for federated queries and data integration

## Citation and Usage

Bio2RDF data and services are freely accessible through public endpoints with no restrictions. The project is covered under the Creative Commons Attribution 3.0 License.

### Recommended Citation

For Bio2RDF:
"Bio2RDF. Available at: https://bio2rdf.org"

For specific publications:
"Callahan A, Cruz-Toledo J, Ansell P, Dumontier M. Bio2RDF Release 2: Improved Coverage, Interoperability and Provenance of Life Science Linked Data. Journal of Biomedical Semantics. 2013;4(Suppl 1):S1."

### Additional Resources

- **Main Website**: https://bio2rdf.org/
- **SPARQL Endpoint**: https://bio2rdf.org/sparql
- **REST API**: https://github.com/bio2rdf/bio2rdf-api
- **Downloads**: https://download.bio2rdf.org/
- **GitHub Repository**: https://github.com/MaastrichtU-IDS/bio2rdf
- **Scripts Repository**: https://github.com/bio2rdf/bio2rdf-scripts
- **BioSearch Search Engine**: https://biosemantics.org/biosearch
- **SIO Ontology**: https://bioportal.bioontology.org/ontologies/SIO
- **Maastricht University IDS**: https://www.maastrichtuniversity.nl/research/institutes/institute-data-science

Bio2RDF continues to serve as critical infrastructure for integrating biomedical knowledge, enabling researchers worldwide to discover novel relationships, generate hypotheses, and advance biomedical science through standardized semantic web technologies.