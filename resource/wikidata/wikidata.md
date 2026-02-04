---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: wikidata-l@lists.wikimedia.org
  - contact_type: url
    value: https://www.wikidata.org/wiki/Wikidata:Contact
  id: wikimedia
  label: Wikimedia Foundation
creation_date: '2025-10-31T00:00:00Z'
description: Wikidata is a free and open knowledge base that can be read and edited
  by both humans and machines. Acting as central storage for the structured data of
  Wikimedia sister projects including Wikipedia, Wikivoyage, Wiktionary, Wikisource,
  and others, it contains over 119 million data items that anyone can edit. Wikidata
  provides structured, machine-readable data under a free license (CC0), supports
  multilingual content, and can be interlinked with other open data sets on the linked
  data web. The content is available through standard formats, SPARQL queries, and
  APIs.
domains:
- general
homepage_url: https://www.wikidata.org/
id: wikidata
infores_id: wikidata
last_modified_date: '2026-02-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0 Public Domain Dedication
name: Wikidata
products:
- category: GraphicalInterface
  description: Main web interface for browsing, searching, and editing Wikidata items,
    properties, and statements with over 119 million data items
  format: http
  id: wikidata.portal
  name: Wikidata Web Portal
  product_url: https://www.wikidata.org/
- category: ProgrammingInterface
  description: SPARQL endpoint for querying Wikidata using semantic web query language,
    enabling complex queries across the knowledge graph
  format: http
  id: wikidata.sparql
  name: Wikidata SPARQL Query Service
  product_url: https://query.wikidata.org/sparql
- category: GraphicalInterface
  description: Interactive web-based SPARQL query editor with example queries, visualization
    tools, and query assistance for exploring Wikidata
  format: http
  id: wikidata.query.editor
  name: Wikidata Query Service Interface
  product_url: https://query.wikidata.org/
- category: Product
  compression: gzip
  description: JSON dumps containing all Wikidata entities
  format: json
  id: wikidata.dumps.json
  name: Wikidata JSON Entity Dumps
  product_url: https://dumps.wikimedia.org/wikidatawiki/entities/latest-all.json.gz
- category: Product
  compression: gzip
  description: Canonical full-statement RDF dump in Turtle format (the "all" dump)
  format: ttl
  id: wikidata.dumps.rdf.full.ttl
  name: Wikidata RDF Full Dump (Turtle)
  product_url: https://dumps.wikimedia.org/wikidatawiki/entities/latest-all.ttl.gz
- category: Product
  compression: gzip
  description: Canonical full-statement RDF dump in N-Triples format (the "all" dump)
  format: ntriples
  id: wikidata.dumps.rdf.full.nt
  name: Wikidata RDF Full Dump (N-Triples)
  product_url: https://dumps.wikimedia.org/wikidatawiki/entities/latest-all.nt.gz
- category: Product
  compression: gzip
  description: RDF "truthy" dump in N-Triples format containing direct values from
    best-rank statements only
  format: ntriples
  id: wikidata.dumps.rdf.truthy.nt
  name: Wikidata RDF Truthy Dump (N-Triples)
  product_url: https://dumps.wikimedia.org/wikidatawiki/entities/latest-truthy.nt.gz
- category: Product
  compression: gzip
  description: Lexeme namespace JSON dump
  format: json
  id: wikidata.dumps.lexemes.json
  name: Wikidata Lexeme JSON Dump
  product_url: https://dumps.wikimedia.org/wikidatawiki/entities/latest-lexemes.json.gz
- category: Product
  compression: gzip
  description: Lexeme namespace RDF dump in Turtle format
  format: ttl
  id: wikidata.dumps.lexemes.ttl
  name: Wikidata Lexeme RDF Dump (Turtle)
  product_url: https://dumps.wikimedia.org/wikidatawiki/entities/latest-lexemes.ttl.gz
- category: Product
  compression: gzip
  description: Lexeme namespace RDF dump in N-Triples format
  format: ntriples
  id: wikidata.dumps.lexemes.nt
  name: Wikidata Lexeme RDF Dump (N-Triples)
  product_url: https://dumps.wikimedia.org/wikidatawiki/entities/latest-lexemes.nt.gz
- category: Product
  description: Full XML database dumps of Wikidata
  format: xml
  id: wikidata.dumps.xml
  name: Wikidata XML Dumps
  product_url: https://dumps.wikimedia.org/wikidatawiki/
- category: Product
  description: Incremental add/change dumps that cover the previous 24 hours
  id: wikidata.dumps.incremental
  name: Wikidata Incremental Dumps
  product_url: https://dumps.wikimedia.org/other/incr/wikidatawiki/
- category: ProgrammingInterface
  description: RESTful API providing programmatic access to Wikidata content, allowing
    reading and editing of items, properties, and statements
  format: http
  id: wikidata.api
  name: Wikidata Action API
  product_url: https://www.wikidata.org/w/api.php
- category: ProgrammingInterface
  description: REST API for accessing entity data in JSON format with content negotiation
    support
  format: http
  id: wikidata.entity.api
  name: Wikidata Entity Data API
  product_url: https://www.wikidata.org/wiki/Special:EntityData
- category: ProgrammingInterface
  description: SPARQL endpoint for ID Mappings
  id: identifier-mappings.sparql
  name: ID Mappings SPARQL
  original_source:
  - identifier-mappings
  - wikidata
  product_url: https://frink.apps.renci.org/identifier-mappings/sparql
- category: ProgrammingInterface
  description: Triple Pattern Fragments endpoint for ID Mappings
  id: identifier-mappings.tpf
  name: ID Mappings TPF
  original_source:
  - identifier-mappings
  - wikidata
  product_url: https://frink.apps.renci.org/ldf/identifier-mappings
repository: https://www.mediawiki.org/wiki/Wikibase
synonyms:
- Wikidata
- Wikidata Knowledge Base
---
## Automated Evaluation

- View the automated evaluation: [wikidata automated evaluation](wikidata_eval_automated.html)
