---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: depmap@broadinstitute.org
  - contact_type: url
    value: https://depmap.org/portal/
  id: broad
  label: DepMap Team, Broad Institute
creation_date: '2025-10-09T00:00:00Z'
description: The Cancer Dependency Map (DepMap) is a genome-wide pooled CRISPR-Cas9
  knockout and small molecule screen of cancer cell lines. The goal of DepMap is to
  systematically identify cancer dependencies and the biomarkers that predict them.
  DepMap provides open access to key cancer dependencies, analytical tools, and visualization
  resources for the research community.
domains:
- biomedical
- genomics
- health
- drug discovery
- precision medicine
homepage_url: https://depmap.org/portal/
id: depmap
infores_id: depmap
last_modified_date: '2026-06-01T00:00:00Z'
layout: resource_detail
license:
  id: https://depmap.org/portal/terms/
  label: DepMap Terms of Use
name: DepMap
products:
- category: GraphicalInterface
  description: Web portal for exploring cancer dependencies, cell line data, and biomarkers
  format: http
  id: depmap.portal
  name: DepMap Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_url: https://depmap.org/portal/
- category: ProgrammingInterface
  connection_url: https://depmap.org/portal/api/
  description: DepMap portal API for programmatic access to portal data and metadata
  format: json
  id: depmap.api
  name: DepMap API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_url: https://depmap.org/portal/api/
- category: GraphicalInterface
  description: Interactive tool for exploring relationships across DepMap datasets
    and cell lines
  format: http
  id: depmap.data_explorer
  name: DepMap Data Explorer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_url: https://depmap.org/portal/interactive/
- category: GraphicalInterface
  description: Tool for exploring and selecting cancer cell lines based on various
    criteria
  format: http
  id: depmap.cell_line_selector
  name: DepMap Cell Line Selector
  original_source:
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_url: https://depmap.org/portal/cell_line_selector/
- category: GraphicalInterface
  description: Context Explorer tool for exploring enriched genetic dependencies and
    compound sensitivities across lineage and subtype contexts
  format: http
  id: depmap.context_explorer
  name: DepMap Context Explorer
  original_source:
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_url: https://depmap.org/portal/context/
- category: GraphicalInterface
  description: Target Discovery App for identifying selective and predictable gene
    dependencies
  format: http
  id: depmap.target_discovery
  name: DepMap Target Discovery
  original_source:
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_url: https://depmap.org/portal/tda/
- category: Product
  description: Complete collection of DepMap datasets available for download including
    CRISPR screens, drug screens, and omics data
  format: mixed
  id: depmap.downloads
  latest_version: DepMap Public 26Q1
  name: DepMap Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_url: https://depmap.org/portal/data_page/?tab=currentRelease
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-03: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-05: HTTP 403 error
    when accessing file'
- category: Product
  description: CRISPR-Cas9 knockout screening data processed with Chronos algorithm
    to identify gene dependencies
  format: csv
  id: depmap.crispr_gene_effects
  name: DepMap CRISPR Gene Effects (Chronos)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_url: https://depmap.org/portal/data_page/
- category: Product
  description: Drug screening data from various platforms including GDSC, PRISM, and
    CTD2
  format: csv
  id: depmap.drug_sensitivity
  name: DepMap Drug Sensitivity Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_url: https://depmap.org/portal/data_page/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: prism
  - relation_type: prov:wasDerivedFrom
    source: ctd2
- category: Product
  description: Gene expression data (RNA-seq) for DepMap cell lines
  format: csv
  id: depmap.expression_data
  name: DepMap Expression Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_url: https://depmap.org/portal/data_page/
- category: Product
  description: Copy number variation data for DepMap cell lines
  format: csv
  id: depmap.copy_number
  name: DepMap Copy Number Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_url: https://depmap.org/portal/data_page/
- category: Product
  description: Mutation data for DepMap cell lines
  format: csv
  id: depmap.mutations
  name: DepMap Mutation Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_url: https://depmap.org/portal/data_page/
- category: Product
  description: Proteomics data for DepMap cell lines
  format: csv
  id: depmap.proteomics
  name: DepMap Proteomics Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_url: https://depmap.org/portal/data_page/
- category: Product
  description: Metabolomics data for DepMap cell lines
  format: csv
  id: depmap.metabolomics
  name: DepMap Metabolomics Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_url: https://depmap.org/portal/data_page/
