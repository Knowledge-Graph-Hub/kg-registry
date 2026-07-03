---
category: GraphProduct
description: Live TRAPI/BioThings metadata endpoint for the Multiomics BigGIM-DrugResponse
  KP, exposing the multiomics knowledge graph served by the Multiomics Provider (built
  from GTEx, TCGA, and drug-response data, with additional clinical-trials, drug-approval
  and knowledge-resource inputs).
format: json
id: multiomics-kp.graph
name: Multiomics KP Knowledge Graph
original_source:
- relation_type: prov:hadPrimarySource
  source: multiomics-kp
- relation_type: prov:hadPrimarySource
  source: gtex
- relation_type: prov:hadPrimarySource
  source: tcga
- relation_type: prov:hadPrimarySource
  source: gdsc
- relation_type: prov:hadPrimarySource
  source: clinicaltrialsgov
- relation_type: prov:hadPrimarySource
  source: dailymed
- relation_type: prov:hadPrimarySource
  source: faers
product_url: https://biothings.transltr.io/biggim_drugresponse_kp/metadata
secondary_source:
- relation_type: prov:wasInfluencedBy
  source: aact
- relation_type: prov:wasInfluencedBy
  source: biogrid
- relation_type: prov:wasInfluencedBy
  source: huri
- relation_type: prov:wasInfluencedBy
  source: cellmarker
- relation_type: prov:wasInfluencedBy
  source: drugcentral
- relation_type: prov:wasInfluencedBy
  source: ttd
- relation_type: prov:wasInfluencedBy
  source: pubmed
layout: product_detail
---
