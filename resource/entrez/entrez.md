---
activity_status: active
category: Aggregator
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.ncbi.nlm.nih.gov/home/about/contact/
    id: ncbi
    label: NCBI
creation_date: '2025-11-05T00:00:00Z'
description: Entrez is NCBI's primary text search and retrieval system that integrates multiple biological databases including PubMed, GenBank, Gene, Protein, and many others. It provides a unified query interface and retrieval mechanism across NCBI's vast collection of biomedical and genomic data resources, enabling researchers to search and access information from disparate databases using a single query system.
domains:
  - biomedical
  - genomics
  - literature
homepage_url: https://www.ncbi.nlm.nih.gov/search/
id: entrez
infores_id: entrez
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/home/about/policies/
  label: NCBI Website and Data Usage Policies (U.S. Government work; some submitted
    records may carry third-party restrictions)
name: Entrez
products:
  - category: ProgrammingInterface
    connection_url: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
    description: Entrez Programming Utilities (E-utilities), a set of server-side programs
      (EInfo, ESearch, ESummary, EFetch, ELink, EPost, EGQuery, ESpell, ECitMatch) with
      a fixed URL syntax for searching, linking and retrieving records from the 38
      Entrez databases. Results are returned as XML, with JSON available for several
      utilities.
    format: mixed
    id: entrez.eutils
    name: Entrez E-utilities
    original_source:
      - source: entrez
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
      - source: pmc
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: dbsnp
        relation_type: prov:hadPrimarySource
      - source: dbvar
        relation_type: prov:hadPrimarySource
      - source: dbgap
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: gtr
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: gene-expression-omnibus
        relation_type: prov:hadPrimarySource
      - source: sra
        relation_type: prov:hadPrimarySource
      - source: cdd
        relation_type: prov:hadPrimarySource
      - source: genbank
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: pubmed
        relation_type: prov:wasInformedBy
      - source: ncbigene
        relation_type: prov:wasInformedBy
      - source: ncbitaxon
        relation_type: prov:wasInformedBy
    product_url: https://www.ncbi.nlm.nih.gov/books/NBK25501/
  - category: GraphicalInterface
    description: NCBI global cross-database search page, which runs a single query
      against all Entrez databases and reports hit counts per database.
    format: http
    id: entrez.web
    name: Entrez Web Interface
    original_source:
      - source: entrez
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
      - source: pmc
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: dbsnp
        relation_type: prov:hadPrimarySource
      - source: dbvar
        relation_type: prov:hadPrimarySource
      - source: dbgap
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: gtr
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: gene-expression-omnibus
        relation_type: prov:hadPrimarySource
      - source: sra
        relation_type: prov:hadPrimarySource
      - source: cdd
        relation_type: prov:hadPrimarySource
      - source: genbank
        relation_type: prov:hadPrimarySource
    product_url: https://www.ncbi.nlm.nih.gov/search/
  - category: ProgrammingInterface
    description: Entrez Direct (EDirect) command-line tools for Unix systems that wrap
      the E-utilities (esearch, efetch, elink, efilter, xtract and others) for pipeline
      access to Entrez databases.
    format: mixed
    id: entrez.edirect
    name: Entrez Direct (EDirect)
    original_source:
      - source: entrez
        relation_type: prov:hadPrimarySource
      - source: pubmed
        relation_type: prov:hadPrimarySource
      - source: pmc
        relation_type: prov:hadPrimarySource
      - source: ncbigene
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: dbsnp
        relation_type: prov:hadPrimarySource
      - source: dbvar
        relation_type: prov:hadPrimarySource
      - source: dbgap
        relation_type: prov:hadPrimarySource
      - source: medgen
        relation_type: prov:hadPrimarySource
      - source: gtr
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: pubchem
        relation_type: prov:hadPrimarySource
      - source: gene-expression-omnibus
        relation_type: prov:hadPrimarySource
      - source: sra
        relation_type: prov:hadPrimarySource
      - source: cdd
        relation_type: prov:hadPrimarySource
      - source: genbank
        relation_type: prov:hadPrimarySource
    product_url: https://www.ncbi.nlm.nih.gov/books/NBK179288/
    repository: https://github.com/ncbi/entrez-direct
