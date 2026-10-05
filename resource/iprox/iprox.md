---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.iprox.cn/
  label: Beijing Proteome Research Center
creation_date: '2026-10-04T00:00:00Z'
description: iProX (integrated Proteome resources) is a public repository for mass
  spectrometry-based proteomics data, hosted in China by the Beijing Proteome Research
  Center and a member of the ProteomeXchange consortium. It accepts submissions, assigns
  IPX project accessions alongside ProteomeXchange PXD accessions, and serves dataset
  metadata and files through a web portal, RESTful web services and Aspera. Datasets
  submitted since 2023-03-23 are released under CC0 and earlier datasets under CC
  BY 4.0.
domains:
- proteomics
homepage_url: https://www.iprox.cn/
id: iprox
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.iprox.org/page/iproxDataLisence.html
  label: CC0 1.0 (datasets submitted since 2023-03-23); CC BY 4.0 (earlier datasets)
name: iProX
products:
- category: GraphicalInterface
  description: iProX web portal for submitting, searching and downloading proteomics
    datasets.
  format: http
  id: iprox.portal
  name: iProX Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iprox
  product_url: https://www.iprox.cn/
- category: GraphicalInterface
  description: Browser for public iProX projects, with project metadata, sample and
    instrument descriptions and file listings for each IPX accession.
  format: http
  id: iprox.projects
  name: iProX Project Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iprox
  product_url: https://www.iprox.cn/page/project.html
- category: ProgrammingInterface
  description: iProX RESTful web services (JSONP) that list the data files of a project,
    or the projects and project XML files released on a given day, month or year.
    Bulk file download is then done with Aspera (ascp) against download.iprox.org
    using an iProX account.
  format: http
  id: iprox.api
  name: iProX Web Service API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iprox
  product_url: https://www.iprox.cn/page/helpApi.html
- category: DocumentationProduct
  description: iProX Data Use Agreement, stating the CC0 and CC BY 4.0 terms for deposited
    datasets and the terms of use of the site.
  format: http
  id: iprox.data-license
  name: iProX Data Use Agreement
  original_source:
  - relation_type: prov:hadPrimarySource
    source: iprox
  product_url: https://www.iprox.org/page/iproxDataLisence.html
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
- category: GraphicalInterface
  description: ProteomeCentral, the central index of ProteomeXchange datasets announced
    by all member repositories, with search, filtering and browsing of datasets and
    spectral libraries, plus USI and Quetzal spectrum viewers.
  format: http
  id: proteomexchange.proteomecentral
  name: ProteomeCentral
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: pride
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  - relation_type: prov:hadPrimarySource
    source: jpost
  - relation_type: prov:hadPrimarySource
    source: iprox
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  product_url: https://proteomecentral.proteomexchange.org/
- category: Product
  description: Full tab-separated listing of all public ProteomeXchange datasets (about
    57,000 rows when checked on 2026-10-04), with identifier, title, repository, species,
    instrument, publication, lab head, announcement date and keywords. Some cells
    contain HTML anchor markup.
  format: tsv
  id: proteomexchange.dataset-list
  name: ProteomeXchange Dataset Listing
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: pride
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  - relation_type: prov:hadPrimarySource
    source: jpost
  - relation_type: prov:hadPrimarySource
    source: iprox
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  product_url: https://proteomecentral.proteomexchange.org/cgi/GetDataset?outputMode=tsv
- category: Product
  description: Per-dataset ProteomeXchange announcement records retrieved by PXD accession
    from ProteomeCentral, available as ProteomeXchange XML (outputMode=XML) or JSON
    (outputMode=JSON). The URL shows dataset PXD000001 as an example.
  format: xml
  id: proteomexchange.dataset-records
  name: ProteomeXchange Dataset Records
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: pride
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  - relation_type: prov:hadPrimarySource
    source: jpost
  - relation_type: prov:hadPrimarySource
    source: iprox
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  product_url: https://proteomecentral.proteomexchange.org/cgi/GetDataset?ID=PXD000001&outputMode=XML
publications:
- authors:
  - Jie Ma
  - Tao Chen
  - Songfeng Wu
  - Chunyuan Yang
  - Mingze Bai
  - Kunxian Shu
  - Kenli Li
  - Guoqing Zhang
  - Zhong Jin
  - Fuchu He
  - Henning Hermjakob
  - Yunping Zhu
  doi: 10.1093/nar/gky869
  id: doi:10.1093/nar/gky869
  journal: Nucleic Acids Research
  preferred: true
  title: 'iProX: an integrated proteome resource'
  year: '2019'
- authors:
  - Tao Chen
  - Jie Ma
  - Yi Liu
  - Zhiguang Chen
  - Nong Xiao
  - Yutong Lu
  - Yinjin Fu
  - Chunyuan Yang
  - Mansheng Li
  - Songfeng Wu
  - Xue Wang
  - Dongsheng Li
  - Fuchu He
  - Henning Hermjakob
  - Yunping Zhu
  doi: 10.1093/nar/gkab1081
  id: doi:10.1093/nar/gkab1081
  journal: Nucleic Acids Research
  title: 'iProX in 2021: connecting proteomics data sharing with big data'
  year: '2022'
synonyms:
- integrated Proteome resources
---
# iProX

iProX (integrated Proteome resources) is a public repository for mass spectrometry-based proteomics data. It is hosted by the Beijing Proteome Research Center in China and is a member of the ProteomeXchange consortium, so its public datasets carry PXD accessions in addition to iProX's own IPX project accessions.

## Access

- **Web portal and project browser**: search, view and download public projects.
- **Web services**: JSONP endpoints list a project's data files, or the projects and project XML files released on a given day, month or year.
- **Aspera**: bulk downloads use `ascp` against `download.iprox.org` with an iProX account, as described on the API help page.

Many help pages on the site redirect to a login page. The API help page and the Data Use Agreement are public.

## License

Per the iProX Data Use Agreement, datasets submitted since 2023-03-23 are released under CC0 1.0 and datasets deposited before then under CC BY 4.0.

## Related resources

iProX also hosts data from the Chinese Human Proteome Project (CNHPP), which has its own data license page. iProX datasets are indexed by [OmicsDI](https://www.omicsdi.org/).