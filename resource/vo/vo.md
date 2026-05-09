---
activity_status: active
category: Ontology
collection:
  - obo-foundry
contacts:
  - category: Individual
    label: Yongqunh He
    orcid: 0000-0001-9189-9661
    contact_details:
      - contact_type: email
        value: yongqunh@med.umich.edu
      - contact_type: github
        value: yongqunh
creation_date: '2025-08-20T00:00:00Z'
description: VO is a biomedical ontology in the domain of vaccine and vaccination.
domains:
  - biomedical
homepage_url: https://violinet.org/vaccineontology
id: vo
last_modified_date: '2026-04-15T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Vaccine Ontology
products:
  - category: OntologyProduct
    description: Vaccine Ontology in OWL format
    format: owl
    id: vo.owl
    name: vo.owl
    product_file_size: 1492352
    product_url: http://purl.obolibrary.org/obo/vo.owl
    original_source:
      - source: vo
        relation_type: prov:hadPrimarySource
  - category: GraphProduct
    description: PheKnowLator graph files, including subsets with and without inverse relations.
    format: owl
    id: pheknowlator.graph
    latest_version: current_build
    name: PheKnowLator graph
    original_source:
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: clo
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: pw
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: ro
        relation_type: prov:hadPrimarySource
      - source: so
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: vo
        relation_type: prov:hadPrimarySource
      - source: bioportal
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: genemania
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
    secondary_source:
      - source: pheknowlator
        relation_type: prov:wasInfluencedBy
    versions:
      - v1.0.0
      - v2.0.0
      - v2.1.0
      - v3.0.2
      - v4.0.0
      - current_build
  - category: GraphProduct
    description: RNA-KG as a Neo4j Dump
    format: neo4j
    id: rna-kg.kg.neo4j
    name: RNA-KG Neo4j Dump
    original_source:
      - source: dbsnp
        relation_type: prov:hadPrimarySource
      - source: cosmic
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: circbase
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: vo
        relation_type: prov:hadPrimarySource
      - source: pw
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
    product_file_size: 3976840239
    product_url: https://rna-kg.biodata.di.unimi.it/rnakgv20.dump
    secondary_source:
      - source: rna-kg
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: RNA-KG Nodes in CSV format
    format: csv
    id: rna-kg.kg.nodes
    name: RNA-KG Nodes
    original_source:
      - source: dbsnp
        relation_type: prov:hadPrimarySource
      - source: cosmic
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: circbase
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: vo
        relation_type: prov:hadPrimarySource
      - source: pw
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
    product_file_size: 4424633304
    product_url: https://rna-kg.biodata.di.unimi.it/nodes.csv
    secondary_source:
      - source: rna-kg
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: RNA-KG Edges in CSV format
    format: csv
    id: rna-kg.kg.edges
    name: RNA-KG Edges
    original_source:
      - source: dbsnp
        relation_type: prov:hadPrimarySource
      - source: cosmic
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: circbase
        relation_type: prov:hadPrimarySource
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: pr
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: cl
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: uberon
        relation_type: prov:hadPrimarySource
      - source: vo
        relation_type: prov:hadPrimarySource
      - source: pw
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
    product_file_size: 18370248815
    product_url: https://rna-kg.biodata.di.unimi.it/edges.csv
    secondary_source:
      - source: rna-kg
        relation_type: prov:wasInfluencedBy
repository: https://github.com/vaccineontology/VO
publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/23256535
    title: Ontology representation and analysis of vaccine formulation and administration and their effects on vaccine immune responses
  - id: https://www.ncbi.nlm.nih.gov/pubmed/21624163
    title: Mining of vaccine-associated IFN-  gene interaction networks using the Vaccine Ontology
---

## Description

VO is a biomedical ontology in the domain of vaccine and vaccination.

## Contacts

- Yongqunh He (yongqunh@med.umich.edu) [ORCID: 0000-0001-9189-9661](https://orcid.org/0000-0001-9189-9661)

## Products

### vo.owl

Vaccine Ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/vo.owl](http://purl.obolibrary.org/obo/vo.owl)

**Format**: owl

## Publications

- [Ontology representation and analysis of vaccine formulation and administration and their effects on vaccine immune responses](https://www.ncbi.nlm.nih.gov/pubmed/23256535)
- [Mining of vaccine-associated IFN-  gene interaction networks using the Vaccine Ontology](https://www.ncbi.nlm.nih.gov/pubmed/21624163)

**Domains**: biomedical

---

*This resource was automatically synchronized from the OBO Foundry registry.*
