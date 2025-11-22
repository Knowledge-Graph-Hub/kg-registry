---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: info@ncbi.nlm.nih.gov
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/home/about/contact/
  label: National Center for Biotechnology Information (NCBI)
description: dbSNP contains human single nucleotide variations, microsatellites, and
  small-scale insertions and deletions along with publication, population frequency,
  molecular consequence, and genomic and RefSeq mapping information for both common
  variations and clinical mutations.
domains:
- biological systems
- health
homepage_url: https://www.ncbi.nlm.nih.gov/snp/
id: dbsnp
infores_id: dbsnp
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/home/about/policies/
  label: Public Domain
name: dbSNP
products:
- category: GraphicalInterface
  description: Web interface for searching and exploring dbSNP data
  id: dbsnp.site
  is_public: true
  name: dbSNP Web Interface
  original_source:
  - dbsnp
  product_url: https://www.ncbi.nlm.nih.gov/snp/
  secondary_source:
  - dbsnp
- category: ProgrammingInterface
  description: Programmatic access to dbSNP data via the NCBI E-utilities API
  id: dbsnp.api
  is_public: true
  name: dbSNP E-utilities API
  original_source:
  - dbsnp
  product_url: https://www.ncbi.nlm.nih.gov/books/NBK25500/
  secondary_source:
  - dbsnp
- category: Product
  compression: gzip
  description: JSON format files with dbSNP RefSNP data
  format: json
  id: dbsnp.json
  name: dbSNP JSON Files
  original_source:
  - dbsnp
  product_url: https://ftp.ncbi.nih.gov/snp/latest_release/JSON/
  secondary_source:
  - dbsnp
- category: ProgrammingInterface
  description: NCBI Variation Services API for accessing and manipulating variant
    data
  id: dbsnp.variation.api
  is_public: true
  name: NCBI Variation Services API
  original_source:
  - dbsnp
  product_url: https://api.ncbi.nlm.nih.gov/variation/v0/
  secondary_source:
  - dbsnp
- category: GraphProduct
  compression: zip
  description: Nodes from dbSNP
  format: csv
  id: biomarkerkg.nodes.variant
  name: BKG Variant Nodes
  original_source:
  - dbsnp
  product_file_size: 782975
  product_url: https://s3.amazonaws.com/maayan-kg/biomarker-kg/Variant.nodes.zip
  secondary_source:
  - biomarkerkg
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
- category: Product
  description: Genetic variant data from ClinVar, dbSNP, GWAS Catalog and other variant
    databases
  format: http
  id: genecards.variant.data
  name: GeneCards Variant Data
  original_source:
  - clinvar
  - dbsnp
  - gwascatalog
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-11-21_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-11-19_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-11-22: HTTP 403 error
    when accessing file'
publications:
- authors:
  - Sherry ST
  - Ward MH
  - Kholodov M
  - Baker J
  - Phan L
  - Smigielski EM
  - Sirotkin K
  doi: doi:10.1093/nar/29.1.308
  id: doi:10.1093/nar/29.1.308
  title: dbSNP - Database for Single Nucleotide Polymorphisms and Other Classes of
    Minor Genetic Variation
  year: '2001'
- authors:
  - Kitts A
  - Phan L
  - Ward M
  - Holmes JB
  doi: doi:10.1093/nar/gkad1045
  id: doi:10.1093/nar/gkad1045
  preferred: true
  title: The evolution of dbSNP - 25 years of impact in genomic research
  year: '2023'
repository: https://github.com/ncbi/dbsnp
---
dbSNP (Database of Single Nucleotide Polymorphisms) is a public archive for genetic variation established in 1999 by the National Center for Biotechnology Information (NCBI) in collaboration with the National Human Genome Research Institute (NHGRI). It serves as a central repository for both single nucleotide variations and small-scale insertions and deletions (indels).

The database contains over 328 million reference SNPs (as noted on the homepage) and includes data on:
- Single nucleotide variations
- Small insertions and deletions
- Microsatellites and short tandem repeats
- Population allele frequencies
- Genomic and RefSeq mapping coordinates
- Molecular consequences and functional impacts
- Clinical significance annotations
- Links to associated publications

dbSNP assigns unique identifiers to variants (RefSNP or "rs" numbers) which are widely used in genomic research and clinical settings for consistent variant identification across different studies and platforms. The database is integrated with other NCBI resources including PubMed, Gene, ClinVar, and the NCBI Variation services.

The resource also includes the Allele Frequency Aggregator (ALFA) project, which provides allele frequency data from over 200,000 subjects with regular updates, aiming to eventually cover data from more than 1 million dbGaP subjects.

Data from dbSNP is available through a web interface, programmatic APIs like E-utilities and Variation Services, and bulk downloads via FTP in formats including VCF, JSON, and XML.