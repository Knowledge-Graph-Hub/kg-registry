---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: pubmedcentral@ncbi.nlm.nih.gov
  - contact_type: url
    value: https://support.nlm.nih.gov/
  label: PubMed Central Help Desk
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.nlm.nih.gov/
  label: National Library of Medicine
creation_date: '2026-06-02T00:00:00Z'
description: PubMed Central (PMC) is NCBI's free full-text archive of biomedical and
  life-sciences journal literature, including article display, searchable records,
  article datasets, and controlled automated retrieval services for reusable PMC content.
domains:
- biomedical
- literature
homepage_url: https://pmc.ncbi.nlm.nih.gov/
id: pmc
infores_id: pubmed-central
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: PubMed Central
products:
- category: GraphicalInterface
  description: PMC web portal for searching, browsing, and reading free full-text
    biomedical and life-sciences journal articles archived by NCBI.
  format: http
  id: pmc.portal
  name: PMC Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pmc
  product_url: https://pmc.ncbi.nlm.nih.gov/
- category: Product
  description: PMC Open Access Subset containing journal articles and preprints made
    available under licenses that permit reuse, with automated retrieval through PMC-approved
    services.
  format: mixed
  id: pmc.open-access-subset
  name: PMC Open Access Subset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pmc
  product_url: https://pmc.ncbi.nlm.nih.gov/tools/openftlist
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-12: HTTP 405 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-13: HTTP 405 error
    when accessing file'
- category: Product
  description: PMC FTP service for retrieving file lists and downloadable article
    files from PMC article datasets, including the Open Access Subset.
  format: mixed
  id: pmc.ftp
  name: PMC FTP Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pmc
  product_url: https://pmc.ncbi.nlm.nih.gov/tools/ftp/
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-12: HTTP 405 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-13: HTTP 405 error
    when accessing file'
- category: ProgrammingInterface
  connection_url: https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi
  description: PMC OA Web Service API for discovering downloadable resources from
    the PMC Open Access Subset.
  format: http
  id: pmc.oa-service
  is_public: true
  name: PMC OA Web Service API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pmc
  product_url: https://pmc.ncbi.nlm.nih.gov/tools/oa-service/
- category: ProgrammingInterface
  connection_url: https://www.ncbi.nlm.nih.gov/pmc/oai/oai.cgi
  description: PMC OAI-PMH service for harvesting PMC metadata and eligible full-text
    article XML through the Open Archives Initiative Protocol for Metadata Harvesting.
  format: http
  id: pmc.oai-pmh
  is_public: true
  name: PMC OAI-PMH Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pmc
  product_url: https://pmc.ncbi.nlm.nih.gov/tools/oai/
- category: ProgrammingInterface
  connection_url: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
  description: NCBI Entrez E-utilities interface for searching and retrieving PMC
    records through the Entrez database layer.
  format: http
  id: pmc.eutils
  is_public: true
  name: PMC E-utilities API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pmc
  product_url: https://pmc.ncbi.nlm.nih.gov/tools/developers/
- category: GraphicalInterface
  description: Web interface for searching and retrieving variant information from
    35+ million PubMed articles with autocomplete, filtering, and entity highlighting
  format: http
  id: litvar.web_interface
  name: LitVar Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: litvar
  product_url: https://www.ncbi.nlm.nih.gov/research/litvar2/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: clingen
  - relation_type: prov:wasInformedBy
    source: clinvar
  - relation_type: prov:wasInformedBy
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: pmc
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:used
    source: pubtator
- category: ProgrammingInterface
  description: RESTful API providing programmatic access to variant summaries, publications,
    search, and gene-level variant queries
  format: http
  id: litvar.api
  name: LitVar API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: litvar
  product_url: https://www.ncbi.nlm.nih.gov/research/litvar2-api/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: clingen
  - relation_type: prov:wasInformedBy
    source: clinvar
  - relation_type: prov:wasInformedBy
    source: dbsnp
  - relation_type: prov:wasDerivedFrom
    source: pmc
  - relation_type: prov:wasDerivedFrom
    source: pubmed
  - relation_type: prov:used
    source: pubtator
synonyms:
- PMC
- PubMed Central
---
# PubMed Central

PubMed Central is NCBI's free full-text archive for biomedical and life-sciences
journal literature. PMC provides article display and search, reusable article
datasets, and documented automated access services for approved PMC content.