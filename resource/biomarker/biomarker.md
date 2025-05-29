---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://glygen.ccrc.uga.edu/frontend/contact
  label: BiomarkerKB Team
description: BiomarkerKB is a Common Fund Data Ecosystem (CFDE) sponsored project
  to develop a knowledgebase that organizes and integrates biomarker data from different
  public sources, providing researchers with comprehensive, integrated access to biomarker
  information.
domains:
- health
- biological systems
- biomedical
homepage_url: https://glygen.ccrc.uga.edu/frontend/home/
id: biomarker
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: BiomarkerKB
products:
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - do
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - cmap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - do
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - cmap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
---
## BiomarkerKB: Comprehensive Biomarker Knowledge Integration

**BiomarkerKB** is a Common Fund Data Ecosystem (CFDE) sponsored project to develop a knowledgebase that organizes and integrates biomarker data from different public sources. It provides researchers with a unified platform for biomarker information access and analysis.

### Overview

BiomarkerKB serves as a centralized resource for biomarker research, facilitating the discovery, validation, and application of biomarkers across various domains including:

- Disease diagnosis and prognosis
- Drug development and personalized medicine
- Health monitoring and disease risk assessment
- Clinical decision support

The knowledgebase is designed to connect heterogeneous biomedical data sources into a unified structure, allowing researchers to explore complex relationships between biomarkers and various biological and clinical entities.

### Key Features

- **Comprehensive Biomarker Information**: Detailed data on biomarkers including molecular characteristics, biological roles, and clinical applications
- **Integrated Data Model**: Standardized representation of biomarker data from diverse sources
- **Relationship Mapping**: Connections between biomarkers and related entities such as diseases, anatomical structures, and biological processes
- **Advanced Search Capabilities**: Multiple query options to find relevant biomarker information
- **Visual Analytics**: Interactive visualizations for exploring biomarker relationships
- **Programmatic Access**: API access for computational analysis and integration with other tools

### Data Sources

BiomarkerKB integrates data from multiple authoritative sources including:

- Clinical biomarker databases
- Research literature
- Molecular and genomic databases
- Pathway and interaction resources
- Disease and phenotype databases

The project is developed by the GlyGen team as part of the NIH Common Fund Data Ecosystem initiative, with a focus on making biomarker data FAIR (Findable, Accessible, Interoperable, and Reusable).