---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://panoramaweb.org/
  - contact_type: github
    value: LabKey
  label: MacCoss Lab, University of Washington
creation_date: '2026-10-04T00:00:00Z'
description: Panorama Public is a ProteomeXchange member repository for quantitative
  mass spectrometry datasets processed in Skyline, covering targeted (SRM/PRM), data
  independent acquisition (DIA) and small molecule experiments. It runs on PanoramaWeb,
  a LabKey Server instance with the Panorama targeted MS modules, hosted by the MacCoss
  Lab at the University of Washington. Each dataset carries its own data license,
  CC BY 4.0 by default or CC0 1.0, and datasets that meet ProteomeXchange requirements
  receive PXD identifiers.
domains:
- proteomics
- biomedical
homepage_url: https://panoramaweb.org/public.url
id: panorama-public
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0 (default per-dataset license; CC0 1.0 also offered)
name: Panorama Public
products:
- category: GraphicalInterface
  description: Panorama Public project page on PanoramaWeb, listing public datasets
    by year with Skyline documents, chromatograms, peptide and small molecule results,
    and links to ProteomeXchange identifiers.
  format: http
  id: panorama-public.portal
  name: Panorama Public Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  product_url: https://panoramaweb.org/project/Panorama%20Public/begin.view
- category: Product
  description: WebDAV root of the Panorama Public project. Each dataset folder holds
    the Skyline documents (.sky.zip) and the raw data files uploaded with it, which
    can be fetched with WebDAV clients such as CyberDuck or WinSCP using the per-dataset
    credentials shown in the Raw Data tab.
  format: mixed
  id: panorama-public.webdav
  name: Panorama Public WebDAV Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  product_url: https://panoramaweb.org/_webdav/Panorama%20Public/
- category: DocumentationProduct
  description: PanoramaWeb documentation for Panorama Public, including how to submit
    Skyline datasets and how ProteomeXchange identifiers are assigned.
  format: http
  id: panorama-public.docs
  name: Panorama Public Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  product_url: https://panoramaweb.org/home/wiki-page.view?name=panorama_public
- category: DocumentationProduct
  description: Instructions for downloading Skyline documents and raw data from public
    datasets, in a web browser or over WebDAV.
  format: http
  id: panorama-public.download-docs
  name: Panorama Public Download Instructions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  product_url: https://panoramaweb.org/wiki/home/page.view?name=download_public_data
- category: ProcessProduct
  description: Source code of the LabKey Server modules behind Panorama Public, including
    the panoramapublic module (submission, ProteomeXchange announcement and data license
    handling) in the MacCossLabModules repository. The targetedms module that stores
    Skyline documents lives in LabKey/targetedms.
  format: java
  id: panorama-public.code
  name: Panorama Public Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  product_url: https://github.com/LabKey/MacCossLabModules/tree/develop/panoramapublic
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
  - Vagisha Sharma
  - Josh Eckels
  - Birgit Schilling
  - Christina Ludwig
  - Jacob D. Jaffe
  - Michael J. MacCoss
  - Brendan MacLean
  doi: 10.1074/mcp.ra117.000543
  id: doi:10.1074/mcp.ra117.000543
  journal: Molecular & Cellular Proteomics
  preferred: true
  title: 'Panorama Public: A Public Repository for Quantitative Data Sets Processed
    in Skyline'
  year: '2018'
repository: https://github.com/LabKey/MacCossLabModules
synonyms:
- PanoramaWeb Public
---
# Panorama Public

Panorama Public is the public data repository on [PanoramaWeb](https://panoramaweb.org/), the hosted instance of the Panorama server application for targeted mass spectrometry. Researchers upload Skyline documents and the associated raw files, and the repository displays chromatograms, peak areas and other results directly in the browser. It accepts targeted (SRM/PRM), DIA and small molecule experiments.

Panorama Public is a member of the ProteomeXchange consortium. Datasets that meet ProteomeXchange submission requirements get a PXD identifier and are announced on ProteomeCentral.

## Access

- Browse datasets on the project page, organized by year and lab.
- Download Skyline documents (`.sky.zip`) from each dataset, and raw data from its Raw Data tab, in a browser or over WebDAV.

## License

Each dataset has a data license chosen at submission. The `panoramapublic` module offers CC BY 4.0, which is the default, and CC0 1.0.

## Related

The Panorama software is described in Sharma et al. 2014, "Panorama: A Targeted Proteomics Knowledge Base" (Journal of Proteome Research, doi:10.1021/pr5006636).