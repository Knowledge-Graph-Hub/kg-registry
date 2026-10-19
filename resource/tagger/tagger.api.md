---
category: ProgrammingInterface
description: Public Tagger web service. Endpoints such as GetEntities and GetHTML
  accept a document and a list of entity types (NCBI Taxonomy IDs for proteins of
  a species, or negative type codes such as -1 for chemicals, -22 for GO cellular
  components, -25 for BTO tissues, -26 for diseases) and return the recognized entities
  with their normalized identifiers as TSV, XML, or annotated HTML. The service uses
  the reduced tagger dictionary. The bare host returns HTTP 400; queries must include
  an endpoint and parameters.
format: http
id: tagger.api
name: Tagger Web Service
original_source:
- relation_type: prov:hadPrimarySource
  source: tagger
product_url: https://tagger.jensenlab.org/GetEntities?document=TP53&entity_types=9606&format=tsv
secondary_source:
- relation_type: prov:wasDerivedFrom
  source: tagger.dictionary
layout: product_detail
---
