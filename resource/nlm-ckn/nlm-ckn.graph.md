---
category: GraphProduct
description: The NLM-CKN knowledge graph of cellular phenotypes. It is built from
  triple assertions (subject-predicate-object) that link single-cell genomics experimental
  data (from the CELLxGENE Census) and computationally derived NS-Forest marker genes
  to the Cell Ontology and other reference ontologies, augmented with literature-derived
  assertions from text mining/NLP. The graph is produced by the NLM-CKN ETL pipeline
  as an ArangoDB archive and served via the web application at https://nlm-ckn.org.
format: http
id: nlm-ckn.graph
name: nlm-ckn-graph
original_source:
- relation_type: prov:hadPrimarySource
  source: nlm-ckn
- relation_type: prov:hadPrimarySource
  source: cellxgene
- relation_type: prov:hadPrimarySource
  source: pubmed
product_url: https://github.com/NIH-NLM/cell-kn-mvp
secondary_source:
- relation_type: prov:wasInfluencedBy
  source: cl
- relation_type: prov:wasInfluencedBy
  source: uberon
- relation_type: prov:wasInfluencedBy
  source: pato
- relation_type: prov:wasInfluencedBy
  source: mondo
- relation_type: prov:wasInfluencedBy
  source: hsapdv
layout: product_detail
---
