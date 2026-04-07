---
activity_status: active
category: DataSource
collection:
- ber
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://signor.uniroma2.it/contact.php
  label: SIGNOR Team (University of Rome Tor Vergata & Sapienza University of Rome)
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
infores_id: signor
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
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for SIGNOR distributed via the NCATS Translator
    release site (release 2026_03_06; build signor_2026_January_e2465db9_2025sep1_4.3.6;
    source version 2026_January; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 18341
  format: kgx-jsonl
  id: translator.signor.graph
  latest_version: '2026_03_06'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator SIGNOR KGX Graph
  node_count: 6633
  original_source:
  - signor
  product_url: https://kgx-storage.rtx.ai/releases/signor/latest/
  secondary_source:
  - translator
  versions:
  - '2026_03_06'
  - signor_2026_January_e2465db9_2025sep1_4.3.6
- category: Product
  description: signor Nodes TSV
  format: tsv
  id: obo-db-ingest.signor.tsv
  license:
    id: https://creativecommons.org/licenses/by-nc/4.0/
    label: CC-BY-NC-4.0
  name: signor Nodes TSV
  original_source:
  - signor
  product_file_size: 29422
  product_url: https://w3id.org/biopragmatics/resources/signor/signor.tsv
  secondary_source:
  - obo-db-ingest
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: Aggregated KGX JSONL graph package combining 29 Translator release
    sources (release 2026_03_27; build 423af7989cac; Biolink 4.3.6; Node Normalizer
    2025sep1).
  edge_count: 29243943
  format: kgx-jsonl
  id: translator.translator_kg.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator Aggregate KGX Graph
  node_count: 1696790
  original_source:
  - alliance
  - bgee
  - bindingdb
  - chembl
  - cohd
  - ctd
  - ctkp
  - drug-approvals-kp
  - dgidb
  - diseases
  - drugrephub
  - drugcentral
  - gtopdb
  - gene2phenotype
  - geneticskp
  - go-cam
  - goa
  - hp
  - icees-kg
  - intact
  - ncbigene
  - panther
  - pathbank
  - semmeddb
  - sider
  - signor
  - text-mining-kp
  - ttd
  - ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
  secondary_source:
  - translator
  versions:
  - '2026_03_27'
  - 423af7989cac
- category: GraphProduct
  description: Graph database dump and additional relationship files for the Clinical
    Knowledge Graph.
  format: neo4j
  id: ckg.graph
  name: CKG Graph Database Dump
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
taxon:
- NCBITaxon:9606
---
# SIGNOR

SIGNOR (SIGnaling Network Open Resource) is a curated knowledgebase capturing causally directed, signed interactions underlying human cellular signaling. Interactions link proteins and other entities (chemicals, stimuli, phenotypes, complexes, families) with effect, mechanism, residue context when available, evidence (PMIDs), and a relevance score. Data can be accessed via the web UI, downloadable latest stable release, and granular REST endpoints (`getData.php`, `getPathwayData.php`, and others for complexes and human-only subsets). Use CC-BY 4.0 licensed data with appropriate citation (Lo Surdo et al., 2022). When integrating, preserve directionality and sign to enable pathway and network inference.