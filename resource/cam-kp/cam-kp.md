---
activity_status: inactive
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: balhoff@renci.org
  label: Jim Balhoff
  orcid: 0000-0001-7695-6090
- category: Organization
  contact_details:
  - contact_type: url
    value: https://renci.org/
  id: renci
  label: RENCI (Renaissance Computing Institute)
creation_date: '2025-12-18T00:00:00Z'
description: CAM-KP (Causal Activity Models Knowledge Provider) is a web service knowledge
  graph that integrates causal biological and chemical models from Gene Ontology,
  Reactome, and Comparative Toxicogenomics Database (CTD) into a unified, semantically
  rich platform. It provides access to structured biomedical knowledge through SPARQL
  and TRAPI-compliant REST APIs, supporting hypothesis generation, drug discovery,
  and environmental health research.
domains:
- health
- pathways
homepage_url: https://automat.renci.org/#/cam-kp
id: cam-kp
infores_id: cam-kp
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License (Repository); Public Domain (Data)
name: CAM-KP (Causal Activity Models Knowledge Provider)
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for complex semantic queries on the RDF triplestore
    containing causal activity models, ontologies, and integrated biomedical knowledge
  format: http
  id: cam-kp.sparql
  is_public: true
  name: CAM-KP SPARQL Endpoint
  product_url: https://stars-app.renci.org/cam/sparql
- category: ProgrammingInterface
  description: TRAPI-compliant REST API for programmatic access to causal knowledge
    graphs supporting Translator ecosystem integration and federated querying
  format: http
  id: cam-kp.api
  is_public: true
  name: CAM-KP REST API
  product_url: https://cam-kp-api-dev.renci.org/1.2.0/query
- category: GraphicalInterface
  description: Interactive knowledge provider interface within RENCI's Automat platform
    for discovering and integrating CAM-KP with other biomedical data sources
  format: http
  id: cam-kp.automat
  is_public: true
  name: CAM-KP on Automat
  product_url: https://automat.renci.org/#/cam-kp
- category: Product
  description: Causal Activity Model graphs automatically generated from Reactome
    pathways using the Pathways2GO tool, translating pathway reactions to causal relationships
  id: cam-kp.reactome-cams
  name: Reactome Pathway CAMs
  original_source:
  - reactome
- category: Product
  description: Gene Ontology Causal Activity Model (GO-CAM) annotations manually curated
    by Gene Ontology biocurators linking genes, proteins, and biological processes
  id: cam-kp.go-cams
  name: Gene Ontology CAMs
  original_source:
  - gene-ontology
- category: Product
  description: Chemical-gene interaction models and toxicological pathways derived
    from the Comparative Toxicogenomics Database (CTD) covering 17,700+ chemicals
    and 55,400 genes
  id: cam-kp.ctd-interactions
  name: CTD Chemical-Gene Models
  original_source:
  - ctd
- category: DocumentationProduct
  description: Comprehensive API documentation, SPARQL endpoint documentation, and
    developer guides for querying and integrating CAM-KP
  format: http
  id: cam-kp.documentation
  is_public: true
  name: CAM-KP Documentation
  product_url: https://github.com/ExposuresProvider/cam-kp-api/wiki
publications:
- authors:
  - Balhoff JP
  - Bizon C
  - Carlson J
  - Fecho K
  - Fink EL
  - Gorow JS
  - Graham TGW
  - Hanna DE
  - Henricks CJ
  - Hoyt CT
  - Imamovic-Tomasovic M
  - Jacobs JM
  - Koslovsky MD
  - Lyzenga Y
  - Nagel R
  - Rasmussen JE
  - Robin A
  - Sullivan R
  - Wagner AH
  - Whetzel PL
  - Williams JA
  doi: 10.48550/arXiv.2004.01269
  id: arXiv:2004.01269
  journal: arXiv
  preferred: true
  title: A Biomedical Knowledge Graph System to Propose Mechanistic Hypotheses for
    Real-World Environmental Health Observations
  year: '2020'
- authors:
  - Balhoff JP
  - Bizon C
  - Carlson J
  - Fecho K
  - Fink EL
  - Gorow JS
  doi: 10.48550/arXiv.2105.04728
  id: arXiv:2105.04728
  journal: JMIR Medical Informatics
  title: A Biomedical Knowledge Graph System to Propose Mechanistic Hypotheses for
    Real-World Environmental Health Observations
  year: '2021'
- authors:
  - Davis AP
  - Wiegers TC
  - Johnson RJ
  doi: 10.1093/nar/gky1209
  id: doi:10.1093/nar/gky1209
  journal: Nucleic Acids Research
  title: 'The Comparative Toxicogenomics Database: update 2023'
  year: '2023'
- authors:
  - Davis AP
  - Wiegers TC
  - Johnson RJ
  doi: 10.1093/nar/gkaq891
  id: doi:10.1093/nar/gkaq891
  journal: Nucleic Acids Research
  title: 'The Comparative Toxicogenomics Database: a knowledgebase and discovery tool
    for chemical-gene-disease networks'
  year: '2020'
