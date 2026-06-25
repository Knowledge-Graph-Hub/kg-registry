---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://remap.univ-amu.fr/contact_page
  label: ReMap Team
creation_date: '2026-05-21T00:00:00Z'
description: ReMap is a curated regulatory genomics resource that integrates public
  DNA-binding sequencing experiments to produce high-quality catalogs of transcriptional
  regulator binding regions across human, mouse, Drosophila, and Arabidopsis.
domains:
- genomics
- systems biology
- biological systems
homepage_url: https://remap.univ-amu.fr/
id: remap
last_modified_date: '2026-05-22T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc/4.0/
  label: CC BY-NC 4.0
name: ReMap
products:
- category: GraphicalInterface
  description: Main ReMap portal for searching transcriptional regulators, tissues,
    and DNA-binding datasets.
  format: http
  id: remap.portal
  name: ReMap Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: remap
  product_url: https://remap.univ-amu.fr/
- category: ProgrammingInterface
  description: ReMap REST interface for programmatic access to search, annotation,
    and regulatory region endpoints.
  format: http
  id: remap.api
  name: ReMap REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: remap
  product_url: https://remap.univ-amu.fr/rest_page
- category: Product
  description: ReMap download page for binding region catalogs, track hubs, and associated
    release files.
  format: http
  id: remap.downloads
  name: ReMap Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: remap
  product_url: https://remap.univ-amu.fr/download_page
- category: GraphProduct
  description: Neo4j knowledge graph integrating transcription factor target libraries,
    coexpression networks, and benchmark datasets used by the ChEA3 resource
  dump_format: neo4j
  format: neo4j
  id: chea-kg.graph
  name: ChEA-KG Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea-kg
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: tcga
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: chea
- category: Product
  description: Download catalog for ChEA3 transcription factor target libraries, benchmark
    datasets, and additional supporting libraries
  format: http
  id: chea-kg.libraries
  name: ChEA-KG Library Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea-kg
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: tcga
  product_url: https://maayanlab.cloud/chea3/index.html#content4-13
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: chea
- category: Product
  description: Download catalog for ChEA3 transcription factor target libraries and
    benchmark datasets
  format: http
  id: chea.libraries
  name: ChEA Library Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: tcga
  product_url: https://maayanlab.cloud/chea3/index.html#content4-13
- category: GraphProduct
  description: "Core TF\u2013target regulon knowledge graph (multi-species) with confidence\
    \ levels (A\u2013E)"
  id: dorothea.graph
  name: DoRothEA Regulon Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hocomoco
  - relation_type: prov:hadPrimarySource
    source: oreganno
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: tfacts
  - relation_type: prov:hadPrimarySource
    source: tred
  product_url: https://github.com/saezlab/dorothea/releases/tag/v1.0.0
publications:
- authors:
  - Hammal F
  - de Langen P
  - Bergon A
  - Lopez F
  - Ballester B
  doi: 10.1093/nar/gkab996
  id: https://doi.org/10.1093/nar/gkab996
  journal: Nucleic Acids Research
  preferred: true
  title: 'ReMap 2022: a database of Human, Mouse, Drosophila and Arabidopsis regulatory
    regions from an integrative analysis of DNA-binding sequencing experiments'
  year: '2022'
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
- NCBITaxon:7227
- NCBITaxon:3702
---
# ReMap

ReMap curates and reprocesses public ChIP-seq, ChIP-exo, and DAP-seq experiments to
produce species-specific catalogs of transcriptional regulator binding regions. The
current public site supports search, download, track hubs, and API-style access for
human, mouse, Drosophila, and Arabidopsis regulatory atlases.

This resource is also an upstream source for ChEA-family transcription factor target
libraries in KG-Registry, so those downstream products remain attached here with explicit
provenance back to ReMap and the derivative resources that consume it.