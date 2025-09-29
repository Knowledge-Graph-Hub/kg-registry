---
activity_status: active
category: DataModel
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: bpeters@lji.org
  - contact_type: github
    value: bpeters42
  label: Bjoern Peters
  orcid: 0000-0002-8457-6693
description: An integrated ontology for the description of life-science and clinical
  investigations
domains:
- biomedical
homepage_url: http://obi-ontology.org
id: obi
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Ontology for Biomedical Investigations
products:
- description: The full version of OBI in OWL format
  format: owl
  id: obi.owl
  name: OBI
  product_file_size: 724538
  product_url: http://purl.obolibrary.org/obo/obi.owl
- description: The OBO-format version of OBI
  format: obo
  id: obi.obo
  name: OBI in OBO
  product_file_size: 299710
  product_url: http://purl.obolibrary.org/obo/obi.obo
- description: A collection of important high-level terms and their relations from
    OBI and other ontologies
  format: owl
  id: obi.obi_core.owl
  name: OBI Core
  product_file_size: 47011
  product_url: http://purl.obolibrary.org/obo/obi/obi_core.owl
- description: Base module for OBI
  format: owl
  id: obi.obi-base.owl
  name: OBI Base module
  product_file_size: 604323
  product_url: http://purl.obolibrary.org/obo/obi/obi-base.owl
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - do
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - cmap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - do
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - cmap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: DataModelProduct
  description: The latest release of EFO in OWL format
  format: owl
  id: efo.owl
  name: EFO OWL
  original_source:
  - bfo
  - bto
  - chebi
  - cl
  - clo
  - cob
  - dc
  - do
  - ecto
  - efo
  - fbbt
  - fbdv
  - fma
  - go
  - hancestro
  - hp
  - iao
  - ido
  - ma
  - mondo
  - mp
  - mpath
  - ncbitaxon
  - ncit
  - oba
  - obi
  - ogms
  - oio
  - omit
  - omo
  - ordo
  - pato
  - po
  - pr
  - ro
  - semapv
  - skos
  - so
  - to
  - uberon
  - uo
  - wbls
  - zfa
  product_file_size: 240665663
  product_url: https://www.ebi.ac.uk/efo/efo.owl
  secondary_source:
  - efo
- category: DataModelProduct
  description: The latest release of EFO in OBO format
  format: obo
  id: efo.obo
  name: EFO OBO
  original_source:
  - bfo
  - bto
  - chebi
  - cl
  - clo
  - cob
  - dc
  - do
  - ecto
  - efo
  - fbbt
  - fbdv
  - fma
  - go
  - hancestro
  - hp
  - iao
  - ido
  - ma
  - mondo
  - mp
  - mpath
  - ncbitaxon
  - ncit
  - oba
  - obi
  - ogms
  - oio
  - omit
  - omo
  - ordo
  - pato
  - po
  - pr
  - ro
  - semapv
  - skos
  - so
  - to
  - uberon
  - uo
  - wbls
  - zfa
  product_file_size: 64058275
  product_url: https://www.ebi.ac.uk/efo/efo.obo
  secondary_source:
  - efo
- category: DataModelProduct
  description: The Basic subset of the Plant Trait Ontology in OBO format
  format: obo
  id: to-basic.obo
  latest_version: v2025-05-20
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: Plant Trait Ontology Basic OBO
  original_source:
  - to
  - chebi
  - ro
  - ncbitaxon
  - go
  - omo
  - ecto
  - ido
  - oio
  - pato
  - envo
  - ohmi
  - iao
  - omrse
  - obi
  - peco
  - po
  - uberon
  - ogms
  - bfo
  product_file_size: 111996
  product_url: http://purl.obolibrary.org/obo/to/subsets/to-basic.obo
  secondary_source:
  - to
  versions:
  - v2025-05-20
  - v2023-07-17
  - v2022-04-13
  - v2022-03-09
  - v2021-04-06
repository: https://github.com/obi-ontology/obi
---
## Description

An integrated ontology for the description of life-science and clinical investigations

## Contacts

- Bjoern Peters (bpeters@lji.org) [ORCID: 0000-0002-8457-6693](https://orcid.org/0000-0002-8457-6693)

## Products

### OBI

The full version of OBI in OWL format

**URL**: [http://purl.obolibrary.org/obo/obi.owl](http://purl.obolibrary.org/obo/obi.owl)

**Format**: owl

### OBI in OBO

The OBO-format version of OBI

**URL**: [http://purl.obolibrary.org/obo/obi.obo](http://purl.obolibrary.org/obo/obi.obo)

**Format**: obo

### OBI Core

A collection of important high-level terms and their relations from OBI and other ontologies

**URL**: [http://purl.obolibrary.org/obo/obi/obi_core.owl](http://purl.obolibrary.org/obo/obi/obi_core.owl)

**Format**: owl

### OBI Base module

Base module for OBI

**URL**: [http://purl.obolibrary.org/obo/obi/obi-base.owl](http://purl.obolibrary.org/obo/obi/obi-base.owl)

**Format**: owl

## Publications

- [The Ontology for Biomedical Investigations](https://www.ncbi.nlm.nih.gov/pubmed/27128319)

**Domains**: biomedical

---

*This resource was automatically synchronized from the OBO Foundry registry.*