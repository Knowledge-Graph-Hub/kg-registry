---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/genbank/
  label: National Center for Biotechnology Information (NCBI)
creation_date: '2026-10-27T00:00:00Z'
description: GenBank is the NIH genetic sequence database, an annotated collection
  of all publicly available DNA sequences, built from submissions by individual laboratories
  and large-scale sequencing projects. It is part of the International Nucleotide
  Sequence Database Collaboration (INSDC), exchanging data daily with the DNA Data
  Bank of Japan (DDBJ) and the European Nucleotide Archive (ENA). GenBank records
  are searchable through the Entrez Nucleotide database and distributed as bimonthly
  releases with daily updates.
domains:
- genomics
- biomedical
homepage_url: https://www.ncbi.nlm.nih.gov/genbank/
id: genbank
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/genbank/about/
  label: NCBI policies (no restrictions on use or distribution of GenBank data)
name: GenBank
products:
- category: Product
  description: Full GenBank releases (every two months) and daily update files in
    GenBank flat-file format.
  format: txt
  compression: gzip
  id: genbank.ftp
  name: GenBank FTP Releases
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genbank
  product_url: https://ftp.ncbi.nlm.nih.gov/genbank/
- category: GraphicalInterface
  description: Entrez Nucleotide search over GenBank and other nucleotide sequence
    records.
  format: http
  id: genbank.nucleotide
  name: Entrez Nucleotide
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genbank
  product_url: https://www.ncbi.nlm.nih.gov/nuccore/
- category: ProgrammingInterface
  connection_url: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
  description: Entrez Programming Utilities (E-utilities), a set of server-side programs
    (EInfo, ESearch, ESummary, EFetch, ELink, EPost, EGQuery, ESpell, ECitMatch) with
    a fixed URL syntax for searching, linking and retrieving records from the 38 Entrez
    databases. Results are returned as XML, with JSON available for several utilities.
  format: mixed
  id: entrez.eutils
  name: Entrez E-utilities
  original_source:
  - relation_type: prov:hadPrimarySource
    source: entrez
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbvar
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: gtr
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: sra
  - relation_type: prov:hadPrimarySource
    source: cdd
  - relation_type: prov:hadPrimarySource
    source: genbank
  - relation_type: prov:hadPrimarySource
    source: ncbi-protein
  - relation_type: prov:hadPrimarySource
    source: bioproject
  - relation_type: prov:hadPrimarySource
    source: biosample
  product_url: https://www.ncbi.nlm.nih.gov/books/NBK25501/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: pubmed
  - relation_type: prov:wasInformedBy
    source: ncbigene
  - relation_type: prov:wasInformedBy
    source: ncbitaxon
- category: GraphicalInterface
  description: NCBI global cross-database search page, which runs a single query against
    all Entrez databases and reports hit counts per database.
  format: http
  id: entrez.web
  name: Entrez Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: entrez
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbvar
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: gtr
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: sra
  - relation_type: prov:hadPrimarySource
    source: cdd
  - relation_type: prov:hadPrimarySource
    source: genbank
  - relation_type: prov:hadPrimarySource
    source: ncbi-protein
  - relation_type: prov:hadPrimarySource
    source: bioproject
  - relation_type: prov:hadPrimarySource
    source: biosample
  product_url: https://www.ncbi.nlm.nih.gov/search/
- category: ProgrammingInterface
  description: Entrez Direct (EDirect) command-line tools for Unix systems that wrap
    the E-utilities (esearch, efetch, elink, efilter, xtract and others) for pipeline
    access to Entrez databases.
  format: mixed
  id: entrez.edirect
  name: Entrez Direct (EDirect)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: entrez
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbvar
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: gtr
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: sra
  - relation_type: prov:hadPrimarySource
    source: cdd
  - relation_type: prov:hadPrimarySource
    source: genbank
  - relation_type: prov:hadPrimarySource
    source: ncbi-protein
  - relation_type: prov:hadPrimarySource
    source: bioproject
  - relation_type: prov:hadPrimarySource
    source: biosample
  product_url: https://www.ncbi.nlm.nih.gov/books/NBK179288/
  repository: https://github.com/ncbi/entrez-direct
- category: GraphicalInterface
  description: Entrez search interface for NCBI Protein sequence records, with links
    to Gene, Nucleotide, Structure, and Conserved Domains.
  format: http
  id: ncbi-protein.web
  name: NCBI Protein Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbi-protein
  - relation_type: prov:hadPrimarySource
    source: genbank
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: pdb
  product_url: https://www.ncbi.nlm.nih.gov/protein/
publications:
- authors:
  - Eric W. Sayers
  - Mark Cavanaugh
  - Linda Frisse
  - Kim D. Pruitt
  - et al.
  doi: 10.1093/nar/gkae1114
  id: doi:10.1093/nar/gkae1114
  journal: Nucleic Acids Research
  preferred: true
  title: GenBank 2025 update
  year: '2025'
synonyms:
- NCBI GenBank
- Nucleotide
---
# GenBank

## Overview

GenBank is the NIH genetic sequence database, an annotated collection of all publicly available DNA sequences. It is part of the International Nucleotide Sequence Database Collaboration (INSDC) with DDBJ and ENA, and the three exchange data daily. A GenBank release comes out every two months, with daily updates in between.

## Access

- FTP releases and daily updates in GenBank flat-file format.
- Entrez Nucleotide search, also reachable through the E-utilities.

NCBI places no restrictions on the use or distribution of GenBank data, though some submitters may claim patent, copyright, or other rights in the data they submitted.

## Citation

Sayers EW, Cavanaugh M, Frisse L, Pruitt KD, et al. GenBank 2025 update. Nucleic Acids Res. 2025. doi:10.1093/nar/gkae1114
