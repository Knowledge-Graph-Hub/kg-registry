---
activity_status: inactive
category: DataSource
creation_date: '2026-06-02T00:00:00Z'
description: PREDICT is a computational drug-indication inference method and associated
  drug-disease gold-standard dataset introduced by Gottlieb and colleagues for large-scale
  drug repositioning and personalized medicine applications.
domains:
- drug discovery
- pharmacology
- biomedical
homepage_url: https://www.embopress.org/doi/abs/10.1038/msb.2011.26
id: predict
last_modified_date: '2026-06-22T00:00:00Z'
layout: resource_detail
name: PREDICT
products:
- category: DocumentationProduct
  description: Open-access Molecular Systems Biology article describing the PREDICT
    drug-indication inference method, its drug-disease gold standard, validation,
    and personalized medicine application.
  format: http
  id: predict.article
  name: PREDICT Article
  original_source:
  - relation_type: prov:hadPrimarySource
    source: predict
  product_url: https://www.embopress.org/doi/abs/10.1038/msb.2011.26
  warnings: []
- category: ProcessProduct
  description: PREDICT computational method for large-scale prediction of drug indications
    using drug-drug and disease-disease similarity measures and known drug-disease
    associations.
  format: http
  id: predict.method
  name: PREDICT Drug-Indication Inference Method
  original_source:
  - relation_type: prov:hadPrimarySource
    source: predict
  product_url: https://www.embopress.org/doi/abs/10.1038/msb.2011.26
  secondary_source:
  - relation_type: prov:used
    source: drugbank
  - relation_type: prov:used
    source: mesh
  - relation_type: prov:used
    source: omim
  warnings: []
- category: Product
  description: Supporting information for the PREDICT study, including supplementary
    tables and data supporting the drug-disease association gold standard and prediction
    analyses.
  format: mixed
  id: predict.supporting-information
  name: PREDICT Supporting Information
  original_source:
  - relation_type: prov:hadPrimarySource
    source: predict
  product_url: https://www.embopress.org/doi/suppl/10.1038/msb.2011.26
  secondary_source:
  - relation_type: prov:used
    source: drugbank
  - relation_type: prov:used
    source: mesh
  - relation_type: prov:used
    source: omim
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-24: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-16: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-06-25: HTTP 404 error
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
  - Assaf Gottlieb
  - Gideon Y Stein
  - Eytan Ruppin
  - Roded Sharan
  doi: 10.1038/msb.2011.26
  id: doi:10.1038/msb.2011.26
  journal: Molecular Systems Biology
  preferred: true
  title: PREDICT, a method for inferring novel drug indications with application to
    personalized medicine
  year: '2011'
warnings:
- No separately maintained PREDICT web database was identified; this entry is curated
  from the 2011 article and supporting information.
---
# PREDICT

PREDICT is a drug-indication inference method and supporting dataset from
Gottlieb and colleagues. It is used as one of the evidence sources informing
PharmacotherapyDB's indication catalog.