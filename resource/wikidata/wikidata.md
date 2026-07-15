---
activity_status: active
category: KnowledgeGraph
collection:
- okn
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: balhoff@renci.org
  - contact_type: github
    value: balhoff
  label: Jim Balhoff
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
  by both humans and machines
domains:
- general
homepage_url: https://www.wikidata.org/
id: wikidata
infores_id: wikidata
last_modified_date: '2026-06-18T00:00:00Z'
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
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_url: https://www.wikidata.org/
- category: ProgrammingInterface
  description: SPARQL endpoint for Wikidata
  format: http
  id: wikidata.sparql
  name: Wikidata SPARQL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_url: https://frink.apps.renci.org/wikidata/sparql
- category: GraphicalInterface
  description: Interactive web-based SPARQL query editor with example queries, visualization
    tools, and query assistance for exploring Wikidata
  format: http
  id: wikidata.query.editor
  name: Wikidata Query Service Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_url: https://query.wikidata.org/
- category: Product
  compression: gzip
  description: JSON dumps containing all Wikidata entities
  format: json
  id: wikidata.dumps.json
  name: Wikidata JSON Entity Dumps
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_file_size: 151566969874
  product_url: https://dumps.wikimedia.org/wikidatawiki/entities/latest-all.json.gz
- category: Product
  compression: gzip
  description: Canonical full-statement RDF dump in Turtle format (the "all" dump)
  format: ttl
  id: wikidata.dumps.rdf.full.ttl
  name: Wikidata RDF Full Dump (Turtle)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_file_size: 149370935070
  product_url: https://dumps.wikimedia.org/wikidatawiki/entities/latest-all.ttl.gz
- category: Product
  compression: gzip
  description: Canonical full-statement RDF dump in N-Triples format (the "all" dump)
  format: ntriples
  id: wikidata.dumps.rdf.full.nt
  name: Wikidata RDF Full Dump (N-Triples)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_file_size: 246159505683
  product_url: https://dumps.wikimedia.org/wikidatawiki/entities/latest-all.nt.gz
- category: Product
  compression: gzip
  description: RDF "truthy" dump in N-Triples format containing direct values from
    best-rank statements only
  format: ntriples
  id: wikidata.dumps.rdf.truthy.nt
  name: Wikidata RDF Truthy Dump (N-Triples)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_file_size: 69713859532
  product_url: https://dumps.wikimedia.org/wikidatawiki/entities/latest-truthy.nt.gz
- category: Product
  compression: gzip
  description: Lexeme namespace JSON dump
  format: json
  id: wikidata.dumps.lexemes.json
  name: Wikidata Lexeme JSON Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_file_size: 575745192
  product_url: https://dumps.wikimedia.org/wikidatawiki/entities/latest-lexemes.json.gz
- category: Product
  compression: gzip
  description: Lexeme namespace RDF dump in Turtle format
  format: ttl
  id: wikidata.dumps.lexemes.ttl
  name: Wikidata Lexeme RDF Dump (Turtle)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_file_size: 762464579
  product_url: https://dumps.wikimedia.org/wikidatawiki/entities/latest-lexemes.ttl.gz
- category: Product
  compression: gzip
  description: Lexeme namespace RDF dump in N-Triples format
  format: ntriples
  id: wikidata.dumps.lexemes.nt
  name: Wikidata Lexeme RDF Dump (N-Triples)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_file_size: 1401838999
  product_url: https://dumps.wikimedia.org/wikidatawiki/entities/latest-lexemes.nt.gz
- category: Product
  description: Full XML database dumps of Wikidata
  format: xml
  id: wikidata.dumps.xml
  name: Wikidata XML Dumps
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_url: https://dumps.wikimedia.org/wikidatawiki/
- category: Product
  description: Incremental add/change dumps that cover the previous 24 hours
  id: wikidata.dumps.incremental
  name: Wikidata Incremental Dumps
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_url: https://dumps.wikimedia.org/other/incr/wikidatawiki/
- category: ProgrammingInterface
  description: RESTful API providing programmatic access to Wikidata content, allowing
    reading and editing of items, properties, and statements
  format: http
  id: wikidata.api
  name: Wikidata Action API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_url: https://www.wikidata.org/w/api.php
