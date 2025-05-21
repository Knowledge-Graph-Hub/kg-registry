---
layout: resource_detail
activity_status: active
id: go-cam
name: Gene Ontology Causal Activity Modeling (GO-CAM)
description: A structured framework for integrating Gene Ontology annotations into
  computable models of biological functions.
domains:
- biological systems
- genomics
- pathways
- proteomics
category: DataModel
contacts:
- category: Individual
  label: Christopher J. Mungall
  orcid: 0000-0002-6601-2165
  contact_details:
  - contact_type: email
    value: cjmungall@lbl.gov
  - contact_type: github
    value: cmungall
- category: Organization
  label: Gene Ontology Consortium
  contact_details:
  - contact_type: url
    value: http://geneontology.org/
  - contact_type: email
    value: go-helpdesk@geneontology.org
homepage_url: http://geneontology.org/go-cam/docs
repository: https://github.com/geneontology/noctua
publications:
- doi: 10.1038/s41588-019-0500-1
  id: doi:10.1038/s41588-019-0500-1
  preferred: true
  year: '2019'
  authors:
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
  title: Gene Ontology Causal Activity Modeling (GO-CAM) moves beyond GO annotations
    to structured descriptions of biological functions and systems
license:
  label: CC0 1.0
  id: https://creativecommons.org/publicdomain/zero/1.0/
products:
- category: GraphicalInterface
  id: go-cam.noctua
  name: Noctua
  description: Web-based tool for collaborative editing of Gene Ontology Causal Activity Models (GO-CAMs)
  product_url: https://noctua.geneontology.org/
  original_source:
  - go-cam
  format: http
- category: GraphicalInterface
  id: go-cam.browser
  name: GO-CAM Browser
  description: Web interface for browsing, searching, and exploring GO-CAM models
  product_url: http://geneontology.org/go-cam
  original_source:
  - go-cam
  format: http
- category: DataModelProduct
  id: go-cam.model
  name: GO-CAM Model Format
  description: RDF-based format for representing causal activity models in Gene Ontology
  product_url: https://github.com/geneontology/go-cam
  original_source:
  - go-cam
  format: rdfxml
- category: ProgrammingInterface
  id: go-cam.api
  name: GO-CAM API
  description: Programmatic access to GO-CAM models through the Gene Ontology API
  product_url: http://api.geneontology.org/api/
  is_public: true
  connection_url: http://api.geneontology.org/api/
  original_source:
  - go-cam
- category: ProcessProduct
  id: go-cam.minerva
  name: Minerva
  description: Server-side component for storing, validating, and reasoning over GO-CAM models
  product_url: https://github.com/geneontology/minerva
  original_source:
  - go-cam
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
