---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://admin.ich.org/page/meddra
    label: ICH MedDRA Maintenance and Support Services Organisation
creation_date: '2026-06-02T00:00:00Z'
description: MedDRA, the Medical Dictionary for Regulatory Activities, is an ICH standardized medical terminology used internationally for registration, documentation, safety monitoring, and pharmacovigilance of medical products.
domains:
  - clinical
  - biomedical
  - pharmacology
homepage_url: https://admin.ich.org/page/meddra
id: meddra
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: MedDRA
products:
  - category: Product
    description: MedDRA terminology release files maintained and distributed by the MedDRA MSSO for subscribers, supporting regulatory coding and pharmacovigilance workflows.
    id: meddra.release-files
    name: MedDRA Terminology Release Files
    original_source:
      - relation_type: prov:hadPrimarySource
        source: meddra
    product_url: https://www.meddra.org/subscription
  - category: GraphicalInterface
    description: MedDRA Web-Based Browser provided for MedDRA subscribers to search and view MedDRA terminology content.
    id: meddra.web-browser
    name: MedDRA Web-Based Browser
    original_source:
      - relation_type: prov:hadPrimarySource
        source: meddra
    product_url: https://mssotools.com/MSSOWeb/wbb/wbb_index.html
  - category: DocumentationProduct
    description: ICH MedDRA page describing the terminology, governance, MSSO maintenance, and regulatory use cases.
    id: meddra.ich-page
    name: ICH MedDRA Documentation
    original_source:
      - relation_type: prov:hadPrimarySource
        source: meddra
    product_url: https://admin.ich.org/page/meddra
  - category: Product
    description: Quarterly data extracts in ASCII format containing demographic, drug, reaction, outcome, and source information for reported adverse events
    format: txt
    id: faers.quarterly_data_ascii
    latest_version: 2026Q1
    name: FAERS Quarterly Data Files (ASCII)
    original_source:
      - relation_type: prov:hadPrimarySource
        source: faers
    product_url: https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html
    secondary_source:
      - relation_type: prov:wasInformedBy
        source: meddra
  - category: Product
    description: Quarterly data extracts in XML format adhering to ICH E2B standards for international safety reporting
    format: xml
    id: faers.quarterly_data_xml
    latest_version: 2026Q1
    name: FAERS Quarterly Data Files (XML)
    original_source:
      - relation_type: prov:hadPrimarySource
        source: faers
    product_url: https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html
    secondary_source:
      - relation_type: prov:wasInformedBy
        source: meddra
synonyms:
  - Medical Dictionary for Regulatory Activities
warnings:
  - MedDRA terminology files and browser access are controlled through the MedDRA MSSO subscription model; access conditions should be checked before reuse.
---

# MedDRA

MedDRA is the international medical terminology maintained by the ICH MedDRA
MSSO for regulatory reporting, safety monitoring, and pharmacovigilance. FAERS
uses MedDRA terminology for adverse-event reaction coding in its quarterly data
files.
