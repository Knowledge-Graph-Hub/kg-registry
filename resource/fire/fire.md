---
activity_status: inactive
category: DataSource
creation_date: '2026-06-18T00:00:00Z'
description: FIRE (Frequently Interacting REgions) are genomic regions that participate
  in an unusually high number of local chromatin interactions, identified from high-throughput
  chromosome conformation capture (Hi-C) data. They were defined by Schmitt et al.
  (Cell Reports, 2016), who built a compendium of chromatin contact maps across 14
  human primary tissues and cell types and showed that FIREs mark spatially active,
  cell-type-specific regions of the genome enriched for super-enhancers and disease-associated
  variants. FIRE serves as an upstream chromatin-architecture data layer in GenomicKB,
  contributing three-dimensional genome-organization annotations to that knowledge
  graph.
domains:
- genomics
- systems biology
- biomedical
homepage_url: https://doi.org/10.1016/j.celrep.2016.10.061
id: fire
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: FIRE (Frequently Interacting REgions)
products:
- category: DataSource
  description: Schmitt et al. (2016) compendium of chromatin contact maps and Frequently
    Interacting REgions, distributed via the PubMed Central article record and its
    supplementary data.
  id: fire.publication
  name: FIRE compendium of chromatin contact maps
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fire
  product_url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5135022/
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
  - Schmitt AD
  - Hu M
  - Jung I
  - Xu Z
  - Qiu Y
  - Tan CL
  - Li Y
  - Lin S
  - Lin Y
  - Barr CL
  - Ren B
  doi: 10.1016/j.celrep.2016.10.061
  id: https://www.ncbi.nlm.nih.gov/pubmed/27851967
  journal: Cell Rep
  preferred: true
  title: A Compendium of Chromatin Contact Maps Reveals Spatially Active Regions in
    the Human Genome
  year: '2016'
---
FIRE (Frequently Interacting REgions) identifies genomic regions that frequently
take part in local chromatin interactions, called from Hi-C data. Introduced by
Schmitt et al. (Cell Reports, 2016), FIREs highlight spatially active, often
cell-type-specific portions of the human genome and are used as an upstream
chromatin-architecture data layer in GenomicKB.

The original FIRE-calling code was published as the `fishHiC` repository
(github.com/yunliUNC/fishHiC), but that repository no longer resolves, so this
record points to the peer-reviewed publication and its archived data as the
canonical source. Because FIRE represents a static, published analysis with no
maintained software or data portal, its activity status is recorded as inactive.