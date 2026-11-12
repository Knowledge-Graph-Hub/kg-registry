---
activity_status: active
category: DataSource
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: zasha@bioinf.uni-leipzig.de
      - contact_type: url
        value: https://zashaweinberglab.org/
    label: Zasha Weinberg
creation_date: '2025-10-29T00:00:00Z'
curators:
  - category: Individual
    contact_details:
      - contact_type: url
        value: https://bitbucket.org/zashaw/
    label: Zasha Weinberg
description: Zasha Weinberg Data (ZWD) is a git-based collection of multiple sequence alignments of structured non-coding RNAs (and some ssDNA) from comparative genomics work by Zasha Weinberg and colleagues, including candidate structured RNAs, riboswitch classes and their variants, self-cleaving ribozymes and other conserved RNA motifs, mostly from bacteria and metagenomes. Each subdirectory holds the Stockholm-format alignments from one publication, with a secondary-structure consensus line in Rfam conventions. Most alignments were submitted to Rfam, and ZWD is an RNAcentral expert database.
domains:
  - genomics
  - non-coding RNA
  - microbiology
homepage_url: https://bitbucket.org/zashaw/zashaweinbergdata/src/master/
id: zwd
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
name: Zasha Weinberg Data
products:
  - category: Product
    description: Stockholm-format multiple sequence alignments of structured RNA and ssDNA motifs, organized in one subdirectory per publication, with consensus secondary structure (including pseudoknots) and, for riboswitch variants, annotation of the key ligand-binding nucleotides. Sequence names use RefSeq or environmental metagenomic accessions.
    format: stockholm
    id: zwd.alignments
    name: Zasha Weinberg Data Repository Sequence Alignments
    product_url: https://bitbucket.org/zashaw/zashaweinbergdata/src/master/
    original_source:
      - source: zwd
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
  - category: MappingProduct
    description: Tab-delimited mapping of the sequence accessions used in the ZWD alignments to NCBI Taxonomy IDs, with -1 where the accession is not in RefSeq.
    format: tsv
    id: zwd.seqid-taxid
    name: ZWD Sequence Accession to NCBI Taxonomy Mapping
    product_url: https://bitbucket.org/zashaw/zashaweinbergdata/raw/master/sto-seqid-taxid.tab
    original_source:
      - source: zwd
        relation_type: prov:hadPrimarySource
      - source: refseq
        relation_type: prov:hadPrimarySource
      - source: ncbitaxon
        relation_type: prov:hadPrimarySource
  - category: GraphicalInterface
    description: Web portal for searching and browsing ncRNA sequences, structures, and annotations
    format: http
    id: rnacentral.portal
    name: RNAcentral Portal
    original_source:
      - source: 5srrnadb
        relation_type: prov:hadPrimarySource
      - source: crd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: ena
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: evlncrnas
        relation_type: prov:hadPrimarySource
      - source: expressionatlas
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: genecards
        relation_type: prov:hadPrimarySource
      - source: greengenes
        relation_type: prov:hadPrimarySource
      - source: gtrnadb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: lncbase
        relation_type: prov:hadPrimarySource
      - source: lncbook
        relation_type: prov:hadPrimarySource
      - source: lncipedia
        relation_type: prov:hadPrimarySource
      - source: lncrnadb
        relation_type: prov:hadPrimarySource
      - source: malacards
        relation_type: prov:hadPrimarySource
      - source: mgnify
        relation_type: prov:hadPrimarySource
      - source: mirbase
        relation_type: prov:hadPrimarySource
      - source: mirgenedb
        relation_type: prov:hadPrimarySource
      - source: modomics
        relation_type: prov:hadPrimarySource
      - source: noncode
        relation_type: prov:hadPrimarySource
      - source: pdbe
        relation_type: prov:hadPrimarySource
      - source: pirbase
        relation_type: prov:hadPrimarySource
      - source: plncdb
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: rdp
        relation_type: prov:hadPrimarySource
      - source: rediportal
        relation_type: prov:hadPrimarySource
      - source: rfam
        relation_type: prov:hadPrimarySource
      - source: rgd
        relation_type: prov:hadPrimarySource
      - source: ribocentre
        relation_type: prov:hadPrimarySource
      - source: ribovision
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: silva
        relation_type: prov:hadPrimarySource
      - source: snodb
        relation_type: prov:hadPrimarySource
      - source: snopy
        relation_type: prov:hadPrimarySource
      - source: snornadatabase
        relation_type: prov:hadPrimarySource
      - source: srpdb
        relation_type: prov:hadPrimarySource
      - source: tair
        relation_type: prov:hadPrimarySource
      - source: tarbase
        relation_type: prov:hadPrimarySource
      - source: tmrnawebsite
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
      - source: zwd
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
    product_url: https://rnacentral.org/
  - category: ProgrammingInterface
    description: REST API for programmatic access to RNAcentral data
    format: http
    id: rnacentral.api
    name: RNAcentral REST API
    original_source:
      - source: 5srrnadb
        relation_type: prov:hadPrimarySource
      - source: crd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: ena
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: evlncrnas
        relation_type: prov:hadPrimarySource
      - source: expressionatlas
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: genecards
        relation_type: prov:hadPrimarySource
      - source: greengenes
        relation_type: prov:hadPrimarySource
      - source: gtrnadb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: lncbase
        relation_type: prov:hadPrimarySource
      - source: lncbook
        relation_type: prov:hadPrimarySource
      - source: lncipedia
        relation_type: prov:hadPrimarySource
      - source: lncrnadb
        relation_type: prov:hadPrimarySource
      - source: malacards
        relation_type: prov:hadPrimarySource
      - source: mgnify
        relation_type: prov:hadPrimarySource
      - source: mirbase
        relation_type: prov:hadPrimarySource
      - source: mirgenedb
        relation_type: prov:hadPrimarySource
      - source: modomics
        relation_type: prov:hadPrimarySource
      - source: noncode
        relation_type: prov:hadPrimarySource
      - source: pdbe
        relation_type: prov:hadPrimarySource
      - source: pirbase
        relation_type: prov:hadPrimarySource
      - source: plncdb
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: rdp
        relation_type: prov:hadPrimarySource
      - source: rediportal
        relation_type: prov:hadPrimarySource
      - source: rfam
        relation_type: prov:hadPrimarySource
      - source: rgd
        relation_type: prov:hadPrimarySource
      - source: ribocentre
        relation_type: prov:hadPrimarySource
      - source: ribovision
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: silva
        relation_type: prov:hadPrimarySource
      - source: snodb
        relation_type: prov:hadPrimarySource
      - source: snopy
        relation_type: prov:hadPrimarySource
      - source: snornadatabase
        relation_type: prov:hadPrimarySource
      - source: srpdb
        relation_type: prov:hadPrimarySource
      - source: tair
        relation_type: prov:hadPrimarySource
      - source: tarbase
        relation_type: prov:hadPrimarySource
      - source: tmrnawebsite
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
      - source: zwd
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
    product_url: https://rnacentral.org/api
  - category: Product
    description: FTP archive with current and archived release files (sequences and annotations)
    format: http
    id: rnacentral.ftp
    name: RNAcentral FTP Archive
    original_source:
      - source: 5srrnadb
        relation_type: prov:hadPrimarySource
      - source: crd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: ena
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: evlncrnas
        relation_type: prov:hadPrimarySource
      - source: expressionatlas
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: genecards
        relation_type: prov:hadPrimarySource
      - source: greengenes
        relation_type: prov:hadPrimarySource
      - source: gtrnadb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: lncbase
        relation_type: prov:hadPrimarySource
      - source: lncbook
        relation_type: prov:hadPrimarySource
      - source: lncipedia
        relation_type: prov:hadPrimarySource
      - source: lncrnadb
        relation_type: prov:hadPrimarySource
      - source: malacards
        relation_type: prov:hadPrimarySource
      - source: mgnify
        relation_type: prov:hadPrimarySource
      - source: mirbase
        relation_type: prov:hadPrimarySource
      - source: mirgenedb
        relation_type: prov:hadPrimarySource
      - source: modomics
        relation_type: prov:hadPrimarySource
      - source: noncode
        relation_type: prov:hadPrimarySource
      - source: pdbe
        relation_type: prov:hadPrimarySource
      - source: pirbase
        relation_type: prov:hadPrimarySource
      - source: plncdb
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: rdp
        relation_type: prov:hadPrimarySource
      - source: rediportal
        relation_type: prov:hadPrimarySource
      - source: rfam
        relation_type: prov:hadPrimarySource
      - source: rgd
        relation_type: prov:hadPrimarySource
      - source: ribocentre
        relation_type: prov:hadPrimarySource
      - source: ribovision
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: silva
        relation_type: prov:hadPrimarySource
      - source: snodb
        relation_type: prov:hadPrimarySource
      - source: snopy
        relation_type: prov:hadPrimarySource
      - source: snornadatabase
        relation_type: prov:hadPrimarySource
      - source: srpdb
        relation_type: prov:hadPrimarySource
      - source: tair
        relation_type: prov:hadPrimarySource
      - source: tarbase
        relation_type: prov:hadPrimarySource
      - source: tmrnawebsite
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
      - source: zwd
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
    product_url: https://ftp.ebi.ac.uk/pub/databases/RNAcentral
  - category: DataModelProduct
    description: Public PostgreSQL database for direct SQL access to RNAcentral data
    format: postgres
    id: rnacentral.public-db
    name: RNAcentral Public Postgres Database
    original_source:
      - source: 5srrnadb
        relation_type: prov:hadPrimarySource
      - source: crd
        relation_type: prov:hadPrimarySource
      - source: dictybase
        relation_type: prov:hadPrimarySource
      - source: ena
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: evlncrnas
        relation_type: prov:hadPrimarySource
      - source: expressionatlas
        relation_type: prov:hadPrimarySource
      - source: flybase
        relation_type: prov:hadPrimarySource
      - source: genecards
        relation_type: prov:hadPrimarySource
      - source: greengenes
        relation_type: prov:hadPrimarySource
      - source: gtrnadb
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: lncbase
        relation_type: prov:hadPrimarySource
      - source: lncbook
        relation_type: prov:hadPrimarySource
      - source: lncipedia
        relation_type: prov:hadPrimarySource
      - source: lncrnadb
        relation_type: prov:hadPrimarySource
      - source: malacards
        relation_type: prov:hadPrimarySource
      - source: mgnify
        relation_type: prov:hadPrimarySource
      - source: mirbase
        relation_type: prov:hadPrimarySource
      - source: mirgenedb
        relation_type: prov:hadPrimarySource
      - source: modomics
        relation_type: prov:hadPrimarySource
      - source: noncode
        relation_type: prov:hadPrimarySource
      - source: pdbe
        relation_type: prov:hadPrimarySource
      - source: pirbase
        relation_type: prov:hadPrimarySource
      - source: plncdb
        relation_type: prov:hadPrimarySource
      - source: pombase
        relation_type: prov:hadPrimarySource
      - source: rdp
        relation_type: prov:hadPrimarySource
      - source: rediportal
        relation_type: prov:hadPrimarySource
      - source: rfam
        relation_type: prov:hadPrimarySource
      - source: rgd
        relation_type: prov:hadPrimarySource
      - source: ribocentre
        relation_type: prov:hadPrimarySource
      - source: ribovision
        relation_type: prov:hadPrimarySource
      - source: sgd
        relation_type: prov:hadPrimarySource
      - source: silva
        relation_type: prov:hadPrimarySource
      - source: snodb
        relation_type: prov:hadPrimarySource
      - source: snopy
        relation_type: prov:hadPrimarySource
      - source: snornadatabase
        relation_type: prov:hadPrimarySource
      - source: srpdb
        relation_type: prov:hadPrimarySource
      - source: tair
        relation_type: prov:hadPrimarySource
      - source: tarbase
        relation_type: prov:hadPrimarySource
      - source: tmrnawebsite
        relation_type: prov:hadPrimarySource
      - source: zfin
        relation_type: prov:hadPrimarySource
      - source: zwd
        relation_type: prov:hadPrimarySource
      - source: rnacentral
        relation_type: prov:hadPrimarySource
    product_url: https://rnacentral.org/help/public-database
