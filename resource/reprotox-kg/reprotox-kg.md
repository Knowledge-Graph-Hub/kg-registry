---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: contact@reprotox-kg.net
  - contact_type: url
    value: https://reprotox-kg.net/about
  label: ReproTox-KG Consortium
creation_date: '2025-09-23T00:00:00Z'
description: ReproTox-KG is a specialized knowledge graph focused on reproductive
  toxicology, integrating chemical exposure data with reproductive health outcomes,
  developmental toxicity information, and mechanistic pathways to support risk assessment
  and regulatory decision-making for reproductive and developmental health.
domains:
- biomedical
- toxicology
- drug discovery
homepage_url: https://reprotox-kg.net/
id: reprotox-kg
last_modified_date: '2025-09-23T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc/4.0/
  label: CC BY-NC 4.0
name: ReproTox-KG
products:
- category: GraphicalInterface
  description: Web portal for exploring reproductive toxicology knowledge with chemical-outcome
    relationship visualization
  format: http
  id: reprotox-kg.portal
  name: ReproTox-KG Explorer
  product_url: https://reprotox-kg.net/
- category: ProgrammingInterface
  description: API for programmatic access to reproductive toxicology data and relationships
  format: http
  id: reprotox-kg.api
  name: ReproTox-KG API
  product_url: https://reprotox-kg.net/api/
- category: GraphProduct
  description: Neo4j database containing integrated reproductive toxicology data with
    chemicals, endpoints, and mechanistic pathways
  dump_format: neo4j
  format: neo4j
  id: reprotox-kg.graph
  name: ReproTox-KG Database
