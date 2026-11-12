---
activity_status: inactive
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: shtar@post.bgu.ac.il
  label: Guy Shtar
- category: Organization
  contact_details:
  - contact_type: url
    value: https://icc.ise.bgu.ac.il/medical_ai/CDCDB/
  label: Department of Software and Information Systems Engineering, Ben-Gurion University
    of the Negev
creation_date: '2026-11-12T00:00:00Z'
description: CDCDB (Continuous Drug Combination Database) is an automatically curated
  and continuously updated database of drug combinations, developed at Ben-Gurion
  University of the Negev as a successor to the static DCDB (last released in 2014).
  It collects combinations of two or more drugs from clinical trial design groups
  in ClinicalTrials.gov (via the AACT database), approved combination products in
  the FDA Orange Book, and drug patents from Clarivate Integrity, using named entity
  recognition against UMLS to separate drugs from free-text intervention names and
  mapping each drug to DrugBank and PubChem identifiers. The 2022 publication reported
  40,795 drug combinations, of which 17,107 are unique combinations of 4,129 individual
  drugs, along with trial conditions, MeSH terms and references, Orange Book product
  and patent details, and patent metadata. New versions were built weekly and offered
  as CSV and SQLite downloads, intended for training and evaluating drug synergy
  prediction models; the most recent version on the website is dated 18 June 2024.
domains:
- pharmacology
- drug discovery
- clinical
- clinical trials
homepage_url: https://icc.ise.bgu.ac.il/medical_ai/CDCDB/
id: cdcdb
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: Continuous Drug Combination Database
products:
- category: GraphicalInterface
  description: CDCDB website, with a preview table of all drug combinations, documentation
    of how the database is built, and downloads of the latest and past weekly versions.
  format: http
  id: cdcdb.portal
  name: CDCDB Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cdcdb
  product_url: https://icc.ise.bgu.ac.il/medical_ai/CDCDB/
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
- category: ProcessProduct
  description: Source code used to generate CDCDB from its source databases.
  format: http
  id: cdcdb.code
  name: CDCDB Generation Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cdcdb
  product_url: https://github.com/Omer-N/CDCDB
publications:
- authors:
  - Shtar G
  - Azulay L
  - Nizri O
  - Rokach L
  - Shapira B
  doi: 10.1038/s41597-022-01360-z
  id: doi:10.1038/s41597-022-01360-z
  journal: Scientific Data
  preferred: true
  title: 'CDCDB: A large and continuously updated drug combination database'
  year: '2022'
repository: https://github.com/Omer-N/CDCDB
synonyms:
- CDCDB
- C-DCDB
version: '18.06.2024'
---
# Continuous Drug Combination Database

## Overview

CDCDB (Continuous Drug Combination Database) is a database of drug combinations
developed at Ben-Gurion University of the Negev and described in Scientific Data
(2022). It was built as a successor to DCDB, whose last version (DCDB 2.0) dates from
2014: rather than manual curation, CDCDB is generated automatically and was meant to
be rebuilt weekly so it stays current.

Combinations come from three sources:

- clinical trial design groups in ClinicalTrials.gov, via the AACT database;
- approved combination products in the FDA Orange Book;
- drug patents from Clarivate Integrity, with metadata from the Derwent Innovations
  Index.

Named entity recognition against UMLS separates drug names from free-text intervention
descriptions, and each drug is mapped to DrugBank and PubChem identifiers. The 2022
paper reported 40,795 drug combinations (17,107 unique) involving 4,129 individual
drugs. The data are intended for training and evaluating drug synergy prediction
models.

## Access

- Website, with a preview table and downloads of current and past versions:
  https://icc.ise.bgu.ac.il/medical_ai/CDCDB/
- Figshare snapshot of 12 April 2022 (CSV and SQLite, CC0):
  https://doi.org/10.6084/m9.figshare.c.5375228.v1
- Generation code: https://github.com/Omer-N/CDCDB

## Status

The website and downloads were reachable on 2026-11-12, but the most recent weekly
version listed is dated 18 June 2024, so the database no longer appears to be updated.
