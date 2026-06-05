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
creation_date: '2025-05-29T00:00:00Z'
description: The Clinical Interpretation of Variants in Cancer (CIViC) knowledgebase
  is a free and open resource for public use that enables the interpretation of variants
  in cancer by providing community-curated information about the clinical significance
  of genomic variants.
domains:
- biomedical
- genomics
- clinical
- precision medicine
homepage_url: https://civicdb.org/
id: civic
infores_id: civic
last_modified_date: '2025-12-13T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: CIViC
products:
- category: GraphicalInterface
  description: Web interface that allows searching, browsing, and curating content
    in the CIViC database.
  id: civic.site
  name: CIViC Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: civic
  product_url: https://civicdb.org/
- category: ProgrammingInterface
  description: GraphQL API for programmatic access to the CIViC database.
  id: civic.api.v2
  is_public: true
  name: CIViC GraphQL API (V2)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: civic
  product_url: https://civicdb.org/api/graphiql
- category: ProgrammingInterface
  description: REST API for programmatic access to the CIViC database (deprecated
    but still accessible).
  id: civic.api.v1
  is_public: true
  name: CIViC REST API (V1 - Deprecated)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: civic
  product_url: https://v1.civicdb.org/api
- category: Product
  description: CIViC Feature summaries, nightly version
  format: tsv
  id: civic.data.features
  name: CIViC Features (Nightly)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: civic
  product_file_size: 171302
  product_url: https://civicdb.org/downloads/nightly/nightly-FeatureSummaries.tsv
- category: Product
  description: CIViC Variant summaries, nightly version
  format: tsv
  id: civic.data.variants
  name: CIViC Variants (Nightly)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: civic
  product_file_size: 533165
  product_url: https://civicdb.org/downloads/nightly/nightly-VariantSummaries.tsv
- category: Product
  description: CIViC Molecular Profile summaries, nightly version
  format: tsv
  id: civic.data.molecularprofile
  name: CIViC Molecular Profiles (Nightly)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: civic
  product_file_size: 621001
  product_url: https://civicdb.org/downloads/nightly/nightly-MolecularProfileSummaries.tsv
- category: Product
  description: CIViC Clinical Evidence summaries, nightly version
  format: tsv
  id: civic.data.evidence
  name: CIViC Clinical Evidence (Nightly)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: civic
  product_file_size: 3711846
  product_url: https://civicdb.org/downloads/nightly/nightly-ClinicalEvidenceSummaries.tsv
- category: Product
  description: CIViC Variant Group summaries, nightly version
  format: tsv
  id: civic.data.variantgroups
  name: CIViC Variant Groups (Nightly)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: civic
  product_file_size: 10453
  product_url: https://civicdb.org/downloads/nightly/nightly-VariantGroupSummaries.tsv
- category: Product
  description: CIViC Assertion summaries, nightly version
  format: tsv
  id: civic.data.assertions
  name: CIViC Assertions (Nightly)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: civic
  product_file_size: 114011
  product_url: https://civicdb.org/downloads/nightly/nightly-AssertionSummaries.tsv
- category: Product
  description: CIViC Accepted Variants, nightly version
  format: vcf
  id: civic.data.acceptedvariants
  name: CIViC Accepted Variants (Nightly)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: civic
  product_file_size: 1229101
  product_url: https://civicdb.org/downloads/nightly/nightly-civic_accepted.vcf
- category: Product
  description: CIViC Accepted and Submitted Variants, nightly version
  format: vcf
  id: civic.data.acceptedsubmittedvariants
  name: CIViC Accepted and Submitted Variants (Nightly)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: civic
  product_file_size: 3014555
  product_url: https://civicdb.org/downloads/nightly/nightly-civic_accepted_and_submitted.vcf
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
- category: Product
  description: civic.gid Nodes TSV
  format: tsv
  id: obo-db-ingest.civic.gid.tsv
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0-1.0
  name: civic.gid Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 34804
  product_url: https://w3id.org/biopragmatics/resources/civic.gid/civic.gid.tsv
- category: Product
  description: Unified BioMuta cancer mutation dataset produced by combining mutation
    records from TCGA, ICGC, CIViC, and COSMIC into a common field structure.
  format: csv
  id: biomuta.dataset
  name: BioMuta Cancer Mutation Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biomuta
  product_url: https://biomuta.readthedocs.io/en/latest/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: civic
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: icgc
  - relation_type: prov:wasDerivedFrom
    source: tcga
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
  title: CIViC is a community knowledgebase for expert crowdsourcing the clinical
    interpretation of variants in cancer
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
  title: Standard operating procedure for curation and clinical interpretation of
    variants in cancer
  year: '2019'
taxon:
- NCBITaxon:9606
---
