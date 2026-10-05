---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.lifewatch.eu/
  label: LifeWatch ERIC
creation_date: '2026-10-04T00:00:00Z'
description: EcoPortal is the LifeWatch ERIC repository of semantic artefacts (ontologies,
  thesauri, controlled vocabularies and glossaries) for ecology, biodiversity and related
  environmental domains. It is built on the open OntoPortal software, the same stack
  as BioPortal and AgroPortal, and offers browsing, search, mappings, an ontology recommender,
  a text annotator, FAIRness assessment, VocBench-based editing and a REST API. As
  of 2026-10-04 it hosted 82 semantic resources, including ECOCORE, PCO, BCO, FOVT,
  ENVTHES, AGROVOC, EUNIS habitats and the Darwin Core and Audubon Core controlled
  vocabularies.
domains:
- ecology
- biodiversity
- environment
- information technology
- organisms
homepage_url: https://ecoportal.lifewatch.eu/
id: ecoportal
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
name: EcoPortal
products:
- category: GraphicalInterface
  description: Web portal for searching, browsing and visualizing ecological ontologies,
    thesauri and their mappings, with ontology recommender, text annotator and submission
    of new semantic artefacts.
  format: http
  id: ecoportal.portal
  name: EcoPortal Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecoportal
  product_url: https://ecoportal.lifewatch.eu/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bioportal
- category: ProgrammingInterface
  description: OntoPortal REST API for EcoPortal ontologies, classes, search, mappings,
    metrics, annotation and downloads. Requests require an API key, available free
    with an EcoPortal account.
  format: http
  id: ecoportal.api
  name: EcoPortal REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecoportal
  product_url: https://data.ecoportal.lifewatch.eu/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bioportal
- category: DocumentationProduct
  description: EcoPortal user guide in the OntoPortal documentation, covering browsing,
    search, submission, the annotator and recommender, and API use.
  format: http
  id: ecoportal.docs
  name: EcoPortal User Guide
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecoportal
  product_url: https://ontoportal.github.io/documentation/user_guide/EcoPortal
- category: DocumentationProduct
  description: EcoPortal Documentation (Version 2.0), a LifeWatch ERIC manual describing
    the portal and its services, published with a DataCite DOI.
  format: http
  id: ecoportal.manual
  name: EcoPortal Documentation 2.0
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ecoportal
  product_url: https://doi.org/10.48373/59AV-7504
- category: Product
  description: Full Bioregistry export as JSON, with every prefix record including names,
    synonyms, URI formats, local identifier patterns, providers and mappings to the prefixes
    of other registries.
  format: json
  id: bioregistry.registry.json
  name: Bioregistry JSON Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:wasInfluencedBy
    source: obofoundry
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  - relation_type: prov:wasInfluencedBy
    source: ols
  - relation_type: prov:wasInfluencedBy
    source: wikidata
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: cellosaurus
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  - relation_type: prov:wasInfluencedBy
    source: biolink
  - relation_type: prov:wasInfluencedBy
    source: n2t
  - relation_type: prov:wasInfluencedBy
    source: identifiers-org
  - relation_type: prov:wasInfluencedBy
    source: fairsharing
  - relation_type: prov:wasInfluencedBy
    source: re3data
  - relation_type: prov:wasInfluencedBy
    source: agroportal
  - relation_type: prov:wasInfluencedBy
    source: ecoportal
  - relation_type: prov:wasInfluencedBy
    source: aberowl
  product_file_size: 786637
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/registry/registry.json
- category: MappingProduct
  description: SSSOM mappings between Bioregistry prefixes and the equivalent prefixes in
    other registries, such as OBO Foundry, BioPortal, OLS, Wikidata, the Gene Ontology registry,
    Cellosaurus, UniProt and NCBI.
  format: sssom
  id: bioregistry.sssom
  name: Bioregistry SSSOM Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:wasInfluencedBy
    source: obofoundry
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  - relation_type: prov:wasInfluencedBy
    source: ols
  - relation_type: prov:wasInfluencedBy
    source: wikidata
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: cellosaurus
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  - relation_type: prov:wasInfluencedBy
    source: biolink
  - relation_type: prov:wasInfluencedBy
    source: n2t
  - relation_type: prov:wasInfluencedBy
    source: identifiers-org
  - relation_type: prov:wasInfluencedBy
    source: fairsharing
  - relation_type: prov:wasInfluencedBy
    source: re3data
  - relation_type: prov:wasInfluencedBy
    source: agroportal
  - relation_type: prov:wasInfluencedBy
    source: ecoportal
  - relation_type: prov:wasInfluencedBy
    source: aberowl
  product_file_size: 136267
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/sssom/bioregistry.sssom.tsv
publications:
- authors:
  - Andrea Tarallo
  - Martina Pulieri
  - Parham Ramezani
  - Ilaria Rosati
  doi: 10.3233/FC-240002
  id: doi:10.3233/FC-240002
  journal: FAIR Connect
  preferred: true
  title: 'Advancements in EcoPortal: Enhancing functionalities for the ecological domain
    semantic artefacts repository'
  year: '2024'
- authors:
  - Xeni Kechagioglou
  - Lucia Vaira
  - Pierfrancesco Tomassino
  - Nicola Fiore
  - Alberto Basset
  - Ilaria Rosati
  id: https://ceur-ws.org/Vol-2969/paper6-s4biodiv.pdf
  journal: CEUR Workshop Proceedings
  title: 'EcoPortal: An Environment for FAIR Semantic Resources in the Ecological Domain'
  year: '2021'
- authors:
  - Cristina Di Muri
  - Martina Pulieri
  - Davide Raho
  - Alexandra N. Muresan
  - Andrea Tarallo
  - Jessica Titocci
  - Enrica Nestola
  - Alberto Basset
  - Sabrina Mazzoni
  - Ilaria Rosati
  doi: 10.1038/s41597-024-03669-3
  id: doi:10.1038/s41597-024-03669-3
  journal: Scientific Data
  title: 'Assessing semantic interoperability in environmental sciences: variety of
    approaches and semantic artefacts'
  year: '2024'
repository: https://github.com/lifewatch-eric
warnings:
- No overall license is stated for EcoPortal content; individual semantic artefacts
  carry their own licenses, so review each one's license metadata before reuse.
---
# EcoPortal

EcoPortal is the LifeWatch ERIC repository of ontologies, thesauri and vocabularies for ecology and biodiversity, built on the OntoPortal software shared with BioPortal and AgroPortal. It provides search, browsing, mappings, annotation, recommendation and a key-authenticated REST API.
