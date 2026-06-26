---
activity_status: active
category: DataSource
collection:
- ber
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.maizegdb.org
  label: USDA-ARS MaizeGDB
creation_date: '2026-06-18T00:00:00Z'
description: MaizeGDB is the community database for maize (Zea mays) genetics and
  genomics, maintained by the USDA-ARS. It integrates genome assemblies and gene models
  for B73 and an expanding set of maize and related Andropogoneae lines, along with
  gene function and expression data, genetic and physical maps, phenotypes, stocks,
  metabolic pathways, and curated literature. The resource provides genome browsers,
  a MaizeMine data-mining interface, and bulk downloads of sequence and annotation
  files, and serves as the upstream data source for eco-KG.
domains:
- genomics
- organisms
- agriculture
homepage_url: https://www.maizegdb.org
id: maizegdb
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: MaizeGDB
products:
- category: DataProduct
  description: Bulk download server hosting maize and Andropogoneae genome assemblies,
    gene models (GFF, CDS, protein, genomic sequence), transposable element annotations,
    and other genomics datasets.
  id: maizegdb.downloads
  name: MaizeGDB Download Server
  original_source:
  - relation_type: prov:hadPrimarySource
    source: maizegdb
  product_url: https://download.maizegdb.org/
- category: DataProduct
  description: Gene model annotation files in GFF format for maize genome assemblies
    hosted on the MaizeGDB download server.
  id: maizegdb.gene_model_gff
  name: MaizeGDB Gene Model GFF Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: maizegdb
  product_url: https://download.maizegdb.org/All_gene_model_GFF/
- category: DataProduct
  description: MaizeMine data warehouse downloads providing integrated and queryable
    maize genomics datasets.
  id: maizegdb.maizemine
  name: MaizeMine Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: maizegdb
  product_url: https://download.maizegdb.org/MaizeMine/
- category: GraphProduct
  compression: tar
  description: Knowledge graph containing plant traits data from Planteome and EOL
    TraitBank
  format: kgx
  id: eco-kg.graph
  name: eco-KG Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eco-kg
  - relation_type: prov:hadPrimarySource
    source: eol-traitbank
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: to
  - relation_type: prov:hadPrimarySource
    source: po
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: maizegdb
  - relation_type: prov:hadPrimarySource
    source: planteome
  - relation_type: prov:hadPrimarySource
    source: rapdb
  product_url: https://github.com/Knowledge-Graph-Hub/eco-kg
publications:
- authors:
  - John L Portwood II
  - Margaret R Woodhouse
  - Ethalinda K Cannon
  - Jack M Gardiner
  - Lisa C Harper
  - Mary L Schaeffer
  - Jesse R Walsh
  - Taner Z Sen
  - Kyoung Tak Cho
  - David A Schott
  - Bremen L Braun
  - Miranda Dietze
  - Brittney Dunfee
  - Christine G Elsik
  - Nancy Manchanda
  - Ed Coe
  - Marty Sachs
  - Philip Stinard
  - Josh Tolbert
  - Shane Zimmerman
  - Carson M Andorf
  doi: 10.1093/nar/gky1046
  id: https://pubmed.ncbi.nlm.nih.gov/30407532/
  journal: Nucleic Acids Res
  preferred: true
  title: 'MaizeGDB 2018: the maize multi-genome genetics and genomics database'
  year: '2019'
---
## Description

MaizeGDB is the community database for maize (Zea mays) genetics and genomics, maintained by the USDA-ARS. It integrates genome assemblies and gene models for B73 and an expanding set of maize and related Andropogoneae lines, along with gene function and expression data, genetic and physical maps, phenotypes, stocks, metabolic pathways, and curated literature. The resource provides genome browsers, a MaizeMine data-mining interface, and bulk downloads of sequence and annotation files, and serves as the upstream data source for eco-KG.

## Contacts

- USDA-ARS MaizeGDB (https://www.maizegdb.org)

## Products

### MaizeGDB Download Server

Bulk download server hosting maize and Andropogoneae genome assemblies, gene models (GFF, CDS, protein, genomic sequence), transposable element annotations, and other genomics datasets.

**URL**: [https://download.maizegdb.org/](https://download.maizegdb.org/)

### MaizeGDB Gene Model GFF Files

Gene model annotation files in GFF format for maize genome assemblies hosted on the MaizeGDB download server.

**URL**: [https://download.maizegdb.org/All_gene_model_GFF/](https://download.maizegdb.org/All_gene_model_GFF/)

### MaizeMine Downloads

MaizeMine data warehouse downloads providing integrated and queryable maize genomics datasets.

**URL**: [https://download.maizegdb.org/MaizeMine/](https://download.maizegdb.org/MaizeMine/)

## Publications

- [MaizeGDB 2018: the maize multi-genome genetics and genomics database](https://pubmed.ncbi.nlm.nih.gov/30407532/)

**Domains**: genomics, organisms, agriculture

---