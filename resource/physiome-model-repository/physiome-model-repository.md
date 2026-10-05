---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: help@physiomeproject.org
  - contact_type: url
    value: https://models.physiomeproject.org/about/contact
  - contact_type: github
    value: PMR2
  label: Auckland Bioengineering Institute, University of Auckland (IUPS Physiome
    Project)
creation_date: '2026-10-04T00:00:00Z'
description: The Physiome Model Repository (PMR) is the IUPS Physiome Project's open
  repository of mathematical models of physiology, run by the Auckland Bioengineering
  Institute. It hosts CellML models (the CellML Model Repository) along with FieldML
  and SED-ML files in version-controlled Git workspaces, and publishes curated, annotated
  views of them as exposures. On 2026-10-04 its JSON listings held 1,303 workspaces
  and 1,108 exposures. Public content is licensed under CC BY 3.0.
domains:
- systems biology
- biological systems
homepage_url: https://models.physiomeproject.org/
id: physiome-model-repository
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
name: Physiome Model Repository
products:
- category: GraphicalInterface
  description: Web portal for searching, browsing and downloading physiology models,
    with model views, curation status and links to simulation in OpenCOR.
  format: http
  id: physiome-model-repository.portal
  name: Physiome Model Repository Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: physiome-model-repository
  product_url: https://models.physiomeproject.org/
- category: GraphicalInterface
  description: Listing of exposures, the published and annotated views of CellML,
    FieldML and SED-ML models, each tied to a specific workspace revision, with model
    documentation, metadata and downloads.
  format: http
  id: physiome-model-repository.exposures
  name: PMR Exposures
  original_source:
  - relation_type: prov:hadPrimarySource
    source: physiome-model-repository
  product_url: https://models.physiomeproject.org/exposure
- category: Product
  description: Listing of version-controlled model workspaces. Each workspace is a
    Git repository holding model files (CellML, FieldML, SED-ML, documentation) that
    can be cloned with git clone using the workspace URI.
  format: mixed
  id: physiome-model-repository.workspaces
  name: PMR Workspaces
  original_source:
  - relation_type: prov:hadPrimarySource
    source: physiome-model-repository
  product_url: https://models.physiomeproject.org/workspace
- category: ProgrammingInterface
  description: JSON web service on the same URLs as the portal. Sending the header
    Accept application/vnd.physiome.pmr2.json.1 returns Collection+JSON hypermedia
    for workspaces, exposures and search; application/vnd.physiome.pmr2.json.0 returns
    plain JSON lists.
  format: json
  id: physiome-model-repository.api
  name: PMR2 JSON Web Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: physiome-model-repository
  product_url: https://aucklandphysiomerepository.readthedocs.io/en/latest/webservice.html
- category: DocumentationProduct
  description: PMR user documentation covering workspaces, exposures, CellML curation,
    semantic metadata and the web service.
  format: http
  id: physiome-model-repository.docs
  name: PMR User Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: physiome-model-repository
  product_url: https://aucklandphysiomerepository.readthedocs.io/en/latest/
- category: ProcessProduct
  description: Source code for PMR2, the Plone-based repository software with Git
    workspace storage that runs the Physiome Model Repository.
  format: python
  id: physiome-model-repository.code
  name: PMR2 Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: physiome-model-repository
  product_url: https://github.com/PMR2
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
    source: gpmdb
  - relation_type: prov:hadPrimarySource
    source: cellcollective
  - relation_type: prov:hadPrimarySource
    source: ecrin-mdr
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  - relation_type: prov:hadPrimarySource
    source: physiome-model-repository
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
    source: gpmdb
  - relation_type: prov:hadPrimarySource
    source: cellcollective
  - relation_type: prov:hadPrimarySource
    source: ecrin-mdr
  - relation_type: prov:hadPrimarySource
    source: panorama-public
  - relation_type: prov:hadPrimarySource
    source: physiome-model-repository
  product_url: https://www.omicsdi.org/ws/swagger-ui/index.html
publications:
- authors:
  - Tommy Yu
  - Catherine M. Lloyd
  - David P. Nickerson
  - Michael T. Cooling
  - Andrew K. Miller
  - Alan Garny
  - Jonna R. Terkildsen
  - James Lawson
  - Randall D. Britten
  - Peter J. Hunter
  - Poul M. F. Nielsen
  doi: 10.1093/bioinformatics/btq723
  id: doi:10.1093/bioinformatics/btq723
  journal: Bioinformatics
  preferred: true
  title: The Physiome Model Repository 2
  year: '2011'
- authors:
  - Dewan M. Sarwar
  - Reza Kalbasi
  - John H. Gennari
  - Brian E. Carlson
  - Maxwell L. Neal
  - Bernard de Bono
  - Koray Atalag
  - Peter J. Hunter
  - David P. Nickerson
  doi: 10.1186/s12859-019-2987-y
  id: doi:10.1186/s12859-019-2987-y
  journal: BMC Bioinformatics
  title: Model annotation and discovery with the Physiome Model Repository
  year: '2019'
synonyms:
- PMR
- PMR2
- CellML Model Repository
---
# Physiome Model Repository

The Physiome Model Repository (PMR) is the open model repository of the IUPS Physiome Project, developed and run by the Auckland Bioengineering Institute at the University of Auckland. It is best known as the home of the CellML Model Repository (also served at `models.cellml.org`), and it also stores FieldML and SED-ML files.

## Structure

- **Workspaces** are Git repositories that hold model files and their full change history. Any public workspace can be cloned with `git clone <workspace URI>`.
- **Exposures** publish a specific workspace revision with documentation, curation status, semantic annotations and download links.

On 2026-10-04 the JSON listings returned 1,303 workspaces and 1,108 exposures.

## Access

There is no separate API server. The same URLs return JSON when requested with `Accept: application/vnd.physiome.pmr2.json.1` (Collection+JSON) or `application/vnd.physiome.pmr2.json.0` (plain JSON), as described in the user documentation.

## License

The repository's license and citation pages state that all publicly accessible content is licensed under the Creative Commons Attribution 3.0 Unported License.

## Related

PMR is one of the model repositories indexed by OmicsDI. The CellML format itself is specified at https://www.cellml.org/specifications.