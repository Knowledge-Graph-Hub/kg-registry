---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: jano@geog.ucsb.edu
  label: Krzysztof Janowicz
  orcid: 0000-0003-4727-3564
- category: Organization
  contact_details:
  - contact_type: url
    value: https://knowwheregraph.org/
  id: ucsb-geography
  label: University of California, Santa Barbara - Department of Geography
creation_date: '2025-12-17T00:00:00Z'
description: KnowWhereGraph is a large-scale geospatial and environmental knowledge
  graph containing over 29 billion RDF triples. It fuses knowledge graph technology
  with geo-enrichment capabilities to provide location-centric answers about environmental
  and human systems globally. The graph integrates 30+ data layers spanning natural
  hazards, climate, soil properties, demographics, health, agriculture, and more.
domains: []
funding:
- National Science Foundation (NSF) - Convergence Accelerated Program (OIA-2033521)
homepage_url: https://knowwheregraph.org/
id: knowwheregraph
infores_id: knowwheregraph
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: KnowWhereGraph
products:
- category: GraphProduct
  description: KnowWhereGraph knowledge graph with 29+ billion RDF triples integrating
    30+ environmental and geospatial data layers accessible through SPARQL endpoint
  edge_count: 29000000000
  format: rdfxml
  id: knowwheregraph.graph
  name: KnowWhereGraph RDF Knowledge Graph
  node_count: 5000000000
  product_url: https://knowwheregraph.org/
- category: ProgrammingInterface
  description: SPARQL endpoint with GeoSPARQL support for querying KnowWhereGraph
    data and performing geospatial queries
  format: http
  id: knowwheregraph.sparql
  is_public: true
  name: KnowWhereGraph SPARQL Endpoint
  product_url: https://knowwheregraph.org/sparql/
- category: GraphicalInterface
  description: Faceted search interface providing table and map-based views for browsing
    and discovering KnowWhereGraph data with automatic SPARQL query generation
  format: http
  id: knowwheregraph.explorer
  is_public: true
  name: KnowWhereGraph Knowledge Explorer
  product_url: https://www.knowwheregraph.org/tools/knowledge-explorer/
