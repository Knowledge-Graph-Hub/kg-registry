---
activity_status: active
category: Ontology
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: giovanni.nisato@pistoiaalliance.org
      - contact_type: url
        value: https://www.pistoiaalliance.org/
    label: Pistoia Alliance
  - category: Individual
    contact_details:
      - contact_type: github
        value: Giovanni-Nisato
    label: Giovanni Nisato
  - category: Individual
    contact_details:
      - contact_type: github
        value: proccaserra
    label: Philippe Rocca-Serra
creation_date: '2025-11-10T00:00:00Z'
description: The Pistoia Alliance Pharma General Ontology (PGO) is a collaborative initiative to provide a shared upper-level reference ontology for the pharmaceutical industry. PGO aims to serve as a "Rosetta Stone" enabling semantic interoperability within and across organizations by identifying key concepts used throughout the drug development lifecycle and selecting public resources that can provide identifiers for each concept. Rather than creating new ontologies or mandating specific terminologies, PGO focuses on providing clear mechanisms to enable unambiguous declaration of the resources used and capturing the criteria for selecting semantic artifacts. The project follows FAIR principles and reuses existing semantic resources, including ontologies and controlled terminologies, as well as open source community software. The initial phase focuses on Research & Development (R&D) operations, defining core concepts and recommendations for associating controlled terminologies to service data exchange among pharmaceutical industry stakeholders. PGO is developed using LinkML for representing and documenting each type, and is supported by a consortium of major pharmaceutical companies including AstraZeneca, Chiesi Group, GSK, Merck KGaA, Novo Nordisk, Pfizer, and Hoffmann-La Roche.
domains:
  - drug discovery
  - general
