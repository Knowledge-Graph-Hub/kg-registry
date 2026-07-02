---
category: GraphProduct
description: Integrated rare-disease knowledge graph produced by the RD-Clust workflow,
  connecting rare diseases to genes, phenotypes, Gene Ontology terms, drugs/ligands,
  and pathway interactions. Distributed as the processed disease ontograph within
  the RD-Clust repository.
format: http
id: ncatsgardkg.graph
name: NCATS GARD Knowledge Graph
original_source:
- relation_type: prov:hadPrimarySource
  source: ncatsgardkg
- relation_type: prov:hadPrimarySource
  source: gard
product_url: https://github.com/ncats/RD-Clust/tree/main/data/processed
secondary_source:
- relation_type: prov:wasInfluencedBy
  source: hp
- relation_type: prov:wasInfluencedBy
  source: go
- relation_type: prov:wasInfluencedBy
  source: mondo
- relation_type: prov:wasInfluencedBy
  source: orphanet
- relation_type: prov:wasInfluencedBy
  source: ncbigene
- relation_type: prov:wasInfluencedBy
  source: pharos
- relation_type: prov:wasInfluencedBy
  source: chembl
- relation_type: prov:wasInfluencedBy
  source: chebi
- relation_type: prov:wasInfluencedBy
  source: pubchem
- relation_type: prov:wasInfluencedBy
  source: pathwaycommons
layout: product_detail
---
