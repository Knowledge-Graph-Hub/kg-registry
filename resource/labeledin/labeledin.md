---
activity_status: inactive
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.ncbi.nlm.nih.gov/
    label: National Center for Biotechnology Information
creation_date: '2026-06-02T00:00:00Z'
description: LabeledIn is a human-reviewed, machine-readable, source-linked catalog of labeled indications for human drugs derived from FDA drug labels made available through DailyMed.
domains:
  - pharmacology
  - clinical
  - biomedical
homepage_url: https://doi.org/10.1016/j.jbi.2014.08.004
id: labeledin
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: U.S. Government Work (public domain)
name: LabeledIn
products:
  - category: Product
    description: LabeledIn indication corpus described in the source publication, containing human-reviewed drug-disease treatment relationships with links back to source drug labels.
    format: http
    id: labeledin.indications
    name: LabeledIn Drug Indication Corpus
    original_source:
      - relation_type: prov:hadPrimarySource
        source: labeledin
    product_url: https://doi.org/10.1016/j.jbi.2014.08.004
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: dailymed
      - relation_type: prov:used
        source: rxnorm
  - category: DocumentationProduct
    description: Publication describing the LabeledIn corpus construction workflow, including drug label selection, automatic disease recognition, and manual indication annotation.
    format: http
    id: labeledin.publication
    name: LabeledIn Publication
    original_source:
      - relation_type: prov:hadPrimarySource
        source: labeledin
    product_url: https://doi.org/10.1016/j.jbi.2014.08.004
  - category: Product
    description: Curated TSV catalog of drug-disease indications classified as disease-modifying, symptomatic, or non-indications
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
      - Ritu Khare
      - Jiao Li
      - Zhiyong Lu
    doi: 10.1016/j.jbi.2014.08.004
    id: doi:10.1016/j.jbi.2014.08.004
    journal: Journal of Biomedical Informatics
    preferred: true
    title: 'LabeledIn: Cataloging labeled indications for human drugs'
    year: '2014'
warnings:
  - The original LabeledIn data distribution is not clearly maintained as a standalone portal; PharmacotherapyDB preserves processed LabeledIn indication evidence.
---

# LabeledIn

LabeledIn is a human-reviewed drug indication corpus built from DailyMed drug
labels. It records drug-disease treatment relationships and source label context,
and it is used as one indication evidence source in PharmacotherapyDB.