- category: Product
  description: Comprehensive metadata and annotations for all DepMap cell lines
  format: csv
  id: depmap.cell_line_info
  name: DepMap Cell Line Information
  original_source:
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_url: https://depmap.org/portal/data_page/
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
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
- category: Product
  description: depmap Nodes TSV
  format: tsv
  id: obo-db-ingest.depmap.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: depmap Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 18757
  product_url: https://w3id.org/biopragmatics/resources/depmap/depmap.tsv
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
- category: Product
  description: DepMap all-data downloads page where current Achilles and related dependency
    datasets are released.
  format: http
  id: achilles.downloads
  name: Project Achilles Data Releases
  original_source:
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: depmap
  product_url: https://depmap.org/portal/download/all/
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-03: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-05: HTTP 403 error
    when accessing file'
- category: Product
  description: DepMap downloads page for PRISM Repurposing primary and secondary screen
    data
  format: csv
  id: prism.datasets
  name: PRISM Drug Sensitivity Dataset Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prism
  product_url: https://depmap.org/portal/data_page/?tab=allData
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: depmap
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-03: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-05: HTTP 403 error
    when accessing file'
- category: Product
  description: Replicate-collapsed log-fold-change matrix from the primary PRISM Repurposing
    screen of pooled-cell line chemical-perturbation viability measurements
  format: csv
  id: prism.primary_screen_lfc
  name: PRISM Repurposing Primary Screen Log-Fold Change
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prism
  product_url: https://ndownloader.figshare.com/files/20237709
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: depmap
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-03: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-05: HTTP 403 error
    when accessing file'
- category: Product
  description: Dose-response curve parameter matrix from the secondary PRISM Repurposing
    screen of 1,448 compounds across cancer cell lines
  format: csv
  id: prism.secondary_screen_dose_response
  name: PRISM Repurposing Secondary Screen Dose Response
  original_source:
  - relation_type: prov:hadPrimarySource
    source: prism
  product_url: https://ndownloader.figshare.com/files/20237739
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: depmap
  warnings:
  - 'File was not able to be retrieved when checked on 2026-06-03: HTTP 403 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2026-06-05: HTTP 403 error
    when accessing file'
- category: Product
  description: Harmonizome 3.0 processed dataset downloads, including dataset-specific
    association files and knowledge graph serialization downloads.
  format: mixed
  id: harmonizome.downloads
  name: Harmonizome Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://maayanlab.cloud/Harmonizome/download
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
- category: GraphProduct
  description: Neo4j knowledge graph serialization of Harmonizome processed datasets,
    including genes, attributes, resources, datasets, and gene-attribute associations.
  dump_format: neo4j
  format: neo4j
  id: harmonizome.kg-neo4j
  latest_version: '3.0'
  name: Harmonizome Knowledge Graph Neo4j Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: harmonizome
  product_url: https://harmonizome-kg.maayanlab.cloud/
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: achilles
  - relation_type: prov:wasDerivedFrom
    source: biogps
  - relation_type: prov:wasDerivedFrom
    source: ccle
  - relation_type: prov:wasDerivedFrom
    source: cellmarker
  - relation_type: prov:wasDerivedFrom
    source: chea
  - relation_type: prov:wasDerivedFrom
    source: clinvar
  - relation_type: prov:wasDerivedFrom
    source: cmap
  - relation_type: prov:wasDerivedFrom
    source: compartments
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: cosmic
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: depmap
  - relation_type: prov:wasDerivedFrom
    source: diseases
  - relation_type: prov:wasDerivedFrom
    source: disgenet
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: encode
  - relation_type: prov:wasDerivedFrom
    source: gdsc
  - relation_type: prov:wasDerivedFrom
    source: geo
  - relation_type: prov:wasDerivedFrom
    source: glygen
  - relation_type: prov:wasDerivedFrom
    source: go
  - relation_type: prov:wasDerivedFrom
    source: gtex
  - relation_type: prov:wasDerivedFrom
    source: gwascatalog
  - relation_type: prov:wasDerivedFrom
    source: hmdb
  - relation_type: prov:wasDerivedFrom
    source: hp
  - relation_type: prov:wasDerivedFrom
    source: hpa
  - relation_type: prov:wasDerivedFrom
    source: hubmap
  - relation_type: prov:wasDerivedFrom
    source: impc
  - relation_type: prov:wasDerivedFrom
    source: interpro
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: lincs-l1000
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: motrpac
  - relation_type: prov:wasDerivedFrom
    source: mp
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: omim
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathwaycommons
  - relation_type: prov:wasDerivedFrom
    source: pfocr
  - relation_type: prov:wasDerivedFrom
    source: phosphositeplus
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: tcga
  - relation_type: prov:wasDerivedFrom
    source: tissues
  - relation_type: prov:wasDerivedFrom
    source: wikipathways
