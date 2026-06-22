---
category: GraphProduct
description: RDF knowledge graph materialized by the MetaBoKG workflow from public
  metabolomics repository outputs, GNPS molecular-networking jobs, annotation evidence,
  sample metadata, and environmental and taxonomic context. The repository documents
  generated per-job Turtle files under mapping/kg and loading into Virtuoso named
  graphs.
format: mixed
id: metabokg.graph
latest_version: arXiv v1 demonstration
name: MetaboKG RDF Graph
original_source:
- relation_type: prov:hadPrimarySource
  source: metabokg
- relation_type: prov:hadPrimarySource
  source: pubmed
- relation_type: prov:hadPrimarySource
  source: pubmedcentral
- relation_type: prov:hadPrimarySource
  source: gnps
- relation_type: prov:hadPrimarySource
  source: massive
- relation_type: prov:hadPrimarySource
  source: redu
product_url: https://github.com/HolobiomicsLab/MetaBoKG
secondary_source:
- relation_type: prov:used
  source: ms
- relation_type: prov:used
  source: chebi
- relation_type: prov:used
  source: ncbitaxon
- relation_type: prov:used
  source: envo
- relation_type: prov:used
  source: ncit
- relation_type: prov:used
  source: uberon
- relation_type: prov:used
  source: chmo
- relation_type: prov:used
  source: sio
- relation_type: prov:used
  source: prov-o
- relation_type: prov:used
  source: dcat
- relation_type: prov:used
  source: afo
warnings:
- No static public graph release or hosted endpoint was available in the GitHub repository
  when curated on 2026-06-02; the repository documents local Turtle materialization
  and Virtuoso loading.
layout: product_detail
---
