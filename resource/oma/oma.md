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
last_modified_date: '2026-05-26T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: OMA
products:
- category: GraphicalInterface
  description: Web interface for exploring OMA data
  format: http
  id: oma.site
  is_public: true
  name: OMA Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/oma/
- category: ProgrammingInterface
  description: RESTful API for accessing OMA data
  format: http
  id: oma.api.rest
  is_public: true
  name: OMA REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/api/
- category: ProgrammingInterface
  description: SPARQL endpoint for accessing OMA data
  format: http
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
  format: txt
  id: oma.groups.txt
  name: OMA Groups (Text)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/All/oma-groups.txt.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
    when accessing file'
- category: Product
  compression: gzip
  description: OMA orthology groups in OrthoXML format
  format: xml
  id: oma.groups.orthoxml
  name: OMA Groups (OrthoXML)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/All/oma-groups.orthoXML.xml.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
    when accessing file'
- category: Product
  compression: gzip
  description: Hierarchical Orthologous Groups (HOGs) in OrthoXML format
  format: xml
  id: oma.hogs.orthoxml
  name: OMA HOGs (OrthoXML)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/All/oma-hogs.orthoXML.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
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
  product_url: https://omabrowser.org/All/oma-pairs.txt.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
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
  product_url: https://omabrowser.org/All/oma-seqs.fa.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
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
  product_url: https://omabrowser.org/All/eukaryotes.cdna.fa.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
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
  product_url: https://omabrowser.org/All/prokaryotes.cdna.fa.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
    when accessing file'
- category: Product
  compression: gzip
  description: cDNA sequences for viral genomes in FASTA format
  format: fasta
  id: oma.cdna.viruses.fasta
  name: OMA cDNA Sequences (Viruses)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/All/viruses.cdna.fa.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
    when accessing file'
- category: Product
  compression: targz
  description: Protein sequences in SeqXML format
  format: xml
  id: oma.proteins.seqxml
  name: OMA Protein Sequences (SeqXML)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/All/oma-seqs.seqxml.tgz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
    when accessing file'
- category: Product
  compression: gzip
  description: Protein annotations in text format
  format: txt
  id: oma.protein-annotations.txt
  name: OMA Protein Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/All/oma-protein-annotations.txt.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
    when accessing file'
- category: Product
  description: OMA Browser database in HDF5 format
  format: hdf5
  id: oma.hdf5
  name: OMA Browser Database (HDF5)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/All/OmaServer.h5
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
    when accessing file'
- category: Product
  description: Suffix index for the OMA Browser HDF5 database
  format: mixed
  id: oma.hdf5.index
  name: OMA Browser Database Index
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/All/OmaServer.h5.idx
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
    when accessing file'
- category: Product
  compression: targz
  description: OMA data in RDF format (Turtle syntax)
  format: ttl
  id: oma.rdf
  name: OMA RDF Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/All/oma-rdf-turtle.tgz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
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
  product_url: https://omabrowser.org/All/oma-uniprot.txt.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
    when accessing file'
- category: MappingProduct
  compression: gzip
  description: Mapping of OMA identifiers to Ensembl identifiers
  format: tsv
  id: oma.mapping.ensembl
  name: OMA to Ensembl Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  - relation_type: prov:hadPrimarySource
    source: ensembl
  product_url: https://omabrowser.org/All/oma-ensembl.txt.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
    when accessing file'
- category: MappingProduct
  compression: gzip
  description: Mapping of OMA identifiers to RefSeq accessions
  format: tsv
  id: oma.mapping.refseq
  name: OMA to RefSeq Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  - relation_type: prov:hadPrimarySource
    source: refseq
  product_url: https://omabrowser.org/All/oma-refseq.txt.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
    when accessing file'
- category: MappingProduct
  compression: gzip
  description: Mapping of OMA identifiers to Entrez Gene identifiers
  format: tsv
  id: oma.mapping.entrez
  name: OMA to Entrez Gene Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_url: https://omabrowser.org/All/oma-entrez.txt.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
    when accessing file'
- category: MappingProduct
  compression: gzip
  description: Mapping of OMA identifiers to Gene Ontology terms
  format: tsv
  id: oma.mapping.go
  name: OMA to GO Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  - relation_type: prov:hadPrimarySource
    source: go
  product_url: https://omabrowser.org/All/oma-go.txt.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
    when accessing file'
- category: Product
  description: Species metadata including taxonomy identifiers and genome source information
  format: txt
  id: oma.species.txt
  name: OMA Species Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/All/oma-species.txt
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: No Content-Length
    header found'
  - 'File was not able to be retrieved when checked on 2026-05-29: No Content-Length
    header found'
- category: Product
  compression: gzip
  description: Text descriptions for OMA groups
  format: txt
  id: oma.group-descriptions.txt
  name: OMA Group Descriptions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oma
  product_url: https://omabrowser.org/All/group-descriptions.txt.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-28: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-05-29: HTTP 403 error
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