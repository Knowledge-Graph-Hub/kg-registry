---
activity_status: active
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.nlm.nih.gov/research/umls/support.html
  label: UMLS and NLM Support Center
creation_date: '2026-02-26T00:00:00Z'
description: UMLS Semantic Types are the broad subject categories in the UMLS Semantic
  Network used to categorize concepts in the UMLS Metathesaurus.
domains:
- biomedical
homepage_url: https://www.nlm.nih.gov/research/umls/knowledge_sources/semantic_network/index.html
id: sty
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: https://lhncbc.nlm.nih.gov/semanticnetwork/
  label: Public Domain
name: UMLS Semantic Types
products:
- category: DocumentationProduct
  description: NLM documentation for the UMLS Semantic Network, including semantic
    type definitions and semantic relations.
  format: http
  id: sty.docs
  name: UMLS Semantic Network Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sty
  product_url: https://www.ncbi.nlm.nih.gov/books/NBK9679/
  warnings: []
- category: Product
  compression: gzip
  description: Current UMLS Semantic Network release archive from NLM.
  format: txt
  id: sty.semantic-network
  name: UMLS Semantic Network Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sty
  product_file_size: 86593
  product_url: https://www.nlm.nih.gov/research/umls/knowledge_sources/semantic_network/sn_current.tgz
- category: Product
  description: Semantic Groups mapping file that aggregates semantic types into coarser-grained
    categories.
  format: txt
  id: sty.semantic-groups
  name: UMLS Semantic Groups File
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sty
  product_url: https://www.nlm.nih.gov/research/umls/knowledge_sources/semantic_network/SemGroups.txt
  warnings: []
- category: Product
  description: sty Nodes TSV
  format: tsv
  id: obo-db-ingest.sty.tsv
  name: sty Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: sty
  product_file_size: 1583
  product_url: https://w3id.org/biopragmatics/resources/sty/sty.tsv
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Semantic Types Ontology (STY), produced by KG-Bioportal
    from the BioPortal submission. The archive contains STY_nodes.tsv and STY_edges.tsv.
  edge_count: 127
  format: kgx
  id: sty.kg-bioportal
  latest_version: 2025AB
  name: STY KGX graph (KG-Bioportal)
  node_count: 130
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sty
  product_file_size: 1363
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/STY.tar.gz
- category: Product
  compression: gzip
  description: Rich Release Format (RRF) file containing semantic type assignments
    with gzip compression
  format: txt
  id: medgen.mgsty
  name: MGSTY (Semantic Types)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: sty
  product_file_size: 1667323
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGSTY.RRF.gz
- category: Product
  description: CSV format data files directory with additional data exports
  format: csv
  id: medgen.csv
  name: CSV Data Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: clinpgx
  - relation_type: prov:hadPrimarySource
    source: gard
  - relation_type: prov:hadPrimarySource
    source: ghr
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: sty
  - relation_type: prov:hadPrimarySource
    source: umls
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/csv/
- category: Product
  description: sty OBO
  format: obo
  id: obo-db-ingest.sty.obo
  name: sty OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: sty
  product_file_size: 2265
  product_url: https://w3id.org/biopragmatics/resources/sty/sty.obo
- category: Product
  description: sty OWL
  format: owl
  id: obo-db-ingest.sty.owl
  name: sty OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: sty
  product_file_size: 3613
  product_url: https://w3id.org/biopragmatics/resources/sty/sty.owl
- category: Product
  description: sty OBO Graph JSON
  format: json
  id: obo-db-ingest.sty.json
  name: sty OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: sty
  product_file_size: 3145
  product_url: https://w3id.org/biopragmatics/resources/sty/sty.json
publications:
- authors:
  - McCray AT
  doi: 10.1002/cfg.255
  id: https://www.ncbi.nlm.nih.gov/pubmed/18629109
  journal: Comp Funct Genomics
  preferred: true
  title: An upper-level ontology for the biomedical domain
  year: '2003'
synonyms:
- STY
- UMLS semantic types
---
# UMLS Semantic Types

The UMLS Semantic Types are part of the UMLS Semantic Network and provide a consistent high-level categorization for concepts represented in the UMLS Metathesaurus.

The Semantic Network couples these broad semantic categories with explicit semantic relations between types, giving the UMLS a compact upper-level structure for organizing concepts drawn from many vocabularies. NLM also publishes a Semantic Groups file that collapses the type system into coarser partitions for common interoperability and analysis tasks.