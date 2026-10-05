---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: support@fair-dom.org
  - contact_type: url
    value: https://fair-dom.org/
  label: FAIRDOM
creation_date: '2026-10-04T00:00:00Z'
description: FAIRDOMHub is a public repository and collaboration environment for sharing
  systems biology research outputs, including data files, models, SOPs, presentations
  and publications, organized by project and by investigation, study and assay (ISA).
  It runs on the open source SEEK platform and is operated by the FAIRDOM consortium.
  On 2026-10-04 its JSON API listed 521 projects, 234 investigations, 6,004 data files
  and 502 SOPs. Each contribution carries a license chosen by its submitter, and metadata
  are licensed CC BY 4.0.
domains:
- systems biology
- biological systems
homepage_url: https://fairdomhub.org/
id: fairdomhub
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0 (metadata; contributions carry submitter-chosen licenses)
name: FAIRDOMHub
products:
- category: GraphicalInterface
  description: Web portal for browsing, searching and downloading shared systems biology
    projects, investigations, studies, assays, data files, models and SOPs.
  format: http
  id: fairdomhub.portal
  name: FAIRDOMHub Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fairdomhub
  product_url: https://fairdomhub.org/
- category: ProgrammingInterface
  description: SEEK JSON:API (version 0.3) for reading and writing FAIRDOMHub resources
    such as projects, investigations, studies, assays, data files, models, SOPs and
    people. Requests use the application/vnd.api+json media type.
  format: http
  id: fairdomhub.api
  name: FAIRDOMHub JSON API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fairdomhub
  product_url: https://fairdomhub.org/api
- category: GraphicalInterface
  description: Web query interface for running SPARQL queries over the RDF metadata
    that FAIRDOMHub exposes for its resources.
  format: http
  id: fairdomhub.sparql
  name: FAIRDOMHub SPARQL Query Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fairdomhub
  product_url: https://fairdomhub.org/sparql
- category: ProcessProduct
  description: Source code of SEEK, the Ruby on Rails web platform for managing and
    sharing FAIR research assets that FAIRDOMHub runs on.
  format: mixed
  id: fairdomhub.seek
  license:
    id: https://opensource.org/licenses/BSD-3-Clause
    label: BSD-3-Clause
  name: SEEK Software
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fairdomhub
  product_url: https://github.com/seek4science/seek
  repository: https://github.com/seek4science/seek
- category: DocumentationProduct
  description: SEEK documentation, including user guides and the API reference used
    by FAIRDOMHub.
  format: http
  id: fairdomhub.docs
  name: SEEK Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fairdomhub
  product_url: https://docs.seek4science.org/
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
  - Katherine Wolstencroft
  - Olga Krebs
  - Jacky L. Snoep
  - Natalie J. Stanford
  - Finn Bacall
  - Martin Golebiewski
  - Rostyk Kuzyakiv
  - Quyen Nguyen
  - Stuart Owen
  - Stian Soiland-Reyes
  - Jakub Straszewski
  - David D. van Niekerk
  - Alan R. Williams
  - Lars Malmström
  - Bernd Rinn
  - Wolfgang Müller
  - Carole Goble
  doi: 10.1093/nar/gkw1032
  id: doi:10.1093/nar/gkw1032
  journal: Nucleic Acids Research
  preferred: true
  title: 'FAIRDOMHub: a repository and collaboration environment for sharing systems
    biology research'
  year: '2017'
repository: https://github.com/seek4science/seek
synonyms:
- FAIRDOM Hub
---
# FAIRDOMHub

FAIRDOMHub is a repository and collaboration environment for systems biology research, run by the FAIRDOM consortium. Projects share data files, models, standard operating procedures, presentations and publications, and organize them with the ISA (investigation, study, assay) structure.

## Platform

FAIRDOMHub runs on [SEEK](https://seek4science.org/), an open source (BSD-3-Clause) Ruby on Rails platform. SEEK provides the JSON:API used for programmatic access, per-resource RDF exports (for example `https://fairdomhub.org/projects/1.rdf`) and a SPARQL query interface over that RDF.

## Licensing

Per the FAIRDOMHub terms and conditions, each submitter chooses the license for a contribution, and metadata are licensed under CC BY 4.0.

## Usage

FAIRDOMHub datasets and models are indexed by OmicsDI under its Models category.