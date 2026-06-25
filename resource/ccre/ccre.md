---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.encodeproject.org/help/contacts/
  label: ENCODE Data Coordination Center (DCC)
creation_date: '2026-06-18T00:00:00Z'
description: The ENCODE Registry of candidate cis-Regulatory Elements (cCREs) is a
  curated annotation of regulatory regions in the human and mouse genomes derived
  from ENCODE and Roadmap Epigenomics data. Each cCRE is classified by its biochemical
  signature, including promoter-like, enhancer-like, and CTCF-bound elements based
  on DNase hypersensitivity, H3K4me3, H3K27ac, and CTCF ChIP-seq signals. The registry
  is explorable through the SCREEN (Search Candidate cis-Regulatory Elements by ENCODE)
  web portal, which lets users browse cCREs and their activity across cell types and
  tissues. cCREs/SCREEN are produced as part of the ENCODE project and serve as an
  upstream source for downstream resources such as GenomicKB.
domains:
- genomics
- biological systems
- systems biology
homepage_url: https://screen.encodeproject.org/
id: ccre
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: ENCODE cCRE Registry (SCREEN)
products:
- category: GraphicalInterface
  description: SCREEN (Search Candidate cis-Regulatory Elements by ENCODE) web portal
    for browsing and searching the registry of candidate cis-Regulatory Elements in
    the human and mouse genomes.
  id: ccre.screen
  name: SCREEN Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ccre
  product_url: https://screen.encodeproject.org/
- category: GraphProduct
  description: GenomicKB 1.0 Neo4j Database Dump (Requires license)
  dump_format: neo4j
  id: genomickb.graph
  name: GenomicKB Graph Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genomickb
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: dbvar
  - relation_type: prov:hadPrimarySource
    source: endb
  - relation_type: prov:hadPrimarySource
    source: enhanceratlas
  - relation_type: prov:hadPrimarySource
    source: ccre
  - relation_type: prov:hadPrimarySource
    source: fire
  - relation_type: prov:hadPrimarySource
    source: motifmap
  product_url: https://available-inventions.umich.edu/product/genomickb-a-knowledgebase-for-the-human-genome
publications:
- authors:
  - Moore JE
  - Purcaro MJ
  - Pratt HE
  - Epstein CB
  - Shoresh N
  - Adrian J
  - Kawli T
  - Davis CA
  - Dobin A
  doi: 10.1038/s41586-020-2493-4
  id: https://pubmed.ncbi.nlm.nih.gov/32728249/
  journal: Nature
  preferred: true
  title: Expanded encyclopaedias of DNA elements in the human and mouse genomes
  year: '2020'
---
## Description

The ENCODE Registry of candidate cis-Regulatory Elements (cCREs) is a curated set of
regulatory regions annotated across the human and mouse genomes. cCREs are derived
from ENCODE and Roadmap Epigenomics assays and are classified by biochemical signature
(promoter-like, enhancer-like, and CTCF-bound). The registry is part of the ENCODE
project and is explored through the SCREEN web portal. It is an upstream source for
GenomicKB.

## Contacts

- ENCODE Data Coordination Center (DCC) — [contact page](https://www.encodeproject.org/help/contacts/)

## Products

### ccre.screen

SCREEN (Search Candidate cis-Regulatory Elements by ENCODE) web portal for browsing
and searching the registry of candidate cis-Regulatory Elements in the human and
mouse genomes.

**URL**: [https://screen.encodeproject.org/](https://screen.encodeproject.org/)

## Publications

- Moore JE et al. (2020) Expanded encyclopaedias of DNA elements in the human and mouse
  genomes. *Nature*. [doi:10.1038/s41586-020-2493-4](https://doi.org/10.1038/s41586-020-2493-4)