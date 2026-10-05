---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://peptideatlas.org/contacts.php
  label: Institute for Systems Biology
- category: Individual
  label: Eric W. Deutsch
  orcid: 0000-0001-8732-0928
creation_date: '2026-10-04T00:00:00Z'
description: PeptideAtlas, from the Institute for Systems Biology (ISB), is a compendium
  of peptides identified in tandem mass spectrometry proteomics experiments. Raw data
  from public datasets are reprocessed through a uniform pipeline (the Trans-Proteomic
  Pipeline) and mapped to reference proteomes and genomes, producing organism- and
  sample-specific builds. On 2026-10-04 its build index listed 110 builds across 39
  organism groups, including the Human 2026-01 build. The project also runs PASSEL,
  a repository for SRM experiments, and SRMAtlas, a library of targeted proteomics
  assays.
domains:
- proteomics
- biomedical
homepage_url: https://peptideatlas.org/
id: peptideatlas
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
name: PeptideAtlas
products:
- category: GraphicalInterface
  description: PeptideAtlas web portal for browsing builds, searching peptides and
    proteins, and reaching related ISB proteomics resources.
  format: http
  id: peptideatlas.portal
  name: PeptideAtlas Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  product_url: https://peptideatlas.org/
- category: Product
  description: Machine-readable JSON index of all PeptideAtlas builds, with build
    id, name, description, organism, number of distinct peptides and the URL of each
    build's download page.
  format: json
  id: peptideatlas.builds
  name: PeptideAtlas Build Index
  original_source:
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  product_url: https://db.systemsbiology.net/sbeams/cgi/PeptideAtlas/main.cgi?output_format=json
- category: Product
  description: FASTA file of all distinct peptides observed in the Human 2026-01 PeptideAtlas
    build (atlas build 607).
  format: fasta
  id: peptideatlas.human.peptides
  latest_version: 2026-01
  name: PeptideAtlas Human Peptides FASTA
  original_source:
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  product_file_size: 167809736
  product_url: https://peptideatlas.org/builds/human/202601/APD_Hs_all.fasta
- category: Product
  compression: zip
  description: Tab-separated tables of the Human 2026-01 PeptideAtlas build (atlas
    build 607), including peptides, protein identifications and mappings (about 6.8
    GB compressed).
  format: tsv
  id: peptideatlas.human.tables
  latest_version: 2026-01
  name: PeptideAtlas Human Build Tables
  original_source:
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  product_file_size: 6762826956
  product_url: https://peptideatlas.org/builds/human/202601/atlas_build_607.tsv.zip
- category: Product
  compression: gzip
  description: MySQL dump of the Human 2026-01 PeptideAtlas build (atlas build 607),
    about 5.8 GB compressed.
  format: mysql
  id: peptideatlas.human.mysql
  latest_version: 2026-01
  name: PeptideAtlas Human Build MySQL Dump
  original_source:
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  product_file_size: 5821913317
  product_url: https://peptideatlas.org/builds/human/202601/atlas_build_607.mysql.gz
- category: MappingProduct
  description: Mapping of Human 2026-01 PeptideAtlas peptides to Ensembl proteins.
  format: tsv
  id: peptideatlas.human.ensembl-mapping
  latest_version: 2026-01
  name: PeptideAtlas Human Peptide to Ensembl Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  - relation_type: prov:hadPrimarySource
    source: ensembl
  product_file_size: 11751640392
  product_url: https://peptideatlas.org/builds/human/202601/APD_ensembl_hits.tsv
- category: Product
  description: Genome coordinate mapping of peptides in the Human 2026-01 PeptideAtlas
    build (about 19 GB, uncompressed text).
  format: txt
  id: peptideatlas.human.coordinates
  latest_version: 2026-01
  name: PeptideAtlas Human Peptide Coordinates
  original_source:
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  product_file_size: 19026695342
  product_url: https://peptideatlas.org/builds/human/202601/coordinate_mapping.txt
- category: GraphicalInterface
  description: SBEAMS search interface for querying peptides across PeptideAtlas builds.
  format: http
  id: peptideatlas.search
  name: PeptideAtlas Peptide Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  product_url: https://db.systemsbiology.net/sbeams/cgi/PeptideAtlas/GetPeptides
