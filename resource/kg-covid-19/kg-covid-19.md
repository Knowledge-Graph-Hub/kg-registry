---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: justaddcoffee
  label: Justin Reese
creation_date: '2025-03-09T00:00:00Z'
description: A knowledge graph for COVID-19 and SARS-COV-2.
domains:
- organisms
- biomedical
- microbiology
- public health
- infectious disease
homepage_url: https://github.com/Knowledge-Graph-Hub/kg-covid-19/wiki
id: kg-covid-19
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/license/bsd-3-clause
  label: BSD3
name: KG-COVID-19
products:
- category: GraphProduct
  description: KGX nodes and edges for KG-COVID-19
  format: kgx
  id: kg-covid-19.graph
  name: KG-COVID-19 graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-covid-19
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cord-19
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://kghub.io/kg-covid-19/
  warnings:
  - 'Download offline as of 2026-07-01: the KG-Hub reorganization has taken this file
    offline. The kghub.io and kg-hub.berkeleybop.io hosts return HTTP 404 for all
    kg-covid-19 artifacts (current and dated) and the kg-hub-public-data S3 objects
    return HTTP 403. No replacement public download URL is available.'
  - 'File was not able to be retrieved when checked on 2026-10-05: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-10-10: HTTP 404 error
    when accessing file'
- category: OntologyProduct
  description: OWL release of neo
  format: owl
  id: neo.model
  name: neo OWL release
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
  product_file_size: 2142188184
  product_url: http://purl.obolibrary.org/obo/go/noctua/neo.owl
- category: OntologyProduct
  description: OBO format release of NEO, built from the same weekly GPI-based build
    as neo.owl.
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
repository: https://github.com/Knowledge-Graph-Hub/kg-covid-19
---
KG-COVID-19: a knowledge graph for COVID-19 and SARS-COV-2.

## Automated Evaluation

- View the automated evaluation: [kg-covid-19 automated evaluation](kg-covid-19_eval_automated.html)