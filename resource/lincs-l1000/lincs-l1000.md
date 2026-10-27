---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: lincs-help@broadinstitute.org
  id: broad
  label: Broad Institute LINCS Transcriptomics Center
creation_date: '2025-01-08T00:00:00Z'
description: The LINCS L1000 is a high-throughput, reduced representation gene expression
  profiling assay developed as part of the NIH Library of Integrated Network-Based
  Cellular Signatures (LINCS) Program. L1000 directly measures 978 landmark genes
  and computationally infers the expression of 11,350 additional genes, enabling cost-effective
  large-scale transcriptional profiling at approximately $2 per sample. The technology
  was developed to create a Connectivity Map (CMap) that catalogs cellular responses
  to genetic and chemical perturbations, facilitating drug discovery, mechanism of
  action determination, and functional annotation of genetic variants. The LINCS L1000
  dataset comprises over 1.3 million gene expression profiles representing responses
  to 19,811 chemical compounds, genetic perturbations targeting 5,075 genes (via shRNA
  knockdowns and cDNA overexpression), and 314 biologics across multiple cell lines
  and time points.
domains:
- drug discovery
- high-throughput screening
- genomics
- gene expression profiling
homepage_url: https://lincsproject.org/LINCS/
id: lincs-l1000
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
name: LINCS L1000
products:
- category: GraphicalInterface
  description: The Connectivity Map (CMap) database containing over 1.3 million L1000
    gene expression profiles from chemical, genetic, and biologic perturbations. Includes
    web-based analysis tools for signature search and perturbagen class discovery.
  format: http
  id: lincs-l1000.cmap
  name: LINCS Connectivity Map (CMap)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_url: https://clue.io
