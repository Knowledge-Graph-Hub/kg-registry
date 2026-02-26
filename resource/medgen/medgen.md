---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  id: ncbi
  label: MedGen Team (NCBI)
  contact_details:
  - contact_type: email
    value: medgen_help@ncbi.nlm.nih.gov
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/medgen/docs/overview/
creation_date: '2025-07-17T00:00:00Z'
description: NCBI's portal to information about conditions, phenotypes, and findings
  in humans related to medical genetics. Aggregates and organizes data from multiple
  authoritative sources including UMLS, OMIM, HPO, Mondo, Orphanet, GeneReviews, PharmGKB,
  and community submissions to GTR and ClinVar. Each concept is assigned a distinct
  Concept Unique Identifier (CUI) and integrated with related information from clinical
  resources, genetic testing registries, medical literature, and molecular resources.
domains:
- genomics
- clinical
- health
- biomedical
homepage_url: https://www.ncbi.nlm.nih.gov/medgen/
id: medgen
infores_id: medgen
last_modified_date: '2026-02-26T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/home/about/policies/
  label: NCBI and NLM Data Usage Policies and Disclaimers
name: MedGen
products:
- category: GraphicalInterface
  description: Main web portal for searching and browsing conditions, phenotypes,
    and findings in humans related to medical genetics
  format: http
  id: medgen.portal
  name: MedGen Portal
  product_url: https://www.ncbi.nlm.nih.gov/medgen/
  original_source:
  - medgen
- category: GraphicalInterface
  description: Advanced search interface with support for queries by name, related
    gene, clinical feature, and other criteria
  format: http
  id: medgen.search
  name: Advanced Search
  product_url: https://www.ncbi.nlm.nih.gov/medgen/advanced/
  original_source:
  - medgen
- category: Product
  compression: gzip
  description: Rich Release Format (RRF) file containing concept names and source
    identifiers with gzip compression
  format: txt
  id: medgen.mgconso
  name: MGCONSO (Concept Names)
  product_file_size: 15843494
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGCONSO.RRF.gz
  original_source:
  - medgen
  - umls
- category: Product
  compression: gzip
  description: Rich Release Format (RRF) file containing definitions and descriptions
    with gzip compression
  format: txt
  id: medgen.mgdef
  name: MGDEF (Definitions)
  product_file_size: 5062289
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGDEF.RRF.gz
  original_source:
  - medgen
  - umls
- category: MappingProduct
  compression: gzip
  description: Rich Release Format (RRF) file containing relationships between concepts
    with gzip compression
  format: txt
  id: medgen.mgrel
  name: MGREL (Relationships)
  product_file_size: 15661303
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGREL.RRF.gz
  original_source:
  - medgen
  - umls
- category: Product
  compression: gzip
  description: Rich Release Format (RRF) file containing attributes and properties
    with gzip compression
  format: txt
  id: medgen.mgsat
  name: MGSAT (Attributes)
  product_file_size: 11710268
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGSAT.RRF.gz
  original_source:
  - medgen
  - umls
- category: Product
  compression: gzip
  description: Rich Release Format (RRF) file containing semantic type assignments
    with gzip compression
  format: txt
  id: medgen.mgsty
  name: MGSTY (Semantic Types)
  product_file_size: 1644564
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MGSTY.RRF.gz
  original_source:
  - medgen
  - umls
- category: Product
  compression: gzip
  description: Rich Release Format (RRF) file containing concept names for search
    with gzip compression
  format: txt
  id: medgen.names
  name: NAMES
  product_file_size: 3097271
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/NAMES.RRF.gz
  original_source:
  - medgen
  - umls
- category: MappingProduct
  compression: gzip
  description: Mappings between MedGen CUIs and external source identifiers with gzip
    compression
  format: txt
  id: medgen.id-mappings
  name: MedGen ID Mappings
  product_file_size: 5955308
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MedGenIDMappings.txt.gz
  original_source:
  - medgen
- category: MappingProduct
  compression: gzip
  description: Mappings between MedGen and Human Phenotype Ontology terms with gzip
    compression
  format: txt
  id: medgen.hpo-mapping
  name: MedGen HPO Mapping
  product_file_size: 389609
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MedGen_HPO_Mapping.txt.gz
  original_source:
  - medgen
  - hp
