---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: suzia@stanford.edu
  - contact_type: github
    value: suzialeksander
  label: Suzi Aleksander
  orcid: 0000-0001-6787-2901
creation_date: '2025-03-16T00:00:00Z'
description: An ontology for describing the function of genes and gene products
domains:
- biological systems
homepage_url: http://geneontology.org/
id: go
infores_id: go
last_modified_date: '2026-02-24T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Gene Ontology
products:
- category: OntologyProduct
  description: The main ontology in OWL. This is self contained and does not have
    connections to other OBO ontologies
  format: owl
  id: go.owl
  name: GO (OWL edition)
  product_file_size: 129057533
  product_url: http://purl.obolibrary.org/obo/go.owl
- category: OntologyProduct
  description: Equivalent to go.owl, in obo format
  format: obo
  id: go.obo
  name: GO (OBO Format edition)
  product_file_size: 36289217
  product_url: http://purl.obolibrary.org/obo/go.obo
- category: OntologyProduct
  description: Equivalent to go.owl, in obograph json format
  format: json
  id: go.json
  name: GO (JSON edition)
  product_url: http://purl.obolibrary.org/obo/go.json
  warnings:
  - 'File was not able to be retrieved when checked on 2026-03-30: No Content-Length
    header found'
- category: OntologyProduct
  description: The main ontology plus axioms connecting to select external ontologies,
    with subsets of those ontologies
  format: owl
  id: go.extensions.go-plus.owl
  name: GO-Plus
  product_file_size: 235714202
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-plus.owl
- category: OntologyProduct
  description: The main ontology plus axioms connecting to select external ontologies,
    excluding the external ontologies themselves
  format: owl
  id: go.go-base.owl
  name: GO Base Module
  product_file_size: 160299649
  product_url: http://purl.obolibrary.org/obo/go/go-base.owl
- category: OntologyProduct
  description: As go-plus.owl, in obographs json format
  format: json
  id: go.extensions.go-plus.json
  name: GO-Plus
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-plus.json
  warnings:
  - 'File was not able to be retrieved when checked on 2026-03-30: No Content-Length
    header found'
- category: OntologyProduct
  description: Basic version of the GO, filtered such that the graph is guaranteed
    to be acyclic and annotations can be propagated up the graph. The relations included
    are is a, part of, regulates, negatively regulates and positively regulates. This
    version excludes relationships that cross the 3 GO hierarchies.
  format: obo
  id: go.go-basic.obo
  name: GO-Basic, Filtered, for use with legacy tools
  product_file_size: 31933366
  product_url: http://purl.obolibrary.org/obo/go/go-basic.obo
- category: OntologyProduct
  description: As go-basic.obo, in json format
  format: json
  id: go.go-basic.json
  name: GO-Basic, Filtered, for use with legacy tools (JSON)
  product_url: http://purl.obolibrary.org/obo/go/go-basic.json
  warnings:
  - 'File was not able to be retrieved when checked on 2026-03-30: No Content-Length
    header found'
- category: OntologyProduct
  description: Classes added to ncbitaxon for groupings such as prokaryotes
  format: owl
  id: go.extensions.go-taxon-groupings.owl
  name: GO Taxon Groupings
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-taxon-groupings.owl
  warnings:
  - 'File was not able to be retrieved when checked on 2026-03-30: HTTP 403 error
    when accessing file'
- category: OntologyProduct
  description: Equivalent to go.owl, but released daily. Note the snapshot release
    is not archived.
  format: owl
  id: go.snapshot.go.owl
  name: GO (OWL edition), daily snapshot release
  product_file_size: 129706298
  product_url: http://purl.obolibrary.org/obo/go/snapshot/go.owl
- category: OntologyProduct
  description: Equivalent to go.owl, but released daily. Note the snapshot release
    is not archived.
  format: obo
  id: go.snapshot.go.obo
  name: GO (OBO Format edition), daily snapshot release
  product_file_size: 36555702
  product_url: http://purl.obolibrary.org/obo/go/snapshot/go.obo
