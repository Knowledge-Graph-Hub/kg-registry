---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: FDA-SRS@fda.hhs.gov
  id: fda
  label: FDA Substance Registration System Team
creation_date: '2025-07-17T00:00:00Z'
description: FDA's Global Substance Registration System (GSRS) is a comprehensive
  database that provides Unique Ingredient Identifiers (UNIIs) for substances in FDA-regulated
  products. UNIIs uniquely define substances based on scientific identity characteristics
  using ISO 11238 data elements, enabling efficient and accurate exchange of substance
  information across regulatory domains.
domains:
- clinical
- drug discovery
- pharmacology
- public health
homepage_url: https://precision.fda.gov/uniisearch
id: unii
infores_id: unii
last_modified_date: '2026-06-12T00:00:00Z'
layout: resource_detail
name: FDA Global Substance Registration System (UNII)
products:
- category: GraphicalInterface
  description: Web-based search interface for finding substances by UNII, name, or
    other identifiers
  format: http
  id: unii.search
  name: UNII Search Service
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://precision.fda.gov/uniisearch
- category: Product
  compression: zip
  description: Downloadable list of all UNIIs with basic substance information
  format: csv
  id: unii.list
  name: UNII List Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://precision.fda.gov/uniisearch/archive/latest/UNIIs.zip
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
- category: Product
  compression: zip
  description: Comprehensive UNII data with detailed substance attributes and mappings
  format: mixed
  id: unii.data
  name: UNII Data Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://precision.fda.gov/uniisearch/archive/latest/UNII_Data.zip
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
- category: Product
  description: Legacy UNII identifiers for historical substances
  format: txt
  id: unii.legacy
  name: Legacy UNIIs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://precision.fda.gov/uniisearch/archive/latest/Legacy_UNIIs.txt
  warnings:
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 403 error when
    accessing file
- description: The MechRepoNet knowledge graph in its original format
  format: mixed
  id: mechreponet.kg
  name: MechRepoNet Knowledge Graph
  original_source:
  - relation_type: prov:hadPrimarySource
    source: biolink
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: complexportal
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hetionet
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: mechreponet
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://github.com/SuLab/MechRepoNet/releases/tag/publication
- category: Product
  description: Downloadable SPL files for all drug labels in the DailyMed database,
    updated daily
  format: xml
  id: dailymed.spl_files
  name: DailyMed SPL Data Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dailymed
  product_url: https://dailymed.nlm.nih.gov/dailymed/spl-resources-all-drug-labels.cfm
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: rxnorm
  - relation_type: prov:wasInformedBy
    source: unii
  - relation_type: prov:wasInformedBy
    source: ndcd
- category: ProgrammingInterface
  connection_url: https://api.fda.gov/
  description: JSON REST APIs (Elasticsearch query syntax) for FDA drug, device, food,
    animal and veterinary, cosmetic, tobacco and other datasets, including drug adverse
    events (FAERS), device adverse events (MAUDE), the National Drug Code directory,
    the Orange Book, UNII substance data, labeling, recalls and enforcement reports.
  format: http
  id: openfda.apis
  is_public: true
  name: openFDA APIs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: openfda
  - relation_type: prov:hadPrimarySource
    source: faers
  - relation_type: prov:hadPrimarySource
    source: maude
  - relation_type: prov:hadPrimarySource
    source: ndcd
  - relation_type: prov:hadPrimarySource
    source: fda-orange-book
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://open.fda.gov/apis/
- category: Product
  compression: zip
  description: Bulk downloads of every openFDA endpoint as zipped JSON files, split
    into partitions for large datasets such as drug adverse events (FAERS) and device
    adverse events (MAUDE), with a machine-readable manifest at https://api.fda.gov/download.json
    listing each endpoint's export date and file partitions.
  format: json
  id: openfda.downloads
  name: openFDA Bulk Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: openfda
  - relation_type: prov:hadPrimarySource
    source: faers
  - relation_type: prov:hadPrimarySource
    source: maude
  - relation_type: prov:hadPrimarySource
    source: ndcd
  - relation_type: prov:hadPrimarySource
    source: fda-orange-book
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://open.fda.gov/data/downloads/
- category: ProgrammingInterface
  description: MyChem.info REST API (v1) for querying chemical and drug annotation
    records by keyword, field or identifier (InChIKey, ChEMBL, DrugBank, PubChem,
    ChEBI and UNII IDs), with batch queries over POST. Data in each record keep the
    license of their original source.
  format: json
  id: mychem.api
  infores_id: mychem-info
  name: MyChem.info API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mychem
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: unii
  - relation_type: prov:hadPrimarySource
    source: ndcd
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: unichem
  - relation_type: prov:hadPrimarySource
    source: aeolus
  - relation_type: prov:hadPrimarySource
    source: sider
  product_url: https://mychem.info/v1/query
