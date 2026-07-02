---
category: GraphProduct
description: RDF knowledge graph of the Experimental Natural Products Knowledge Graph,
  integrating experimental LC-MS/MS spectra and GNPS-based annotations, ISDB-LOTUS
  structural annotations, taxonomic and bioactivity metadata, cross-linked to Wikidata
  and served from the public GraphDB/SPARQL endpoint.
format: ttl
id: kg-enp.graph
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/legalcode
  label: CC0-1.0
name: ENPKG RDF Knowledge Graph
original_source:
- relation_type: prov:hadPrimarySource
  source: kg-enp
- relation_type: prov:hadPrimarySource
  source: gnps
- relation_type: prov:hadPrimarySource
  source: lotus
- relation_type: prov:hadPrimarySource
  source: wikidata
product_url: https://enpkg.commons-lab.org/graphdb
secondary_source:
- relation_type: prov:wasInfluencedBy
  source: open-tree-of-life
- relation_type: prov:wasInfluencedBy
  source: chembl
layout: product_detail
---