homepage_url: https://pistoia-alliance-inc.github.io/Pistoia-Alliance-PGO/
id: pistoia-pgo
last_modified_date: '2026-11-10T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png
name: Pistoia Alliance Pharma General Ontology
products:
  - category: OntologyProduct
    description: GitHub repository containing the PGO core concept list (Markdown, CSV, and Excel), per-concept documentation pages, concept diagrams, and the source of the documentation website. Documentation releases are tagged (latest docs-public-V1.0.2, October 2026).
    format: http
    id: pistoia-pgo.github
    name: PGO GitHub Repository
    product_url: https://github.com/Pistoia-Alliance-Inc/Pistoia-Alliance-PGO
    original_source:
      - source: pistoia-pgo
        relation_type: prov:hadPrimarySource
  - category: DocumentationProduct
    description: Documentation website for PGO including core concepts, process descriptions, and use cases
    format: http
    id: pistoia-pgo.documentation
    name: PGO Documentation Website
    product_url: https://pistoia-alliance-inc.github.io/Pistoia-Alliance-PGO/
    original_source:
      - source: pistoia-pgo
        relation_type: prov:hadPrimarySource
  - category: DocumentationProduct
    description: Markdown list of the PGO Version 1.0 core concepts defining essential entities for pharmaceutical R&D data exchange
    format: txt
    id: pistoia-pgo.core_concepts
    name: PGO Core Concepts (Version 1.0)
    product_file_size: 16543
    product_url: https://raw.githubusercontent.com/Pistoia-Alliance-Inc/Pistoia-Alliance-PGO/development/2025_PGO_V1.0_core_concepts.md
    original_source:
      - source: pistoia-pgo
        relation_type: prov:hadPrimarySource
  - category: Product
    description: CSV release of the PGO Version 1.0 core concept list dated 2026-03-20, giving 17 core concepts with recommended definitions, the source vocabulary and identifier of each definition (mostly NCIt, plus OBI, MeSH, ChEBI, PSI-MI, UniProt, and QUDT), steering committee approval dates, and example sources.
    format: csv
    id: pistoia-pgo.core_concepts_csv
    name: PGO Core Concepts CSV (Version 1.0)
    original_source:
      - source: pistoia-pgo
        relation_type: prov:hadPrimarySource
    product_file_size: 11226
    product_url: https://raw.githubusercontent.com/Pistoia-Alliance-Inc/Pistoia-Alliance-PGO/development/PGO_V1.0_core_concepts_2026-03-20.csv
    secondary_source:
      - source: ncit
        relation_type: prov:used
      - source: obi
        relation_type: prov:used
      - source: mesh
        relation_type: prov:used
      - source: chebi
        relation_type: prov:used
      - source: mi
        relation_type: prov:used
      - source: uniprot
        relation_type: prov:used
  - category: Product
    description: Excel release of the PGO Version 1.0 core concept list dated 2026-03-20, with the same content as the CSV release (recommended definitions and their source vocabularies, including NCIt, OBI, MeSH, ChEBI, PSI-MI, UniProt, and QUDT).
    format: xlsx
    id: pistoia-pgo.core_concepts_xlsx
    name: PGO Core Concepts Excel (Version 1.0)
    original_source:
      - source: pistoia-pgo
        relation_type: prov:hadPrimarySource
    product_file_size: 23347
    product_url: https://raw.githubusercontent.com/Pistoia-Alliance-Inc/Pistoia-Alliance-PGO/development/PGO_V1.0_core_concepts_2026-03-20.xlsx
    secondary_source:
      - source: ncit
        relation_type: prov:used
      - source: obi
        relation_type: prov:used
      - source: mesh
        relation_type: prov:used
      - source: chebi
        relation_type: prov:used
      - source: mi
        relation_type: prov:used
      - source: uniprot
        relation_type: prov:used
  - category: DocumentationProduct
    description: High-level use cases demonstrating PGO applications in pharmaceutical data exchange (project deliverable D2.2)
    format: http
    id: pistoia-pgo.use_cases
    name: PGO Use Cases
    product_url: https://pistoiaalliance.org/resource-library/pharma-general-ontology-use-cases/
    original_source:
      - source: pistoia-pgo
        relation_type: prov:hadPrimarySource
  - category: DocumentationProduct
    description: Pistoia Alliance project page for PGO, linking project deliverables such as posters, the Phase 1 webinar, the use case report, governance documents, and the roadmap. Some documents require a Pistoia Alliance member login.
    format: http
    id: pistoia-pgo.project_page
    name: PGO Project Page
    product_url: https://pistoiaalliance.org/project/pharma-general-ontology/
    original_source:
      - source: pistoia-pgo
        relation_type: prov:hadPrimarySource
publications:
  - authors:
      - Joshua Valdez
      - Philippe Rocca-Serra
      - Markus Hartmann
      - Darko Hric
      - Asiyah Yu Lin
      - Birgit Meldal
      - Peter McQuilton
      - Riccardo Mariani
      - Martin Romacker
      - Giovanni Nisato
      - Ben Gardner
    id: https://ceur-ws.org/Vol-4196/paper_3.pdf
    journal: CEUR Workshop Proceedings
    preferred: true
    title: 'The Pistoia Alliance Pharma General Ontology: Experience Using LinkML in Pharma'
    year: '2025'
repository: https://github.com/Pistoia-Alliance-Inc/Pistoia-Alliance-PGO
synonyms:
  - PGO
  - Pharma General Ontology
  - PGO-Terminology
version: '1.0'
warnings:
  - The repository README says the documentation is a work in progress and that
    listed sources are not recommendations at this stage.
  - PGO is currently released as a list of core concepts with recommended definitions
    (Markdown, CSV, and Excel) rather than as an OWL or LinkML ontology file; a machine-readable
    version of PGO-terminology is on the 2026 roadmap.
---

## Description

The Pistoia Alliance Pharma General Ontology (PGO), also called PGO-Terminology, is a collaborative Pistoia Alliance project to agree on a shared set of core concepts for pharmaceutical research and development and to recommend public vocabularies that can supply identifiers for each concept.

## Overview

