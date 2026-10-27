---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/biosample/
  label: National Center for Biotechnology Information (NCBI)
creation_date: '2026-10-27T00:00:00Z'
description: The BioSample database contains descriptions of biological source materials
  used in experimental assays. Each record captures sample attributes such as organism,
  tissue, cell line, isolate, and environment, using community attribute packages
  such as MIxS, and links to the experimental data derived from the sample in SRA,
  GenBank, GEO, dbGaP, and other archives. BioSample accessions (SAMN, and SAMEA and
  SAMD through the INSDC partners ENA and DDBJ) are exchanged with EMBL-EBI and DDBJ.
domains:
- genomics
- metadata
- information technology
- biomedical
homepage_url: https://www.ncbi.nlm.nih.gov/biosample/
id: biosample
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/home/about/policies/
  label: NCBI usage policies
name: NCBI BioSample
products:
- category: GraphicalInterface
  description: Entrez BioSample search over biological sample records and their links
    to experimental data.
  format: http
  id: biosample.web
  name: BioSample Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biosample
  product_url: https://www.ncbi.nlm.nih.gov/biosample/
- category: Product
  description: Bulk BioSample records in XML and attribute summary files.
  format: xml
  id: biosample.ftp
  name: BioSample FTP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biosample
  product_url: https://ftp.ncbi.nlm.nih.gov/biosample/
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
  - T. Barrett
  - K. Clark
  - R. Gevorgyan
  - V. Gorelenkov
  - et al.
  doi: 10.1093/nar/gkr1163
  id: doi:10.1093/nar/gkr1163
  journal: Nucleic Acids Research
  preferred: true
  title: 'BioProject and BioSample databases at NCBI: facilitating capture and organization
    of metadata'
  year: '2012'
synonyms:
- BioSample
---
# NCBI BioSample

## Overview

The BioSample database contains descriptions of the biological source materials used in experimental assays. Records capture sample attributes using community attribute packages such as MIxS, and link to the data derived from each sample in SRA, GenBank, GEO, dbGaP, and other archives. On 2026-10-27 it held about 60.6 million records.

## Access

- Entrez BioSample search, also reachable through the E-utilities (`db=biosample`).
- Bulk XML records and attribute summary files on the NCBI FTP site.

## Citation

Barrett T, Clark K, Gevorgyan R, Gorelenkov V, et al. BioProject and BioSample databases at NCBI: facilitating capture and organization of metadata. Nucleic Acids Res. 2012. doi:10.1093/nar/gkr1163
