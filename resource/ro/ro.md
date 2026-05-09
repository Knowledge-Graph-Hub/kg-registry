---
activity_status: active
category: Ontology
collection:
  - obo-foundry
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: cjmungall@lbl.gov
      - contact_type: github
        value: cmungall
    label: Chris Mungall
    orcid: 0000-0002-6601-2165
creation_date: '2025-06-25T00:00:00Z'
description: Relationship types shared across multiple ontologies
domains:
  - biological systems
homepage_url: https://oborel.github.io/
id: ro
infores_id: ro
last_modified_date: '2026-04-15T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png
name: Relation Ontology
products:
  - category: OntologyProduct
    description: Canonical edition
    format: owl
    id: ro.owl
    name: Relation Ontology
    product_file_size: 132025
    product_url: http://purl.obolibrary.org/obo/ro.owl
    original_source:
      - source: ro
        relation_type: prov:hadPrimarySource
  - category: OntologyProduct
    description: The obo edition is less expressive than the OWL, and has imports merged in
    format: obo
    id: ro.obo
    name: Relation Ontology in obo format
    product_file_size: 84333
    product_url: http://purl.obolibrary.org/obo/ro.obo
    original_source:
      - source: ro
        relation_type: prov:hadPrimarySource
  - category: OntologyProduct
    description: Relation Ontology in obojson format
    format: json
    id: ro.json
    name: Relation Ontology in obojson format
    product_file_size: 114142
    product_url: http://purl.obolibrary.org/obo/ro.json
    original_source:
      - source: ro
        relation_type: prov:hadPrimarySource
  - category: OntologyProduct
    description: Minimal subset intended to work with BFO-classes
    format: owl
    id: ro.core.owl
    name: RO Core relations
    product_file_size: 7819
    product_url: http://purl.obolibrary.org/obo/ro/core.owl
    original_source:
      - source: ro
        relation_type: prov:hadPrimarySource
  - category: OntologyProduct
    description: Axioms defined within RO and to be used in imports for other ontologies
    format: owl
    id: ro.ro-base.owl
    name: RO base ontology
    product_file_size: 97499
    product_url: http://purl.obolibrary.org/obo/ro/ro-base.owl
    original_source:
      - source: ro
        relation_type: prov:hadPrimarySource
  - category: OntologyProduct
    description: For use in ecology and environmental science
    format: owl
    id: ro.subsets.ro-interaction.owl
    name: Interaction relations
    product_file_size: 64252
    product_url: http://purl.obolibrary.org/obo/ro/subsets/ro-interaction.owl
    original_source:
      - source: ro
        relation_type: prov:hadPrimarySource
  - category: OntologyProduct
    description: Ecology subset
    format: owl
    id: ro.subsets.ro-eco.owl
    name: Ecology subset
    product_url: http://purl.obolibrary.org/obo/ro/subsets/ro-eco.owl
    warnings:
      - 'File was not able to be retrieved when checked on 2026-05-04: HTTP 404 error when accessing file'
      - 'File was not able to be retrieved when checked on 2026-05-09: HTTP 404 error when accessing file'
    original_source:
      - source: ro
        relation_type: prov:hadPrimarySource
  - category: OntologyProduct
    description: For use in neuroscience
    format: owl
    id: ro.subsets.ro-neuro.owl
    name: Neuroscience subset
    product_file_size: 5164
    product_url: http://purl.obolibrary.org/obo/ro/subsets/ro-neuro.owl
    original_source:
      - source: ro
        relation_type: prov:hadPrimarySource
  - category: GraphProduct
    description: PheKnowLator graph files, including subsets with and without inverse relations.
    format: owl
    id: pheknowlator.graph
    latest_version: current_build
    name: PheKnowLator graph
    original_source:
      - relation_type: prov:hadPrimarySource
        source: cl
      - relation_type: prov:hadPrimarySource
        source: clo
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: pw
      - relation_type: prov:hadPrimarySource
        source: pr
      - relation_type: prov:hadPrimarySource
        source: ro
      - relation_type: prov:hadPrimarySource
        source: so
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: vo
      - relation_type: prov:hadPrimarySource
        source: bioportal
      - relation_type: prov:hadPrimarySource
        source: clinvar
      - relation_type: prov:hadPrimarySource
        source: ctd
      - relation_type: prov:hadPrimarySource
        source: disgenet
      - relation_type: prov:hadPrimarySource
        source: ensembl
      - relation_type: prov:hadPrimarySource
        source: genemania
      - relation_type: prov:hadPrimarySource
        source: hgnc
      - relation_type: prov:hadPrimarySource
        source: hpa
      - relation_type: prov:hadPrimarySource
        source: ncbigene
      - relation_type: prov:hadPrimarySource
        source: medgen
      - relation_type: prov:hadPrimarySource
        source: reactome
      - relation_type: prov:hadPrimarySource
        source: string
      - relation_type: prov:hadPrimarySource
        source: uniprot
    product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: pheknowlator
    versions:
      - v1.0.0
      - v2.0.0
      - v2.1.0
      - v3.0.2
      - v4.0.0
      - current_build
  - category: OntologyProduct
    description: OWL release of Monochrom Ontology
    format: owl
    id: chr.model.owl
    name: Monochrom Ontology OWL release
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ro
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: ncbitaxon
      - relation_type: prov:hadPrimarySource
        source: iao
      - relation_type: prov:hadPrimarySource
        source: geno
      - relation_type: prov:hadPrimarySource
        source: skos
      - relation_type: prov:hadPrimarySource
        source: gff
    product_file_size: 102365
    product_url: https://raw.githubusercontent.com/monarch-initiative/monochrom/refs/heads/master/chr.owl
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: chr
  - category: OntologyProduct
    description: The latest release of EFO in OWL format
    format: owl
    id: efo.owl
    name: EFO OWL
    original_source:
      - relation_type: prov:hadPrimarySource
        source: bfo
      - relation_type: prov:hadPrimarySource
        source: bto
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: cl
      - relation_type: prov:hadPrimarySource
        source: clo
      - relation_type: prov:hadPrimarySource
        source: cob
      - relation_type: prov:hadPrimarySource
        source: dc
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: ecto
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: fbbt
      - relation_type: prov:hadPrimarySource
        source: fbdv
      - relation_type: prov:hadPrimarySource
        source: fma
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hancestro
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: iao
      - relation_type: prov:hadPrimarySource
        source: ido
      - relation_type: prov:hadPrimarySource
        source: ma
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: mp
      - relation_type: prov:hadPrimarySource
        source: mpath
      - relation_type: prov:hadPrimarySource
        source: ncbitaxon
      - relation_type: prov:hadPrimarySource
        source: ncit
      - relation_type: prov:hadPrimarySource
        source: oba
      - relation_type: prov:hadPrimarySource
        source: obi
      - relation_type: prov:hadPrimarySource
        source: ogms
      - relation_type: prov:hadPrimarySource
        source: oio
      - relation_type: prov:hadPrimarySource
        source: omit
      - relation_type: prov:hadPrimarySource
        source: omo
      - relation_type: prov:hadPrimarySource
        source: ordo
      - relation_type: prov:hadPrimarySource
        source: pato
      - relation_type: prov:hadPrimarySource
        source: po
      - relation_type: prov:hadPrimarySource
        source: pr
      - relation_type: prov:hadPrimarySource
        source: ro
      - relation_type: prov:hadPrimarySource
        source: semapv
      - relation_type: prov:hadPrimarySource
        source: skos
      - relation_type: prov:hadPrimarySource
        source: so
      - relation_type: prov:hadPrimarySource
        source: to
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: uo
      - relation_type: prov:hadPrimarySource
        source: wbls
      - relation_type: prov:hadPrimarySource
        source: zfa
    product_file_size: 240665663
    product_url: https://www.ebi.ac.uk/efo/efo.owl
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: efo
  - category: OntologyProduct
    description: The latest release of EFO in OBO format
    format: obo
    id: efo.obo
    name: EFO OBO
    original_source:
      - relation_type: prov:hadPrimarySource
        source: bfo
      - relation_type: prov:hadPrimarySource
        source: bto
      - relation_type: prov:hadPrimarySource
        source: chebi
      - relation_type: prov:hadPrimarySource
        source: cl
      - relation_type: prov:hadPrimarySource
        source: clo
      - relation_type: prov:hadPrimarySource
        source: cob
      - relation_type: prov:hadPrimarySource
        source: dc
      - relation_type: prov:hadPrimarySource
        source: doid
      - relation_type: prov:hadPrimarySource
        source: ecto
      - relation_type: prov:hadPrimarySource
        source: efo
      - relation_type: prov:hadPrimarySource
        source: fbbt
      - relation_type: prov:hadPrimarySource
        source: fbdv
      - relation_type: prov:hadPrimarySource
        source: fma
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: hancestro
      - relation_type: prov:hadPrimarySource
        source: hp
      - relation_type: prov:hadPrimarySource
        source: iao
      - relation_type: prov:hadPrimarySource
        source: ido
      - relation_type: prov:hadPrimarySource
        source: ma
      - relation_type: prov:hadPrimarySource
        source: mondo
      - relation_type: prov:hadPrimarySource
        source: mp
      - relation_type: prov:hadPrimarySource
        source: mpath
      - relation_type: prov:hadPrimarySource
        source: ncbitaxon
      - relation_type: prov:hadPrimarySource
        source: ncit
      - relation_type: prov:hadPrimarySource
        source: oba
      - relation_type: prov:hadPrimarySource
        source: obi
      - relation_type: prov:hadPrimarySource
        source: ogms
      - relation_type: prov:hadPrimarySource
        source: oio
      - relation_type: prov:hadPrimarySource
        source: omit
      - relation_type: prov:hadPrimarySource
        source: omo
      - relation_type: prov:hadPrimarySource
        source: ordo
      - relation_type: prov:hadPrimarySource
        source: pato
      - relation_type: prov:hadPrimarySource
        source: po
      - relation_type: prov:hadPrimarySource
        source: pr
      - relation_type: prov:hadPrimarySource
        source: ro
      - relation_type: prov:hadPrimarySource
        source: semapv
      - relation_type: prov:hadPrimarySource
        source: skos
      - relation_type: prov:hadPrimarySource
        source: so
      - relation_type: prov:hadPrimarySource
        source: to
      - relation_type: prov:hadPrimarySource
        source: uberon
      - relation_type: prov:hadPrimarySource
        source: uo
      - relation_type: prov:hadPrimarySource
        source: wbls
      - relation_type: prov:hadPrimarySource
        source: zfa
    product_file_size: 64058275
    product_url: https://www.ebi.ac.uk/efo/efo.obo
    secondary_source:
      - relation_type: prov:wasInfluencedBy
        source: efo
