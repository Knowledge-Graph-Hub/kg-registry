---
category: GraphProduct
compatibility:
- standard: biolink
description: A Biolink-conformant KGX TSV node file for the Sniff cross-species substrate,
  covering dog and human genes and canine and human diseases. Part of the facts-only
  federation bundle intended for ingest into other knowledge graphs.
format: kgx
id: sniff.federation-nodes
name: Sniff KGX federation export, nodes
node_categories:
- biolink:Gene
- biolink:Disease
node_count: 36915
original_source:
- relation_type: prov:hadPrimarySource
  source: sniff
product_file_size: 3726803
product_url: https://sniffdog-data.s3.amazonaws.com/federation/kgx/sniff_nodes.tsv
secondary_source:
- relation_type: prov:wasDerivedFrom
  source: clinvar
- relation_type: prov:wasDerivedFrom
  source: ensembl
- relation_type: prov:wasDerivedFrom
  source: mondo
layout: product_detail
---
