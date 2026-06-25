---
activity_status: inactive
category: DataSource
creation_date: '2026-06-18T00:00:00Z'
description: TFactS is a catalogue of literature-curated, signed transcription factor
  to target gene regulatory interactions, where each interaction records whether a
  transcription factor up-regulates or down-regulates its target. By comparing these
  curated "regulons" against differentially expressed genes, TFactS infers the activation
  or repression state of transcription factors from gene expression (microarray) data.
  It served as a foundational upstream source for the DoRothEA regulon collection.
  The original web service at tfacts.org is no longer operational and the domain has
  been re-registered for unrelated content.
domains:
- genomics
- systems biology
- pathways
homepage_url: http://www.tfacts.org/
id: tfacts
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: TFactS
products:
- category: DocumentationProduct
  description: Peer-reviewed publication describing the TFactS method and the curated
    catalogue of signed transcription factor to target gene interactions. The original
    tfacts.org web server is defunct, so the paper serves as the authoritative reference
    for the resource.
  id: tfacts.publication
  name: TFactS publication (Nucleic Acids Research, 2010)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tfacts
  product_url: https://doi.org/10.1093/nar/gkq149
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
  - Essaghir A
  - Toffalini F
  - Knoops L
  - Kallin A
  - van Helden J
  - Demoulin JB
  doi: 10.1093/nar/gkq149
  id: https://pubmed.ncbi.nlm.nih.gov/20215436/
  journal: Nucleic Acids Res
  preferred: true
  title: Transcription factor regulation can be accurately predicted from the presence
    of target gene signatures in microarray gene expression data
  year: '2010'
---
## Description

**TFactS** is a catalogue of literature-curated transcription factor to target
gene interactions, each annotated with a sign of regulation (up- or
down-regulation). Given a list of differentially expressed genes, TFactS scores
the over-representation of each transcription factor's curated target set to
infer which factors are activated or repressed in a given gene expression
(microarray) experiment.

The resource is an upstream source of **DoRothEA**, the widely used regulon
collection. The original web service at tfacts.org is no longer operational; the
domain currently resolves to unrelated content, so the resource is marked
**inactive** and the 2010 publication serves as its authoritative reference.

## Products

- **TFactS publication (Nucleic Acids Research, 2010)** — the peer-reviewed
  paper describing the method and the curated catalogue of signed transcription
  factor to target gene interactions.