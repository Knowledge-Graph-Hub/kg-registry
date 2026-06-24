---
activity_status: active
category: DataSource
collection:
- ber
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.itis.gov/
  - contact_type: email
    value: itiswebmaster@itis.gov
  label: Integrated Taxonomic Information System (ITIS)
creation_date: '2025-09-03T00:00:00Z'
description: The Integrated Taxonomic Information System (ITIS) provides authoritative
  taxonomic information on plants, animals, fungi, and microbes of North America and
  the world. ITIS compiles standardized scientific names, common names, taxonomic
  serial numbers (TSNs), hierarchical classification, and associated metadata curated
  through interagency and international collaboration to support biodiversity data
  integration, ecological research, regulatory processes, and interoperability across
  biological information systems.
domains:
- organisms
- environment
homepage_url: https://www.itis.gov/
id: itis
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://www.itis.gov/access.html
  label: Public Domain
name: ITIS
products:
- category: GraphicalInterface
  description: Web portal for browsing taxonomic records, hierarchical classification,
    name sources, and reports
  format: http
  id: itis.portal
  name: ITIS Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: itis
  product_url: https://www.itis.gov/
- category: ProgrammingInterface
  connection_url: https://www.itis.gov/ITISWebService/jsonservice/
  description: REST JSON services providing programmatic access to taxonomic records,
    synonyms, hierarchy, and search utilities
  format: json
  id: itis.api
  is_public: true
  name: ITIS REST Services
  original_source:
  - relation_type: prov:hadPrimarySource
    source: itis
  product_url: https://www.itis.gov/ws_description.html
- category: Product
  compression: gzip
  description: Full ITIS data set for MySQL by-table bulk loading.
  format: mysql
  id: itis.mysql_tables
  name: ITIS MySQL Tables Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: itis
  product_file_size: 57611377
  product_url: https://www.itis.gov/downloads/itisMySQLTables.tar.gz
- category: Product
  compression: zip
  description: Full ITIS data set packaged as a SQLite database download.
  format: sqlite
  id: itis.sqlite
  name: ITIS SQLite Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: itis
  product_file_size: 222746679
  product_url: https://www.itis.gov/downloads/itisSqlite.zip
- category: Product
  description: itis OBO
  format: obo
  id: obo-db-ingest.itis.obo
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: itis OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: itis
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 10936424
  product_url: https://w3id.org/biopragmatics/resources/itis/itis.obo
- category: Product
  compression: gzip
  description: itis OWL
  format: owl
  id: obo-db-ingest.itis.owl
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: itis OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: itis
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 14607611
  product_url: https://w3id.org/biopragmatics/resources/itis/itis.owl.gz
- category: Product
  compression: gzip
  description: itis OBO Graph JSON
  format: json
  id: obo-db-ingest.itis.json
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: itis OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: itis
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 12669423
  product_url: https://w3id.org/biopragmatics/resources/itis/itis.json.gz
- category: Product
  description: itis Nodes TSV
  format: tsv
  id: obo-db-ingest.itis.tsv
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: itis Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: itis
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 9497861
  product_url: https://w3id.org/biopragmatics/resources/itis/itis.tsv
- category: Product
  description: Annual comprehensive Catalogue of Life releases (Base Release with
    expert curation and Extended Release with broader source integration) with permanent
    archiving and DOI assignment
  id: catalogue-of-life.annual-releases
  name: Annual Releases
  original_source:
  - relation_type: prov:hadPrimarySource
    source: catalogue-of-life
  - relation_type: prov:hadPrimarySource
    source: itis
  - relation_type: prov:hadPrimarySource
    source: gbif
  product_url: https://www.catalogueoflife.org/
- category: Product
  description: Downloadable Catalogue of Life datasets in multiple standardized formats
    including Catalogue of Life Data Package (ColDP), Darwin Core Archive, ACEF, TextTree,
    and MySQL dumps
  id: catalogue-of-life.downloads
  name: Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: catalogue-of-life
  - relation_type: prov:hadPrimarySource
    source: itis
  - relation_type: prov:hadPrimarySource
    source: gbif
  product_url: https://www.catalogueoflife.org/data/download
  warnings:
  - Automated checks may return HTTP 418 due to anti-bot challenge on catalogueoflife.org
    download pages; URL is retained as the canonical human-access endpoint.
- category: GraphicalInterface
  description: Web interface for browsing, querying, and visualizing ecological networks
  format: http
  id: mangal.portal
  name: mangal.io Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mangal
  product_url: https://mangal.io/
  secondary_source:
  - relation_type: prov:used
    source: catalogue-of-life
  - relation_type: prov:used
    source: gbif
  - relation_type: prov:used
    source: itis
- category: ProgrammingInterface
  description: RESTful API for programmatic access to network data and metadata
  format: http
  id: mangal.api
  is_public: true
  name: mangal.io API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mangal
  product_url: https://api.mangal.io/
  secondary_source:
  - relation_type: prov:used
    source: catalogue-of-life
  - relation_type: prov:used
    source: gbif
  - relation_type: prov:used
    source: itis
  warnings:
  - Host api.mangal.io was not resolvable when checked on 2026-06-02.
- category: DocumentationProduct
  description: API documentation, user guides, and data model specification
  format: http
  id: mangal.docs
  name: mangal.io Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mangal
  product_url: https://mangal.io/documentation
- category: ProcessProduct
  description: R package for retrieving and exploring data from the Mangal ecological
    interactions database
  format: http
  id: mangal.rmangal
  name: rmangal R Client
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mangal
  product_url: https://docs.ropensci.org/rmangal/
  secondary_source:
  - relation_type: prov:used
    source: catalogue-of-life
  - relation_type: prov:used
    source: gbif
  - relation_type: prov:used
    source: itis
