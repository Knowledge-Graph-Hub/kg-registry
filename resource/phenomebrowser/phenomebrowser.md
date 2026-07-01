---
activity_status: active
category: DataSource
creation_date: '2026-06-18T00:00:00Z'
description: PhenomeBrowser is a web resource from the Hoehndorf group that provides
  drug-phenotype and gene-phenotype associations integrated across multiple species
  within the PhenomeNET ecosystem. It applies ontology-based phenotype representations
  and cross-species semantic similarity to connect genes, drugs, diseases, and their
  phenotypic manifestations. PhenomeBrowser serves as the upstream source of the GP-KG
  knowledge graph used for drug repurposing.
domains:
- phenotype
- genomics
- pharmacology
- systems biology
homepage_url: http://phenomebrowser.net/
id: phenomebrowser
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: PhenomeBrowser
products:
- category: GraphicalInterface
  description: PhenomeBrowser web portal for searching and browsing drug-phenotype
    and gene-phenotype associations integrated across species via the PhenomeNET ecosystem.
  format: http
  id: phenomebrowser.web
  name: PhenomeBrowser Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: phenomebrowser
  product_url: http://phenomebrowser.net/
- category: GraphProduct
  description: GP_KG.txt
  edge_count: 1246726
  format: txt
  id: gp-kg.graph
  name: GP-KG
  node_count: 61146
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gp-kg
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: mgi
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: goa
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: umls
  - relation_type: prov:wasDerivedFrom
    source: uberon
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: faers
  - relation_type: prov:wasDerivedFrom
    source: phenomebrowser
  - relation_type: prov:wasDerivedFrom
    source: treatkb
  product_file_size: 48397035
  product_url: http://nlp.case.edu/public/data/GPKG-Predict/data/GP_KG.txt
publications:
- authors:
  - "Rodr\xEDguez-Garc\xEDa M\xC1"
  - Gkoutos GV
  - Schofield PN
  - Hoehndorf R
  doi: 10.1186/s13326-017-0167-4
  id: https://www.ncbi.nlm.nih.gov/pubmed/29258588
  journal: J Biomed Semantics
  preferred: true
  title: Integrating phenotype ontologies with PhenomeNET
  year: '2017'
---
## Overview

PhenomeBrowser is part of the PhenomeNET ecosystem developed by the Hoehndorf
group. It integrates gene-phenotype and drug-phenotype associations across
multiple species, using ontology-based phenotype representations and
cross-species semantic similarity to relate genes, drugs, diseases, and their
phenotypes.

## Use as a Data Source

PhenomeBrowser is the upstream primary source of the GP-KG knowledge graph,
which is used for computational drug repurposing.

## Access

The PhenomeBrowser web portal is available at http://phenomebrowser.net/.

## Licensing & Citation

No explicit data license was identified for PhenomeBrowser. When using the
resource, please cite the associated PhenomeNET publication.