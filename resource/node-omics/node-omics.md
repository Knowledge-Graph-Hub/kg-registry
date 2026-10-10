---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.biosino.org/
  label: Bio-Med Big Data Center (BIOSINO), Shanghai Institute of Nutrition and Health,
    Chinese Academy of Sciences
creation_date: '2026-10-04T00:00:00Z'
description: NODE (National Omics Data Encyclopedia) is a Chinese repository for submitting,
  archiving and sharing multi-omics data, including sequencing, proteomics, metabolomics
  and associated metadata, run by the Bio-Med Big Data Center (BIOSINO) of the Shanghai
  Institute of Nutrition and Health, Chinese Academy of Sciences. Data are organized
  as projects (OEP accessions), experiments, samples, runs and analyses, and each
  item is public, restricted (searchable, with download on request to the owner) or
  private. NODE is indexed by OmicsDI.
domains:
- genomics
- proteomics
- metabolomics
- chemistry and biochemistry
- biomedical
homepage_url: https://www.biosino.org/node/
id: node-omics
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
name: National Omics Data Encyclopedia
products:
- category: GraphicalInterface
  description: NODE web portal for submitting, searching, viewing and downloading
    omics projects, experiments, samples, runs and analyses. Public data can be downloaded
    over HTTP from each detail page.
  format: http
  id: node-omics.portal
  name: NODE Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: node-omics
  product_url: https://www.biosino.org/node/
- category: GraphicalInterface
  description: NODE browse and search interface over public and restricted projects,
    experiments, samples and analyses, with lookups for taxonomy, biome, disease and
    platform.
  format: http
  id: node-omics.browse
  name: NODE Browse
  original_source:
  - relation_type: prov:hadPrimarySource
    source: node-omics
  product_url: https://www.biosino.org/node/browse
- category: Product
  description: SFTP service for bulk download of NODE data files (raw reads and analysis
    files), at host fms.biosino.org on port 44398, using a NODE account (email and
    password). Upload uses port 44397.
  format: mixed
  id: node-omics.sftp
  name: NODE SFTP Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: node-omics
  product_url: sftp://fms.biosino.org
  warnings:
  - 'File was not able to be retrieved when checked on 2026-10-10: Error connecting
    to URL: No connection adapters were found for ''sftp://fms.biosino.org'''
  - The SFTP service requires a NODE account and was not tested when checked on 2026-10-04.
    Host and ports are taken from the NODE help pages.
- category: GraphicalInterface
  description: NODE statistics pages summarizing data volume, data flow, popular datasets
    and linked publications.
  format: http
  id: node-omics.statistics
  name: NODE Statistics
  original_source:
  - relation_type: prov:hadPrimarySource
    source: node-omics
  product_url: https://www.biosino.org/node/statistic
- category: DocumentationProduct
  description: NODE help documentation covering registration, metadata and raw data
    submission, data security levels, HTTP and SFTP download, and how to cite NODE
    accessions.
  format: http
  id: node-omics.help
  name: NODE Help Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: node-omics
  product_url: https://www.biosino.org/node/help
- category: GraphicalInterface
  description: Web portal for searching and browsing integrated omics dataset metadata
    across repositories.
  format: http
  id: omicsdi.portal
  name: OmicsDI Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omicsdi
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: metabolights
  - relation_type: prov:hadPrimarySource
    source: ega
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  - relation_type: prov:hadPrimarySource
    source: biomodels
  - relation_type: prov:hadPrimarySource
    source: pride
  - relation_type: prov:hadPrimarySource
    source: iprox
  - relation_type: prov:hadPrimarySource
    source: fairdomhub
  - relation_type: prov:hadPrimarySource
    source: eva
  - relation_type: prov:hadPrimarySource
    source: node-omics
  - relation_type: prov:hadPrimarySource
    source: jpost
  - relation_type: prov:hadPrimarySource
    source: gpmdb
  - relation_type: prov:hadPrimarySource
    source: cellcollective
  - relation_type: prov:hadPrimarySource
    source: ecrin-mdr
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  - relation_type: prov:hadPrimarySource
    source: physiome-model-repository
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  product_url: https://www.omicsdi.org/
- category: ProgrammingInterface
  connection_url: https://www.omicsdi.org/ws
  description: Swagger-documented web service for programmatic querying of OmicsDI
    dataset metadata.
  format: http
  id: omicsdi.api
  is_public: true
  name: OmicsDI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omicsdi
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: metabolights
  - relation_type: prov:hadPrimarySource
    source: ega
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  - relation_type: prov:hadPrimarySource
    source: biomodels
  - relation_type: prov:hadPrimarySource
    source: pride
  - relation_type: prov:hadPrimarySource
    source: iprox
  - relation_type: prov:hadPrimarySource
    source: fairdomhub
  - relation_type: prov:hadPrimarySource
    source: eva
  - relation_type: prov:hadPrimarySource
    source: node-omics
  - relation_type: prov:hadPrimarySource
    source: jpost
  - relation_type: prov:hadPrimarySource
    source: gpmdb
  - relation_type: prov:hadPrimarySource
    source: cellcollective
  - relation_type: prov:hadPrimarySource
    source: ecrin-mdr
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  - relation_type: prov:hadPrimarySource
    source: physiome-model-repository
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  product_url: https://www.omicsdi.org/ws/swagger-ui/index.html
synonyms:
- NODE
- National Omics Data Encyclopedia
---
# National Omics Data Encyclopedia (NODE)

NODE is a multi-omics data repository run by the Bio-Med Big Data Center (BIOSINO) at the Shanghai Institute of Nutrition and Health, Chinese Academy of Sciences. It accepts sequencing, proteomics, metabolomics and other omics data with structured metadata.

## Data Model

Submissions are organized as projects (accessions such as `OEP00000073`), experiments, samples, runs and analyses. Each item carries one of three security levels:

- **Public**: anyone can search, view and download it.
- **Restricted**: it is searchable, and access or download requires a request to the data owner.
- **Private**: it is visible only to the submitter.

Data can only move toward lower security (private to restricted or public, restricted to public).

## Access

The portal is a JavaScript single-page application, so every path under `/node/` returns HTTP 200 even when no such page exists. Public files download over HTTP from the detail pages. Bulk download uses SFTP at `fms.biosino.org` (port 44398) with NODE account credentials. The web application calls an internal JSON API under `https://www.biosino.org/node/api/`, but no public API documentation was found.

## License

NODE states no data license. Access is governed by each dataset's security level.

## Citation

NODE asks users to cite data as "All data are accessible in NODE (https://www.biosino.org/node) with the accession number XXX". Its site cites the article "Advances in multi-omics big data sharing platform research", *Chinese Bulletin of Life Sciences* 2023, 35(12): 1553-1560, DOI 10.13376/j.cbls/2023169. That DOI is not registered with Crossref, so it is not listed as a publication here.

## Related Resources

NODE is indexed by [OmicsDI](https://www.omicsdi.org/).