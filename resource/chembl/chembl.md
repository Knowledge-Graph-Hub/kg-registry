---
layout: resource_detail
activity_status: active
id: chembl
name: ChEMBL
description: ChEMBL is a manually curated database of bioactive molecules with drug-like
  properties. It brings together chemical, bioactivity and genomic data to aid the
  translation of genomic information into effective new drugs.
domains:
- chemistry and biochemistry
contacts:
- category: Organization
  label: ChEMBL
  contact_details:
  - contact_type: email
    value: chembl-help@ebi.ac.uk
homepage_url: https://www.ebi.ac.uk/chembl/
repository: https://github.com/chembl
category: DataSource
license:
  label: CC-BY-SA-3.0
  id: https://creativecommons.org/licenses/by-sa/3.0/
products:
- category: GraphicalInterface
  description: Web interface for searching and exploring ChEMBL data
  id: chembl.site
  name: ChEMBL Web Interface
  original_source:
  - chembl
  product_url: https://www.ebi.ac.uk/chembl/
  secondary_source:
  - chembl
  is_public: true
- category: ProgrammingInterface
  description: RESTful API for accessing ChEMBL data programmatically
  id: chembl.api
  name: ChEMBL API
  original_source:
  - chembl
  product_url: https://www.ebi.ac.uk/chembl/api/data/docs
  secondary_source:
  - chembl
  is_public: true
- category: Product
  description: PostgreSQL database dump of the complete ChEMBL database
  format: postgres
  compression: gzip
  id: chembl.postgres
  name: ChEMBL PostgreSQL
  original_source:
  - chembl
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/
  secondary_source:
  - chembl
- category: Product
  description: MySQL database dump of the complete ChEMBL database
  format: sql
  compression: gzip
  id: chembl.mysql
  name: ChEMBL MySQL
  original_source:
  - chembl
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/
  secondary_source:
  - chembl
- category: Product
  description: SQLite database file containing the complete ChEMBL database
  compression: gzip
  id: chembl.sqlite
  name: ChEMBL SQLite
  original_source:
  - chembl
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/
  secondary_source:
  - chembl
- category: Product
  description: Structure data files for all chemical compounds in ChEMBL
  format: sdf
  compression: gzip
  id: chembl.sdf
  name: ChEMBL SDF
  original_source:
  - chembl
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/
  secondary_source:
  - chembl
- category: Product
  description: RDF version of the ChEMBL database
  format: ttl
  compression: gzip
  id: chembl.rdf
  name: ChEMBL RDF
  original_source:
  - chembl
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBL-RDF/latest/
  secondary_source:
  - chembl
- category: ProgrammingInterface
  description: SPARQL endpoint for the ChEMBL RDF data
  id: chembl.sparql
  name: ChEMBL SPARQL
  original_source:
  - chembl
  product_url: https://www.ebi.ac.uk/rdf/services/sparql
  secondary_source:
  - chembl
  is_public: true
- category: MappingProduct
  description: Mapping between chembl_35 target chembl_ids and UniProt accessions
  id: chembl.sparql
  name: ChEMBL SPARQL
  original_source:
  - chembl
  - uniprot
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/chembl_uniprot_mapping.txt
  secondary_source:
  - chembl
  is_public: true
publications:
- doi: doi:10.1093/nar/gkad1004
  id: doi:10.1093/nar/gkad1004
  preferred: true
  year: '2023'
  authors:
  - Zdrazil B
  - Felix E
  - Hunter F
  - Manners EJM
  - Blackshaw J
  - Corbett S
  - de Veij M
  - Ioannidis H
  - Mendez Lopez DM
  - Mosquera JF
  - Magarinos MP
  - Bosc N
  - Arcila R
  - "Kizil\xF6ren T"
  - Gaulton A
  - Bento AP
  - Adasme MF
  - Monecke PM
  - Landrum GA
  - Leach AR
  title: 'The ChEMBL Database in 2023: a drug discovery platform spanning multiple
    bioactivity data types and time periods'
---

ChEMBL is a manually curated database of bioactive molecules with drug-like properties. It brings together chemical, bioactivity and genomic data to aid the translation of genomic information into effective new drugs.

The database contains detailed information on:
- Over 2 million compounds
- More than 1 million assays
- Binding, functional, and ADMET data
- Over 15,000 targets, including proteins, cells, and organisms
- Around 90,000 publications and documents

ChEMBL is widely used in drug discovery, pharmacology research, chemical biology, and medicinal chemistry. The database undergoes regular updates, with new data releases typically occurring 3-4 times per year.
