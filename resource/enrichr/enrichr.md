---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://labs.icahn.mssm.edu/maayanlab/
  label: Ma'ayan Laboratory
creation_date: '2026-05-21T00:00:00Z'
description: Enrichr is a Ma'ayan Lab web-based gene set enrichment analysis resource
  that accepts gene lists and related inputs, tests them against more than 200 gene
  set libraries compiled from external databases (e.g. GO, KEGG, Reactome, WikiPathways,
  MSigDB, ENCODE/ChEA, GTEx, ARCHS4, LINCS L1000, GEO, DisGeNET, GWAS Catalog) and
  crowd-sourced submissions, and provides ranked enrichment results, visualizations,
  downloadable libraries, and programmatic access.
domains:
- biomedical
- genomics
- systems biology
homepage_url: https://maayanlab.cloud/Enrichr/
id: enrichr
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Enrichr
products:
- category: GraphicalInterface
  description: Main Enrichr web interface for submitting gene sets, exploring enrichment
    results, browsing libraries, and viewing interactive visualizations
  format: http
  id: enrichr.portal
  name: Enrichr Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr
  product_url: https://maayanlab.cloud/Enrichr/
- category: ProgrammingInterface
  connection_url: https://maayanlab.cloud/Enrichr/addList
  description: REST API for submitting gene lists, retrieving enrichment results,
    exporting analyses, and querying Enrichr programmatically
  format: json
  id: enrichr.api
  is_public: true
  name: Enrichr API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr
  product_url: https://maayanlab.cloud/Enrichr/help#api
- category: Product
  description: JSON endpoint listing Enrichr gene set libraries with category assignments,
    term counts, gene coverage, and source links
  format: json
  id: enrichr.library-statistics
  name: Enrichr Library Statistics
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr
  product_url: https://maayanlab.cloud/Enrichr/datasetStatistics
  warnings: []
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
  - relation_type: prov:hadPrimarySource
    source: biocarta
  product_url: https://maayanlab.cloud/Enrichr/#libraries
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
    source: gene-expression-omnibus
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
    source: gene-expression-omnibus
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
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: tcga
  product_url: https://maayanlab.cloud/chea3/index.html#content4-13
- category: GraphicalInterface
  description: Interactive web interface for gene set enrichment analysis, Enrichr
    term expansion, and graph exploration across integrated Enrichr-KG libraries
  format: http
  id: enrichr-kg.portal
  name: Enrichr-KG Explorer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr-kg
  product_url: https://maayanlab.cloud/enrichr-kg/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: enrichr
- category: ProgrammingInterface
  description: API surface for programmatic access to Enrichr-KG enrichment analysis
    and graph-backed query results
  format: json
  id: enrichr-kg.api
  is_public: true
  name: Enrichr-KG API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr-kg
  product_url: https://maayanlab.cloud/enrichr-kg/api/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: enrichr
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
- category: Product
  description: Node-table CSV snapshot from the Enrichr-KG downloads page containing
    node metadata for a current release
  format: csv
  id: enrichr-kg.nodes-csv
  name: Enrichr-KG Node CSV Snapshot
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr-kg
  - relation_type: prov:hadPrimarySource
    source: enrichr
  product_file_size: 1588029
  product_url: https://s3.amazonaws.com/maayan-kg/enrichr-kg/current/Gene.nodes.csv
- category: Product
  description: Edge-table CSV snapshot from the Enrichr-KG downloads page using source.relation.target
    edge triples
  format: csv
  id: enrichr-kg.edges-csv
  name: Enrichr-KG Edge CSV Snapshot
  original_source:
  - relation_type: prov:hadPrimarySource
    source: enrichr-kg
  - relation_type: prov:hadPrimarySource
    source: enrichr
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 35177347
  product_url: https://s3.amazonaws.com/maayan-kg/enrichr-kg/current/GO_Biological_Process_2021.GO_BP.Gene.edges.csv
- category: Product
  description: Gene-gene co-occurrence matrix computed from gene lists submitted to
    Enrichr, used by Geneshot to predict related genes.
  format: tsv
  id: geneshot.enrichr-cooccurrence
  name: Enrichr Gene Co-occurrence Matrix
  original_source:
  - relation_type: prov:hadPrimarySource
    source: geneshot
  - relation_type: prov:hadPrimarySource
    source: enrichr
  product_file_size: 1593574495
  product_url: https://s3.amazonaws.com/mssm-data/list_off_co.tsv
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
  - 'File was not able to be retrieved when checked on 2026-10-27: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-10-28: HTTP 404 error
    when accessing file'
