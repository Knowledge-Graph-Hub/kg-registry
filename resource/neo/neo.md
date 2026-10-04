---
activity_status: active
category: Resource
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: cjmungall@lbl.gov
      - contact_type: github
        value: cmungall
    label: Christopher J. Mungall
    orcid: 0000-0002-6601-2165
description: 'This repository contains classes required by Noctua/Minerva for representing entities that are object of ''enabled by'' relations, and similar molecular relationships. This includes: genes, protein (gene-level generic proteins and isoforms), functional RNAs, and complexes. These are represented as ontology classes, although NEO is not really an ontology in a conventional sense: there is no hierarchy, it is organized as a largely flat list.'
domains:
  - biological systems
  - genomics
  - proteomics
homepage_url: https://github.com/geneontology/neo/
id: neo
layout: resource_detail
name: Noctua Entity Ontology
products:
  - category: OntologyProduct
    description: OWL release of neo
    format: owl
    id: neo.model
    name: neo OWL release
    original_source:
      - source: neo
        relation_type: prov:hadPrimarySource
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: goa
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: sgd
      - relation_type: prov:hadPrimarySource
        source: pombase
      - relation_type: prov:hadPrimarySource
        source: mgi
      - relation_type: prov:hadPrimarySource
        source: zfin
      - relation_type: prov:hadPrimarySource
        source: rgd
      - relation_type: prov:hadPrimarySource
        source: dictybase
      - relation_type: prov:hadPrimarySource
        source: flybase
      - relation_type: prov:hadPrimarySource
        source: tair
      - relation_type: prov:hadPrimarySource
        source: wormbase
      - relation_type: prov:hadPrimarySource
        source: xenbase
      - relation_type: prov:hadPrimarySource
        source: ecocyc
      - relation_type: prov:hadPrimarySource
        source: kg-covid-19
      - relation_type: prov:hadPrimarySource
        source: pr
      - relation_type: prov:hadPrimarySource
        source: rnacentral
    product_file_size: 2142188184
    product_url: http://purl.obolibrary.org/obo/go/noctua/neo.owl
  - category: OntologyProduct
    description: OBO format release of NEO, built from the same weekly GPI-based build as neo.owl.
    format: obo
    id: neo.obo
    name: NEO (OBO format)
    original_source:
      - relation_type: prov:hadPrimarySource
        source: neo
      - relation_type: prov:hadPrimarySource
        source: go
      - relation_type: prov:hadPrimarySource
        source: goa
      - relation_type: prov:hadPrimarySource
        source: uniprot
      - relation_type: prov:hadPrimarySource
        source: sgd
      - relation_type: prov:hadPrimarySource
        source: pombase
      - relation_type: prov:hadPrimarySource
        source: mgi
      - relation_type: prov:hadPrimarySource
        source: zfin
      - relation_type: prov:hadPrimarySource
        source: rgd
      - relation_type: prov:hadPrimarySource
        source: dictybase
      - relation_type: prov:hadPrimarySource
        source: flybase
      - relation_type: prov:hadPrimarySource
        source: tair
      - relation_type: prov:hadPrimarySource
        source: wormbase
      - relation_type: prov:hadPrimarySource
        source: xenbase
      - relation_type: prov:hadPrimarySource
        source: ecocyc
      - relation_type: prov:hadPrimarySource
        source: kg-covid-19
      - relation_type: prov:hadPrimarySource
        source: pr
      - relation_type: prov:hadPrimarySource
        source: rnacentral
    product_file_size: 681668343
    product_url: http://purl.obolibrary.org/obo/go/noctua/neo.obo
repository: https://github.com/geneontology/neo/
creation_date: '2025-03-09T00:00:00Z'
last_modified_date: '2026-10-04T00:00:00Z'
---

Noctua Entity Ontology. Conversion of gene and gene-centric entity IDs from uniprot and MODs.
