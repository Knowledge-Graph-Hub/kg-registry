---
activity_status: active
category: DataSource
creation_date: '2025-11-19T00:00:00Z'
description: The FDA National Drug Code Directory is a comprehensive database maintained
  by the U.S. Food and Drug Administration containing information about finished drug
  products, unfinished drugs, and compounded drug products. Drug establishments are
  required to provide FDA with current lists of all drugs using unique three-segment
  National Drug Code (NDC) numbers. The directory includes prescription and over-the-counter
  drugs, approved and unapproved drugs, and repackaged and relabeled drugs. The database
  is updated daily and provides essential drug identification and regulatory information
  for healthcare professionals, researchers, and regulatory compliance.
domains:
- pharmacology
- drug discovery
- clinical
- biomedical
homepage_url: https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory
id: ndcd
infores_id: ndcd
last_modified_date: '2025-11-19T00:00:00Z'
layout: resource_detail
name: National Drug Code Directory
products:
- category: GraphicalInterface
  description: Web-based search interface for the NDC Directory allowing users to
    search and browse National Drug Code information
  format: http
  id: ndcd.search
  name: NDC Directory Search
  original_source:
  - ndcd
  product_url: https://www.accessdata.fda.gov/scripts/cder/ndc
- category: Product
  compression: zip
  description: Downloadable database file in text format containing finished drug
    product information, updated daily
  format: txt
  id: ndcd.text
  name: NDC Database Text File
  original_source:
  - ndcd
  product_url: https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory
  warnings:
  - File was not able to be retrieved when checked on 2026-02-04_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-02-13_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-02-15: HTTP 404 error
    when accessing file'
- category: Product
  compression: zip
  description: Downloadable database file in Excel format containing finished drug
    product information
  id: ndcd.excel
  name: NDC Database Excel File
  original_source:
  - ndcd
  product_url: https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory
  warnings:
  - File was not able to be retrieved when checked on 2026-02-04_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-02-13_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-02-15: HTTP 404 error
    when accessing file'
- category: ProgrammingInterface
  description: REST API providing programmatic access to National Drug Code data through
    the openFDA platform
  format: http
  id: ndcd.api
  name: NDC API
  original_source:
  - ndcd
  product_url: https://open.fda.gov/apis/drug/ndc/
synonyms:
- NDCD
- NDC Directory
taxon:
- NCBITaxon:9606
---
# National Drug Code Directory

The FDA National Drug Code Directory is an authoritative database of drug products maintained by the U.S. Food and Drug Administration. It serves as the central registry for National Drug Codes (NDCs), which are unique three-segment numerical identifiers assigned to all drugs and drug packages in the United States.

## Key Features

- **Daily Updates**: Database is updated daily with new drug registrations and modifications
- **Comprehensive Coverage**: Includes prescription drugs, over-the-counter medications, approved and unapproved drugs, and repackaged/relabeled products
- **Multiple Product Types**: Covers finished drug products, unfinished drugs, and compounded drug products
- **Public Access**: Free access to all data through web interface, downloadable files, and API
- **Regulatory Compliance**: Required registration system for all drug establishments

## NDC Structure

National Drug Codes use a three-segment format that identifies:
1. **Labeler code**: The firm that manufactures, repacks, or distributes the drug
2. **Product code**: The specific strength, dosage form, and formulation
3. **Package code**: The package size and type

## Information Resource ID

This resource has the Information Resource identifier: `infores:ndcd`