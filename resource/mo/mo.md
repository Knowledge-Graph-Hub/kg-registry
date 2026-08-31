---
activity_status: inactive
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: stoeckrt@pcbi.upenn.edu
  label: Chris Stoeckert
  orcid: 0000-0002-5714-991X
creation_date: '2025-09-29T00:00:00Z'
description: A standardized description of a microarray experiment in support of MAGE
  v.1.
domains:
- biomedical
- general
homepage_url: http://mged.sourceforge.net/ontologies/MGEDontology.php
id: mo
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: Microarray experimental conditions
products:
- category: OntologyProduct
  description: Microarray experimental conditions in OWL format
  format: owl
  id: mo.owl
  name: mo.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mo
  product_url: http://purl.obolibrary.org/obo/mo.owl
  warnings:
  - The original OBO PURL (http://purl.obolibrary.org/obo/mo.owl) no longer resolves
    (HTTP 404); product_url now points to a Wayback Machine archived snapshot of the
    MGED Ontology OWL.
  - 'File was not able to be retrieved when checked on 2026-08-17: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-08-31: HTTP 404 error
    when accessing file'
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Microarray and Gene Expression Data Ontology (MO),
    produced by KG-Bioportal from the BioPortal submission. The archive contains MO_nodes.tsv
    and MO_edges.tsv.
  edge_count: 464
  format: kgx
  id: mo.kg-bioportal
  latest_version: 1.3.1.1
  name: MO KGX graph (KG-Bioportal)
  node_count: 1045
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mo
  product_file_size: 18675
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.08/MO.tar.gz
publications:
- authors:
  - Whetzel PL
  - Parkinson H
  - Causton HC
  - Fan L
  - Fostel J
  - Fragoso G
  - Game L
  - Heiskanen M
  - Morrison N
  - Rocca-Serra P
  - Sansone SA
  - Taylor C
  - White J
  - Stoeckert CJ Jr
  doi: 10.1093/bioinformatics/btl005
  id: https://www.ncbi.nlm.nih.gov/pubmed/16428806
  journal: Bioinformatics
  preferred: true
  title: 'The MGED Ontology: a resource for semantics-based description of microarray
    experiments'
  year: '2006'
repository: https://sourceforge.net/projects/mged/
use_instead:
- obi
---
## Description

A standardized description of a microarray experiment in support of MAGE v.1.

## Contacts

- Chris Stoeckert (stoeckrt@pcbi.upenn.edu) [ORCID: 0000-0002-5714-991X](https://orcid.org/0000-0002-5714-991X)

## Products

### mo.owl

Microarray experimental conditions in OWL format

**URL**: [http://purl.obolibrary.org/obo/mo.owl](http://purl.obolibrary.org/obo/mo.owl)

**Format**: owl

**Domains**: biomedical

---

*This resource was automatically synchronized from the OBO Foundry registry.*