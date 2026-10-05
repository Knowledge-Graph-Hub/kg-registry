---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://obofoundry.org/
  - contact_type: github
    value: OBOFoundry
  label: OBO Foundry Operations Committee
creation_date: '2026-10-04T00:00:00Z'
description: The Open Biological and Biomedical Ontology (OBO) Foundry is a community
  of ontology developers committed to a shared set of principles for open, interoperable
  biomedical ontologies. It runs the OBO registry, the canonical list of member ontologies
  with their metadata, persistent URLs (PURLs), release products, licenses and contacts,
  and it reviews ontologies against its principles. When checked on 2026-10-04 the
  registry listed 267 ontologies, 191 of them active.
domains:
- biomedical
- information technology
- metadata
homepage_url: https://obofoundry.org/
id: obofoundry
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: OBO Foundry
products:
- category: Product
  description: Machine-readable metadata for every ontology in the OBO registry (ids,
    titles, descriptions, PURLs, products, licenses, contacts, dependencies and activity
    status), in YAML.
  format: yaml
  id: obofoundry.registry.yaml
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: OBO Foundry Registry Metadata (YAML)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obofoundry
  product_file_size: 76313
  product_url: https://obofoundry.org/registry/ontologies.yml
- category: Product
  description: OBO registry ontology metadata serialized as JSON-LD.
  format: jsonld
  id: obofoundry.registry.jsonld
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: OBO Foundry Registry Metadata (JSON-LD)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obofoundry
  product_file_size: 85640
  product_url: https://obofoundry.org/registry/ontologies.jsonld
- category: Product
  description: OBO registry ontology metadata serialized as RDF Turtle.
  format: ttl
  id: obofoundry.registry.ttl
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: OBO Foundry Registry Metadata (Turtle)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obofoundry
  product_file_size: 537368
  product_url: https://obofoundry.org/registry/ontologies.ttl
- category: GraphicalInterface
  description: OBO Foundry website with a browsable table of registered ontologies,
    a detail page per ontology, and documentation of the OBO principles and review
    process.
  format: http
  id: obofoundry.portal
  name: OBO Foundry Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obofoundry
  product_url: https://obofoundry.org/
- category: DocumentationProduct
  description: Summary of the OBO Foundry principles that member ontologies are expected
    to follow, such as openness, common format, URI/identifier space, versioning and
    documentation.
  format: http
  id: obofoundry.principles
  name: OBO Foundry Principles
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obofoundry
  product_url: https://obofoundry.org/principles/fp-000-summary.html
- category: Product
  description: GitHub repository holding the OBO registry metadata (one Markdown file
    with YAML front matter per ontology), the Jekyll website, and the Python tooling
    that builds the registry exports and runs the OBO Dashboard checks. Data are CC0
    1.0 and code is BSD 3-Clause.
  format: mixed
  id: obofoundry.repository
  name: OBO Foundry GitHub Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obofoundry
  product_url: https://github.com/OBOFoundry/OBOFoundry.github.io
- category: GraphicalInterface
  description: Web portal for searching, browsing, and visualizing biomedical ontologies
    and mappings
  format: http
  id: bioportal.portal
  name: BioPortal Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioportal
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:wasDerivedFrom
    source: obofoundry
  product_url: https://bioportal.bioontology.org/
- category: ProgrammingInterface
  description: REST API for ontology concepts, search, mappings, metrics, and downloads.
    Most endpoints require a free BioPortal API key.
  format: http
  id: bioportal.api
  name: BioPortal REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioportal
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:wasDerivedFrom
    source: obofoundry
  product_url: https://data.bioontology.org/
