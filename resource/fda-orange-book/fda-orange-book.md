---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: druginfo@fda.hhs.gov
  - contact_type: url
    value: https://www.fda.gov/
  label: U.S. Food and Drug Administration
creation_date: '2026-06-02T00:00:00Z'
description: The FDA Orange Book, Approved Drug Products with Therapeutic Equivalence
  Evaluations, identifies drug products approved on the basis of safety and effectiveness
  by FDA and provides therapeutic equivalence, patent, and exclusivity information.
domains:
- pharmacology
- clinical
- biomedical
homepage_url: https://www.fda.gov/drugs/drug-approvals-and-databases/approved-drug-products-therapeutic-equivalence-evaluations-orange-book
id: fda-orange-book
last_modified_date: '2026-09-16T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: U.S. Government Work (public domain)
name: FDA Orange Book
products:
- category: GraphicalInterface
  description: FDA searchable Orange Book database for approved drug products, active
    ingredients, proprietary names, applicants, application numbers, dosage forms,
    routes, and patent numbers.
  format: http
  id: fda-orange-book.search
  name: FDA Orange Book Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fda-orange-book
  product_url: https://www.fda.gov/drugs/drug-approvals-and-databases/approved-drug-products-therapeutic-equivalence-evaluations-orange-book
- category: Product
  description: FDA Orange Book data files and appendices for approved drug products,
    therapeutic equivalence evaluations, patents, exclusivity, and related regulatory
    information.
  format: mixed
  id: fda-orange-book.data-files
  name: FDA Orange Book Data Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fda-orange-book
  product_url: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files
  warnings:
  - 'File was not able to be retrieved when checked on 2026-11-12: HTTP 404 error when
    accessing file'
- category: DocumentationProduct
  description: FDA Orange Book preface describing publication structure, therapeutic
    equivalence codes, and interpretation of Orange Book listings.
  format: http
  id: fda-orange-book.preface
  name: FDA Orange Book Preface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fda-orange-book
  product_url: https://www.fda.gov/drugs/development-approval-process-drugs/orange-book-preface
  warnings:
  - 'File was not able to be retrieved when checked on 2026-11-12: HTTP 404 error when
    accessing file'
- category: Product
  description: FDA Orange Book regulatory source extract from the medic v1.0.1 release
  format: xlsx
  id: medi.orangebook
  latest_version: v1.0.1
  name: MeDI Orange Book Extract
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medi
  product_file_size: 924266
  product_url: https://github.com/marcello-deluca/medic/releases/download/v1.0.1/orangebook.xlsx
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: fda-orange-book
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
- category: Product
  compression: zip
  description: Latest CDCDB release (version of 18 June 2024) as CSV tables covering
    clinical trial design groups, studies, conditions, MeSH terms and references,
    FDA Orange Book combination products and patents, patent drug, metadata and IPC
    tables, and the all-combinations table with DrugBank and PubChem identifiers.
  format: csv
  id: cdcdb.csv
  name: CDCDB CSV Tables
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cdcdb
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: aact
  - relation_type: prov:hadPrimarySource
    source: fda-orange-book
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: pubchem
  product_file_size: 70422005
  product_url: https://icc.ise.bgu.ac.il/medical_ai/api/version/18.06.2024.zip
  secondary_source:
  - relation_type: prov:used
    source: umls
- category: Product
  compression: zip
  description: Latest CDCDB release (version of 18 June 2024) as a SQLite database
    holding the same tables as the CSV release.
  format: sqlite
  id: cdcdb.sqlite
  name: CDCDB SQLite Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cdcdb
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: aact
  - relation_type: prov:hadPrimarySource
    source: fda-orange-book
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: pubchem
  product_file_size: 75016574
  product_url: https://icc.ise.bgu.ac.il/medical_ai/api/version/18.06.2024.sqlite.zip
  secondary_source:
  - relation_type: prov:used
    source: umls
- category: Product
  description: Figshare collection accompanying the Scientific Data paper, with the
    CSV and SQLite versions of CDCDB from 12 April 2022, the database schema, a description
    and a read-me file, released under CC0.
  format: mixed
  id: cdcdb.figshare
  name: CDCDB Figshare Collection (12 April 2022)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cdcdb
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: aact
  - relation_type: prov:hadPrimarySource
    source: fda-orange-book
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: pubchem
  product_url: https://doi.org/10.6084/m9.figshare.c.5375228.v1
- category: Product
  compression: zip
  description: DCDB 2.0 data as tab-delimited plain text files (drug combinations,
    components, targets and their interactions), formerly offered on the DCDB download
    page alongside an Oracle 11.2 dump.
  format: tsv
  id: dcdb.plain_text_dump
  name: DCDB 2.0 Plain Text Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dcdb
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: fda-orange-book
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: http://www.cls.zju.edu.cn/dcdb/downloadfile/DCDB2_plaintxt.zip
  warnings:
  - File was not able to be retrieved when checked on 2026-11-12 (HTTP 404); no archived
    copy was found in the Internet Archive.
rrid: SCR_013727
synonyms:
- Approved Drug Products with Therapeutic Equivalence Evaluations
- Orange Book
---
# FDA Orange Book

The FDA Orange Book is the authoritative FDA publication for approved drug
products with therapeutic equivalence evaluations. It provides search and data
file access to product approval, therapeutic equivalence, patent, and exclusivity
information used by downstream regulatory and drug indication resources.