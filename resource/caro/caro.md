---
activity_status: inactive
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: haendel@ohsu.edu
  - contact_type: github
    value: mellybelly
  label: Melissa Haendel
  orcid: 0000-0001-9114-8737
creation_date: '2025-09-29T00:00:00Z'
description: An upper level ontology to facilitate interoperability between existing
  anatomy ontologies for different species
domains:
- anatomy and development
homepage_url: https://github.com/obophenotype/caro/
id: caro
last_modified_date: '2026-08-06T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Common Anatomy Reference Ontology
products:
- category: OntologyProduct
  description: Common Anatomy Reference Ontology in OWL format
  format: owl
  id: caro.owl
  name: caro.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: caro
  product_file_size: 586722
  product_url: http://purl.obolibrary.org/obo/caro.owl
- category: GraphProduct
  compression: targz
  description: KGX TSV transform of Common Anatomy Reference Ontology (CARO), produced
    by KG-Bioportal from the BioPortal submission. The archive contains CARO_nodes.tsv
    and CARO_edges.tsv.
  edge_count: 10155
  format: kgx
  id: caro.kg-bioportal
  latest_version: '2023-03-15'
  name: CARO KGX graph (KG-Bioportal)
  node_count: 8891
  original_source:
  - relation_type: prov:hadPrimarySource
    source: caro
  product_file_size: 313461
  product_url: https://github.com/ncbo/kg-bioportal/releases/download/data-2026.07/CARO.tar.gz
- category: OntologyProduct
  description: Ontology for the Anatomy of the Insect SkeletoMuscular system (AISM)
    in OWL format
  format: owl
  id: aism.owl
  name: aism.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aism
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 1378303
  product_url: http://purl.obolibrary.org/obo/aism.owl
- category: OntologyProduct
  description: Ontology for the Anatomy of the Insect SkeletoMuscular system (AISM)
    in OBO format
  format: obo
  id: aism.obo
  name: aism.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aism
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 896550
  product_url: http://purl.obolibrary.org/obo/aism.obo
- category: OntologyProduct
  description: Ontology for the Anatomy of the Insect SkeletoMuscular system (AISM)
    in JSON format
  format: json
  id: aism.json
  name: aism.json
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aism
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 929390
  product_url: http://purl.obolibrary.org/obo/aism.json
- category: OntologyProduct
  description: Coleoptera Anatomy Ontology (COLAO) in OWL format
  format: owl
  id: colao.owl
  name: colao.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: colao
  - relation_type: prov:hadPrimarySource
    source: aism
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 164547
  product_url: http://purl.obolibrary.org/obo/colao.owl
- category: OntologyProduct
  description: Coleoptera Anatomy Ontology (COLAO) in OBO format
  format: obo
  id: colao.obo
  name: colao.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: colao
  - relation_type: prov:hadPrimarySource
    source: aism
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 83585
  product_url: http://purl.obolibrary.org/obo/colao.obo
- category: OntologyProduct
  description: Human developmental anatomy, abstract in OWL format
  format: owl
  id: ehdaa2.owl
  name: ehdaa2.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ehdaa2
  - relation_type: prov:hadPrimarySource
    source: aeo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: cl
  product_file_size: 125946
  product_url: http://purl.obolibrary.org/obo/ehdaa2.owl
- category: OntologyProduct
  description: Human developmental anatomy, abstract in OBO format
  format: obo
  id: ehdaa2.obo
  name: ehdaa2.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ehdaa2
  - relation_type: prov:hadPrimarySource
    source: aeo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: cl
  product_file_size: 83809
  product_url: http://purl.obolibrary.org/obo/ehdaa2.obo
- category: OntologyProduct
  description: Plant Gall Ontology in OWL format
  format: owl
  id: gallont.owl
  name: gallont.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gallont
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: flopo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: poro
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 91521
  product_url: http://purl.obolibrary.org/obo/gallont.owl
- category: OntologyProduct
  description: Plant Gall Ontology in OBO format
  format: obo
  id: gallont.obo
  name: gallont.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gallont
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: flopo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: poro
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 60631
  product_url: http://purl.obolibrary.org/obo/gallont.obo
- category: OntologyProduct
  description: Lepidoptera Anatomy Ontology in OWL format
  format: owl
  id: lepao.owl
  name: lepao.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lepao
  - relation_type: prov:hadPrimarySource
    source: aism
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 141799
  product_url: http://purl.obolibrary.org/obo/lepao.owl
- category: OntologyProduct
  description: Lepidoptera Anatomy Ontology in OBO format
  format: obo
  id: lepao.obo
  name: lepao.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lepao
  - relation_type: prov:hadPrimarySource
    source: aism
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: uberon
  product_file_size: 74809
  product_url: http://purl.obolibrary.org/obo/lepao.obo
- category: OntologyProduct
  description: Population and Community Ontology in OWL format
  format: owl
  id: pco.owl
  name: pco.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pco
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: caro
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: iao
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: ro
  product_file_size: 62282
  product_url: http://purl.obolibrary.org/obo/pco.owl
publications: []
repository: https://github.com/obophenotype/caro
---
## Description

An upper level ontology to facilitate interoperability between existing anatomy ontologies for different species

## Contacts

- Melissa Haendel (haendel@ohsu.edu) [ORCID: 0000-0001-9114-8737](https://orcid.org/0000-0001-9114-8737)

## Products

### caro.owl

Common Anatomy Reference Ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/caro.owl](http://purl.obolibrary.org/obo/caro.owl)

**Format**: owl

**Domains**: anatomy and development

---

*This resource was automatically synchronized from the OBO Foundry registry.*