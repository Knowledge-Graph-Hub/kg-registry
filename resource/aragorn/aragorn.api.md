---
category: ProgrammingInterface
description: RENCI-hosted TRAPI endpoint (/query, /asyncquery) for the ARAGORN ARA,
  with Swagger documentation. Queries are answered by Strider over the knowledge providers
  it has registered (here including the Automat ROBOKOP KG, CAM-KP, ICEES, Ubergraph,
  GeLiNEA, Genetics KP, MolePro, OpenPredict and Text Mining KP co-occurrence), plus
  direct ROBOKOP KG lookups for inferred queries, SRI Node Normalizer identifier normalization
  and OmniCorp literature co-occurrence overlays for scoring.
format: http
id: aragorn.api
name: ARAGORN API
original_source:
- relation_type: prov:hadPrimarySource
  source: aragorn
- relation_type: prov:hadPrimarySource
  source: robokop
- relation_type: prov:hadPrimarySource
  source: automat
- relation_type: prov:hadPrimarySource
  source: omnicorp
- relation_type: prov:hadPrimarySource
  source: node-normalizer
- relation_type: prov:hadPrimarySource
  source: cam-kp
- relation_type: prov:hadPrimarySource
  source: icees-kg
- relation_type: prov:hadPrimarySource
  source: ubergraph
- relation_type: prov:hadPrimarySource
  source: gelinea
- relation_type: prov:hadPrimarySource
  source: genetics-kp
- relation_type: prov:hadPrimarySource
  source: molepro
- relation_type: prov:hadPrimarySource
  source: openpredict
- relation_type: prov:hadPrimarySource
  source: text-mining-kp
- relation_type: prov:hadPrimarySource
  source: strider
product_url: https://aragorn.renci.org/docs
layout: product_detail
---
