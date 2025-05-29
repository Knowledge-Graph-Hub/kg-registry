---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: help@civicdb.org
  label: CIViC Support
- category: Organization
  label: The McDonnell Genome Institute at Washington University School of Medicine
description: The Clinical Interpretation of Variants in Cancer (CIViC) knowledgebase is a free and open resource for public use that enables the interpretation of variants in cancer by providing community-curated information about the clinical significance of genomic variants.
domains:
- biomedical
- health
- genomics
- clinical
- precision medicine
- cancer
homepage_url: https://civicdb.org/
id: civic
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: CIViC
products:
- category: GraphicalInterface
  description: Web interface that allows searching, browsing, and curating content in the CIViC database.
  id: civic.site
  name: CIViC Web Interface
  product_url: https://civicdb.org/
- category: ProgrammingInterface
  description: GraphQL API for programmatic access to the CIViC database.
  id: civic.api.v2
  is_public: true
  name: CIViC GraphQL API (V2)
  product_url: https://civicdb.org/api/graphiql
- category: ProgrammingInterface
  description: REST API for programmatic access to the CIViC database (deprecated but still accessible).
  id: civic.api.v1
  is_public: true
  name: CIViC REST API (V1 - Deprecated)
  product_url: https://v1.civicdb.org/api
- category: Product
  description: CIViC Feature summaries, nightly version
  id: civic.data.features
  name: CIViC Features (Nightly)
  product_url: https://civicdb.org/downloads/nightly/nightly-FeatureSummaries.tsv
  format: tsv
- category: Product
  description: CIViC Variant summaries, nightly version
  id: civic.data.variants
  name: CIViC Variants (Nightly)
  product_url: https://civicdb.org/downloads/nightly/nightly-VariantSummaries.tsv
  format: tsv
- category: Product
  description: CIViC Molecular Profile summaries, nightly version
  id: civic.data.molecularprofile
  name: CIViC Molecular Profiles (Nightly)
  product_url: https://civicdb.org/downloads/nightly/nightly-MolecularProfileSummaries.tsv
  format: tsv
- category: Product
  description: CIViC Clinical Evidence summaries, nightly version
  id: civic.data.evidence
  name: CIViC Clinical Evidence (Nightly)
  product_url: https://civicdb.org/downloads/nightly/nightly-ClinicalEvidenceSummaries.tsv
  format: tsv
- category: Product
  description: CIViC Variant Group summaries, nightly version
  id: civic.data.variantgroups
  name: CIViC Variant Groups (Nightly)
  product_url: https://civicdb.org/downloads/nightly/nightly-VariantGroupSummaries.tsv
  format: tsv
- category: Product
  description: CIViC Assertion summaries, nightly version
  id: civic.data.assertions
  name: CIViC Assertions (Nightly)
  product_url: https://civicdb.org/downloads/nightly/nightly-AssertionSummaries.tsv
  format: tsv
- category: Product
  description: CIViC Accepted Variants, nightly version
  id: civic.data.acceptedvariants
  name: CIViC Accepted Variants (Nightly)
  product_url: https://civicdb.org/downloads/nightly/nightly-civic_accepted.vcf
  format: vcf
- category: Product
  description: CIViC Accepted and Submitted Variants, nightly version
  id: civic.data.acceptedsubmittedvariants
  name: CIViC Accepted and Submitted Variants (Nightly)
  product_url: https://civicdb.org/downloads/nightly/nightly-civic_accepted_and_submitted.vcf
  format: vcf
publications:
- authors:
  - Griffith M
  - Spies NC
  - Krysiak K
  - McMichael JF
  - Coffman AC
  - Danos AM
  - Ainscough BJ
  - Ramirez CA
  - Rieke DT
  - Kujan L
  - Barnell EK
  - Wagner AH
  - Skidmore ZL
  - Wollam A
  - Liu CJ
  - Jones MR
  - Bilski RL
  - Lesurf R
  - Feng YY
  - Shah NM
  - Bonakdar M
  - Trani L
  - Matlock M
  - Ramu A
  - Campbell KM
  - Spies GC
  - Graubert AP
  - Gangavarapu K
  - Eldred JM
  - Larson DE
  - Walker JR
  - Good BM
  - Wu C
  - Su AI
  - Dienstmann R
  - Margolin AA
  - Tamborero D
  - Lopez-Bigas N
  - Jones SJ
  - Bose R
  - Spencer DH
  - Wartman LD
  - Wilson RK
  - Mardis ER
  - Griffith OL
  doi: doi:10.1038/ng.3774
  id: https://doi.org/10.1038/ng.3774
  journal: Nature Genetics
  preferred: true
  title: CIViC is a community knowledgebase for expert crowdsourcing the clinical interpretation of variants in cancer
  year: "2017"
- authors:
  - Danos AM
  - Krysiak K
  - Barnell EK
  - Coffman AC
  - McMichael JF
  - Kiwala S
  - Spies NC
  - Sheta LM
  - Pema SP
  - Kujan L
  - Clark KA
  - Wollam AZ
  - Rao S
  - Ritter DI
  - Sonkin D
  - Raca G
  - Lin WH
  - Grisdale CJ
  - Kim RH
  - Wagner AH
  - Madhavan S
  - Griffith M
  - Griffith OL
  doi: doi:10.1093/nar/gkac979
  id: https://doi.org/10.1093/nar/gkac979
  journal: Nucleic Acids Research
  title: Evolution of the open-access CIViC knowledgebase is driven by the needs of the cancer variant interpretation community
  year: "2022"
- authors:
  - Danos AM
  - Ritter DI
  - Wagner AH
  - Krysiak K
  - Sonkin D
  - Micheel C
  - McCoy M
  - Rao S
  - Raca G
  - Boca SM
  - Roy A
  - Barnell EK
  - McMichael JF
  - Kiwala S
  - Coffman AC
  - Kujan L
  - Kulkarni S
  - Griffith M
  - Madhavan S
  - Griffith OL
  doi: doi:10.1186/s13073-019-0687-x
  id: https://doi.org/10.1186/s13073-019-0687-x
  journal: Genome Medicine
  title: Standard operating procedure for curation and clinical interpretation of variants in cancer
  year: "2019"
tags:
- data source
- cancer genomics
- variant interpretation
- clinical decision support
- expert curation
- community-driven
usages:
- id: civic.usage.clinical-decision-support
  name: Clinical Decision Support
  description: CIViC is used by researchers and clinicians to support clinical decision-making by providing evidence-based interpretations of genomic variants in cancer.
- id: civic.usage.variant-annotation
  name: Variant Annotation
  description: CIViC provides detailed annotations of genomic variants, including their clinical significance, predictive and prognostic value, and diagnostic implications.
- id: civic.usage.research
  name: Cancer Research
  description: CIViC supports cancer research by providing a centralized resource for understanding the clinical relevance of genomic alterations.
- id: civic.usage.knowledge-integration
  name: Knowledge Integration
  description: CIViC data is integrated into various clinical genomics pipelines, knowledge graphs, and cancer-focused databases.
version: "2.0"
