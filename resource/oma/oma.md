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
  id: sib
  label: OMA Team - SIB Swiss Institute of Bioinformatics
- category: Individual
  contact_details:
  - contact_type: email
    value: adrian.altenhoff@inf.ethz.ch
  - contact_type: url
    value: https://omabrowser.org/oma/team/
  label: Adrian Altenhoff
creation_date: '2025-05-07T00:00:00Z'
description: OMA (Orthologous MAtrix) is a database of orthologous genes among multiple
  species, providing a systematic classification of orthologs across complete genomes.
domains:
- biological systems
- organisms
homepage_url: https://omabrowser.org/
id: oma
last_modified_date: '2026-05-23T00:00:00Z'
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
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/oma/
- category: ProgrammingInterface
  description: RESTful API for accessing OMA data
  id: oma.api.rest
  is_public: true
  name: OMA REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/api/
- category: ProgrammingInterface
  description: SPARQL endpoint for accessing OMA data
  id: oma.api.sparql
  is_public: true
  name: OMA SPARQL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://sparql.omabrowser.org/lode/sparql
- category: Product
  compression: gzip
  description: OMA orthology groups in plain text format
  id: oma.groups.txt
  name: OMA Groups (Text)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/oma/current/OmaGroups.txt.gz
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-28_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-03_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2025-12-15_ HTTP 502 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-05-21: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-23: HTTP 403 error
    when accessing file'
- category: Product
  description: OMA orthology groups in OrthoXML format
  format: xml
  id: oma.groups.orthoxml
  name: OMA Groups (OrthoXML)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/oma/current/OmaGroups.orthoxml
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-02-18_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2026-01-28_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-15_ HTTP 502 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-05-21: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-23: HTTP 403 error
    when accessing file'
- category: Product
  description: Hierarchical Orthologous Groups (HOGs) in OrthoXML format
  format: xml
  id: oma.hogs.orthoxml
  name: OMA HOGs (OrthoXML)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/oma/current/OmaHOGs.orthoxml
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-28_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-03_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2025-12-15_ HTTP 502 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-05-21: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-03-30: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-05-23: HTTP 403 error
    when accessing file'
- category: Product
  compression: gzip
  description: Pairwise orthologs in tab-separated text format
  format: tsv
  id: oma.pairs.txt
  name: OMA Pairwise Orthologs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/oma/current/OrthologousPairs.txt.gz
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-28_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-03_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2025-12-15_ HTTP 502 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-05-21: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-23: HTTP 403 error
    when accessing file'
- category: Product
  compression: gzip
  description: Protein sequences from all genomes in FASTA format
  format: fasta
  id: oma.proteins.fasta
  name: OMA Protein Sequences
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/oma/current/oma-proteins.fa.gz
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-28_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-03_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2026-01-02_ HTTP 502 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-05-21: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-23: HTTP 403 error
    when accessing file'
- category: Product
  compression: gzip
  description: cDNA sequences for Eukaryotic genomes in FASTA format
  format: fasta
  id: oma.cdna.eukaryotes.fasta
  name: OMA cDNA Sequences (Eukaryotes)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/oma/current/oma-eukaryotes.cdna.fa.gz
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-28_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-03_ HTTP 502 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-13_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2026-05-21: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-23: HTTP 403 error
    when accessing file'
- category: Product
  compression: gzip
  description: cDNA sequences for Prokaryotic genomes in FASTA format
  format: fasta
  id: oma.cdna.prokaryotes.fasta
  name: OMA cDNA Sequences (Prokaryotes)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/oma/current/oma-prokaryotes.cdna.fa.gz
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-28_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-03_ HTTP 502 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-13_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2026-05-21: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-23: HTTP 403 error
    when accessing file'
- category: Product
  description: OMA Browser database in HDF5 format
  id: oma.hdf5
  name: OMA Browser Database (HDF5)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/oma/current/OmaServer.h5
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-03-30_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2026-01-28_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-03_ HTTP 502 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-05-21: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-03-30: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-05-23: HTTP 403 error
    when accessing file'
- category: Product
  compression: gzip
  description: OMA data in RDF format (Turtle syntax)
  format: ttl
  id: oma.rdf
  name: OMA RDF Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/oma/current/OMA.ttl.gz
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-03-30_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2026-01-28_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-03_ HTTP 502 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-05-21: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-23: HTTP 403 error
    when accessing file'
- category: MappingProduct
  compression: gzip
  description: Mapping of OMA identifiers to UniProt accession numbers
  format: tsv
  id: oma.mapping.uniprot
  name: OMA to UniProt Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://omabrowser.org/oma/current/oma-uniprot.txt.gz
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-02-18_ Timeout connecting
    to URL
  - File was not able to be retrieved when checked on 2026-01-28_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-03_ HTTP 502 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-05-21: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-23: HTTP 403 error
    when accessing file'
publications:
- id: https://doi.org/10.1093/nar/gkad1020
  title: 'OMA orthology in 2024: improved prokaryote coverage, ancestral and extant
    GO enrichment, a revamped synteny viewer and more in the OMA Ecosystem'
- id: https://doi.org/10.1093/nar/gkaa1007
  title: 'OMA orthology in 2021: website overhaul, conserved isoforms, ancestral gene
    order and more'
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