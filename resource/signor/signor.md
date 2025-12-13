---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://signor.uniroma2.it/contact.php
  label: SIGNOR Team (University of Rome Tor Vergata & Sapienza University of Rome)
collection:
- ber
creation_date: '2025-08-12T00:00:00Z'
description: "SIGNOR (SIGnaling Network Open Resource) is a manually curated repository\
  \ of experimentally supported, causal relationships between human proteins and other\
  \ biologically relevant entities (chemicals, phenotypes, complexes, families, stimuli).\
  \ Each interaction is annotated with effect, mechanism, directionality, evidence\
  \ (PMID), and a relevance score, enabling construction and analysis of signed, directed\
  \ signaling networks and pathways. Cite SIGNOR (Lo Surdo et al., 2022 NAR) when\
  \ using data; interaction data are directional and signed\u2014verify effect/mechanism\
  \ fields when integrating."
domains:
- pathways
- biomedical
- systems biology
- proteomics
homepage_url: https://signor.uniroma2.it/
id: signor
last_modified_date: '2025-08-23T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY 4.0
name: SIGNOR
products:
- category: GraphicalInterface
  description: Web interface for browsing entities, pathways, and visualizing causal
    signaling graphs
  format: http
  id: signor.web
  name: SIGNOR Website
  original_source:
  - signor
  product_url: https://signor.uniroma2.it/
- category: ProgrammingInterface
  description: REST-style endpoints for retrieving interaction, pathway, complex,
    and organism-specific datasets (tab-separated)
  format: http
  id: signor.api
  is_public: true
  name: SIGNOR REST API
  original_source:
  - signor
  product_url: https://signor.uniroma2.it/APIs.php
- category: GraphProduct
  compression: zip
  description: Latest stable SIGNOR complete dataset (signed, directed causal interactions
    with effects, mechanisms, PMIDs, scores)
  format: tsv
  id: signor.complete
  name: SIGNOR Latest Stable Release
  original_source:
  - signor
  product_url: https://signor.uniroma2.it/releases/getLatestRelease.php
- category: ProgrammingInterface
  description: Programmatic interaction data query returning tab-separated causal
    interaction records for specified entity IDs with configurable depth and type
  format: tsv
  id: signor.interactions.dynamic
  name: SIGNOR Interaction Query Endpoint
  original_source:
  - signor
  product_url: https://signor.uniroma2.it/getData.php
- category: ProgrammingInterface
  description: Pathway data (entities and relations) retrievable via parameterized
    REST calls supporting per-pathway or global views
  format: tsv
  id: signor.pathways
  name: SIGNOR Pathway Data
  original_source:
  - signor
  product_url: https://signor.uniroma2.it/getPathwayData.php
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - doid
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: cancer-genome-interpreter.clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - doid
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
publications:
- id: https://doi.org/10.1093/nar/gkac883
  journal: Nucleic Acids Research
  preferred: true
  title: 'SIGNOR 3.0, the SIGnaling network open resource 3.0: 2022 update'
  year: '2022'
infores_id: signor
taxon:
- NCBITaxon:9606
---

# SIGNOR

SIGNOR (SIGnaling Network Open Resource) is a curated knowledgebase capturing causally directed, signed interactions underlying human cellular signaling. Interactions link proteins and other entities (chemicals, stimuli, phenotypes, complexes, families) with effect, mechanism, residue context when available, evidence (PMIDs), and a relevance score. Data can be accessed via the web UI, downloadable latest stable release, and granular REST endpoints (`getData.php`, `getPathwayData.php`, and others for complexes and human-only subsets). Use CC-BY 4.0 licensed data with appropriate citation (Lo Surdo et al., 2022). When integrating, preserve directionality and sign to enable pathway and network inference.
