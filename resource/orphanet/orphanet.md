---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.orpha.net/en/institutions/get-in-touch/
  label: Orphanet
creation_date: '2025-07-10T00:00:00Z'
description: Orphanet is a unique resource for information and data on rare diseases
  and orphan drugs, aimed at improving diagnosis, care, and treatment of patients
  with rare diseases. It maintains the Orphanet rare disease nomenclature (ORPHAcodes),
  which is essential for improving the visibility of rare diseases in health and research
  information systems.
domains:
- biomedical
- clinical
homepage_url: https://www.orpha.net/
id: orphanet
infores_id: orphanet
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Orphanet
products:
- category: GraphicalInterface
  description: Main Orphanet portal for rare disease and orphan drug information
  format: http
  id: orphanet.portal
  name: Orphanet Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://www.orpha.net/
- category: GraphicalInterface
  description: Orphadata Science portal for Orphanet scientific knowledge files, ORDO,
    HOOM, and Orphapackets downloads
  format: http
  id: orphanet.orphadata_science
  name: Orphadata Science Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://sciences.orphadata.com/
- category: Product
  description: Orphanet scientific knowledge files for rare disease alignments, classifications,
    genes, phenotypes, functional consequences, epidemiology, and natural history
  format: xml
  id: orphanet.scientific_knowledge_files
  name: Orphanet Scientific Knowledge Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://sciences.orphadata.com/orphanet-scientific-knowledge-files/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: hp
  - relation_type: prov:wasInformedBy
    source: mesh
  - relation_type: prov:wasInformedBy
    source: mondo
  - relation_type: prov:wasInformedBy
    source: omim
- category: DocumentationProduct
  description: Current Orphadata Science page for the Orphanet Rare Disease Ontology
    release, including ORDO 4.8 OWL downloads and release notes
  format: http
  id: orphanet.ordo_release
  name: ORDO Release Page
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: ordo
  product_url: https://sciences.orphadata.com/ordo/
- category: Product
  description: XML dataset containing information on expert centers dedicated to the
    medical management and/or genetic counselling for rare diseases.
  format: xml
  id: orphanet.expertcenters
  name: Expert Centers Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on expert center networks for rare
    diseases.
  format: xml
  id: orphanet.expertcentersnetworks
  name: Expert Centers Networks Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on diagnostic tests and clinical
    laboratories for rare diseases.
  format: xml
  id: orphanet.diagnostictests
  name: Diagnostic Tests and Laboratories Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on patient organizations dedicated
    to rare diseases.
  format: xml
  id: orphanet.patientorganizations
  name: Patient Organizations Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on patient organization networks
    for rare diseases.
  format: xml
  id: orphanet.patientorganizationsnetworks
  name: Patient Organizations Networks Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on national research projects focused
    on rare diseases.
  format: xml
  id: orphanet.researchprojects
  name: National Research Projects Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on multinational research project
    networks for rare diseases.
  format: xml
  id: orphanet.researchprojectsnetworks
  name: Multinational Research Projects Networks Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on national clinical trials for
    rare diseases.
  format: xml
  id: orphanet.clinicaltrials
  name: National Clinical Trials Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on multinational clinical trial
    networks for rare diseases.
  format: xml
  id: orphanet.clinicaltrialsnetworks
  name: Multinational Clinical Trials Networks Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on patient registries for rare diseases.
  format: xml
  id: orphanet.patientregistries
  name: Patient Registries Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on patient registry networks for
    rare diseases.
  format: xml
  id: orphanet.patientregistriesnetworks
  name: Patient Registries Networks Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on biobanks dedicated to rare diseases.
  format: xml
  id: orphanet.biobanks
  name: Biobanks Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on biobank networks for rare diseases.
  format: xml
  id: orphanet.biobanksnetworks
  name: Biobanks Networks Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://www.orphadata.com/expert-resources/
- category: Product
  description: XML dataset containing information on orphan drugs for rare diseases,
    including substances with orphan designation and/or marketing authorization.
  format: xml
  id: orphanet.orphandrugs
  name: Orphan Drugs Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://www.orphadata.com/expert-resources/
