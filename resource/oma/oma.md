---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: contact@omabrowser.org
  - contact_type: url
    value: https://omabrowser.org/contact/
  label: OMA Team - SIB Swiss Institute of Bioinformatics
- category: Individual
  contact_details:
  - contact_type: email
    value: adrian.altenhoff@inf.ethz.ch
  - contact_type: url
    value: https://omabrowser.org/oma/team/
  label: Adrian Altenhoff
description: OMA (Orthologous MAtrix) is a database of orthologous genes among multiple
  species, providing a systematic classification of orthologs across complete genomes.
domains:
- biological systems
- organisms
homepage_url: https://omabrowser.org/
id: oma
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: OMA
products:
- category: GraphicalInterface
  description: Web interface for exploring OMA data
  id: oma.site
  is_public: true
  name: OMA Browser
  original_source:
  - oma
  product_url: https://omabrowser.org/oma/
  secondary_source:
  - oma
- category: ProgrammingInterface
  description: RESTful API for accessing OMA data
  id: oma.api.rest
  is_public: true
  name: OMA REST API
  original_source:
  - oma
  product_url: https://omabrowser.org/api/
  secondary_source:
  - oma
- category: ProgrammingInterface
  description: SPARQL endpoint for accessing OMA data
  id: oma.api.sparql
  is_public: true
  name: OMA SPARQL
  original_source:
  - oma
  product_url: https://sparql.omabrowser.org/lode/sparql
  secondary_source:
  - oma
- category: Product
  compression: gzip
  description: OMA orthology groups in plain text format
  id: oma.groups.txt
  name: OMA Groups (Text)
  original_source:
  - oma
  product_url: https://omabrowser.org/oma/current/OmaGroups.txt.gz
  secondary_source:
  - oma
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-02: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-09-01: HTTP 502 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-13: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2025-09-03: HTTP 404 error
    when accessing file'
- category: Product
  description: OMA orthology groups in OrthoXML format
  format: xml
  id: oma.groups.orthoxml
  name: OMA Groups (OrthoXML)
  original_source:
  - oma
  product_url: https://omabrowser.org/oma/current/OmaGroups.orthoxml
  secondary_source:
  - oma
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-02: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-09-01: HTTP 502 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-13: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2025-09-03: HTTP 404 error
    when accessing file'
- category: Product
  description: Hierarchical Orthologous Groups (HOGs) in OrthoXML format
  format: xml
  id: oma.hogs.orthoxml
  name: OMA HOGs (OrthoXML)
  original_source:
  - oma
  product_url: https://omabrowser.org/oma/current/OmaHOGs.orthoxml
  secondary_source:
  - oma
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-02: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-09-02: HTTP 502 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2025-09-03: HTTP 404 error
    when accessing file'
- category: Product
  compression: gzip
  description: Pairwise orthologs in tab-separated text format
  format: tsv
  id: oma.pairs.txt
  name: OMA Pairwise Orthologs
  original_source:
  - oma
  product_url: https://omabrowser.org/oma/current/OrthologousPairs.txt.gz
  secondary_source:
  - oma
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-02: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-31: HTTP 502 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2025-09-03: HTTP 502 error
    when accessing file'
- category: Product
  compression: gzip
  description: Protein sequences from all genomes in FASTA format
  format: fasta
  id: oma.proteins.fasta
  name: OMA Protein Sequences
  original_source:
  - oma
  product_url: https://omabrowser.org/oma/current/oma-proteins.fa.gz
  secondary_source:
  - oma
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-02: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-09-01: HTTP 502 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2025-09-03: HTTP 404 error
    when accessing file'
- category: Product
  compression: gzip
  description: cDNA sequences for Eukaryotic genomes in FASTA format
  format: fasta
  id: oma.cdna.eukaryotes.fasta
  name: OMA cDNA Sequences (Eukaryotes)
  original_source:
  - oma
  product_url: https://omabrowser.org/oma/current/oma-eukaryotes.cdna.fa.gz
  secondary_source:
  - oma
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-02: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-31: HTTP 502 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-12: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2025-09-03: HTTP 404 error
    when accessing file'
- category: Product
  compression: gzip
  description: cDNA sequences for Prokaryotic genomes in FASTA format
  format: fasta
  id: oma.cdna.prokaryotes.fasta
  name: OMA cDNA Sequences (Prokaryotes)
  original_source:
  - oma
  product_url: https://omabrowser.org/oma/current/oma-prokaryotes.cdna.fa.gz
  secondary_source:
  - oma
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-02: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-13: HTTP 502 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-13: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2025-09-03: HTTP 404 error
    when accessing file'
- category: Product
  description: OMA Browser database in HDF5 format
  id: oma.hdf5
  name: OMA Browser Database (HDF5)
  original_source:
  - oma
  product_url: https://omabrowser.org/oma/current/OmaServer.h5
  secondary_source:
  - oma
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-02: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-26: HTTP 502 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-09-03: HTTP 404 error
    when accessing file'
- category: Product
  compression: gzip
  description: OMA data in RDF format (Turtle syntax)
  format: ttl
  id: oma.rdf
  name: OMA RDF Data
  original_source:
  - oma
  product_url: https://omabrowser.org/oma/current/OMA.ttl.gz
  secondary_source:
  - oma
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-02: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-13: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2025-08-12: HTTP 502 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-09-03: HTTP 404 error
    when accessing file'
- category: MappingProduct
  compression: gzip
  description: Mapping of OMA identifiers to UniProt accession numbers
  format: tsv
  id: oma.mapping.uniprot
  name: OMA to UniProt Mapping
  original_source:
  - oma
  - uniprot
  product_url: https://omabrowser.org/oma/current/oma-uniprot.txt.gz
  secondary_source:
  - oma
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-02: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-13: HTTP 502 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-13: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2025-09-03: HTTP 404 error
    when accessing file'
---
OMA (Orthologous MAtrix) is a comprehensive database of orthologous gene relationships across multiple species. It provides a systematic and efficient approach to identifying orthologs among complete genomes, which are genes in different species that evolved from a common ancestor through speciation.

The OMA methodology employs an algorithm that starts with an all-against-all sequence alignment, followed by the identification of orthologous pairs and the construction of orthologous groups. The database includes:

- Regular orthology inference across thousands of genomes
- Hierarchical Orthologous Groups (HOGs) to capture evolutionary relationships at different taxonomic levels
- Pairwise orthologous relationships between genes
- Protein and DNA sequence data
- Cross-references to major biological databases (UniProt, Ensembl, RefSeq, etc.)
- Functional annotations and GO term mappings

OMA is maintained by the Dessimoz Lab at the University of Lausanne and the Swiss Institute of Bioinformatics (SIB), with biannual releases adding new genomes and improving data quality. The database is widely used for comparative genomics, phylogenetics, functional annotation transfer, and evolutionary studies.

Access to OMA data is provided through a user-friendly web interface, a REST API for programmatic access, and bulk downloads in various formats including text files, OrthoXML, FASTA, and RDF.