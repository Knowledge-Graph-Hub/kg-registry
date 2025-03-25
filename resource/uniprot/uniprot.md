---
activity_status: active
category: DataSource
contacts:
- category: Organization
  email: help@uniprot.org
  label: UniProt Consortium
description: UniProt Protein Knowledge Base
domain: biological systems
homepage_url: https://www.uniprot.org/
id: uniprot
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: uniprot
products:
- category: GraphProduct
  compression: targz
  description: UniProt proteins from microbes, as graph nodes and edges
  format: kgx
  id: kg-microbe.graph.uniprot
  name: KG-Microbe UniProt microbe transform
  original_source:
  - uniprot
  product_url: https://kghub.io/kg-microbe/KGMicrobe-transformed-uniprot-microbes-20240924.tar.gz
  secondary_source:
  - kg-microbe
- category: Product
  compression: gzip
  description: The Reviewed (Swiss-Prot) section of UniProt proteins
  format: kgx
  id: uniprot.swissprot.xml
  name: Reviewed (Swiss-Prot) XML
  original_source:
  - uniprot
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.xml.gz
  secondary_source:
  - uniprot
- category: Product
  compression: gzip
  description: The Reviewed (Swiss-Prot) section of UniProt proteins
  format: fasta
  id: uniprot.swissprot.xml
  name: Reviewed (Swiss-Prot) FASTA
  original_source:
  - uniprot
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
  secondary_source:
  - uniprot
- category: Product
  compression: gzip
  description: The Unreviewed (TrEMBL) section of UniProt proteins
  format: xml
  id: uniprot.swissprot.xml
  name: Unreviewed (TrEMBL) XML
  original_source:
  - uniprot
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_trembl.xml.gz
  secondary_source:
  - uniprot
- category: Product
  compression: gzip
  description: The Unreviewed (TrEMBL) section of UniProt proteins
  format: fasta
  id: uniprot.swissprot.xml
  name: Unreviewed (TrEMBL) FASTA
  original_source:
  - uniprot
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_trembl.fasta.gz
  secondary_source:
  - uniprot
repository: https://www.uniprot.org/help/downloads
---
UniProt Protein Knowledge Base