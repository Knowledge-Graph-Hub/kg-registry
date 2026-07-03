---
activity_status: active
category: DataSource
collection:
  - translator
contacts:
  - category: Organization
    id: mcgill-genepi
    label: Richards Lab (Genetic Epidemiology), McGill University
    contact_details:
      - contact_type: url
        value: https://www.mcgill.ca/genepi/
creation_date: '2026-02-18T00:00:00Z'
description: >-
  The Richards Effector Gene List (REGL) provides the results of the Effector
  Index (Ei), a machine-learning method that prioritizes the likely causal
  (effector) target genes at genome-wide association study (GWAS) loci. Developed
  by the Richards Lab at McGill University, the Ei was trained and validated
  against positive-control gene sets derived from Mendelian disease genes and
  approved drug targets across 12 common diseases and quantitative traits, using
  genomic features such as coding or transcript-altering variants, distance to
  gene, and open-chromatin-based metrics. It is integrated into the NCATS
  Biomedical Data Translator as a source for linking genetic association signals
  to their probable effector genes.
domains:
  - genomics
  - biomedical
  - drug discovery
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/Richards-Effector-Gene-List
id: regl
infores_id: regl
last_modified_date: '2026-07-02T00:00:00Z'
layout: resource_detail
name: Richards Effector Gene List
products:
  - category: DocumentationProduct
    description: Translator wiki documentation page for the Richards Effector Gene List.
    format: http
    id: regl.docs
    name: REGL Documentation
    original_source:
      - source: regl
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/NCATSTranslator/Translator-All/wiki/Richards-Effector-Gene-List
publications:
  - authors:
      - Forgetta V
      - Jiang L
      - Vulpescu NA
      - Hogan MS
      - Chen S
      - Morris JA
      - Grinek S
      - Benner C
      - Jang DK
      - Hoang Q
      - Burtt N
      - Flannick JA
      - McCarthy MI
      - Fauman E
      - Greenwood CMT
      - Maurano MT
      - Richards JB
    doi: 10.1007/s00439-022-02434-z
    id: https://www.ncbi.nlm.nih.gov/pubmed/35147782
    journal: Hum Genet
    preferred: true
    title: An effector index to predict target genes at GWAS loci
    year: '2022'
taxon:
  - NCBITaxon:9606
---

# Richards Effector Gene List

The Richards Effector Gene List (REGL) is the output of the Effector Index (Ei),
a method developed by the Richards Lab at McGill University to predict the causal
effector genes underlying signals at GWAS loci. The Ei ranks candidate genes at a
locus using genomic evidence such as coding or transcript-altering variants,
distance to gene, and open-chromatin-based features, and was validated against
Mendelian disease genes and approved drug targets across 12 common diseases and
traits. REGL is tracked in KG-Registry as a source used by the NCATS Biomedical
Data Translator for effector-gene prioritization.
