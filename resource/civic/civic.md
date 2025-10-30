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
homepage_url: https://civicdb.org/
id: civic
layout: resource_detail
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
    format: tsv
    id: civic.data.features
    name: CIViC Features (Nightly)
    product_file_size: 171302
    product_url: https://civicdb.org/downloads/nightly/nightly-FeatureSummaries.tsv
  - category: Product
    description: CIViC Variant summaries, nightly version
    format: tsv
    id: civic.data.variants
    name: CIViC Variants (Nightly)
    product_file_size: 533165
    product_url: https://civicdb.org/downloads/nightly/nightly-VariantSummaries.tsv
  - category: Product
    description: CIViC Molecular Profile summaries, nightly version
    format: tsv
    id: civic.data.molecularprofile
    name: CIViC Molecular Profiles (Nightly)
    product_file_size: 621001
    product_url: https://civicdb.org/downloads/nightly/nightly-MolecularProfileSummaries.tsv
  - category: Product
    description: CIViC Clinical Evidence summaries, nightly version
    format: tsv
    id: civic.data.evidence
    name: CIViC Clinical Evidence (Nightly)
    product_file_size: 3711846
    product_url: https://civicdb.org/downloads/nightly/nightly-ClinicalEvidenceSummaries.tsv
  - category: Product
    description: CIViC Variant Group summaries, nightly version
    format: tsv
    id: civic.data.variantgroups
    name: CIViC Variant Groups (Nightly)
    product_file_size: 10453
    product_url: https://civicdb.org/downloads/nightly/nightly-VariantGroupSummaries.tsv
  - category: Product
    description: CIViC Assertion summaries, nightly version
    format: tsv
    id: civic.data.assertions
    name: CIViC Assertions (Nightly)
    product_file_size: 114011
    product_url: https://civicdb.org/downloads/nightly/nightly-AssertionSummaries.tsv
  - category: Product
    description: CIViC Accepted Variants, nightly version
    format: vcf
    id: civic.data.acceptedvariants
    name: CIViC Accepted Variants (Nightly)
    product_file_size: 1229101
    product_url: https://civicdb.org/downloads/nightly/nightly-civic_accepted.vcf
  - category: Product
    description: CIViC Accepted and Submitted Variants, nightly version
    format: vcf
    id: civic.data.acceptedsubmittedvariants
    name: CIViC Accepted and Submitted Variants (Nightly)
    product_file_size: 3014555
    product_url: https://civicdb.org/downloads/nightly/nightly-civic_accepted_and_submitted.vcf
  - category: GraphProduct
    description: The SPOKE knowledge graph containing nodes and edges from multiple biomedical data sources.
    id: spoke.graph
    name: SPOKE Graph
    original_source:
      - ncbigene
      - medline
      - mesh
      - pid
      - doid
      - diseases
      - drugcentral
      - go
      - gwascatalog
      - reactome
      - lincs-l1000
      - uberon
      - wikipathways
      - bindingdb
      - drugbank
      - sider
      - bgee
      - uniprot
      - string
      - omim
      - chembl
      - foodb
      - civic
      - gdsc
      - clinicaltrialsgov
      - hpa
      - cl
      - kegg
      - metacyc
      - bv-brc
      - ncbitaxon
      - pathophenodb
      - pfam
      - interpro
      - protcid
    secondary_source:
      - spoke
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
    title: CIViC is a community knowledgebase for expert crowdsourcing the clinical interpretation of variants in cancer
    year: '2017'
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
    year: '2019'
infores_id: civic
---
