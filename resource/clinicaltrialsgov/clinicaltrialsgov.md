---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: ClinicalTrials.gov@nih.gov
  - contact_type: url
    value: https://clinicaltrials.gov/about-site/contact
  id: ncbi
  label: National Library of Medicine Clinical Trials Team
- category: Organization
  contact_details:
  - contact_type: email
    value: register@clinicaltrials.gov
  label: ClinicalTrials.gov Help Desk
creation_date: '2025-05-28T00:00:00Z'
description: ClinicalTrials.gov is a database of privately and publicly funded clinical
  studies conducted around the world, maintained by the National Library of Medicine
  (NLM) at the National Institutes of Health (NIH). The registry contains information
  on over 400,000 studies covering a wide range of diseases and conditions, providing
  details about study design, locations, eligibility criteria, interventions, outcomes,
  and results. ClinicalTrials.gov serves as the primary registry for clinical trials
  required by the FDA Amendments Act and WHO International Clinical Trials Registry
  Platform (ICTRP).
domains:
- clinical
- biomedical
- public health
- drug discovery
- precision medicine
fairsharing_id: FAIRsharing.mewhad
homepage_url: https://clinicaltrials.gov/
id: clinicaltrialsgov
infores_id: clinicaltrials
last_modified_date: '2026-05-27T00:00:00Z'
layout: resource_detail
license:
  id: https://clinicaltrials.gov/about-site/terms-conditions
  label: Public Domain
name: ClinicalTrials.gov
products:
- category: GraphicalInterface
  description: Web-based interface for searching and browsing clinical trials with
    advanced filtering and export capabilities
  format: http
  id: clinicaltrialsgov.search
  name: ClinicalTrials.gov Search Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  product_url: https://clinicaltrials.gov/search
- category: ProgrammingInterface
  description: RESTful API providing programmatic access to all clinical trial records
    with JSON and CSV output formats
  format: http
  id: clinicaltrialsgov.api
  is_public: true
  name: ClinicalTrials.gov API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  product_url: https://clinicaltrials.gov/data-api/api
- category: Product
  description: Bulk downloads of all clinical trial records in multiple formats including
    XML, JSON, and CSV
  format: mixed
  id: clinicaltrialsgov.downloads
  name: ClinicalTrials.gov Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  product_url: https://clinicaltrials.gov/data-about-studies/download-clinical-trial-data
- category: Product
  description: Aggregate Analysis of ClinicalTrials.gov (AACT) - A relational PostgreSQL
    database containing all clinical trial data, updated daily
  format: postgres
  id: clinicaltrialsgov.aact
  name: AACT Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: aact
  product_url: https://aact.ctti-clinicaltrials.org/
- category: DocumentationProduct
  description: Comprehensive documentation covering data structure, data element definitions,
    and API usage
  format: http
  id: clinicaltrialsgov.docs
  name: ClinicalTrials.gov Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  product_url: https://clinicaltrials.gov/about-site
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  format: http
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: metacyc
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: protcid
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: spoke
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://spoke.ucsf.edu/data-tools
- category: GraphProduct
  description: DisGeNET data, including gene to disease associations and variant to
    disease associations (requires registration and subscription).
  id: disgenet.data
  name: DisGeNET Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: mgd
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: psygenet
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: phewascat
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: finngen
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  product_url: https://www.disgenet.com/
- category: ProcessProduct
  description: INDRA CoGEx is a graph database integrating causal relations, ontological
    relations, properties, and data, assembled at scale automatically from the scientific
    literature and structured sources. This is the code to build the graph.
  id: indra.cogex.code
  name: INDRA CoGEx Build Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: indra
  product_url: https://github.com/gyorilab/indra_cogex
- category: Product
  description: Complete RepoDB dataset containing drug repositioning successes and
    failures, with approved drugs, indications, and clinical trial outcomes
  format: csv
  id: repodb.full_dataset
  name: RepoDB Full Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: repodb
  product_url: https://unmtid-shinyapps.net/shiny/repodb/session/98046b0f66cea75c432b5576c1ba2840/download/downloadFull?w=
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-10-27_ HTTP 500 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-08-07_ No Content-Length
    header found
  - 'File was not able to be retrieved when checked on 2026-06-16: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-17: HTTP 404 error
    when accessing file'
