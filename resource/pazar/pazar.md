---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: pazar@cmmt.ubc.ca
  label: PAZAR Group (Wasserman Lab, Centre for Molecular Medicine and Therapeutics,
    University of British Columbia)
- category: Individual
  label: Wyeth W. Wasserman
creation_date: '2026-11-12T00:00:00Z'
description: PAZAR is an open-access, open-source software framework and database
  for the collection and dissemination of cis-regulatory sequence annotation, including
  experimentally characterized and predicted transcription factor binding sites, regulatory
  sequences and transcription factor to target gene relationships. It works as an
  "information mall" of independently curated "boutique" projects whose curators own
  and release their data, with contributed collections such as ORegAnno, JASPAR CORE
  and NFIRegulome alongside many ChIP-chip and ChIP-seq derived datasets. PAZAR was
  developed by the Wasserman lab at the Centre for Molecular Medicine and Therapeutics
  (University of British Columbia) and offered weekly tab-delimited TF-target gene
  dumps, GFF and XML exports, ChIP-seq peak files and a Perl API. The pazar.info site
  stopped serving the database around 2019 and the domain was later parked; the site
  survives only as Internet Archive Wayback Machine snapshots, and the source code
  remains on SourceForge.
domains:
- genomics
- gene regulation
homepage_url: http://www.pazar.info/
id: pazar
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
name: PAZAR
products:
- category: GraphicalInterface
  description: Archived snapshot of the PAZAR web portal in the Internet Archive Wayback
    Machine, preserved because pazar.info is defunct. The portal supported searching
    by transcription factor, target gene or regulatory sequence (by Ensembl, Entrez
    Gene, RefSeq, Swiss-Prot or PAZAR identifiers) across public boutique projects.
  format: http
  id: pazar.portal
  name: PAZAR web portal (Wayback Machine archive)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pazar
  product_url: https://web.archive.org/web/20170930132649/http://www.pazar.info/
  warnings:
  - The original pazar.info site is no longer operational and the domain has been
    parked; this product points to an Internet Archive Wayback Machine snapshot.
- category: Product
  description: Weekly tab-delimited TF - target gene dumps for each public PAZAR project
    (one CSV file per project, plus a combined tftargets.zip archive), as listed on
    an archived snapshot of the PAZAR downloads page. Projects include data contributed
    from ORegAnno, JASPAR and NFIRegulome.
  format: http
  id: pazar.tf_target_downloads
  name: PAZAR TF - target gene file downloads (Wayback Machine archive)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pazar
  - relation_type: prov:hadPrimarySource
    source: oreganno
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: nfiregulomedb
  product_url: https://web.archive.org/web/20170929231049/http://www.pazar.info/cgi-bin/downloads_csv.pl
  warnings:
  - The original pazar.info site is no longer operational; this product points to
    an Internet Archive Wayback Machine snapshot, and individual data files may not
    all have been archived.
- category: Product
  description: Per-project exports of PAZAR public data in the PAZAR XML exchange
    format, as listed on an archived snapshot of the PAZAR XML downloads page. GFF
    exports were offered on a parallel page.
  format: http
  id: pazar.xml_downloads
  name: PAZAR XML downloads (Wayback Machine archive)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pazar
  product_url: https://web.archive.org/web/20160701080813/http://www.pazar.info/cgi-bin/downloads_xml.pl
  warnings:
  - The original pazar.info site is no longer operational; this product points to
    an Internet Archive Wayback Machine snapshot, and individual data files may not
    all have been archived.
- category: DocumentationProduct
  description: Archived documentation for the PAZAR Perl API (release 0.01, December
    2011), with modules for projects, genes, transcripts, regulatory sequences, transcription
    factors and their targets, and example scripts for retrieving TF-target information.
  format: http
  id: pazar.api_docs
  name: PAZAR API documentation (Wayback Machine archive)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pazar
  product_url: https://web.archive.org/web/20130209063359/http://www.pazar.info:80/apidocs/
  warnings:
  - The original pazar.info site is no longer operational; this product points to
    an Internet Archive Wayback Machine snapshot.