publications:
- authors:
  - Meyers RM
  - Bryan JG
  - McFarland JM
  - Weir BA
  - Sizemore AE
  - Xu H
  doi: 10.1038/ng.3984
  id: doi:10.1038/ng.3984
  journal: Nature Genetics
  title: Computational correction of copy number effect improves specificity of CRISPR-Cas9
    essentiality screens in cancer cells
  year: '2017'
- authors:
  - Tsherniak A
  - Vazquez F
  - Montgomery PG
  - Weir BA
  - Kryukov G
  - Cowley GS
  doi: 10.1016/j.cell.2017.06.010
  id: doi:10.1016/j.cell.2017.06.010
  journal: Cell
  title: Defining a Cancer Dependency Map
  year: '2017'
repository: https://github.com/broadinstitute/depmap_omics
taxon:
- NCBITaxon:9606
---
# DepMap

The Cancer Dependency Map (DepMap) is a comprehensive effort to systematically identify cancer dependencies and the biomarkers that predict them. As a collaborative initiative led by the Broad Institute, DepMap aims to accelerate the development of precision treatments for cancer by providing open access to key cancer dependency data, analytical tools, and visualization resources.

## About DepMap

DepMap uses genome-wide pooled CRISPR-Cas9 knockout screens and small molecule screens across thousands of genomically characterized cancer cell lines to identify dependencies that are specific to tumor subsets. These dependencies represent potential therapeutic targets, as they are genes or pathways that cancer cells rely on for survival but that normal cells can tolerate losing.

### Key Features

- **Comprehensive Screening**: Over 2,000 cancer cell lines representing diverse cancer types and molecular contexts
- **Multi-modal Data**: Integration of CRISPR screens, drug screens, and omics data (genomics, transcriptomics, proteomics, metabolomics)
- **Quarterly Releases**: Regular data updates with new cell lines, assays, and analytical improvements
- **Open Access**: All data and tools are freely available to the research community

## Data Types

### CRISPR Dependency Data
- **Gene Effects**: Processed using the Chronos algorithm to correct for copy number effects
- **Cell Line Coverage**: 2,000+ cell lines spanning multiple cancer types
- **Gene Coverage**: Genome-wide screening targeting ~18,000 genes

### Drug Sensitivity Data
- **Platforms**: Integration of data from GDSC, PRISM, and CTD2 screening efforts
- **Compound Coverage**: Thousands of compounds including FDA-approved drugs and experimental molecules
- **Dose-Response**: Comprehensive dose-response curves for accurate sensitivity measurements

### Omics Data
- **Expression**: RNA-seq data for all cell lines
- **Mutations**: Comprehensive mutation calling from whole-exome sequencing
- **Copy Number**: High-resolution copy number profiles
- **Proteomics**: Mass spectrometry-based protein abundance measurements
- **Metabolomics**: Small molecule metabolite profiles

## Tools and Interfaces

### Data Explorer
Interactive visualization tool allowing users to explore relationships between different data types, compare biomarkers, and identify patterns across cell lines.

### Cell Line Selector
Specialized tool for identifying and selecting cell lines based on specific criteria such as lineage, mutations, expression levels, or dependency profiles.

### Target Discovery App
Advanced analytics platform for identifying the most selective and predictable gene dependencies, helping prioritize potential therapeutic targets.

### Context Explorer
Tool for exploring genetic dependencies and compound sensitivities within specific cancer contexts, lineages, and molecular subtypes.

## Applications

DepMap data enables researchers to:
- Identify novel therapeutic targets specific to cancer subtypes
- Discover biomarkers that predict drug sensitivity
- Understand the genetic basis of cancer dependencies
- Prioritize compounds for further development
- Design combination therapy strategies

## Data Access

All DepMap data is freely available through:
- **Interactive Portal**: Web-based tools for data exploration and visualization
- **Bulk Downloads**: Complete datasets in standard formats (CSV, TSV)
- **Quarterly Releases**: Regular data updates with version control
- **Documentation**: Comprehensive guides and tutorials for data usage

## Citation

When using DepMap data, please cite the foundational publications and acknowledge the specific data release version used in your research.