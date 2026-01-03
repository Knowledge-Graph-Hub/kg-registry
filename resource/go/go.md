---
id: go
name: Gene Ontology
description: An ontology for describing the function of genes and gene products
activity_status: active
homepage_url: http://geneontology.org/
repository: https://github.com/geneontology/go-ontology
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
collection:
- obo-foundry
layout: resource_detail
category: Ontology
domains:
- biological systems
taxon:
- NCBITaxon:1
contacts:
- category: Individual
  label: Suzi Aleksander
  orcid: 0000-0001-6787-2901
  contact_details:
  - contact_type: email
    value: suzia@stanford.edu
  - contact_type: github
    value: suzialeksander
products:
- id: go.owl
  name: GO (OWL edition)
  description: The main ontology in OWL. This is self contained and does not have
    connections to other OBO ontologies
  format: owl
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/go.owl
- id: go.obo
  name: GO (OBO Format edition)
  description: Equivalent to go.owl, in obo format
  format: obo
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/go.obo
- id: go.json
  name: GO (JSON edition)
  description: Equivalent to go.owl, in obograph json format
  format: json
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/go.json
- id: go.extensions.go-plus.owl
  name: GO-Plus
  description: The main ontology plus axioms connecting to select external ontologies,
    with subsets of those ontologies
  format: owl
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-plus.owl
- id: go.go-base.owl
  name: GO Base Module
  description: The main ontology plus axioms connecting to select external ontologies,
    excluding the external ontologies themselves
  format: owl
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/go/go-base.owl
- id: go.extensions.go-plus.json
  name: GO-Plus
  description: As go-plus.owl, in obographs json format
  format: json
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-plus.json
- id: go.go-basic.obo
  name: GO-Basic, Filtered, for use with legacy tools
  description: Basic version of the GO, filtered such that the graph is guaranteed
    to be acyclic and annotations can be propagated up the graph. The relations included
    are is a, part of, regulates, negatively regulates and positively regulates. This
    version excludes relationships that cross the 3 GO hierarchies.
  format: obo
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/go/go-basic.obo
- id: go.go-basic.json
  name: GO-Basic, Filtered, for use with legacy tools (JSON)
  description: As go-basic.obo, in json format
  format: json
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/go/go-basic.json
- id: go.extensions.go-taxon-groupings.owl
  name: GO Taxon Groupings
  description: Classes added to ncbitaxon for groupings such as prokaryotes
  format: owl
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/go/extensions/go-taxon-groupings.owl
- id: go.snapshot.go.owl
  name: GO (OWL edition), daily snapshot release
  description: Equivalent to go.owl, but released daily. Note the snapshot release
    is not archived.
  format: owl
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/go/snapshot/go.owl
- id: go.snapshot.go.obo
  name: GO (OBO Format edition), daily snapshot release
  description: Equivalent to go.owl, but released daily. Note the snapshot release
    is not archived.
  format: obo
  category: OntologyProduct
  product_url: http://purl.obolibrary.org/obo/go/snapshot/go.obo
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
