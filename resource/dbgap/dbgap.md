---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/gap/
  id: ncbi
  label: dbGaP Team, National Center for Biotechnology Information (NCBI)
creation_date: '2026-10-04T00:00:00Z'
description: The database of Genotypes and Phenotypes (dbGaP) is NCBI's archive for
  data and results from studies of the interaction of genotype and phenotype in humans,
  including genome-wide association studies, medical sequencing, molecular diagnostic
  assays and associations between genotype and non-clinical traits. Study descriptions,
  protocols, data dictionaries and summary-level variable statistics are public, while
  individual-level genotype and phenotype data are distributed through controlled
  access under data use limitations set by each study. When checked on 2026-10-04
  the public FTP site held study directories for 3,322 phs accessions.
domains:
- biomedical
- genomics
- genetic variation
- genome-wide association studies
- clinical
fairsharing_id: FAIRsharing.88v2k0
homepage_url: https://www.ncbi.nlm.nih.gov/gap/
id: dbgap
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/home/about/policies/
  label: Public Domain (U.S. Government work; NCBI and NLM Data Usage Policies) for
    public metadata; individual-level data are controlled access
name: dbGaP
products:
- category: GraphicalInterface
  description: dbGaP web portal for searching and browsing studies, variables, datasets,
    documents and analyses, with study pages linking to public summaries and to the
    controlled-access request system.
  format: http
  id: dbgap.portal
  name: dbGaP Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbgap
  product_url: https://www.ncbi.nlm.nih.gov/gap/
- category: GraphicalInterface
  description: dbGaP Advanced Search interface for faceted searching of studies by
    study design, molecular data type, consent and other attributes.
  format: http
  id: dbgap.advanced-search
  name: dbGaP Advanced Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbgap
  product_url: https://www.ncbi.nlm.nih.gov/gap/advanced_search/
- category: Product
  description: Public FTP directory of released studies, one directory per phs accession
    and version, holding GapExchange study XML, data dictionaries, variable summaries,
    release notes, manifests and study documents. Individual-level data are not included.
  format: mixed
  id: dbgap.ftp
  name: dbGaP Public Study Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbgap
  product_url: https://ftp.ncbi.nlm.nih.gov/dbgap/studies/
- category: Product
  description: Public FTP directory of GWAS analysis results and summary statistics
    released through dbGaP.
  format: mixed
  id: dbgap.gwas-analysis
  name: dbGaP GWAS Analysis Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbgap
  product_url: https://ftp.ncbi.nlm.nih.gov/dbgap/gwas_analysis/
- category: ProgrammingInterface
  description: dbGaP Study Metadata (SSTR) API returning JSON summaries of a study
    version, including name, BioProject links and consent groups, for example /api/v1/study/phs000001.v3.p1/summary.
  format: http
  id: dbgap.sstr-api
  name: dbGaP Study Metadata API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbgap
  product_url: https://www.ncbi.nlm.nih.gov/gap/sstr/
- category: ProgrammingInterface
  description: dbGaP FHIR API exposing study, subject and phenotype metadata as HL7
    FHIR resources; open studies are public and controlled studies require authorization.
  format: http
  id: dbgap.fhir-api
  name: dbGaP FHIR API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbgap
  product_url: https://dbgap-api.ncbi.nlm.nih.gov/fhir/x1/metadata
  repository: https://github.com/ncbi/DbGaP-FHIR-API-Docs
- category: GraphicalInterface
  description: dbGaP Authorized Access system, where approved investigators submit
    data access requests and download controlled-access individual-level data. Requires
    an eRA Commons or NIH login.
  format: http
  id: dbgap.authorized-access
  name: dbGaP Authorized Access
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbgap
  product_url: https://dbgap.ncbi.nlm.nih.gov/aa/wga.cgi?page=login
- category: DocumentationProduct
  description: dbGaP Study Submission Guide describing submission, data dictionaries,
    consent and file formats.
  format: http
  id: dbgap.submission-guide
  name: dbGaP Study Submission Guide
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dbgap
  product_url: https://www.ncbi.nlm.nih.gov/gap/docs/submissionguide/
- category: Product
  description: Individual-level genotype and phenotype data available through dbGaP
  format: vcf
  id: gtex.dbgap-data
  name: GTEx dbGaP Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtex
  product_url: https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000424
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: dbgap
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
  - Matthew D Mailman
  - Michael Feolo
  - Yumi Jin
  - Masato Kimura
  - Kimberly Tryka
  - Rinat Bagoutdinov
  - Luning Hao
  - Anne Kiang
  - Justin Paschall
  - Lon Phan
  - Natalia Popova
  - Stephanie Pretel
  - Lora Ziyabari
  - Moira Lee
  - Yu Shao
  - Zhen Y Wang
  - Karl Sirotkin
  - Minghong Ward
  - Michael Kholodov
  - Kerry Zbicz
  - Jeffrey Beck
  - Michael Kimelman
  - Sergey Shevelev
  - Don Preuss
  - Eugene Yaschenko
  - Alan Graeff
  - James Ostell
  - Stephen T Sherry
  doi: 10.1038/ng1007-1181
  id: doi:10.1038/ng1007-1181
  journal: Nature Genetics
  preferred: true
  title: The NCBI dbGaP database of genotypes and phenotypes
  year: '2007'
- authors:
  - Kimberly A. Tryka
  - Luning Hao
  - Anne Sturcke
  - Yumi Jin
  - Zhen Y. Wang
  - Lora Ziyabari
  - Moira Lee
  - Natalia Popova
  - Nataliya Sharopova
  - Masato Kimura
  - Michael Feolo
  doi: 10.1093/nar/gkt1211
  id: doi:10.1093/nar/gkt1211
  journal: Nucleic Acids Research
  title: 'NCBI’s Database of Genotypes and Phenotypes: dbGaP'
  year: '2014'
synonyms:
- database of Genotypes and Phenotypes
- NCBI dbGaP
taxon:
- NCBITaxon:9606
---
# dbGaP

The database of Genotypes and Phenotypes (dbGaP) was developed by NCBI to archive and distribute the data and results of studies that investigate the interaction of genotype and phenotype in humans. It holds genome-wide association studies, medical sequencing and clinical studies, and molecular data from programs such as GTEx, TOPMed and Kids First.

## Access Tiers

- **Public**: study descriptions, protocols, questionnaires, data dictionaries, variable summaries and some GWAS analysis results. These are browsable on the portal and downloadable from the public FTP site.
- **Controlled access**: de-identified individual-level genotypes and phenotypes. Investigators apply through dbGaP Authorized Access, and each request is reviewed by a Data Access Committee against the study's consent groups and data use limitations.

## Accessions

Studies have `phs` accessions with version and participant set (for example `phs000001.v3.p1`). Datasets, variables, documents and analyses have `pht`, `phv`, `phd` and `pha` accessions.

## Programmatic Access

The Study Metadata (SSTR) API returns JSON study summaries, and the dbGaP FHIR API exposes study and phenotype metadata as FHIR resources. The public FTP site mirrors released study metadata by accession.