- category: GraphicalInterface
  description: Web interface that allows searching, browsing, and exploring food compounds
    and their properties.
  format: http
  id: foodb.web
  name: FooDB Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodb
  product_url: https://foodb.ca/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: hmdb
  - relation_type: prov:wasInformedBy
    source: pubchem
  - relation_type: prov:wasInformedBy
    source: chebi
  - relation_type: prov:wasInformedBy
    source: kegg
  - relation_type: prov:wasInformedBy
    source: ncbitaxon
  - relation_type: prov:wasInformedBy
    source: pubmed
  - relation_type: prov:wasInformedBy
    source: itis
  - relation_type: prov:wasInformedBy
    source: wikipedia
  - relation_type: prov:wasInformedBy
    source: wikispecies
- category: Product
  compression: targz
  description: Complete FooDB database in CSV format
  format: csv
  id: foodb.data.csv
  name: FooDB CSV Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodb
  product_file_size: 998314299
  product_url: https://foodb.ca/public/system/downloads/foodb_2020_4_7_csv.tar.gz
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: hmdb
  - relation_type: prov:wasInformedBy
    source: pubchem
  - relation_type: prov:wasInformedBy
    source: chebi
  - relation_type: prov:wasInformedBy
    source: kegg
  - relation_type: prov:wasInformedBy
    source: ncbitaxon
  - relation_type: prov:wasInformedBy
    source: pubmed
  - relation_type: prov:wasInformedBy
    source: itis
  - relation_type: prov:wasInformedBy
    source: wikipedia
  - relation_type: prov:wasInformedBy
    source: wikispecies
- category: Product
  compression: targz
  description: Complete FooDB database in XML format
  format: xml
  id: foodb.data.xml
  name: FooDB XML Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodb
  product_file_size: 6731854848
  product_url: https://foodb.ca/public/system/downloads/foodb_2020_4_7_xml.tar.gz
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: hmdb
  - relation_type: prov:wasInformedBy
    source: pubchem
  - relation_type: prov:wasInformedBy
    source: chebi
  - relation_type: prov:wasInformedBy
    source: kegg
  - relation_type: prov:wasInformedBy
    source: ncbitaxon
  - relation_type: prov:wasInformedBy
    source: pubmed
  - relation_type: prov:wasInformedBy
    source: itis
  - relation_type: prov:wasInformedBy
    source: wikipedia
  - relation_type: prov:wasInformedBy
    source: wikispecies
- category: Product
  compression: zip
  description: Complete FooDB database in JSON format
  format: json
  id: foodb.data.json
  name: FooDB JSON Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodb
  product_file_size: 90852659
  product_url: https://foodb.ca/public/system/downloads/foodb_2020_04_07_json.zip
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: hmdb
  - relation_type: prov:wasInformedBy
    source: pubchem
  - relation_type: prov:wasInformedBy
    source: chebi
  - relation_type: prov:wasInformedBy
    source: kegg
  - relation_type: prov:wasInformedBy
    source: ncbitaxon
  - relation_type: prov:wasInformedBy
    source: pubmed
  - relation_type: prov:wasInformedBy
    source: itis
  - relation_type: prov:wasInformedBy
    source: wikipedia
  - relation_type: prov:wasInformedBy
    source: wikispecies
- category: Product
  compression: targz
  description: Complete FooDB database as MySQL dump
  format: mysql
  id: foodb.data.mysql
  name: FooDB MySQL Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: foodb
  product_file_size: 180900659
  product_url: https://foodb.ca/public/system/downloads/foodb_2020_4_7_mysql.tar.gz
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: hmdb
  - relation_type: prov:wasInformedBy
    source: pubchem
  - relation_type: prov:wasInformedBy
    source: chebi
  - relation_type: prov:wasInformedBy
    source: kegg
  - relation_type: prov:wasInformedBy
    source: ncbitaxon
  - relation_type: prov:wasInformedBy
    source: pubmed
  - relation_type: prov:wasInformedBy
    source: itis
  - relation_type: prov:wasInformedBy
    source: wikipedia
  - relation_type: prov:wasInformedBy
    source: wikispecies
taxon:
- NCBITaxon:2759
---
## Overview

The Integrated Taxonomic Information System (ITIS) is a partnership of U.S., Canadian, and Mexican agencies, and other organizations, producing a curated reference of global taxonomic information. Each taxon is assigned a persistent Taxonomic Serial Number (TSN) that facilitates integration and reconciliation across biodiversity, ecological, and regulatory datasets.

## Data Scope

- Scientific and common names with synonymy and name usage
- Hierarchical classification spanning kingdoms to species (and infraspecific ranks)
- Authorship, publication, and nomenclatural references
- Geographic data indicators and taxonomic status flags
- Cross-references to other authoritative nomenclature sources where available

## Access & Services

Programmatic access is provided via publicly available REST services returning JSON for record lookup, hierarchy traversal, and search queries. Bulk database downloads support offline integration and local analytics. OBO, OWL, and OBO Graph JSON exports are available via the OBO DB ingest transformation for ontology/graph workflows.

## Licensing & Use

ITIS data are in the public domain. Users may copy and use the data freely with appropriate attribution recommended (e.g., citing ITIS and access date). See the access and data use policy page for details.

## Citation

Integrated Taxonomic Information System (ITIS). www.itis.gov (Accessed YYYY-MM-DD).

## Contact

General inquiries or technical questions: itiswebmaster@itis.gov. Additional support and documentation are available through the portal and web service description pages.