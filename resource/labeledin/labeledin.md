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
description: LabeledIn is a human-reviewed, machine-readable, source-linked catalog of labeled indications for human drugs derived from FDA drug labels made available through DailyMed. It links 7,805 drug-disease treatment relationships to UMLS disease concepts and RxNorm drug identifiers, and was extended with a crowdsourced annotation set covering a further 706 drug labels.
domains:
  - pharmacology
  - clinical
  - biomedical
homepage_url: https://ftp.ncbi.nlm.nih.gov/pub/lu/LabeledIn/
id: labeledin
last_modified_date: '2026-11-10T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: U.S. Government Work (public domain)
name: LabeledIn
products:
  - category: Product
    description: Pipe-delimited structured LabeledIn results (September 2014 release), with one row per annotated drug label giving the DailyMed SPL Set ID, UMLS CUIs for the annotated indications, and linked RxNorm ingredient, dose form, and clinical drug RXCUIs.
    format: txt
    id: labeledin.indications
    name: LabeledIn Structured Indications
    original_source:
      - relation_type: prov:hadPrimarySource
        source: labeledin
    product_file_size: 70793
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/lu/LabeledIn/LabeledIn_Structured_Results.txt
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: dailymed
      - relation_type: prov:used
        source: rxnorm
      - relation_type: prov:used
        source: umls
  - category: Product
    description: LabeledIn annotated corpus in pipe-delimited form, containing the Indications and Usage section of each DailyMed drug label with expert indication mentions marked up in inline XML tags carrying UMLS CUIs.
    format: txt
    id: labeledin.annotated-xml
    name: LabeledIn Annotated XML Corpus
    original_source:
      - relation_type: prov:hadPrimarySource
        source: labeledin
    product_file_size: 977027
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/lu/LabeledIn/LabeledIn_annotated_XML.txt
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: dailymed
      - relation_type: prov:used
        source: rxnorm
      - relation_type: prov:used
        source: umls
  - category: GraphicalInterface
    description: Single-page HTML view of the LabeledIn corpus that visually presents the annotated drug labels and their linked indications.
    format: http
    id: labeledin.corpus-html
    name: LabeledIn Visual HTML Corpus
    original_source:
      - relation_type: prov:hadPrimarySource
        source: labeledin
    product_file_size: 2275981
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/lu/LabeledIn/LabeledIn_corpus.html
  - category: Product
    description: Crowdsourced LabeledIn extension (2015) in pipe-delimited structured form, covering 3,004 Amazon Mechanical Turk tasks over 706 DailyMed drug labels, with UMLS CUIs, RxNorm RXCUIs, and the majority-vote indication judgement. Annotated XML and HTML versions and answer codes are in the same directory.
    format: txt
    id: labeledin.crowdsourced
    name: LabeledIn Crowdsourced Indications
    original_source:
      - relation_type: prov:hadPrimarySource
        source: labeledin
    product_file_size: 360250
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/lu/LabeledIn/Crowdsourcing/Crowdsourced_Results.txt
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: dailymed
      - relation_type: prov:used
        source: rxnorm
      - relation_type: prov:used
        source: umls
  - category: DocumentationProduct
    description: Annotation guidelines used by the expert annotators to mark drug indications in FDA drug label text for LabeledIn.
    format: pdf
    id: labeledin.guidelines
    name: LabeledIn Annotation Guidelines
    original_source:
      - relation_type: prov:hadPrimarySource
        source: labeledin
    product_file_size: 273880
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/lu/LabeledIn/Annotation_Guidelines.pdf
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
  - authors:
      - Ritu Khare
      - John D. Burger
      - John S. Aberdeen
      - David W. Tresner-Kirsch
      - Theodore J. Corrales
      - Lynette Hirschman
      - Zhiyong Lu
    doi: 10.1093/database/bav016
    id: doi:10.1093/database/bav016
    journal: Database
    title: Scaling drug indication curation through crowdsourcing
    year: '2015'
warnings:
  - LabeledIn has not been updated since its 2014 release (crowdsourced extension 2015). Annotations are based on the August 28, 2012 DailyMed release, so indications and SPL Set IDs may not reflect current drug labels.
---

# LabeledIn

LabeledIn is a human-reviewed drug indication catalog built by the NCBI
text-mining group (Zhiyong Lu lab) from the Indications and Usage sections of
FDA drug labels in DailyMed (August 28, 2012 release). Indication mentions
were found by automatic disease recognition and then reviewed by expert
annotators. Each indication is normalized to a UMLS concept, and each drug label
is linked to RxNorm identifiers at the ingredient, ingredient plus dose form, and
clinical drug levels. The core set covers 250 drugs frequently accessed in
PubMed Health (500 unique DailyMed labels) and contains 7,805 drug-disease
treatment relationships, with drugs represented by ingredient, dose form, and
strength.

The September 2014 release is distributed from the NCBI FTP site in three
formats: a pipe-delimited structured results file, a pipe-delimited file of
label text with inline XML annotations, and a visual HTML corpus. Annotation
guidelines and overview slides are also provided. A 2015 crowdsourced
extension (Crowdsourcing/ subdirectory) covers 706 more drug labels annotated
through Amazon Mechanical Turk.

The data carries an NCBI public domain notice (U.S. Government Work). LabeledIn
is one of the indication evidence sources aggregated in PharmacotherapyDB.
