---
activity_status: active
category: Aggregator
creation_date: '2010-01-01T00:00:00Z'
description: NCBI's portal to information about conditions, phenotypes, and findings in humans related to medical genetics. Aggregates and organizes data from multiple authoritative sources including UMLS, OMIM, HPO, Mondo, Orphanet, GeneReviews, PharmGKB, and community submissions to GTR and ClinVar. Each concept is assigned a distinct Concept Unique Identifier (CUI) and integrated with related information from clinical resources, genetic testing registries, medical literature, and molecular resources.
domains:
  - genomics
  - clinical
  - health
  - biomedical
homepage_url: https://www.ncbi.nlm.nih.gov/medgen/
id: medgen
last_modified_date: '2025-10-21T00:00:00Z'
layout: resource_detail
name: MedGen
products:
  - category: GraphicalInterface
    description: Main web portal for searching and browsing conditions, phenotypes, and findings in humans related to medical genetics
    format: http
    id: medgen.portal
    name: MedGen Portal
    product_url: https://www.ncbi.nlm.nih.gov/medgen/
  - category: GraphicalInterface
    description: Advanced search interface with support for queries by name, related gene, clinical feature, and other criteria
    format: http
    id: medgen.search
    name: Advanced Search
    product_url: https://www.ncbi.nlm.nih.gov/medgen/advanced
  - category: Product
    description: Rich Rich Format file containing concept names and source identifiers with gzip compression
    format: txt
    compression: gzip
    id: medgen.mgconso
    name: MGCONSO (Concept Names)
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGCONSO.RRF.gz
  - category: Product
    description: Rich Rich Format file containing definitions and descriptions with gzip compression
    format: txt
    compression: gzip
    id: medgen.mgdef
    name: MGDEF (Definitions)
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGDEF.RRF.gz
  - category: MappingProduct
    description: Rich Rich Format file containing relationships between concepts with gzip compression
    format: txt
    compression: gzip
    id: medgen.mgrel
    name: MGREL (Relationships)
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGREL.RRF.gz
  - category: Product
    description: Rich Rich Format file containing attributes and properties with gzip compression
    format: txt
    compression: gzip
    id: medgen.mgsat
    name: MGSAT (Attributes)
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGSAT.RRF.gz
  - category: Product
    description: Rich Rich Format file containing semantic type assignments with gzip compression
    format: txt
    compression: gzip
    id: medgen.mgsty
    name: MGSTY (Semantic Types)
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGSTY.RRF.gz
  - category: Product
    description: Rich Rich Format file containing concept names for search with gzip compression
    format: txt
    compression: gzip
    id: medgen.names
    name: NAMES
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/NAMES.RRF.gz
  - category: MappingProduct
    description: Mappings between MedGen CUIs and external source identifiers with gzip compression
    format: txt
    compression: gzip
    id: medgen.id-mappings
    name: MedGen ID Mappings
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MedGenIDMappings.txt.gz
  - category: MappingProduct
    description: Mappings between MedGen and Human Phenotype Ontology terms with gzip compression
    format: txt
    compression: gzip
    id: medgen.hpo-mapping
    name: MedGen HPO Mapping
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MedGen_HPO_Mapping.txt.gz
  - category: MappingProduct
    description: Combined mappings between MedGen, HPO, and OMIM with gzip compression
    format: txt
    compression: gzip
    id: medgen.hpo-omim-mapping
    name: MedGen HPO OMIM Mapping
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MedGen_HPO_OMIM_Mapping.txt.gz
  - category: Product
    description: Links between MedGen concepts and PubMed articles with gzip compression
    format: txt
    compression: gzip
    id: medgen.pubmed-links
    name: MedGen PubMed Links
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/medgen_pubmed_lnk.txt.gz
  - category: Product
    description: History file tracking changes to MedGen CUIs
    format: txt
    id: medgen.cui-history
    name: MedGen CUI History
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MedGen_CUI_history.txt
  - category: Product
    description: History file tracking changes to HPO term mappings to CUIs
    format: txt
    id: medgen.hpo-history
    name: HPO CUI History
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/HPO_CUI_history.txt
  - category: Product
    description: History file tracking changes to Mondo term mappings to CUIs
    format: txt
    id: medgen.mondo-history
    name: Mondo CUI History
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MONDO_CUI_history.txt
  - category: Product
    description: History file tracking changes to Orphanet term mappings to CUIs
    format: txt
    id: medgen.ordo-history
    name: ORDO CUI History
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/ORDO_CUI_history.txt
  - category: Product
    description: Information about source databases and their contributions to MedGen
    format: txt
    id: medgen.sources
    name: MedGen Sources
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MedGen_Sources.txt
  - category: Product
    description: Merged CUI mappings showing concept consolidations with gzip compression
    format: txt
    compression: gzip
    id: medgen.merged
    name: MERGED (Merged CUIs)
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MERGED.RRF.gz
  - category: Product
    description: CSV format data files directory with additional data exports
    format: csv
    id: medgen.csv
    name: CSV Data Files
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/csv/
  - category: DocumentationProduct
    description: Documentation, help pages, and user guides for MedGen
    format: http
    id: medgen.help
    name: MedGen Documentation
    product_url: https://www.ncbi.nlm.nih.gov/medgen/docs/overview/
  - category: DocumentationProduct
    description: Frequently asked questions about MedGen
    format: http
    id: medgen.faq
    name: FAQ
    product_url: https://www.ncbi.nlm.nih.gov/medgen/docs/faq/
  - category: DocumentationProduct
    description: README file with detailed information about FTP data files and formats
    format: txt
    id: medgen.readme
    name: README
    product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/README.txt
