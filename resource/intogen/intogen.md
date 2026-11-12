---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://bbglab.irbbarcelona.org
  - contact_type: github
    value: bbglab
  label: Barcelona Biomedical Genomics Lab (bbglab), IRB Barcelona
creation_date: '2026-11-12T00:00:00Z'
description: IntOGen is a framework and web platform that identifies mutational cancer
  driver genes by running a pipeline of complementary driver discovery methods over
  somatic mutation data from tumor cohorts, and publishes the resulting Compendium
  of Cancer Genes. The 2024.09.20 release analyzes 271 cohorts (about 33,000 tumor
  samples across 87 cancer types) from sources such as TCGA, PCAWG, ICGC, the Hartwig
  Medical Foundation, St. Jude, and CPTAC, and reports 633 driver genes with their
  mutational features, combined significance, and consensus mode of action per cohort.
domains:
- biomedical
- cancer
- genomics
- genetic variation
- precision medicine
homepage_url: https://www.intogen.org/
id: intogen
last_modified_date: '2026-11-12T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: IntOGen
products:
- category: GraphicalInterface
  description: Web interface for searching and browsing cancer driver genes, cohorts,
    cancer types, and mutation distributions in the current IntOGen release.
  format: http
  id: intogen.portal
  is_public: true
  name: IntOGen Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: intogen
  product_url: https://www.intogen.org/search
- category: Product
  compression: zip
  description: Compendium of Cancer Genes from the current IntOGen release, containing
    the catalog of driver genes (Compendium_Cancer_Genes.tsv) and the unfiltered driver
    results (Unfiltered_drivers.tsv) across all analyzed cohorts, with tumor type,
    mutated samples, method-specific and combined significance, and mode of action.
    Cohorts are drawn from TCGA, PCAWG, ICGC, Hartwig Medical Foundation, and other
    sequencing projects; genes are annotated with Ensembl canonical transcripts and
    the COSMIC Cancer Gene Census.
  format: tsv
  id: intogen.drivers
  is_public: true
  latest_version: '2024.09.20'
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: IntOGen Compendium of Cancer Genes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: intogen
  - relation_type: prov:hadPrimarySource
    source: tcga
  - relation_type: prov:hadPrimarySource
    source: icgc
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: cosmic
  product_file_size: 964758
  product_url: https://www.intogen.org/download?file=IntOGen-Drivers-20240920.zip
- category: Product
  compression: zip
  description: Table of the cohorts analyzed in the current IntOGen release (cohorts.tsv),
    with cancer type, data source, sequencing platform, literature reference, treatment
    status, and sample and mutation counts for each cohort.
  format: tsv
  id: intogen.cohorts
  is_public: true
  latest_version: '2024.09.20'
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: IntOGen Cohorts Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: intogen
  - relation_type: prov:hadPrimarySource
    source: tcga
  - relation_type: prov:hadPrimarySource
    source: icgc
  product_file_size: 13918
  product_url: https://www.intogen.org/download?file=IntOGen-Cohorts-20240920.zip
- category: ProcessProduct
  description: Source code of the IntOGen pipeline (intogen-plus), which combines
    multiple driver discovery methods to identify cancer driver genes from somatic mutation
    data.
  format: mixed
  id: intogen.pipeline
  is_public: true
  license:
    id: https://www.gnu.org/licenses/gpl-3.0.en.html
    label: GPL-3.0
  name: IntOGen Pipeline Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: intogen
  product_url: https://github.com/bbglab/intogen-plus
- category: DocumentationProduct
  description: Documentation for the IntOGen pipeline, covering its methods, inputs,
    outputs, and post-processing of driver gene results.
  format: http
  id: intogen.docs
  is_public: true
  name: IntOGen Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: intogen
  product_url: https://intogen.readthedocs.io/en/latest/
publications:
- authors:
  - Francisco Martínez-Jiménez
  - Ferran Muiños
  - Inés Sentís
  - Jordi Deu-Pons
  doi: 10.1038/s41568-020-0290-x
  id: doi:10.1038/s41568-020-0290-x
  journal: Nature Reviews Cancer
  preferred: true
  title: A compendium of mutational cancer driver genes
  year: '2020'
repository: https://github.com/bbglab/intogen-plus
rrid: SCR_027727
taxon:
- NCBITaxon:9606
---
# IntOGen

IntOGen (Integrative OncoGenomics) is developed by the Barcelona Biomedical Genomics Lab at IRB Barcelona. It runs a pipeline of complementary driver discovery methods (dNdScv, CBaSE, OncodriveFML, OncodriveCLUSTL, HotMAPS, smRegions, and MutPanning) over somatic mutation data from tumor sequencing cohorts and combines their results to produce the Compendium of Cancer Genes, a catalog of mutational cancer driver genes per cohort and tumor type, each annotated with its mutational features and consensus mode of action (loss of function, activating, or ambiguous).

The 2024.09.20 release covers 271 cohorts and reports 633 driver genes. It switched to MANE reference transcripts, updated the Hartwig Medical Foundation data with Oncotree-based tumor type annotation, and updated annotation to Cancer Gene Census v99. Data released by IntOGen are dedicated to the public domain under CC0 1.0; the pipeline source code is released under GPL-3.0.
