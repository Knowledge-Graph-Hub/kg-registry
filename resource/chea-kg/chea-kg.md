---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: avi.maayan@mssm.edu
      - contact_type: url
        value: https://labs.icahn.mssm.edu/maayanlab/
    label: Ma'ayan Laboratory
creation_date: '2025-09-23T00:00:00Z'
description: ChEA-KG is a Ma'ayan Lab transcription factor knowledge graph and web resource associated with the ChEA3 platform, integrating transcription factor target gene libraries, coexpression networks, benchmarking datasets, and interactive query results for transcription factor enrichment analysis.
domains:
  - biomedical
  - genomics
  - systems biology
homepage_url: https://maayanlab.cloud/chea-kg/
id: chea-kg
last_modified_date: '2026-05-21T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc-sa/4.0/
  label: CC BY-NC-SA 4.0
name: ChEA-KG
products:
  - category: GraphicalInterface
    description: Interactive ChEA3 web interface for transcription factor enrichment analysis, result tables, and network visualizations
    format: http
    id: chea-kg.portal
    name: ChEA-KG Explorer
    product_url: https://maayanlab.cloud/chea-kg/
    original_source:
      - source: chea-kg
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: chea
        relation_type: prov:wasInfluencedBy
  - category: ProgrammingInterface
    description: ChEA3 API endpoint for submitting gene sets and retrieving transcription factor enrichment results as JSON
    format: http
    id: chea-kg.api
    name: ChEA-KG API
    product_url: https://maayanlab.cloud/chea3/api/enrich/
    original_source:
      - source: chea-kg
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: chea
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Neo4j knowledge graph integrating transcription factor target libraries, coexpression networks, and benchmark datasets used by the ChEA3 resource
    dump_format: neo4j
    format: neo4j
    id: chea-kg.graph
    name: ChEA-KG Database
    original_source:
      - source: chea-kg
        relation_type: prov:hadPrimarySource
      - source: encode
        relation_type: prov:hadPrimarySource
      - source: remap
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: archs4
        relation_type: prov:hadPrimarySource
      - source: enrichr
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: tcga
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: chea
        relation_type: prov:wasInfluencedBy
  - category: Product
    description: Download catalog for ChEA3 transcription factor target libraries, benchmark datasets, and additional supporting libraries
    format: http
    id: chea-kg.libraries
    name: ChEA-KG Library Downloads
    product_url: https://maayanlab.cloud/chea3/index.html#content4-13
    original_source:
      - source: chea-kg
        relation_type: prov:hadPrimarySource
      - source: encode
        relation_type: prov:hadPrimarySource
      - source: remap
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: archs4
        relation_type: prov:hadPrimarySource
      - source: enrichr
        relation_type: prov:hadPrimarySource
      - source: geo
        relation_type: prov:hadPrimarySource
      - source: tcga
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: chea
        relation_type: prov:wasInfluencedBy
publications:
- authors:
  - Keenan AB
  - Torre D
  - Lachmann A
  - Leong AK
  - Wojciechowicz ML
  - Utti V
  - Jagodnik KM
  - Kropiwnicki E
  - Wang Z
  - Ma'ayan A
  doi: 10.1093/nar/gkz446
  id: doi:10.1093/nar/gkz446
  journal: Nucleic Acids Research
  preferred: true
  title: 'ChEA3: transcription factor enrichment analysis by orthogonal omics integration'
  year: '2019'
repository: https://github.com/MaayanLab/chea-kg
---

# ChEA-KG

ChEA-KG is a Ma'ayan Lab transcription factor knowledge-graph project whose public web deployment currently presents the ChEA3 transcription factor enrichment interface. The resource combines transcription factor target libraries, coexpression-based networks, and benchmark perturbation datasets to support transcription factor enrichment analysis, ranked results, and interactive network visualization.

The public ChEA3 site explicitly documents the major upstream library families used by the resource. Primary libraries include ENCODE and ReMap ChIP-seq collections, literature-derived ChIP-seq libraries from prior ChEA releases, GTEx and ARCHS4 coexpression libraries, and Enrichr query co-occurrence data. Benchmarking datasets include single-transcription-factor perturbation signatures mined from GEO, while some network visualizations and annotations also draw on TCGA expression-derived modules.

The source repository documents a Neo4j-backed implementation and Docker-based local deployment workflow. The public site exposes a browser interface, a POST-based API endpoint for submitting gene sets to ChEA3, and a download section listing the library files used for enrichment analysis and benchmarking.

## Original Sources

- ChEA and ChEA2 literature-derived transcription factor target collections
- ENCODE ChIP-seq transcription factor target libraries
- ReMap ChIP-seq transcription factor target libraries
- GTEx coexpression-derived transcription factor target libraries
- ARCHS4 coexpression-derived transcription factor target libraries
- Enrichr query co-occurrence libraries
- GEO-derived single-transcription-factor perturbation benchmark sets
- TCGA-based transcription factor coexpression network views

## Automated Evaluation

- View the automated evaluation: [chea-kg automated evaluation](chea-kg_eval_automated.html)
