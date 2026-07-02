---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.epa.gov/ground-water-and-drinking-water/safe-drinking-water-information-system-sdwis-federal-reporting
  label: US Environmental Protection Agency
creation_date: '2026-07-01T00:00:00Z'
description: The Safe Drinking Water Information System (SDWIS) is the US Environmental
  Protection Agency's national database of public water system information collected
  under the Safe Drinking Water Act. It records public water systems, their sampling
  points, monitoring results, and violations, including per- and polyfluoroalkyl substance
  (PFAS) sampling reported by states and EPA. SDWIS PFAS results are distributed through
  the EPA PFAS Analytic Tools and SDWIS Federal Reports interfaces. SAWGraph uses
  SDWIS drinking water PFAS data as a primary source for PFAS occurrence in public
  water systems.
domains:
- environment
- public health
- chemistry and biochemistry
homepage_url: https://www.epa.gov/ground-water-and-drinking-water/safe-drinking-water-information-system-sdwis-federal-reporting
id: epa-sdwis
last_modified_date: '2026-07-01T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: US federal government public domain
name: EPA Safe Drinking Water Information System (SDWIS)
products:
- category: GraphicalInterface
  description: EPA overview page describing SDWIS federal reporting, the national
    database of public water system information collected under the Safe Drinking
    Water Act.
  format: http
  id: epa-sdwis.landing
  name: EPA SDWIS federal reporting landing page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epa-sdwis
  product_url: https://www.epa.gov/ground-water-and-drinking-water/safe-drinking-water-information-system-sdwis-federal-reporting
- category: GraphicalInterface
  description: The SDWIS Federal Reports Search interface for querying public water
    system, sampling, and violation data.
  format: http
  id: epa-sdwis.reports
  name: SDWIS Federal Reports Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epa-sdwis
  product_url: https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/sdwis_fed_reports_public/200
- category: GraphProduct
  description: The SAWGraph PFAS knowledge graph, integrating PFAS observations and
    releases with the samples, geospatial features, environmental media, and chemical
    substances they describe. The RDF (Turtle) graph is constructed from federal and
    state PFAS datasets and geospatial reference data, and is served through the SAWGraph
    SPARQL and Triple Pattern Fragments endpoints.
  format: ttl
  id: sawgraph.graph
  name: SAWGraph PFAS Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sawgraph
  - relation_type: prov:hadPrimarySource
    source: epa-sdwis
  - relation_type: prov:hadPrimarySource
    source: epa-ucmr
  - relation_type: prov:hadPrimarySource
    source: water-quality-portal
  - relation_type: prov:hadPrimarySource
    source: epa-ghg
  - relation_type: prov:hadPrimarySource
    source: epa-frs
  - relation_type: prov:hadPrimarySource
    source: maine-egad
  product_url: https://github.com/SAWGraph/pfas-kg
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: epa-echo
  - relation_type: prov:wasInfluencedBy
    source: usgs-nhd
  - relation_type: prov:wasInfluencedBy
    source: us-census
  - relation_type: prov:wasInfluencedBy
    source: knowwheregraph
  - relation_type: prov:wasInfluencedBy
    source: ssurgo
  - relation_type: prov:wasInfluencedBy
    source: cropland-data-layer
---
## Description

The Safe Drinking Water Information System (SDWIS) is the US Environmental
Protection Agency's national database of public water system information
collected under the Safe Drinking Water Act. It records public water systems,
their sampling points, monitoring results, and violations, including per- and
polyfluoroalkyl substance (PFAS) sampling.

SAWGraph uses SDWIS drinking water PFAS data, obtained through the EPA PFAS
Analytic Tools, as a primary source for PFAS occurrence in public water systems.