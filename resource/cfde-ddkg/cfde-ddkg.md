---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Individual
    contact_details:
      - contact_type: github
        value: jeevangelista
    label: John Erol Evangelista
  - category: Organization
    contact_details:
      - contact_type: github
        value: MaayanLab
      - contact_type: url
        value: https://maayanlab.cloud/
    label: Ma'ayan Lab
description: The Data Distillery Knowledge Graph (DDKG) integrates summarized ("distilled")
  data from multiple NIH Common Fund Data Coordinating Centers (DCCs) within a knowledge
  graph, as part of the Common Fund Data Ecosystem (CFDE). Its schema is based on the
  Unified Biomedical Knowledge Graph (UBKG), which builds on the UMLS and adds over 180
  ontologies and standards. The DDKG is accessible through a web interface, a programmatic
  API, and downloadable per-DCC subgraphs.
domains:
  - biomedical
homepage_url: https://dd-kg-ui.cfde.cloud/
id: cfde-ddkg
last_modified_date: '2026-10-09T00:00:00Z'
layout: resource_detail
license:
  display_note: 'No license is declared for this resource. This is the most restrictive
    license (custom) among its sources: 4dn, gtex, msigdb, ubkg, umls. Not accounted
    for, no known license: gene-expression-omnibus, kidsfirst, lincs, mw, sckan.'
  id: https://data.4dnucleome.org/help/user-guide/faq#downloading-and-using-data-from-the-4dn-data-portal
  inferred_from:
  - 4dn
  - gtex
  - msigdb
  - ubkg
  - umls
  label: Varies
  restrictiveness: custom
  status: inferred
  unresolved_sources:
  - gene-expression-omnibus
  - kidsfirst
  - lincs
  - mw
  - sckan
