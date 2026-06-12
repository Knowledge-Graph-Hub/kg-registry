---
activity_status: active
category: DataSource
creation_date: '2026-03-11T00:00:00Z'
description: Wikipedia is a free, collaboratively edited multilingual encyclopedia
  published by the Wikimedia movement. Its article content is widely reused as an
  open reference source and serves as a primary upstream source for derivative resources
  such as DBpedia. Wikipedia content is accessible through the web portal, public
  APIs, and Wikimedia dump infrastructure.
domains:
- general
homepage_url: https://www.wikipedia.org/
id: wikipedia
last_modified_date: '2026-03-11T00:00:00Z'
layout: resource_detail
name: Wikipedia
products:
- category: GraphicalInterface
  description: Main Wikipedia web portal for browsing and searching article content
    across language editions.
  format: http
  id: wikipedia.portal
  name: Wikipedia Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  product_url: https://www.wikipedia.org/
- category: ProgrammingInterface
  description: Public MediaWiki Action API for querying and editing Wikipedia content.
    The exact modules vary by wiki; this entry uses the English Wikipedia endpoint
    as a canonical example.
  format: http
  id: wikipedia.api
  is_public: true
  name: Wikipedia MediaWiki Action API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  product_url: https://en.wikipedia.org/w/api.php
- category: ProgrammingInterface
  description: Public Wikimedia REST API for machine-readable Wikipedia content and
    metadata. This entry uses the English Wikipedia REST base path as a canonical
    example.
  format: http
  id: wikipedia.rest
  is_public: true
  name: Wikipedia Wikimedia REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  product_url: https://en.wikipedia.org/api/rest_v1/
- category: Product
  description: English Wikipedia current-content XML export directory from the Wikimedia
    dump service. This dump contains the latest revision of each exported page, split
    across multiple `.xml.bz2` files.
  format: xml
  id: wikipedia.dumps.enwiki.current
  name: English Wikipedia Current Content XML Dumps
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  product_url: https://dumps.wikimedia.org/other/mediawiki_content_current/enwiki/2026-03-01/xml/bzip2/
- category: Product
  description: English Wikipedia full revision-history XML export directory from the
    Wikimedia dump service. This dump contains complete page revision histories, split
    across multiple `.xml.bz2` files.
  format: xml
  id: wikipedia.dumps.enwiki.history
  name: English Wikipedia Full Revision History XML Dumps
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  product_url: https://dumps.wikimedia.org/other/mediawiki_content_history/enwiki/2026-03-01/xml/bzip2/
- category: GraphProduct
  description: Databus collection for the latest core DBpedia release used by the
    main SPARQL endpoint and linked data interface.
  format: http
  id: dbpedia.latest-core
  name: DBpedia Latest Core Collection
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbpedia
  - relation_type: prov:wasDerivedFrom
    source: wikipedia
  - relation_type: prov:wasDerivedFrom
    source: wikidata
  product_file_size: 18605
  product_url: https://databus.dbpedia.org/dbpedia/collections/latest-core
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
synonyms:
- English Wikipedia
---
# Wikipedia

## Overview

Wikipedia is a multilingual, collaboratively edited encyclopedia published on the
web by the Wikimedia movement. In addition to its browser interface, Wikimedia
provides public API access and regular bulk dumps of Wikipedia content. This page
tracks English Wikipedia dump products rather than the full multilingual Wikimedia
dump catalog.