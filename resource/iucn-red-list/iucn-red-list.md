---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.iucnredlist.org/
  label: International Union for Conservation of Nature (IUCN)
creation_date: '2026-07-03T00:00:00Z'
description: The IUCN Red List of Threatened Species is the world's most comprehensive
  information source on the global extinction risk status of animal, fungus, and plant
  species. It provides assessments of conservation status, population trends, threats,
  habitats, and geographic ranges, and is maintained by the International Union for
  Conservation of Nature (IUCN).
domains:
- organisms
- environment
homepage_url: https://www.iucnredlist.org/
id: iucn-red-list
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
name: IUCN Red List of Threatened Species
products:
- category: GraphicalInterface
  description: Web portal for searching and browsing IUCN Red List species assessments,
    including extinction risk category, population trend, threats, habitat, and range
    information.
  format: http
  id: iucn-red-list.portal
  name: IUCN Red List Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iucn-red-list
  product_url: https://www.iucnredlist.org/
- category: ProgrammingInterface
  description: IUCN Red List API providing programmatic access to species assessment
    data, conservation status categories, and related metadata.
  format: http
  id: iucn-red-list.api
  name: IUCN Red List API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iucn-red-list
  product_url: https://api.iucnredlist.org/
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
# IUCN Red List of Threatened Species

The IUCN Red List is a global inventory of the conservation status of species,
classifying taxa into categories of extinction risk based on standardized criteria.
Alongside status, each assessment documents distribution, population, habitat and
ecology, threats, and conservation actions. It is a widely used authority for
biodiversity and conservation research and policy.