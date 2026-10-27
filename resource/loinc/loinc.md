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
- genomics
- clinical coding
homepage_url: https://loinc.org/
id: loinc
infores_id: loinc
last_modified_date: '2026-09-23T00:00:00Z'
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
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 503 error when
    accessing file
- category: DocumentationProduct
  description: LOINC Mission, Vision, and Guiding Principles for open terminology
    development (CC-BY 4.0 licensed document)
  format: http
  id: loinc.principles
  name: LOINC Principles Document
  original_source:
  - relation_type: prov:hadPrimarySource
    source: loinc
  product_url: https://loinc.org/principles/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 503 error when
    accessing file
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
    source: cmap
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
    source: cmap
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
- category: Product
  description: The proprietary clinical knowledge graph content itself, comprising
    IMO clinical interface terminology concepts, hierarchies, clinical relationships,
    and cross-maps to standard code systems including ICD-10-CM, ICD-10, SNOMED CT,
    CPT, LOINC, and RxNorm. Delivered under commercial license through the IMO Health
    APIs, EHR integrations, or bulk data agreements.
  format: http
  id: imo-knowledge-graph.data
  name: IMO Health Knowledge Graph Content
  original_source:
  - relation_type: prov:hadPrimarySource
    source: imo-knowledge-graph
  product_url: https://www.imohealth.com/knowledge-graph/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: cpt
  - relation_type: prov:wasDerivedFrom
    source: icd10
  - relation_type: prov:wasDerivedFrom
    source: icd10cm
  - relation_type: prov:wasDerivedFrom
    source: loinc
  - relation_type: prov:wasDerivedFrom
    source: rxnorm
  - relation_type: prov:wasDerivedFrom
    source: snomedct
  warnings:
  - The knowledge graph content is proprietary and is not available as a public bulk
    download. Access requires a commercial agreement with IMO Health.
- category: GraphicalInterface
  description: RadLex Playbook, a lexicon of radiology orderables and imaging procedure
    step names built on RadLex. The Playbook is now harmonized with LOINC as the LOINC/RSNA
    Radiology Playbook.
  format: http
  id: radlex.playbook
  name: RadLex Playbook
  original_source:
  - relation_type: prov:hadPrimarySource
    source: radlex
  - relation_type: prov:hadPrimarySource
    source: loinc
  product_url: https://playbook.radlex.org/
- category: GraphicalInterface
  description: OxO2 web interface for searching and browsing ontology cross-references
    and SSSOM mappings, including asserted mappings from OLS ontologies and curated
    mapping sets, plus inferred cross-set mappings
  format: http
  id: oxo.portal
  name: OxO Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oxo
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: upheno
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: clinvar
  product_url: https://www.ebi.ac.uk/spot/oxo/
- category: ProgrammingInterface
  connection_url: https://www.ebi.ac.uk/spot/oxo/api/v2
  description: OxO2 REST API (OpenAPI 3) for querying mappings, mapping sets, and
    ontologies; supports SSSOM-shaped JSON and SSSOM TSV export of mapping search
    results. Also exposes legacy OxO v1-compatible endpoints.
  format: http
  id: oxo.api
  is_public: true
  name: OxO2 REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oxo
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: upheno
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: clinvar
  product_url: https://www.ebi.ac.uk/spot/oxo/swagger-ui.html
publications:
- authors:
  - Clement J McDonald
  - Stanley M Huff
  - Jeffrey G Suico
  - Gilbert Hill
  - Dennis Leavelle
  - Raymond Aller
  - Arden Forrey
  - Kathy Mercer
  - Georges DeMoor
  - John Hook
  - Warren Williams
  - James Case
  - Pat Maloney
  doi: 10.1373/49.4.624
  id: doi:10.1373/49.4.624
  journal: Clinical Chemistry
  preferred: true
  title: 'LOINC, a Universal Standard for Identifying Laboratory Observations: A 5-Year
    Update'
  year: '2003'
taxon:
- NCBITaxon:9606
warnings:
- LOINC downloads and API require a free account; ensure you cite the specific version
  (e.g., 2.81) when using the terminology.
---
# LOINC

LOINC (Logical Observation Identifiers Names and Codes) standardizes identifiers and names for laboratory tests, clinical measurements, panels, and documents. A free account unlocks downloads of the complete release (currently 2.81) and access to web tooling (SearchLOINC, Hierarchy Browser) and the HL7 FHIR API. LOINC’s mission and guiding principles emphasize openness, accessibility, pragmatics, agility, and diligence in developing global health data standards. Cite the specific version employed in your implementation.