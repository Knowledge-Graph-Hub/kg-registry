---
activity_status: active
category: KnowledgeGraph
creation_date: '2026-04-06T00:00:00Z'
description: Clinical Knowledge Graph (CKG) is an open-source biomedical knowledge graph platform that integrates proteomics data, clinical data, biomedical databases, and literature to support clinically meaningful querying, analysis, and hypothesis generation. CKG has been integrated into the BioCypher framework while its original repository, documentation, and graph database dump remain available.
domains:
  - clinical
  - biomedical
  - precision medicine
  - proteomics
  - health
homepage_url: https://ckg.readthedocs.io/
id: ckg
last_modified_date: '2026-06-01T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
name: Clinical Knowledge Graph
products:
  - category: GraphProduct
    description: Graph database dump and additional relationship files for the Clinical Knowledge Graph.
    format: neo4j
    id: ckg.graph
    latest_version: '1'
    license:
      id: https://creativecommons.org/licenses/by/4.0/
      label: CC BY 4.0
    name: CKG Graph Database Dump
    original_source:
      - source: bto
        relation_type: prov:hadPrimarySource
      - source: cancer-genome-interpreter
        relation_type: prov:hadPrimarySource
      - source: ckg
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: dgidb
        relation_type: prov:hadPrimarySource
      - source: diseases
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: foodb
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: hmdb
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: mod
        relation_type: prov:hadPrimarySource
      - source: ms
        relation_type: prov:hadPrimarySource
      - source: mutationds
        relation_type: prov:hadPrimarySource
      - source: oncokb
        relation_type: prov:hadPrimarySource
      - source: pfam
        relation_type: prov:hadPrimarySource
      - source: phosphositeplus
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: signor
        relation_type: prov:hadPrimarySource
      - source: smpdb
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
    product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
  - category: DocumentationProduct
    description: Project documentation for installing, building, and querying the Clinical Knowledge Graph.
    format: http
    id: ckg.docs
    name: CKG Documentation
    original_source:
      - source: ckg
        relation_type: prov:hadPrimarySource
    product_url: https://ckg.readthedocs.io/
publications:
  - authors:
      - Alberto Santos
      - Ana R. Colaço
      - Annelaura B. Nielsen
      - Lili Niu
      - Maximilian Strauss
      - Philipp E. Geyer
      - Fabian Coscia
      - Nicolai J. Wewer Albrechtsen
      - Filip Mundt
      - Lars Juhl Jensen
      - Matthias Mann
    doi: 10.1038/s41587-021-01145-6
    id: doi:10.1038/s41587-021-01145-6
    journal: Nature Biotechnology
    preferred: true
    title: A knowledge graph to interpret clinical proteomics data
    year: '2022'
repository: https://github.com/MannLabs/CKG
taxon:
  - NCBITaxon:9606
---

# Clinical Knowledge Graph

Clinical Knowledge Graph (CKG) is a biomedical knowledge graph framework built around proteomics and clinical interpretation workflows. It combines experimental data, biomedical databases, and literature in a graph structure that supports interactive exploration, graph querying, and downstream statistical analysis.

CKG has been integrated into the BioCypher framework. The original CKG repository,
documentation, and Mendeley graph database dump remain available as reference
resources for the published platform.