publications:
- authors:
  - Chen EY
  - Tan CM
  - Kou Y
  - Duan Q
  - Wang Z
  - Meirelles GV
  - Clark NR
  - Ma'ayan A
  doi: 10.1186/1471-2105-14-128
  id: doi:10.1186/1471-2105-14-128
  journal: BMC Bioinformatics
  preferred: true
  title: 'Enrichr: interactive and collaborative HTML5 gene list enrichment analysis
    tool'
  year: '2013'
- authors:
  - Kuleshov MV
  - Jones MR
  - Rouillard AD
  - Fernandez NF
  - Duan Q
  - Wang Z
  - Koplev S
  - Jenkins SL
  - Jagodnik KM
  - Lachmann A
  - McDermott MG
  - Monteiro CD
  - Gundersen GW
  - Ma'ayan A
  doi: 10.1093/nar/gkw377
  id: doi:10.1093/nar/gkw377
  journal: Nucleic Acids Research
  preferred: false
  title: 'Enrichr: a comprehensive gene set enrichment analysis web server 2016 update'
  year: '2016'
- authors:
  - Xie Z
  - Bailey A
  - Kuleshov MV
  - Clarke DJB
  - Evangelista JE
  - Jenkins SL
  - Lachmann A
  - Wojciechowicz ML
  - Kropiwnicki E
  - Jagodnik KM
  - Jeon M
  - Ma'ayan A
  doi: 10.1002/cpz1.90
  id: doi:10.1002/cpz1.90
  journal: Current Protocols
  preferred: false
  title: Gene Set Knowledge Discovery with Enrichr
  year: '2021'
repository: https://github.com/MaayanLab/enrichr_issues
rrid: SCR_001575
taxon:
- NCBITaxon:9606
---
# Enrichr

Enrichr is a widely used web-based enrichment analysis platform for interpreting gene lists against a large collection of curated and derived gene set libraries. The current public deployment provides interactive submission and result views, library browsing, multiple scoring schemes, and a documented REST API for automated workflows.

Current Enrichr documentation describes support for crisp and fuzzy gene sets, optional background-aware enrichment through the linked Speedrichr service, downloadable enrichment result exports, and a large catalog of libraries spanning transcription, pathways, ontologies, diseases, drugs, cell types, and crowd-contributed signatures. The public site also exposes library statistics as structured JSON.

## Access

- Main portal: [Enrichr](https://maayanlab.cloud/Enrichr/)
- API documentation: [Enrichr API](https://maayanlab.cloud/Enrichr/help#api)
- Library statistics: [datasetStatistics](https://maayanlab.cloud/Enrichr/datasetStatistics)
- Gene set library downloads: [Libraries](https://maayanlab.cloud/Enrichr/#libraries); individual libraries can be fetched as GMT-style text via `https://maayanlab.cloud/Enrichr/geneSetLibrary?mode=text&libraryName=<library>`

## Gene Set Library Sources

As of October 2026 the library statistics endpoint lists 228 libraries in eight categories (Transcription, Pathways, Ontologies, Diseases/Drugs, Cell Types, Misc, Legacy, Crowd). Libraries are built from external resources including Gene Ontology, KEGG, Reactome, WikiPathways, PFOCR, PANTHER, HumanCyc, BioPlanet, NCI-Nature PID, MSigDB, ChEA, ENCODE, JASPAR, TRRUST, ARCHS4, GTEx, BioGPS, ProteomicsDB, LINCS L1000 and the Connectivity Map, GEO-derived perturbation signatures, DepMap/Achilles and CCLE, DisGeNET, OMIM, Orphanet, ClinVar, GWAS Catalog, UK Biobank, dbGaP, the Human Phenotype Ontology, MGI Mammalian Phenotype annotations, IMPC/KOMP2, CellMarker, HuBMAP/Azimuth, the JensenLab COMPARTMENTS, DISEASES, and TISSUES resources, DGIdb, DrugCentral, KINOMEscan, HMDB, CORUM, BioPlex, miRTarBase, and others, as well as crowd-contributed Enrichr gene lists.

## Citation

- Chen EY et al. Enrichr: interactive and collaborative HTML5 gene list enrichment analysis tool. BMC Bioinformatics. 2013;14:128. doi:10.1186/1471-2105-14-128
- Kuleshov MV et al. Enrichr: a comprehensive gene set enrichment analysis web server 2016 update. Nucleic Acids Research. 2016. doi:10.1093/nar/gkw377
- Xie Z et al. Gene Set Knowledge Discovery with Enrichr. Current Protocols. 2021;1:e90. doi:10.1002/cpz1.90

## Automated Evaluation

- View the automated evaluation: [enrichr automated evaluation](enrichr_eval_automated.html)