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
creation_date: '2025-06-04T00:00:00Z'
description: Standard terms for annotating mammalian phenotypic data.
domains:
- biological systems
homepage_url: https://www.informatics.jax.org/vocab/mp_ontology/
id: mp
infores_id: mp
last_modified_date: '2026-04-15T00:00:00Z'
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
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mp
  product_file_size: 103265062
  product_url: http://purl.obolibrary.org/obo/mp.owl
- category: OntologyProduct
  description: A direct translation of the MP (OWL edition) into OBO format.
  format: obo
  id: mp.obo
  name: MP (OBO edition)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mp
  product_url: http://purl.obolibrary.org/obo/mp.obo
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-26: No Content-Length
    header found'
- category: OntologyProduct
  description: For a description of the format see https://github.com/geneontology/obographs.
  format: json
  id: mp.json
  name: MP (obographs JSON edition)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mp
  product_file_size: 55018989
  product_url: http://purl.obolibrary.org/obo/mp.json
- category: OntologyProduct
  description: The main ontology plus axioms connecting to select external ontologies,
    excluding axioms from the the external ontologies themselves.
  format: owl
  id: mp.mp-base.owl
  name: MP Base Module
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mp
  product_file_size: 50597438
  product_url: http://purl.obolibrary.org/obo/mp/mp-base.owl
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
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
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/40963406
  title: Expanding and refining the Mammalian Phenotype Ontology to enhance disease
    model discovery
- id: https://www.ncbi.nlm.nih.gov/pubmed/22961259
  title: The Mammalian Phenotype Ontology as a unifying standard for experimental
    and high-throughput phenotyping data
- id: https://www.ncbi.nlm.nih.gov/pubmed/25825651
  title: Expanding the mammalian phenotype ontology to support automated exchange
    of high throughput mouse phenotyping data generated by large-scale mouse knockout
    screens
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

- [Expanding and refining the Mammalian Phenotype Ontology to enhance disease model discovery](https://www.ncbi.nlm.nih.gov/pubmed/40963406)
- [The Mammalian Phenotype Ontology as a unifying standard for experimental and high-throughput phenotyping data](https://www.ncbi.nlm.nih.gov/pubmed/22961259)
- [Expanding the mammalian phenotype ontology to support automated exchange of high throughput mouse phenotyping data generated by large-scale mouse knockout screens](https://www.ncbi.nlm.nih.gov/pubmed/25825651)

**Domains**: biological systems

**Taxon**: NCBITaxon:40674

---

*This resource was automatically synchronized from the OBO Foundry registry.*