- category: ProgrammingInterface
  description: MyGene.info REST API (v3) for gene query and annotation retrieval by
    Entrez or Ensembl gene id, with batch POST queries and field filtering. Returns
    JSON documents merged from the integrated sources.
  format: http
  id: mygene.api
  infores_id: mygene-info
  name: MyGene.info API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mygene
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pir
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: cpdb
  - relation_type: prov:hadPrimarySource
    source: pharos
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: unii
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: cellmarker
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  product_url: https://mygene.info/v3/api
- category: Product
  description: Babel compendia, one file per Biolink type (for example Gene, Protein, Disease,
    ChemicalEntity, SmallMolecule, AnatomicalEntity). Each line is a JSON object for one clique,
    listing its identifiers with labels, descriptions and taxa, plus the preferred name and
    information content. Files carry a .txt extension; the Gene and Protein files (about 17.8
    GB and 46.7 GB) are also split into parts.
  format: json
  id: babel.compendia
  latest_version: 2026jul22
  name: Babel Compendia
  original_source:
  - relation_type: prov:hadPrimarySource
    source: babel
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: unii
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: fma
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: meddra
  - relation_type: prov:hadPrimarySource
    source: wormbase
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: clo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: smpdb
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: complexportal
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: emapa
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: cl
  product_url: https://stars.renci.org/var/babel_outputs/latest/compendia/
publications:
- id: https://www.fda.gov/science-research/fda-grand-rounds/fdas-global-substance-registration-system-gsrs-unique-ingredient-identifiers-uniis-uniquely-define
  title: FDA’s Global Substance Registration System (GSRS) Unique Ingredient Identifiers
    (UNIIs) uniquely define substances in FDA-regulated products - 06/08/2023 | FDA
repository: https://ginas.ncats.nih.gov/ginas/app
taxon:
- NCBITaxon:9606
---
# FDA Global Substance Registration System (UNII)

The FDA's Global Substance Registration System (GSRS) is a comprehensive, authoritative database that generates Unique Ingredient Identifiers (UNIIs) for substances in FDA-regulated products. Developed through collaboration between the FDA's Informatics team, NIH's National Center for Advancing Translational Sciences (NCATS), and the European Medicines Agency (EMA), GSRS addresses the critical need for accurate substance identification across global regulatory domains.

## Overview

UNIIs are generated based on scientific identity characteristics using ISO 11238 data elements, providing standardized identifiers that transcend the variability of substance names across different regulatory domains, countries, and regions. The system classifies substances as chemical, protein, nucleic acid, polymer, structurally diverse, or mixture as detailed in ISO 11238 and ISO DTS 19844 standards.

## Key Features

- **Comprehensive Coverage**: UNIIs can be generated for any substance at any time in the regulatory life cycle, from atoms to organisms
- **Global Standardization**: Enables efficient and accurate exchange of substance information across regulatory domains
- **Scientific Classification**: Substances are defined by standardized, scientific descriptions rather than variable names
- **Regulatory Integration**: Used in electronic listing systems like DailyMed and throughout product life cycles including clinical trials, marketing, and post-market surveillance

## Products and Access

The GSRS provides multiple ways to access UNII data:

1. **UNII Search Service**: Interactive web interface for searching substances by UNII, name, or other identifiers
2. **Downloadable Data**: Comprehensive datasets including UNII lists and detailed substance data
3. **Public GSRS Interface**: Full access to the Global Substance Registration System hosted by NCATS
4. **PrecisionFDA Integration**: Collaborative tools for filtering, exporting, and creating GSRS records

## Applications

UNII identifiers are essential for:
- Drug labeling and electronic submissions
- Clinical trial identification
- Product safety monitoring
- Global supply chain tracking
- Regulatory compliance across FDA-regulated products (food, drugs, tobacco, cosmetics)

## Data Quality and Updates

The system is regularly updated, with the most recent data refresh on August 18, 2025. UNIIs are generated based on the best available public information, and synonyms and mappings are continuously refined. The FDA encourages reporting of data issues to maintain accuracy and completeness.