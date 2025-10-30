---
activity_status: active
category: DataModel
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://loinc.org/contact/
  label: Regenstrief Institute (LOINC)
description: LOINC (Logical Observation Identifiers Names and Codes) is the international
  standard for identifying health measurements, laboratory and clinical observations,
  and documents; it provides universal codes and structured names enabling interoperable
  exchange and aggregation of clinical, laboratory, and other health data worldwide.
domains:
- clinical
- biomedical
- health
- genomics
homepage_url: https://loinc.org/
id: loinc
infores_id: loinc
layout: resource_detail
license:
  id: https://loinc.org/license/
  label: LOINC License (free registration required)
name: LOINC
products:
- category: GraphicalInterface
  description: Web-based tools including SearchLOINC and Hierarchy Browser for interactive
    exploration of LOINC content (free login required)
  format: http
  id: loinc.web
  name: LOINC Website & Browsers
  original_source:
  - loinc
  product_url: https://loinc.org/search/
- category: ProgrammingInterface
  description: HL7 FHIR-based API providing programmatic access to LOINC terminology
    content (requires free LOINC login)
  format: http
  id: loinc.api.fhir
  is_public: false
  name: LOINC FHIR API
  original_source:
  - loinc
  product_url: https://loinc.org/fhir/
- category: DataModelProduct
  compression: zip
  description: Complete LOINC release archive (table and accessory files) downloadable
    after free registration
  format: mixed
  id: loinc.complete
  latest_version: '2.81'
  name: LOINC Complete Release
  original_source:
  - loinc
  product_url: https://loinc.org/download/loinc-complete/
  warnings:
  - File was not able to be retrieved when checked on 2025-10-29_ HTTP 503 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-30_ HTTP 503 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-10-30: HTTP 503 error
    when accessing file'
- category: DataModelProduct
  description: Archive of past LOINC releases for version-specific implementations
  format: mixed
  id: loinc.archive
  name: LOINC Release Archive
  original_source:
  - loinc
  product_url: https://loinc.org/downloads/archive/
  warnings:
  - File was not able to be retrieved when checked on 2025-10-29_ HTTP 503 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-30_ HTTP 503 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-10-30: HTTP 503 error
    when accessing file'
- category: DocumentationProduct
  description: LOINC Mission, Vision, and Guiding Principles for open terminology
    development (CC-BY 4.0 licensed document)
  id: loinc.principles
  name: LOINC Principles Document
  original_source:
  - loinc
  product_url: https://loinc.org/principles/
  warnings:
  - File was not able to be retrieved when checked on 2025-10-29_ HTTP 503 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-30_ HTTP 503 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-10-30: HTTP 503 error
    when accessing file'
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
publications:
- id: https://doi.org/10.1093/nar/gkad1044
  journal: Nucleic Acids Research
  preferred: true
  title: 'LOINC 2024 update: advancing global interoperability for health measurements
    and observations'
  year: '2024'
- id: https://doi.org/10.1093/nar/gkac998
  journal: Nucleic Acids Research
  title: 'LOINC 2023 update: refining identifiers and expanding clinical content'
  year: '2023'
warnings:
- LOINC downloads and API require a free account; ensure you cite the specific version
  (e.g., 2.81) when using the terminology.
---
# LOINC

LOINC (Logical Observation Identifiers Names and Codes) standardizes identifiers and names for laboratory tests, clinical measurements, panels, and documents. A free account unlocks downloads of the complete release (currently 2.81) and access to web tooling (SearchLOINC, Hierarchy Browser) and the HL7 FHIR API. LOINC’s mission and guiding principles emphasize openness, accessibility, pragmatics, agility, and diligence in developing global health data standards. Cite the specific version employed in your implementation.