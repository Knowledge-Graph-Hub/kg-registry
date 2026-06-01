---
activity_status: active
category: Aggregator
creation_date: '2025-08-25T00:00:00Z'
description: circBase is a database and exploration portal for circular RNAs (circRNAs),
  aggregating published circRNA detection datasets across multiple species, tissues,
  and experimental conditions, and providing search, genomic context, expression summaries,
  and downloadable data plus scripts for circRNA discovery.
domains:
- genomics
- biological systems
- organisms
homepage_url: https://www.circbase.org/
id: circbase
last_modified_date: '2026-06-01T00:00:00Z'
layout: resource_detail
license:
  id: http://www.circbase.org/
  label: circBase site terms (dataset-specific; cite original studies)
name: circBase
products:
- category: GraphProduct
  description: RNA-KG as a Neo4j Dump
  format: neo4j
  id: rna-kg.kg.neo4j
  name: RNA-KG Neo4j Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: circbase
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rna-kg
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_file_size: 3976840239
  product_url: https://rna-kg.biodata.di.unimi.it/rnakgv20.dump
- category: GraphicalInterface
  description: Web interface for searching and browsing circular RNA annotations across
    species.
  format: http
  id: circbase.portal
  name: circBase Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: circbase
  product_url: https://www.circbase.org/
- category: Product
  description: Bulk data downloads (BED/GFF and sequence files) for circular RNAs
    provided via the downloads CGI page.
  format: http
  id: circbase.downloads
  name: circBase Bulk Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: circbase
  product_url: https://www.circbase.org/cgi-bin/downloads.cgi
- category: DocumentationProduct
  description: Help and documentation describing circBase data sources, identifiers,
    and usage notes.
  format: http
  id: circbase.docs
  name: circBase Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: circbase
  product_url: https://www.circbase.org/doc/help_mod.html
- category: GraphProduct
  description: RNA-KG Nodes in CSV format
  format: csv
  id: rna-kg.kg.nodes
  name: RNA-KG Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: circbase
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rna-kg
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_file_size: 4424633304
  product_url: https://rna-kg.biodata.di.unimi.it/nodes.csv
- category: GraphProduct
  description: RNA-KG Edges in CSV format
  format: csv
  id: rna-kg.kg.edges
  name: RNA-KG Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: circbase
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rna-kg
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_file_size: 18370248815
  product_url: https://rna-kg.biodata.di.unimi.it/edges.csv
publications:
- id: doi:10.1261/rna.043687.113
  journal: RNA
  preferred: true
  title: 'circBase: a database for circular RNAs'
  year: '2014'
---
# circBase

circBase is a public aggregation and exploration resource for circular RNAs
(circRNAs). It brings together published circRNA detection datasets across
multiple species, tissues, and experimental settings, then exposes them through
search, genomic-context views, table filtering, sequence-based search, and bulk
downloads.

The live circBase site supports identifier, gene, and genomic-position queries,
dataset slicing through the table browser, and export of tables and FASTA
sequences. It also distributes the custom `find_circ` scripts and historical
dataset files used in early circRNA discovery workflows. In KG-Registry, the
RNA-KG products remain attached as downstream derivatives that reuse circBase as
one upstream source among several RNA resources.