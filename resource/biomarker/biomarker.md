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
  information.
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
  description: Downloadable BiomarkerKB datasets, including per-condition datasets
    and full data dumps of curated biomarker-condition associations in JSON format.
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
  product_url: https://github.com/clinical-biomarkers/Knowledge-Graph
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: ubkg
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
  description: The community-developed BiomarkerKB data model (data dictionary and
    derived JSON schema) that harmonizes biomarker knowledge across diverse biological
    data types, following the FDA-NIH BEST biomarker definition.
  format: json
  id: biomarker.datamodel
  name: BiomarkerKB Data Model
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomarker
  product_url: https://github.com/clinical-biomarkers/biomarker-partnership
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
publications:
- authors:
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
  id: doi:10.64898/2026.01.26.701395
  journal: bioRxiv
  preferred: true
  title: 'BiomarkerKB: An Integrated Knowledgebase Supporting Biomarker-Centric Exploration
    of Biomedical Data'
  year: '2026'
repository: https://github.com/clinical-biomarkers
---
## BiomarkerKB: Comprehensive Biomarker Knowledge Integration

**BiomarkerKB** is a Common Fund Data Ecosystem (CFDE) sponsored project to develop a knowledgebase that organizes and integrates biomarker data from different public sources. It provides researchers with a unified platform for biomarker information access and analysis.

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