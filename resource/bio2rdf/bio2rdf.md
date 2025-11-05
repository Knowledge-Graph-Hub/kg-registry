---
activity_status: inactive
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://bio2rdf.org
  label: Bio2RDF
creation_date: '2025-11-05T00:00:00Z'
description: Bio2RDF is a large-scale semantic web integration project that converts diverse biological and biomedical datasets into RDF (Resource Description Framework) and makes them available through SPARQL endpoints. The project provides linked data representations of over 35 biological databases including UniProt, GenBank, KEGG, DrugBank, and many others, enabling federated queries across heterogeneous data sources using standard semantic web technologies.
domains:
  - biomedical
  - genomics
  - biological systems
  - information technology
homepage_url: https://bio2rdf.org
id: bio2rdf
infores_id: bio2rdf
last_modified_date: '2025-11-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
name: Bio2RDF
products:
- category: ProgrammingInterface
  description: SPARQL endpoint for querying Bio2RDF linked data
  format: http
  id: bio2rdf.sparql
  name: Bio2RDF SPARQL Endpoint
  original_source:
  - bio2rdf
  product_url: https://bio2rdf.org/sparql
- category: Product
  description: RDF dumps of integrated biological databases
  format: ttl
  id: bio2rdf.dumps
  name: Bio2RDF RDF Dumps
  original_source:
  - bio2rdf
  product_url: https://download.bio2rdf.org/
- category: GraphicalInterface
  description: Web interface for browsing Bio2RDF resources
  format: http
  id: bio2rdf.web
  name: Bio2RDF Web Interface
  original_source:
  - bio2rdf
  product_url: https://bio2rdf.org
publications:
- id: https://doi.org/10.1186/2041-1480-4-S1-S1
repository: https://github.com/bio2rdf/bio2rdf-scripts
synonyms:
  - Bio2RDF
  - bio2rdf
warnings:
- The Bio2RDF project has reduced activity in recent years. Some endpoints and data may be outdated or unavailable.
---

# Bio2RDF

## Overview

Bio2RDF is a large-scale semantic web integration project that converts diverse biological and biomedical datasets into RDF (Resource Description Framework) and makes them available through SPARQL endpoints. 

The project provides linked data representations of over 35 biological databases including UniProt, GenBank, KEGG, DrugBank, and many others, enabling federated queries across heterogeneous data sources using standard semantic web technologies.

## Key Features

- **Semantic Web Integration**: Converts biological databases to RDF format
- **SPARQL Access**: Provides SPARQL endpoints for federated queries
- **Linked Data**: Creates links between related entities across databases
- **Standardized Identifiers**: Uses consistent URI schemes for biological entities
- **Multiple Data Sources**: Integrates 35+ major biological databases

## Integrated Databases

Bio2RDF provides RDF representations of numerous databases including:
- Protein databases (UniProt, PDB)
- Genomic databases (GenBank, Ensembl)
- Pathway databases (KEGG, Reactome)
- Drug databases (DrugBank, ChEMBL)
- Disease databases (OMIM, Orphanet)
- And many more

## Products

### SPARQL Endpoint
Query Bio2RDF's integrated linked data using standard SPARQL queries across multiple biological data sources.

### RDF Dumps
Download complete RDF representations of integrated biological databases for local processing and analysis.

### Web Interface
Browse and explore Bio2RDF resources through a web-based interface.

## Information Resource ID

This resource has the Information Resource identifier: `infores:bio2rdf`

## Publications

- [Bio2RDF Release 2: Improved Coverage, Interoperability and Provenance of Life Science Linked Data](https://doi.org/10.1186/2041-1480-4-S1-S1) (2013)

## Domains

- Biomedical
- Genomics
- Biological Systems
- Information Technology

## Status Note

The Bio2RDF project has reduced activity in recent years. Some endpoints and data may be outdated or unavailable. Users should verify the availability of specific resources before relying on them for production workflows.

