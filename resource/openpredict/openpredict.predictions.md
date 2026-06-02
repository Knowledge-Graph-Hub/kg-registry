---
category: Product
description: Pre-computed prediction outputs exposed through API operations for predicted
  drugs, predicted diseases, similar entities, and evidence paths
format: mixed
id: openpredict.predictions
name: OpenPredict Prediction Data
original_source:
- relation_type: prov:hadPrimarySource
  source: openpredict
product_url: https://openpredict.semanticscience.org/docs
secondary_source:
- relation_type: prov:used
  source: drugbank
- relation_type: prov:used
  source: go
- relation_type: prov:used
  source: hp
- relation_type: prov:used
  source: kegg
- relation_type: prov:used
  source: mesh
- relation_type: prov:used
  source: omim
warnings:
- Prediction results are exposed through POST/GET API operations rather than as a
  stable public bulk data file.
layout: product_detail
---