---

# MedGen

MedGen is NCBI's portal to information about conditions, phenotypes, and findings in humans related to medical genetics. It serves as a comprehensive aggregator that organizes and integrates information from multiple authoritative sources, providing a unified view of genetic conditions and their relationships.

## Overview

MedGen includes diseases such as Mendelian disorders, multi-factorial disorders, chronic disease susceptibilities, somatic phenotypes, and pharmacogenetic responses. The database also includes infectious disease terms to support submitters of the NIH Genetic Testing Registry (GTR) and clinicians looking for tests and terms related to infectious agents in human samples.

## Core Concept

Terms from various sources including GTR and ClinVar submissions, Unified Medical Language System (UMLS), Online Mendelian Inheritance in Man (OMIM), Human Phenotype Ontology (HPO), Mondo Disease Ontology, rare disease terms from Orphanet Rare Disease Ontology (ORDO), and other sources are integrated into unique concepts. Each concept is assigned a distinct identifier called the Concept Unique Identifier (CUI) and a preferred name.

## Content Integration

The core content of a concept record includes:

- **Names and Identifiers**: Names used by different databases with links to external resources (ontologies such as HPO, ORDO, and Mondo)
- **Modes of Inheritance**: Information about genetic inheritance patterns
- **Clinical Features**: Associated phenotypes and clinical characteristics
- **Genomic Location**: Map location of the loci affecting the phenotype
- **External Resources**: Links to resources for clinicians (OMIM), customers (MedlinePlus), genetic tests (GTR), medical literature (GeneReviews, PubMed), and molecular resources (ClinVar, RefSeqGene)

## Data Sources

MedGen aggregates data from multiple authoritative sources with varying update frequencies:

| Source | Update Frequency | Primary Data Types | Coverage |
|--------|------------------|-------------------|----------|
| UMLS | 2x/year | CUI, descriptions, name and ID | 96% |
| HPO | Monthly | Name and ID, Phenotype:Disease relationships | 8% |
| Mondo | Monthly | Name, ID; Orphanet and GARD | 10% |
| Orphanet (ORDO) | Monthly | Name, ID, Mode of Inheritance | 4% |
| OMIM | Daily | Name, ID, Gene:Disease, description | 5% |
| GeneReviews | Weekly | Name, Gene:Disease, description | 0.4% |
| PharmGKB | Monthly | Drug name, ID, Drug:Gene relationships | 0.5% |
| MedGen (internal) | Daily | Name, CN CUI, Drug:Disease, Disease:Disease | 2% |
| NCBI Gene | Daily | Gene symbol, chromosome location | N/A |

*Note: MedGen terms can have one or more external identifiers/sources mapped. Percentages are averaged from data analyzed in 2024.*

## Concept Unique Identifiers

MedGen primarily uses CUIs from the UMLS dataset. When a CUI cannot be found in UMLS to match a record in MedGen, an NCBI-generated CUI is provided instead. These begin with "CN" to clarify they are not UMLS-provided CUIs (which all begin with "C"). CN-type CUIs may be created from submissions in the NIH Genetic Testing Registry or ClinVar that do not match a record in UMLS.

## Pharmacogenomics

MedGen provides standardized terminology for pharmacogenomics, describing the interaction between an individual's genetic code and medication response. Using data from PharmGKB, MedGen creates disease records describing abnormal responses to drugs driven by genetic or environmental factors. These terms are created and maintained by MedGen with links to expert clinical recommendations, FDA-approved drug labels, and PharmGKB pages.

## Data Processing and Curation

MedGen employs both automated and manual curation processes:

### Automated Alignment
When new versions of source data become available, automated pipelines download and process the data, making local copies. The relevant data is subset, existing terms are updated as needed, and new terms are added. Mapping is done between identifiers or concept preferred names, or both, depending on the data sources involved.

### Manual Curation
The manual curation process follows a standard decision tree to evaluate source terms and potential matches in MedGen. When source data is unclear, curators contact the source to clarify term scope and meaning. MedGen terms are curated to align with sources by splitting or merging terms or creating novel MedGen records as needed.

## Related NCBI Resources

MedGen integrates with several NCBI resources:
- **ClinVar**: Database of genomic variation and its relationship to human health
- **Gene**: NCBI's gene-centered database
- **Genetic Testing Registry (GTR)**: Registry of genetic tests
- **GeneReviews**: Expert-authored disease descriptions
- **RefSeqGene**: Reference standard sequences for human genes
- **Medical Genetics Summaries**: Information about genetic conditions

## FTP Data Files

MedGen provides extensive downloadable data through its FTP site, including:
- **Rich Rich Format (RRF) files**: Core database files with concept names, definitions, relationships, attributes, and semantic types
- **Mapping files**: ID mappings to external sources, HPO, OMIM, and other databases
- **History files**: Tracking changes to CUIs and external term mappings
- **Literature links**: Connections between concepts and PubMed articles
- **CSV exports**: Alternative format data files for easier processing

All major data files are provided with gzip compression to reduce file sizes while maintaining complete data integrity.
