---
activity_status: active
category: Ontology
collection:
- obo-foundry
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: gthayman@mcw.edu
  - contact_type: github
    value: gthayman
  label: G. Thomas Hayman
  orcid: 0000-0002-9553-7227
creation_date: '2025-08-20T00:00:00Z'
description: A controlled vocabulary for annotating gene products to pathways.
domains:
- biological systems
homepage_url: http://rgd.mcw.edu/rgdweb/ontology/search.html
id: pw
last_modified_date: '2026-04-15T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Pathway ontology
products:
- category: OntologyProduct
  description: Pathway ontology in OWL format
  format: owl
  id: pw.owl
  name: pw.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pw
  product_file_size: 5404760
  product_url: http://purl.obolibrary.org/obo/pw.owl
- category: OntologyProduct
  description: Pathway ontology in OBO format
  format: obo
  id: pw.obo
  name: pw.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pw
  product_file_size: 1347597
  product_url: http://purl.obolibrary.org/obo/pw.obo
- category: GraphProduct
  description: PheKnowLator graph files, including subsets with and without inverse
    relations.
  format: owl
  id: pheknowlator.graph
  latest_version: current_build
  name: PheKnowLator graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioportal
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: genemania
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pheknowlator
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vo
  product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
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
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: circbase
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rna-kg
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_file_size: 3976840239
  product_url: https://rna-kg.biodata.di.unimi.it/rnakgv20.dump
- category: GraphProduct
  description: RNA-KG Nodes in CSV format
  format: csv
  id: rna-kg.kg.nodes
  name: RNA-KG Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: circbase
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rna-kg
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_file_size: 4424633304
  product_url: https://rna-kg.biodata.di.unimi.it/nodes.csv
- category: GraphProduct
  description: RNA-KG Edges in CSV format
  format: csv
  id: rna-kg.kg.edges
  name: RNA-KG Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: circbase
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: pw
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rna-kg
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: vo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_file_size: 18370248815
  product_url: https://rna-kg.biodata.di.unimi.it/edges.csv
publications:
- authors:
  - Petri V
  - Shimoyama M
  - Hayman GT
  - Smith JR
  - Tutaj M
  - de Pons J
  - Dwinell MR
  - Munzenmaier DH
  - Twigger SN
  - Jacob HJ
  - RGD Team
  doi: 10.1093/database/bar010
  id: https://www.ncbi.nlm.nih.gov/pubmed/21478484
  journal: Database (Oxford)
  title: The Rat Genome Database pathway portal.
  year: '2011'
- authors:
  - Petri V
  - Jayaraman P
  - Tutaj M
  - Hayman GT
  - Smith JR
  - De Pons J
  - Laulederkind SJ
  - Lowry TF
  - Nigam R
  - Wang SJ
  - Shimoyama M
  - Dwinell MR
  - Munzenmaier DH
  - Worthey EA
  - Jacob HJ
  doi: 10.1186/2041-1480-5-7
  id: https://www.ncbi.nlm.nih.gov/pubmed/24499703
  journal: J Biomed Semantics
  title: The pathway ontology - updates and applications.
  year: '2014'
repository: https://github.com/rat-genome-database/PW-Pathway-Ontology
---
## Description

A controlled vocabulary for annotating gene products to pathways.

## Contacts

- G. Thomas Hayman (gthayman@mcw.edu) [ORCID: 0000-0002-9553-7227](https://orcid.org/0000-0002-9553-7227)

## Products

### pw.owl

Pathway ontology in OWL format

**URL**: [http://purl.obolibrary.org/obo/pw.owl](http://purl.obolibrary.org/obo/pw.owl)

**Format**: owl

### pw.obo

Pathway ontology in OBO format

**URL**: [http://purl.obolibrary.org/obo/pw.obo](http://purl.obolibrary.org/obo/pw.obo)

**Format**: obo

## Publications

- [The Rat Genome Database pathway portal.](https://www.ncbi.nlm.nih.gov/pubmed/21478484)
- [The pathway ontology - updates and applications.](https://www.ncbi.nlm.nih.gov/pubmed/24499703)

**Domains**: biological systems

---

*This resource was automatically synchronized from the OBO Foundry registry.*