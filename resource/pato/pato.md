---
activity_status: active
category: DataModel
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: g.gkoutos@gmail.com
  - contact_type: github
    value: gkoutos
  label: George Gkoutos
  orcid: 0000-0002-2061-091X
description: An ontology of phenotypic qualities (properties, attributes or characteristics)
domains:
- biological systems
homepage_url: https://github.com/pato-ontology/pato/
id: pato
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Phenotype And Trait Ontology
products:
- description: Phenotype And Trait Ontology in OWL format
  format: owl
  id: pato.owl
  name: pato.owl
  product_file_size: 1205348
  product_url: http://purl.obolibrary.org/obo/pato.owl
- description: Phenotype And Trait Ontology in OBO format
  format: obo
  id: pato.obo
  name: pato.obo
  product_file_size: 110437
  product_url: http://purl.obolibrary.org/obo/pato.obo
- description: Phenotype And Trait Ontology in JSON format
  format: json
  id: pato.json
  name: pato.json
  product_file_size: 883967
  product_url: http://purl.obolibrary.org/obo/pato.json
- description: Includes axioms linking to other ontologies, but no imports of those
    ontologies
  format: owl
  id: pato.pato-base.owl
  name: pato.pato-base.owl
  product_file_size: 180954
  product_url: http://purl.obolibrary.org/obo/pato/pato-base.owl
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
repository: https://github.com/pato-ontology/pato
---
## Description

An ontology of phenotypic qualities (properties, attributes or characteristics)

## Contacts

- George Gkoutos (g.gkoutos@gmail.com) [ORCID: 0000-0002-2061-091X](https://orcid.org/0000-0002-2061-091X)

## Products

### pato.owl

Phenotype And Trait Ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/pato.owl](http://purl.obolibrary.org/obo/pato.owl)

**Format**: owl

### pato.obo

Phenotype And Trait Ontology in OBO format

**URL**: [http://purl.obolibrary.org/obo/pato.obo](http://purl.obolibrary.org/obo/pato.obo)

**Format**: obo

### pato.json

Phenotype And Trait Ontology in JSON format

**URL**: [http://purl.obolibrary.org/obo/pato.json](http://purl.obolibrary.org/obo/pato.json)

**Format**: json

### pato.pato-base.owl

Includes axioms linking to other ontologies, but no imports of those ontologies

**URL**: [http://purl.obolibrary.org/obo/pato/pato-base.owl](http://purl.obolibrary.org/obo/pato/pato-base.owl)

**Format**: owl

## Publications

- [The anatomy of phenotype ontologies: principles, properties and applications](https://www.ncbi.nlm.nih.gov/pubmed/28387809)
- [Using ontologies to describe mouse phenotypes](https://www.ncbi.nlm.nih.gov/pubmed/15642100)

**Domains**: biological systems

---

*This resource was automatically synchronized from the OBO Foundry registry.*