- category: ProgrammingInterface
  description: Contact point for API-mediated or request-mediated access to Orphanet
    scientific knowledge, ORPHAcodes, and expert resources data.
  format: http
  id: orphanet.orphadataapi
  is_public: true
  name: Orphadata API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://www.orphadata.com/contact/
  warnings:
  - The former Orphadata API landing-page URL returned 404 when checked on 2026-06-02;
    the registry points to the Orphadata contact page for access questions.
- category: GraphProduct
  description: DisGeNET data, including gene to disease associations and variant to
    disease associations (requires registration and subscription).
  format: http
  id: disgenet.data
  name: DisGeNET Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: mgd
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: psygenet
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: phewascat
  - relation_type: prov:hadPrimarySource
    source: ukbiobank
  - relation_type: prov:hadPrimarySource
    source: finngen
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  product_url: https://www.disgenet.com/
- category: Product
  description: Disease association data integrated from OMIM, MalaCards, ClinVar,
    Orphanet, DisGeNET and other disease databases
  format: http
  id: genecards.disease.associations
  name: GeneCards Disease Associations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
- category: Product
  description: History file tracking changes to Orphanet term mappings to CUIs
  format: txt
  id: medgen.ordo-history
  name: ORDO CUI History
  original_source:
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: orphanet
  product_file_size: 1130936
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/ORDO_CUI_history.txt
- category: GraphicalInterface
  description: Main Raras portal for searching rare diseases, symptoms, genes, and
    patient communities
  format: http
  id: raras.portal
  name: Raras Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: raras
  - relation_type: prov:wasInformedBy
    source: mondo
  - relation_type: prov:wasInformedBy
    source: omim
  - relation_type: prov:wasInformedBy
    source: orphanet
  - relation_type: prov:wasInformedBy
    source: icd10
  - relation_type: prov:wasInformedBy
    source: icd11
  - relation_type: prov:wasInformedBy
    source: wikidata
  - relation_type: prov:wasInformedBy
    source: clinvar
  product_url: https://raras.org/
- category: GraphicalInterface
  description: Rare disease encyclopedia for browsing disease families, disease records,
    and related knowledge graph content
  format: http
  id: raras.encyclopedia
  name: Raras Encyclopedia
  original_source:
  - relation_type: prov:hadPrimarySource
    source: raras
  - relation_type: prov:wasInformedBy
    source: mondo
  - relation_type: prov:wasInformedBy
    source: omim
  - relation_type: prov:wasInformedBy
    source: orphanet
  - relation_type: prov:wasInformedBy
    source: icd10
  - relation_type: prov:wasInformedBy
    source: icd11
  - relation_type: prov:wasInformedBy
    source: wikidata
  - relation_type: prov:wasInformedBy
    source: clinvar
  product_url: https://raras.org/explorar
- category: GraphProduct
  description: The OREGANO knowledge graph dataset integrating drug, protein, gene,
    and disease information for drug repositioning.
  format: http
  id: oregano.graph
  name: OREGANO Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: oregano
  product_url: https://gitub.u-bordeaux.fr/erias/oregano/-/tree/master/Data_OREGANO/Graphs
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: cmaup
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: npass
  - relation_type: prov:wasDerivedFrom
    source: orphanet
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: sider
  - relation_type: prov:wasDerivedFrom
    source: ttd
  - relation_type: prov:wasDerivedFrom
    source: umls
  - relation_type: prov:wasDerivedFrom
    source: uniprot
  - relation_type: prov:wasDerivedFrom
    source: bio2rdf
- category: GraphicalInterface
  description: Web-based interface for browsing and querying rare disease annotations
    including phenotypes, symptoms, genes, and genotypes with tree-structured disease
    organization
  format: http
  id: eram.web
  name: eRAM Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eram
  product_url: http://119.3.41.228/eram/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: omim
  - relation_type: prov:wasInformedBy
    source: umls
  - relation_type: prov:wasInformedBy
    source: doid
  - relation_type: prov:wasInformedBy
    source: mesh
  - relation_type: prov:wasInformedBy
    source: orphanet
  - relation_type: prov:wasInformedBy
    source: hp
  - relation_type: prov:wasInformedBy
    source: mp
