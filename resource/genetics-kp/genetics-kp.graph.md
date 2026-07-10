---
category: GraphProduct
description: TRAPI knowledge graph served by the Genetics KP, exposing gene/disease
  and gene/phenotype associations computed from large-scale human genetics data (e.g.
  Genebass exome association statistics aggregated with methods such as MAGMA and
  the HuGE calculator) and integrated curated gene-condition resources. The linked
  endpoint returns the meta knowledge graph describing the served node and edge types.
format: json
id: genetics-kp.graph
name: Genetics KP Knowledge Graph
original_source:
- relation_type: prov:hadPrimarySource
  source: genetics-kp
- relation_type: prov:hadPrimarySource
  source: genebass
product_file_size: 3538
product_url: https://genetics-kp.transltr.io/genetics_provider/trapi/v1.5/meta_knowledge_graph
secondary_source:
- relation_type: prov:wasInfluencedBy
  source: gencc
- relation_type: prov:wasInfluencedBy
  source: clinvar
- relation_type: prov:wasInfluencedBy
  source: clingen
layout: product_detail
---
