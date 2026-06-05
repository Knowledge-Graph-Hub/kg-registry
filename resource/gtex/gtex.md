---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: gtex-help@broadinstitute.org
  - contact_type: url
    value: https://www.gtexportal.org/home/contact
  label: GTEx Consortium
creation_date: '2025-06-04T00:00:00Z'
description: The Genotype-Tissue Expression (GTEx) project provides a comprehensive
  resource to study tissue-specific gene expression and regulation. Samples were collected
  from 54 non-diseased tissue sites across nearly 1000 individuals, primarily for
  molecular assays including WGS, WES, and RNA-Seq.
domains:
- genomics
- biomedical
- anatomy and development
homepage_url: https://www.gtexportal.org/home/
id: gtex
infores_id: gtex
last_modified_date: '2026-04-16T00:00:00Z'
layout: resource_detail
license:
  id: https://www.gtexportal.org/home/license
  label: GTEx Portal Data License
name: GTEx
products:
- category: GraphicalInterface
  description: GTEx Portal web interface for exploring tissue-specific gene expression
    data, eQTLs, and other genomic analyses
  format: http
  id: gtex.portal
  name: GTEx Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtex
  product_url: https://www.gtexportal.org/home/
- category: Product
  description: Complete GTEx v8 data including gene expression, transcript expression,
    exon expression, and junction data across tissues
  format: tsv
  id: gtex.bulk-data
  name: GTEx Bulk Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtex
  product_url: https://www.gtexportal.org/home/downloads/adult-gtex
- category: Product
  description: eQTL (expression quantitative trait loci) data linking genetic variants
    to gene expression across tissues
  format: tsv
  id: gtex.eqtl-data
  name: GTEx eQTL Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtex
  product_url: https://www.gtexportal.org/home/downloads/adult-gtex/qtl
- category: ProgrammingInterface
  description: GTEx REST API for programmatic access to gene expression and eQTL data
  format: json
  id: gtex.api
  name: GTEx REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtex
  product_url: https://gtexportal.org/rest/
- category: Product
  description: Individual-level genotype and phenotype data available through dbGaP
  format: vcf
  id: gtex.dbgap-data
  name: GTEx dbGaP Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtex
  product_url: https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000424
- category: GraphProduct
  description: GTEx Automat
  format: kgx-jsonl
  id: automat.gtex
  infores_id: automat-gtex
  name: gtex_automat
  original_source:
  - relation_type: prov:hadPrimarySource
    source: automat
  - relation_type: prov:hadPrimarySource
    source: gtex
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/GTEx_Automat/a6448b9092bb81a1/
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: bioteque
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chemicalchecker
  - relation_type: prov:hadPrimarySource
    source: clue
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: creeds
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: huri
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: offsides
  - relation_type: prov:hadPrimarySource
    source: omnipath
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  - relation_type: prov:hadPrimarySource
    source: prism
  - relation_type: prov:hadPrimarySource
    source: progeny
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 4dn
  - relation_type: prov:hadPrimarySource
    source: biomarker
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: connectivitymap
  - relation_type: prov:hadPrimarySource
    source: dct
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: edam
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: erccrbp
  - relation_type: prov:hadPrimarySource
    source: erccreg
  - relation_type: prov:hadPrimarySource
    source: faldo
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: glycocoo
  - relation_type: prov:hadPrimarySource
    source: glycordf
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hra
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: kidsfirst
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: loinc
  - relation_type: prov:hadPrimarySource
    source: mi
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: npo
  - relation_type: prov:hadPrimarySource
    source: obi
  - relation_type: prov:hadPrimarySource
    source: obib
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pgo
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sbo
  - relation_type: prov:hadPrimarySource
    source: sckan
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: stellar
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: uo
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://ubkg-downloads.xconsortia.org/
- category: GraphProduct
  description: Integrated graph knowledge base combining Mendelian randomization causal
    estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships
    (Neo4j backend)
  format: neo4j
  id: epigraphdb.graph
  name: EpiGraphDB Graph Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: epigraphdb
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: vectology
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: prsatlas
  - relation_type: prov:hadPrimarySource
    source: eqtlgen
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: cpic
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: mrbase
  product_url: https://docs.epigraphdb.org/graph-database/
- category: Product
  description: Gene expression data aggregated from GTEx, BioGPS, Bgee and other expression
    databases
  format: http
  id: genecards.expression.data
  name: GeneCards Expression Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: gtex
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-06-03: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-05: HTTP 403 error
    when accessing file'
- category: GraphProduct
  description: Neo4j knowledge graph integrating transcription factor target libraries,
    coexpression networks, and benchmark datasets used by the ChEA3 resource
  dump_format: neo4j
  format: neo4j
  id: chea-kg.graph
  name: ChEA-KG Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea-kg
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: tcga
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: chea
- category: Product
  description: Download catalog for ChEA3 transcription factor target libraries, benchmark
    datasets, and additional supporting libraries
  format: http
  id: chea-kg.libraries
  name: ChEA-KG Library Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea-kg
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: tcga
  product_url: https://maayanlab.cloud/chea3/index.html#content4-13
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: chea
- category: Product
  description: Download catalog for ChEA3 transcription factor target libraries and
    benchmark datasets
  format: http
  id: chea.libraries
  name: ChEA Library Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: chea
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: remap
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: geo
  - relation_type: prov:hadPrimarySource
    source: tcga
  product_url: https://maayanlab.cloud/chea3/index.html#content4-13
