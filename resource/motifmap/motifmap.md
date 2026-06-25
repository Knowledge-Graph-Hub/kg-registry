---
activity_status: inactive
category: DataSource
creation_date: '2026-06-18T00:00:00Z'
description: MotifMap is a system from UC Irvine that provides integrative genome-wide
  maps of predicted transcription factor binding sites (regulatory motifs) across
  the human genome and other model species. It combines databases of transcription
  factor binding motifs, refined multiple-genome alignments, and a comparative genomic
  statistical scoring approach (Bayesian Branch Length Score) to call candidate regulatory
  motif sites with associated false discovery rates. The released maps cover yeast,
  fly, worm, mouse, and human, with the human map containing over 500,000 sites for
  hundreds of motif matrices. MotifMap is an upstream source of the GenomicKB knowledge
  graph.
domains:
- genomics
- systems biology
- biomedical
homepage_url: https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-12-495
id: motifmap
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: MotifMap
products:
- category: GraphicalInterface
  description: Historical MotifMap web portal at UC Irvine for searching and browsing
    genome-wide predicted transcription factor binding site maps. The portal subdomain
    no longer resolves in DNS and the service is offline.
  id: motifmap.portal
  name: MotifMap Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: motifmap
  product_url: https://motifmap.ics.uci.edu/
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
  - Kenneth Daily
  - Vishal R. Patel
  - Paul Rigor
  - Xiaohui Xie
  - Pierre Baldi
  doi: 10.1186/1471-2105-12-495
  id: https://pubmed.ncbi.nlm.nih.gov/22208852/
  journal: BMC Bioinformatics
  preferred: true
  title: 'MotifMap: integrative genome-wide maps of regulatory motif sites for model
    species'
  year: '2011'
---
# MotifMap

MotifMap, developed at the University of California, Irvine, provides integrative
genome-wide maps of candidate regulatory motif sites, focusing on predicted
transcription factor binding sites across the human genome and other model
species. The system combines curated transcription factor binding motif
databases with refined multiple-genome alignments and a comparative genomic
statistical approach to score and report candidate sites along with false
discovery rate estimates.

The published maps span yeast, fly, worm, mouse, and human, and were designed to
be integrated with other omics data to support genome-wide analysis of gene
regulation. MotifMap serves as an upstream source of the GenomicKB knowledge
graph.

## Status

The original MotifMap web service is no longer reachable: the canonical homepage
subdomain (`motifmap.ics.uci.edu`, formerly also `motifmap.igb.uci.edu`) does
not resolve in DNS, and the sibling MotifMap-RNA service returns a server error.
The resource is recorded here as inactive, with the live BMC Bioinformatics
article used as the stable reference homepage.