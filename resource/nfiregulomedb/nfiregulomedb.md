---
activity_status: inactive
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: rgron@buffalo.edu
  label: Richard M. Gronostajski
creation_date: '2026-11-12T00:00:00Z'
description: NFIregulomeDB (the NFI-Regulome Database) is a literature-curated database
  of the promoter and enhancer regions of genes regulated by the Nuclear Factor I
  (NFI) family of transcription factors. Each control region is annotated with transcription
  and translation start sites, NFI binding sites and the sites of other known or unknown
  transcription factors, placed on the gene sequence obtained from the UCSC Genome
  Browser. Genes can be searched by transcription factor family, gene, tissue of expression
  or disease, and the relative locations and numbers of binding sites across sets
  of genes can be displayed and compared. The database covers human, mouse and rat
  genes and was built by the Gronostajski lab at the University at Buffalo (State
  University of New York); its data were also contributed to ORegAnno and appear as
  a project in PAZAR. The original site at nfiregulome.ccr.buffalo.edu no longer
  responds and survives only as Internet Archive Wayback Machine snapshots.
domains:
- genomics
- gene regulation
homepage_url: http://nfiregulome.ccr.buffalo.edu/
id: nfiregulomedb
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
name: NFIregulomeDB
products:
- category: GraphicalInterface
  description: Archived snapshot of the NFIRegulomeDB gene search interface in the
    Internet Archive Wayback Machine, preserved because the original site is defunct.
    The interface found genes regulated by selected transcription factor families
    or retrieved annotated control regions by gene name.
  format: http
  id: nfiregulomedb.portal
  name: NFIRegulomeDB web interface (Wayback Machine archive)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nfiregulomedb
  - relation_type: prov:hadPrimarySource
    source: ucsc
  product_url: https://web.archive.org/web/20150321060046/http://nfiregulome.ccr.buffalo.edu/basicquery1.0.php
  warnings:
  - The original nfiregulome.ccr.buffalo.edu site is no longer reachable; this product
    points to an Internet Archive Wayback Machine snapshot.
- category: DocumentationProduct
  description: Archived NFIRegulomeDB About page describing the purpose, annotation
    system and analysis functions of the database, with links to a downloadable public
    version of the database source, a user guide, and the NFIRegulomeDB dataset in
    ORegAnno (OREGDS00015).
  format: http
  id: nfiregulomedb.about
  name: NFIRegulomeDB About page (Wayback Machine archive)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nfiregulomedb
  product_url: https://web.archive.org/web/20151009100812/http://nfiregulome.ccr.buffalo.edu/about.php
  warnings:
  - The original nfiregulome.ccr.buffalo.edu site is no longer reachable; this product
    points to an Internet Archive Wayback Machine snapshot. The linked database download
    and user guide were not archived.
- category: DocumentationProduct
  description: Peer-reviewed publication describing the NFI-Regulome database, its
    data model and its tools for annotating and comparing the control regions of
    NFI-regulated genes. Serves as the authoritative reference now that the website
    is defunct.
  format: http
  id: nfiregulomedb.publication
  name: NFI-Regulome Database publication (Journal of Clinical Bioinformatics, 2011)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nfiregulomedb
  product_url: https://doi.org/10.1186/2043-9113-1-4
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
  - Gronostajski RM
  - Guaneri J
  - Lee D
  - Gallo SM
  doi: 10.1186/2043-9113-1-4
  id: doi:10.1186/2043-9113-1-4
  journal: Journal of Clinical Bioinformatics
  preferred: true
  title: 'The NFI-Regulome Database: A tool for annotation and analysis of control
    regions of genes regulated by Nuclear Factor I transcription factors'
  year: '2011'
synonyms:
- NFI-Regulome Database
- NFIRegulomeDB
- NFI Regulome
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
- NCBITaxon:10116
warnings:
- The original website at nfiregulome.ccr.buffalo.edu is no longer reachable. The
  interface is available only as Internet Archive Wayback Machine snapshots.
---
## Description

**NFIregulomeDB** (the NFI-Regulome Database) is a literature-curated database
of the control regions (promoters and enhancers) of genes regulated by the
Nuclear Factor I (NFI) family of transcription factors. Binding sites for NFI
and other transcription factors, plus transcription and translation start
sites, are annotated on gene sequences taken from the UCSC Genome Browser. Users
can compare the layout of binding sites across genes grouped by expression
pattern, disease involvement or binding-site type. Human, mouse and rat genes
are covered.

The database was built by the Gronostajski lab at the University at Buffalo
(SUNY). Its data were contributed to ORegAnno and appear as a project in PAZAR,
and it is an upstream source of **TFactS**. The original site no longer
responds, so the resource is marked **inactive**. It survives as Wayback
Machine snapshots.

## Products

- **NFIRegulomeDB web interface (Wayback Machine archive)**: gene search.
- **NFIRegulomeDB About page (Wayback Machine archive)**: description and links.
- **NFI-Regulome Database publication (2011)**: the reference paper.
