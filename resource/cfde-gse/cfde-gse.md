---
activity_status: active
category: KnowledgeGraph
creation_date: '2025-09-23T00:00:00Z'
description: Common Fund Data Ecosystem Gene Set Enrichment (CFDE-GSE) is a knowledge graph that integrates gene set collections from multiple Common Fund programs to enable cross-program gene set enrichment analysis, functional annotation, and systems-level understanding of biological processes across diverse biomedical research domains.
domains:
- biomedical
- genomics
- systems biology
- functional genomics
- biological systems
- data integration
homepage_url: https://cfde.cloud/gse/
id: cfde-gse
last_modified_date: '2025-09-23T00:00:00Z'
layout: resource_detail
name: Common Fund Data Ecosystem Gene Set Enrichment (CFDE-GSE)
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: cfde-support@nih-cfde.org
  - contact_type: url
    value: https://cfde.cloud/
  label: Common Fund Data Ecosystem
- category: Organization
  contact_details:
  - contact_type: email
    value: avi.maayan@mssm.edu
  - contact_type: url
    value: https://labs.icahn.mssm.edu/maayanlab/
  label: Ma'ayan Laboratory
products:
- category: GraphicalInterface
  description: Interactive web interface for cross-program gene set enrichment analysis across Common Fund datasets
  format: http
  id: cfde-gse.portal
  name: CFDE Gene Set Enrichment Portal
  product_url: https://cfde.cloud/gse/
- category: ProgrammingInterface
  description: RESTful API for programmatic access to Common Fund gene set collections and enrichment analysis
  format: http
  id: cfde-gse.api
  name: CFDE-GSE API
  product_url: https://cfde.cloud/gse/api/
- category: GraphProduct
  description: Neo4j knowledge graph containing integrated gene sets from multiple Common Fund programs with cross-references
  format: neo4j
  id: cfde-gse.graph
  name: CFDE-GSE Knowledge Graph
  dump_format: neo4j
- category: Product
  description: Standardized gene set collections from Common Fund programs in GMT format
  id: cfde-gse.genesets
  name: CFDE Gene Set Collections
  product_url: https://cfde.cloud/gse/downloads/
publications:
- id: doi:10.1038/s41467-2022-28631-3
  title: "Cross-program analysis of the CFDE gene sets reveals common biological themes"
  year: '2022'
  journal: Nature Communications
  authors:
  - Clarke DJB
  - Jeon M
  - Stein DJ
  - Moiseyev N
  - Kropiwnicki E
  - Ben-Moshe NB
  - Barupal DK
  - Ma'ayan A
  preferred: true
repository: https://github.com/nih-cfde/cfde-gse
---

# Common Fund Data Ecosystem Gene Set Enrichment (CFDE-GSE)

CFDE-GSE is a comprehensive knowledge graph and analysis platform that integrates gene set collections from multiple NIH Common Fund programs, enabling researchers to perform cross-program enrichment analysis and discover biological connections across diverse research domains and datasets.

## Key Features

### Cross-Program Integration
- Gene sets from 15+ Common Fund programs including GTEx, HuBMAP, LINCS, and others
- Standardized gene identifiers and annotations across all programs
- Cross-reference mappings between program-specific terminologies
- Unified metadata schema for consistent data access

### Comprehensive Gene Set Collections
- Over 100,000 curated gene sets from Common Fund studies
- Cell type-specific gene signatures from single-cell analyses
- Tissue-specific expression profiles from bulk RNA-seq
- Drug perturbation signatures from LINCS
- Disease-associated gene sets from clinical studies

### Advanced Enrichment Analysis
- Statistical enrichment analysis with multiple correction methods
- Cross-program comparative enrichment capabilities
- Network-based enrichment using gene-gene relationships
- Time-course and dose-response enrichment patterns

## Data Sources

### Common Fund Programs
- **GTEx**: Tissue-specific gene expression signatures
- **HuBMAP**: Cell type-specific markers and spatial signatures
- **LINCS**: Drug and genetic perturbation signatures  
- **4D Nucleome**: Chromatin structure and regulatory signatures
- **Gabriella Miller Kids First**: Pediatric disease gene sets
- **Metabolomics**: Metabolic pathway gene associations
- **Protein Data Bank**: Structural biology gene signatures
- **Stimulating Peripheral Activity to Relieve Conditions (SPARC)**: Organ system gene sets

### External References
- Gene Ontology biological process and molecular function terms
- KEGG pathway annotations
- Reactome pathway database
- MSigDB hallmark and curated gene sets
- DisGeNET disease-gene associations

## Data Types

### Expression Signatures
- Differential expression results from RNA-seq studies
- Cell type marker genes from single-cell RNA-seq
- Tissue-enriched genes from bulk expression profiles
- Development stage-specific expression patterns

### Functional Annotations  
- Pathway membership and functional classifications
- Protein-protein interaction network modules
- Regulatory network target gene sets
- Metabolic pathway enzyme gene groups

### Perturbation Responses
- Drug treatment response signatures
- Genetic knockout/knockdown effects
- Environmental stress response patterns
- Disease state-associated expression changes

### Clinical Associations
- Disease biomarker gene sets
- Treatment response predictive signatures
- Prognostic gene expression profiles
- Pharmacogenomic gene variants

## Applications

### Cross-Program Discovery
- Identify shared biological themes across Common Fund studies
- Discover novel connections between different research domains
- Validate findings across independent datasets and methodologies
- Generate hypotheses for collaborative research initiatives

### Functional Interpretation
- Annotate gene lists from omics experiments with Common Fund signatures  
- Identify relevant cell types and tissues for experimental findings
- Connect molecular signatures to physiological processes and diseases
- Prioritize genes based on multi-program evidence

### Data Integration
- Harmonize gene expression data across Common Fund programs
- Enable meta-analyses spanning multiple research initiatives
- Facilitate data reuse and cross-validation studies
- Support FAIR data principles implementation

### Hypothesis Generation
- Discover unexpected biological connections through enrichment patterns
- Identify understudied genes with consistent signatures across programs
- Generate testable hypotheses for mechanism studies
- Guide experimental design based on existing Common Fund data

## Technical Implementation
CFDE-GSE is implemented as a Neo4j graph database with standardized nodes for genes, gene sets, studies, and biological annotations. The platform includes web-based tools for interactive enrichment analysis and programmatic APIs for computational workflows. All data processing follows CFDE metadata standards and includes comprehensive provenance tracking.