- category: ProgrammingInterface
  description: REST API for accessing entity data in JSON format with content negotiation
    support
  format: http
  id: wikidata.entity.api
  name: Wikidata Entity Data API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_url: https://www.wikidata.org/wiki/Special:EntityData
- category: ProgrammingInterface
  description: SPARQL endpoint for ID Mappings
  format: http
  id: identifier-mappings.sparql
  name: ID Mappings SPARQL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: identifier-mappings
  product_url: https://apps.okn.us/identifier-mappings/sparql
- category: ProgrammingInterface
  description: Triple Pattern Fragments endpoint for ID Mappings
  format: http
  id: identifier-mappings.tpf
  name: ID Mappings TPF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: identifier-mappings
  product_url: https://apps.okn.us/ldf/identifier-mappings
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
- category: GraphProduct
  description: RDF dump of the Open Research Knowledge Graph distributed in N-Triples
    format.
  format: ntriples
  id: orkg.dump
  name: ORKG RDF Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orkg
  - relation_type: prov:hadPrimarySource
    source: wikidata
  - relation_type: prov:hadPrimarySource
    source: geonames
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: omit
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: stato
  - relation_type: prov:hadPrimarySource
    source: obi
  product_file_size: 642902930
  product_url: https://orkg.org/files/rdf-dumps/rdf-export-orkg.nt
- category: ProgrammingInterface
  description: Triple Pattern Fragments endpoint for Wikidata
  format: http
  id: wikidata.tpf
  name: Wikidata TPF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_url: https://frink.apps.renci.org/ldf/wikidata
- category: GraphicalInterface
  description: Main Raras portal for searching rare diseases, symptoms, genes, and
    patient communities
  format: http
  id: raras.portal
  name: Raras Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: raras
  - relation_type: prov:wasInformedBy
    source: mondo
  - relation_type: prov:wasInformedBy
    source: omim
  - relation_type: prov:wasInformedBy
    source: orphanet
  - relation_type: prov:wasInformedBy
    source: icd10
  - relation_type: prov:wasInformedBy
    source: icd11
  - relation_type: prov:wasInformedBy
    source: wikidata
  - relation_type: prov:wasInformedBy
    source: clinvar
  product_url: https://raras.org/
- category: GraphicalInterface
  description: Rare disease encyclopedia for browsing disease families, disease records,
    and related knowledge graph content
  format: http
  id: raras.encyclopedia
  name: Raras Encyclopedia
  original_source:
  - relation_type: prov:hadPrimarySource
    source: raras
  - relation_type: prov:wasInformedBy
    source: mondo
  - relation_type: prov:wasInformedBy
    source: omim
  - relation_type: prov:wasInformedBy
    source: orphanet
  - relation_type: prov:wasInformedBy
    source: icd10
  - relation_type: prov:wasInformedBy
    source: icd11
  - relation_type: prov:wasInformedBy
    source: wikidata
  - relation_type: prov:wasInformedBy
    source: clinvar
  product_url: https://raras.org/explorar
- category: GraphProduct
  description: KnowWhereGraph knowledge graph with 29+ billion RDF triples integrating
    30+ environmental and geospatial data layers accessible through SPARQL endpoint
  edge_count: 29000000000
  format: rdfxml
  id: knowwheregraph.graph
  name: KnowWhereGraph RDF Knowledge Graph
  node_count: 5000000000
  original_source:
  - relation_type: prov:hadPrimarySource
    source: knowwheregraph
  - relation_type: prov:wasDerivedFrom
    source: wikidata
  - relation_type: prov:hadPrimarySource
    source: bluesky
  - relation_type: prov:hadPrimarySource
    source: cdc-places
  - relation_type: prov:hadPrimarySource
    source: cdc-svi
  - relation_type: prov:hadPrimarySource
    source: cropland-data-layer
  - relation_type: prov:hadPrimarySource
    source: epa-aqs
  - relation_type: prov:hadPrimarySource
    source: gadm
  - relation_type: prov:hadPrimarySource
    source: gnis
  - relation_type: prov:hadPrimarySource
    source: hifld
  - relation_type: prov:hadPrimarySource
    source: mtbs
  - relation_type: prov:hadPrimarySource
    source: nhpn
  - relation_type: prov:hadPrimarySource
    source: nifc
  - relation_type: prov:hadPrimarySource
    source: noaa-hms
  - relation_type: prov:hadPrimarySource
    source: noaa-ncei
  - relation_type: prov:hadPrimarySource
    source: openfema
  - relation_type: prov:hadPrimarySource
    source: reliefweb
  - relation_type: prov:hadPrimarySource
    source: ssurgo
  - relation_type: prov:hadPrimarySource
    source: us-census
  - relation_type: prov:hadPrimarySource
    source: usdm
  - relation_type: prov:hadPrimarySource
    source: usgs-comcat
  product_url: https://knowwheregraph.org/
