---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://wikimediafoundation.org/
  label: Wikimedia Foundation
creation_date: '2026-06-12T00:00:00Z'
description: Wikispecies is a free, collaboratively edited Wikimedia species directory
  containing taxonomic information, nomenclature, references, and related links for
  organisms.
domains:
- organisms
- general
homepage_url: https://species.wikimedia.org/wiki/Main_Page
id: wikispecies
last_modified_date: '2026-06-12T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC BY-SA 4.0
name: Wikispecies
products:
- category: GraphicalInterface
  description: Main Wikispecies web interface for browsing and editing taxonomic pages.
  format: http
  id: wikispecies.portal
  name: Wikispecies Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikispecies
  product_url: https://species.wikimedia.org/wiki/Main_Page
- category: ProgrammingInterface
  description: Public MediaWiki Action API endpoint for Wikispecies content.
  format: http
  id: wikispecies.api
  is_public: true
  name: Wikispecies MediaWiki Action API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikispecies
  product_url: https://species.wikimedia.org/w/api.php
- category: Product
  description: Latest Wikispecies XML dump directory from Wikimedia Downloads.
  format: xml
  id: wikispecies.dumps.latest
  name: Wikispecies Latest XML Dumps
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikispecies
  product_url: https://dumps.wikimedia.org/specieswiki/latest/
- category: GraphicalInterface
  description: Web interface that allows searching, browsing, and exploring food compounds
    and their properties.
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
---
Wikispecies is a Wikimedia Foundation project that provides collaboratively curated
species and taxonomy pages through a public wiki, MediaWiki API, and Wikimedia dump
infrastructure.