PGO addresses the insufficient and ambiguous asset descriptions that hamper information exchange within and across pharmaceutical organizations. Rather than mandating one resource over another, PGO aims to make it clear which controlled terminologies are used and why. Phase 1 started in April 2024 and focused on research and early development (R&ED).

The Version 1.0 core concept list contains 17 concepts: Assay, Biomarker, Biospecimen, Cell, Clinical study, Clinical study site, Compound, Device, Disease, Drug, Gene, Indication, Pharmaceutical product, Protein, Species, Substance, and Unit. Each concept has a recommended definition reused from an existing resource, mostly the NCI Thesaurus, with others taken from OBI, MeSH, ChEBI, PSI-MI, UniProt, and QUDT, along with the date the PGO steering committee approved it and examples of candidate sources.

## Key Features

- **Core Concepts**: Defines essential entities most frequently used when exchanging pharmaceutical R&D data
- **Reused Definitions**: Recommended definitions come from existing public resources, with source identifiers and attribution
- **Controlled Terminologies**: Aims to specify value sets for key attributes using community-agreed resources
- **FAIR Principles**: Follows Findable, Accessible, Interoperable, and Reusable data management principles
- **LinkML**: The project uses LinkML to represent and document each type

## Project Roadmap

**Phase 1 (2024-2025)**:
- Process flow, expert identification, and candidate definitions of core concepts
- Identification of high-level use cases
- Expert consultation, alignment, and formalization of core concepts for R&ED
- Implementation and testing using LinkML
- First release of the recommended core concepts

**Phase 2 (2025-2026)**:
- Field testing and application
- Extension of the core-concept vocabulary
- Updated version of the core-concept vocabulary
- Machine-readable version of PGO-Terminology

## Project Sponsors

Phase 1 sponsors listed in the repository are AstraZeneca, Chiesi Group, GSK, Merck KGaA, Novo Nordisk, Pfizer, and Roche. The Pistoia Alliance project page also lists Vertex as a supporter.

## Contacts

- Pistoia Alliance (https://www.pistoiaalliance.org/)
- Giovanni Nisato (Project Manager)
- Philippe Rocca-Serra (Technical Lead)

## Products

- **PGO GitHub Repository**: core concept list, per-concept Markdown pages, diagrams, and website source ([GitHub](https://github.com/Pistoia-Alliance-Inc/Pistoia-Alliance-PGO)). Documentation releases are tagged; the latest is docs-public-V1.0.2 (October 2026).
- **PGO Documentation Website**: [pistoia-alliance-inc.github.io/Pistoia-Alliance-PGO](https://pistoia-alliance-inc.github.io/Pistoia-Alliance-PGO/)
- **PGO Core Concepts (Version 1.0)**: [Markdown](https://github.com/Pistoia-Alliance-Inc/Pistoia-Alliance-PGO/blob/development/2025_PGO_V1.0_core_concepts.md), [CSV](https://raw.githubusercontent.com/Pistoia-Alliance-Inc/Pistoia-Alliance-PGO/development/PGO_V1.0_core_concepts_2026-03-20.csv), and [Excel](https://raw.githubusercontent.com/Pistoia-Alliance-Inc/Pistoia-Alliance-PGO/development/PGO_V1.0_core_concepts_2026-03-20.xlsx) versions, dated 2026-03-20
- **PGO Use Cases**: [use case report (D2.2)](https://pistoiaalliance.org/resource-library/pharma-general-ontology-use-cases/)
- **PGO Project Page**: [Pistoia Alliance project page](https://pistoiaalliance.org/project/pharma-general-ontology/)

## Publications

- Valdez J, Rocca-Serra P, et al. [The Pistoia Alliance Pharma General Ontology: Experience Using LinkML in Pharma](https://ceur-ws.org/Vol-4196/paper_3.pdf). SWAT4HCLS 2025, CEUR Workshop Proceedings Vol-4196.

---

*This resource was manually curated for the Knowledge Graph Registry.*
