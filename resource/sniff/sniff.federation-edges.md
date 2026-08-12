---
category: GraphProduct
compatibility:
- standard: biolink
description: A Biolink-conformant KGX TSV edge file for the Sniff cross-species substrate,
  covering dog-to-human orthology and canine disease associations. Every edge carries
  provenance and an evidence level, and all edges with a knowledge level of prediction
  are excluded.
edge_count: 19823
format: kgx
id: sniff.federation-edges
name: Sniff KGX federation export, edges
original_source:
- relation_type: prov:hadPrimarySource
  source: sniff
predicates:
- biolink:orthologous_to
- biolink:causes
- biolink:gene_associated_with_condition
- biolink:associated_with_increased_likelihood_of
product_file_size: 5247253
product_url: https://sniffdog-data.s3.amazonaws.com/federation/kgx/sniff_edges.tsv
secondary_source:
- relation_type: prov:wasDerivedFrom
  source: clinvar
- relation_type: prov:wasDerivedFrom
  source: ensembl
- relation_type: prov:wasDerivedFrom
  source: mondo
layout: product_detail
---