- category: Product
  description: Downloadable data files containing rare disease annotations, phenotypes,
    symptoms, genes, and genotypes
  format: mixed
  id: eram.downloads
  name: eRAM Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: eram
  product_url: http://119.3.41.228/eram/download.php
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: umls
  - relation_type: prov:wasDerivedFrom
    source: doid
  - relation_type: prov:wasDerivedFrom
    source: mesh
  - relation_type: prov:wasDerivedFrom
    source: orphanet
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: mp
- category: ProgrammingInterface
  description: REST API for searching identifiers and special keywords, mapping between
    data sources with a chain-query syntax, and retrieving entries across the integrated
    BioBTree databases.
  format: http
  id: biobtree.api
  is_public: true
  name: BioBTree REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biobtree
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: alphamissense
  - relation_type: prov:hadPrimarySource
    source: bao
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: brenda
  - relation_type: prov:hadPrimarySource
    source: cellphonedb
  - relation_type: prov:hadPrimarySource
    source: cellxgene
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: collectri
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: expressionatlas
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: gencc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: jaspar
  - relation_type: prov:hadPrimarySource
    source: lipidmaps
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mirdb
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: surechembl
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://sugi.bio/biobtree/api/
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
  - Pavan S
  - Rommel K
  - Mateo Marquina ME
  - Höhn S
  - Lanneau V
  - Rath A
  doi: 10.1371/journal.pone.0170365
  id: https://www.ncbi.nlm.nih.gov/pubmed/28099516
  journal: PLoS One
  preferred: true
  title: 'Clinical Practice Guidelines for Rare Diseases: The Orphanet Database'
  year: '2017'
repository: https://github.com/Orphanet
taxon:
- NCBITaxon:9606
version: December 2025
---
# Orphanet

Orphanet is a unique resource gathering and improving knowledge on rare diseases to enhance diagnosis, care, and treatment of patients with rare diseases. It aims to provide high-quality information on rare diseases and ensure equal access to knowledge for all stakeholders.

## Overview

Established in France by INSERM (French National Institute for Health and Medical Research) in 1997, Orphanet has evolved into a European endeavor, gradually growing to a Consortium of 40 countries worldwide. The Orphanet database contains information on:

- 6,528+ rare diseases
- 4,512+ genes
- 8,722+ expert centers
- 36,595+ diagnostic tests
- 30,456+ professionals
These counts are historical context from earlier Orphanet summaries and may differ
from the current public portal.

## Key Resources

### Orphanet Rare Disease Ontology (ORDO)

ORDO is a structured vocabulary for rare diseases derived from the Orphanet database. It captures relationships between diseases, genes, and other relevant features, providing integrated, re-usable data for computational analysis. The ontology is maintained by Orphanet and follows OBO guidelines.

### ORPHAcodes - Orphanet Nomenclature

The Orphanet nomenclature is a multilingual, standardized, controlled medical terminology specific to rare diseases. Each clinical entity is associated with a unique numerical identifier (ORPHAcode), preferred term, synonyms, and definition. The nomenclature pack includes files for implementing ORPHAcodes in health information systems.

### Orphanet Scientific Knowledge Base

This comprehensive collection of datasets provides structured information about rare diseases, including:
- Disease alignments with other terminologies (ICD-10, ICD-11, OMIM, UMLS, MONDO, MeSH, MedDRA, GARD)
- Classifications of rare diseases
- Gene associations
- Clinical signs and symptoms
- Functional consequences
- Epidemiological data
- Natural history information

## Recognition

Orphadata Science (which includes ORDO and the scientific knowledge files) has been recognized as:
- An ELIXIR Core Data Resource
- A Global Core Biodata Resource
- An IRDiRC Recognized Resource

## Data Access

All Orphanet data resources are available under the Creative Commons Attribution 4.0 International (CC BY 4.0) license, making them freely accessible for research and implementation. Data are updated bi-annually in July and December; the current Orphadata Science pages checked during this curation listed December 2025 releases for the scientific knowledge files and ORDO 4.8.