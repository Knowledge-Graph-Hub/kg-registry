---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.cabi.org/
  label: CABI
creation_date: '2026-07-03T00:00:00Z'
description: The CABI Invasive Species Compendium (ISC) is an encyclopedic reference
  resource covering invasive species that threaten agriculture, biodiversity, and
  the environment. It brings together datasheets, distribution data, host and pathway
  information, images, and a bibliographic database, and is published by CABI as part
  of the CABI Compendium on the CABI Digital Library.
domains:
- organisms
- environment
- agriculture
homepage_url: https://www.cabidigitallibrary.org/product/qi
id: cabi-isc
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
license:
  id: https://www.cabidigitallibrary.org/terms-and-conditions
  label: CABI Digital Library Terms and Conditions (proprietary / subscription)
name: CABI Invasive Species Compendium
products:
- category: GraphicalInterface
  description: Web portal for the CABI Invasive Species Compendium providing species
    datasheets, distribution and host information, and bibliographic references on
    invasive species.
  format: http
  id: cabi-isc.portal
  name: CABI Invasive Species Compendium Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cabi-isc
  product_url: https://www.cabidigitallibrary.org/product/qi
- category: GraphProduct
  description: The Wildlife-KN knowledge graph, an integrative RDF network of managed
    species and their habitats, environmental factors, and climate context, built
    to support wildlife management under climate change. It is served as Linked Data
    through the Wildlife-KN SPARQL and Triple Pattern Fragments endpoints.
  format: ttl
  id: wildlifekn.graph
  name: Wildlife-KN Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: wildlifekn
  - relation_type: prov:hadPrimarySource
    source: usgs
  - relation_type: prov:hadPrimarySource
    source: edrr-invasive-catalog
  - relation_type: prov:hadPrimarySource
    source: gbif
  - relation_type: prov:hadPrimarySource
    source: worldclim
  - relation_type: prov:hadPrimarySource
    source: iucn-red-list
  - relation_type: prov:hadPrimarySource
    source: cabi-isc
  product_url: https://apps.okn.us/ldf/wildlifekn
---
# CABI Invasive Species Compendium

The CABI Invasive Species Compendium (ISC) is a reference resource that consolidates
information on invasive species affecting agriculture, biodiversity, and the
environment. It provides detailed datasheets covering identity, distribution, hosts,
pathways, impacts, and management, backed by a bibliographic database. It is
published by CABI as part of the CABI Compendium.