- category: MappingProduct
  compression: gzip
  description: Combined mappings between MedGen, HPO, and OMIM with gzip compression
  format: txt
  id: medgen.hpo-omim-mapping
  name: MedGen HPO OMIM Mapping
  product_file_size: 4125863
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MedGen_HPO_OMIM_Mapping.txt.gz
  original_source:
  - medgen
  - hp
  - omim
- category: Product
  compression: gzip
  description: Links between MedGen concepts and PubMed articles with gzip compression
  format: txt
  id: medgen.pubmed-links
  name: MedGen PubMed Links
  product_file_size: 239947326
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/medgen_pubmed_lnk.txt.gz
  original_source:
  - medgen
  - pubmed
- category: Product
  description: History file tracking changes to MedGen CUIs
  format: txt
  id: medgen.cui-history
  name: MedGen CUI History
  product_file_size: 88702
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MedGen_CUI_history.txt
  original_source:
  - medgen
- category: Product
  description: History of mappings between MedGen UIDs and CUIs over time
  format: txt
  id: medgen.uid-cui-history
  name: MedGen UID CUI History
  original_source:
  - medgen
  product_file_size: 59225507
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MedGen_UID_CUI_history.txt
- category: Product
  description: History file tracking changes to HPO term mappings to CUIs
  format: txt
  id: medgen.hpo-history
  name: HPO CUI History
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/HPO_CUI_history.txt
  product_file_size: 1299018
  original_source:
  - medgen
  - hp
- category: Product
  description: History file tracking changes to Mondo term mappings to CUIs
  format: txt
  id: medgen.mondo-history
  name: Mondo CUI History
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MONDO_CUI_history.txt
  product_file_size: 1012883
  original_source:
  - medgen
  - mondo
- category: Product
  description: History file tracking changes to Orphanet term mappings to CUIs
  format: txt
  id: medgen.ordo-history
  name: ORDO CUI History
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/ORDO_CUI_history.txt
  product_file_size: 1130936
  original_source:
  - medgen
  - orphanet
- category: Product
  description: Information about source databases and their contributions to MedGen
  format: txt
  id: medgen.sources
  name: MedGen Sources
  product_file_size: 10385
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MedGen_Sources.txt
  original_source:
  - medgen
- category: Product
  compression: gzip
  description: Merged CUI mappings showing concept consolidations with gzip compression
  format: txt
  id: medgen.merged
  name: MERGED (Merged CUIs)
  product_file_size: 47602
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/MERGED.RRF.gz
  original_source:
  - medgen
  - umls
- category: Product
  description: CSV format data files directory with additional data exports
  format: csv
  id: medgen.csv
  name: CSV Data Files
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/csv/
  original_source:
  - medgen
- category: DocumentationProduct
  description: Documentation, help pages, and user guides for MedGen
  format: http
  id: medgen.help
  name: MedGen Documentation
  product_url: https://www.ncbi.nlm.nih.gov/medgen/docs/overview/
  original_source:
  - medgen
- category: DocumentationProduct
  description: Frequently asked questions about MedGen
  format: http
  id: medgen.faq
  name: FAQ
  product_url: https://www.ncbi.nlm.nih.gov/medgen/docs/faq/
  original_source:
  - medgen
- category: DocumentationProduct
  description: README file with detailed information about FTP data files and formats
  format: txt
  id: medgen.readme
  name: README
  product_file_size: 17286
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/README.txt
  original_source:
  - medgen
- category: GraphProduct
  description: PheKnowLator graph files, including subsets with and without inverse
    relations.
  format: owl
  id: pheknowlator.graph
  latest_version: current_build
  name: PheKnowLator graph
  original_source:
  - cl
  - clo
  - chebi
  - go
  - hp
  - mondo
  - pw
  - pr
  - ro
  - so
  - uberon
  - vo
  - bioportal
  - clinvar
  - ctd
  - disgenet
  - ensembl
  - genemania
  - hgnc
  - hpa
  - ncbigene
  - medgen
  - reactome
  - string
  - uniprot
  product_url: https://console.cloud.google.com/storage/browser/pheknowlator/current_build/knowledge_graphs?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&inv=1&invt=Ab5_1Q&project=pheknowlator
  secondary_source:
  - pheknowlator
  versions:
  - v1.0.0
  - v2.0.0
  - v2.1.0
  - v3.0.2
  - v4.0.0
  - current_build
