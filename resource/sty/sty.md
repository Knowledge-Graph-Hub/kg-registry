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
last_modified_date: '2026-05-30T00:00:00Z'
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
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-22: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2026-06-24: No Content-Length
    header found'
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
synonyms:
- STY
- UMLS semantic types
---
# UMLS Semantic Types

The UMLS Semantic Types are part of the UMLS Semantic Network and provide a consistent high-level categorization for concepts represented in the UMLS Metathesaurus.

The Semantic Network couples these broad semantic categories with explicit semantic relations between types, giving the UMLS a compact upper-level structure for organizing concepts drawn from many vocabularies. NLM also publishes a Semantic Groups file that collapses the type system into coarser partitions for common interoperability and analysis tasks.