---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://labs.icahn.mssm.edu/maayanlab/
  label: Ma'ayan Laboratory
creation_date: '2026-05-21T00:00:00Z'
description: Enrichr is a Ma'ayan Lab web-based gene set enrichment analysis resource
  that accepts gene lists and related inputs, tests them against hundreds of curated
  and crowd-sourced gene set libraries, and provides ranked enrichment results, visualizations,
  and programmatic access.
domains:
- biomedical
- genomics
- systems biology
homepage_url: https://maayanlab.cloud/Enrichr/
id: enrichr
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Enrichr
products:
- category: GraphicalInterface
  description: Main Enrichr web interface for submitting gene sets, exploring enrichment
    results, browsing libraries, and viewing interactive visualizations
  format: http
  id: enrichr.portal
  name: Enrichr Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr
  product_url: https://maayanlab.cloud/Enrichr/
- category: ProgrammingInterface
  connection_url: https://maayanlab.cloud/Enrichr/addList
  description: REST API for submitting gene lists, retrieving enrichment results,
    exporting analyses, and querying Enrichr programmatically
  format: json
  id: enrichr.api
  is_public: true
  name: Enrichr API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr
  product_url: https://maayanlab.cloud/Enrichr/help#api
- category: Product
  description: JSON endpoint listing Enrichr gene set libraries with category assignments,
    term counts, gene coverage, and source links
  format: json
  id: enrichr.library-statistics
  name: Enrichr Library Statistics
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr
  product_url: https://maayanlab.cloud/Enrichr/datasetStatistics
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-12: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2026-06-13: No Content-Length
    header found'
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
- category: GraphicalInterface
  description: Interactive web interface for gene set enrichment analysis, Enrichr
    term expansion, and graph exploration across integrated Enrichr-KG libraries
  format: http
  id: enrichr-kg.portal
  name: Enrichr-KG Explorer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr-kg
  product_url: https://maayanlab.cloud/enrichr-kg/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: enrichr
- category: ProgrammingInterface
  description: API surface for programmatic access to Enrichr-KG enrichment analysis
    and graph-backed query results
  format: json
  id: enrichr-kg.api
  is_public: true
  name: Enrichr-KG API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr-kg
  product_url: https://maayanlab.cloud/enrichr-kg/api/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: enrichr
- category: GraphProduct
  description: Neo4j graph database integrating Enrichr gene set libraries with genes,
    terms, pathways, diseases, drugs, cell types, and other functional annotations
  dump_format: neo4j
  format: neo4j
  id: enrichr-kg.graph
  name: Enrichr-KG Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr-kg
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: kg-jensenlab-diseases
- category: Product
  description: Node-table CSV snapshot from the Enrichr-KG downloads page containing
    node metadata for a current release
  format: csv
  id: enrichr-kg.nodes-csv
  name: Enrichr-KG Node CSV Snapshot
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr-kg
  - relation_type: prov:hadPrimarySource
    source: enrichr
  product_file_size: 1588029
  product_url: https://s3.amazonaws.com/maayan-kg/enrichr-kg/current/Gene.nodes.csv
- category: Product
  description: Edge-table CSV snapshot from the Enrichr-KG downloads page using source.relation.target
    edge triples
  format: csv
  id: enrichr-kg.edges-csv
  name: Enrichr-KG Edge CSV Snapshot
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr-kg
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 35177347
  product_url: https://s3.amazonaws.com/maayan-kg/enrichr-kg/current/GO_Biological_Process_2021.GO_BP.Gene.edges.csv
publications:
- authors:
  - Chen EY
  - Tan CM
  - Kou Y
  - Duan Q
  - Wang Z
  - Meirelles GV
  - Clark NR
  - Ma'ayan A
  doi: 10.1186/1471-2105-14-128
  id: doi:10.1186/1471-2105-14-128
  journal: BMC Bioinformatics
  preferred: true
  title: 'Enrichr: interactive and collaborative HTML5 gene list enrichment analysis
    tool'
  year: '2013'
- authors:
  - Kuleshov MV
  - Jones MR
  - Rouillard AD
  - Fernandez NF
  - Duan Q
  - Wang Z
  - Koplev S
  - Jenkins SL
  - Jagodnik KM
  - Lachmann A
  - McDermott MG
  - Monteiro CD
  - Ma'ayan A
  doi: 10.1093/nar/gkw377
  id: doi:10.1093/nar/gkw377
  journal: Nucleic Acids Research
  preferred: false
  title: 'Enrichr: a comprehensive gene set enrichment analysis web server 2016 update'
  year: '2016'
repository: https://github.com/MaayanLab/enrichr_issues
taxon:
- NCBITaxon:9606
---
# Enrichr

Enrichr is a widely used web-based enrichment analysis platform for interpreting gene lists against a large collection of curated and derived gene set libraries. The current public deployment provides interactive submission and result views, library browsing, multiple scoring schemes, and a documented REST API for automated workflows.

Current Enrichr documentation describes support for crisp and fuzzy gene sets, optional background-aware enrichment through the linked Speedrichr service, downloadable enrichment result exports, and a large catalog of libraries spanning transcription, pathways, ontologies, diseases, drugs, cell types, and crowd-contributed signatures. The public site also exposes library statistics as structured JSON.

## Access

- Main portal: [Enrichr](https://maayanlab.cloud/Enrichr/)
- API documentation: [Enrichr API](https://maayanlab.cloud/Enrichr/help#api)
- Library statistics: [datasetStatistics](https://maayanlab.cloud/Enrichr/datasetStatistics)

## Automated Evaluation

- View the automated evaluation: [enrichr automated evaluation](enrichr_eval_automated.html)