- category: GraphicalInterface
  description: PeptideAtlas data repository, which holds the raw and processed datasets
    contributed to PeptideAtlas.
  format: http
  id: peptideatlas.repository
  name: PeptideAtlas Data Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  product_url: https://peptideatlas.org/repository/
- category: GraphicalInterface
  description: PASSEL (PeptideAtlas SRM Experiment Library), the PeptideAtlas component
    for submission, browsing and querying of selected reaction monitoring (SRM) experiment
    results.
  format: http
  id: peptideatlas.passel
  name: PASSEL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  product_url: https://peptideatlas.org/passel/
- category: GraphicalInterface
  description: SRMAtlas, a compendium of targeted proteomics (SRM) assays for the
    complete human proteome and other organisms, built by the PeptideAtlas team.
  format: http
  id: peptideatlas.srmatlas
  name: SRMAtlas
  original_source:
  - relation_type: prov:hadPrimarySource
    source: peptideatlas
  product_url: https://srmatlas.org/
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
    source: proteomexchange
  product_url: https://www.omicsdi.org/ws/swagger-ui/index.html
publications:
- authors:
  - F. Desiere
  doi: 10.1093/nar/gkj040
  id: doi:10.1093/nar/gkj040
  journal: Nucleic Acids Research
  preferred: true
  title: The PeptideAtlas project
  year: '2006'
- authors:
  - Eric W Deutsch
  - Henry Lam
  - Ruedi Aebersold
  doi: 10.1038/embor.2008.56
  id: doi:10.1038/embor.2008.56
  journal: The EMBO Reports
  title: 'PeptideAtlas: a resource for target selection for emerging targeted proteomics
    workflows'
  year: '2008'
- authors:
  - Ulrike Kusebauch
  - David S. Campbell
  - Eric W. Deutsch
  - Caroline S. Chu
  - Douglas A. Spicer
  - Mi-Youn Brusniak
  - Joseph Slagel
  - Zhi Sun
  - Jeffrey Stevens
  - Barbara Grimes
  - David Shteynberg
  - Michael R. Hoopmann
  - Peter Blattmann
  - Alexander V. Ratushny
  - Oliver Rinner
  - Paola Picotti
  - Christine Carapito
  - Chung-Ying Huang
  - Meghan Kapousouz
  - Henry Lam
  - Tommy Tran
  - Emek Demir
  - John D. Aitchison
  - Chris Sander
  - Leroy Hood
  - Ruedi Aebersold
  - Robert L. Moritz
  doi: 10.1016/j.cell.2016.06.041
  id: doi:10.1016/j.cell.2016.06.041
  journal: Cell
  title: 'Human SRMAtlas: A Resource of Targeted Assays to Quantify the Complete Human
    Proteome'
  year: '2016'
synonyms:
- PA
- PASSEL
- SRMAtlas
---
# PeptideAtlas

PeptideAtlas is a multi-organism compendium of peptides identified in tandem mass spectrometry (MS/MS) proteomics experiments, run by the Institute for Systems Biology (ISB) in Seattle. Public datasets, many of them deposited through ProteomeXchange repositories, are reprocessed with the Trans-Proteomic Pipeline (Comet, X!Tandem, SpectraST, PeptideProphet, ProteinProphet). Identified peptides are mapped to reference protein sequences and genome coordinates and assigned stable identifiers of the form `PAp00000001`.

## Builds

Builds are made per organism and for important sample groups, such as human plasma, urine, HLA peptidome and post-translational modification enrichments (phospho, acetyl, methyl, SUMO and ubiquitin). The build index (`main.cgi?output_format=json`) listed 110 builds on 2026-10-04. Each build has a download page with peptide FASTA files, tab-separated tables, a MySQL dump and coordinate mappings. Download URLs include the build date (for example `builds/human/202601/`), so the products here point to the Human 2026-01 build (atlas build 607) and must be updated when a new build appears.

## Related Resources

- **PASSEL** (PeptideAtlas SRM Experiment Library) accepts and shares SRM experiment results and is a ProteomeXchange member repository.
- **SRMAtlas** provides targeted proteomics assays for the human proteome and other organisms.
- **SWATHAtlas** provides spectral libraries for DIA/SWATH analysis.
- PeptideAtlas serves as a main reference for the HUPO Human Proteome Project (HPP) protein evidence levels.

## License

The site states "All Rights Reserved" in its footer and no data license was found on 2026-10-04.