name: Data Distillery Knowledge Graph (DDKG)
products:
  - category: GraphicalInterface
    description: Interactive web interface for browsing and querying Data Distillery Knowledge Graph resources.
    format: http
    id: cfde-ddkg.portal
    name: DDKG Web Interface
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: ubkg
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
    product_url: https://dd-kg-ui.cfde.cloud/
  - category: Product
    description: JSON manifest listing downloadable DDKG resources and files.
    format: json
    id: cfde-ddkg.downloads
    name: DDKG Downloads Manifest
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: ubkg
        relation_type: prov:hadPrimarySource
      - source: umls
        relation_type: prov:hadPrimarySource
    product_file_size: 5216
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/minio/downloads.json
  - category: GraphProduct
    compression: zip
    description: Data Distillery HuBMAP subgraph (build of 2024-09-20) as CSV node and
      edge files. Tissue, cell-type and gene specific markers from single-cell data.
    format: csv
    id: cfde-ddkg.hubmap
    name: DDKG HuBMAP Subgraph
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: hubmap
        relation_type: prov:hadPrimarySource
    product_file_size: 70525
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/09202024/HuBMAP.zip
  - category: GraphProduct
    compression: zip
    description: Data Distillery IDG subgraph (build of 2024-09-20) as CSV node and
      edge files. Relationships between compounds, diseases, and proteins.
    format: csv
    id: cfde-ddkg.idg
    name: DDKG IDG Subgraph
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: tcrd
        relation_type: prov:hadPrimarySource
    product_file_size: 29239738
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/09202024/IDG.zip
  - category: GraphProduct
    compression: zip
    description: Data Distillery GlyGen subgraph (build of 2024-09-20) as CSV node and
      edge files. Associations from multiple glycomics database.
    format: csv
    id: cfde-ddkg.glygen
    name: DDKG GlyGen Subgraph
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: glygen
        relation_type: prov:hadPrimarySource
    product_file_size: 43798093
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/09202024/GlyGen.zip
  - category: GraphProduct
    compression: zip
    description: Data Distillery GTEx subgraph (build of 2024-09-20) as CSV node and
      edge files. Expression and eQTL data from GTEx.
    format: csv
    id: cfde-ddkg.gtex
    name: DDKG GTEx Subgraph
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
    product_file_size: 410137152
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/09202024/GTEx.zip
  - category: GraphProduct
    compression: zip
    description: Data Distillery SPARC subgraph (build of 2024-09-20) as CSV node and
      edge files. The SPARC Knowledge base of the Autonomic Nervous System (SCKAN).
    format: csv
    id: cfde-ddkg.sparc
    name: DDKG SPARC Subgraph
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: sparc
        relation_type: prov:hadPrimarySource
      - source: sckan
        relation_type: prov:hadPrimarySource
    product_file_size: 198292
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/09202024/SPARC.zip
  - category: GraphProduct
    compression: zip
    description: Data Distillery HGNC-HPO subgraph (build of 2024-09-20) as CSV node and
      edge files. HGNC gene node mapping to Human Phenotype Ontology.
    format: csv
    id: cfde-ddkg.hgnchpo
    name: DDKG HGNC-HPO Subgraph
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
    product_file_size: 15167322
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/09202024/HGNCHPO.zip
  - category: GraphProduct
    compression: zip
    description: Data Distillery ClinVar subgraph (build of 2024-09-20) as CSV node and
      edge files. Assertions between human genes and phenotypes.
    format: csv
    id: cfde-ddkg.clinvar
    name: DDKG ClinVar Subgraph
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
    product_file_size: 2469156
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/09202024/CLINVAR.zip
  - category: GraphProduct
    compression: zip
    description: Data Distillery MoTrPAC subgraph (build of 2024-09-20) as CSV node and
      edge files. Differential gene expression data from endurance training exercise of young adult rats.
    format: csv
    id: cfde-ddkg.motrpac
    name: DDKG MoTrPAC Subgraph
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: motrpac
        relation_type: prov:hadPrimarySource
    product_file_size: 1285545
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/09202024/MoTrPAC.zip
  - category: GraphProduct
    compression: zip
    description: Data Distillery HGNC-UniProt subgraph (build of 2024-09-20) as CSV node and
      edge files. Gene-Protein relationships.
    format: csv
    id: cfde-ddkg.hgncuniprot
    name: DDKG HGNC-UniProt Subgraph
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
    product_file_size: 937014
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/09202024/HGNCUNIPROT.zip
  - category: GraphProduct
    compression: zip
    description: Data Distillery Kids First subgraph (build of 2024-09-20) as CSV node and
      edge files. Genotypic and phenotypic data from the Pediatric Cardiac Genetics Consortium cohort in Kids First.
    format: csv
    id: cfde-ddkg.kf
    name: DDKG Kids First Subgraph
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: kidsfirst
        relation_type: prov:hadPrimarySource
    product_file_size: 3407714
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/09202024/KF.zip
  - category: GraphProduct
    compression: zip
    description: Data Distillery LINCS subgraph (build of 2024-09-20) as CSV node and
      edge files. Gene expression data from drug perturbation, as well as drug-drug similarity.
    format: csv
    id: cfde-ddkg.lincs
    name: DDKG LINCS Subgraph
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
    product_file_size: 12175464
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/09202024/LINCS.zip
  - category: GraphProduct
    compression: zip
    description: Data Distillery HGNC Enzyme Genes subgraph (build of 2024-09-20) as CSV node and
      edge files. HGNC enzyme gene list.
    format: csv
    id: cfde-ddkg.hgnc-enzyme
    name: DDKG HGNC Enzyme Genes Subgraph
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: hgnc
        relation_type: prov:hadPrimarySource
    product_file_size: 84470
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/09202024/hgnc_enzyme.zip
  - category: GraphProduct
    compression: zip
    description: Data Distillery ARCHS4 subgraph (build of 2024-09-20) as CSV node and
      edge files. Coexpression Matrix based on Human RNA-seq studies from GEO.
    format: csv
    id: cfde-ddkg.archs4
    name: DDKG ARCHS4 Subgraph
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: archs4
        relation_type: prov:hadPrimarySource
      - source: gene-expression-omnibus
        relation_type: prov:hadPrimarySource
    product_file_size: 11358770
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/09202024/ARCHS4.zip
  - category: GraphProduct
    compression: zip
    description: Data Distillery Metabolomics Workbench subgraph (build of 2024-09-20) as CSV node and
      edge files. Metabolite relationships with gene, disease, and cell.
    format: csv
    id: cfde-ddkg.mw
    name: DDKG Metabolomics Workbench Subgraph
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: mw
        relation_type: prov:hadPrimarySource
    product_file_size: 2157693
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/09202024/MW.zip
  - category: GraphProduct
    compression: zip
    description: Data Distillery MSigDB subgraph (build of 2024-09-20) as CSV node and
      edge files. Five subsets of MSigDB v7.4 datasets.
    format: csv
    id: cfde-ddkg.msigdb
    name: DDKG MSigDB Subgraph
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: msigdb
        relation_type: prov:hadPrimarySource
    product_file_size: 34094044
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/09202024/MSIGDB.zip
  - category: GraphProduct
    compression: zip
    description: Data Distillery ERCC subgraph (build of 2024-09-20) as CSV node and
      edge files. eCLIP-seq and CHIP-seq associations from ERCC.
    format: csv
    id: cfde-ddkg.ercc
    name: DDKG ERCC Subgraph
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: erccrbp
        relation_type: prov:hadPrimarySource
      - source: erccreg
        relation_type: prov:hadPrimarySource
    product_file_size: 405251470
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/09202024/ERCC.zip
  - category: GraphProduct
    compression: zip
    description: Data Distillery 4DN subgraph (build of 2024-09-20) as CSV node and
      edge files. Chromatin loops called from Hi-C experiments performed in select cell lines.
    format: csv
    id: cfde-ddkg.4dn
    name: DDKG 4DN Subgraph
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
      - source: 4dn
        relation_type: prov:hadPrimarySource
    product_file_size: 51622960
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/09202024/4DN.zip
  - category: ProgrammingInterface
    description: REST API for searching DDKG nodes, retrieving subgraphs, and running
      Data Distillery use-case queries. The OpenAPI specification is at
      https://s3.amazonaws.com/maayan-kg/dd-kg/minio/specs.json.
    format: http
    id: cfde-ddkg.api
    is_public: true
    name: DDKG API
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
    product_url: https://dd-kg-ui.cfde.cloud/api-doc
  - category: DocumentationProduct
    description: Data dictionary describing the DDKG node types, edge types, and
      source abbreviations (SABs).
    format: http
    id: cfde-ddkg.dictionary
    name: DDKG Data Dictionary
    original_source:
      - source: cfde-ddkg
        relation_type: prov:hadPrimarySource
    product_file_size: 191306
    product_url: https://s3.amazonaws.com/maayan-kg/dd-kg/minio/Dictionary/DataDistilleryDataDictionary0228.html
