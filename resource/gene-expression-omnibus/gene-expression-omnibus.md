---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: geo@ncbi.nlm.nih.gov
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/geo/
  label: NCBI Gene Expression Omnibus
creation_date: '2026-07-01T00:00:00Z'
description: The Gene Expression Omnibus (GEO) is a public functional genomics data
  repository maintained by the NCBI at the U.S. National Library of Medicine. It archives
  and freely distributes high-throughput gene expression and other functional genomics
  datasets, including the single-cell and single-nucleus studies of human pancreatic
  islets that PanKbase identified and reprocessed.
domains:
- biomedical
- genomics
- gene expression profiling
homepage_url: https://www.ncbi.nlm.nih.gov/geo/
id: gene-expression-omnibus
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
name: Gene Expression Omnibus (GEO)
products:
- category: GraphicalInterface
  description: Web portal for searching, browsing, and downloading functional genomics
    datasets archived in the Gene Expression Omnibus.
  format: http
  id: gene-expression-omnibus.portal
  name: GEO Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  product_url: https://www.ncbi.nlm.nih.gov/geo/
- category: GraphProduct
  description: Pancreas-focused knowledge graph integrating genes, SNPs, pancreatic
    expression QTLs, and donor-derived islet datasets harmonized within PanKbase.
  format: http
  id: pankgraph.graph
  name: PanKgraph Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pankgraph
  - relation_type: prov:wasDerivedFrom
    source: pankbase
  - relation_type: prov:hadPrimarySource
    source: hpap
  - relation_type: prov:hadPrimarySource
    source: iidp
  - relation_type: prov:hadPrimarySource
    source: prodo
  product_url: https://pankgraph.org/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: gene-expression-omnibus
- category: GraphProduct
  description: RDF (Turtle) knowledge graph of the NIAID Data Ecosystem, harmonizing
    dataset and computational-tool metadata harvested from NIAID-funded and globally-relevant
    infectious and immune-mediated disease repositories. Served through the Proto-OKN
    FRINK federated SPARQL platform.
  format: ttl
  id: nde.graph
  name: NIAID Data Ecosystem KG (graph)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nde
  - relation_type: prov:hadPrimarySource
    source: immport
  - relation_type: prov:hadPrimarySource
    source: vdjserver
  product_url: https://frink.apps.renci.org/nde
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: gene-expression-omnibus
  - relation_type: prov:wasInfluencedBy
    source: sra
  - relation_type: prov:wasInfluencedBy
    source: omicsdi
  - relation_type: prov:wasInfluencedBy
    source: hubmap
  - relation_type: prov:wasInfluencedBy
    source: massive
  - relation_type: prov:wasInfluencedBy
    source: pdb
  - relation_type: prov:wasInfluencedBy
    source: lincs
- category: Product
  description: Sample metadata for every organoid sample in OrganoidDB, with study
    and sample accessions, tissue, platform, species, PubMed ID and sample characteristics.
  format: csv
  id: organoiddb.all-organoid-samples
  name: OrganoidDB all organoid samples
  original_source:
  - relation_type: prov:hadPrimarySource
    source: organoiddb
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_file_size: 3258002
  product_url: http://www.inbirg.com/organoid_db/download/all_org_samples
- category: Product
  description: Sample metadata for the organoid samples used by the OrganoidDB organoid
    specificity search.
  format: csv
  id: organoiddb.organoid-specificity-samples
  name: OrganoidDB organoid specificity samples
  original_source:
  - relation_type: prov:hadPrimarySource
    source: organoiddb
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_file_size: 257601
  product_url: http://www.inbirg.com/organoid_db/download/org_specificity_samples
- category: Product
  description: Sample metadata for the primary tissue and cell line samples that OrganoidDB
    uses for comparison with organoids.
  format: csv
  id: organoiddb.general-samples
  name: OrganoidDB general samples
  original_source:
  - relation_type: prov:hadPrimarySource
    source: organoiddb
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  product_file_size: 94026
  product_url: http://www.inbirg.com/organoid_db/download/general_samples
- category: GraphicalInterface
  description: KLOCD web interface for searching its drug, chemical, gene expression
    dataset, disease, toxicant, literature, patent and organ-on-chip model sub-databases,
    built from PubMed, PubChem, TogoWS, UniChem, DrugBank, ChEMBL, ClinicalTrials.gov,
    AACT, the European Medicines Agency, CTD, NCBI GEO, openFDA and Disease Ontology,
    among other public sources.
  format: http
  id: klocd.portal
  name: KLOCD Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: klocd
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: togows
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: aact
  - relation_type: prov:hadPrimarySource
    source: ema
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: openfda
  - relation_type: prov:hadPrimarySource
    source: doid
  product_url: http://www.organchip.cn/
- category: GraphicalInterface
  description: Web portal for searching and browsing integrated omics dataset metadata
    across repositories.
  format: http
  id: omicsdi.portal
  name: OmicsDI Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omicsdi
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  product_url: https://www.omicsdi.org/
- category: ProgrammingInterface
  connection_url: https://www.omicsdi.org/ws
  description: Swagger-documented web service for programmatic querying of OmicsDI
    dataset metadata.
  format: http
  id: omicsdi.api
  is_public: true
  name: OmicsDI API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: omicsdi
  - relation_type: prov:hadPrimarySource
    source: gene-expression-omnibus
  - relation_type: prov:hadPrimarySource
    source: arrayexpress
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: biostudies
  - relation_type: prov:hadPrimarySource
    source: massive
  - relation_type: prov:hadPrimarySource
    source: gnps
  - relation_type: prov:hadPrimarySource
    source: mw
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: proteomexchange
  product_url: https://www.omicsdi.org/ws/swagger-ui/index.html
---
Gene Expression Omnibus (GEO)

## Description

The Gene Expression Omnibus (GEO) is a public functional genomics data repository operated by the NCBI. PanKbase used systematic searches of GEO to identify islet single-cell and single-nucleus studies (including those using IIDP- and Prodo-supplied islets), which were then reprocessed through a harmonized pipeline. GEO therefore acts as an aggregating upstream influence on PanKbase and PanKgraph.