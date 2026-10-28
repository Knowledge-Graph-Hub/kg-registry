---
activity_status: unresponsive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://publichealth.jhu.edu/faculty/4036/hongkai-ji
  label: Ji Lab, Johns Hopkins Bloomberg School of Public Health
creation_date: '2026-10-19T00:00:00Z'
description: hmChIP is a database and web server for exploring publicly available
  genome-wide chromatin immunoprecipitation (ChIP-seq and ChIP-chip) data in human
  and mouse. Users query the database to retrieve protein-DNA binding intensities
  from individual samples for user-supplied genomic regions, and cluster samples and
  regions to compare binding patterns across cell types. At publication (2011) it
  held 2,016 samples from 492 experiments covering 170 proteins. The web server and
  download pages were unreachable (HTTP 500 and HTTP 403) when checked in October
  2026.
domains:
- gene regulation
- genomics
homepage_url: http://jilab.biostat.jhsph.edu/database/cgi-bin/hmChIP.pl
id: hmchip
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
name: hmChIP
products:
- category: Product
  description: HTRIdb download page offering all transcription factor-target gene
    interactions (optionally with associated protein-protein interactions), with experimental
    techniques and PubMed IDs, as tab-delimited or spreadsheet files. Interactions
    were manually curated from the literature (found through PubMed searches) and
    from ChIP-chip and ChIP-seq studies selected via the hmChIP database. The site
    did not respond when checked on 2026-10-19.
  format: http
  id: htridb.downloads
  name: HTRIdb Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: htridb
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:wasDerivedFrom
    source: hmchip
  product_url: http://www.lbbc.ibb.unesp.br/htri/pagdown.jsp
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: ncbigene
  warnings:
  - Site did not respond (connection timed out) when checked on 2026-10-19; the last
    Internet Archive snapshot is from 2022-08-17.
  - 'File was not able to be retrieved when checked on 2026-10-28: Timeout connecting
    to URL'
- category: GraphicalInterface
  description: Web server and query interface to the hmChIP database, retrieving protein-DNA
    binding intensities from individual human and mouse ChIP-seq and ChIP-chip samples
    for user-supplied genomic regions, with clustering of samples and regions. The
    server returned HTTP 500 and was unreachable when checked in October 2026.
  format: http
  id: hmchip.webserver
  name: hmChIP Web Server
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hmchip
  product_url: http://jilab.biostat.jhsph.edu/database/cgi-bin/hmChIP.pl
publications:
- authors:
  - Li Chen
  - George Wu
  - Hongkai Ji
  doi: 10.1093/bioinformatics/btr156
  id: doi:10.1093/bioinformatics/btr156
  journal: Bioinformatics
  preferred: true
  title: 'hmChIP: a database and web server for exploring publicly available human
    and mouse ChIP-seq and ChIP-chip data'
  year: '2011'
rrid: SCR_005407
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
---
# hmChIP

## Overview

hmChIP is a database and web server for publicly available human and mouse ChIP-seq and ChIP-chip data. It stores curated protein-DNA binding data so that users can retrieve binding intensities for individual samples over supplied genomic regions and compare binding patterns across experiments, cell types, and proteins. At its 2011 publication the database held 2,016 samples from 492 experiments covering 170 proteins.

## Access

- Web server: query interface for binding intensities over user-supplied regions (returned HTTP 500 and was unreachable when checked in October 2026).
- Bulk downloads: curated sample data and protein-DNA interaction tables (download page returned HTTP 403 when checked in October 2026).

The resource appears unmaintained since 2011 and is recorded here with an activity status of unresponsive.

## Citation

Please cite: Chen L, Wu G, Ji H. hmChIP: a database and web server for exploring publicly available human and mouse ChIP-seq and ChIP-chip data. Bioinformatics. 2011;27(10):1447–1448. doi:10.1093/bioinformatics/btr156