- category: ProcessProduct
  description: PAZAR open-source project on SourceForge, hosting the source code repository,
    file releases, mailing list and discussion forums for the PAZAR framework (last
    updated 2015).
  format: http
  id: pazar.sourceforge
  name: PAZAR SourceForge project
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pazar
  product_url: https://sourceforge.net/projects/pazar/
- category: Product
  description: TFactS catalogues (version 2) as a legacy Excel workbook, recovered
    from an Internet Archive Wayback Machine snapshot of tfacts.org. The workbook
    has a sign-less sheet of about 6,800 transcription factor to target gene pairs,
    with references, species and accessions, and a sign-sensitive sheet of about 3,250
    pairs annotated as up- or down-regulation with PubMed references. Sources include
    TRED and PubMed literature.
  format: http
  id: tfacts.catalogues
  name: TFactS Catalogues (version 2, Wayback Machine archive)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tfacts
  - relation_type: prov:hadPrimarySource
    source: tred
  - relation_type: prov:hadPrimarySource
    source: pazar
  - relation_type: prov:hadPrimarySource
    source: nfiregulomedb
  - relation_type: prov:hadPrimarySource
    source: trrd
  product_url: https://web.archive.org/web/20220617202237/https://www.tfacts.org/TFactS-new/TFactS-v2/tfacts/data/Catalogues.xls
publications:
- authors:
  - Elodie Portales-Casamar
  - Stefan Kirov
  - Jonathan Lim
  - Stuart Lithwick
  - Magdalena I Swanson
  - Amy Ticoll
  - Jay Snoddy
  - Wyeth W Wasserman
  doi: 10.1186/gb-2007-8-10-r207
  id: doi:10.1186/gb-2007-8-10-r207
  journal: Genome Biology
  preferred: true
  title: 'PAZAR: a framework for collection and dissemination of cis-regulatory sequence
    annotation'
  year: '2007'
- authors:
  - Elodie Portales-Casamar
  - David Arenillas
  - Jonathan Lim
  - Magdalena I. Swanson
  - Steven Jiang
  - Anthony McCallum
  - Stefan Kirov
  - Wyeth W. Wasserman
  doi: 10.1093/nar/gkn783
  id: doi:10.1093/nar/gkn783
  journal: Nucleic Acids Research
  title: The PAZAR database of gene regulatory information coupled to the ORCA toolkit
    for the study of regulatory sequences
  year: '2009'
synonyms:
- PAZAR database
warnings:
- The original pazar.info website is no longer operational (the domain was parked
  by 2020). The portal and download pages are available only as Internet Archive
  Wayback Machine snapshots.
---
## Description

**PAZAR** is an open-access, open-source framework and database for
cis-regulatory sequence annotation: transcription factor binding sites,
regulatory sequences and transcription factor to target gene relationships,
both experimentally characterized and predicted. It is organized as an
"information mall" of independently curated "boutique" projects, each owned and
released by its curators. Contributed collections included ORegAnno, JASPAR
CORE and NFIRegulome, plus many ChIP-chip and ChIP-seq derived datasets.

PAZAR was built by the Wasserman lab at the Centre for Molecular Medicine and
Therapeutics, University of British Columbia, and is an upstream source of
**TFactS**. The pazar.info site stopped serving the database around 2019 and the
domain was later parked, so the resource is marked **inactive**. The portal and
download pages survive as Wayback Machine snapshots, and the source code remains
on SourceForge.

## Products

- **PAZAR web portal (Wayback Machine archive)**: search by TF, gene or sequence.
- **PAZAR TF - target gene file downloads (Wayback Machine archive)**: weekly
  per-project tab-delimited dumps.
- **PAZAR XML downloads (Wayback Machine archive)**: per-project XML exports.
- **PAZAR API documentation (Wayback Machine archive)**: Perl API docs.
- **PAZAR SourceForge project**: source code, releases and forums.