- category: GraphicalInterface
  description: The CLUE platform provides interactive analysis tools and data access
    for the LINCS L1000 Connectivity Map dataset, including query tools, visualization,
    and APIs for programmatic access.
  format: http
  id: lincs-l1000.clue
  name: CLUE Platform
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_url: https://clue.io
- category: Product
  description: LINCS L1000 data deposited in the Gene Expression Omnibus, including
    raw and processed gene expression data at multiple levels of preprocessing for
    all 1.3+ million profiles.
  format: http
  id: lincs-l1000.geo
  name: LINCS L1000 GEO Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_url: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE92742
  warnings:
  - File was not able to be retrieved when checked on 2025-11-10_ Timeout connecting
    to URL
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  format: http
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: atc
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: cdc-places
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: dailymed
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: epa-ucmr
  - relation_type: prov:hadPrimarySource
    source: fideo
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: geonames
  - relation_type: prov:hadPrimarySource
    source: ghr
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: intact
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
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pathophenodb
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
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
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tflink
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: who
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://spoke.ucsf.edu/data-tools
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alzkb
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  format: mixed
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alzkb
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hetionet
- category: Product
  description: Harmonizome 3.0 processed dataset downloads, including dataset-specific
    association files and knowledge graph serialization downloads.
  format: mixed
  id: harmonizome.downloads
  name: Harmonizome Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://maayanlab.cloud/Harmonizome/download
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: gene-expression-omnibus
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  description: Neo4j knowledge graph serialization of Harmonizome processed datasets,
    including genes, attributes, resources, datasets, and gene-attribute associations.
  dump_format: neo4j
  format: neo4j
  id: harmonizome.kg-neo4j
  latest_version: '3.0'
  name: Harmonizome Knowledge Graph Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://harmonizome-kg.maayanlab.cloud/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: gene-expression-omnibus
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  description: The SPOKE-OKN knowledge graph, an OKN-hosted RDF publication of the
    SPOKE biomedical and environmental health knowledge graph, served through FRINK
    query services.
  format: ttl
  id: spoke-okn.graph
  name: SPOKE-OKN Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: spoke-okn
  - relation_type: prov:wasDerivedFrom
    source: spoke
  product_url: https://spoke.ucsf.edu
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bgee
  - relation_type: prov:wasInfluencedBy
    source: bindingdb
  - relation_type: prov:wasInfluencedBy
    source: bv-brc
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: civic
  - relation_type: prov:wasInfluencedBy
    source: cl
  - relation_type: prov:wasInfluencedBy
    source: clinicaltrialsgov
  - relation_type: prov:wasInfluencedBy
    source: diseases
  - relation_type: prov:wasInfluencedBy
    source: doid
  - relation_type: prov:wasInfluencedBy
    source: drugbank
  - relation_type: prov:wasInfluencedBy
    source: drugcentral
  - relation_type: prov:wasInfluencedBy
    source: foodb
  - relation_type: prov:wasInfluencedBy
    source: gdsc
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: gwascatalog
  - relation_type: prov:wasInfluencedBy
    source: hpa
  - relation_type: prov:wasInfluencedBy
    source: interpro
  - relation_type: prov:wasInfluencedBy
    source: kegg
  - relation_type: prov:wasInfluencedBy
    source: lincs-l1000
  - relation_type: prov:wasInfluencedBy
    source: mesh
  - relation_type: prov:wasInfluencedBy
    source: metacyc
  - relation_type: prov:wasInfluencedBy
    source: ncbigene
  - relation_type: prov:wasInfluencedBy
    source: ncbitaxon
  - relation_type: prov:wasInfluencedBy
    source: omim
  - relation_type: prov:wasInfluencedBy
    source: pathophenodb
  - relation_type: prov:wasInfluencedBy
    source: pfam
  - relation_type: prov:wasInfluencedBy
    source: pid
  - relation_type: prov:wasInfluencedBy
    source: protcid
  - relation_type: prov:wasInfluencedBy
    source: pubmed
  - relation_type: prov:wasInfluencedBy
    source: reactome
  - relation_type: prov:wasInfluencedBy
    source: sider
  - relation_type: prov:wasInfluencedBy
    source: string
  - relation_type: prov:wasInfluencedBy
    source: uberon
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: wikipathways
- category: GraphProduct
  description: Drug-to-gene up- and down-regulation edges from SigCom LINCS L1000
    signatures (8,942 nodes, 225,509 edges).
  format: json
  id: reprotox-kg.graph.sigcom-lincs
  name: ReproTox-KG SigCom LINCS Drug-Gene Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  product_file_size: 114587395
  product_url: https://s3.amazonaws.com/maayan-kg/reprotox/sigcom_lincs_serialization.valid.json
- category: GraphProduct
  description: Drug-drug cosine similarity edges computed from LINCS L1000 signatures
    (4,523 nodes, 20,785 edges).
  format: json
  id: reprotox-kg.graph.drug-similarity
  name: ReproTox-KG LINCS Drug Similarity Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: reprotox-kg
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 15033998
  product_url: https://s3.amazonaws.com/maayan-kg/reprotox/sigcom_lincs_drug_similarity.valid.json
- category: Product
  description: Statistics for the 29 drug set libraries (109,284 terms) served by
    DrugEnrichr, built from ATC, the Drug Repurposing Hub, KINOMEscan, PharmGKB and
    OFFSIDES, DrugCentral, CREEDS, Geneshot, L1000FWD, SIDER, and STITCH. Each library
    can be downloaded as a GMT-style text file from the geneSetLibrary endpoint (mode=text&libraryName=<library>).
  format: json
  id: drugenrichr.libraries
  name: DrugEnrichr Drug Set Libraries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugenrichr
  - relation_type: prov:hadPrimarySource
    source: atc
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: creeds
  - relation_type: prov:hadPrimarySource
    source: geneshot
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: stitch
  product_file_size: 4251
  product_url: https://maayanlab.cloud/DrugEnrichr/datasetStatistics
- category: Product
  description: Drug-drug similarity matrix from cosine similarity of L1000 drug-induced
    gene expression signatures (SEP-L1000), used to predict related compounds.
  format: hdf5
  id: drugshot.l1000-similarity
  name: L1000 Drug-Drug Similarity Matrix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugshot
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 1550026868
  product_url: https://appyters.maayanlab.cloud/storage/DrugShot/L1000_coexpression.h5
