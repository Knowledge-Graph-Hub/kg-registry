---
activity_status: active
category: DataModel
collection:
- omop
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://loinc.org/contact/
  label: Regenstrief Institute (LOINC)
creation_date: '2025-06-04T00:00:00Z'
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
last_modified_date: '2026-04-10T00:00:00Z'
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
  - relation_type: prov:hadPrimarySource
    source: loinc
  product_url: https://loinc.org/search/
- category: ProgrammingInterface
  description: HL7 FHIR-based API providing programmatic access to LOINC terminology
    content (requires free LOINC login)
  format: http
  id: loinc.api.fhir
  is_public: false
  name: LOINC FHIR API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: loinc
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
  - relation_type: prov:hadPrimarySource
    source: loinc
  product_url: https://loinc.org/download/loinc-complete/
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-26: HTTP 503 error
    when accessing file'
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 503 error when
    accessing file
- category: DataModelProduct
  description: Archive of past LOINC releases for version-specific implementations
  format: mixed
  id: loinc.archive
  name: LOINC Release Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: loinc
  product_url: https://loinc.org/downloads/archive/
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-26: HTTP 503 error
    when accessing file'
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 503 error when
    accessing file
- category: DocumentationProduct
  description: LOINC Mission, Vision, and Guiding Principles for open terminology
    development (CC-BY 4.0 licensed document)
  id: loinc.principles
  name: LOINC Principles Document
  original_source:
  - relation_type: prov:hadPrimarySource
    source: loinc
  product_url: https://loinc.org/principles/
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-26: HTTP 503 error
    when accessing file'
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 503 error when
    accessing file
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
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
- category: MappingProduct
  description: Concept mappings between different terminology systems
  format: csv
  id: athena.mappings
  name: Athena Concept Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: athena
  - relation_type: prov:hadPrimarySource
    source: cdiscvocab
  - relation_type: prov:hadPrimarySource
    source: ciel
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: icd10cm
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: snomedct
  product_url: https://athena.ohdsi.org/search-terms/start
  warnings:
  - Athena mapping exports are accessed through the authenticated Athena web application;
    stable direct public file URLs are not exposed.
- category: Product
  description: Downloadable standardized vocabulary bundles for OMOP CDM assembled
    through the authenticated Athena web application
  format: csv
  id: athena.vocabularies
  name: Athena Vocabulary Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: athena
  - relation_type: prov:hadPrimarySource
    source: cdiscvocab
  - relation_type: prov:hadPrimarySource
    source: ciel
  - relation_type: prov:hadPrimarySource
    source: gemscript
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: icd10cm
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: medispan-gpi
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ndcd
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: snomedct
  product_url: https://athena.ohdsi.org/vocabulary/list
  warnings:
  - Athena vocabulary downloads are prepared through the logged-in web application;
    stable direct public file URLs are not exposed.
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
taxon:
- NCBITaxon:9606
warnings:
- LOINC downloads and API require a free account; ensure you cite the specific version
  (e.g., 2.81) when using the terminology.
---
# LOINC

LOINC (Logical Observation Identifiers Names and Codes) standardizes identifiers and names for laboratory tests, clinical measurements, panels, and documents. A free account unlocks downloads of the complete release (currently 2.81) and access to web tooling (SearchLOINC, Hierarchy Browser) and the HL7 FHIR API. LOINC’s mission and guiding principles emphasize openness, accessibility, pragmatics, agility, and diligence in developing global health data standards. Cite the specific version employed in your implementation.