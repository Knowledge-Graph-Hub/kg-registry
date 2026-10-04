---
category: GraphProduct
compatibility:
- standard: biolink
  version: 4.2.1
description: KGX JSONL nodes and edges files for the OHD@Carolina Automat graph (build
  f627ebbefd242454, source version 2024-11-18, published 2025-10-06), with 27,356
  nodes and 22,732,570 edges. Edges use biolink:positively_correlated_with (22,352,823)
  and biolink:negatively_correlated_with (379,747).
edge_count: 22732570
format: kgx-jsonl
id: ohd-carolina.graph
infores_id: automat-openhealthdata-carolina
name: OHD@Carolina Automat KGX Graph
node_categories:
- biolink:Disease
- biolink:PhenotypicFeature
- biolink:Drug
- biolink:SmallMolecule
- biolink:MolecularMixture
- biolink:ChemicalEntity
- biolink:Protein
- biolink:OrganismTaxon
- biolink:ComplexMolecularMixture
- biolink:Gene
- biolink:InformationContentEntity
node_count: 27356
original_source:
- relation_type: prov:hadPrimarySource
  source: ohd-carolina
- relation_type: prov:wasInfluencedBy
  source: ohdsi
predicates:
- biolink:positively_correlated_with
- biolink:negatively_correlated_with
product_url: https://stars.renci.org/var/plater/bl-4.2.1/OHD_Carolina_Automat/f627ebbefd242454/
versions:
- f627ebbefd242454
layout: product_detail
---