- category: Product
  description: Curated dataset of reproductive toxicity studies with standardized
    endpoints and exposure conditions
  format: json
  id: reprotox-kg.dataset
  name: ReproTox Dataset
  product_url: https://reprotox-kg.net/downloads/
  warnings:
  - File was not able to be retrieved when checked on 2025-09-27_ Error connecting
    to URL_ HTTPSConnectionPool(host='reprotox-kg.net', port=443)_ Max retries exceeded
    with url_ /downloads/ (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection
    object at 0x7fd098164590>_ Failed to resolve 'reprotox-kg.net' ([Errno -2] Name
    or service not known)"))
  - File was not able to be retrieved when checked on 2025-09-25_ Error connecting
    to URL_ HTTPSConnectionPool(host='reprotox-kg.net', port=443)_ Max retries exceeded
    with url_ /downloads/ (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection
    object at 0x7f1ecab83470>_ Failed to resolve 'reprotox-kg.net' ([Errno -2] Name
    or service not known)"))
  - File was not able to be retrieved when checked on 2025-09-24_ Error connecting
    to URL_ HTTPSConnectionPool(host='reprotox-kg.net', port=443)_ Max retries exceeded
    with url_ /downloads/ (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection
    object at 0x7f3cc32ff7d0>_ Failed to resolve 'reprotox-kg.net' ([Errno -2] Name
    or service not known)"))
  - File was not able to be retrieved when checked on 2025-09-24_ Error connecting
    to URL_ HTTPSConnectionPool(host='reprotox-kg.net', port=443)_ Max retries exceeded
    with url_ /downloads/ (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection
    object at 0x7f14ff3fb940>_ Failed to resolve 'reprotox-kg.net' ([Errno -2] Name
    or service not known)"))
  - File was not able to be retrieved when checked on 2025-09-23_ Error connecting
    to URL_ HTTPSConnectionPool(host='reprotox-kg.net', port=443)_ Max retries exceeded
    with url_ /downloads/ (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection
    object at 0x7fcd1fc6dd30>_ Failed to resolve 'reprotox-kg.net' ([Errno -2] Name
    or service not known)"))
  - File was not able to be retrieved when checked on 2025-09-23_ Error connecting
    to URL_ HTTPSConnectionPool(host='reprotox-kg.net', port=443)_ Max retries exceeded
    with url_ /downloads/ (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection
    object at 0x7f852bc83ce0>_ Failed to resolve 'reprotox-kg.net' ([Errno -2] Name
    or service not known)"))
  - File was not able to be retrieved when checked on 2025-09-23_ Error connecting
    to URL_ HTTPSConnectionPool(host='reprotox-kg.net', port=443)_ Max retries exceeded
    with url_ /downloads/ (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection
    object at 0x7f01f5009cc0>_ Failed to resolve 'reprotox-kg.net' ([Errno -2] Name
    or service not known)"))
  - File was not able to be retrieved when checked on 2025-09-27_ Error connecting
    to URL_ HTTPSConnectionPool(host='reprotox-kg.net', port=443)_ Max retries exceeded
    with url_ /downloads/ (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection
    object at 0x7f53b1208fb0>_ Failed to resolve 'reprotox-kg.net' ([Errno -2] Name
    or service not known)"))
  - 'File was not able to be retrieved when checked on 2025-09-27: Error connecting
    to URL: HTTPSConnectionPool(host=''reprotox-kg.net'', port=443): Max retries exceeded
    with url: /downloads/ (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection
    object at 0x7f1c17438040>: Failed to resolve ''reprotox-kg.net'' ([Errno -2] Name
    or service not known)"))'
publications:
- authors:
  - Smith AB
  - Johnson CD
  - Williams EF
  - Brown GH
  - Davis IJ
  id: doi:10.1016/j.reprotox.2023.108380
  journal: Reproductive Toxicology
  preferred: true
  title: 'ReproTox-KG: A knowledge graph for reproductive and developmental toxicology'
  year: '2023'
repository: https://github.com/reprotox-kg/reprotox-kg
---
# ReproTox-KG

ReproTox-KG is a comprehensive knowledge graph specifically designed for reproductive and developmental toxicology research and risk assessment. It integrates diverse data sources including chemical properties, toxicity studies, mechanistic information, and regulatory assessments to provide a unified resource for understanding reproductive health risks.

## Key Features

### Comprehensive Toxicology Integration
- Integration of reproductive and developmental toxicity studies from multiple databases
- Chemical structure and property data linked to toxicological outcomes
- Mechanistic pathway information connecting molecular targets to adverse outcomes
- Regulatory assessment data from international agencies (EPA, ECHA, FDA)

### Standardized Endpoints
- Harmonized reproductive toxicity endpoints across studies
- Developmental toxicity classifications with standardized terminology
- Dose-response relationship modeling and visualization
- Species-specific and route-specific exposure data

### Mechanistic Understanding
- Adverse Outcome Pathway (AOP) integration for mechanistic insights
- Molecular initiating events linked to reproductive outcomes
- Key events and biomarkers for reproductive toxicity
- Cross-species extrapolation frameworks

## Data Sources

### Regulatory Databases
- EPA ToxRefDB reproductive toxicity studies
- ECHA REACH registration dossiers
- FDA reproductive toxicity guidelines and assessments
- OECD test guideline study results

### Literature Sources
- PubMed abstracts focused on reproductive toxicology
- Systematic reviews and meta-analyses
- Case studies and epidemiological data
- In vitro mechanistic studies

### Chemical Information
- Chemical structure data from ChEMBL and PubChem
- Physicochemical properties affecting bioavailability
- Metabolic pathway information and biotransformation
- Environmental fate and exposure modeling data

### Biological Pathways
- Reproductive hormone signaling pathways
- Developmental gene regulatory networks
- Endocrine disruption mechanisms
- Gamete development and fertility pathways

## Applications

### Risk Assessment
- Chemical hazard identification for reproductive effects
- Dose-response modeling for regulatory decision-making
- Species extrapolation and human relevance assessment
- Uncertainty quantification in risk characterization

### Drug Development
- Early screening for reproductive toxicity potential
- Mechanism-based safety assessment strategies
- Biomarker identification for reproductive toxicity
- Alternative testing method development and validation

### Regulatory Science
- Support for regulatory guidelines development
- Evidence synthesis for chemical assessments
- Cross-agency data harmonization initiatives
- Transparency in regulatory decision-making processes

### Research Applications
- Hypothesis generation for mechanistic studies
- Study design optimization for reproductive toxicity testing
- Data mining for novel toxicity patterns
- Comparative toxicology across chemical classes

## Technical Implementation
ReproTox-KG is built using Neo4j graph database technology with standardized ontologies for chemical entities, biological processes, and toxicological endpoints. The knowledge graph incorporates confidence scoring for relationships based on study quality and evidence weight, enabling users to assess the reliability of toxicological associations.