- category: Product
  compression: gzip
  description: Consensus (mean) characteristic-direction coefficient matrix of L1000
    chemical perturbation signatures, 2021 processing.
  format: tsv
  id: sigcom-lincs.cp-consensus
  name: L1000 Chemical Perturbation Consensus Signatures
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 1897525732
  product_url: https://lincs-dcic.s3.amazonaws.com/LINCS-sigs-2021/means/cp_mean_coeff_mat.tsv.gz
- category: Product
  compression: gzip
  description: Consensus (mean) characteristic-direction coefficient matrix of L1000
    CRISPR knockout signatures, 2021 processing.
  format: tsv
  id: sigcom-lincs.xpr-consensus
  name: L1000 CRISPR Knockout Consensus Signatures
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 432492125
  product_url: https://lincs-dcic.s3.amazonaws.com/LINCS-sigs-2021/means/xpr_mean_coeff_mat.tsv.gz
- category: Product
  description: Up and down gene sets for each L1000 chemical perturbation signature
    in GMT format, 2021 processing.
  format: tsv
  id: sigcom-lincs.cp-gmt
  name: L1000 Chemical Perturbation Gene Sets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 2245934983
  product_url: https://lincs-dcic.s3.amazonaws.com/LINCS-sigs-2021/gmt/l1000_cp.gmt
- category: Product
  description: Up and down gene sets for each L1000 CRISPR knockout signature in GMT
    format.
  format: tsv
  id: sigcom-lincs.xpr-gmt
  name: L1000 CRISPR Knockout Gene Sets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 438363414
  product_url: https://lincs-dcic.s3.amazonaws.com/LINCS-sigs-2021/gmt/l1000_xpr.gmt
- category: Product
  description: Up and down gene sets for each L1000 shRNA knockdown signature in GMT
    format.
  format: tsv
  id: sigcom-lincs.shrna-gmt
  name: L1000 shRNA Gene Sets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 501676713
  product_url: https://lincs-dcic.s3.amazonaws.com/LINCS-sigs-2021/gmt/l1000_shRNA.gmt
- category: Product
  description: Up and down gene sets for each L1000 overexpression signature in GMT
    format.
  format: tsv
  id: sigcom-lincs.oe-gmt
  name: L1000 Overexpression Gene Sets
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 105994280
  product_url: https://lincs-dcic.s3.amazonaws.com/LINCS-sigs-2021/gmt/l1000_oe.gmt
- category: Product
  description: Characteristic-direction coefficient matrix for all individual L1000
    chemical perturbation signatures in GCTX (HDF5) format.
  format: hdf5
  id: sigcom-lincs.cp-coefficients
  name: L1000 Chemical Perturbation Signature Matrix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 36084518760
  product_url: https://lincs-dcic.s3.amazonaws.com/LINCS-sigs-2021/gctx/cd-coefficient/cp_coeff_mat.gctx
- category: Product
  description: Drug-drug cosine similarity matrix computed from L1000 landmark gene
    signatures.
  format: hdf5
  id: sigcom-lincs.drug-similarity
  name: L1000 Drug-Drug Similarity Matrix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 4521206656
  product_url: https://lincs-dcic.s3.amazonaws.com/LINCS-data-2020/similarity/L1000_2021_cosine_drug_similarity_lm.h5
- category: Product
  description: Gene-gene cosine similarity matrix computed from L1000 genetic perturbation
    signatures on landmark genes.
  format: hdf5
  id: sigcom-lincs.gene-similarity
  name: L1000 Gene-Gene Similarity Matrix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  product_file_size: 225768016
  product_url: https://lincs-dcic.s3.amazonaws.com/LINCS-data-2020/similarity/L1000_2021_cosine_gene_similarity_lm.h5
