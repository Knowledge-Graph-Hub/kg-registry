---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://lincs.hms.harvard.edu/
  label: HMS LINCS Project
creation_date: '2025-10-30T00:00:00Z'
description: KINOMEscan is a biochemical kinase profiling assay that measures drug
  binding using a panel of approximately 440 purified kinases. The HMS LINCS Project
  provides a comprehensive table of all small molecules in the HMS LINCS collection
  that have been profiled by KINOMEscan, with links to raw binding data.
domains:
- drug discovery
- pharmacology
- biomedical
- high-throughput screening
homepage_url: https://lincs.hms.harvard.edu/kinomescan/
id: kinomescan
infores_id: kinomescan
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
name: KINOMEscan
products:
- category: GraphicalInterface
  description: Web interface providing searchable table of all small molecules profiled
    by KINOMEscan
  format: http
  id: kinomescan.portal
  name: KINOMEscan Data Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  product_url: https://lincs.hms.harvard.edu/kinomescan/
- category: DocumentationProduct
  description: Excel spreadsheet containing HMS LINCS KINOMEscan datasets with compound
    information and data links
  format: xlsx
  id: kinomescan.spreadsheet
  name: KINOMEscan Datasets Spreadsheet
  original_source:
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  product_file_size: 17872
  product_url: http://lincs.hms.harvard.edu/wordpress/wp-content/uploads/2013/11/HMS-LINCS_KinomeScan_Datasets_2018-01-18.xlsx
- category: GraphProduct
  description: KGX nodes for Molecular Data KP
  format: kgx
  id: molepro.graph.nodes
  name: Nodes for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molepro
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
    source: repohub
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
  id: molepro.graph.edges
  name: Edges for Molecular Data KP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molepro
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
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  product_file_size: 20140191116
  product_url: https://molepro.s3.amazonaws.com/edges.tsv
- category: ProgrammingInterface
  description: MolePro API providing access to the knowledge graph of chemical entities
    and biological targets
  format: http
  id: molepro.api
  name: MolePro API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molepro
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: genetics-kp
  product_url: https://molepro.transltr.io/molecular_data_provider/api
- category: ProgrammingInterface
  description: TRAPI-compliant interface for MolePro knowledge graph following the
    Translator Reasoner API standard
  format: http
  id: molepro.trapi
  name: MolePro TRAPI Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molepro
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: genetics-kp
  product_url: https://molepro-trapi.transltr.io/molepro/trapi/v1.5/ui/
- category: Product
  description: Catalog of MolePro knowledge sources in JSON format
  format: json
  id: molepro.catalog
  name: MolePro Knowledge Sources Catalog
  original_source:
  - relation_type: prov:hadPrimarySource
    source: molepro
  - relation_type: prov:hadPrimarySource
    source: bigg
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembank
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: cmap
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: ctrp
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: gelinea
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: inxight-drugs
  - relation_type: prov:hadPrimarySource
    source: kinomescan
  - relation_type: prov:hadPrimarySource
    source: msigdb
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: probe-miner
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: genetics-kp
  product_file_size: 2127877
  product_url: https://translator.broadinstitute.org/molecular_data_provider/transformers
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
synonyms:
- HMS LINCS KINOMEscan
---
# KINOMEscan

## Overview

KINOMEscan is a biochemical kinase profiling assay technology that measures drug binding using a panel of approximately 440 purified kinases. The data resource is maintained by the HMS LINCS (Harvard Medical School Library of Integrated Network-based Cellular Signatures) Project. The assay provides comprehensive profiling of small molecule compounds against a large kinase panel, enabling drug discovery and selectivity profiling studies.

## Data Content

The HMS LINCS KINOMEscan data collection includes:

- **Compound Coverage**: Small molecules from the HMS LINCS collection that have been profiled by KINOMEscan
- **Kinase Panel**: Approximately 440 purified kinases representing a broad coverage of the human kinome
- **Binding Data**: Raw binding data for each compound-kinase interaction
- **Compound Information**: HMSL identifiers, LSM numbers, common names, and synonyms for each profiled compound

The data includes kinase inhibitors, multi-kinase inhibitors, and other bioactive small molecules commonly used in drug discovery and chemical biology research.

## Key Features

- **Comprehensive Kinase Coverage**: ~440 kinases representing diverse families
- **Biochemical Assay**: Direct measurement of compound binding to purified kinases
- **Searchable Data**: Web interface with compound names and identifiers
- **Downloadable Datasets**: Excel spreadsheet format for offline analysis
- **HMS LINCS Integration**: Part of the broader HMS LINCS data ecosystem

## Access Methods

1. **Web Interface**: Browse and search KINOMEscan data through the HMS LINCS portal
2. **Spreadsheet Download**: Excel file containing complete dataset information and links (last updated January 18, 2018)

## Data Format

- **Online**: HTML table with compound information and data links
- **Downloadable**: Microsoft Excel (.xlsx) format

## Use Cases

- **Drug Discovery**: Kinase inhibitor profiling and selectivity assessment
- **Target Validation**: Understanding kinase inhibitor specificity
- **Polypharmacology Studies**: Identifying off-target kinase interactions
- **Structure-Activity Relationships**: Correlating compound structure with kinase binding profiles
- **Chemical Biology**: Tool compound characterization

## Management

The KINOMEscan data resource is managed and curated by the HMS LINCS Project at Harvard Medical School.

## Related Resources

- HMS LINCS Database: https://lincs.hms.harvard.edu/db/
- HMS LINCS Data Exploration Tools: https://lincs.hms.harvard.edu/explore/
- HMS LINCS Publications: https://lincs.hms.harvard.edu/about/publications/

## Last Update

The downloadable spreadsheet was last updated on January 18, 2018.