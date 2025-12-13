---
activity_status: active
category: DataSource
creation_date: '2025-08-30T00:00:00Z'
description: The Eukaryotic Pathogen Database (EuPathDB) is an integrated genomics
  database covering numerous eukaryotic pathogens including Plasmodium, Trypanosoma,
  and other parasites. It provides functional genomics resources integrating data
  from human and veterinary parasites, now known as VEuPathDB (Vectorbase and EuPathDB).
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
  description: Web portal for searching, browsing, and analyzing eukaryotic pathogen
    genomic data including gene searches, genome browsers, and pathway analysis.
  format: http
  id: eupathdb.portal
  name: VEuPathDB Web Portal
  product_url: https://veupathdb.org/veupathdb/app
- category: ProgrammingInterface
  description: Web services API for programmatic access to EuPathDB data and analyses.
  format: http
  id: eupathdb.api
  name: VEuPathDB Web Services API
  product_url: https://veupathdb.org/veupathdb/service
- category: Product
  description: FTP and download access to genome sequences, annotations, and analysis
    results for component databases.
  format: http
  id: eupathdb.downloads
  name: VEuPathDB Data Downloads
  product_url: https://veupathdb.org/veupathdb/app/downloads
- category: GraphicalInterface
  description: Real-time collaborative genome annotation and curation platform for
    structural and functional annotation.
  format: http
  id: eupathdb.apollo
  name: Apollo Genome Annotation
  product_url: https://veupathdb.org/veupathdb/app/workspace/strategies
- category: GraphicalInterface
  description: Map-based visualization tool for field-collected data including insecticide
    resistance, population abundance, and pathogen infection status.
  format: http
  id: eupathdb.mapveu
  name: MapVEu
  product_url: https://mapveu.org
- category: DocumentationProduct
  description: Comprehensive documentation including tutorials, exercises, and user
    guides for VEuPathDB tools and features.
  format: http
  id: eupathdb.docs
  name: VEuPathDB Documentation and Tutorials
  product_url: https://veupathdb.org/veupathdb/app/static-content/landing.html
- category: ProgrammingInterface
  description: TRAPI web API for querying MicrobiomeKG
  format: http
  id: microbiomekg.api
  name: MicrobiomeKG Plover API
  original_source:
  - biolink
  - chebi
  - ncbitaxon
  - ncbigene
  - mesh
  - pubchem
  - go
  - mondo
  - ncit
  - efo
  - uniprot
  - rhea
  - pr
  - uberon
  - panther
  - hgnc
  - drugbank
  - eupathdb
  product_url: https://multiomics.transltr.io/mbkp
  secondary_source:
  - microbiomekg
publications:
- authors:
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
  id: https://doi.org/10.1093/nar/gks1113
  journal: Nucleic Acids Research
  preferred: true
  title: 'EuPathDB: the eukaryotic pathogen database'
  year: '2013'
warnings:
- EuPathDB is an active data source providing integrated genomics resources for eukaryotic
  pathogens. The project is now known as VEuPathDB.
taxon:
- NCBITaxon:9606
- NCBITaxon:2759
---
# Eukaryotic Pathogen Database (EuPathDB)

The Eukaryotic Pathogen Database (EuPathDB) is an integrated genomics database covering numerous eukaryotic pathogens including Plasmodium, Trypanosoma, and other parasites. It provides functional genomics resources integrating data from human and veterinary parasites. EuPathDB is now part of VEuPathDB (Vectorbase and EuPathDB), which is funded by the Fund for Advancement of Science and Medicine, Open Philanthropy, and the Chan Zuckerberg Initiative. For more information, visit the [VEuPathDB Portal](https://veupathdb.org/veupathdb/app) or see the [documentation](https://veupathdb.org/veupathdb/app/static-content/landing.html).