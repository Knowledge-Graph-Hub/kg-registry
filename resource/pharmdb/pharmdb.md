---
activity_status: orphaned
category: KnowledgeGraph
creation_date: '2025-09-10T00:00:00Z'
description: PharmDB (PharmDB-K) is a pharmacological knowledge graph integrating
  drugs, targets, diseases, indications, and related biomedical entities to facilitate
  computational repositioning and network pharmacology analyses.
domains:
- drug discovery
- biomedical
homepage_url: http://www.pharmdb-k.org/
id: pharmdb
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
name: PharmDB
products:
- category: GraphicalInterface
  description: Legacy web portal for browsing PharmDB-K integrated pharmacological
    relationships
  format: http
  id: pharmdb.portal
  name: PharmDB Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmdb
  product_url: http://www.pharmdb-k.org/
- category: GraphProduct
  description: Integrated pharmacological knowledge graph (PharmDB-K) of drugs, targets,
    diseases, and associations
  format: http
  id: pharmdb.graph
  name: PharmDB-K Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmdb
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  format: mixed
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: bioteque
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chemicalchecker
  - relation_type: prov:hadPrimarySource
    source: clue
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: creeds
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: huri
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: offsides
  - relation_type: prov:hadPrimarySource
    source: omnipath
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  - relation_type: prov:hadPrimarySource
    source: prism
  - relation_type: prov:hadPrimarySource
    source: progeny
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
taxon:
- NCBITaxon:9606
---
# PharmDB

## Overview

PharmDB (PharmDB-K) is an integrated pharmacological knowledge graph unifying drugs, targets, diseases, and related biomedical associations to support network pharmacology and drug repurposing analyses. While historically useful, the project has not shown recent update activity, so content should be treated as archival.

## Access

- Portal (legacy): browse integrated relationships and entity-centric views
- Graph: represented internally as PharmDB-K; no current standalone bulk export identified

## Status

The resource appears inactive. Links may function intermittently, but data curation and releases have likely ceased. Use with caution and verify critical relationships against more current sources. The Bioteque embeddings product remains attached here as a downstream derivative that cites PharmDB as one of many upstream inputs.

## Automated Evaluation

- View the automated evaluation: [pharmdb automated evaluation](pharmdb_eval_automated.html)