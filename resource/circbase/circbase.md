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
- non-coding RNA
homepage_url: https://www.circbase.org/
id: circbase
last_modified_date: '2026-09-23T00:00:00Z'
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
- category: Product
  description: Tab-delimited table of experimentally supported ncRNAs associated with
    drug resistance or drug response, manually curated from the literature, with ncRNA
    and drug identifiers, effect, target genes, pathways, detection method and condition.
  format: tsv
  id: ncrnadrug.drug-resistance-curated
  name: ncRNADrug Curated Drug Resistance Associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncrnadrug
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: circbase
  product_file_size: 15627539
  product_url: http://www.jianglab.cn/ncRNADrug/data_download/DR_Curated.txt
- category: Product
  description: Tab-delimited table of experimentally supported ncRNAs targeted by
    drugs (drugs that regulate ncRNA expression), manually curated from the literature,
    with ncRNA and drug identifiers, regulation direction, detection method and condition.
  format: tsv
  id: ncrnadrug.drug-target-curated
  name: ncRNADrug Curated Drug Target Associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncrnadrug
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: circbase
  product_file_size: 16640321
  product_url: http://www.jianglab.cn/ncRNADrug/data_download/DT_Curated.txt
- category: GraphProduct
  compression: gzip
  description: All NPInter v5.0 ncRNA interactions (literature-curated, high-throughput
    and computational) as a gzipped tab-delimited table of ncRNA, partner, interaction
    class, level, experiment, data source, organism, tissue or cell, and PubMed IDs.
  format: tsv
  id: npinter.interactions
  latest_version: '5.0'
  name: NPInter v5.0 All Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: npinter
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: circbase
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: ensembl
  product_file_size: 43319525
  product_url: http://bigdata.ibp.ac.cn/npinter5/download/file/interaction_NPInterv5.txt.gz
publications:
- authors:
  - Petar Glažar
  - Panagiotis Papavasileiou
  - Nikolaus Rajewsky
  doi: 10.1261/rna.043687.113
  id: doi:10.1261/rna.043687.113
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