- category: GraphProduct
  description: Mappings between Wikidata entities and external identifiers, extracted
    and represented as RDF using standard RDF predicates
  format: ttl
  id: identifier-mappings.graph
  name: ID Mappings Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: identifier-mappings
  - relation_type: prov:wasDerivedFrom
    source: wikidata
  product_url: https://www.wikidata.org/
- category: GraphProduct
  description: RDF knowledge graph of the Experimental Natural Products Knowledge
    Graph, integrating experimental LC-MS/MS spectra and GNPS-based annotations, ISDB-LOTUS
    structural annotations, taxonomic and bioactivity metadata, cross-linked to Wikidata
    and served from the public GraphDB/SPARQL endpoint.
  format: ttl
  id: kg-enp.graph
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/legalcode
    label: CC0-1.0
  name: ENPKG RDF Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-enp
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: lotus
  - relation_type: prov:hadPrimarySource
    source: wikidata
  product_url: https://enpkg.commons-lab.org/graphdb
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: open-tree-of-life
  - relation_type: prov:wasInfluencedBy
    source: chembl
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-10: HTTP 406 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-07-15: HTTP 406 error
    when accessing file'
- category: Product
  compression: gzip
  description: PubChem substance information in ASN.1 format
  format: xml
  id: pubchem.substances.asn
  name: PubChem Substances ASN
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  product_url: https://ftp.ncbi.nlm.nih.gov/pubchem/Substance/CURRENT-Full/ASN/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: clinvar
  - relation_type: prov:wasInfluencedBy
    source: dbsnp
  - relation_type: prov:wasInfluencedBy
    source: dgidb
  - relation_type: prov:wasInfluencedBy
    source: mesh
  - relation_type: prov:wasInfluencedBy
    source: ncbigene
  - relation_type: prov:wasInfluencedBy
    source: omim
  - relation_type: prov:wasInfluencedBy
    source: pharmgkb
  - relation_type: prov:wasInfluencedBy
    source: reactome
  - relation_type: prov:wasInfluencedBy
    source: unichem
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: wikidata
  - relation_type: prov:wasInfluencedBy
    source: wikipathways
- category: Product
  compression: gzip
  description: PubChem substance information in SDF format
  format: sdf
  id: pubchem.substances.sdf
  name: PubChem Substances SDF
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  product_url: https://ftp.ncbi.nlm.nih.gov/pubchem/Substance/CURRENT-Full/SDF/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: clinvar
  - relation_type: prov:wasInfluencedBy
    source: dbsnp
  - relation_type: prov:wasInfluencedBy
    source: dgidb
  - relation_type: prov:wasInfluencedBy
    source: mesh
  - relation_type: prov:wasInfluencedBy
    source: ncbigene
  - relation_type: prov:wasInfluencedBy
    source: omim
  - relation_type: prov:wasInfluencedBy
    source: pharmgkb
  - relation_type: prov:wasInfluencedBy
    source: reactome
  - relation_type: prov:wasInfluencedBy
    source: unichem
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: wikidata
  - relation_type: prov:wasInfluencedBy
    source: wikipathways
repository: https://www.mediawiki.org/wiki/Wikibase
synonyms:
- Wikidata
- Wikidata Knowledge Base
---
## Automated Evaluation

- View the automated evaluation: [wikidata automated evaluation](wikidata_eval_automated.html)