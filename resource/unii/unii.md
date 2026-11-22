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
last_modified_date: '2026-11-22T00:00:00Z'
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
  description: Zipped tab-delimited list of all names associated with each UNII (name,
    name type such as official, systematic, common, code or brand name, UNII and preferred
    display name), with a README describing the fields
  format: tsv
  id: unii.list
  name: UNII List Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unii
  product_file_size: 20344194
  product_url: https://precision.fda.gov/uniisearch/archive/latest/UNIIs.zip
- category: MappingProduct
  compression: zip
  description: Zipped tab-delimited UNII records file with one row per UNII, giving
    the display name, molecular formula, InChIKey, SMILES, ingredient type and ISO
    11238 substance type, plus cross-references to CAS registry numbers, EC numbers,
    NCI Thesaurus, RxNorm, PubChem, EMA SMS IDs, EPA CompTox (DSSTox), Catalogue of
    Life, ITIS, NCBI Taxonomy, USDA PLANTS, Plants of the World Online, GRIN, the Kew
    Medicinal Plant Names Services, INN and USAN codes, and DailyMed. Also includes
    the Legacy UNIIs file.
  format: tsv
  id: unii.data
  name: UNII Data Download
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unii
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: rxnorm
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: dsstoxdb
  - relation_type: prov:hadPrimarySource
    source: catalogue-of-life
  - relation_type: prov:hadPrimarySource
    source: itis
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: dailymed
  product_file_size: 14477857
  product_url: https://precision.fda.gov/uniisearch/archive/latest/UNII_Data.zip
- category: MappingProduct
  description: Tab-delimited mapping of retired (legacy) UNIIs to their current replacement
    UNII and preferred term
  format: tsv
  id: unii.legacy
  name: Legacy UNIIs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unii
  product_file_size: 7922
  product_url: https://precision.fda.gov/uniisearch/archive/latest/Legacy_UNIIs.txt
- category: GraphicalInterface
  description: Public Global Substance Registration System hosted by NCATS, for searching
    and browsing full GSRS substance records (chemicals, proteins, nucleic acids, polymers,
    structurally diverse substances and mixtures) with their names, codes, relationships
    and references
  format: http
  id: unii.gsrs
  name: NCATS Public GSRS
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://gsrs.ncats.nih.gov/ginas/app/ui/
- category: ProgrammingInterface
  description: REST API of the public NCATS GSRS, returning GSRS substance records
    as JSON (for example /api/v1/substances)
  format: http
  id: unii.gsrs.api
  name: NCATS Public GSRS REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://gsrs.ncats.nih.gov/api/v1/substances
- category: ProcessProduct
  description: Source repository for deploying the GSRS 3 software, a set of Java Spring
    Boot microservices and an Angular frontend developed by NCATS and FDA
  format: java
  id: unii.gsrs.software
  name: GSRS 3 Deployment Repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: unii
  product_url: https://github.com/ncats/gsrs3-main-deployment
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
  - relation_type: prov:hadPrimarySource
    source: fda-orphan-drugs
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
- authors:
  - Tyler Peryea
  - Noel Southall
  - Mitch Miller
  - Daniel Katzel
  - Niko Anderson
  - Jorge Neyra
  - Sarah Stemann
  - Ðắc-Trung Nguyễn
  - Dammika Amugoda
  - Archana Newatia
  - Ramez Ghazzaoui
  - Elaine Johanson
  - Herman Diederik
  - Larry Callahan
  - Frank Switzer
  doi: 10.1093/nar/gkaa962
  id: doi:10.1093/nar/gkaa962
  journal: Nucleic Acids Research
  preferred: true
  title: 'Global Substance Registration System: consistent scientific descriptions
    for substances related to health'
  year: '2021'
- id: https://www.fda.gov/science-research/fda-grand-rounds/fdas-global-substance-registration-system-gsrs-unique-ingredient-identifiers-uniis-uniquely-define
  title: FDA’s Global Substance Registration System (GSRS) Unique Ingredient Identifiers
    (UNIIs) uniquely define substances in FDA-regulated products - 06/08/2023 | FDA
repository: https://github.com/ncats/gsrs3-main-deployment
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

The system is regularly updated; the downloadable UNII files current as of November 2026 are the August 4, 2026 release. UNIIs are generated based on the best available public information, and synonyms and mappings are continuously refined. The FDA encourages reporting of data issues to maintain accuracy and completeness.