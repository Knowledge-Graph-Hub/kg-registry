---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.proteomexchange.org/contact/
  label: ProteomeXchange Consortium
creation_date: '2026-10-04T00:00:00Z'
description: ProteomeXchange is a consortium of mass spectrometry proteomics data
  repositories (PRIDE, PeptideAtlas/PASSEL, MassIVE, jPOST, iProX and Panorama Public)
  that share common submission and dissemination guidelines and assign PXD accessions
  to public datasets. Its ProteomeCentral portal indexes the datasets announced by
  all member repositories and provides per-dataset XML and JSON records, a full dataset
  listing, and the PROXI web service API.
domains:
- proteomics
- metadata
- information technology
homepage_url: https://www.proteomexchange.org/
id: proteomexchange
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
name: ProteomeXchange
products:
- category: GraphicalInterface
  description: ProteomeXchange consortium website describing member repositories,
    data submission guidelines, subscription options and consortium publications.
  format: http
  id: proteomexchange.portal
  name: ProteomeXchange Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  product_url: https://www.proteomexchange.org/
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
- category: ProgrammingInterface
  connection_url: https://proteomecentral.proteomexchange.org/api/proxi/v0.1/
  description: ProteomeCentral implementation of the PROXI (Proteomics Expression
    Interface) web service, an OpenAPI endpoint for querying datasets, libraries,
    spectra and peptides with filtering, free-text search, facets and pagination.
    The URL points to the Swagger UI documentation.
  format: http
  id: proteomexchange.proxi-api
  is_public: true
  name: ProteomeCentral PROXI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  product_url: https://proteomecentral.proteomexchange.org/api/proxi/v0.1/ui/
- category: Product
  description: RSS feed of announcements of new public ProteomeXchange datasets, published
    through the ProteomeXchange Google group.
  format: xml
  id: proteomexchange.rss
  name: ProteomeXchange Announcements RSS Feed
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  product_url: https://groups.google.com/forum/feed/proteomexchange/msgs/rss_v2_0.xml
  warnings:
  - Feed was not able to be retrieved when checked on 2026-10-04. The URL listed on
    the ProteomeXchange subscription page returned HTTP 404.
- category: DocumentationProduct
  description: ProteomeXchange data submission and dissemination guidelines for partner
    repositories and submitters.
  format: pdf
  id: proteomexchange.guidelines
  name: ProteomeXchange Guidelines
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  product_url: https://www.proteomexchange.org/docs/guidelines_px.pdf
- category: DocumentationProduct
  description: Instructions for submitting datasets to ProteomeXchange through its
    member repositories.
  format: http
  id: proteomexchange.submission-docs
  name: ProteomeXchange Submission Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  product_url: https://www.proteomexchange.org/submission/
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
publications:
- authors:
  - Eric W Deutsch
  - Nuno Bandeira
  - Yasset Perez-Riverol
  - Vagisha Sharma
  - Jeremy J Carver
  - Luis Mendoza
  - Deepti J Kundu
  - Chakradhar Bandla
  - Selvakumar Kamatchinathan
  - Suresh Hewapathirana
  - Zhi Sun
  - Shin Kawano
  - Shujiro Okuda
  - Brian Connolly
  - Brendan MacLean
  - Michael J MacCoss
  - Tao Chen
  - Yunping Zhu
  - Yasushi Ishihama
  - Juan Antonio Vizcaíno
  doi: 10.1093/nar/gkaf1146
  id: doi:10.1093/nar/gkaf1146
  journal: Nucleic Acids Research
  preferred: true
  title: 'The ProteomeXchange consortium in 2026: making proteomics data FAIR'
  year: '2026'
- authors:
  - Eric W Deutsch
  - Nuno Bandeira
  - Yasset Perez-Riverol
  - Vagisha Sharma
  - Jeremy J Carver
  - Luis Mendoza
  - Deepti J Kundu
  - Shengbo Wang
  - Chakradhar Bandla
  - Selvakumar Kamatchinathan
  - Suresh Hewapathirana
  - Benjamin S Pullman
  - Julie Wertz
  - Zhi Sun
  - Shin Kawano
  - Shujiro Okuda
  - Yu Watanabe
  - Brendan MacLean
  - Michael J MacCoss
  - Yunping Zhu
  - Yasushi Ishihama
  - Juan Antonio Vizcaíno
  doi: 10.1093/nar/gkac1040
  id: doi:10.1093/nar/gkac1040
  journal: Nucleic Acids Research
  title: 'The ProteomeXchange consortium at 10 years: 2023 update'
  year: '2023'
- authors:
  - Eric W. Deutsch
  - Attila Csordas
  - Zhi Sun
  - Andrew Jarnuczak
  - Yasset Perez-Riverol
  - Tobias Ternent
  - David S. Campbell
  - Manuel Bernal-Llinares
  - Shujiro Okuda
  - Shin Kawano
  - Robert L. Moritz
  - Jeremy J. Carver
  - Mingxun Wang
  - Yasushi Ishihama
  - Nuno Bandeira
  - Henning Hermjakob
  - Juan Antonio Vizcaíno
  doi: 10.1093/nar/gkw936
  id: doi:10.1093/nar/gkw936
  journal: Nucleic Acids Research
  title: 'The ProteomeXchange consortium in 2017: supporting the cultural change in
    proteomics public data deposition'
  year: '2017'
synonyms:
- PX
- ProteomeCentral
---
# ProteomeXchange

ProteomeXchange is an international consortium of proteomics data repositories, established to standardize the submission and open dissemination of mass spectrometry proteomics data. Its six member repositories are PRIDE (EMBL-EBI), PeptideAtlas/PASSEL (Institute for Systems Biology), MassIVE (UC San Diego), jPOST (Japan), iProX (China) and Panorama Public (University of Washington). Each public dataset receives a PXD accession, and ProteomeXchange resources were named Global Core Biodata Resources in 2022.

## ProteomeCentral

ProteomeCentral is the common portal that indexes datasets announced by all member repositories. It provides:

- A searchable, browsable dataset index and a full dataset listing as TSV.
- Per-dataset announcement records in ProteomeXchange XML or JSON (`/cgi/GetDataset?ID=<PXD>&outputMode=XML|JSON`).
- The PROXI web service API (OpenAPI, `/api/proxi/v0.1/`) for datasets, libraries, spectra and peptides.
- Universal Spectrum Identifier (USI) and Quetzal spectrum viewers.

## Licensing

ProteomeXchange does not state a single license for the consortium. According to the 2026 update paper, most member repositories assign CC0 to datasets by default, while Panorama Public uses CC BY with CC0 available.