- category: DocumentationProduct
  description: Comprehensive ontology documentation and reference for the KnowWhereGraph
    ontology with 150 classes, 70 object properties, and 75 data properties
  format: http
  id: knowwheregraph.ontology
  is_public: true
  name: KnowWhereGraph Ontology Documentation
  product_url: https://stko-kwg.geog.ucsb.edu/lod/ontology
  warnings:
  - 'File was not able to be retrieved when checked on 2026-02-15: HTTP 404 error
    when accessing file'
  - File was not able to be retrieved when checked on 2026-02-13_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-05_ Error connecting
    to URL_ HTTPSConnectionPool(host='stko-kwg.geog.ucsb.edu', port=443)_ Max retries
    exceeded with url_ /lod/ontology (Caused by NewConnectionError("HTTPSConnection(host='stko-kwg.geog.ucsb.edu',
    port=443)_ Failed to establish a new connection_ [Errno 111] Connection refused"))
  - File was not able to be retrieved when checked on 2025-12-17_ Timeout connecting
    to URL
publications:
- authors:
  - Zhu R
  - Shimizu C
  - Janowicz K
  - Hitzler P
  doi: 10.48550/arXiv.2502.13874
  id: arXiv:2502.13874
  journal: arXiv
  preferred: true
  title: 'The KnowWhereGraph: A Large-Scale Geo-Knowledge Graph for Interdisciplinary
    Knowledge Discovery and Geo-Enrichment'
  year: '2025'
- authors:
  - Shimizu C
  - Hitzler P
  - Janowicz K
  doi: 10.1016/j.websem.2024.100819
  id: doi:10.1016/j.websem.2024.100819
  journal: Journal of Web Semantics
  title: The KnowWhereGraph Ontology
  year: '2024'
- authors:
  - Janowicz K
  - Hitzler P
  - Li W
  - Rehberger D
  - Schildhauer M
  doi: 10.1002/aaai.12043
  id: doi:10.1002/aaai.12043
  journal: AI Magazine
  title: 'Know, Know Where, KnowWhereGraph: A Densely Connected, Cross-Domain Knowledge
    Graph and Geo-Enrichment Service Stack for Applications in Environmental Intelligence'
  year: '2022'
repository: https://github.com/KnowWhereGraph
usages:
- description: Humanitarian aid coordination and supply chain management during crises
  id: knowwheregraph.use.humanitarian
  label: Humanitarian Response
- description: Food supply chain sustainability, agriculture sustainability assessment
  id: knowwheregraph.use.supply_chain
  label: Supply Chain Management
- description: Disaster response, emergency management, natural hazard assessment
  id: knowwheregraph.use.emergency
  label: Emergency Management
- description: Farm credit assessment, land valuation, agricultural potential evaluation
  id: knowwheregraph.use.agriculture
  label: Agricultural Finance
---
# KnowWhereGraph

## Overview

KnowWhereGraph is the first large-scale geospatial and environmental knowledge graph, combining knowledge graph technology with geo-enrichment capabilities to answer fundamental geographic questions: "What is here?", "What happened here before?", and "How does this region compare to...?" for any location on Earth within seconds.

The graph contains over 29 billion RDF triples representing densely-integrated statements across diverse environmental and human systems domains. It integrates 30+ data layers spanning natural hazards, climate variables, soil properties, demographics, health indicators, agriculture, and more, creating a comprehensive framework for environmental intelligence and geospatial knowledge discovery.

## Data Content and Scale

### Graph Statistics

- **Total Triples**: 29+ billion RDF statements
- **Node Count**: Estimated 5+ billion entities
- **Data Layers Integrated**: 30+ diverse datasets
- **Spatial Coverage**: Global - designed for any location on Earth

### Domains and Topics

KnowWhereGraph covers a comprehensive range of environmental and human systems:

**Environmental and Climate:**
- Natural hazards: hurricanes, wildfires, earthquakes, debris flows, severe weather
- Climate variables: air temperature, precipitation, climate divisions, seasonal patterns
- Soil properties: soil types, soil characteristics, pedogenic processes
- Land cover: crop types, land use classifications
- Water systems: hydrological features, water availability

**Human and Social Systems:**
- Demographics: population statistics, population density, population change
- Human health: health indicators, disease data, health outcomes
- Transportation: transportation networks, infrastructure data
- Food systems: agricultural production, food security, food supply chains
- Expert networks: domain expertise, research networks

**Geographic and Spatial:**
- Place and region identifiers: gazetteers, boundaries
- Hierarchical spatial representations: S2 Discrete Global Grid cells
- Multiple geographic conceptualizations: ZIP codes, climate divisions, administrative boundaries
- Geopolitical boundaries: administrative regions, political entities

## Data Access and Formats

### Query Interfaces

**SPARQL Endpoint**
- Direct SPARQL and GeoSPARQL query support
- Location: https://knowwheregraph.org/sparql/
- Enables complex geospatial queries across all data layers
- Supports spatial reasoning and analysis

**Knowledge Explorer**
- Web-based faceted search interface
- Features:
  - Faceted filtering by multiple data characteristics
  - Table view and map view panels for results
  - Automatic SPARQL query generation from user input
  - Hyperlinked result navigation for graph dereferencing
- Location: https://www.knowwheregraph.org/tools/knowledge-explorer/

### GIS Integration

**ArcGIS Integration**
- Native ArcGIS Pro plugin for graph queries
- Automatic geodatabase creation from query results
- Seamless integration with GIS workflows

**QGIS Integration**
- Open-source GIS plugin for graph querying
- Geo-enrichment capabilities within QGIS
- Support for adding multidisciplinary geospatial data

### Data Format

- **Primary Format**: RDF (Resource Description Framework)
- **Standards**: OWL (Web Ontology Language), GeoSPARQL, SHACL
- **Ontologies**: Custom KnowWhereGraph Ontology, SOSA, OWL-Time, GeoSPARQL
- **Spatial Representation**: S2 Hierarchical Discrete Global Grid (DGG)
- **Backend**: GraphDB semantic repository

## Technical Architecture

### Ontology

The KnowWhereGraph Ontology (KWGO) provides the semantic foundation:
- **150 entity classes** for representing concepts
- **70 object properties** for relationships
- **75 data properties** for attributes
- Modular design for extensibility
- Alignment with standard semantic web vocabularies

### Design Principles

- **Geo-enrichment**: Specialized capabilities for linking disparate geospatial datasets
- **Cross-domain integration**: Semantic linking across diverse data silos
- **Densely connected**: Highly interconnected through inferred relationships
- **Spatially explicit**: All data elements have spatial grounding
- **Semantically lifted**: Includes novel strategies for lifting imagery data into semantic form

## Key Features

### Geo-Enrichment Pioneer

KnowWhereGraph is pioneering geo-enrichment capabilities directly integrated into knowledge graphs and GIS environments, enabling:
- Automatic data enrichment based on spatial relationships
- Cross-domain insights for any geographic location
- Multidisciplinary data synthesis at scale

### Multi-Interface Access

Multiple complementary interfaces for different use cases:
- Programmatic access for developers (SPARQL, GeoSPARQL)
- GIS-native tools for domain specialists (ArcGIS, QGIS)
- Faceted search for knowledge discovery (Knowledge Explorer)
- API-based access for application integration

### Densely Connected Graph

Highly interconnected relationships enable:
- Complex multi-hop queries across domains
- Inference of new knowledge through semantic relationships
- Comparative analysis across regions and time periods

### Semantically Lifted Imagery

Novel approaches to include:
- Remotely sensed imagery integrated as knowledge graph entities
- Drone imagery semantically linked to ground-truth data
- AI-based methods for automated imagery analysis and integration

## Use Cases and Applications

### Supply Chain Management

- Food supply chain sustainability and traceability
- Wildfires impact assessment on agricultural production
- Commodity market and supply chain analysis
- Food security assessment and forecasting

### Humanitarian Response

- Emergency response coordination and resource allocation
- Expert-need matching during crises
- Humanitarian aid supply chain management
- Crisis situation awareness and rapid assessment

### Disaster Management

- Natural hazard monitoring and forecasting
- Emergency management planning and response
- Risk assessment for communities and critical infrastructure
- Multi-hazard analysis and planning

### Agricultural Applications

- Crop planning and optimization
- Soil analysis and land suitability assessment
- Farm credit assessment and land valuation
- Agricultural sustainability evaluation
- Food system resilience analysis

### Environmental Policy

- Agricultural sustainability metrics and assessment
- Soil conservation practice evaluation
- Farm labor impact assessment
- Environmental regulation development and enforcement
- Climate adaptation planning

## Organizational Structure

### Lead Organization
- **University of California, Santa Barbara** - Center for Spatial Studies, Department of Geography

### Partner Institutions
- Kansas State University (agricultural data expertise)
- Michigan State University (soil and agricultural systems)
- Arizona State University (supply chain and optimization)
- University of Southern California (environmental systems)
- University of Bristol (knowledge graph and semantic web)

### Industry and Government Partners
- **Esri** - Geographic Information Systems technology
- **Oliver Wyman** - Commodity markets and supply chain expertise
- **Hydronos Labs** - Weather, climate, and agriculture information
- **U.S. Geological Survey (USGS)** - Geospatial data expertise
- **Natural Resources Conservation Service (NRCS)** - Agricultural and environmental data
- **Direct Relief** - Humanitarian aid operational experience

## Funding and Support

- **Funder**: National Science Foundation (NSF)
- **Program**: Convergence Accelerated Program
- **Grant**: OIA-2033521
- **Duration**: Multi-year support for infrastructure and research

## Citation and Usage

KnowWhereGraph data and services are freely available under the Creative Commons Attribution 4.0 (CC BY 4.0) license. Users are encouraged to cite appropriate KnowWhereGraph publications when using data or services in research and applications.

The knowledge graph is maintained and operated by the Center for Spatial Studies at University of California, Santa Barbara in collaboration with partner institutions and supported by the National Science Foundation.

## Automated Evaluation

- View the automated evaluation: [knowwheregraph automated evaluation](knowwheregraph_eval_automated.html)