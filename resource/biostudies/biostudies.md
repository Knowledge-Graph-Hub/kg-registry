---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: biostudies@ebi.ac.uk
  - contact_type: url
    value: https://www.ebi.ac.uk/biostudies/
  label: BioStudies team, EMBL-EBI
creation_date: '2026-10-03T00:00:00Z'
description: BioStudies is an EMBL-EBI repository for descriptions of biological studies.
  It links each study to its associated data, whether held in other EMBL-EBI databases,
  in external resources, or in BioStudies itself, and accepts data that do not fit
  into specialised archives. Studies are organised into collections with their own
  metadata guidelines; the largest holds supplementary data imported from Europe PMC
  articles, and ArrayExpress has been served as a BioStudies collection since 2021.
domains:
- general
- metadata
- information technology
- scholarly communication
- literature
homepage_url: https://www.ebi.ac.uk/biostudies/
id: biostudies
last_modified_date: '2026-10-03T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ebi.ac.uk/about/terms-of-use
  label: EMBL-EBI Terms of Use
name: BioStudies
products:
- category: GraphicalInterface
  description: Web interface for searching and browsing BioStudies studies and collections,
    with study descriptions, links to associated data in other resources, and downloadable
    files.
  format: http
  id: biostudies.portal
  name: BioStudies Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biostudies
  product_url: https://www.ebi.ac.uk/biostudies/
- category: ProgrammingInterface
  connection_url: https://www.ebi.ac.uk/biostudies/api/v1/search
  description: REST API returning JSON for searching BioStudies, with per-collection
    search endpoints and per-study metadata and file listings. Covers all collections,
    including supplementary data imported from Europe PMC.
  format: http
  id: biostudies.api
  is_public: true
  name: BioStudies REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: europepmc
  product_url: https://www.ebi.ac.uk/biostudies/api/v1/search
- category: Product
  description: FTP/HTTPS archive of BioStudies study files, organized by accession
    prefix, including Europe PMC supplementary data and ArrayExpress experiment files.
  format: mixed
  id: biostudies.ftp
  name: BioStudies FTP Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: europepmc
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_url: https://ftp.ebi.ac.uk/pub/databases/biostudies/
- category: GraphicalInterface
  description: BioStudies submission tool for depositing study descriptions and data
    files.
  format: http
  id: biostudies.submission
  name: BioStudies Submission Tool
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biostudies
  product_url: https://www.ebi.ac.uk/biostudies/submissions/
- category: ProgrammingInterface
  connection_url: https://www.ebi.ac.uk/biostudies/api/v1/arrayexpress/search
  description: BioStudies REST API endpoint for searching ArrayExpress studies, returning
    JSON; per-study metadata and file listings are available from the BioStudies studies
    endpoints.
  format: http
  id: arrayexpress.api
  is_public: true
  name: ArrayExpress Search API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: biostudies
  product_url: https://www.ebi.ac.uk/biostudies/api/v1/arrayexpress/search
- category: MappingProduct
  description: CSV files, one per database, linking Europe PMC articles to accessions
    text-mined from their full text, covering ArrayExpress, BioStudies, ChEBI, Cellosaurus,
    AlphaFold DB, BioProject, BioSample, BRENDA, CATH and others.
  format: csv
  id: europepmc.textmined-terms
  name: Europe PMC Text-Mined Database Accession Links
  original_source:
  - relation_type: prov:hadPrimarySource
    source: europepmc
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: brenda
  product_url: https://ftp.ebi.ac.uk/pub/databases/pmc/TextMinedTerms/
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
  - Awais Athar
  - Ehsan Behrangi
  - Mauricio Martinez Jimenez
  - Jhoan Manuel Munoz Serrano
  - Juan Camilo Rada Mesa
  - Eliot Ragueneau
  - Ugis Sarkans
  doi: 10.1016/j.jmb.2026.169874
  id: doi:10.1016/j.jmb.2026.169874
  journal: Journal of Molecular Biology
  preferred: true
  title: 'BioStudies Database: A Platform for Life Sciences Study Data Dissemination'
  year: '2026'
- authors:
  - Ugis Sarkans
  - Mikhail Gostev
  - Awais Athar
  - Ehsan Behrangi
  - Olga Melnichuk
  - Ahmed Ali
  - Jasmine Minguet
  - Juan Camillo Rada
  - Catherine Snow
  - Andrew Tikhonov
  - Alvis Brazma
  - Johanna McEntyre
  doi: 10.1093/nar/gkx965
  id: doi:10.1093/nar/gkx965
  journal: Nucleic Acids Research
  title: The BioStudies database - one stop shop for all data supporting a life sciences
    study
  year: '2018'
- authors:
  - Jo McEntyre
  - Ugis Sarkans
  - Alvis Brazma
  doi: 10.15252/msb.20156658
  id: doi:10.15252/msb.20156658
  journal: Molecular Systems Biology
  title: The BioStudies database
  year: '2015'
repository: https://github.com/EBIBioStudies
---
# BioStudies

BioStudies is an EMBL-EBI repository for descriptions of biological studies. It links
each study to its associated data, whether held in other EMBL-EBI databases, in
external resources, or in BioStudies itself, and it accepts data that do not fit into
specialised archives. A study is often, but not always, tied to a publication.

BioStudies supports data sharing during collaborative projects, deposition at
manuscript submission, and data packages after publication, and it has taken over
archival for projects moving off legacy infrastructure.

## Collections

Datasets are organised into collections with their own metadata guidelines. On
2026-10-03 the search API reported 3,413,177 entries in total. Of these, 3,302,748
belonged to the EuropePMC collection (`S-EPMC` accessions), which holds supplementary
data imported from Europe PMC articles. Other collections include ArrayExpress
(80,947 studies), served as a BioStudies collection since 2021, and BioImages (5,128).

## Access

- Web interface: https://www.ebi.ac.uk/biostudies/
- REST API: https://www.ebi.ac.uk/biostudies/api/v1/search, with per-collection
  endpoints such as `/api/v1/arrayexpress/search` and per-study endpoints such as
  `/api/v1/studies/<accession>/info`
- Files: https://ftp.ebi.ac.uk/pub/databases/biostudies/, organized by accession
  prefix
- Submissions: https://www.ebi.ac.uk/biostudies/submissions/
- Code: https://github.com/EBIBioStudies, including the PageTab submission format
  specification

## License

The site links the EMBL-EBI Terms of Use. Individual studies may carry their own
terms; no single data license is stated.