- category: Product
  description: Clinical trial information from ClinicalTrials.gov
  format: http
  id: genecards.clinical.trials
  name: GeneCards Clinical Trials
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: genecards
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
- category: Product
  description: Cloud-based PostgreSQL database with daily refreshed clinical trial
    data, accessible via standard PostgreSQL clients
  format: postgres
  id: aact.database
  name: AACT Cloud Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aact
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  product_url: https://aact.ctti-clinicaltrials.org/connect
- category: Product
  description: Static downloadable copies of the complete AACT database
  format: postgres
  id: aact.downloads
  name: AACT Database Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aact
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  product_url: https://aact.ctti-clinicaltrials.org/downloads
- category: Product
  compression: gzip
  description: clinicaltrials OBO
  format: obo
  id: obo-db-ingest.clinicaltrialsgov.obo
  license:
    id: https://clinicaltrials.gov/about-site/terms-conditions#availability
    label: Custom
  name: clinicaltrials OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 41571299
  product_url: https://w3id.org/biopragmatics/resources/clinicaltrials/clinicaltrials.obo.gz
- category: Product
  compression: gzip
  description: clinicaltrials OWL
  format: owl
  id: obo-db-ingest.clinicaltrialsgov.owl
  license:
    id: https://clinicaltrials.gov/about-site/terms-conditions#availability
    label: Custom
  name: clinicaltrials OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 40291602
  product_url: https://w3id.org/biopragmatics/resources/clinicaltrials/clinicaltrials.owl.gz
- category: Product
  compression: gzip
  description: clinicaltrials OBO Graph JSON
  format: json
  id: obo-db-ingest.clinicaltrialsgov.json
  license:
    id: https://clinicaltrials.gov/about-site/terms-conditions#availability
    label: Custom
  name: clinicaltrials OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 40813205
  product_url: https://w3id.org/biopragmatics/resources/clinicaltrials/clinicaltrials.json.gz
- category: MappingProduct
  description: clinicaltrials SSSOM
  format: sssom
  id: obo-db-ingest.clinicaltrialsgov.sssom.tsv
  license:
    id: https://clinicaltrials.gov/about-site/terms-conditions#availability
    label: Custom
  name: clinicaltrials SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 6299996
  product_url: https://w3id.org/biopragmatics/resources/clinicaltrials/clinicaltrials.sssom.tsv
- category: Product
  description: clinicaltrials Nodes TSV
  format: tsv
  id: obo-db-ingest.clinicaltrialsgov.tsv
  license:
    id: https://clinicaltrials.gov/about-site/terms-conditions#availability
    label: Custom
  name: clinicaltrials Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 19140027
  product_url: https://w3id.org/biopragmatics/resources/clinicaltrials/clinicaltrials.tsv
- category: Product
  description: Raw format target information including all TTD target data
  format: txt
  id: ttd.targets-raw
  name: TTD Targets Information
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-01-TTD_target_download.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-29_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Drug to disease mapping with ICD identifiers
  format: txt
  id: ttd.drug-disease
  name: Drug-Disease Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-05-Drug_disease.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-30_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Target to disease mapping with ICD identifiers
  format: txt
  id: ttd.target-disease
  name: Target-Disease Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-06-Target_disease.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Target to drug mapping with mode of action information
  format: csv
  id: ttd.target-drug
  name: Target-Drug Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-07-Drug-TargetMapping.xlsx
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Biomarker to disease mapping with ICD identifiers
  format: txt
  id: ttd.biomarker-disease
  name: Biomarker-Disease Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-08-Biomarker_disease.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: Product
  description: Target to compound mapping with experimental activity data
  format: txt
  id: ttd.target-compound
  name: Target-Compound Activity Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: pubmed
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P1-09-Target_compound_activity.txt
  warnings:
  - File was not able to be retrieved when checked on 2025-10-31_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: GraphProduct
  compatibility:
  - standard: biolink
    version: 4.3.6
  description: KGX JSONL graph package for CTKP distributed via the NCATS Translator
    release site (release 2026_03_27; build ctkp_3.1.37_a99268cc_2025sep1_4.3.6; source
    version 3.1.37; Biolink 4.3.6; Node Normalizer 2025sep1).
  edge_count: 438575
  format: kgx-jsonl
  id: translator.ctkp.graph
  latest_version: '2026_03_27'
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Translator CTKP KGX Graph
  node_count: 41243
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ctkp
  - relation_type: prov:hadPrimarySource
    source: translator
  product_url: https://kgx-storage.rtx.ai/releases/ctkp/latest/
  versions:
  - '2026_03_27'
  - ctkp_3.1.37_a99268cc_2025sep1_4.3.6