publications: []
repository: https://github.com/oborel/obo-relations
---

## Description

Relationship types shared across multiple ontologies

## Contacts

- Chris Mungall (cjmungall@lbl.gov) [ORCID: 0000-0002-6601-2165](https://orcid.org/0000-0002-6601-2165)

## Products

### Relation Ontology

Canonical edition

**URL**: [http://purl.obolibrary.org/obo/ro.owl](http://purl.obolibrary.org/obo/ro.owl)

**Format**: owl

### Relation Ontology in obo format

The obo edition is less expressive than the OWL, and has imports merged in

**URL**: [http://purl.obolibrary.org/obo/ro.obo](http://purl.obolibrary.org/obo/ro.obo)

**Format**: obo

### Relation Ontology in obojson format

Relation Ontology in obojson format

**URL**: [http://purl.obolibrary.org/obo/ro.json](http://purl.obolibrary.org/obo/ro.json)

**Format**: json

### RO Core relations

Minimal subset intended to work with BFO-classes

**URL**: [http://purl.obolibrary.org/obo/ro/core.owl](http://purl.obolibrary.org/obo/ro/core.owl)

**Format**: owl

### RO base ontology

Axioms defined within RO and to be used in imports for other ontologies

**URL**: [http://purl.obolibrary.org/obo/ro/ro-base.owl](http://purl.obolibrary.org/obo/ro/ro-base.owl)

**Format**: owl

### Interaction relations

For use in ecology and environmental science

**URL**: [http://purl.obolibrary.org/obo/ro/subsets/ro-interaction.owl](http://purl.obolibrary.org/obo/ro/subsets/ro-interaction.owl)

**Format**: owl

### Ecology subset

Ecology subset

**URL**: [http://purl.obolibrary.org/obo/ro/subsets/ro-eco.owl](http://purl.obolibrary.org/obo/ro/subsets/ro-eco.owl)

**Format**: owl

### Neuroscience subset

For use in neuroscience

**URL**: [http://purl.obolibrary.org/obo/ro/subsets/ro-neuro.owl](http://purl.obolibrary.org/obo/ro/subsets/ro-neuro.owl)

**Format**: owl

**Domains**: biological systems

---

*This resource was automatically synchronized from the OBO Foundry registry.*