- category: GraphProduct
  description: GTEx expression anatomy nodes (GTEXEXP) used in ProKN
  format: csv
  id: prokn.gtexexp.anatomy.nodes
  name: ProKN GTEx Anatomy Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 6993
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GTEXEXP.Anatomy.nodes.csv
- category: GraphProduct
  description: GTEx gene expressed in anatomy edges
  format: csv
  id: prokn.gtexexp.gene.expressed_in.anatomy.edges
  name: ProKN GTEx Gene Expression Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 341113044
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GTEXEXP.Gene.EXPRESSED_IN.Anatomy.edges.csv
- category: GraphProduct
  description: GTEx expression to anatomy edges (GTExEXP node type)
  format: csv
  id: prokn.gtexexp.gtexexp.expressed_in.anatomy.edges
  name: ProKN GTExEXP Anatomy Expression Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 406384547
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GTEXEXP.GTExEXP.EXPRESSED_IN.Anatomy.edges.csv
- category: GraphProduct
  description: GTEx expression to gene edges (GTExEXP node type)
  format: csv
  id: prokn.gtexexp.gtexexp.expressed_in.gene.edges
  name: ProKN GTExEXP Gene Expression Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 386708211
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GTEXEXP.GTExEXP.EXPRESSED_IN.Gene.edges.csv
- category: GraphProduct
  description: GTEx expression to expression bins edges
  format: csv
  id: prokn.gtexexp.gtexexp.has_expression.expbins.edges
  name: ProKN GTExEXP Expression Bin Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 413542626
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_GTEXEXP.GTExEXP.HAS_EXPRESSION.EXPBINS.edges.csv
- category: GraphProduct
  description: Neo4j knowledge graph containing integrated gene sets from multiple
    Common Fund programs with cross-references
  dump_format: neo4j
  format: neo4j
  id: cfde-gse.graph
  name: CFDE-GSE Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cfde-gse
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: motrpac
- category: Product
  description: Standardized gene set collections from Common Fund programs in GMT
    format
  id: cfde-gse.genesets
  name: CFDE Gene Set Collections
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cfde-gse
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: motrpac
  product_url: https://gse.cfde.cloud/downloads/
- category: GraphProduct
  description: Neo4j graph database integrating Enrichr gene set libraries with genes,
    terms, pathways, diseases, drugs, cell types, and other functional annotations
  dump_format: neo4j
  format: neo4j
  id: enrichr-kg.graph
  name: Enrichr-KG Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr-kg
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hubmap
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: archs4
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: kg-jensenlab-diseases
- category: GraphProduct
  description: Neo4j knowledge graph containing lncRNAs, protein-coding genes, regulatory
    interactions, and disease associations
  dump_format: neo4j
  format: neo4j
  id: lncrnalyzr.graph
  name: lncRNAlyzr Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lncrnalyzr
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: doid
- category: GraphProduct
  description: A comprehensive multi-omics biomedical knowledge graph connecting genomic,
    transcriptomic, proteomic, and clinical data. Contains over 32 million nodes and
    118 million relationships.
  dump_format: neo4j
  edge_count: 118000000
  id: petagraph.graph
  name: Petagraph Knowledge Graph (Neo4J)
  node_count: 32000000
  original_source:
  - relation_type: prov:hadPrimarySource
    source: petagraph
  - relation_type: prov:hadPrimarySource
    source: ubkg
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: lincs
  product_url: https://ubkg-downloads.xconsortia.org/
