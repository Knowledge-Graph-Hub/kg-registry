---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://support.nlm.nih.gov/support/create-case/
  id: ncbi
  label: National Library of Medicine
creation_date: '2025-11-08T00:00:00Z'
description: DailyMed is the National Library of Medicine's official provider of FDA
  drug label information, offering a searchable database of the most recent labeling
  submitted to the Food and Drug Administration by pharmaceutical companies and currently
  in use. As a comprehensive public resource providing over 154,000 drug labels, DailyMed
  contains labeling for prescription and nonprescription drugs for both human and
  animal use, as well as additional products including medical gases, devices, cosmetics,
  dietary supplements, and medical foods. All labeling information is formatted in
  Structured Product Labeling (SPL), an HL7 standard that provides a standardized,
  machine-readable format for drug product information enabling interoperability between
  healthcare systems. DailyMed serves as the authoritative source for current package
  inserts, medication guides, patient information sheets, and prescribing information
  directly as submitted by manufacturers to the FDA. The database is updated daily
  as new labeling is submitted and approved, ensuring users have access to the most
  current drug safety and efficacy information available. DailyMed provides detailed
  information including indications and usage, dosage and administration, contraindications,
  warnings and precautions, adverse reactions, drug interactions, use in specific
  populations, clinical pharmacology, and how the drug is supplied.
domains:
- health
homepage_url: https://dailymed.nlm.nih.gov/dailymed/
id: dailymed
infores_id: dailymed
last_modified_date: '2025-11-08T00:00:00Z'
layout: resource_detail
name: DailyMed
products:
- category: GraphicalInterface
  description: Interactive web interface providing searchable access to over 154,000
    FDA-approved drug labels with advanced search, browsing by therapeutic class,
    and pill image viewing
  format: http
  id: dailymed.website
  name: DailyMed Website
  product_url: https://dailymed.nlm.nih.gov/dailymed/
- category: ProgrammingInterface
  description: RESTful web services enabling programmatic access to DailyMed drug
    labeling data in Structured Product Labeling (SPL) format
  format: xml
  id: dailymed.web_services
  name: DailyMed Web Services
  product_url: https://dailymed.nlm.nih.gov/dailymed/app-support-web-services.cfm
- category: Product
  description: Downloadable SPL files for all drug labels in the DailyMed database,
    updated daily
  format: xml
  id: dailymed.spl_files
  name: DailyMed SPL Data Files
  product_url: https://dailymed.nlm.nih.gov/dailymed/spl-resources-all-drug-labels.cfm
- category: Product
  description: Mapping files linking DailyMed drug labels to RxNorm codes, UNII identifiers,
    and NDC codes for interoperability
  format: http
  id: dailymed.mapping_files
  name: DailyMed Mapping Files
  product_url: https://dailymed.nlm.nih.gov/dailymed/app-support-mapping-files.cfm
- category: Product
  description: RSS feeds providing notifications of new and updated drug labels published
    on DailyMed
  format: http
  id: dailymed.rss_feeds
  name: DailyMed RSS Feeds
  product_url: https://dailymed.nlm.nih.gov/dailymed/rss-updates.cfm
taxon:
- NCBITaxon:9606
---

# DailyMed

## Overview

DailyMed is the National Library of Medicine's official public repository for FDA-approved drug labeling information, providing free access to over 154,000 current drug labels for prescription and nonprescription medications, as well as other FDA-regulated products.

## Information Resource ID

This resource has the Information Resource identifier: `infores:dailymed`

## Mission and Scope

DailyMed provides the most recent labeling submitted to the FDA by pharmaceutical companies and currently in use. The database serves as the authoritative public source for official package inserts and prescribing information, reformatted by NLM for improved readability while maintaining the FDA-approved content.

## Content Coverage

- **Prescription drugs**: Full labeling for human prescription medications
- **Over-the-counter drugs**: Nonprescription medications for human use
- **Animal drugs**: Veterinary medications
- **Additional products**: Medical gases, devices, cosmetics, dietary supplements, medical foods
- **Daily updates**: New and revised labels as submitted to FDA

## Structured Product Labeling (SPL)

All DailyMed content uses the HL7 Structured Product Labeling standard, providing:
- Machine-readable drug information format
- Standardized sections for indications, dosing, warnings, and more
- Interoperability with electronic health records and pharmacy systems
- Links to standardized terminologies (RxNorm, UNII, NDC)

## Key Features

### Comprehensive Drug Information
Each label includes standardized sections:
- Indications and usage
- Dosage and administration
- Contraindications
- Warnings and precautions
- Adverse reactions
- Drug interactions
- Use in specific populations
- Clinical pharmacology
- How supplied/storage information

### Search and Navigation
- Search by drug name, active ingredient, or National Drug Code (NDC)
- Browse by therapeutic class
- Advanced search with multiple criteria
- Pill image viewing for oral solid dosage forms

### Risk Evaluation and Mitigation Strategies (REMS)
Access to REMS information for drugs requiring special safety monitoring and management programs.

## Data Access Methods

### Interactive Website
User-friendly interface with search, browse, and filtering capabilities for patients, healthcare providers, and researchers.

### Web Services APIs
RESTful APIs providing programmatic access to:
- Drug label content in SPL format
- Search and retrieval functions
- Metadata and classification information

### Bulk Data Downloads
Complete dataset downloads including:
- All drug labels in SPL XML format
- Indexing files for search and classification
- Mapping files to RxNorm, UNII, and NDC
- Updated daily

### RSS Feeds
Notification feeds for:
- New drug labels published
- Updated label information
- Product-specific or general updates

## Integration and Interoperability

DailyMed provides mapping files enabling integration with:
- **RxNorm**: Standardized drug nomenclature
- **UNII**: Unique Ingredient Identifiers
- **NDC**: National Drug Codes
- **Electronic health records**: Direct label access from EHR systems

## Public Service Mission

DailyMed is provided free to the public without advertising or commercial bias. The NLM maintains DailyMed as a public health service, ensuring access to authoritative, current drug safety and efficacy information for all users.