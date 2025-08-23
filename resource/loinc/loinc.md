---
activity_status: active
category: DataModel
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://loinc.org/contact/"
    label: Regenstrief Institute (LOINC)
description: LOINC (Logical Observation Identifiers Names and Codes) is the international standard for identifying health measurements, laboratory and clinical observations, and documents; it provides universal codes and structured names enabling interoperable exchange and aggregation of clinical, laboratory, and other health data worldwide.
domains:
  - clinical
  - biomedical
  - health
  - genomics
homepage_url: https://loinc.org/
id: "loinc"
layout: resource_detail
license:
  id: "https://loinc.org/license/"
  label: LOINC License (free registration required)
name: LOINC
products:
  - category: GraphicalInterface
    description: Web-based tools including SearchLOINC and Hierarchy Browser for interactive exploration of LOINC content (free login required)
    format: http
    id: "loinc.web"
    name: LOINC Website & Browsers
    original_source:
      - loinc
    product_url: https://loinc.org/search/
  - category: ProgrammingInterface
    description: HL7 FHIR-based API providing programmatic access to LOINC terminology content (requires free LOINC login)
    format: http
    id: "loinc.api.fhir"
    is_public: false
    name: LOINC FHIR API
    original_source:
      - loinc
    product_url: https://loinc.org/fhir/
  - category: DataModelProduct
    compression: zip
    description: Complete LOINC release archive (table and accessory files) downloadable after free registration
    format: mixed
    id: "loinc.complete"
    latest_version: "2.81"
    name: LOINC Complete Release
    original_source:
      - loinc
    product_url: https://loinc.org/download/loinc-complete/
  - category: DataModelProduct
    description: Archive of past LOINC releases for version-specific implementations
    format: mixed
    id: "loinc.archive"
    name: LOINC Release Archive
    original_source:
      - loinc
    product_url: https://loinc.org/downloads/archive/
  - category: DocumentationProduct
    description: LOINC Mission, Vision, and Guiding Principles for open terminology development (CC-BY 4.0 licensed document)
    id: "loinc.principles"
    name: LOINC Principles Document
    original_source:
      - loinc
    product_url: https://loinc.org/principles/
publications:
  - id: "https://doi.org/10.1093/nar/gkad1044"
    journal: Nucleic Acids Research
    preferred: true
    title: "LOINC 2024 update: advancing global interoperability for health measurements and observations"
    year: "2024"
  - id: "https://doi.org/10.1093/nar/gkac998"
    journal: Nucleic Acids Research
    title: "LOINC 2023 update: refining identifiers and expanding clinical content"
    year: "2023"
warnings:
  - LOINC downloads and API require a free account; ensure you cite the specific version (e.g., 2.81) when using the terminology.
---

# LOINC

LOINC (Logical Observation Identifiers Names and Codes) standardizes identifiers and names for laboratory tests, clinical measurements, panels, and documents. A free account unlocks downloads of the complete release (currently 2.81) and access to web tooling (SearchLOINC, Hierarchy Browser) and the HL7 FHIR API. LOINC’s mission and guiding principles emphasize openness, accessibility, pragmatics, agility, and diligence in developing global health data standards. Cite the specific version employed in your implementation.
