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
- biomedical
homepage_url: https://dailymed.nlm.nih.gov/dailymed/
id: dailymed
infores_id: dailymed
last_modified_date: '2026-06-01T00:00:00Z'
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
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dailymed
  product_url: https://dailymed.nlm.nih.gov/dailymed/
- category: ProgrammingInterface
  connection_url: https://dailymed.nlm.nih.gov/dailymed/services/v2/
  description: RESTful web services enabling programmatic access to DailyMed drug
    labeling data in Structured Product Labeling (SPL) format
  format: xml
  id: dailymed.web_services
  name: DailyMed Web Services
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dailymed
  product_url: https://dailymed.nlm.nih.gov/dailymed/app-support-web-services.cfm
- category: Product
  description: Downloadable SPL files for all drug labels in the DailyMed database,
    updated daily
  format: xml
  id: dailymed.spl_files
  name: DailyMed SPL Data Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dailymed
  product_url: https://dailymed.nlm.nih.gov/dailymed/spl-resources-all-drug-labels.cfm
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: rxnorm
  - relation_type: prov:wasInformedBy
    source: unii
  - relation_type: prov:wasInformedBy
    source: ndcd
- category: Product
  description: Mapping files linking DailyMed drug labels to RxNorm codes, UNII identifiers,
    and NDC codes for interoperability
  format: http
  id: dailymed.mapping_files
  name: DailyMed Mapping Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dailymed
  product_url: https://dailymed.nlm.nih.gov/dailymed/app-support-mapping-files.cfm
- category: Product
  description: RSS feeds providing notifications of new and updated drug labels published
    on DailyMed
  format: http
  id: dailymed.rss_feeds
  name: DailyMed RSS Feeds
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dailymed
  product_url: https://dailymed.nlm.nih.gov/dailymed/rss-updates.cfm
- category: Product
  compression: zip
  description: Current MED-RT DTS release archive from the NCI EVS MED-RT distribution.
  id: med-rt.core_dts
  name: Core MED-RT DTS Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: med-rt
  product_file_size: 2479793
  product_url: https://evs.nci.nih.gov/ftp1/MED-RT/Core_MEDRT_DTS.zip
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasInformedBy
    source: dailymed
  - relation_type: prov:wasInformedBy
    source: mesh
  - relation_type: prov:wasInformedBy
    source: rxnorm
  - relation_type: prov:wasInformedBy
    source: snomedct
  - relation_type: prov:wasInformedBy
    source: umls
- category: Product
  compression: zip
  description: Current MED-RT XML release archive from the NCI EVS MED-RT distribution.
  format: xml
  id: med-rt.core_xml
  name: Core MED-RT XML Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: med-rt
  product_file_size: 2558768
  product_url: https://evs.nci.nih.gov/ftp1/MED-RT/Core_MEDRT_XML.zip
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: ndfrt
  - relation_type: prov:wasInformedBy
    source: dailymed
  - relation_type: prov:wasInformedBy
    source: mesh
  - relation_type: prov:wasInformedBy
    source: rxnorm
  - relation_type: prov:wasInformedBy
    source: snomedct
  - relation_type: prov:wasInformedBy
    source: umls
- category: Product
  compression: zip
  description: Structured Product Labeling subset archive from the current MED-RT
    distribution.
  id: med-rt.core_spl
  name: Core MED-RT SPL Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: med-rt
  product_file_size: 40677
  product_url: https://evs.nci.nih.gov/ftp1/MED-RT/Core_MEDRT_SPL.zip
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: dailymed
  - relation_type: prov:wasInformedBy
    source: rxnorm
  - relation_type: prov:wasInformedBy
    source: umls
- category: ProcessProduct
  description: Active GitHub repository for MeDI/medic medicines, diseases, indications,
    and contraindications data and processing code
  format: http
  id: medi.github
  name: medic GitHub Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medi
  product_url: https://github.com/marcello-deluca/medic
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: dailymed
  - relation_type: prov:wasInformedBy
    source: mondo
- category: Product
  description: Matrix indication list spreadsheet from the medic v1.0.1 release
  id: medi.matrix_indication_list
  latest_version: v1.0.1
  name: Matrix Indication List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medi
  product_file_size: 2173559
  product_url: https://github.com/marcello-deluca/medic/releases/download/v1.0.1/matrix_indication_list.xlsx
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: dailymed
  - relation_type: prov:used
    source: mondo
- category: Product
  description: Flexible drug list CSV from the medic v1.0.1 release
  format: csv
  id: medi.drug_list_flexible
  latest_version: v1.0.1
  name: MeDI Flexible Drug List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medi
  product_file_size: 4428523
  product_url: https://github.com/marcello-deluca/medic/releases/download/v1.0.1/drug_list_flexible.csv
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: dailymed
  - relation_type: prov:wasInformedBy
    source: rxnorm
- category: Product
  description: Stringent drug list CSV from the medic v1.0.1 release
  format: csv
  id: medi.drug_list_stringent
  latest_version: v1.0.1
  name: MeDI Stringent Drug List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medi
  product_file_size: 3672087
  product_url: https://github.com/marcello-deluca/medic/releases/download/v1.0.1/drug_list_stringent.csv
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: dailymed
  - relation_type: prov:wasInformedBy
    source: rxnorm
- category: Product
  description: LabeledIn indication corpus described in the source publication, containing
    human-reviewed drug-disease treatment relationships with links back to source
    drug labels.
  id: labeledin.indications
  name: LabeledIn Drug Indication Corpus
  original_source:
  - relation_type: prov:hadPrimarySource
    source: labeledin
  product_url: https://doi.org/10.1016/j.jbi.2014.08.004
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: dailymed
  - relation_type: prov:used
    source: rxnorm
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