- category: Product
  description: Full Bioregistry export as JSON, with every prefix record including
    names, synonyms, URI formats, local identifier patterns, providers and mappings
    to the prefixes of other registries.
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
  product_file_size: 786637
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/registry/registry.json
- category: MappingProduct
  description: SSSOM mappings between Bioregistry prefixes and the equivalent prefixes
    in other registries, such as OBO Foundry, BioPortal, OLS, Wikidata, the Gene Ontology
    registry, Cellosaurus, UniProt and NCBI.
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
  product_file_size: 136267
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/sssom/bioregistry.sssom.tsv
- category: Product
  compression: targz
  description: Gzipped tar archive (ontology_jsons.tgz, about 2 GB) of all ontologies
    loaded into OLS, in OLS JSON format.
  format: json
  id: ols.json
  name: OLS Ontologies JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:wasDerivedFrom
    source: obofoundry
  product_url: https://ftp.ebi.ac.uk/pub/databases/spot/ols/latest/
- category: Product
  compression: targz
  description: Gzipped tar archive (ontology_jsons_linked.tgz) of OLS ontology JSON
    with added cross-ontology and external database links.
  format: json
  id: ols.json-linked
  name: OLS Linked Ontology JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:wasDerivedFrom
    source: obofoundry
  product_url: https://ftp.ebi.ac.uk/pub/databases/spot/ols/latest/
publications:
- authors:
  - Rebecca Jackson
  - Nicolas Matentzoglu
  - James A Overton
  - Randi Vita
  - James P Balhoff
  - Pier Luigi Buttigieg
  - Seth Carbon
  - Melanie Courtot
  - Alexander D Diehl
  - Damion M Dooley
  - William D Duncan
  - Nomi L Harris
  - Melissa A Haendel
  - Suzanna E Lewis
  - Darren A Natale
  - David Osumi-Sutherland
  - Alan Ruttenberg
  - Lynn M Schriml
  - Barry Smith
  - Christian J Stoeckert Jr.
  - Nicole A Vasilevsky
  - Ramona L Walls
  - Jie Zheng
  - Christopher J Mungall
  - Bjoern Peters
  doi: 10.1093/database/baab069
  id: doi:10.1093/database/baab069
  journal: Database
  preferred: true
  title: 'OBO Foundry in 2021: operationalizing open data principles to evaluate ontologies'
  year: '2021'
- authors:
  - Barry Smith
  - Michael Ashburner
  - Cornelius Rosse
  - Jonathan Bard
  - William Bug
  - Werner Ceusters
  - Louis J Goldberg
  - Karen Eilbeck
  - Amelia Ireland
  - Christopher J Mungall
  - Neocles Leontis
  - Philippe Rocca-Serra
  - Alan Ruttenberg
  - Susanna-Assunta Sansone
  - Richard H Scheuermann
  - Nigam Shah
  - Patricia L Whetzel
  - Suzanna Lewis
  doi: 10.1038/nbt1346
  id: doi:10.1038/nbt1346
  journal: Nature Biotechnology
  title: 'The OBO Foundry: coordinated evolution of ontologies to support biomedical
    data integration'
  year: '2007'
repository: https://github.com/OBOFoundry/OBOFoundry.github.io
synonyms:
- OBO
- Open Biological and Biomedical Ontology Foundry
- OBO Library
- OBO registry
---
# OBO Foundry

The Open Biological and Biomedical Ontology (OBO) Foundry is a collective of ontology developers who agree to follow shared principles so that their ontologies interoperate. It began in 2007 and is coordinated by an Operations Committee with working groups for editorial review, technical infrastructure and outreach.

## Registry

The OBO registry is the list of member ontologies. Each ontology has an entry with its id prefix, title, description, homepage, PURLs for its release products, license, contact and activity status. The registry is maintained on GitHub and exported as YAML, JSON-LD and Turtle at https://obofoundry.org/registry/. Many downstream services, such as the Ontology Lookup Service, BioPortal and the Bioregistry, load or align with this metadata.

When checked on 2026-10-04 the registry listed 267 ontologies, 191 marked active.

## Principles

Member ontologies are expected to follow the OBO principles, which cover open licensing, a common format, a unique identifier space, versioning, textual definitions, documented scope and use of the shared relations ontology. The OBO Dashboard reports automated checks against these principles.

In KG-Registry, OBO Foundry ontologies carry the `obo-foundry` collection tag.