repository: https://github.com/geneontology/go-ontology
taxon:
- NCBITaxon:1
---
## Description

An ontology for describing the function of genes and gene products

## Contacts

- Suzi Aleksander (suzia@stanford.edu) [ORCID: 0000-0001-6787-2901](https://orcid.org/0000-0001-6787-2901)

## Products

### GO (OWL edition)

The main ontology in OWL. This is self contained and does not have connections to other OBO ontologies

**URL**: [http://purl.obolibrary.org/obo/go.owl](http://purl.obolibrary.org/obo/go.owl)

**Format**: owl

### GO (OBO Format edition)

Equivalent to go.owl, in obo format

**URL**: [http://purl.obolibrary.org/obo/go.obo](http://purl.obolibrary.org/obo/go.obo)

**Format**: obo

### GO (JSON edition)

Equivalent to go.owl, in obograph json format

**URL**: [http://purl.obolibrary.org/obo/go.json](http://purl.obolibrary.org/obo/go.json)

**Format**: json

### GO-Plus

The main ontology plus axioms connecting to select external ontologies, with subsets of those ontologies

**URL**: [http://purl.obolibrary.org/obo/go/extensions/go-plus.owl](http://purl.obolibrary.org/obo/go/extensions/go-plus.owl)

**Format**: owl

### GO Base Module

The main ontology plus axioms connecting to select external ontologies, excluding the external ontologies themselves

**URL**: [http://purl.obolibrary.org/obo/go/go-base.owl](http://purl.obolibrary.org/obo/go/go-base.owl)

**Format**: owl

### GO-Plus

As go-plus.owl, in obographs json format

**URL**: [http://purl.obolibrary.org/obo/go/extensions/go-plus.json](http://purl.obolibrary.org/obo/go/extensions/go-plus.json)

**Format**: json

### GO-Basic, Filtered, for use with legacy tools

Basic version of the GO, filtered such that the graph is guaranteed to be acyclic and annotations can be propagated up the graph. The relations included are is a, part of, regulates, negatively regulates and positively regulates. This version excludes relationships that cross the 3 GO hierarchies.

**URL**: [http://purl.obolibrary.org/obo/go/go-basic.obo](http://purl.obolibrary.org/obo/go/go-basic.obo)

**Format**: obo

### GO-Basic, Filtered, for use with legacy tools (JSON)

As go-basic.obo, in json format

**URL**: [http://purl.obolibrary.org/obo/go/go-basic.json](http://purl.obolibrary.org/obo/go/go-basic.json)

**Format**: json

### GO Taxon Groupings

Classes added to ncbitaxon for groupings such as prokaryotes

**URL**: [http://purl.obolibrary.org/obo/go/extensions/go-taxon-groupings.owl](http://purl.obolibrary.org/obo/go/extensions/go-taxon-groupings.owl)

**Format**: owl

### GO (OWL edition), daily snapshot release

Equivalent to go.owl, but released daily. Note the snapshot release is not archived.

**URL**: [http://purl.obolibrary.org/obo/go/snapshot/go.owl](http://purl.obolibrary.org/obo/go/snapshot/go.owl)

**Format**: owl

### GO (OBO Format edition), daily snapshot release

Equivalent to go.owl, but released daily. Note the snapshot release is not archived.

**URL**: [http://purl.obolibrary.org/obo/go/snapshot/go.obo](http://purl.obolibrary.org/obo/go/snapshot/go.obo)

**Format**: obo

## Publications

- [Gene ontology: tool for the unification of biology. The Gene Ontology Consortium](https://www.ncbi.nlm.nih.gov/pubmed/10802651)
- [The Gene Ontology resource: enriching a GOld mine](https://www.ncbi.nlm.nih.gov/pubmed/33290552)

**Domains**: biological systems

**Taxon**: NCBITaxon:1

---

*This resource was automatically synchronized from the OBO Foundry registry.*