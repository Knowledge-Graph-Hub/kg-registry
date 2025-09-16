---
activity_status: active
category: Aggregator
creation_date: '2025-08-25T00:00:00Z'
description: circBase is a database and exploration portal for circular RNAs (circRNAs), aggregating published circRNA detection datasets across multiple species, tissues, and experimental conditions, and providing search, genomic context, expression summaries, and downloadable data plus scripts for circRNA discovery.
domains:
  - genomics
  - biological systems
  - organisms
id: circbase
last_modified_date: '2025-09-16T00:00:00Z'
layout: resource_detail
name: circBase
license:
  id: http://www.circbase.org/
  label: circBase site terms (dataset-specific; cite original studies)
publications:
  - id: doi:10.1261/rna.043687.113
    title: "circBase: a database for circular RNAs"
    year: '2014'
    journal: RNA
    preferred: true
products:
- category: GraphProduct
  description: RNA-KG as a Neo4j Dump
  format: neo4j
  id: rna-kg.kg.neo4j
  name: RNA-KG Neo4j Dump
  original_source:
  - dbsnp
  - cosmic
  - rnacentral
  - ensembl
  - circbase
  - chebi
  - pr
  - ncbigene
  - cl
  - go
  - mondo
  - hp
  - uberon
  - vo
  - pw
  - reactome
  - wikipathways
  product_file_size: 3976840239
  product_url: https://rna-kg.biodata.di.unimi.it/rnakgv20.dump
  secondary_source:
  - rna-kg
- category: GraphProduct
  description: RNA-KG Nodes in CSV format
  format: csv
  id: rna-kg.kg.nodes
  name: RNA-KG Nodes
  original_source:
  - dbsnp
  - cosmic
  - rnacentral
  - ensembl
  - circbase
  - chebi
  - pr
  - ncbigene
  - cl
  - go
  - mondo
  - hp
  - uberon
  - vo
  - pw
  - reactome
  - wikipathways
  product_file_size: 4424633304
  product_url: https://rna-kg.biodata.di.unimi.it/nodes.csv
  secondary_source:
  - rna-kg
- category: GraphProduct
  description: RNA-KG Edges in CSV format
  format: csv
  id: rna-kg.kg.edges
  name: RNA-KG Edges
  original_source:
  - dbsnp
  - cosmic
  - rnacentral
  - ensembl
  - circbase
  - chebi
  - pr
  - ncbigene
  - cl
  - go
  - mondo
  - hp
  - uberon
  - vo
  - pw
  - reactome
  - wikipathways
  product_file_size: 18370248815
  product_url: https://rna-kg.biodata.di.unimi.it/edges.csv
  secondary_source:
  - rna-kg

---
# circBase

This is an automatically generated stub page for circbase. Please update with proper information.