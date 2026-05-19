---
activity_status: active
category: DataModel
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: cjmungall@lbl.gov
  - contact_type: github
    value: cmungall
  label: Christopher J. Mungall
  orcid: 0000-0002-6601-2165
- category: Organization
  contact_details:
  - contact_type: url
    value: http://geneontology.org/
  - contact_type: email
    value: go-helpdesk@geneontology.org
  label: Gene Ontology Consortium
creation_date: '2025-03-09T00:00:00Z'
description: A structured framework for integrating Gene Ontology annotations into
  computable models of biological functions.
domains:
- biological systems
- genomics
- pathways
- proteomics
homepage_url: http://geneontology.org/go-cam/docs
id: go-cam
infores_id: go-cam
last_modified_date: '2026-05-19T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: Gene Ontology Causal Activity Modeling (GO-CAM)
products:
- category: GraphicalInterface
  description: Web-based tool for collaborative editing of Gene Ontology Causal Activity
    Models (GO-CAMs)
  format: http
  id: go-cam.noctua
  name: Noctua
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go-cam
  product_url: https://noctua.geneontology.org/
- category: GraphicalInterface
  description: Web interface for browsing, searching, and exploring GO-CAM models
  format: http
  id: go-cam.browser
  name: GO-CAM Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go-cam
  product_url: http://geneontology.org/go-cam
- category: DataModelProduct
  description: RDF-based format for representing causal activity models in Gene Ontology
  format: rdfxml
  id: go-cam.model
  name: GO-CAM Model Format
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go-cam
  product_url: https://github.com/geneontology/go-cam
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-05-09: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-19: HTTP 404 error
    when accessing file'
- category: DataModelProduct
  description: LinkML YAML schema for representing Gene Ontology Causal Activity Models
    (GO-CAMs)
  format: yaml
  id: go-cam.linkml-schema
  name: GO-CAM LinkML Schema
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go-cam
  product_file_size: 7830
  product_url: https://raw.githubusercontent.com/geneontology/gocam-py/main/src/gocam/schema/gocam.yaml
- category: ProgrammingInterface
  connection_url: http://api.geneontology.org/
  description: Programmatic access to GO-CAM models through the Gene Ontology API
  id: go-cam.api
  is_public: true
  name: GO-CAM API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go-cam
  product_url: http://api.geneontology.org/
- category: ProcessProduct
  description: Server-side component for storing, validating, and reasoning over GO-CAM
    models
  id: go-cam.minerva
  name: Minerva
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go-cam
  product_url: https://github.com/geneontology/minerva
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for GO-CAM distributed via the NCATS Translator
    release site (release 2026_03_06; build go_cam_2026-01-23_b6972b4a_2025sep1_4.3.6;
    source version 2026-01-23; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 4539
  format: kgx-jsonl
  id: translator.go_cam.graph
  latest_version: '2026_03_06'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator GO-CAM KGX Graph
  node_count: 3181
  original_source:
  - relation_type: prov:hadPrimarySource
    source: go-cam
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://kgx-storage.rtx.ai/releases/go_cam/latest/
  versions:
  - '2026_03_06'
  - go_cam_2026-01-23_b6972b4a_2025sep1_4.3.6
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
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cohd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: drug-approvals-kp
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: geneticskp
  - relation_type: prov:hadPrimarySource
    source: go-cam
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: icees-kg
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathbank
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: translator
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ubergraph
  product_url: https://kgx-storage.rtx.ai/releases/translator_kg/latest/
  versions:
  - '2026_03_27'
  - 423af7989cac
publications:
- authors:
  - Paul D Thomas
  - David P Hill
  - Huaiyu Mi
  - David Osumi-Sutherland
  - Kimberly Van Auken
  - Seth Carbon
  - James P Balhoff
  - Laurent-Philippe Albou
  - Benjamin Good
  - Pascale Gaudet
  - Suzanna E Lewis
  - Christopher J Mungall
  doi: 10.1038/s41588-019-0500-1
  id: doi:10.1038/s41588-019-0500-1
  preferred: true
  title: Gene Ontology Causal Activity Modeling (GO-CAM) moves beyond GO annotations
    to structured descriptions of biological functions and systems
  year: '2019'
repository: https://github.com/geneontology/noctua
---
GO-CAM provides a structured framework for integrating Gene Ontology annotations into 
computable models of biological functions. Unlike standard GO annotations, which link 
individual gene products to GO terms, GO-CAM models connect multiple annotations to 
form causal networks that describe biological processes in greater detail. These models 
enable richer pathway and network analyses and support automated reasoning over 
biological knowledge.

## Overview

GO-CAM (Gene Ontology Causal Activity Modeling) extends the traditional Gene Ontology annotation paradigm to create causal networks that represent molecular activities and their relationships within biological systems. Each GO-CAM model represents a biological pathway or process as an interconnected set of molecular activities.

## Features and Components

- **Causal Models**: Connects molecular activities in causal chains, showing how one activity leads to another
- **Molecular Context**: Specifies cellular locations where activities occur
- **Molecular Functions**: Integrates standard GO molecular function terms
- **Biological Processes**: Associates activities with broader biological processes
- **Evidence**: Links each assertion to supporting evidence codes and literature references

## Tools and Access

- **Noctua**: Web-based collaborative editor for creating and modifying GO-CAM models
- **GO-CAM Browser**: Platform for exploring, searching, and visualizing the complete set of GO-CAM models
- **Minerva**: Backend system providing model storage, validation, and reasoning capabilities
- **API Access**: Programmatic access to models through the Gene Ontology API

## Applications

GO-CAM models are used for:
- Pathway modeling and visualization
- Systems biology analyses
- Hypothesis generation about molecular mechanisms
- Comparative analyses across species
- Data integration from multiple experimental sources

Browse the GO-CAM model repository at [GO-CAM Public Site](http://geneontology.org/go-cam).