- category: Product
  compression: zip
  description: Pipe-delimited text exports of the AACT database for import into databases
    or analysis tools
  format: csv
  id: aact.pipe_delimited
  name: AACT Pipe-Delimited Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aact
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  product_url: https://aact.ctti-clinicaltrials.org/downloads
- category: Product
  description: Alzheimer's disease case study drug repurposing predictions
  format: csv
  id: kg-predict.ad_predictions
  name: AD Drug Predictions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-predict
  product_file_size: 44034
  product_url: https://nlp.case.edu/public/data/GPKG-Predict/case_study_predict_results.csv
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: clinicaltrialsgov
- category: Product
  description: Alzheimer's disease National Clinical Trial evidence file used with
    the KG-Predict case study
  format: csv
  id: kg-predict.ad_nct_evidence
  name: AD National Clinical Trial Evidence
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-predict
  product_file_size: 1789
  product_url: https://nlp.case.edu/public/data/GPKG-Predict/ad_nct_evidence.csv
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: clinicaltrialsgov
- category: GraphProduct
  description: Source CSV tables for AcuKG, including acupoint therapeutic actions,
    indications, anatomy relationships, clinical trial links, and PubMed links.
  edge_count: 11527
  format: csv
  id: acukg.csv
  name: AcuKG CSV tables
  node_count: 1839
  original_source:
  - relation_type: prov:hadPrimarySource
    source: acukg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:used
    source: mesh
  - relation_type: prov:used
    source: uberon
  - relation_type: prov:used
    source: snomedct
  product_url: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture/tree/main/AcuKG
- category: GraphProduct
  description: RDF Turtle representation of AcuKG relationship tables.
  edge_count: 11527
  format: ttl
  id: acukg.rdf
  name: AcuKG RDF Turtle files
  node_count: 1839
  original_source:
  - relation_type: prov:hadPrimarySource
    source: acukg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:used
    source: mesh
  - relation_type: prov:used
    source: uberon
  - relation_type: prov:used
    source: snomedct
  product_url: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture/tree/main/AcuKG_RDF
- category: GraphProduct
  description: JSON representation of AcuKG relationship tables.
  edge_count: 11527
  format: json
  id: acukg.json
  name: AcuKG JSON files
  node_count: 1839
  original_source:
  - relation_type: prov:hadPrimarySource
    source: acukg
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:used
    source: mesh
  - relation_type: prov:used
    source: uberon
  - relation_type: prov:used
    source: snomedct
  product_url: https://github.com/yimingli99/AcuKG-Knowledge-graph-for-medical-acupuncture/tree/main/AcuKG_json
- category: GraphProduct
  description: Multilayer epilepsy knowledge graph generated by the myAURA data processing
    workflow from biomedical, clinical, literature, and patient-centered data sources.
  id: myaura.graph
  name: myAURA epilepsy knowledge graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: myaura
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: web-of-science
  product_url: https://github.com/cns-iu/myaura
- category: ProgrammingInterface
  description: REST API for searching identifiers and special keywords, mapping between
    data sources with a chain-query syntax, and retrieving entries across the integrated
    BioBTree databases.
  format: http
  id: biobtree.api
  is_public: true
  name: BioBTree REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: bao
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: brenda
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: collectri
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://sugi.bio/biobtree/api/
- category: GraphicalInterface
  description: Web-based interface for searching and browsing comprehensive gene-centric
    information integrating data from over 200 sources
  format: http
  id: genecards.web.interface
  name: GeneCards Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: aminode
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: cdd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: craft
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: fabric
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: gard
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: geneorganizer
  - relation_type: prov:hadPrimarySource
    source: genomernai
  - relation_type: prov:hadPrimarySource
    source: glyconnect
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: humancyc
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: iid
  - relation_type: prov:hadPrimarySource
    source: imgt
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadisease
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: nextprot
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pirsf
  - relation_type: prov:hadPrimarySource
    source: prosite
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  - relation_type: prov:hadPrimarySource
    source: proteopedia
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: scop
  - relation_type: prov:hadPrimarySource
    source: sfld
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: treefam
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ucnebase
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vista
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_url: https://www.genecards.org/
publications:
- authors:
  - Zarin DA
  - Tse T
  - Williams RJ
  - Califf RM
  - Ide NC
  doi: doi:10.1056/NEJMsa1012065
  id: https://pubmed.ncbi.nlm.nih.gov/21366476/
  journal: The New England Journal of Medicine
  preferred: true
  title: The ClinicalTrials.gov results database--update and key issues
  year: '2011'