- category: Product
  description: The 35 Drugmonizome drug set libraries, listed with metadata and per-library
    download links. Each library is downloadable as a GMT-like DMT file keyed by InChIKey
    or by drug name. Sources are DrugBank (targets, enzymes, carriers, transporters,
    ATC codes), DrugCentral targets, the Drug Repurposing Hub (targets and mechanisms
    of action), STITCH targets, KINOMEscan kinases, SIDER side effects and indications,
    PharmGKB variants and OFFSIDES side effects, PubChem and RDKit MACCS chemical
    fingerprints, Geneshot literature and predicted genes (including ARCHS4 coexpression
    and Enrichr co-occurrence), CREEDS signatures, and L1000FWD signatures, Enrichr
    GO and KEGG terms, and SEP-L1000 predicted side effects.
  format: json
  id: drugmonizome.libraries
  name: Drugmonizome Drug Set Libraries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: drugmonizome
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: atc
  - relation_type: prov:wasDerivedFrom
    source: drugcentral
  - relation_type: prov:wasDerivedFrom
    source: repohub
  - relation_type: prov:wasDerivedFrom
    source: stitch
  - relation_type: prov:wasDerivedFrom
    source: kinomescan
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: offsides
  - relation_type: prov:wasDerivedFrom
    source: pubchem
  - relation_type: prov:wasDerivedFrom
    source: geneshot
  - relation_type: prov:wasDerivedFrom
    source: archs4
  - relation_type: prov:wasDerivedFrom
    source: enrichr
  - relation_type: prov:wasDerivedFrom
    source: creeds
  - relation_type: prov:wasDerivedFrom
    source: l1000fwd
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: sep-l1000
  product_url: https://maayanlab.cloud/drugmonizome/metadata-api/libraries
  warnings:
  - 'File was not able to be retrieved when checked on 2026-10-21: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-10-27: HTTP 404 error
    when accessing file'
- category: GraphicalInterface
  description: Interactive fireworks and t-SNE maps of drug-induced L1000 signatures
    for all cell lines and individual cell lines, with signature similarity search
    using up and down gene sets, signature landing pages, and subset visualization.
  format: http
  id: l1000fwd.portal
  name: L1000FWD Web Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: l1000fwd
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  product_url: https://maayanlab.cloud/l1000fwd/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: creeds
  warnings:
  - Web application returned HTTP 503 when checked on 2026-10-19, although static
    download files were served; the homepage was archived with HTTP 200 on 2026-09-29.
- category: ProgrammingInterface
  description: REST API for searching drugs by name or synonym, retrieving a signature
    by ID, querying signatures with up and down gene sets, and retrieving the top
    50 results. Documented on the API page with Python and R examples.
  format: json
  id: l1000fwd.api
  is_public: true
  name: L1000FWD API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: l1000fwd
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  product_url: https://maayanlab.cloud/l1000fwd/api_page
  warnings:
  - API page returned HTTP 503 when checked on 2026-10-19.
- category: Product
  description: Characteristic direction (CD) signature matrix for 42,809 significant
    L1000 drug and small-molecule signatures in the 978 landmark gene space, in GCTX
    (HDF5) format.
  format: hdf5
  id: l1000fwd.cd-signatures-landmark
  name: L1000FWD CD Signatures (Landmark Genes)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: l1000fwd
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  product_file_size: 346694992
  product_url: https://maayanlab.cloud/l1000fwd/download/CD_signatures_LM_42809x978.gctx
- category: Product
  description: Characteristic direction (CD) signature matrix for 42,809 significant
    L1000 drug and small-molecule signatures in the full space of 22,268 probes, in
    GCTX (HDF5) format.
  format: hdf5
  id: l1000fwd.cd-signatures-full
  name: L1000FWD CD Signatures (Full Space)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: l1000fwd
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  product_file_size: 7638514350
  product_url: https://maayanlab.cloud/l1000fwd/download/CD_signatures_full_42809x22268.gctx