publications:
  - id: doi:10.1093/nar/gkaf1060
    doi: 10.1093/nar/gkaf1060
    title: Database resources of the National Center for Biotechnology Information in 2026
    authors:
      - Sayers EW
      - Bolton EE
      - Fine AM
      - Kelly C
      - Kim S
      - Landrum M
      - Lathrop S
      - Malheiro A
      - Murphy TD
      - Phan L
      - Pujar S
      - Trawick BW
      - Schneider VA
      - Pruitt KD
    journal: Nucleic Acids Research
    year: '2026'
    preferred: true
  - id: doi:10.1016/s0076-6879(96)66012-1
    doi: 10.1016/s0076-6879(96)66012-1
    title: 'Entrez: molecular biology database and retrieval system'
    authors:
      - Schuler GD
      - Epstein JA
      - Ohkawa H
      - Kans JA
    journal: Methods in Enzymology
    year: '1996'
rrid: SCR_016640
synonyms:
  - Entrez
  - NCBI Entrez
  - Entrez Global Query Cross-Database Search System
taxon:
  - NCBITaxon:1
---

# Entrez

## Overview

Entrez is NCBI's primary text search and retrieval system that integrates multiple biological databases including PubMed, GenBank, Gene, Protein, and many others. It provides a unified query interface and retrieval mechanism across NCBI's vast collection of biomedical and genomic data resources.

## Key Features

- **Unified Search**: Single query interface across the 38 Entrez databases
- **Cross-Database Links**: Integrated links between related records in different databases
- **Programmatic Access**: E-utilities API and Entrez Direct command-line tools
- **Advanced Queries**: Boolean operators, field-specific searches, and query history
- **Comprehensive Coverage**: Access to literature, sequences, structures, genomes, and more

## Integrated Databases

As of 2026-10-27 the E-utilities EInfo service lists 38 Entrez databases, including:
- **Literature**: PubMed, PMC, Books, NLM Catalog, MeSH
- **Genes and sequences**: Gene, Nucleotide/Nuccore (GenBank and RefSeq), Protein, Genome, Assembly, SRA, BioProject, BioSample
- **Variation and clinical**: dbSNP, dbVar, ClinVar, dbGaP, MedGen, GTR, OMIM
- **Expression**: GEO DataSets and GEO Profiles
- **Chemicals and structure**: PubChem Compound, Substance and BioAssay; Structure (MMDB); Conserved Domains (CDD)
- **Taxonomy**: NCBI Taxonomy

## Products

### E-utilities API
The Entrez Programming Utilities (E-utilities) provide programmatic access to NCBI databases through a set of server-side programs that accept fixed URL syntax for retrieving data (https://www.ncbi.nlm.nih.gov/books/NBK25501/).

### Entrez Direct (EDirect)
Command-line tools that provide access to NCBI's suite of interconnected databases from a Unix terminal window (https://www.ncbi.nlm.nih.gov/books/NBK179288/).

### Web Interface
The NCBI global cross-database search page (https://www.ncbi.nlm.nih.gov/search/).

## License

NCBI data are generally U.S. Government works without copyright restrictions, but some submitted records may be subject to third-party rights. See the [NCBI Website and Data Usage Policies](https://www.ncbi.nlm.nih.gov/home/about/policies/).

## Citation

Sayers EW, et al. Database resources of the National Center for Biotechnology Information in 2026. Nucleic Acids Research. 2026. doi:10.1093/nar/gkaf1060

Schuler GD, Epstein JA, Ohkawa H, Kans JA. Entrez: molecular biology database and retrieval system. Methods in Enzymology. 1996;266:141-162. doi:10.1016/s0076-6879(96)66012-1

## Information Resource ID

This resource has the Information Resource identifier: `infores:entrez`

RRID: SCR_016640

## Domains

- Biomedical
- Genomics
- Literature

## Taxon Coverage

All organisms (NCBITaxon:1 - root of NCBI Taxonomy)
