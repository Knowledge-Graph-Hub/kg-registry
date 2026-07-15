---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://biomarkerkb.org/contact
  label: BiomarkerKB Team
creation_date: '2025-05-29T00:00:00Z'
description: BiomarkerKB is a Common Fund Data Ecosystem (CFDE) sponsored project
  to develop a knowledgebase that organizes and integrates biomarker data from different
  public sources, providing researchers with comprehensive, integrated access to biomarker
  information. Note that BiomarkerKB (this resource, id `biomarker`) is the source
  knowledgebase and is distinct from the similarly named BiomarkerKB KG (id
  `biomarkerkg`), a separate knowledge-graph resource built from BiomarkerKB data.
domains:
- biomedical
- biological systems
homepage_url: https://biomarkerkb.org/
id: biomarker
last_modified_date: '2026-07-14T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: BiomarkerKB
products:
- category: GraphicalInterface
  description: Public web portal for BiomarkerKB providing keyword search, filtering,
    data downloads, and interactive graph visualization of biomarker-condition associations.
  format: http
  id: biomarker.portal
  name: BiomarkerKB Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomarker
  product_url: https://biomarkerkb.org/
- category: Product
  description: Downloadable BiomarkerKB datasets, including per-condition datasets and
    full data dumps of curated biomarker-condition associations in JSON format.
  format: json
  id: biomarker.downloads
  name: BiomarkerKB Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomarker
  product_url: https://data.biomarkerkb.org/
- category: ProgrammingInterface
  description: Backend REST API that powers the BiomarkerKB web portal and provides
    programmatic access to biomarker records and the biomarker ID assignment system.
  format: http
  id: biomarker.api
  is_public: true
  name: BiomarkerKB API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomarker
  product_url: https://api.biomarkerkb.org/
- category: GraphProduct
  description: Neo4j knowledge graph built from curated BiomarkerKB data and integrated
    into the CFDE Unified Biomedical Knowledge Graph (UBKG). The initial release comprises
    over 300,000 nodes and 1.2 million edges.
  edge_count: 1200000
  format: neo4j
  id: biomarker.kg
  name: BiomarkerKB Knowledge Graph
  node_count: 300000
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomarker
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: ubkg
  product_url: https://github.com/clinical-biomarkers/Knowledge-Graph
- category: OntologyProduct
  description: The Ontology for Biomarkers of Clinical Interest (OBCI), which formally
    defines biomarkers for diseases, phenotypes, and effects used to structure BiomarkerKB.
  format: owl
  id: biomarker.obci
  name: Ontology for Biomarkers of Clinical Interest (OBCI)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomarker
  product_url: https://github.com/clinical-biomarkers/OBCI
- category: DataModelProduct
  description: The community-developed BiomarkerKB data model (data dictionary and derived
    JSON schema) that harmonizes biomarker knowledge across diverse biological data
    types, following the FDA-NIH BEST biomarker definition.
  format: json
  id: biomarker.datamodel
  name: BiomarkerKB Data Model
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomarker
  product_url: https://github.com/clinical-biomarkers/biomarker-partnership
publications:
- id: doi:10.64898/2026.01.26.701395
  authors:
  - Daniall Masood
  - Mariia Kim
  - Jeet Vora
  - Robel Kahsay
  - Patrick McNeeley
  - Sean Kim
  - Sujeet Kulkarni
  - Darren A. Natale
  - Srinivasan Ramachandran
  - Shakti Gupta
  - Mano Maurya
  - Cristian G. Bologa
  - Thomas S. DeNapoli
  - Vincent T. Metzger
  - Praveen Kumar
  - Nasheath Ahmed
  - John Erol Evangelista
  - Sean C. Kelly
  - Jorge L. Sepulveda
  - Avi Ma'ayan
  - Jonathan Silverstein
  - Deanne M. Taylor
  - Daniel J. Crichton
  - Ashish Mahabal
  - Jeremy J. Yang
  - Christophe G. Lambert
  - Shankar Subramaniam
  - Mike Tiemeyer
  - Rene Ranzinger
  - Raja Mazumder
  doi: 10.64898/2026.01.26.701395
  journal: bioRxiv
  preferred: true
  title: 'BiomarkerKB: An Integrated Knowledgebase Supporting Biomarker-Centric Exploration
    of Biomedical Data'
  year: '2026'
repository: https://github.com/clinical-biomarkers
---
## BiomarkerKB: Comprehensive Biomarker Knowledge Integration

**BiomarkerKB** is a Common Fund Data Ecosystem (CFDE) sponsored project to develop a knowledgebase that organizes and integrates biomarker data from different public sources. It provides researchers with a unified platform for biomarker information access and analysis.

> **Disambiguation:** This resource (`biomarker`) is the BiomarkerKB *knowledgebase*. It should not be confused with **BiomarkerKB KG** (`biomarkerkg`), a separate registry resource for the knowledge-graph representation that is built from BiomarkerKB data. The two projects have very similar names.

### Overview

BiomarkerKB serves as a centralized resource for biomarker research, facilitating the discovery, validation, and application of biomarkers across various domains including:

- Disease diagnosis and prognosis
- Drug development and personalized medicine
- Health monitoring and disease risk assessment
- Clinical decision support

The knowledgebase is designed to connect heterogeneous biomedical data sources into a unified structure, allowing researchers to explore complex relationships between biomarkers and various biological and clinical entities. The initial release integrates more than 200,000 biomarker-condition associations spanning genes, proteins, metabolites, and glycans.

### Key Features

- **Comprehensive Biomarker Information**: Detailed data on biomarkers including molecular characteristics, biological roles, and clinical applications
- **Integrated Data Model**: Standardized representation of biomarker data from diverse sources, following the FDA-NIH BEST biomarker definition
- **Relationship Mapping**: Connections between biomarkers and related entities such as diseases, anatomical structures, and biological processes
- **Advanced Search Capabilities**: Multiple query options to find relevant biomarker information
- **Visual Analytics**: Interactive visualizations for exploring biomarker relationships
- **Programmatic Access**: A public API and downloadable datasets for computational analysis and integration with other tools

### Data Sources

BiomarkerKB integrates biomarker data harmonized from multiple authoritative resources, including OpenTargets, ClinVar, GWAS Catalog, MarkerDB, and OncoMX, as well as CFDE Data Coordinating Centers such as LINCS, Metabolomics Workbench, GlyGen, and EDRN. Curated biomarker data are ingested into a Neo4j knowledge graph and integrated with the CFDE Unified Biomedical Knowledge Graph (UBKG).

The project is developed by the clinical-biomarkers (Biomarker Partnership) team as part of the NIH Common Fund Data Ecosystem initiative, with a focus on making biomarker data FAIR (Findable, Accessible, Interoperable, and Reusable).

## Automated Evaluation

- View the automated evaluation: [biomarker automated evaluation](biomarker_eval_automated.html)