publications:
  - authors:
      - Weinberg Z
      - Lünse CE
      - Corbino KA
      - Ames TD
      - Nelson JW
      - Roth A
      - Perkins KR
      - Sherlock ME
      - Breaker RR
    doi: 10.1093/nar/gkx699
    id: doi:10.1093/nar/gkx699
    journal: Nucleic Acids Research
    preferred: true
    title: Detection of 224 candidate structured RNAs by comparative analysis of specific subsets of intergenic regions
    year: '2017'
repository: https://bitbucket.org/zashaw/zashaweinbergdata
synonyms:
  - ZWD
  - ZashaWeinbergData
---

# Zasha Weinberg Data

Zasha Weinberg Data (ZWD) is a git repository on Bitbucket of multiple sequence alignments of structured RNA (and some ssDNA) motifs from comparative genomics work by Zasha Weinberg and colleagues. It covers candidate structured RNAs found in bacterial intergenic regions and metagenomes, riboswitch classes and their ligand-binding variants, self-cleaving ribozymes and other conserved motifs.

## Contents

- Each subdirectory holds the alignments from one publication; the tab-delimited `PAPERS` file links each subdirectory to its PubMed record. The `patches` directory holds rough, unpublished alignments of known RNAs that were used to annotate more homologs.
- All alignments are in Stockholm format and follow Rfam conventions: a `#=GC SS_cons` consensus structure line (pseudoknots as matching upper- and lower-case letters) and sequence names of the form `SEQID/START-END`, where the accessions come from RefSeq or environmental metagenomic sequence collections.
- Alignments in `variants` also mark the "key" (presumed ligand-binding) nucleotides with `#=GC CORE` and `#=GF CORESEQ` lines.
- `sto-seqid-taxid.tab` maps the sequence accessions used in the alignments to NCBI Taxonomy IDs.
- `not-for-Rfam` lists alignments that were not submitted to Rfam because their biological function was considered ambiguous, and `CHANGES.txt` records changes made after publication.

## Integration

Most ZWD alignments were submitted to Rfam. ZWD is also an RNAcentral expert database, so its sequences can be searched through the RNAcentral portal, API, FTP archive and public PostgreSQL database.

## Citation

RNAcentral cites Weinberg et al. (2017), "Detection of 224 candidate structured RNAs by comparative analysis of specific subsets of intergenic regions", Nucleic Acids Research, doi:10.1093/nar/gkx699, as the reference for ZWD. Each subdirectory has its own source publication, listed in `PAPERS`.
