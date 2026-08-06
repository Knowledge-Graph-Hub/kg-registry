---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: allyson.lister@oerc.ox.ac.uk
  - contact_type: github
    value: allysonlister
  label: Allyson Lister
  orcid: 0000-0002-7702-4495
creation_date: '2025-09-29T00:00:00Z'
description: The Software Ontology (SWO) is a resource for describing software tools,
  their types, tasks, versions, provenance and associated data. It contains detailed
  information on licensing and formats as well as software applications themselves,
  mainly (but not limited) to the bioinformatics community.
domains:
- biomedical
- information technology
homepage_url: https://github.com/allysonlister/swo
id: swo
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Software ontology
products:
- category: OntologyProduct
  description: Software ontology in OWL format
  format: owl
  id: swo.owl
  name: swo.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swo
  product_file_size: 236485
  product_url: http://purl.obolibrary.org/obo/swo.owl
- category: OntologyProduct
  description: Software ontology in JSON format
  format: json
  id: swo.json
  name: swo.json
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swo
  product_file_size: 204434
  product_url: http://purl.obolibrary.org/obo/swo.json
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Software Ontology (SWO), produced by KG-Bioportal
    from the BioPortal submission. The archive contains SWO_nodes.tsv and SWO_edges.tsv.
  edge_count: 5783
  format: kgx
  id: swo.kg-bioportal
  latest_version: '2023-03-05'
  name: SWO KGX graph (KG-Bioportal)
  node_count: 3542
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swo
  product_file_size: 220577
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/SWO.tar.gz
publications:
- authors:
  - Malone J
  - Brown A
  - Lister AL
  - Ison J
  - Hull D
  - Parkinson H
  - Stevens R
  doi: 10.1186/2041-1480-5-25
  id: https://www.ncbi.nlm.nih.gov/pubmed/25068035
  journal: J Biomed Semantics
  title: 'The Software Ontology (SWO): a resource for reproducibility in biomedical
    data analysis, curation and digital preservation'
  year: '2014'
repository: https://github.com/allysonlister/swo
---
## Description

The Software Ontology (SWO) is a resource for describing software tools, their types, tasks, versions, provenance and associated data. It contains detailed information on licensing and formats as well as software applications themselves, mainly (but not limited) to the bioinformatics community.

## Contacts

- Allyson Lister (allyson.lister@oerc.ox.ac.uk) [ORCID: 0000-0002-7702-4495](https://orcid.org/0000-0002-7702-4495)

## Products

### swo.owl

Software ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/swo.owl](http://purl.obolibrary.org/obo/swo.owl)

**Format**: owl

### swo.json

Software ontology in JSON format

**URL**: [http://purl.obolibrary.org/obo/swo.json](http://purl.obolibrary.org/obo/swo.json)

**Format**: json

## Publications

- [The Software Ontology (SWO): a resource for reproducibility in biomedical data analysis, curation and digital preservation](https://www.ncbi.nlm.nih.gov/pubmed/25068035)

**Domains**: biomedical

---

*This resource was automatically synchronized from the OBO Foundry registry.*