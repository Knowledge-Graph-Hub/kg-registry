---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: yongqunh@med.umich.edu
  - contact_type: github
    value: yongqunh
  label: Yongqunh He
  orcid: 0000-0001-9189-9661
description: VO is a biomedical ontology in the domain of vaccine and vaccination.
domains:
- biomedical
homepage_url: https://violinet.org/vaccineontology
id: vo
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
  product_url: http://purl.obolibrary.org/obo/vo.owl
- category: GraphProduct
  description: PheKnowLator graph files, including subsets with and without inverse
    relations.
  format: owl
  id: pheknowlator.graph
  latest_version: current_build
  name: PheKnowLator graph
  original_source:
  - cl
  - clo
  - chebi
  - go
  - hp
  - mondo
  - pw
  - pr
  - ro
  - so
  - uberon
  - vo
  - bioportal
  - clinvar
  - ctd
  - disgenet
  - ensembl
  - genemania
  - hgnc
  - hpa
  - ncbigene
  - medgen
  - reactome
  - string
  - uniprot
  product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
  secondary_source:
  - pheknowlator
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
  - dbsnp
  - cosmic
  - rnacentral
  - ensembl
  - circbase
  - chebi
  - pr
  - ncbigene
  - cl
  - go
  - mondo
  - hp
  - uberon
  - vo
  - pw
  - reactome
  - wikipathways
  product_file_size: 3976840239
  product_url: https://rna-kg.biodata.di.unimi.it/rnakgv20.dump
  secondary_source:
  - rna-kg
- category: GraphProduct
  description: RNA-KG Nodes in CSV format
  format: csv
  id: rna-kg.kg.nodes
  name: RNA-KG Nodes
  original_source:
  - dbsnp
  - cosmic
  - rnacentral
  - ensembl
  - circbase
  - chebi
  - pr
  - ncbigene
  - cl
  - go
  - mondo
  - hp
  - uberon
  - vo
  - pw
  - reactome
  - wikipathways
  product_file_size: 4424633304
  product_url: https://rna-kg.biodata.di.unimi.it/nodes.csv
  secondary_source:
  - rna-kg
- category: GraphProduct
  description: RNA-KG Edges in CSV format
  format: csv
  id: rna-kg.kg.edges
  name: RNA-KG Edges
  original_source:
  - dbsnp
  - cosmic
  - rnacentral
  - ensembl
  - circbase
  - chebi
  - pr
  - ncbigene
  - cl
  - go
  - mondo
  - hp
  - uberon
  - vo
  - pw
  - reactome
  - wikipathways
  product_file_size: 18370248815
  product_url: https://rna-kg.biodata.di.unimi.it/edges.csv
  secondary_source:
  - rna-kg
repository: https://github.com/vaccineontology/VO
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