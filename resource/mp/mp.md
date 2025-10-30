---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: pheno@jax.org
  - contact_type: github
    value: sbello
  label: Sue Bello
  orcid: 0000-0003-4606-0597
description: Standard terms for annotating mammalian phenotypic data.
domains:
- biological systems
homepage_url: https://www.informatics.jax.org/vocab/mp_ontology/
id: mp
infores_id: mp
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Mammalian Phenotype Ontology
products:
- category: OntologyProduct
  description: The main ontology in OWL. Contains all MP terms and links to other
    OBO ontologies.
  format: owl
  id: mp.owl
  name: MP (OWL edition)
  product_file_size: 114430024
  product_url: http://purl.obolibrary.org/obo/mp.owl
- category: OntologyProduct
  description: A direct translation of the MP (OWL edition) into OBO format.
  format: obo
  id: mp.obo
  name: MP (OBO edition)
  product_url: http://purl.obolibrary.org/obo/mp.obo
  warnings:
  - 'File was not able to be retrieved when checked on 2025-10-30: No Content-Length
    header found'
- category: OntologyProduct
  description: For a description of the format see https://github.com/geneontology/obographs.
  format: json
  id: mp.json
  name: MP (obographs JSON edition)
  product_file_size: 59988123
  product_url: http://purl.obolibrary.org/obo/mp.json
- category: OntologyProduct
  description: The main ontology plus axioms connecting to select external ontologies,
    excluding axioms from the the external ontologies themselves.
  format: owl
  id: mp.mp-base.owl
  name: MP Base Module
  product_file_size: 49905597
  product_url: http://purl.obolibrary.org/obo/mp/mp-base.owl
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
  - doid
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
  - connectivitymap
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
  - sckan
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
  - doid
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
  - connectivitymap
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
  - sckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: OntologyProduct
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
  - doid
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
- category: OntologyProduct
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
  - doid
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
repository: https://github.com/mgijax/mammalian-phenotype-ontology
taxon:
- NCBITaxon:40674
---
## Description

Standard terms for annotating mammalian phenotypic data.

## Contacts

- Sue Bello (pheno@jax.org) [ORCID: 0000-0003-4606-0597](https://orcid.org/0000-0003-4606-0597)

## Products

### MP (OWL edition)

The main ontology in OWL. Contains all MP terms and links to other OBO ontologies.

**URL**: [http://purl.obolibrary.org/obo/mp.owl](http://purl.obolibrary.org/obo/mp.owl)

**Format**: owl

### MP (OBO edition)

A direct translation of the MP (OWL edition) into OBO format.

**URL**: [http://purl.obolibrary.org/obo/mp.obo](http://purl.obolibrary.org/obo/mp.obo)

**Format**: obo

### MP (obographs JSON edition)

For a description of the format see https://github.com/geneontology/obographs.

**URL**: [http://purl.obolibrary.org/obo/mp.json](http://purl.obolibrary.org/obo/mp.json)

**Format**: json

### MP Base Module

The main ontology plus axioms connecting to select external ontologies, excluding axioms from the the external ontologies themselves.

**URL**: [http://purl.obolibrary.org/obo/mp/mp-base.owl](http://purl.obolibrary.org/obo/mp/mp-base.owl)

**Format**: owl

## Publications

- [The Mammalian Phenotype Ontology as a unifying standard for experimental and high-throughput phenotyping data](https://www.ncbi.nlm.nih.gov/pubmed/22961259)

**Domains**: biological systems

**Taxon**: NCBITaxon:40674

---

*This resource was automatically synchronized from the OBO Foundry registry.*