repository: https://github.com/ExposuresProvider/cam-kp-api
taxon:
- NCBITaxon:1
---
# CAM-KP (Causal Activity Models Knowledge Provider)

## Overview

CAM-KP (Causal Activity Models Knowledge Provider) is a web service knowledge graph that provides access to integrated causal biological and chemical models. As part of the NCATS Biomedical Data Translator initiative, CAM-KP serves as a critical infrastructure component for connecting siloed biomedical datasets through standardized semantic representations.

The knowledge graph integrates multiple types of causal models—including manually curated Gene Ontology Causal Activity Models (GO-CAMs), automatically derived Reactome pathway models, and chemical-gene interactions from the Comparative Toxicogenomics Database (CTD)—into a unified, OWL-based semantic platform accessible via both SPARQL and TRAPI-compliant REST APIs.

## Data Content and Scale

### Model Types and Coverage

CAM-KP combines three primary sources of causal models:

**Gene Ontology Causal Activity Models (GO-CAMs)**
- Manually annotated by Gene Ontology expert biocurators
- Over 750,000 experimental gene annotations from 150,000+ distinct scientific publications
- Link genes, gene products, and biological processes in causal networks
- Structured using Gene Ontology controlled vocabularies

**Reactome Pathway CAMs**
- Complete set of normal human Reactome pathways converted to GO-CAM representation
- Reactions translated to gene product activities
- Causal relations inferred between molecular activities
- Enables pathway reasoning through GO-CAM framework

**Comparative Toxicogenomics Database (CTD) Interactions**
- 3.8+ million direct chemical-gene interactions
- 17,700+ chemicals covered
- 55,400 genes represented
- 7,200 diseases linked to chemical exposures
- 214,000+ documented exposures

### Knowledge Representation

- **RDF Triplestore**: Triple format knowledge graph with semantic richness
- **OWL 2 Ontology Layer**: Enables formal semantic reasoning over implicit knowledge
- **Merged Bio-Ontology**: Integrated vocabulary from 39+ OBO Library ontologies
- **Precomputed Inferences**: OWL-based reasoning results stored for efficient query response

## Data Access and Formats

### Query Interfaces

**SPARQL Endpoint**
- Direct semantic queries: https://stars-app.renci.org/cam/sparql
- Full W3C SPARQL support
- Complex graph pattern matching over RDF triples
- Suitable for advanced semantic queries

**TRAPI-Compliant REST API**
- RESTful web service: https://cam-kp-api-dev.renci.org/1.2.0/query
- JSON request/response format
- Standardized Translator Reasoner API (TRAPI) compliance
- Enables federated querying across Translator ecosystem

**Automat Integration**
- Discovery and integration interface: https://automat.renci.org/#/cam-kp
- Part of broader RENCI knowledge provider integration platform
- Simplified access for researchers unfamiliar with APIs

### Data Formats

**Core Semantic Standards:**
- **RDF (Resource Description Framework)** - Triple-based knowledge representation
- **OWL 2 (Web Ontology Language)** - Semantic expressiveness and reasoning
- **SPARQL** - Graph query language
- **JSON** - API response format with JSON-LD context
- **TRAPI** - Translator Reasoner API standard

**Data Organization:**
- **Biolink Model** - Universal schema for biomedical knowledge graphs with standardized entity types and relationships
- **OBO Format** - Integration with 39+ Open Biomedical Ontologies
- **CURIE Representation** - Compact URIs for cross-database entity identification

## Data Sources and Integration

### Primary Contributors

**Gene Ontology Consortium**
- Gene Ontology Causal Activity Models (GO-CAMs)
- Expert biocurator annotations
- Controlled vocabularies and structured annotations

**Reactome Database**
- Entire set of human biochemical pathway models
- Converted to GO-CAM representation via Pathways2GO tool
- Enables systems-level biological reasoning

**Comparative Toxicogenomics Database (CTD)**
- Manually curated chemical-gene interactions
- Chemical-disease associations
- Gene-disease relationships
- Cross-species data integration

**OBO Foundry Ontologies**
- Basic Formal Ontology (BFO) for foundational concepts
- Relation Ontology for relationship definitions
- Domain-specific ontologies for specialized knowledge
- Total of 39+ integrated OBO ontologies

### Data Integration Pipeline

The cam-pipeline ETL system processes raw data through:
1. Data extraction from source databases
2. Standardization to Darwin Core terms where applicable
3. RDF/OWL conversion
4. Ontology alignment and semantic harmonization
5. OWL 2 inference and reasoning
6. Triplestore loading and indexing

## Technical Architecture

### System Components

**Data Ingestion**
- cam-pipeline: ETL framework for automated data loading
- Pathways2GO: Tool for converting Reactome pathways to GO-CAM format
- Bulk loaders for Gene Ontology and CTD data

**Knowledge Representation Layer**
- RDF triplestore backend
- OWL 2 ontology with precomputed reasoning
- Integrated vocabulary from 39+ OBO ontologies
- Support for semantic web standards