- category: Product
  description: Cosine similarity adjacency matrix among all 42,809 significant CD
    signatures in the landmark gene space, in GCTX (HDF5) format.
  format: hdf5
  id: l1000fwd.adjacency-matrix
  name: L1000FWD Signature Adjacency Matrix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: l1000fwd
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  product_file_size: 14684362180
  product_url: https://maayanlab.cloud/l1000fwd/download/Adjacency_matrix_LM_space_42809x42809.gctx
- category: Product
  description: Up and down gene sets for the 42,809 CD signatures in the full gene
    space, in GMT format.
  format: tsv
  id: l1000fwd.gene-sets-gmt
  name: L1000FWD Signature Gene Sets (GMT)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: l1000fwd
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  product_file_size: 120617799
  product_url: https://maayanlab.cloud/l1000fwd/download/CD_signatures_binary_42809.gmt
- category: Product
  description: Up and down gene sets for the 42,809 CD signatures in the full gene
    space, in JSON format.
  format: json
  id: l1000fwd.gene-sets-json
  name: L1000FWD Signature Gene Sets (JSON)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: l1000fwd
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  product_file_size: 177765632
  product_url: https://maayanlab.cloud/l1000fwd/download/CD_signatures_binary_42809.json
- category: Product
  description: Metadata for the L1000FWD signatures indexed by sig_id, including batch,
    cell line, perturbagen, dose, time, and signature strength.
  format: csv
  id: l1000fwd.signature-metadata
  name: L1000FWD Signature Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: l1000fwd
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  product_file_size: 5075455
  product_url: https://maayanlab.cloud/l1000fwd/download/CD_signature_metadata.csv
- category: Product
  description: Metadata for the profiled drugs and small molecules indexed by pert_id,
    including LINCS small molecule IDs, names, SMILES, InChIKeys, molecular formulas,
    and PubChem CIDs.
  format: csv
  id: l1000fwd.drug-metadata
  name: L1000FWD Drug Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: l1000fwd
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: lincs
  product_file_size: 7797325
  product_url: https://maayanlab.cloud/l1000fwd/download/Drugs_metadata.csv
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: pubchem
- category: Product
  description: Metadata for the L1000 probes of the 978 landmark genes.
  format: csv
  id: l1000fwd.probes-landmark-metadata
  name: L1000FWD Landmark Probe Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: l1000fwd
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  product_file_size: 16690
  product_url: https://maayanlab.cloud/l1000fwd/download/Probes_L1000_metadata.csv
- category: Product
  description: Metadata for the 22,268 probes used in the full gene space.
  format: csv
  id: l1000fwd.probes-full-metadata
  name: L1000FWD Full Probe Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: l1000fwd
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  product_file_size: 372943
  product_url: https://maayanlab.cloud/l1000fwd/download/Probes_full_metadata.csv
- category: GraphicalInterface
  description: Web portal for browsing and searching predicted and known drug-side
    effect connections by drug or side effect, with side effect-GO term and side effect-phenotype
    networks.
  format: http
  id: sep-l1000.portal
  name: SEP-L1000 Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sep-l1000
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: offsides
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: mlpcn-profiling
  product_url: http://maayanlab.net/SEP-L1000/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: meddra
  - relation_type: prov:wasInformedBy
    source: drugbank
- category: Product
  compression: gzip
  description: Characteristic direction gene expression signatures for 20,339 drugs
    and small molecules in the 978 landmark gene space, computed from LINCS L1000
    profiles.
  format: csv
  id: sep-l1000.lincs-signatures
  name: SEP-L1000 LINCS L1000 CD Signatures
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sep-l1000
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  product_file_size: 40428519
  product_url: http://maayanlab.net/SEP-L1000/downloads/LINCS_Gene_Experssion_signatures_CD.csv.gz
- category: Product
  compression: gzip
  description: Gene Ontology transformed L1000 signatures, giving Principal Angle
    Enrichment Analysis p-values of each drug signature against GO Biological Process,
    Cellular Component, and Molecular Function gene sets (20,338 compounds by 4,438
    terms).
  format: csv
  id: sep-l1000.go-signatures
  name: SEP-L1000 GO-Transformed Signatures
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sep-l1000
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: go
  product_file_size: 230607368
  product_url: http://maayanlab.net/SEP-L1000/downloads/GO_transformed_signatures_PAEA.csv.gz
