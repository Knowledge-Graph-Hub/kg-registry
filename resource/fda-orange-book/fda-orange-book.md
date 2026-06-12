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
homepage_url: https://www.fda.gov/cder/ob/default.htm
id: fda-orange-book
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: FDA Orange Book
products:
- category: GraphicalInterface
  description: FDA searchable Orange Book database for approved drug products, active
    ingredients, proprietary names, applicants, application numbers, dosage forms,
    routes, and patent numbers.
  id: fda-orange-book.search
  name: FDA Orange Book Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fda-orange-book
  product_url: https://www.fda.gov/cder/ob/default.htm
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
  - 'File was not able to be retrieved when checked on 2026-06-05: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-12: HTTP 404 error
    when accessing file'
- category: DocumentationProduct
  description: FDA Orange Book preface describing publication structure, therapeutic
    equivalence codes, and interpretation of Orange Book listings.
  id: fda-orange-book.preface
  name: FDA Orange Book Preface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fda-orange-book
  product_url: https://www.fda.gov/drugs/development-approval-process-drugs/orange-book-preface
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-05: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-12: HTTP 404 error
    when accessing file'
- category: Product
  description: FDA Orange Book regulatory source extract from the medic v1.0.1 release
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
synonyms:
- Approved Drug Products with Therapeutic Equivalence Evaluations
- Orange Book
---
# FDA Orange Book

The FDA Orange Book is the authoritative FDA publication for approved drug
products with therapeutic equivalence evaluations. It provides search and data
file access to product approval, therapeutic equivalence, patent, and exclusivity
information used by downstream regulatory and drug indication resources.