---
activity_status: inactive
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: slarson@ncmir.ucsd.edu
  label: Stephen Larson
creation_date: '2025-09-29T00:00:00Z'
description: Description unavailable.
domains:
- anatomy and development
homepage_url: http://ccdb.ucsd.edu/CCDBWebSite/sao.html
id: sao
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: Subcellular anatomy ontology
products:
- category: OntologyProduct
  description: Canonical OWL edition of the Subcellular Anatomy Ontology distributed
    via OBO PURL.
  format: owl
  id: sao.owl
  name: Subcellular anatomy ontology OWL edition
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sao
  product_url: http://purl.obolibrary.org/obo/sao.owl
  warnings:
  - 'File was not able to be retrieved when checked on 2026-08-06: HTTP 404 error
    when accessing file'
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Subcellular Anatomy Ontology (SAO), produced by
    KG-Bioportal from the BioPortal submission. The archive contains SAO_nodes.tsv
    and SAO_edges.tsv.
  edge_count: 2541
  format: kgx
  id: sao.kg-bioportal
  latest_version: Version 1.2
  name: SAO KGX graph (KG-Bioportal)
  node_count: 863
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sao
  product_file_size: 40424
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/SAO.tar.gz
publications: []
taxon:
- NCBITaxon:9606
use_instead:
- go
---
## Description

The Subcellular Anatomy Ontology for the Nervous System describes cellular, subcellular,
supracellular, and macromolecular structures for microscopy and neuroscience annotation.
This ontology is deprecated, and OBO Foundry recommends using GO.

## Contacts

- Stephen Larson (slarson@ncmir.ucsd.edu)

**Domains**: anatomy and development

**Taxon**: NCBITaxon:9606

---

*This resource was automatically synchronized from the OBO Foundry registry.*