- category: Product
  compression: gzip
  description: 166-bit MACCS chemical fingerprint matrix for 41,774 drugs and small
    molecules from LINCS L1000 and MLPCN, computed with Open Babel from SMILES.
  format: csv
  id: sep-l1000.maccs-fingerprints
  name: SEP-L1000 MACCS Fingerprints
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sep-l1000
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mlpcn-profiling
  product_file_size: 1254411
  product_url: http://maayanlab.net/SEP-L1000/downloads/MACCS_bitmatrix.csv.gz
- category: Product
  description: Metadata mapping each LINCS L1000 compound (pert_id) to the control
    and perturbation distil_ids and the strongest signature used.
  format: csv
  id: sep-l1000.strongest-signatures-metadata
  name: SEP-L1000 Strongest Signature Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sep-l1000
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  product_file_size: 33352601
  product_url: http://maayanlab.net/SEP-L1000/downloads/meta_LINCS_strongest_signatures.csv
- category: Product
  description: Mapping of L1000 probes to gene symbols.
  format: csv
  id: sep-l1000.probes-metadata
  name: SEP-L1000 Probe Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sep-l1000
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  product_file_size: 370344
  product_url: http://maayanlab.net/SEP-L1000/downloads/meta_Probes_info.csv
- category: Product
  description: Compound metadata for 41,774 LINCS L1000 and MLPCN small molecules
    with pert_id, name, PubChem CID, and SMILES.
  format: csv
  id: sep-l1000.smiles-metadata
  name: SEP-L1000 Compound SMILES Metadata
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sep-l1000
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mlpcn-profiling
  product_file_size: 4014816
  product_url: http://maayanlab.net/SEP-L1000/downloads/meta_SMILES.csv
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: pubchem
- category: Product
  description: Downloadable Enrichr gene set libraries (more than 200 libraries across
    transcription, pathways, ontologies, diseases/drugs, cell types, crowd-contributed,
    and legacy categories), each retrievable as a GMT-style tab-delimited text file
    via the geneSetLibrary endpoint (e.g. geneSetLibrary?mode=text&libraryName=KEGG_2021_Human).
    Libraries are compiled from external databases including GO, KEGG, Reactome, WikiPathways,
    MSigDB, ChEA/ENCODE, GTEx, ARCHS4, LINCS L1000, GEO, DisGeNET, OMIM, GWAS Catalog,
    HPO, MGI, CellMarker, and others.
  format: txt
  id: enrichr.libraries
  name: Enrichr Gene Set Libraries
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: bioplanet
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  - relation_type: prov:hadPrimarySource
    source: chea
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: dbgap
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: humancyc
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: pfocr
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: ncipidkg
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: sigcom-lincs
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  - relation_type: prov:hadPrimarySource
    source: open-tggates
  - relation_type: prov:hadPrimarySource
    source: trrust
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: geneshot
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_url: https://maayanlab.cloud/Enrichr/#libraries
- category: GraphicalInterface
  description: Web interface for searching, browsing, and analyzing protein target
    information with advanced filtering, visualizations, and data export capabilities
    across the druggable genome
  format: http
  id: pharos.portal
  name: Pharos Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: eram
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: tiga
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: human-proteome-map
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cspa
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hcop
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: darkkinasekb
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  product_url: https://pharos.nih.gov/
- category: Product
  description: Target Central Resource Database (TCRD) downloadable database files
    containing comprehensive protein target information including druggability classifications,
    expression data, disease associations, and chemical probe information
  format: http
  id: pharos.tcrd.download
  name: TCRD Database Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: eram
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: tiga
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: human-proteome-map
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cspa
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hcop
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: darkkinasekb
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  product_url: https://opendata.ncats.nih.gov/public/pharos/
  warnings:
  - The Pharos footer still links the historical Juniper TCRD download host, but the
    about page points Pharos data downloads to NCATS OpenData; the registry uses the
    NCATS OpenData URL.
