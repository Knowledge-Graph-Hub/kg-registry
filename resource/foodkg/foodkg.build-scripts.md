---
category: ProcessProduct
description: Python scripts that build FoodKG from the Recipe1M recipe dataset (layer1.json
  and det_ingrs.json, acquired manually), USDA nutrient data and FoodOn (downloaded
  automatically). Outputs are three TriG files, usda-links.trig (about 4.1 million
  triples), foodon-links.trig (about 30 thousand triples) and foodkg-core.trig (about
  63 million triples), intended for loading into Blazegraph.
format: python
id: foodkg.build-scripts
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache-2.0
name: FoodKG Construction Scripts
original_source:
- relation_type: prov:hadPrimarySource
  source: foodkg
- relation_type: prov:hadPrimarySource
  source: foodon
- relation_type: prov:hadPrimarySource
  source: uo
- relation_type: prov:wasDerivedFrom
  source: fooddata-central
product_url: https://github.com/foodkg/foodkg.github.io/tree/master/src
layout: product_detail
---
