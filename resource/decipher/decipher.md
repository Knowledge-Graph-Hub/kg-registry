---
activity_status: active
category: DataSource
contacts:
- category: Organization
  id: wellcome-sanger-institute
  label: Wellcome Sanger Institute
  homepage_url: https://www.sanger.ac.uk/
creation_date: '2026-06-18T00:00:00Z'
description: >-
  DECIPHER (DatabasE of genomiC varIation and Phenotype in Humans using Ensembl
  Resources) is a web-based platform, hosted at the Wellcome Sanger Institute,
  that aggregates and shares anonymized clinical and genomic data on
  submicroscopic chromosomal imbalances and other genomic variants in patients
  with rare developmental and genetic disorders. It links genomic variants to
  associated phenotypes (using Human Phenotype Ontology terms) to support
  interpretation of variant pathogenicity and clinical diagnosis. DECIPHER
  integrates Ensembl genome resources and an international consortium of clinical
  genetics centers. It is an upstream data source for the SRI-Reference Knowledge
  Graph and the Monarch Initiative.
domains:
- genomics
- clinical
- phenotype
- precision medicine
homepage_url: https://www.deciphergenomics.org/
id: decipher
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: DECIPHER
products:
- category: GraphicalInterface
  description: DECIPHER web interface for browsing genomic variants, syndromes, and
    associated phenotypes in patients with rare developmental disorders.
  format: http
  id: decipher.web
  name: DECIPHER web platform
  original_source:
  - relation_type: prov:hadPrimarySource
    source: decipher
  product_url: https://www.deciphergenomics.org/
- category: Product
  description: DECIPHER downloadable datasets, including aggregated patient variant
    and phenotype data and supporting genomic annotation files.
  format: http
  id: decipher.downloads
  name: DECIPHER downloadable data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: decipher
  product_url: https://www.deciphergenomics.org/about/downloads/data
publications:
- authors:
  - Helen V. Firth
  - Shola M. Richards
  - A. Paul Bevan
  - Stephen Clayton
  - Manuel Corpas
  - Diana Rajan
  - Steven Van Vooren
  - Yves Moreau
  - Roger M. Pettett
  - Nigel P. Carter
  doi: 10.1016/j.ajhg.2009.03.010
  id: https://pubmed.ncbi.nlm.nih.gov/19344873/
  journal: Am J Hum Genet
  preferred: true
  title: 'DECIPHER: Database of Chromosomal Imbalance and Phenotype in Humans Using
    Ensembl Resources'
  year: '2009'
---
# DECIPHER

DECIPHER (DatabasE of genomiC varIation and Phenotype in Humans using Ensembl
Resources) is a database and web platform hosted by the Wellcome Sanger Institute
that shares anonymized clinical and genomic data on submicroscopic chromosomal
imbalances and other genomic variants linked to patient phenotypes.

It supports interpretation of variant pathogenicity and clinical diagnosis of rare
developmental disorders, and serves as an upstream data source for the
SRI-Reference Knowledge Graph and the Monarch Initiative.
