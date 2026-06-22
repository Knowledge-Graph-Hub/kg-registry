---
activity_status: inactive
category: DataSource
creation_date: '2025-12-03T00:00:00Z'
description: PharmacotherapyDB is a curated catalog of medical indications between
  small molecule compounds and complex human diseases. It was created as part of a
  network-based drug repurposing project and differentiates between disease-modifying
  (DM) and symptomatic (SYM) treatments, with each indication reviewed by multiple
  physicians. The initial release contains 97 diseases and 601 drugs, with 755 disease-modifying
  therapies, 390 symptomatic therapies, and 243 non-indications. The catalog uses
  standardized vocabularies (Disease Ontology and DrugBank) to facilitate data integration
  and adheres to pathophysiological principles.
domains:
- drug discovery
- pharmacology
- biomedical
homepage_url: https://github.com/dhimmel/indications
id: pharmacotherapydb
infores_id: pharmacotherapydb
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0-1.0
name: PharmacotherapyDB
products:
- category: Product
  description: Figshare archive for PharmacotherapyDB 1.0, the open catalog of drug
    therapies for disease
  format: http
  id: pharmacotherapydb.figshare
  name: PharmacotherapyDB 1.0 Figshare Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  product_url: https://doi.org/10.6084/m9.figshare.3103054
  warnings: []
- category: Product
  description: Curated TSV catalog of drug-disease indications classified as disease-modifying,
    symptomatic, or non-indications
  format: tsv
  id: pharmacotherapydb.indications
  name: PharmacotherapyDB Indications TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  product_file_size: 76754
  product_url: https://raw.githubusercontent.com/dhimmel/indications/gh-pages/catalog/indications.tsv
  secondary_source:
  - relation_type: prov:used
    source: doid
  - relation_type: prov:used
    source: drugbank
  - relation_type: prov:wasInformedBy
    source: labeledin
  - relation_type: prov:wasInformedBy
    source: medi
  - relation_type: prov:wasInformedBy
    source: ehrlink
  - relation_type: prov:wasInformedBy
    source: predict
- category: Product
  description: Excel workbook for the PharmacotherapyDB catalog release
  format: http
  id: pharmacotherapydb.catalog_xlsx
  name: PharmacotherapyDB Catalog Workbook
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  product_file_size: 115234
  product_url: https://raw.githubusercontent.com/dhimmel/indications/gh-pages/catalog/catalog.xlsx
- category: Product
  description: Disease table for the PharmacotherapyDB catalog using Disease Ontology
    identifiers
  format: tsv
  id: pharmacotherapydb.diseases
  name: PharmacotherapyDB Diseases TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  product_file_size: 1665
  product_url: https://raw.githubusercontent.com/dhimmel/indications/gh-pages/catalog/diseases.tsv
  secondary_source:
  - relation_type: prov:used
    source: doid
- category: Product
  description: Drug table for the PharmacotherapyDB catalog using DrugBank identifiers
  format: tsv
  id: pharmacotherapydb.drugs
  name: PharmacotherapyDB Drugs TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  product_file_size: 6142
  product_url: https://raw.githubusercontent.com/dhimmel/indications/gh-pages/catalog/drugs.tsv
  secondary_source:
  - relation_type: prov:used
    source: drugbank
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alzkb
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dsstox
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  format: mixed
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: alzkb
  - relation_type: prov:hadPrimarySource
    source: aop-db
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: dsstox
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: lincs-l1000
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: pharmacotherapydb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: hetionet
- category: Product
  description: PharmacotherapyDB processing workspace for EHRLink medication-problem
    association data, including notebooks for converting, mapping, and preparing EHRLink-derived
    indications.
  id: ehrlink.pharmacotherapydb-processing
  name: EHRLink PharmacotherapyDB Processing Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ehrlink
  product_url: https://github.com/dhimmel/indications/tree/gh-pages/ehrlink
  repository: https://github.com/dhimmel/indications
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: pharmacotherapydb
publications:
- authors:
  - Himmelstein DS
  - Lizee A
  - Hessler C
  - Brueggeman L
  - Chen SL
  - Hadley D
  - Green A
  - Khankhanian P
  - Baranzini SE
  doi: 10.7554/eLife.26726
  id: doi:10.7554/eLife.26726
  journal: eLife
  preferred: true
  title: Systematic integration of biomedical knowledge prioritizes drugs for repurposing
  year: '2017'
taxon:
- NCBITaxon:9606
warnings:
- The repository README states original PharmacotherapyDB content is CC0, but also
  notes upstream license constraints for integrated sources including DrugBank, MEDI,
  PREDICT, and EHRLink.
---
# PharmacotherapyDB

PharmacotherapyDB is a curated catalog of medical indications between small molecule compounds and complex human diseases. Created as part of a network-based drug repurposing project, it differentiates between disease-modifying (DM) and symptomatic (SYM) treatments, with each indication reviewed by multiple physicians. The initial release contains 97 diseases, 601 drugs, 755 disease-modifying therapies, 390 symptomatic therapies, and 243 non-indications. The catalog uses standardized vocabularies (Disease Ontology and DrugBank) to facilitate data integration and is designed as a gold standard for computational drug repurposing approaches.