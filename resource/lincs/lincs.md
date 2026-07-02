---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: ilincs@googlegroups.com
  label: BD2K-LINCS Data Coordination and Integration Center
- category: Organization
  label: National Institutes of Health (NIH) Common Fund
creation_date: '2025-05-29T00:00:00Z'
description: The Library of Integrated Network-based Cellular Signatures (LINCS) is
  a comprehensive collection of data that catalogs how human cells globally respond
  to chemical, genetic, and disease perturbations. It aims to better understand human
  disease and advance the development of new therapies by assembling an integrated
  picture of the range of responses of human cells exposed to many perturbations.
domains:
- biomedical
- drug discovery
- systems biology
- genomics
- proteomics
- precision medicine
homepage_url: https://lincsportal.ccs.miami.edu/signatures/home
id: lincs
infores_id: lincs
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
name: LINCS
products:
- category: GraphicalInterface
  description: Web interface that allows users to explore, analyze, and visualize
    LINCS signatures and datasets.
  format: http
  id: lincs.portal
  name: LINCS Data Portal 2.0
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lincs
  product_url: https://lincsportal.ccs.miami.edu/signatures/home
- category: ProgrammingInterface
  description: API for programmatic access to LINCS data and signatures.
  format: http
  id: lincs.api
  is_public: true
  name: LINCS API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lincs
  product_url: https://lincsportal.ccs.miami.edu/sigc-api/swagger-ui.html#/
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  format: neo4j
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
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  format: mixed
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
  description: LINCS compound similarity edges
  format: csv
  id: prokn.lincs.compound.in_similarity_relationship_with.compound.edges
  name: ProKN LINCS Compound Similarity Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 6193189
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_LINCS.Compound.IN_SIMILARITY_RELATIONSHIP_WITH.Compound.edges.csv
- category: GraphProduct
  description: LINCS compound negatively regulates gene edges
  format: csv
  id: prokn.lincs.compound.negatively_regulates.gene.edges
  name: ProKN LINCS Negative Regulation Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 28342168
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_LINCS.Compound.NEGATIVELY_REGULATES.Gene.edges.csv
- category: GraphProduct
  description: LINCS compound positively regulates gene edges
  format: csv
  id: prokn.lincs.compound.positively_regulates.gene.edges
  name: ProKN LINCS Positive Regulation Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 28223124
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_LINCS.Compound.POSITIVELY_REGULATES.Gene.edges.csv
- category: GraphProduct
  description: LINCS P100 perturbagen experiment edges
  format: csv
  id: prokn.lincs_p100.perturbagen.is_used_in.experiment.edges
  name: ProKN LINCS P100 Perturbagen Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 541848
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/LINCS_P100.Perturbagen.IS_USED_IN.Experiment.edges.csv
- category: GraphProduct
  description: LINCS P100 experiment perturbation effect on PTM site edges
  format: csv
  id: prokn.lincs_p100.experiment.perturbation_effect.ptmsite.edges
  name: ProKN LINCS P100 Perturbation Effect Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 52555993
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/LINCS_P100.Experiment.PERTURBATION_EFFECT.PTMSite.edges.csv
- category: GraphProduct
  description: LINCS P100 PTM site is site of site edges
  format: csv
  id: prokn.lincs_p100.ptmsite.is_site.site.edges
  name: ProKN LINCS P100 PTM Site Mapping Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 980
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/LINCS_P100.PTMSite.IS_SITE.Site.edges.csv
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
  format: txt
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
  product_file_size: 522141103
  product_url: https://s3.amazonaws.com/maayan-kg/enrichr-kg/dumps/enrichr-kg-042123.dump
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
- category: GraphicalInterface
  description: Cloud-based user interface providing suite of apps for querying gene
    expression signatures, browsing perturbagen data, searching metadata, and visualizing
    connectivity results
  format: http
  id: cmap.clue
  name: CLUE Platform
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmap
  product_url: https://clue.io/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: lincs
