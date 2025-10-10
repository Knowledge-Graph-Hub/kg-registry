---
activity_status: active
category: DataSource
creation_date: '2025-08-30T00:00:00Z'
description: The Eukaryotic Pathogen Database (EuPathDB) is an integrated genomics database covering numerous eukaryotic pathogens including Plasmodium, Trypanosoma, and other parasites. It provides functional genomics resources integrating data from human and veterinary parasites, now known as VEuPathDB (Vectorbase and EuPathDB).
domains:
  - genomics
  - biological systems
  - organisms
id: eupathdb
last_modified_date: '2025-10-10T00:00:00Z'
layout: resource_detail
name: Eukaryotic Pathogen Database (EuPathDB)
products:
  - category: GraphicalInterface
    name: VEuPathDB Web Portal
    id: eupathdb.portal
    description: Web portal for searching, browsing, and analyzing eukaryotic pathogen genomic data including gene searches, genome browsers, and pathway analysis.
    format: http
    product_url: https://veupathdb.org/veupathdb/app
  - category: ProgrammingInterface
    name: VEuPathDB Web Services API
    id: eupathdb.api
    description: Web services API for programmatic access to EuPathDB data and analyses.
    format: http
    product_url: https://veupathdb.org/veupathdb/service
  - category: Product
    name: VEuPathDB Data Downloads
    id: eupathdb.downloads
    description: FTP and download access to genome sequences, annotations, and analysis results for component databases.
    format: http
    product_url: https://veupathdb.org/veupathdb/app/downloads
  - category: GraphicalInterface
    name: Apollo Genome Annotation
    id: eupathdb.apollo
    description: Real-time collaborative genome annotation and curation platform for structural and functional annotation.
    format: http
    product_url: https://veupathdb.org/veupathdb/app/workspace/strategies
  - category: GraphicalInterface
    name: MapVEu
    id: eupathdb.mapveu
    description: Map-based visualization tool for field-collected data including insecticide resistance, population abundance, and pathogen infection status.
    format: http
    product_url: https://mapveu.org
  - category: DocumentationProduct
    name: VEuPathDB Documentation and Tutorials
    id: eupathdb.docs
    description: Comprehensive documentation including tutorials, exercises, and user guides for VEuPathDB tools and features.
    format: http
    product_url: https://veupathdb.org/veupathdb/app/static-content/landing.html
publications:
  - id: "https://doi.org/10.1093/nar/gks1113"
    preferred: true
    title: "EuPathDB: the eukaryotic pathogen database"
    authors:
      - Aurrecoechea C
      - Barreto A
      - Brestelli J
      - Brunk BP
      - Cade S
      - Doherty R
      - Fischer S
      - Gajria B
      - Gao X
      - Gingle A
    year: "2013"
    journal: "Nucleic Acids Research"
warnings:
  - EuPathDB is an active data source providing integrated genomics resources for eukaryotic pathogens. The project is now known as VEuPathDB.
---

# Eukaryotic Pathogen Database (EuPathDB)

The Eukaryotic Pathogen Database (EuPathDB) is an integrated genomics database covering numerous eukaryotic pathogens including Plasmodium, Trypanosoma, and other parasites. It provides functional genomics resources integrating data from human and veterinary parasites. EuPathDB is now part of VEuPathDB (Vectorbase and EuPathDB), which is funded by the Fund for Advancement of Science and Medicine, Open Philanthropy, and the Chan Zuckerberg Initiative. For more information, visit the [VEuPathDB Portal](https://veupathdb.org/veupathdb/app) or see the [documentation](https://veupathdb.org/veupathdb/app/static-content/landing.html).
