---
activity_status: inactive
category: DataSource
creation_date: '2026-06-02T00:00:00Z'
description: EHRLink is a drug-indication evidence source derived from a study in
  which clinicians linked prescribed medications to clinical problems in an electronic
  health record workflow; PharmacotherapyDB later processed these relationships for
  indication catalog construction.
domains:
- clinical
- biomedical
- pharmacology
homepage_url: https://github.com/dhimmel/indications/tree/gh-pages/ehrlink
id: ehrlink
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: EHRLink
products:
- category: Product
  description: PharmacotherapyDB processing workspace for EHRLink medication-problem
    association data, including notebooks for converting, mapping, and preparing EHRLink-derived
    indications.
  id: ehrlink.pharmacotherapydb-processing
  name: EHRLink PharmacotherapyDB Processing Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ehrlink
  product_url: https://github.com/dhimmel/indications/tree/gh-pages/ehrlink
  repository: https://github.com/dhimmel/indications
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: pharmacotherapydb
- category: DocumentationProduct
  description: Publication describing the crowdsourcing methodology used to identify
    relationships between clinical problems and medications in EHRLink.
  id: ehrlink.publication
  name: EHRLink Methodology Publication
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ehrlink
  product_url: https://doi.org/10.1136/amiajnl-2012-000852
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-12: HTTP 403 error
    when accessing file'
- category: Product
  description: Curated TSV catalog of drug-disease indications classified as disease-modifying,
    symptomatic, or non-indications
  format: tsv
  id: pharmacotherapydb.indications
  name: PharmacotherapyDB Indications TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  product_file_size: 76754
  product_url: https://raw.githubusercontent.com/dhimmel/indications/gh-pages/catalog/indications.tsv
  secondary_source:
  - relation_type: prov:used
    source: doid
  - relation_type: prov:used
    source: drugbank
  - relation_type: prov:wasInformedBy
    source: labeledin
  - relation_type: prov:wasInformedBy
    source: medi
  - relation_type: prov:wasInformedBy
    source: ehrlink
  - relation_type: prov:wasInformedBy
    source: predict
publications:
- authors:
  - Allison B McCoy
  - Adam Wright
  - Archana Laxmisan
  - Madelene J Ottosen
  - Jacob A McCoy
  - David Butten
  - Dean F Sittig
  doi: 10.1136/amiajnl-2012-000852
  id: doi:10.1136/amiajnl-2012-000852
  journal: Journal of the American Medical Informatics Association
  preferred: true
  title: 'Development and evaluation of a crowdsourcing methodology for knowledge
    base construction: identifying relationships between clinical problems and medications'
  year: '2012'
repository: https://github.com/dhimmel/indications
warnings:
- EHRLink does not appear to have a maintained standalone public portal; the registry
  entry points to the source publication and PharmacotherapyDB processing materials.
---
# EHRLink

EHRLink is an indication evidence source based on clinician-entered links between
clinical problems and medications in an electronic health record setting. The
data are represented in PharmacotherapyDB processing materials and inform the
PharmacotherapyDB indication catalog.