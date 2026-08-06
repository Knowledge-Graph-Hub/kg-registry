---
activity_status: active
category: Resource
collection:
- ber
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: cjmungall@lbl.gov
  - contact_type: github
    value: cmungall
  label: Christopher J. Mungall
  orcid: 0000-0002-6601-2165
creation_date: '2025-03-09T00:00:00Z'
description: Ontology rendering of the EcoSIM Land System Model
domains:
- environment
homepage_url: https://github.com/bioepic-data/ecosim-ontology
id: ecosim
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
name: ecosim
products:
- category: Product
  description: OWL release of ecosim
  format: owl
  id: ecosim.model.owl
  name: ecosim OWL release
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecosim
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of ecosim ontology (ECOSIM), produced by KG-Bioportal
    from the BioPortal submission. The archive contains ECOSIM_nodes.tsv and ECOSIM_edges.tsv.
  edge_count: 1
  format: kgx
  id: ecosim.kg-bioportal
  latest_version: '2025-05-29'
  name: ECOSIM KGX graph (KG-Bioportal)
  node_count: 6
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecosim
  product_file_size: 489
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/ECOSIM.tar.gz
repository: https://github.com/bioepic-data/ecosim-ontology
---
Ontology rendering of the EcoSIM Land System Model