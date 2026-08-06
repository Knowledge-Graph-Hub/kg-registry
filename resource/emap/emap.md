---
activity_status: inactive
category: Ontology
collection:
  - obo-foundry
contacts:
  - category: Individual
    label: Terry Hayamizu
    orcid: 0000-0002-0956-8634
    contact_details:
      - contact_type: email
        value: Terry.Hayamizu@jax.org
      - contact_type: github
        value: tfhayamizu
creation_date: '2025-09-29T00:00:00Z'
description: A structured controlled vocabulary of stage-specific anatomical structures of the mouse (Mus).
domains:
  - anatomy and development
homepage_url: http://emouseatlas.org
id: emap
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: Mouse gross anatomy and development, timed
products:
  - category: OntologyProduct
    description: Mouse gross anatomy and development, timed in OWL format
    format: owl
    id: emap.owl
    name: emap.owl
    product_file_size: 611769
    product_url: http://purl.obolibrary.org/obo/emap.owl
    original_source:
      - source: emap
        relation_type: prov:hadPrimarySource
  - id: emap.kg-bioportal
    name: EMAP KGX graph (KG-Bioportal)
    category: GraphProduct
    description: KGX TSV transform of Mouse Gross Anatomy and Development Ontology (EMAP), produced by KG-Bioportal from the BioPortal submission. The archive contains EMAP_nodes.tsv and EMAP_edges.tsv.
    product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/EMAP.tar.gz
    format: kgx
    compression: targz
    original_source:
      - source: emap
        relation_type: prov:hadPrimarySource
    node_count: 19455
    edge_count: 21721
    latest_version: unknown
taxon:
  - NCBITaxon:10088
publications: []
use_instead:
  - emapa
---

## Description

A structured controlled vocabulary of stage-specific anatomical structures of the mouse (Mus).

## Contacts

- Terry Hayamizu (Terry.Hayamizu@jax.org) [ORCID: 0000-0002-0956-8634](https://orcid.org/0000-0002-0956-8634)

## Products

### emap.owl

Mouse gross anatomy and development, timed in OWL format

**URL**: [http://purl.obolibrary.org/obo/emap.owl](http://purl.obolibrary.org/obo/emap.owl)

**Format**: owl

**Domains**: anatomy and development

**Taxon**: NCBITaxon:10088

---

*This resource was automatically synchronized from the OBO Foundry registry.*
