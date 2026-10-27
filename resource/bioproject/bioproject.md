---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/bioproject/
  label: National Center for Biotechnology Information (NCBI)
creation_date: '2026-10-27T00:00:00Z'
description: BioProject is NCBI's database of biological research projects. A BioProject
  is a collection of biological data related to a single initiative, originating from
  a single organization or from a consortium, and its record provides a single place
  to find links to the diverse data types generated for that project in NCBI archives
  such as SRA, GenBank, GEO, dbGaP, and Assembly. It replaced the earlier Genome Project
  database. BioProject accessions (PRJNA, and PRJEB and PRJDB through the INSDC partners
  ENA and DDBJ) organize submissions from single studies to large consortia.
domains:
- genomics
- metadata
- information technology
- biomedical
homepage_url: https://www.ncbi.nlm.nih.gov/bioproject/
id: bioproject
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/home/about/policies/
  label: NCBI usage policies
name: NCBI BioProject
products:
- category: GraphicalInterface
  description: Entrez BioProject search over research project records and their links
    to data in other NCBI archives.
  format: http
  id: bioproject.web
  name: BioProject Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioproject
  product_url: https://www.ncbi.nlm.nih.gov/bioproject/
- category: Product
  description: Bulk BioProject records in XML and summary files.
  format: xml
  id: bioproject.ftp
  name: BioProject FTP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioproject
  product_url: https://ftp.ncbi.nlm.nih.gov/bioproject/
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
- BioProject
---
# NCBI BioProject

## Overview

BioProject is NCBI's database of research projects. A BioProject is a collection of biological data related to a single initiative, from a single organization or a consortium. Its record links the data that project generated across NCBI archives such as SRA, GenBank, GEO, dbGaP, and Assembly. On 2026-10-27 it held about 1.11 million records.

## Access

- Entrez BioProject search, also reachable through the E-utilities (`db=bioproject`).
- Bulk XML records and summary files on the NCBI FTP site.

## Citation

Barrett T, Clark K, Gevorgyan R, Gorelenkov V, et al. BioProject and BioSample databases at NCBI: facilitating capture and organization of metadata. Nucleic Acids Res. 2012. doi:10.1093/nar/gkr1163
