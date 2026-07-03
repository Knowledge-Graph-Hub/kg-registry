---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://vdjserver.org/
  label: VDJServer
creation_date: '2026-07-02T00:00:00Z'
description: VDJServer is a NIAID-supported, cloud-based analysis portal and public
  data repository for adaptive immune receptor repertoire (AIRR) sequencing data.
  It provides tools for processing B-cell and T-cell receptor repertoire sequences
  and hosts an AIRR Data Commons-compliant repository for sharing immune repertoire
  datasets. VDJServer is one of the NIAID-sponsored repositories whose dataset metadata
  is harvested and indexed by the NIAID Data Ecosystem Discovery Portal.
domains:
- biomedical
- immunology
- genomics
homepage_url: https://vdjserver.org/
id: vdjserver
last_modified_date: '2026-07-02T00:00:00Z'
layout: resource_detail
name: VDJServer
products:
- category: DataSource
  description: Cloud-based analysis portal and AIRR-compliant repository for searching,
    browsing, and downloading immune repertoire sequencing datasets.
  format: http
  id: vdjserver.portal
  name: VDJServer Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: vdjserver
  product_url: https://vdjserver.org/
- category: GraphProduct
  description: RDF (Turtle) knowledge graph of the NIAID Data Ecosystem, harmonizing
    dataset and computational-tool metadata harvested from NIAID-funded and globally-relevant
    infectious and immune-mediated disease repositories. Served through the Proto-OKN
    FRINK federated SPARQL platform.
  format: ttl
  id: nde.graph
  name: NIAID Data Ecosystem KG (graph)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nde
  - relation_type: prov:hadPrimarySource
    source: immport
  - relation_type: prov:hadPrimarySource
    source: vdjserver
  product_url: https://frink.apps.renci.org/nde
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: gene-expression-omnibus
  - relation_type: prov:wasInfluencedBy
    source: sra
  - relation_type: prov:wasInfluencedBy
    source: omicsdi
  - relation_type: prov:wasInfluencedBy
    source: hubmap
  - relation_type: prov:wasInfluencedBy
    source: massive
  - relation_type: prov:wasInfluencedBy
    source: pdb
  - relation_type: prov:wasInfluencedBy
    source: lincs
taxon:
- NCBITaxon:9606
---
VDJServer

## Description

VDJServer is a NIAID-supported cloud analysis platform and AIRR-compliant data
repository for adaptive immune receptor repertoire (AIRR) sequencing. It is one of
the source repositories harvested by the NIAID Data Ecosystem Discovery Portal.