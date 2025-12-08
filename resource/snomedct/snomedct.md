---
activity_status: active
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: info@snomed.org
  - contact_type: url
    value: https://www.snomed.org/contact-us
  label: SNOMED International
- category: Organization
  contact_details:
  - contact_type: email
    value: custserv@nlm.nih.gov
  - contact_type: url
    value: https://www.nlm.nih.gov/healthit/snomedct/index.html
  id: ncbi
  label: National Library of Medicine (NLM)
description: SNOMED CT (Systematized Nomenclature of Medicine Clinical Terms) is the
  most comprehensive, multilingual clinical healthcare terminology in the world. It
  provides a standardized way to represent clinical phrases captured by clinicians
  and enables automatic interpretation of these terms. SNOMED CT includes more than
  360,000 active concepts with unique meanings and formal logic-based definitions
  organized into hierarchies.
domains:
- biomedical
- clinical
- health
homepage_url: https://www.snomed.org/
id: snomedct
infores_id: snomedct
layout: resource_detail
license:
  id: https://www.snomed.org/snomed-ct/get-snomed
  label: SNOMED CT Affiliate License
name: SNOMED CT
products:
- category: OntologyProduct
  description: The biannual release of the US Edition of SNOMED CT, combining content
    from both the US Extension and International releases.
  id: snomedct.us.content
  name: SNOMED CT US Edition
  original_source:
  - snomedct
  product_url: https://download.nlm.nih.gov/mlb/utsauth/USExt/doc_SnomedCT-USEdition-ReleaseNotes_Current_en-US_US1000124_20250301.pdf
- category: OntologyProduct
  description: The monthly release of the International Edition of SNOMED CT, the
    core release from SNOMED International, as RF2 files.
  id: snomedct.international.content
  name: SNOMED CT International Edition
  original_source:
  - snomedct
  product_url: https://download.nlm.nih.gov/umls/kss/IHTSDO2025/IHTSDO20250601/SnomedCT_InternationalRF2_PRODUCTION_20250601T120000Z.zip
- category: MappingProduct
  description: The biannual release of the SNOMED CT to ICD-10-CM Map, which maps
    SNOMED CT concepts to ICD-10-CM codes.
  id: snomedct.icd10cm.map
  name: SNOMED CT to ICD-10-CM Map
  original_source:
  - snomedct
  - icd10
  product_url: https://download.nlm.nih.gov/mlb/utsauth/ICD10CM/SNOMED_CT_to_ICD-10-CM_Resources_20250301.zip
- category: GraphicalInterface
  description: The SNOMED International browser for exploring the SNOMED CT terminology.
  format: http
  id: snomedct.browser
  name: SNOMED CT Browser
  original_source:
  - snomedct
  product_url: https://browser.ihtsdotools.org/
- category: OntologyProduct
  description: A frequently used subset of SNOMED CT concepts for nursing documentation
    in electronic health records. August 2017 release.
  id: snomedct.nursing
  name: SNOMED CT Nursing Problem List Subset
  original_source:
  - snomedct
  product_url: https://download.nlm.nih.gov/mlb/utsauth/NursingProblemListSubset/SNOMEDCT_Nursing_201708.csv
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
  - doid
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
  - connectivitymap
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
  - sckan
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
  - doid
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
  - connectivitymap
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
  - sckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - doid
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: cancer-genome-interpreter.clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - doid
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: MappingProduct
  description: Concept mappings between different terminology systems
  format: csv
  id: athena.mappings
  name: Athena Concept Mappings
  original_source:
  - snomedct
  - icd10
  - icd10cm
  - mesh
  - loinc
  - cdiscvocab
  - ciel
  product_url: https://athena.ohdsi.org/search-terms/start
  secondary_source:
  - athena
  warnings:
  - File was not able to be retrieved when checked on 2025-12-08_ Error connecting
    to URL_ Exceeded 30 redirects.
  - File was not able to be retrieved when checked on 2025-12-07_ Error connecting
    to URL_ Exceeded 30 redirects.
  - 'File was not able to be retrieved when checked on 2025-12-08: Error connecting
    to URL: Exceeded 30 redirects.'
repository: https://browser.ihtsdotools.org/
---
# SNOMED CT

SNOMED CT (Systematized Nomenclature of Medicine Clinical Terms) is the most comprehensive, multilingual clinical healthcare terminology in the world. It serves as a standardized vocabulary for clinical documentation and enables consistent representation of clinical content in electronic health records.

## Overview

SNOMED CT provides a systematic, computer-processable collection of medical terms covering areas such as:
- Diseases
- Findings
- Procedures
- Microorganisms
- Substances
- Body structures
- Physical objects
- Physical forces
- Events
- Social contexts

The terminology contains more than 360,000 active concepts with unique meanings and formal logic-based definitions organized into hierarchies. SNOMED CT content is represented using three types of components:

1. **Concepts** - Each concept represents a unique clinical meaning identified by a unique, numeric SNOMED CT identifier.
2. **Descriptions** - Human-readable terms associated with concepts, including Fully Specified Names (FSN) and synonyms.
3. **Relationships** - Logical connections between concepts that define their meaning in a computer-processable way.

## Distribution and Licensing

SNOMED CT is owned, maintained, and distributed by SNOMED International, a not-for-profit association. As the United States National Release Center for SNOMED CT, the National Library of Medicine (NLM) provides SNOMED CT data and resources to licensees of the NLM UMLS Metathesaurus.

The SNOMED CT US Edition is released biannually (March and September) and combines content from both the US Extension and the International releases. The International Edition follows a monthly release cycle. Access to SNOMED CT requires an Affiliate License, which is free in SNOMED International Member territories (including the United States), in low-income countries, and for qualifying research projects.

## Applications and Benefits

SNOMED CT is designated as a standard for electronic exchange of clinical health information in many countries and is required in interoperability specifications of the U.S. Healthcare Information Technology Standards Panel. It is used in various clinical applications including:

- Electronic health records
- Clinical decision support
- Clinical and translational research
- Public health reporting
- Healthcare analytics
- Knowledge representation

Benefits include:
- Enabling consistent recording of clinical information
- Supporting real-time clinical decision support
- Facilitating interoperability and data exchange
- Enabling more accurate retrieval of patient data
- Supporting multilingual use through international translations
- Improving population health monitoring and research