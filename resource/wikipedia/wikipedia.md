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
- category: GraphicalInterface
  description: Web-based interface for searching and browsing comprehensive gene-centric
    information integrating data from over 200 sources
  format: http
  id: genecards.web.interface
  name: GeneCards Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: aminode
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: cdd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: craft
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: fabric
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: gard
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: geneorganizer
  - relation_type: prov:hadPrimarySource
    source: genomernai
  - relation_type: prov:hadPrimarySource
    source: glyconnect
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: humancyc
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: iid
  - relation_type: prov:hadPrimarySource
    source: imgt
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadisease
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: nextprot
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pirsf
  - relation_type: prov:hadPrimarySource
    source: prosite
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  - relation_type: prov:hadPrimarySource
    source: proteopedia
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: scop
  - relation_type: prov:hadPrimarySource
    source: sfld
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: treefam
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ucnebase
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vista
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_url: https://www.genecards.org/
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