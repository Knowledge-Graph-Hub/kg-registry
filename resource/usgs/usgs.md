---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.usgs.gov/
  label: U.S. Geological Survey (USGS)
creation_date: '2026-07-03T00:00:00Z'
description: The U.S. Geological Survey (USGS) is the science agency of the U.S. Department
  of the Interior. It produces and publishes data and research across the biological,
  geological, hydrological, and geographic sciences, and distributes datasets through
  its data repositories, including the ScienceBase catalog.
domains:
- environment
- general
homepage_url: https://www.usgs.gov/
id: usgs
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
name: U.S. Geological Survey (USGS)
products:
- category: GraphicalInterface
  description: USGS data catalog and products portal providing access to USGS-published
    scientific datasets across the biological, geological, hydrological, and geographic
    sciences.
  format: http
  id: usgs.data
  name: USGS Science Data Catalog
  original_source:
  - relation_type: prov:hadPrimarySource
    source: usgs
  product_url: https://www.usgs.gov/products/data
- category: GraphicalInterface
  description: ScienceBase is the USGS data and information repository for cataloging,
    managing, and distributing scientific data and associated metadata.
  format: http
  id: usgs.sciencebase
  name: USGS ScienceBase Catalog
  original_source:
  - relation_type: prov:hadPrimarySource
    source: usgs
  product_url: https://www.sciencebase.gov/catalog/
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
# U.S. Geological Survey (USGS)

The U.S. Geological Survey is a federal scientific agency that studies the
landscape, natural resources, and natural hazards of the United States. It publishes
a broad range of open datasets and data products, distributed largely through its
ScienceBase repository and science data catalog, that are widely reused in
environmental and biological research.