---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: help@uniprot.org
  label: UniProt Consortium
description: UniProt Protein Knowledge Base
domains:
- biological systems
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
  id: uniprot.swissprot.fasta
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
  id: uniprot.trembl.xml
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
  id: uniprot.trembl.fasta
  name: Unreviewed (TrEMBL) FASTA
  original_source:
  - uniprot
  product_url: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_trembl.fasta.gz
  secondary_source:
  - uniprot
- category: Product
  description: Tab-delimited file of systematic ID, primary gene name (where assigned),
    chromosome, product description, UniProtKB accession, all synonyms, and product
    type (protein coding, ncRNA, etc.) for each gene
  format: tsv
  id: pombase.genes-products
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: PomBase gene names and products
  original_source:
  - uniprot
  - pombase
  product_url: https://www.pombase.org/data/names_and_identifiers/gene_IDs_names_products.tsv
  secondary_source:
  - pombase
- category: MappingProduct
  description: Tab-delimited file with the PomBase systematic identifier for each
    protein-coding gene mapped to the corresponding UniProt accession number
  format: tsv
  id: pombase.to-uniprot
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: PomBase to UniProt map
  original_source:
  - uniprot
  - pombase
  product_url: https://www.pombase.org/data/names_and_identifiers/PomBase2UniProt.tsv
  secondary_source:
  - pombase
- category: MappingProduct
  description: Mapping between chembl_35 target chembl_ids and UniProt accessions
  id: chembl.map_to_uniprot
  is_public: true
  name: ChEMBL map to UniProt
  original_source:
  - chembl
  - uniprot
  product_url: https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/chembl_uniprot_mapping.txt
  secondary_source:
  - chembl
repository: https://www.uniprot.org/help/downloads
---
UniProt Protein Knowledge Base