- category: Product
  description: MySQL database dump files containing the complete TCRD relational database
    schema and data for local installation and analysis
  format: mysql
  id: tcrd.database_download
  name: TCRD Database Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  product_url: http://juniper.health.unm.edu/tcrd/download/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: drugcentral
  - relation_type: prov:wasInfluencedBy
    source: string
  - relation_type: prov:wasInfluencedBy
    source: gtex
  - relation_type: prov:wasInfluencedBy
    source: omim
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2026-06-03: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-06-02: Error connecting
    to URL: HTTPConnectionPool(host=''juniper.health.unm.edu'', port=80): Max retries
    exceeded with url: /tcrd/download/ (Caused by NameResolutionError("HTTPConnection(host=''juniper.health.unm.edu'',
    port=80): Failed to resolve ''juniper.health.unm.edu'' ([Errno -3] Temporary failure
    in name resolution)"))'
  - 'File was not able to be retrieved when checked on 2026-06-05: Timeout connecting
    to URL'
- category: ProgrammingInterface
  description: RESTful API providing programmatic access to TCRD data through Pharos
    for computational workflows and custom applications
  format: http
  id: tcrd.api
  is_public: true
  name: Pharos API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  product_url: https://pharos.nih.gov/api
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: drugcentral
  - relation_type: prov:wasInfluencedBy
    source: string
  - relation_type: prov:wasInfluencedBy
    source: gtex
  - relation_type: prov:wasInfluencedBy
    source: omim
- category: DocumentationProduct
  description: Comprehensive documentation describing TCRD data sources, schema structure,
    and usage guidelines
  format: http
  id: tcrd.documentation
  name: TCRD Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  product_url: http://juniper.health.unm.edu/tcrd/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: chembl
  - relation_type: prov:wasInfluencedBy
    source: drugcentral
  - relation_type: prov:wasInfluencedBy
    source: string
  - relation_type: prov:wasInfluencedBy
    source: gtex
  - relation_type: prov:wasInfluencedBy
    source: omim
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2026-06-03: Timeout connecting
    to URL'
  - 'File was not able to be retrieved when checked on 2026-06-02: Error connecting
    to URL: HTTPConnectionPool(host=''juniper.health.unm.edu'', port=80): Max retries
    exceeded with url: /tcrd/ (Caused by NameResolutionError("HTTPConnection(host=''juniper.health.unm.edu'',
    port=80): Failed to resolve ''juniper.health.unm.edu'' ([Errno -3] Temporary failure
    in name resolution)"))'
  - 'File was not able to be retrieved when checked on 2026-06-05: Timeout connecting
    to URL'
- category: GraphProduct
  description: GP-KG tab-delimited knowledge graph containing 1,246,726 associations
    between 61,146 entities from multiple genotypic and phenotypic databases
  format: tsv
  id: kg-predict.gpkg
  name: GP-KG Knowledge Graph Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-predict
  product_file_size: 48397035
  product_url: https://nlp.case.edu/public/data/GPKG-Predict/data/GP_KG.txt
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: faers
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: mgi
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: string
  - relation_type: prov:wasDerivedFrom
    source: umls
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
    source: geo
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
    source: geo
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
publications:
- authors:
  - GTEx Consortium
  doi: 10.1126/science.aaz1776
  id: doi:10.1126/science.aaz1776
  title: The GTEx Consortium atlas of genetic regulatory effects across human tissues
  year: '2020'
- authors:
  - GTEx Consortium
  doi: 10.1126/science.1262110
  id: doi:10.1126/science.1262110
  title: 'The Genotype-Tissue Expression (GTEx) pilot analysis: multitissue gene regulation
    in humans'
  year: '2015'
repository: https://github.com/broadinstitute/gtex-pipeline
taxon:
- NCBITaxon:9606
---
# GTEx (Genotype-Tissue Expression)

## Overview

The Genotype-Tissue Expression (GTEx) project is a comprehensive public resource to study tissue-specific gene expression and its regulation. GTEx provides insights into the mechanisms of gene regulation by analyzing human gene expression across diverse tissues and linking expression patterns to genetic variation.

## Data Collection

### Sample Collection
- **Donors**: Nearly 1,000 individuals (predominantly of European ancestry)
- **Tissues**: 54 non-diseased tissue sites
- **Quality Control**: Strict protocols for rapid tissue collection and processing
- **Sample Size**: Over 17,000 tissue samples analyzed

### Molecular Assays
- **RNA-Seq**: Comprehensive transcriptomic profiling across all tissue samples
- **Whole Genome Sequencing (WGS)**: High-coverage sequencing for genetic variant detection
- **Whole Exome Sequencing (WES)**: Focused sequencing of protein-coding regions
- **Genotyping Arrays**: Additional genotype data for population genetic analyses

## Key Features

### Expression Quantitative Trait Loci (eQTLs)
- Systematic mapping of genetic variants affecting gene expression
- Tissue-specific and cross-tissue eQTL analysis
- Fine-mapping of causal variants
- Integration with GWAS data for functional interpretation

### Tissue-Specific Expression Patterns
- Comparative analysis across 54 tissue types
- Identification of tissue-specific genes and isoforms
- Co-expression network analysis
- Developmental and physiological expression patterns

### Splicing Analysis
- Genome-wide splicing QTL (sQTL) mapping
- Alternative splicing patterns across tissues
- Splicing efficiency and regulation analysis
- Integration with protein-coding predictions

## Access and Usage

### Data Portal
The GTEx Portal provides user-friendly interfaces for:
- Gene expression visualization across tissues
- eQTL browsing and analysis tools
- Single tissue and cross-tissue analyses
- Data download capabilities

### Programmatic Access
- REST API for automated data retrieval
- Bulk data downloads in standard formats
- Integration with analysis pipelines
- R/Python package compatibility

### Data Sharing
- Open access to summary-level data
- Individual-level data available through dbGaP (phs000424)
- Standardized data formats for interoperability
- Regular data releases with expanded sample sizes

## Applications

### Functional Genomics
- Interpretation of GWAS findings
- Identification of target genes for disease variants
- Understanding of regulatory mechanisms
- Prioritization of therapeutic targets

### Comparative Biology
- Cross-tissue expression comparisons
- Evolutionary conservation of expression patterns
- Tissue-specific regulatory networks
- Development and aging studies

### Precision Medicine
- Pharmacogenomics applications
- Disease susceptibility prediction
- Treatment response biomarkers
- Population-specific analyses