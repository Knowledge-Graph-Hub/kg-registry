---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: edong@umich.edu
  - contact_type: github
    value: e4ong1031
  label: Edison Ong
  orcid: 0000-0002-5159-414X
creation_date: '2025-09-29T00:00:00Z'
description: OHPI is a community-driven ontology of host-pathogen interactions (OHPI)
  and represents the virulence factors (VFs) and how the mutants of VFs in the Victors
  database become less virulence inside a host organism or host cells. It is developed
  to represent manually curated HPI knowledge available in the PHIDIAS resource.
domains:
- biological systems
homepage_url: https://github.com/OHPI/ohpi
id: ohpi
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Ontology of Host Pathogen Interactions
products:
- category: OntologyProduct
  description: Ontology of Host Pathogen Interactions in OWL format
  format: owl
  id: ohpi.owl
  name: ohpi.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ohpi
  product_file_size: 1482262
  product_url: http://purl.obolibrary.org/obo/ohpi.owl
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Ontology of Host-Pathogen Interactions (OHPI),
    produced by KG-Bioportal from the BioPortal submission. The archive contains OHPI_nodes.tsv
    and OHPI_edges.tsv.
  edge_count: 41474
  format: kgx
  id: ohpi.kg-bioportal
  latest_version: 1.0.26
  name: OHPI KGX graph (KG-Bioportal)
  node_count: 14180
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ohpi
  product_file_size: 1144821
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/OHPI.tar.gz
publications:
- authors:
  - Sayers S
  - Li L
  - Ong E
  - Deng S
  - Fu G
  - Lin Y
  - Yang B
  - Zhang S
  - Fa Z
  - Zhao B
  - Xiang Z
  - Li Y
  - Zhao XM
  - Olszewski MA
  - Chen L
  - He Y
  doi: 10.1093/nar/gky999
  id: https://www.ncbi.nlm.nih.gov/pubmed/30365026
  journal: Nucleic Acids Res
  title: 'Victors: a web-based knowledge base of virulence factors in human and animal
    pathogens'
  year: '2019'
repository: https://github.com/OHPI/ohpi
---
## Description

OHPI is a community-driven ontology of host-pathogen interactions (OHPI) and represents the virulence factors (VFs) and how the mutants of VFs in the Victors database become less virulence inside a host organism or host cells. It is developed to represent manually curated HPI knowledge available in the PHIDIAS resource.

## Contacts

- Edison Ong (edong@umich.edu) [ORCID: 0000-0002-5159-414X](https://orcid.org/0000-0002-5159-414X)

## Products

### ohpi.owl

Ontology of Host Pathogen Interactions in OWL format

**URL**: [http://purl.obolibrary.org/obo/ohpi.owl](http://purl.obolibrary.org/obo/ohpi.owl)

**Format**: owl

## Publications

- [Victors: a web-based knowledge base of virulence factors in human and animal pathogens](https://www.ncbi.nlm.nih.gov/pubmed/30365026)

**Domains**: biological systems

---

*This resource was automatically synchronized from the OBO Foundry registry.*