---
category: ProcessProduct
description: The NLM-CKN ETL pipeline, which produces the knowledge graph as an ArangoDB
  archive from single-cell genomics results and source ontologies. It combines a data
  processing pipeline (DataFetcher, DataTransformer, TupleWriters, ResultsGraphBuilder)
  with an ontology processing pipeline (OntologyDownloader, OntologyGraphBuilder),
  then selects a relevant induced subgraph.
id: nlm-ckn.etl
name: nlm-ckn-etl
original_source:
- relation_type: prov:hadPrimarySource
  source: nlm-ckn
product_url: https://github.com/NIH-NLM/nlm-ckn-etl
layout: product_detail
---
