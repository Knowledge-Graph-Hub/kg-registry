---
activity_status: active
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://elter-ri.eu/
  label: eLTER RI
creation_date: '2026-10-05T00:00:00Z'
description: EnvThes (Environmental Thesaurus) is the controlled vocabulary of the
  European Long-Term Ecosystem, critical zone and socio-ecological Research Infrastructure
  (eLTER RI), published as a SKOS thesaurus. It provides harmonised terms for describing
  observations and measurements of ecosystem processes, including parameters, methods,
  variables and research topics, and supplies common keywords for annotating and querying
  metadata in DEIMS-SDR. Concepts carry multilingual labels and links to matching
  concepts in thesauri such as GEMET, EUROVOC and AGROVOC and in ENVO. The vocabulary
  is coordinated by Umweltbundesamt GmbH (Austria), maintained as a spreadsheet that
  is converted to RDF on GitHub, and served through a Skosmos browser.
domains:
- ecology
- environment
fairsharing_id: FAIRsharing.dS2o69
homepage_url: https://vocabs.lter-europe.net/EnvThes/en/
id: envthes
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: EnvThes
products:
- category: GraphicalInterface
  description: Skosmos browser for EnvThes with alphabetical and hierarchical navigation,
    search and concept pages for each term.
  format: http
  id: envthes.skosmos
  name: EnvThes Skosmos Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envthes
  product_url: https://vocabs.lter-europe.net/EnvThes/en/
- category: ProgrammingInterface
  description: Skosmos REST API for EnvThes, with endpoints for vocabulary metadata,
    statistics, search and per-concept RDF (Turtle, RDF/XML or JSON-LD).
  format: http
  id: envthes.api
  name: EnvThes Skosmos REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envthes
  product_url: https://vocabs.lter-europe.net/rest/v1/EnvThes/
  warnings:
  - The whole-vocabulary download endpoint (https://vocabs.lter-europe.net/rest/v1/EnvThes/data)
    returned HTTP 404 ("No download source URL known for vocabulary EnvThes") when
    checked on 2026-10-05. Per-concept data requests with a uri parameter worked.
- category: OntologyProduct
  description: Full EnvThes SKOS thesaurus in Turtle, generated from the source spreadsheet
    by the sheet2rdf workflow in the EnvThes GitHub repository.
  format: ttl
  id: envthes.ttl
  name: EnvThes Turtle
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envthes
  - relation_type: prov:wasInfluencedBy
    source: envo
  product_file_size: 3138937
  product_url: https://raw.githubusercontent.com/LTER-Europe/EnvThes/main/EnvThes.ttl
  repository: https://github.com/LTER-Europe/EnvThes
- category: Product
  description: CSV export of the EnvThes source spreadsheet.
  format: csv
  id: envthes.csv
  name: EnvThes CSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envthes
  product_file_size: 2376357
  product_url: https://raw.githubusercontent.com/LTER-Europe/EnvThes/main/EnvThes.csv
  repository: https://github.com/LTER-Europe/EnvThes
- category: Product
  description: EnvThes source spreadsheet, fetched from the authoritative Google Sheet
    and used as input for RDF generation.
  format: xlsx
  id: envthes.xlsx
  name: EnvThes Spreadsheet
  original_source:
  - relation_type: prov:hadPrimarySource
    source: envthes
  product_file_size: 4862426
  product_url: https://raw.githubusercontent.com/LTER-Europe/EnvThes/main/EnvThes.xlsx
  repository: https://github.com/LTER-Europe/EnvThes
publications:
- authors:
  - Herbert Schentz
  - Johannes Peterseil
  - Nic Bertrand
  id: https://dl.gi.de/handle/20.500.12116/25815
  journal: Proceedings of the 27th Conference on Environmental Informatics - Informatics
    for Environmental Protection, Sustainable Development and Risk Management
  preferred: true
  title: EnvThes – interlinked thesaurus for long term ecological research, monitoring,
    and experiments
  year: '2013'
repository: https://github.com/LTER-Europe/EnvThes
synonyms:
- Environmental Thesaurus
- eLTER Environmental Thesaurus
- ENVTHES
---
# EnvThes

EnvThes (Environmental Thesaurus) is the controlled vocabulary of the eLTER Research Infrastructure for long-term ecological research, monitoring and experiments. Development began in 2013 within the EnvEurope and ExpeER projects, originally using PoolParty, and the thesaurus now holds about 5,600 SKOS concepts (about 2,900 of them deprecated), at version 5.0.16 as of 2026-10-05. It is coordinated by Umweltbundesamt GmbH (Austria).

EnvThes drew on existing vocabularies such as the US LTER controlled vocabulary, the EUNIS habitat list, Catalogue of Life and NASA units, and links its concepts to matching terms in GEMET, EUROVOC, AGROVOC and ENVO. It provides the shared keywords used by DEIMS-SDR to annotate site and dataset metadata.

## Access

- **Skosmos**: browse and search at [vocabs.lter-europe.net/EnvThes](https://vocabs.lter-europe.net/EnvThes/en/) (also served at vocabs.elter-ri.eu). Note that the Skosmos vocabulary identifier is case-sensitive: `envthes` returns 404.
- **GitHub**: [LTER-Europe/EnvThes](https://github.com/LTER-Europe/EnvThes) holds the Turtle, CSV and XLSX files, regenerated from a Google Sheet by the sheet2rdf workflow. Term requests go through the repository's issue tracker.
- **Other portals**: EnvThes is also listed in EcoPortal (DOI [10.48373/0PWD-C575](https://doi.org/10.48373/0PWD-C575)), BioPortal, AberOWL, BARTOC and the TIB Terminology Service.

The vocabulary is released under CC BY 4.0.
