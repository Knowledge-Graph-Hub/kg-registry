---
activity_status: active
category: DataSource
collection:
- omop
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
last_modified_date: '2026-10-03T00:00:00Z'
layout: resource_detail
license:
  id: https://www.fda.gov/about-fda/about-website/website-policies
  label: Public Domain
name: National Drug Code Directory
products:
- category: GraphicalInterface
  description: Web-based search interface for the NDC Directory allowing users to
    search and browse National Drug Code information
  format: http
  id: ndcd.search
  name: NDC Directory Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ndcd
  product_url: https://www.accessdata.fda.gov/scripts/cder/ndc
- category: Product
  compression: zip
  description: Downloadable database file in text format containing finished drug
    product information, updated daily
  format: txt
  id: ndcd.text
  name: NDC Database Text File
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ndcd
  product_file_size: 10514948
  product_url: https://www.accessdata.fda.gov/cder/ndctext.zip
- category: Product
  compression: zip
  description: Downloadable NDC database files (product.xls and package.xls) containing finished drug product information. Despite the .xls extension, the files are tab-delimited text.
  format: tsv
  id: ndcd.excel
  name: NDC Database Excel File
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ndcd
  product_file_size: 10514948
  product_url: https://www.accessdata.fda.gov/cder/ndcxls.zip
- category: ProgrammingInterface
  description: REST API providing programmatic access to National Drug Code data through
    the openFDA platform
  format: http
  id: ndcd.api
  name: NDC API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ndcd
  - relation_type: prov:hadPrimarySource
    source: openfda
  product_url: https://open.fda.gov/apis/drug/ndc/
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
- category: ProgrammingInterface
  connection_url: https://api.fda.gov/
  description: JSON REST APIs (Elasticsearch query syntax) for FDA drug, device, food,
    animal and veterinary, cosmetic, tobacco and other datasets, including drug adverse
    events (FAERS), device adverse events (MAUDE), the National Drug Code directory,
    the Orange Book, UNII substance data, labeling, recalls and enforcement reports.
  format: http
  id: openfda.apis
  is_public: true
  name: openFDA APIs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: openfda
  - relation_type: prov:hadPrimarySource
    source: faers
  - relation_type: prov:hadPrimarySource
    source: maude
  - relation_type: prov:hadPrimarySource
    source: ndcd
  - relation_type: prov:hadPrimarySource
    source: fda-orange-book
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://open.fda.gov/apis/
- category: Product
  compression: zip
  description: Bulk downloads of every openFDA endpoint as zipped JSON files, split
    into partitions for large datasets such as drug adverse events (FAERS) and device
    adverse events (MAUDE), with a machine-readable manifest at https://api.fda.gov/download.json
    listing each endpoint's export date and file partitions.
  format: json
  id: openfda.downloads
  name: openFDA Bulk Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: openfda
  - relation_type: prov:hadPrimarySource
    source: faers
  - relation_type: prov:hadPrimarySource
    source: maude
  - relation_type: prov:hadPrimarySource
    source: ndcd
  - relation_type: prov:hadPrimarySource
    source: fda-orange-book
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://open.fda.gov/data/downloads/
- category: ProgrammingInterface
  description: MyChem.info REST API (v1) for querying chemical and drug annotation records
    by keyword, field or identifier (InChIKey, ChEMBL, DrugBank, PubChem, ChEBI and UNII IDs),
    with batch queries over POST. Data in each record keep the license of their original source.
  format: json
  id: mychem.api
  infores_id: mychem-info
  name: MyChem.info API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mychem
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: unii
  - relation_type: prov:hadPrimarySource
    source: ndcd
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: aeolus
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: fda-orphan-drugs
  product_url: https://mychem.info/v1/query
synonyms:
- NDC
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