- category: ProgrammingInterface
  description: Python library cmapBQ for programmatic access to CMap data through
    Google BigQuery with query capabilities for signatures and metadata
  format: http
  id: cmap.python_api
  is_public: true
  name: cmapBQ Python Library
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmap
  product_url: https://cmapbq.readthedocs.io/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: lincs
- category: GraphicalInterface
  description: Query app enabling users to search CMap database with custom gene expression
    signatures to find perturbagens with similar or opposing transcriptional effects
  format: http
  id: cmap.query_app
  name: CLUE Query App
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmap
  product_url: https://clue.io/query
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: lincs
- category: Product
  description: Data releases containing replicate-collapsed signatures and gene expression
    profiles in GCTx matrix format available for download
  format: hdf5
  id: cmap.data_downloads
  name: CMap Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmap
  product_url: https://clue.io/releases/data-dashboard
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: lincs
- category: DocumentationProduct
  description: Comprehensive knowledge base containing glossary, tutorials, analytical
    methods, experimental protocols, and detailed documentation
  format: http
  id: cmap.connectopedia
  name: Connectopedia
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cmap
  product_url: https://clue.io/connectopedia
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: lincs
- category: GraphProduct
  description: Statistically inferred genomic evidence graph connecting genes, gene
    sets, inferred disease mechanisms, and human phenotypes. Gene sets are derived
    from eleven NIH Common Fund programs (GlyGen, GTEx, IDG, IMPC/KOMP2, LINCS, MoTrPAC,
    Bridge2AI, HuBMAP, Metabolomics Workbench, SenNet, and SPARC) and phenotype-gene
    set relationships are computed with PIGEAN (Priors Inferred from GEne ANnotations).
  format: http
  id: digcfdekg.graph
  name: CFDE REVEAL Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: digcfdekg
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: impc
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: motrpac
  - relation_type: prov:hadPrimarySource
    source: bridge2ai
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: sennet
  - relation_type: prov:hadPrimarySource
    source: sparc
  product_url: https://cfdeknowledge.org/r/cfde_reveal
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hubmap
publications:
- authors:
  - Keenan AB
  - Jenkins SL
  - Jagodnik KM
  - Koplev S
  - He E
  - Torre D
  - Wang Z
  - Dohlman AB
  - Silverstein MC
  - Lachmann A
  - Kuleshov MV
  - Ma'ayan A
  - Stathias V
  - Terryn R
  - Cooper D
  - Forlin M
  - Koleti A
  - Vidovic D
  - Chung C
  - "Sch\xFCrer SC"
  - Vasiliauskas J
  - Pilarczyk M
  - Shamsaei B
  - Fazel M
  - Ren Y
  - Niu W
  - Clark NA
  - White S
  - Mahi N
  - Zhang L
  - Kouril M
  - Reichard JF
  - Sivaganesan S
  - Medvedovic M
  - Meller J
  - Koch RJ
  - Birtwistle MR
  - Iyengar R
  - Sobie EA
  - Azeloglu EU
  - Kaye J
  - Osterloh J
  - Haston K
  - Kalra J
  - Finkbiener S
  - Li J
  - Milani P
  - Adam M
  - Escalante-Chong R
  - Sachs K
  - Lenail A
  - Ramamoorthy D
  - Fraenkel E
  - Daigle G
  - Hussain U
  - Coye A
  - Rothstein J
  - Sareen D
  - Ornelas L
  - Banuelos M
  - Mandefro B
  - Ho R
  - Svendsen CN
  - Lim RG
  - Stocksdale J
  - Casale MS
  - Thompson TG
  - Wu J
  - Thompson LM
  - Dardov V
  - Venkatraman V
  - Matlock A
  - Van Eyk JE
  - Jaffe JD
  - Papanastasiou M
  - Subramanian A
  - Golub TR
  - Erickson SD
  - Fallahi-Sichani M
  - Hafner M
  - Gray NS
  - Lin JR
  - Mills CE
  - Muhlich JL
  - Niepel M
  - Shamu CE
  - Williams EH
  - Wrobel D
  - Sorger PK
  - Heiser LM
  - Gray JW
  - Korkola JE
  - Mills GB
  - LaBarge M
  - Feiler HS
  - Dane MA
  - Bucher E
  - Nederlof M
  - Sudar D
  - Gross S
  - Kilburn DF
  - Smith R
  - Devlin K
  - Margolis R
  - Derr L
  - Lee A
  - Pillai A
  doi: doi:10.1016/j.cels.2017.11.001
  id: https://doi.org/10.1016/j.cels.2017.11.001
  journal: Cell Systems
  preferred: true
  title: The Library of Integrated Network-Based Cellular Signatures NIH Program -
    System-Level Cataloging of Human Cells Response to Perturbations
  year: '2018'
