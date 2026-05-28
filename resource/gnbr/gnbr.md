---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: github
    value: jakelever
  - contact_type: url
    value: https://github.com/jakelever/GNBR
  label: GNBR
creation_date: '2025-08-12T00:00:00Z'
description: The Global Network of Biomedical Relationships (GNBR) is a large-scale
  biomedical knowledge graph derived from literature. GNBR uses text mining of PubMed
  abstracts to extract typed relationships between genes, diseases and drugs/chemicals,
  organizing them into semantic themes suitable for link prediction and downstream
  applications such as drug repurposing. GNBR has been widely used as a text-derived
  KG resource and is available via GitHub and Zenodo.
domains:
- biomedical
- literature
- health
homepage_url: https://github.com/jakelever/GNBR
id: gnbr
infores_id: gnbr
last_modified_date: '2026-05-27T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: GNBR
products:
- category: GraphProduct
  description: "Text-mined biomedical knowledge graph of gene\u2013disease\u2013drug\
    \ relationships (semantic themes)"
  id: gnbr.graph
  name: GNBR graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gnbr
  - relation_type: prov:hadPrimarySource
    source: pubtator
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://zenodo.org/records/3459420
- category: GraphProduct
  description: Cleaned benchmark graph (PharmKG-8k) with typed relations between genes,
    chemicals, and diseases
  edge_count: 500958
  id: pharmkg.graph
  name: PharmKG graph
  node_count: 7603
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: gnbr
  - relation_type: prov:hadPrimarySource
    source: humannet
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pharmkg
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: ttd
  product_url: https://zenodo.org/record/4077338
publications:
- authors:
  - Percha B
  - Altman RB
  doi: 10.1093/bioinformatics/bty114
  id: doi:10.1093/bioinformatics/bty114
  journal: Bioinformatics
  title: A global network of biomedical relationships derived from text
  year: '2018'
repository: https://github.com/jakelever/GNBR
taxon:
- NCBITaxon:9606
---
GNBR

## Evaluation

- View the evaluation: [gnbr evaluation](gnbr_eval.html)