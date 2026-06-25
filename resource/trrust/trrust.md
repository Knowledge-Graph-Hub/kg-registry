---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.grnpedia.org/trrust/
  label: Network Biology Laboratory, Yonsei University
creation_date: '2026-06-18T00:00:00Z'
description: TRRUST (Transcriptional Regulatory Relationships Unraveled by Sentence-based
  Text mining) is a manually curated database of human and mouse transcriptional regulatory
  networks. Its interactions are extracted from sentences in PubMed abstracts using
  sentence-based text mining followed by manual expert curation, capturing transcription
  factor (TF) to target-gene relationships along with the mode of regulation (activation,
  repression, or unknown). The v2 release contains 8,444 human and 6,552 mouse TF-target
  regulatory interactions derived from over 11,000 PubMed articles, each linked to
  the supporting literature evidence. TRRUST serves as an upstream primary source
  for derived regulatory-network resources such as DoRothEA.
domains:
- genomics
- systems biology
- biological systems
homepage_url: https://www.grnpedia.org/trrust/
id: trrust
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: Creative Commons Attribution-ShareAlike 4.0 International
name: TRRUST
products:
- category: Product
  description: TRRUST web resource for browsing and searching manually curated human
    and mouse transcription factor-target regulatory interactions.
  format: http
  id: trrust.web
  name: TRRUST Web Resource
  original_source:
  - relation_type: prov:hadPrimarySource
    source: trrust
  product_url: https://www.grnpedia.org/trrust/
- category: Product
  description: TRRUST v2 human transcription factor-target regulatory interactions
    in tab-separated format, with TF, target gene, mode of regulation, and supporting
    PubMed identifiers.
  format: tsv
  id: trrust.human.tsv
  name: TRRUST Human Interactions (TSV)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: trrust
  product_file_size: 297659
  product_url: https://www.grnpedia.org/trrust/data/trrust_rawdata.human.tsv
- category: Product
  description: TRRUST v2 mouse transcription factor-target regulatory interactions
    in tab-separated format, with TF, target gene, mode of regulation, and supporting
    PubMed identifiers.
  format: tsv
  id: trrust.mouse.tsv
  name: TRRUST Mouse Interactions (TSV)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: trrust
  product_file_size: 220353
  product_url: https://www.grnpedia.org/trrust/data/trrust_rawdata.mouse.tsv
- category: GraphProduct
  description: Core TF–target regulon knowledge graph (multi-species) with confidence
    levels (A–E)
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
  - Han H
  - Cho JW
  - Lee S
  - Yun A
  - Kim H
  - Bae D
  - Yang S
  - Kim CY
  - Lee M
  - Kim E
  - Lee S
  - Kang B
  - Jeong D
  - Kim Y
  - Jeon HN
  - Jung H
  - Nam S
  - Chung M
  - Kim JH
  - Lee I
  doi: 10.1093/nar/gkx1013
  id: https://www.ncbi.nlm.nih.gov/pubmed/29087512
  journal: Nucleic Acids Res
  preferred: true
  title: 'TRRUST v2: an expanded reference database of human and mouse transcriptional
    regulatory interactions'
  year: '2018'
---
# TRRUST

TRRUST is a manually curated data source of human and mouse transcriptional regulatory
interactions, providing transcription factor-target relationships with their mode of
regulation and supporting literature evidence. It is an upstream primary source of
derived regulatory-network resources such as DoRothEA.