- category: ProgrammingInterface
  connection_url: https://pharos-api.ncats.io/graphql
  description: GraphQL API for programmatic access to Pharos and TCRD data enabling
    custom queries and integrations. The pharos.nih.gov/graphql page is the in-browser
    explorer; queries are served by the pharos-api.ncats.io/graphql endpoint used
    by the Pharos frontend.
  format: graphql
  id: pharos.api
  name: Pharos GraphQL API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: eram
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: tiga
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: human-proteome-map
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cspa
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: bioplex
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hcop
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: darkkinasekb
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  product_url: https://pharos.nih.gov/graphql
publications:
- authors:
  - Subramanian, A.
  - Narayan, R.
  - Corsello, S.M.
  - Peck, D.D.
  - Natoli, T.E.
  - Lu, X.
  - Gould, J.
  - Davis, J.F.
  - Tubelli, A.A.
  - Asiedu, J.K.
  - Lahr, D.L.
  - Hirschman, J.E.
  - Liu, Z.
  - Donahue, M.
  - Julian, B.
  - Khan, M.
  - Wadden, D.
  - Smith, I.C.
  - Lam, D.
  - Liberzon, A.
  - Toder, C.
  - Bagul, M.
  - Orzechowski, M.
  - Enache, O.M.
  - Piccioni, F.
  - Johnson, S.A.
  - Lyons, N.J.
  - Berger, A.H.
  - Shamji, A.F.
  - Brooks, A.N.
  - Vrcic, A.
  - Flynn, C.
  - Rosains, J.
  - Takeda, D.Y.
  - Hu, R.
  - Davison, D.
  - Lamb, J.
  - Ardlie, K.
  - Hogstrom, L.
  - Greenside, P.
  - Gray, N.S.
  - Clemons, P.A.
  - Silver, S.
  - Wu, X.
  - Zhao, W.N.
  - Read-Button, W.
  - Wu, X.
  - Haggarty, S.J.
  - Ronco, L.V.
  - Boehm, J.S.
  - Schreiber, S.L.
  - Doench, J.G.
  - Bittker, J.A.
  - Root, D.E.
  - Wong, B.
  - Golub, T.R.
  doi: 10.1016/j.cell.2017.10.049
  id: doi:10.1016/j.cell.2017.10.049
  journal: Cell
  preferred: true
  title: 'A Next Generation Connectivity Map: L1000 platform and the first 1,000,000
    profiles'
  year: '2017'
repository: https://github.com/cmap/l1000-jupyter
taxon:
- NCBITaxon:9606
---
## Overview

The LINCS L1000 platform represents a major advance in high-throughput transcriptional profiling technology. By measuring only 978 carefully selected "landmark" genes and using computational inference for the remaining transcriptome, L1000 achieves dramatic cost reduction (approximately $2 per sample) while maintaining high reproducibility and comparability to RNA-seq. This breakthrough enabled the generation of over 1.3 million gene expression profiles as part of the NIH LINCS Program, creating one of the largest publicly available transcriptional profiling resources.

## Key Features

### Technology
- **Landmark genes**: 978 directly measured genes selected through data-driven analysis of 12,000+ microarray profiles
- **Inferred genes**: 11,350 genes computationally inferred with 81% showing high accuracy
- **Platform**: Ligation-mediated amplification (LMA) with Luminex bead-based detection
- **Cost**: Approximately $2 per profile (vs. traditional microarrays or RNA-seq)
- **Reproducibility**: >88% of technical replicates show Spearman correlation >0.9
- **Validation**: Highly comparable to RNA-seq (median cross-platform correlation 0.84)

### Dataset Composition (CMap-L1000v1)
- **1,319,138 L1000 profiles** comprising:
  - **19,811 small molecule compounds** (drugs, tool compounds, screening libraries)
  - **18,493 shRNAs** targeting 5,075 genes for loss-of-function studies
  - **3,462 cDNAs** for gain-of-function studies
  - **314 biologics**
  - **473,647 signatures** (consolidating biological replicates)

