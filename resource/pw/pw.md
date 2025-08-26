---
activity_status: active
category: DataModel
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: gthayman@mcw.edu
  - contact_type: github
    value: gthayman
  label: G. Thomas Hayman
  orcid: 0000-0002-9553-7227
creation_date: '2025-08-20T00:00:00Z'
description: The Pathway Ontology (PW) is a controlled vocabulary for biological pathways,
  including canonical, altered, and disease pathways. Developed at the Rat Genome
  Database, it supports standardized annotation of rat, human, and mouse genes and
  enables navigation across pathway suites and interactive pathway diagrams.
domains:
- biological systems
homepage_url: https://rgd.mcw.edu/rgdweb/ontology/search.html
id: pw
last_modified_date: '2025-08-20T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: Pathway Ontology
products:
- category: DataModelProduct
  description: PW OWL release
  format: owl
  id: pw.owl
  name: PW OWL
  original_source:
  - pw
  - iao
  - go
  product_file_size: 5403526
  product_url: http://purl.obolibrary.org/obo/pw.owl
  secondary_source:
  - pw
- category: DataModelProduct
  description: PW OBO release
  format: obo
  id: pw.obo
  name: PW OBO
  original_source:
  - pw
  - iao
  - go
  product_file_size: 1347302
  product_url: http://purl.obolibrary.org/obo/pw.obo
  secondary_source:
  - pw
- category: GraphProduct
  description: PheKnowLator graph files, including subsets with and without inverse
    relations.
  format: owl
  id: pheknowlator.graph
  latest_version: current_build
  name: PheKnowLator graph
  original_source:
  - cl
  - clo
  - chebi
  - go
  - hp
  - mondo
  - pw
  - pr
  - ro
  - so
  - uberon
  - vo
  - bioportal
  - clinvar
  - ctd
  - disgenet
  - ensembl
  - genemania
  - hgnc
  - hpa
  - ncbigene
  - medgen
  - reactome
  - string
  - uniprot
  product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
  secondary_source:
  - pheknowlator
  versions:
  - v1.0.0
  - v2.0.0
  - v2.1.0
  - v3.0.2
  - v4.0.0
  - current_build
- description: RNA-KG as a Neo4j Dump
  dump_format: neo4j
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
- description: RNA-KG Nodes in CSV format
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
- description: RNA-KG Edges in CSV format
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
publications:
- authors:
  - Petri V
  - Jayaraman P
  - Tutaj M
  - Hayman GT
  - Smith JR
  - De Pons J
  - Laulederkind SJF
  - et al.
  doi: 10.1186/2041-1480-5-7
  id: doi:10.1186/2041-1480-5-7
  journal: Journal of Biomedical Semantics
  preferred: true
  title: The pathway ontology - updates and applications
  year: '2014'
repository: https://github.com/rat-genome-database/PW-Pathway-Ontology
---
The Pathway Ontology provides standard terms for annotating genes to pathways and supports
integration and exploration of pathway knowledge across species.