repository: https://github.com/ctti-clinicaltrials/aact
taxon:
- NCBITaxon:9606
---
# ClinicalTrials.gov

## Overview

ClinicalTrials.gov is a comprehensive database of clinical studies conducted in the United States and around the world. Maintained by the National Library of Medicine (NLM) at the National Institutes of Health (NIH), it provides the public with easy access to information on publicly and privately supported clinical studies on a wide range of diseases and conditions.

The resource was established in 2000 in response to the Food and Drug Administration Modernization Act of 1997 (FDAMA). The database was expanded in response to the Food and Drug Administration Amendments Act of 2007 (FDAAA) to include more comprehensive trial registration data and basic results reporting. The system continues to evolve to improve transparency in clinical research and provide valuable information to researchers, healthcare providers, and patients.

## Content and Coverage

### Study Types
- **Interventional Studies**: Trials testing new treatments, drugs, devices, or behavioral interventions
- **Observational Studies**: Studies examining health outcomes in specific populations without intervention
- **Expanded Access**: Investigational treatments available outside of clinical trials
- **Patient Registries**: Collections of patient health information for specific diseases or conditions

### Data Elements
Each clinical trial record includes:
- Study identification and registration information
- Study title and summary
- Study design and methodology
- Eligibility criteria (inclusion/exclusion)
- Interventions and comparators
- Outcome measures (primary and secondary)
- Study locations and contact information
- Study start and completion dates
- Participant demographics
- Results data (when available)
- Adverse events
- Publications and references

### Coverage Statistics
- **400,000+** registered clinical studies
- **220+ countries** represented
- **All 50 US states** plus territories
- **Daily updates** with new and modified records

## Regulatory Context

ClinicalTrials.gov serves as the primary registry for:
- FDA Amendments Act (FDAAA) Section 801 compliance
- WHO International Clinical Trials Registry Platform (ICTRP)
- International Committee of Medical Journal Editors (ICMJE) requirements
- Support for regulatory compliance with trial registration and results reporting requirements

## Data Access Methods

### Web Interface
The primary search portal allows:
- Advanced search with multiple filters
- Geographic visualization of study locations
- Export of search results
- Study comparison tools
- Linkage to published literature via PubMed

### REST API
The ClinicalTrials.gov API provides:
- Programmatic access to all trial records
- JSON and CSV output formats
- Field-level queries
- Pagination for large result sets
- Rate limiting: No authentication required for reasonable use

### Bulk Downloads
Complete database exports available in:
- XML format (pipe-delimited files)
- JSON format
- CSV format
- Daily and monthly update files

### AACT Database
The Aggregate Analysis of ClinicalTrials.gov (AACT) database:
- Relational PostgreSQL database
- Daily updates from ClinicalTrials.gov
- Optimized for aggregate analysis and research
- Free access with straightforward schema
- Maintained by the Clinical Trials Transformation Initiative (CTTI)
- Code repository: https://github.com/ctti-clinicaltrials/aact

## Use Cases

1. **Patient Recruitment**: Finding eligible clinical trials for specific conditions
2. **Research**: Analyzing trends in clinical research and drug development
3. **Systematic Reviews**: Identifying all trials for meta-analyses
4. **Regulatory Compliance**: Meeting trial registration requirements
5. **Transparency**: Public access to study designs and results
6. **Competitive Intelligence**: Tracking clinical development pipelines
7. **Public Health**: Monitoring research activity for specific diseases

## Data Quality and Compliance

- Study sponsors and investigators are responsible for data accuracy
- Results must be submitted within one year of study completion (FDAAA requirement)
- NLM performs quality control checks but does not independently verify all data
- Records marked with data quality issues or non-compliance indicators

## Information Resource ID

This resource has the Information Resource identifier: `infores:clinicaltrials`

## Important Notes

- **Registration is not approval**: Listing a study does not mean it has been evaluated by the US Federal Government
- **Results may be incomplete**: Not all studies are required to submit results
- **Contact study sites**: For participation, contact information is provided in each record
- **Updates**: Records are maintained by study sponsors and may be updated throughout the study lifecycle