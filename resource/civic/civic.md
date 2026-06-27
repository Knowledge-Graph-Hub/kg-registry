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
last_modified_date: '2026-06-27T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: CIViC
products:
- category: GraphicalInterface
  description: Web interface that allows searching, browsing, and curating content
    in the CIViC database.
  format: http
  id: civic.site
  name: CIViC Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: civic
  product_url: https://civicdb.org/
- category: ProgrammingInterface
  description: GraphQL API for programmatic access to the CIViC database.
  format: http
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
  format: http
  id: civic.api.v1
  is_public: true
  name: CIViC REST API (V1 - Deprecated)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: civic
  product_url: https://civicdb.org/api/graphql
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
- category: GraphicalInterface
  description: Web-based interface for searching and browsing comprehensive gene-centric
    information integrating data from over 200 sources
  format: http
  id: genecards.web.interface
  name: GeneCards Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: aminode
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: cdd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: craft
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: fabric
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: gard
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: geneorganizer
  - relation_type: prov:hadPrimarySource
    source: genomernai
  - relation_type: prov:hadPrimarySource
    source: glyconnect
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: humancyc
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: iid
  - relation_type: prov:hadPrimarySource
    source: imgt
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadisease
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: nextprot
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pirsf
  - relation_type: prov:hadPrimarySource
    source: prosite
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  - relation_type: prov:hadPrimarySource
    source: proteopedia
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: scop
  - relation_type: prov:hadPrimarySource
    source: sfld
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: treefam
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ucnebase
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vista
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_url: https://www.genecards.org/
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
