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
description: The Catalog of U.S. Federal Early Detection/Rapid Response (EDRR) Invasive
  Species Databases and Tools catalogs and describes existing online, federally supported
  databases and tools relevant to a potential national early detection and rapid response
  invasive species framework. It is published as a USGS data release on ScienceBase.
domains:
- organisms
- environment
homepage_url: https://www.sciencebase.gov/catalog/item/5bf87027e4b045bfcae2ece6
id: edrr-invasive-catalog
last_modified_date: '2026-07-03T00:00:00Z'
layout: resource_detail
name: Catalog of U.S. Federal Early Detection/Rapid Response Invasive Species Databases
  and Tools
products:
- category: Product
  description: USGS ScienceBase data release containing the catalog of U.S. federal
    early detection/rapid response invasive species databases and tools, distributed
    as tabular spreadsheet data with metadata.
  id: edrr-invasive-catalog.dataset
  name: EDRR Invasive Species Databases and Tools Catalog (Version 2.0)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: edrr-invasive-catalog
  product_url: https://www.sciencebase.gov/catalog/item/5bf87027e4b045bfcae2ece6
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-03: No Content-Length
    header found'
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
publications:
- authors:
  - Simpson A
  - Morisette JT
  - Fuller P
  - Reaser J
  - Guala GF
  doi: 10.5066/P9CNVBYR
  id: doi:10.5066/P9CNVBYR
  title: 'Catalog of U.S. Federal Early Detection/Rapid Response Invasive Species
    Databases and Tools: Version 2.0'
  year: '2019'
---
# Catalog of U.S. Federal Early Detection/Rapid Response Invasive Species Databases and Tools

This catalog documents existing online, federally supported databases and tools that
address aspects of a potential national early detection and rapid response (EDRR)
framework for invasive species. Published as a USGS data release on ScienceBase, it
provides a structured inventory of relevant federal invasive-species data resources.