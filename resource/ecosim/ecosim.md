---
layout: resource_detail
activity_status: active
collection:
  - ber
id: ecosim
name: ecosim
description: Ontology rendering of the EcoSIM Land System Model
domains:
  - environment
contacts:
  - category: Individual
    label: Christopher J. Mungall
    orcid: 0000-0002-6601-2165
    contact_details:
      - contact_type: email
        value: cjmungall@lbl.gov
      - contact_type: github
        value: cmungall
homepage_url: https://github.com/bioepic-data/ecosim-ontology
repository: https://github.com/bioepic-data/ecosim-ontology
products:
  - id: ecosim.model.owl
    name: ecosim OWL release
    description: OWL release of ecosim
    category: Product
    format: owl
    original_source:
      - source: ecosim
        relation_type: prov:hadPrimarySource
  - id: ecosim.kg-bioportal
    name: ECOSIM KGX graph (KG-Bioportal)
    category: GraphProduct
    description: KGX TSV transform of ecosim ontology (ECOSIM), produced by KG-Bioportal from the BioPortal submission. The archive contains ECOSIM_nodes.tsv and ECOSIM_edges.tsv.
    product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/ECOSIM.tar.gz
    format: kgx
    compression: targz
    original_source:
      - source: ecosim
        relation_type: prov:hadPrimarySource
    node_count: 6
    edge_count: 1
    latest_version: '2025-05-29'
category: Resource
creation_date: '2025-03-09T00:00:00Z'
last_modified_date: '2026-08-06T00:00:00Z'
---

Ontology rendering of the EcoSIM Land System Model
