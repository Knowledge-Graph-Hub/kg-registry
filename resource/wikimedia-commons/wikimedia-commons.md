---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://commons.wikimedia.org/wiki/Commons:Contact_us
  id: wikimedia
  label: Wikimedia Foundation
creation_date: '2026-10-10T00:00:00Z'
description: Wikimedia Commons is a collaboratively built repository of freely licensed
  images, sounds, videos, and other media files, holding more than 149 million files
  that are used across Wikipedia and other Wikimedia projects. Its content is contributed
  and curated by a volunteer community and hosted by the Wikimedia Foundation. Through
  Structured Data on Commons, each file also has a Wikibase MediaInfo entity carrying
  multilingual captions and statements, such as what a file depicts, that use Wikidata
  properties and items.
domains:
- general
- humanities and cultural heritage
homepage_url: https://commons.wikimedia.org/
id: wikimedia-commons
last_modified_date: '2026-10-10T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC-BY-SA-4.0 (text); structured data CC0; media files under per-file free
    licenses
name: Wikimedia Commons
products:
- category: GraphicalInterface
  description: Wikimedia Commons website for browsing, searching, uploading, and describing
    media files.
  format: http
  id: wikimedia-commons.portal
  name: Wikimedia Commons Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikimedia-commons
  product_url: https://commons.wikimedia.org/
- category: ProgrammingInterface
  description: MediaWiki Action API for Wikimedia Commons, serving page and file metadata
    and, through the Wikibase modules, Structured Data on Commons MediaInfo entities.
  format: http
  id: wikimedia-commons.api
  is_public: true
  name: Wikimedia Commons Action API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikimedia-commons
  product_url: https://commons.wikimedia.org/w/api.php
- category: ProgrammingInterface
  description: Wikimedia Commons Query Service, a SPARQL endpoint and query interface
    over Structured Data on Commons statements. Requires logging in with a Commons
    account.
  format: http
  id: wikimedia-commons.query-service
  is_public: false
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: Wikimedia Commons Query Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikimedia-commons
  product_url: https://commons-query.wikimedia.org/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: wikidata
- category: Product
  description: Directory of the latest Wikimedia Commons database dumps, including
    page text XML and SQL table dumps.
  format: mixed
  id: wikimedia-commons.dumps
  name: Wikimedia Commons Database Dumps
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikimedia-commons
  product_url: https://dumps.wikimedia.org/commonswiki/latest/
- category: Product
  description: Latest dump of current Wikimedia Commons page text, including file description
    pages, as bzip2-compressed multistream XML.
  format: xml
  id: wikimedia-commons.pages-articles
  name: Wikimedia Commons Pages-Articles Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikimedia-commons
  product_file_size: 126904073228
  product_url: https://dumps.wikimedia.org/commonswiki/latest/commonswiki-latest-pages-articles-multistream.xml.bz2
- category: Product
  compression: gzip
  description: SQL dump of the image table, with metadata for every file on Commons
    (name, size, dimensions, media type, and upload details).
  format: mysql
  id: wikimedia-commons.image-table
  name: Wikimedia Commons Image Table Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikimedia-commons
  product_file_size: 18622844065
  product_url: https://dumps.wikimedia.org/commonswiki/latest/commonswiki-latest-image.sql.gz
- category: Product
  compression: gzip
  description: SQL dump of the globalimagelinks table, recording where Commons files
    are used across all Wikimedia wikis.
  format: mysql
  id: wikimedia-commons.globalimagelinks
  name: Wikimedia Commons Global Image Links Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikimedia-commons
  product_file_size: 11585333125
  product_url: https://dumps.wikimedia.org/commonswiki/latest/commonswiki-latest-globalimagelinks.sql.gz
- category: Product
  compression: gzip
  description: Weekly dump of all Structured Data on Commons MediaInfo entities (captions
    and statements) in JSON.
  format: json
  id: wikimedia-commons.mediainfo.json
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: Structured Data on Commons Dump (JSON)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikimedia-commons
  product_file_size: 78893159156
  product_url: https://dumps.wikimedia.org/other/wikibase/commonswiki/latest-mediainfo.json.gz
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: wikidata
- category: GraphProduct
  compression: gzip
  description: Weekly dump of all Structured Data on Commons MediaInfo entities as
    RDF in Turtle.
  format: ttl
  id: wikimedia-commons.mediainfo.ttl
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: Structured Data on Commons Dump (Turtle)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikimedia-commons
  product_file_size: 114887363530
  product_url: https://dumps.wikimedia.org/other/wikibase/commonswiki/latest-mediainfo.ttl.gz
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: wikidata
- category: DocumentationProduct
  description: Commons licensing policy, explaining which free licenses are accepted
    for media files.
  format: http
  id: wikimedia-commons.licensing
  name: Commons Licensing Policy
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikimedia-commons
  product_url: https://commons.wikimedia.org/wiki/Commons:Licensing
publications:
- authors:
  - Yihan Yu
  - David W. McDonald
  doi: 10.1145/3555766
  id: doi:10.1145/3555766
  journal: Proceedings of the ACM on Human-Computer Interaction
  title: 'Unpacking Stitching between Wikipedia and Wikimedia Commons: Barriers to
    Cross-Platform Collaboration'
  year: '2022'
- authors:
  - Elizabeth Joan Kelly
  doi: 10.18438/eblip29575
  id: doi:10.18438/eblip29575
  journal: Evidence Based Library and Information Practice
  title: Reuse of Wikimedia Commons Cultural Heritage Images on the Wider Web
  year: '2019'
repository: https://github.com/wikimedia/mediawiki-extensions-WikibaseMediaInfo
synonyms:
- Commons
- Structured Data on Commons
---
# Wikimedia Commons

Wikimedia Commons is the shared media repository of the Wikimedia projects. It holds more than 149 million freely licensed images, sounds, videos, and other files, which Wikipedia and its sister projects embed directly. There is no central editorial board: volunteers upload, describe, categorize, and curate the files, and the Wikimedia Foundation hosts the site.

## Structured data

Through Structured Data on Commons, every file has a Wikibase MediaInfo entity, whose identifier is `M` followed by the file's page id. These entities hold multilingual captions and statements, such as what a file depicts, built from Wikidata properties and items. The software is the WikibaseMediaInfo MediaWiki extension. Structured data can be retrieved through the Action API, queried with SPARQL in the Wikimedia Commons Query Service (which requires a Commons login), or downloaded in weekly JSON, Turtle, and N-Triples dumps.

## Licensing

Commons accepts only free content. Each media file carries its own license (for example CC0, CC BY, CC BY-SA, or public domain), stated on its description page. Unstructured text is available under CC BY-SA 4.0, and all structured data in the file namespace is under CC0.

## Use in KG-Registry

DBpedia extracted Commons file metadata as the DBpedia Commons dataset (Vaidya et al. 2015).
