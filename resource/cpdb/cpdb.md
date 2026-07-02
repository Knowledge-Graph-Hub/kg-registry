---
activity_status: active
category: Aggregator
creation_date: '2025-11-19T00:00:00Z'
description: ConsensusPathDB integrates molecular interaction data from over 30 public
  databases, including protein-protein, genetic, metabolic, signaling, gene regulatory
  and drug-target interactions. It provides comprehensive pathway and functional analysis
  tools, allowing users to explore molecular networks and pathways from multiple sources
  through a unified interface. The frames-based site remains reachable and reports
  Release 35 for the human instance, dated June 5, 2021.
domains:
- pathways
- proteomics
- systems biology
- biomedical
- biological systems
- chemistry and biochemistry
homepage_url: http://cpdb.molgen.mpg.de/
id: cpdb
infores_id: cpdb
last_modified_date: '2026-06-27T00:00:00Z'
layout: resource_detail
license:
  id: http://cpdb.molgen.mpg.de/
  label: Free for academic use; commercial users must contact the developers (integrated
    interaction data inherits the license terms of the contributing source databases)
name: ConsensusPathDB
products:
- category: GraphicalInterface
  description: Web-based interface for integrated pathway and interaction analysis
    from multiple databases
  format: http
  id: cpdb.web
  name: ConsensusPathDB Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cpdb
  product_url: http://cpdb.molgen.mpg.de/
- category: Product
  description: Download and access page for ConsensusPathDB data and service assets
  format: http
  id: cpdb.downloads
  name: ConsensusPathDB Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cpdb
  product_url: http://cpdb.molgen.mpg.de/download
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-01: No Content-Length
    header found'
- category: ProgrammingInterface
  description: SOAP web service description for ConsensusPathDB programmatic access
  format: xml
  id: cpdb.wsdl
  name: ConsensusPathDB SOAP WSDL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cpdb
  product_url: http://cpdb.molgen.mpg.de/download/CPDB.wsdl
- category: GraphProduct
  description: Knowledge graph connecting rare diseases with genes, drugs, pathways,
    and medical images
  edge_count: 22293
  id: rdbridge.graph
  name: RDBridge Knowledge Graph
  node_count: 11704
  original_source:
  - relation_type: prov:hadPrimarySource
    source: rdbridge
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: cpdb
publications:
- authors:
  - Atanas Kamburov
  - Konstantin Pentchev
  - Hanna Galicka
  - Christoph Wierling
  - Hans Lehrach
  - Ralf Herwig
  doi: 10.1093/nar/gkq1156
  id: doi:10.1093/nar/gkq1156
  journal: Nucleic Acids Research
  preferred: true
  title: 'ConsensusPathDB: toward a more complete picture of cell biology'
  year: '2011'
- authors:
  - Atanas Kamburov
  - Christoph Wierling
  - Hans Lehrach
  - Ralf Herwig
  doi: 10.1093/nar/gkn698
  id: doi:10.1093/nar/gkn698
  journal: Nucleic Acids Research
  title: ConsensusPathDB--a database for integrating human functional interaction
    networks
  year: '2009'
synonyms:
- CPDB
- CPDB-human
- ConsensusPathDB-human
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
- NCBITaxon:4932
---
# ConsensusPathDB

## Overview

ConsensusPathDB is an integrated molecular interaction database that consolidates data from over 30 public databases, including protein-protein interactions, genetic interactions, metabolic pathways, signaling pathways, gene regulatory interactions, and drug-target interactions. It provides a comprehensive platform for pathway and functional analysis of molecular networks.

The frames-based website remains reachable and reports Release 35 for the human instance, dated June 5, 2021. The site also links mouse and yeast instances. Historical `/CPDB/download` links are unavailable, but the root access page and SOAP WSDL remain reachable.

## Information Resource ID

This resource has the Information Resource identifier: `infores:cpdb`