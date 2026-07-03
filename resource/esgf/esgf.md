---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://esgf.llnl.gov/
  label: Earth System Grid Federation
creation_date: '2026-07-03T00:00:00Z'
description: The Earth System Grid Federation (ESGF) is an international, distributed
  data infrastructure that archives and serves climate model output and observational
  data, including the CMIP model ensembles. ESGF exposes dataset metadata such as
  source_id, experiment_id, variable_id, and activity_id through federated search
  nodes and APIs, enabling discovery and download of climate simulation datasets.
domains:
- environment
- information technology
- general
homepage_url: https://esgf.llnl.gov/
id: esgf
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
name: Earth System Grid Federation (ESGF)
products:
- category: ProgrammingInterface
  description: The ESGF search interface (MetaGrid / AIMS) provides discovery and
    access to climate dataset metadata across the federation, including CMIP model
    output indexed by source_id, experiment_id, variable_id, and activity_id.
  format: http
  id: esgf.search
  name: ESGF Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: esgf
  product_url: https://aims2.llnl.gov/search
- category: GraphProduct
  description: RDF/Turtle knowledge graph integrating climate model and dataset metadata
    (from ESGF, CMIP controlled vocabularies, and the NASA GCMD keyword taxonomy)
    with entities and relationships extracted from climate-science publications. Served
    through the FRINK federation and the SPARQL and TPF endpoints.
  format: ttl
  id: climatemodelskg.graph
  name: Climate Models KG Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: climatemodelskg
  - relation_type: prov:hadPrimarySource
    source: esgf
  - relation_type: prov:hadPrimarySource
    source: cmip
  - relation_type: prov:hadPrimarySource
    source: gcmd
  product_url: https://frink.renci.org/registry/kgs/climatepub4-kg/
---
## Description

The Earth System Grid Federation (ESGF) is an international, distributed data
infrastructure for archiving and serving Earth system model output and
observational datasets. It is the primary distribution system for the Coupled
Model Intercomparison Project (CMIP) ensembles and related activities. ESGF nodes
publish rich dataset metadata (source_id, experiment_id, variable_id, activity_id,
and more) that can be searched and retrieved through federated search portals and
programmatic APIs.

## Products

### ESGF Search

Federated search and download interface for climate dataset metadata across ESGF
nodes.

**URL**: [https://aims2.llnl.gov/search](https://aims2.llnl.gov/search)

**Format**: http
</content>
</invoke>