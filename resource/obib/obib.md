---
activity_status: active
category: Ontology
collection:
  - obo-foundry
contacts:
  - category: Individual
    label: Justin Whorton
    orcid: 0009-0003-4268-6207
    contact_details:
      - contact_type: email
        value: jmwhorton@uams.edu
      - contact_type: github
        value: jmwhorton
creation_date: '2025-06-04T00:00:00Z'
description: An ontology built for annotation and modeling of biobank repository and biobanking administration
domains:
  - biomedical
homepage_url: https://github.com/biobanking/biobanking
id: obib
last_modified_date: '2026-04-15T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Ontology for Biobanking
products:
  - category: OntologyProduct
    description: Ontology for Biobanking in OWL format
    format: owl
    id: obib.owl
    name: obib.owl
    product_file_size: 230390
    product_url: http://purl.obolibrary.org/obo/obib.owl
  - category: GraphProduct
    description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG instances as neo4j graph databases, running in a Docker container. Requires UMLS API key to access.
    dump_format: neo4j
    id: ubkg.neo4j
    name: UBKG Neo4j Docker Distribution
    original_source:
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: icd10
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: obib
        relation_type: prov:hadPrimarySource
      - source: edam
        relation_type: prov:hadPrimarySource
      - source: hsapdv
        relation_type: prov:hadPrimarySource
      - source: sbo
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: pgo
        relation_type: prov:hadPrimarySource
      - source: gencode
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: hra
        relation_type: prov:hadPrimarySource
      - source: hubmap
        relation_type: prov:hadPrimarySource
      - source: sennet
        relation_type: prov:hadPrimarySource
      - source: stellar
        relation_type: prov:hadPrimarySource
      - source: dct
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: connectivitymap
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: msigdb
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: 4dn
        relation_type: prov:hadPrimarySource
      - source: erccrbp
        relation_type: prov:hadPrimarySource
      - source: erccreg
        relation_type: prov:hadPrimarySource
      - source: faldo
        relation_type: prov:hadPrimarySource
      - source: glycordf
        relation_type: prov:hadPrimarySource
      - source: glycocoo
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: kidsfirst
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: motrpac
        relation_type: prov:hadPrimarySource
      - source: mw
        relation_type: prov:hadPrimarySource
      - source: npo
        relation_type: prov:hadPrimarySource
      - source: sckan
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: biomarker
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - source: ubkg
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Ontology CSV files that can be imported into a neo4j instance to create a UBKG database. Requires UMLS API key to access.
    format: csv
    id: ubkg.csv
    name: UBKG Ontology CSV Files
    original_source:
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: icd10
        relation_type: prov:hadPrimarySource
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: pato
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: doid
        relation_type: prov:hadPrimarySource
      - source: obi
        relation_type: prov:hadPrimarySource
      - source: obib
        relation_type: prov:hadPrimarySource
      - source: edam
        relation_type: prov:hadPrimarySource
      - source: hsapdv
        relation_type: prov:hadPrimarySource
      - source: sbo
        relation_type: prov:hadPrimarySource
      - source: mi
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: ordo
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: uo
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: pgo
        relation_type: prov:hadPrimarySource
      - source: gencode
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: hra
        relation_type: prov:hadPrimarySource
      - source: hubmap
        relation_type: prov:hadPrimarySource
      - source: sennet
        relation_type: prov:hadPrimarySource
      - source: stellar
        relation_type: prov:hadPrimarySource
      - source: dct
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: connectivitymap
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mp
        relation_type: prov:hadPrimarySource
      - source: msigdb
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: 4dn
        relation_type: prov:hadPrimarySource
      - source: erccrbp
        relation_type: prov:hadPrimarySource
      - source: erccreg
        relation_type: prov:hadPrimarySource
      - source: faldo
        relation_type: prov:hadPrimarySource
      - source: glycordf
        relation_type: prov:hadPrimarySource
      - source: glycocoo
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: kidsfirst
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: motrpac
        relation_type: prov:hadPrimarySource
      - source: mw
        relation_type: prov:hadPrimarySource
      - source: npo
        relation_type: prov:hadPrimarySource
      - source: sckan
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: biomarker
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
    product_url: https://ubkg-downloads.xconsortia.org/
    secondary_source:
      - source: ubkg
        relation_type: prov:wasInfluencedBy
repository: https://github.com/biobanking/biobanking
publications: []
---

## Description

An ontology built for annotation and modeling of biobank repository and biobanking administration

## Contacts

- Justin Whorton (jmwhorton@uams.edu) [ORCID: 0009-0003-4268-6207](https://orcid.org/0009-0003-4268-6207)

## Products

### obib.owl

Ontology for Biobanking in OWL format

**URL**: [http://purl.obolibrary.org/obo/obib.owl](http://purl.obolibrary.org/obo/obib.owl)

**Format**: owl

**Domains**: biomedical

---

*This resource was automatically synchronized from the OBO Foundry registry.*
