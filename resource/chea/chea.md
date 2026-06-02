---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: avi.maayan@mssm.edu
  - contact_type: url
    value: https://labs.icahn.mssm.edu/maayanlab/
  label: Ma'ayan Laboratory
creation_date: '2026-05-21T00:00:00Z'
description: ChEA is a family of transcription factor enrichment resources developed
  by the Ma'ayan Lab, spanning the original ChIP Enrichment Analysis database and
  later ChEA2 and ChEA3 releases that assemble transcription factor target gene sets
  from ChIP-X experiments and other orthogonal omics data.
domains:
- biomedical
- genomics
- systems biology
homepage_url: https://maayanlab.cloud/chea3/
id: chea
last_modified_date: '2026-06-01T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc-sa/4.0/
  label: CC BY-NC-SA 4.0
name: ChEA
products:
- category: GraphicalInterface
  description: Public ChEA3 web interface for transcription factor enrichment analysis
    and result visualization
  format: http
  id: chea.portal
  name: ChEA Explorer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea
  product_url: https://maayanlab.cloud/chea3/
- category: ProgrammingInterface
  connection_url: https://maayanlab.cloud/chea3/api/enrich/
  description: ChEA3 enrichment API for submitting gene sets and retrieving transcription
    factor ranking results
  format: http
  id: chea.api
  name: ChEA API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea
  product_url: https://maayanlab.cloud/chea3/api/enrich/
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
- category: Product
  description: Docker image for running the ChEA3 web application locally
  format: mixed
  id: chea.docker
  name: ChEA3 Docker Image
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea
  product_url: https://hub.docker.com/r/maayanlab/chea3
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-02: No Content-Length
    header found'
- category: GraphicalInterface
  description: Interactive ChEA3 web interface for transcription factor enrichment
    analysis, result tables, and network visualizations
  format: http
  id: chea-kg.portal
  name: ChEA-KG Explorer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea-kg
  product_url: https://maayanlab.cloud/chea-kg/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: chea
- category: ProgrammingInterface
  description: ChEA3 API endpoint for submitting gene sets and retrieving transcription
    factor enrichment results as JSON
  format: http
  id: chea-kg.api
  name: ChEA-KG API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea-kg
  product_url: https://maayanlab.cloud/chea3/api/enrich/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: chea
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
publications:
- authors:
  - Lachmann A
  - Xu H
  - Krishnan J
  - Berger SI
  - Mazloom AR
  - Ma'ayan A
  doi: 10.1093/bioinformatics/btq466
  id: doi:10.1093/bioinformatics/btq466
  journal: Bioinformatics
  title: 'ChEA: transcription factor regulation inferred from integrating genome-wide
    ChIP-X experiments'
  year: '2010'
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
repository: https://github.com/MaayanLab/chea3web
---
# ChEA

ChEA is the Ma'ayan Lab's transcription factor enrichment analysis resource family. The original ChEA database integrated genome-wide ChIP-X experiments to create transcription factor target gene sets, and later releases such as ChEA2 and ChEA3 expanded the available libraries, benchmarking datasets, and interactive analysis workflows.

The current public deployment is the ChEA3 web application and API. Its documented upstream libraries include ENCODE and ReMap ChIP-seq collections, literature-derived ChIP-seq target sets from earlier ChEA releases, GTEx and ARCHS4 coexpression libraries, Enrichr query co-occurrence libraries, GEO-derived single-transcription-factor perturbation benchmarks, and some TCGA-derived network views.

This KG-Registry entry treats ChEA, ChEA2, and ChEA3 as one canonical resource represented by the identifier `chea`.