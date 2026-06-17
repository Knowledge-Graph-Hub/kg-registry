---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: http://www.treefam.org/
  label: TreeFam
creation_date: '2026-06-17T00:00:00Z'
description: TreeFam (Tree families database) is a database of phylogenetic trees of
  animal gene families. It provides curated and automatically generated gene trees,
  inferred orthologs and paralogs, and gene family annotations across a wide range
  of animal species.
domains:
- genomics
- organisms
homepage_url: http://www.treefam.org/
id: treefam
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
name: TreeFam
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching gene families and their
    phylogenetic trees.
  format: http
  id: treefam.site
  is_public: true
  name: TreeFam Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: treefam
  product_url: http://www.treefam.org/
- category: Product
  description: Bulk downloads of gene trees, alignments, and family annotations.
  format: mixed
  id: treefam.downloads
  name: TreeFam Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: treefam
  product_url: http://www.treefam.org/download
publications:
- authors:
  - Fabian Schreiber
  - Mateus Patricio
  - Matthieu Muffato
  - Miguel Pignatelli
  - Alex Bateman
  doi: 10.1093/nar/gkt1055
  id: https://doi.org/10.1093/nar/gkt1055
  journal: Nucleic Acids Research
  preferred: true
  title: 'TreeFam v9: a new website, more species and orthology-on-the-fly'
  year: '2014'
---
# TreeFam

TreeFam (Tree families database) is a resource of phylogenetic trees for animal gene
families. It combines automated pipelines with manual curation to provide reliable gene
trees, from which orthology and paralogy relationships, gene family memberships, and
functional annotations are derived.

Content includes:

- Curated and automatically generated gene trees for animal gene families
- Inferred orthologs and paralogs across species
- Multiple sequence alignments and HMMs for gene families
- Bulk downloads of trees, alignments, and annotations

GeneCards integrates gene family and phylogenetic information from TreeFam.