publications:
  - authors:
      - Taha Mohseni Ahooyi
      - Benjamin Stear
      - J. Alan Simmons
      - Vincent T. Metzger
      - Praveen Kumar
      - John Erol Evangelista
      - Daniel J. B. Clarke
      - Zhuorui Xie
      - Heesu Kim
      - Sherry L. Jenkins
      - Mano R. Maurya
      - Srinivasan Ramachandran
      - Eoin Fahy
      - Thomas H. Gillespie
      - Fahim T. Imam
      - Natallia Kokash
      - Matthew E. Roth
      - Robert Fullem
      - Dubravka Jevtic
      - Aleks Mihajlovic
      - Michael Tiemeyer
      - Clara Bakker
      - Andrew J. Schroeder
      - Julia Markowski
      - Jared Nedzel
      - Dave D. Hill
      - James Terry
      - Christopher Nemarich
      - Jyl Boline
      - Peter J. Park
      - Kristin G. Ardlie
      - Jeet Vora
      - Raja Mazumder
      - Rene Ranzinger
      - Bernard de Bono
      - Shankar Subramaniam
      - Jeffrey S. Grethe
      - Jeremy J. Yang
      - Christophe G. Lambert
      - Adam Resnick
      - Aleks Milosavljevic
      - Avi Ma’ayan
      - Jonathan C. Silverstein
      - Deanne M. Taylor
    doi: 10.1101/2025.08.11.666099
    id: doi:10.1101/2025.08.11.666099
    journal: bioRxiv
    preferred: true
    title: 'The Data Distillery: A Graph Framework for Semantic Integration and Querying
      of Biomedical Data'
    year: '2025'
repository: https://github.com/MaayanLab/datadistillery-kg
creation_date: '2025-03-09T00:00:00Z'
---

The Common Fund Data Ecosystem (CFDE) aims to facilitate better integration, and reuse 
of Common Fund data to accelerate discoveries in biomedical research. The Data Distillery 
project aims to integrate summarized (“distilled”) Common Fund data within a knowledge 
graph. The purpose of the Data Distillery Knowledge Graph (DDKG) is to link multiple 
sources of expertly curated data, thus providing data integration across multiple 
Common Fund data coordinating centers (DCCs). The summarized data are provided by 
participating DCCs and funded as part of the Common Fund Data Ecosystem (CFDE) project. 
The DDKG schema is based on the Unified Biomedical Knowledge Graph (UBKG) which 
originates from the Unified Medical Language System (UMLS). The UBKG supports the 
DDKG with over 180 different ontologies and standards supporting the Common Fund 
data that either are native to UMLS or were explicitly added to support biomolecular 
data. The DDKG can be used to create simple to complex queries, and use the results 
for a range of different applications related to the use of Common Fund data.

The September 2024 build is distributed as one zipped set of CSV node and edge files
per contributing DCC dataset, listed in the downloads manifest. The DDKG is described
in a 2025 bioRxiv preprint (doi:10.1101/2025.08.11.666099).

## Automated Evaluation

- View the automated evaluation: [cfde-ddkg automated evaluation](cfde-ddkg_eval_automated.html)