- category: MappingProduct
  description: MIM to Gene and MedGen mapping data connecting genetic disorders to
    genes
  format: tsv
  id: ncbigene.mim2gene_medgen
  name: MIM to Gene MedGen Mapping
  original_source:
  - ncbigene
  - medgen
  - omim
  product_file_size: 954971
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/mim2gene_medgen
- category: GraphProduct
  description: Core UniBioMap graph edges file.
  format: csv
  id: unibiomap.links
  name: UniBioMap Graph Links
  original_source:
  - unibiomap
  - hpa
  - go
  - bindingdb
  - foodb
  - tcdb
  - biogrid
  - ctd
  - chebi
  - stitch
  - intact
  - uniprot
  - unichem
  - pubchem
  - batman
  - string
  - ncbigene
  - drugbank
  - kegg
  - sider
  - compath
  - phosphositeplus
  - hp
  - chembl
  - reactome
  - smpdb
  - uberon
  - hmdb
  - medgen
  - umls
  - mesh
  - inchikey
  - unichem
  - omim
  product_file_size: 1406201678
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.links.csv
- category: GraphProduct
  description: Auxiliary UniBioMap graph annotations and metadata.
  format: tsv
  id: unibiomap.auxs
  name: UniBioMap Graph Auxiliaries
  original_source:
  - unibiomap
  - hpa
  - go
  - bindingdb
  - foodb
  - tcdb
  - biogrid
  - ctd
  - chebi
  - stitch
  - intact
  - uniprot
  - unichem
  - pubchem
  - batman
  - string
  - ncbigene
  - drugbank
  - kegg
  - sider
  - compath
  - phosphositeplus
  - hp
  - chembl
  - reactome
  - smpdb
  - uberon
  - hmdb
  - medgen
  - umls
  - mesh
  - inchikey
  - unichem
  - omim
  product_file_size: 591290539
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.auxs.tsv
- category: GraphProduct
  description: Predicted UniBioMap graph edges with confidence scores.
  format: csv
  id: unibiomap.pred
  name: UniBioMap Predicted Graph
  original_source:
  - unibiomap
  - hpa
  - go
  - bindingdb
  - foodb
  - tcdb
  - biogrid
  - ctd
  - chebi
  - stitch
  - intact
  - uniprot
  - unichem
  - pubchem
  - batman
  - string
  - ncbigene
  - drugbank
  - kegg
  - sider
  - compath
  - phosphositeplus
  - hp
  - chembl
  - reactome
  - smpdb
  - uberon
  - hmdb
  - medgen
  - umls
  - mesh
  - inchikey
  - unichem
  - omim
  product_file_size: 2484982268
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.csv
- category: GraphProduct
  description: Full unfiltered UniBioMap predicted graph edges file.
  format: csv
  id: unibiomap.pred.full
  name: UniBioMap Predicted Graph (Full)
  original_source:
  - unibiomap
  - hpa
  - go
  - bindingdb
  - foodb
  - tcdb
  - biogrid
  - ctd
  - chebi
  - stitch
  - intact
  - uniprot
  - unichem
  - pubchem
  - batman
  - string
  - ncbigene
  - drugbank
  - kegg
  - sider
  - compath
  - phosphositeplus
  - hp
  - chembl
  - reactome
  - smpdb
  - uberon
  - hmdb
  - medgen
  - umls
  - mesh
  - inchikey
  - unichem
  - omim
  product_file_size: 6303875907
  product_url: https://aideepmed.com/UniBioMap/database/unibiomap/unibiomap.pred.full.csv
- category: DocumentationProduct
  description: Directory of MedGen presentations related to terminology and curation
    workflows
  format: http
  id: medgen.presentations
  name: MedGen Presentations
  original_source:
  - medgen
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/medgen/presentations/
taxon:
- NCBITaxon:9606
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