- authors:
  - Koleti A
  - Terryn R
  - Stathias V
  - Chung C
  - Cooper DJ
  - Turner JP
  - Vidovic D
  - Forlin M
  - Kelley TT
  - D'Urso A
  - Allen BK
  - Torre D
  - Jagodnik KM
  - Wang L
  - Jenkins SL
  - Mader C
  - Niu W
  - Fazel M
  - Mahi N
  - Pilarczyk M
  - Clark N
  - Shamsaei B
  - Meller J
  - Vasiliauskas J
  - Reichard J
  - Medvedovic M
  - Ma'ayan A
  - Pillai A
  - "Sch\xFCrer SC"
  doi: doi:10.1093/nar/gkx1063
  id: https://doi.org/10.1093/nar/gkx1063
  journal: Nucleic Acids Research
  title: Data Portal for the Library of Integrated Network-based Cellular Signatures
    (LINCS) program - integrated access to diverse large-scale cellular perturbation
    response data
  year: '2018'
- authors:
  - Marcin Pilarczyk
  - Mehdi Fazel-Najafabadi
  - Michal Kouril
  - Behrouz Shamsaei
  - Juozas Vasiliauskas
  - Wen Niu
  - Naim Mahi
  - Lixia Zhang
  - Nicholas A. Clark
  - Yan Ren
  - Shana White
  - Rashid Karim
  - Huan Xu
  - Jacek Biesiada
  - Mark F. Bennett
  - Sarah E. Davidson
  - John F. Reichard
  - Kurt Roberts
  - Vasileios Stathias
  - Amar Koleti
  - Dusica Vidovic
  - Daniel J. B. Clarke
  - "Stephan C. Sch\xFCrer"
  - "Avi Ma\u2019ayan"
  - Jarek Meller
  - Mario Medvedovic
  doi: 10.1038/s41467-022-32205-3
  id: doi:10.1038/s41467-022-32205-3
  journal: Nature Communications
  title: Connecting omics signatures and revealing biological mechanisms with iLINCS
  year: '2022'
taxon:
- NCBITaxon:9606
---
The Library of Integrated Network-based Cellular Signatures (LINCS) is an NIH Common Fund program that catalogs how human cells globally respond to chemical, genetic, and disease perturbations. By assembling an integrated picture of the range of responses of human cells exposed to many perturbations, the LINCS program aims to better understand human disease and to advance the development of new therapies.

LINCS contains data on cellular responses to thousands of perturbagens (including drugs, genetic perturbations, tissue micro-environments, antibodies, and disease-causing mutations) across multiple cell types. These responses are measured using various high-throughput technologies including:

1. **L1000 Technology**: A cost-effective method to measure the expression of ~1,000 landmark genes that can be used to infer the expression of the rest of the transcriptome
2. **P100 Assay**: A targeted mass spectrometry-based proteomics approach that measures ~100 key phosphorylation sites
3. **Cell Painting**: A high-content imaging method that uses multiple fluorescent dyes to label different cellular components
4. **Other Assays**: Including RNA-seq, proteomics, epigenomics, and other cellular measurements

The program focuses on cellular physiology shared among tissues and cell types relevant to an array of diseases, including cancer, heart disease, and neurodegenerative disorders. The data generated by LINCS is freely available to the research community through various portals and tools, with iLINCS being one of the primary access points.

LINCS data has led to important research discoveries, including new tools for enhancing drug discovery and predicting adverse health events. Although the NIH Common Fund supported the LINCS program from 2011 to 2020, the data and resources continue to be available for researchers worldwide.