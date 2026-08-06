---
activity_status: inactive
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  label: Jonathan Bard
  contact_details:
  - contact_type: email
    value: J.Bard@ed.ac.uk
creation_date: '2025-09-29T00:00:00Z'
description: Description unavailable.
domains:
- anatomy and development
homepage_url: http://genex.hgu.mrc.ac.uk/
id: ehda
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: Human developmental anatomy, timed version
products:
- id: ehda.kg-bioportal
  name: EHDA KGX graph (KG-Bioportal)
  category: GraphProduct
  description: KGX TSV transform of Human Developmental Anatomy Ontology, timed version
    (EHDA), produced by KG-Bioportal from the BioPortal submission. The archive contains
    EHDA_nodes.tsv and EHDA_edges.tsv.
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/EHDA.tar.gz
  format: kgx
  compression: targz
  original_source:
  - source: ehda
    relation_type: prov:hadPrimarySource
  node_count: 8353
  edge_count: 8339
  latest_version: unknown
publications:
- authors:
  - Hunter A
  - Kaufman MH
  - McKay A
  - Baldock R
  - Simmen MW
  - Bard JBL
  doi: 10.1046/j.1469-7580.2003.00224.x
  id: https://pubmed.ncbi.nlm.nih.gov/14620375/
  journal: J Anat
  preferred: true
  title: An ontology of human developmental anatomy
  year: '2003'
taxon:
- NCBITaxon:9606
use_instead:
- ehdaa2
---
## Description

A structured controlled vocabulary of stage-specific anatomical structures of the human. It has been designed to mesh with the mouse anatomy and incorporates each Carnegie stage of development (CS1-20). This timed version is deprecated in the OBO Foundry, which identifies EHDAA2 as the successor resource.

## Contacts

- Jonathan Bard (J.Bard@ed.ac.uk)

**Domains**: anatomy and development

**Taxon**: NCBITaxon:9606

---

*This resource was automatically synchronized from the OBO Foundry registry.*
