---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/
  id: ncbi
  label: National Center for Biotechnology Information (NCBI), U.S. National Library
    of Medicine
creation_date: '2026-06-18T00:00:00Z'
description: dbVar is NCBI's public archive of human genomic structural variation,
  covering large-scale variants such as insertions, deletions, duplications, inversions,
  copy number variants (CNVs), and translocations. It aggregates submitted structural
  variant calls together with their genomic placements, supporting evidence, and associated
  clinical assertions, and exchanges data with the European DGVa archive. dbVar provides
  a web portal for searching and browsing variants and regions, as well as bulk FTP
  downloads of variant call and region files in multiple formats. It serves as an
  upstream source for integrative knowledge graphs such as GenomicKB.
domains:
- genomics
- clinical
- biomedical
- genetic variation
homepage_url: https://www.ncbi.nlm.nih.gov/dbvar/
id: dbvar
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/home/about/policies/
  label: Public Domain (U.S. Government work; NCBI and NLM Data Usage Policies)
name: dbVar
products:
- category: GraphicalInterface
  description: Web portal for searching and browsing dbVar structural variation studies,
    variants, and genomic regions
  format: http
  id: dbvar.portal
  name: dbVar Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbvar
  product_url: https://www.ncbi.nlm.nih.gov/dbvar/
- category: Product
  description: FTP site hosting bulk downloads of dbVar structural variant call and
    region data files in multiple formats
  format: http
  id: dbvar.ftp
  name: dbVar FTP Site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbvar
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/dbVar/
- category: GraphProduct
  description: GenomicKB 1.0 Neo4j Database Dump (Requires license)
  dump_format: neo4j
  format: http
  id: genomickb.graph
  name: GenomicKB Graph Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: genomickb
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: dbvar
  - relation_type: prov:hadPrimarySource
    source: endb
  - relation_type: prov:hadPrimarySource
    source: enhanceratlas
  - relation_type: prov:hadPrimarySource
    source: ccre
  - relation_type: prov:hadPrimarySource
    source: fire
  - relation_type: prov:hadPrimarySource
    source: motifmap
  product_url: https://available-inventions.umich.edu/product/genomickb-a-knowledgebase-for-the-human-genome
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
publications:
- authors:
  - Lappalainen I
  - Lopez J
  - Skipper L
  - Hefferon T
  - Spalding JD
  - Garner J
  - Chen C
  - Maguire M
  - Corbett M
  - Zhou G
  - Paschall J
  - Ananiev V
  - Flicek P
  - Church DM
  doi: 10.1093/nar/gks1213
  id: https://www.ncbi.nlm.nih.gov/pubmed/23193291
  journal: Nucleic Acids Res
  preferred: true
  title: 'DbVar and DGVa: public archives for genomic structural variation'
  year: '2013'
rrid: SCR_003219
taxon:
- NCBITaxon:9606
---
# dbVar

## Overview

dbVar is the U.S. National Center for Biotechnology Information (NCBI) public archive of human genomic structural variation. It records large-scale genomic variants, including insertions, deletions, duplications, inversions, copy number variants (CNVs), and translocations, along with their placements on reference assemblies and supporting evidence.

## Access

- Portal: search and browse structural variation studies, variants, and regions at the dbVar website
- Bulk download: variant call and region files via the NCBI FTP site

## Related resources

dbVar exchanges structural variation data with the European DGVa archive and serves as an upstream source for integrative knowledge graphs such as GenomicKB.

## Terms and citation

dbVar is produced by NCBI/NLM; specific license terms are not stated here. Please cite the dbVar NAR publication when using the resource.