- **Cell line coverage**:
  - 9 core cancer cell lines (Touchstone reference dataset)
  - Up to 77 cell lines for Discovery dataset
  - Includes neuronal cell types (NPCs and differentiated neurons)

- **Time points**: 6h and 24h for chemical perturbations, 96h for genetic perturbations

### Applications
- **Drug discovery**: Mechanism of action (MOA) determination, off-target effect identification
- **Compound annotation**: Functional classification of uncharacterized molecules via connectivity to Perturbagen Classes (PCLs)
- **Genetic variant interpretation**: Assess functional impact of disease-associated alleles (e.g., FBXW7, KEAP1, PTEN)
- **Clinical trial analysis**: Evaluate target engagement and identify resistance mechanisms
- **Connectivity mapping**: Discover relationships between genes, drugs, and disease states through gene expression signatures
- **Bioactivity screening**: Identify transcriptionally active compounds from screening libraries

## Data Access and Tools

### Primary Data Portals
- **CLUE Platform** (https://clue.io): Interactive analysis tools, signature search, data downloads, and APIs
- **GEO** (GSE92742): Raw and processed data at multiple preprocessing levels
- **GitHub** (https://github.com/cmap/cmapM): Pre-processing code and tools

### Additional LINCS Resources
- **SigCom LINCS** (https://maayanlab.cloud/sigcom-lincs): Search across 1.5M+ signatures
- **L1000FWD** (https://maayanlab.cloud/L1000FWD/): L1000 Characteristic Direction Signature Search Engine
- **iLINCS** (http://www.ilincs.org): Integrated LINCS data portal
- **LINCS Data Portal** (http://lincsportal.ccs.miami.edu/dcic-portal/): DCIC data coordination center

### Data Levels
1. **Level 1**: Raw bead count and fluorescence intensity
2. **Level 2**: Deconvoluted data (assigning expression to two genes per bead color)
3. **Level 3**: Normalized data (LISS + quantile normalization) with inferred gene expression
4. **Level 4**: Differential expression (z-scores)
5. **Level 5**: Replicate-consensus signatures

## Methodology Highlights

### Perturbagen Classes (PCLs)
171 high-confidence Perturbagen Classes have been defined, representing groups of perturbagens with shared mechanisms. These include:
- 92 compound classes (e.g., HDAC inhibitors, kinase inhibitors)
- 60 loss-of-function gene classes
- 17 gain-of-function gene classes

PCLs enhance interpretability by aggregating similar perturbagens to strengthen on-target signals while diminishing off-target effects.

### Consensus Gene Signatures (CGS)
To mitigate strong off-target effects of shRNAs (where seed sequence effects often exceed on-target effects), a Consensus Gene Signature algorithm was developed that identifies consistent gene expression changes across multiple shRNAs targeting the same gene.

### Query Methodology
The Connectivity Map uses a weighted connectivity score (WTCS) approach similar to Gene Set Enrichment Analysis, computing similarity between query gene signatures and database signatures. Results are normalized and summarized across cell lines using quantile-based metrics (τ scores) to identify robust connections.

## Key Publications and Citations

**Primary Reference**:
- Subramanian A, Narayan R, Corsello SM, et al. A Next Generation Connectivity Map: L1000 platform and the first 1,000,000 profiles. *Cell*. 2017;171(6):1437-1452.e17. doi:10.1016/j.cell.2017.10.049

**Additional Resources**:
- Original Connectivity Map concept: Lamb J, et al. The Connectivity Map: using gene-expression signatures to connect small molecules, genes, and disease. *Science*. 2006;313(5795):1929-1935.
- Detailed protocols: https://clue.io/sop-L1000.pdf
- Connectopedia knowledge base: https://clue.io/connectopedia

## Funding

Supported by NIH grants including 5U54HG006093, U54HG008699, and 5U01HG008699 as part of the NIH Common Fund LINCS Program.