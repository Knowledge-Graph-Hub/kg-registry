---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://cellcollective.org/
  - contact_type: email
    value: support@cellcollective.org
  - contact_type: github
    value: HelikarLab
  label: Helikar Lab, University of Nebraska-Lincoln
creation_date: '2026-10-04T00:00:00Z'
description: Cell Collective is a web platform for building, simulating and sharing
  interactive logical (Boolean) models of biological networks, with a public library
  of curated published models. It comes from the Helikar lab at the University of
  Nebraska-Lincoln and runs separate research, teaching and learning environments.
  Models can be exported as SBML-qual, Boolean expressions, truth tables, GML and
  interaction matrices. OmicsDI indexes 241 Cell Collective models (checked 2026-10-04).
domains:
- systems biology
- biological systems
homepage_url: https://cellcollective.org/
id: cellcollective
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
name: Cell Collective
products:
- category: GraphicalInterface
  description: Cell Collective web platform for browsing the public model library
    and building, simulating and analysing logical models of biological networks.
  format: http
  id: cellcollective.portal
  name: Cell Collective Platform
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellcollective
  product_url: https://cellcollective.org/
- category: GraphicalInterface
  description: Research environment of Cell Collective, with the published model library
    and export of individual models as SBML-qual, Boolean expressions, truth tables,
    GML or interaction matrices. Exports are generated per model through the web application;
    there is no documented bulk download or public API.
  format: http
  id: cellcollective.research
  name: Cell Collective Research
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellcollective
  product_url: https://research.cellcollective.org/
- category: GraphicalInterface
  description: Learning environment of Cell Collective, offering interactive model-based
    lessons for biology education.
  format: http
  id: cellcollective.learn
  name: Cell Collective Learn
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cellcollective
  product_url: https://learn.cellcollective.org/
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
  - Tomáš Helikar
  - Bryan Kowal
  - Sean McClenathan
  - Mitchell Bruckner
  - Thaine Rowley
  - Alex Madrahimov
  - Ben Wicks
  - Manish Shrestha
  - Kahani Limbu
  - Jim A Rogers
  doi: 10.1186/1752-0509-6-96
  id: doi:10.1186/1752-0509-6-96
  journal: BMC Systems Biology
  preferred: true
  title: 'The Cell Collective: Toward an open and collaborative approach to systems
    biology'
  year: '2012'
synonyms:
- CellCollective
---
# Cell Collective

Cell Collective is an interactive, collaborative platform for logical (Boolean) modeling of biological networks. Users build models with the Bio-Logic Builder, run simulations in the browser and share models publicly. Published models in the library are curated by reconstruction and re-simulation so their dynamics match the source publications.

The platform runs three environments: research (`research.cellcollective.org`), teaching and learning (`learn.cellcollective.org`).

## Access

Models are exported one at a time from the web application as SBML-qual, Boolean expressions, truth tables, GML or interaction matrices. The application uses an internal web API under `research.cellcollective.org/web/`, which is undocumented, so it is not listed as a product. No bulk download was found.

## License

No license for the platform or the public models was found on the site when checked on 2026-10-04.

## Indexing

OmicsDI indexes Cell Collective as a model repository (241 models on 2026-10-04).