---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://druggablegenome.net/
  - contact_type: email
    value: idg.rdoc@gmail.com
  label: Illuminating the Druggable Genome (IDG) Program
- category: Organization
  contact_details:
  - contact_type: url
    value: https://druggablegenome.net/KMC_UNM
  label: Knowledge Management Center - University of New Mexico
- category: Individual
  contact_details:
  - contact_type: github
    value: tudoroprea
  label: Tudor I. Oprea
creation_date: '2025-01-10T00:00:00Z'
description: The Target Central Resource Database (TCRD) is a comprehensive multi-omics
  knowledge base developed by the NIH Common Fund Illuminating the Druggable Genome
  (IDG) program to catalog and illuminate the human proteome, with special focus on
  understudied proteins in four major druggable protein families G-protein coupled
  receptors (GPCRs), nuclear receptors, ion channels, and protein kinases. TCRD aggregates
  data from over 80 diverse sources including protein-protein interactions, disease
  associations, drug-target relationships, gene expression profiles, tissue specificity,
  pathway memberships, phenotype associations, and pharmacological data to create
  a unified resource for target prioritization and drug discovery research. The database
  employs a protein Target Development Level (TDL) classification system (Tclin, Tchem,
  Tbio, Tdark) that ranks proteins based on the amount of available knowledge, specifically
  highlighting understudied dark proteins that lack adequate characterization. TCRD
  contains extensive information on protein sequences, structures, functions, disease
  relationships, and chemical interactions, integrating data from resources such as
  UniProt, ChEMBL, DrugCentral, STRING, GTEx, OMIM, and many others. The database
  is designed to be machine-learning ready with structured data formats suitable for
  computational analysis and target prediction algorithms. TCRD serves as the backend
  data infrastructure for Pharos, the user-friendly web interface that enables researchers
  to browse, visualize, and analyze the integrated target data through interactive
  tools and visualizations. The resource is continuously updated with new data sources
  and releases, with current version 6.13.5 containing comprehensive annotations for
  the human proteome.
domains:
- drug discovery
- genomics
- biological systems
homepage_url: https://datascience.unm.edu/tcrd/
id: tcrd
infores_id: tcrd
last_modified_date: '2026-06-22T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC BY-SA 4.0
name: Target Central Resource Database
products:
- category: Product
  description: MySQL database dump files containing the complete TCRD relational database
    schema and data for local installation and analysis
  format: mysql
  id: tcrd.database_download
  name: TCRD Database Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  product_url: https://unmtid-dbs.net/download/TCRD/
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
  product_url: https://unmtid-dbs.net/download/TCRD/
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
- category: GraphProduct
  description: IDG/TCRD compound-protein nodes used in ProKN
  format: csv
  id: prokn.idgp.compound.nodes
  name: ProKN TCRD Compound-Protein Compound Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 83991029
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_IDGP.Compound.nodes.csv
- category: GraphProduct
  description: TCRD compound bioactivity to protein edges
  format: csv
  id: prokn.idgp.compound.bioactivity.protein.edges
  name: ProKN TCRD Compound-Protein Bioactivity Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 128158013
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_IDGP.Compound.BIOACTIVITY.Protein.edges.csv
- category: GraphProduct
  description: IDG/TCRD compound-disease nodes used in ProKN
  format: csv
  id: prokn.idgd.compound.nodes
  name: ProKN TCRD Compound-Disease Compound Nodes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 105796
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_IDGD.Compound.nodes.csv
- category: GraphProduct
  description: TCRD compound indication edges to disease and phenotype terms
  format: csv
  id: prokn.idgd.compound.indication.diseaseorphenotype.edges
  name: ProKN TCRD Compound-Disease Indication Edges
  original_source:
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: prokn
  product_file_size: 1686928
  product_url: https://research.bioinformatics.udel.edu/prokn_dp/downloads/current/DDKG_IDGD.Compound.INDICATION.DiseaseOrPhenotype.edges.csv
- category: GraphProduct
  description: KGX Distribution of KG-IDG
  format: kgx
  id: kg-idg.graph
  name: KGX Distribution of KG-IDG
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kg-idg
  - relation_type: prov:hadPrimarySource
    source: atc
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ogms
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tcrd
  product_url: https://kg-hub.berkeleybop.io/kg-idg/current/kg-idg.tar.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-01: HTTP 404 error.
    The kg-hub.berkeleybop.io host is being reorganized and KG-IDG downloads are pending
    relocation to a new home; no live download is currently available.'
  - 'File was not able to be retrieved when checked on 2026-07-02: HTTP 404 error
    when accessing file'
- category: GraphProduct
  description: KGX nodes for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.nodes
  name: Nodes for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molecular-data-kp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 3676906360
  product_url: https://molepro.s3.amazonaws.com/nodes.tsv
- category: GraphProduct
  description: KGX edges for Molecular Data KP
  format: kgx
  id: molecular-data-kp.graph.edges
  name: Edges for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molecular-data-kp
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: tcrd
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: inchikey
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: drugrephub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 20140191116
  product_url: https://molepro.s3.amazonaws.com/edges.tsv
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
  - Timothy K Sheils
  - Stephen L Mathias
  - Keith J Kelleher
  - Vishal B Siramshetty
  - Dac-Trung Nguyen
  - Cristian G Bologa
  - Lars Juhl Jensen
  - Dušica Vidović
  - Amar Koleti
  - Stephan C Schürer
  - Anna Waller
  - Jeremy J Yang
  - Jayme Holmes
  - Giovanni Bocci
  - Noel Southall
  - Poorva Dharkar
  - Ewy Mathé
  - Anton Simeonov
  - Tudor I Oprea
  doi: 10.1093/nar/gkaa993
  id: https://doi.org/10.1093/nar/gkaa993
  journal: Nucleic Acids Research
  title: 'Pharos 2021: mining the human proteome for disease biology'
  year: '2021'
- authors:
  - Dac-Trung Nguyen
  - Stephen Mathias
  - Cristian Bologa
  - Soren Brunak
  - Nicolas Fernandez
  - Anna Gaulton
  - Anne Hersey
  - Jayme Holmes
  - Lars Juhl Jensen
  - Anneli Karlsson
  - Guixia Liu
  - Avi Ma'ayan
  - Geetha Mandava
  - Subramani Mani
  - Saurabh Mehta
  - John Overington
  - Juhee Patel
  - Andrew D. Rouillard
  - Stephan Schürer
  - Timothy Sheils
  - Anton Simeonov
  - Larry A. Sklar
  - Noel Southall
  - Oleg Ursu
  - Dusica Vidovic
  - Anna Waller
  - Jeremy Yang
  - Ajit Jadhav
  - Tudor I. Oprea
  - Rajarshi Guha
  doi: 10.1093/nar/gkw1072
  id: doi:10.1093/nar/gkw1072
  journal: Nucleic Acids Research
  title: 'Pharos: Collating protein information to shed light on the druggable genome'
  year: '2017'
repository: https://github.com/unmtransinfo/TCRD
synonyms:
- TCRD
- Target Central Resource Database
- IDG TCRD
taxon:
- NCBITaxon:9606
---
# Target Central Resource Database

## Overview

The Target Central Resource Database (TCRD) is the central data repository for the NIH Common Fund's Illuminating the Druggable Genome (IDG) program. It integrates data from 80+ sources to provide comprehensive annotations for human protein targets, with emphasis on understudied proteins in GPCRs, ion channels, kinases, and nuclear receptors.

## Information Resource ID

This resource has the Information Resource identifier: `infores:tcrd`