**Query Infrastructure**
- SPARQL endpoint for direct semantic queries
- TRAPI-compliant REST API for standardized access
- JSON-LD context management for CURIE expansion
- Support for federated query composition

**Integration**
- NCATS Translator ecosystem participation
- Biolink Model compliance
- OpenAPI/Swagger documentation
- Automat platform integration

### Technologies Used

- **Semantic Web**: RDF, OWL, SPARQL
- **Knowledge Representation**: OBO ontologies, Gene Ontology, Biolink Model
- **API Standards**: TRAPI (Translator Reasoner API), OpenAPI
- **Infrastructure**: RENCI Stars platform hosting
- **Version Control**: GitHub repositories

## Use Cases and Applications

### Research Applications

**Mechanistic Hypothesis Generation**
- Propose molecular pathways connecting chemicals to disease
- Identify target pathways for drug discovery
- Support environmental health research with mechanistic understanding

**Drug Discovery and Repurposing**
- Identify potential therapeutic targets
- Discover new applications for existing drugs
- Generate biomedical hypotheses through integrated reasoning

**Chemical Safety Assessment**
- Understand toxicological mechanisms of action
- Predict adverse outcomes from chemical exposures
- Support regulatory decision-making

**Translational Research**
- Bridge molecular discoveries to clinical applications
- Generate testable hypotheses for experimental validation
- Support precision medicine research

**Environmental Health Research**
- Link environmental exposures to health outcomes
- Identify vulnerable populations and biomarkers
- Support exposure science studies

**Systems Biology**
- Model complex biological processes in causal networks
- Connect molecular, cellular, and organism-level effects
- Support hypothesis-driven research

### Integration with Other Resources

CAM-KP operates as part of the NCATS Data Translator ecosystem, integrating with:
- **ICEES** (Integrated Clinical and Environmental Exposures Service) for clinical-environmental data
- **Gene Ontology** for curated biological annotations
- **Reactome** for pathway knowledge
- **CTD** for chemical-gene-disease associations
- Other NCATS Translator Knowledge Providers for federated queries

## Organizational Structure

### Leadership

**Jim Balhoff** (RENCI, UNC Chapel Hill)
- Assistant Director of Analytics & Data Science
- Expertise in bio-ontologies, semantic web, data integration, bioinformatics
- ORCID: 0000-0001-7695-6090

**Stephen Edwards** (RTI International)
- Director at US Environmental Protection Agency
- Expertise in data mining, knowledgebase design, ontology-based modeling

### Host Institution

**RENCI (Renaissance Computing Institute)**
- Part of University of North Carolina at Chapel Hill
- Provides infrastructure, hosting, and technical development
- Participates in NCATS Biomedical Data Translator program

### Collaborating Organizations

- **Gene Ontology Consortium** - GO-CAM curation and maintenance
- **RTI International** - Development and environmental expertise
- **NCATS (National Center for Advancing Translational Sciences)** - Funding and program oversight

## Funding and Support

**Primary Funder**: National Center for Advancing Translational Sciences (NCATS), National Institutes of Health (NIH)

**Program**: NCATS Biomedical Data Translator Initiative
- Launched in 2016 as multiyear, iterative program
- Supports nationwide biomedical research data integration
- Consortium funding: approximately $13.5 million in FY 2020
- NCATS FY 2024 budget: $928,323,000 overall

**Status**: Repository archived May 23, 2024 (read-only); service continues to operate with active maintenance and support

## Citation and Usage

CAM-KP data and services are freely accessible through public endpoints with no licensing restrictions. Data from integrated sources (Gene Ontology, Reactome, CTD) follow their respective open licenses (typically CC-BY or CC0).

### Recommended Citation

For CAM-KP:
"CAM-KP (Causal Activity Models Knowledge Provider). Available at: https://automat.renci.org/#/cam-kp"

For the foundational work:
"Balhoff JP, Bizon C, Carlson J, et al. A Biomedical Knowledge Graph System to Propose Mechanistic Hypotheses for Real-World Environmental Health Observations. JMIR Medical Informatics. 2021;9(7):e26714."

### Additional Resources

- **Main Access**: https://automat.renci.org/#/cam-kp
- **SPARQL Endpoint**: https://stars-app.renci.org/cam/sparql
- **REST API**: https://cam-kp-api-dev.renci.org/1.2.0/query
- **Documentation**: https://github.com/ExposuresProvider/cam-kp-api/wiki
- **GitHub Repository**: https://github.com/ExposuresProvider/cam-kp-api
- **Data Pipeline**: https://github.com/ExposuresProvider/cam-pipeline
- **Contact**: Jim Balhoff (balhoff@renci.org)

CAM-KP continues to serve as a critical infrastructure component for the NCATS Biomedical Data Translator, enabling researchers to generate mechanistic hypotheses, support drug discovery efforts, and advance environmental health research through integrated access to curated biomedical knowledge.

## Automated Evaluation

- View the automated evaluation: [cam-kp automated evaluation](cam-kp_eval_automated.html)
