---
activity_status: active
category: KnowledgeGraph
creation_date: '2025-09-23T00:00:00Z'
description: Enrichr-KG is a comprehensive knowledge graph that integrates gene set enrichment analysis libraries from Enrichr, connecting genes to biological terms, pathways, diseases, drugs, and other functional annotations across multiple domains and species to enable multi-layered biological discovery and hypothesis generation.
domains:
- biomedical
- genomics
- systems biology
- drug discovery
- biological systems
homepage_url: https://maayanlab.cloud/enrichr-kg/
id: enrichr-kg
last_modified_date: '2025-09-23T00:00:00Z'
layout: resource_detail
name: Enrichr-KG
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: avi.maayan@mssm.edu
  - contact_type: url
    value: https://labs.icahn.mssm.edu/maayanlab/
  label: Ma'ayan Laboratory
products:
- category: GraphicalInterface
  description: Interactive web interface for exploring the Enrichr-KG knowledge graph with single and two-term search capabilities
  format: http
  id: enrichr-kg.portal
  name: Enrichr-KG Explorer
  product_url: https://maayanlab.cloud/enrichr-kg/
- category: ProgrammingInterface
  description: API endpoints for programmatic access to Enrichr-KG graph data and enrichment analysis
  format: http
  id: enrichr-kg.api
  name: Enrichr-KG API
  product_url: https://maayanlab.cloud/enrichr-kg/api/
- category: GraphProduct
  description: Neo4j graph database containing integrated gene set enrichment libraries with genes, terms, pathways, and functional annotations
  format: neo4j
  id: enrichr-kg.graph
  name: Enrichr-KG Neo4j Database
  dump_format: neo4j
publications:
- id: doi:10.1093/nar/gkad393
  title: "Enrichr-KG: bridging enrichment analysis across multiple libraries"
  year: '2023'
  journal: Nucleic Acids Research
  authors:
  - Evangelista JE
  - Xie Z
  - Marino GB
  - Nguyen N
  - Clarke DJB
  - Ma'ayan A
  preferred: true
repository: https://github.com/MaayanLab/enrichr-kg
---

# Enrichr-KG

Enrichr-KG is a comprehensive knowledge graph that bridges multiple gene set enrichment analysis libraries from the Enrichr platform. The knowledge graph integrates over 200 gene set libraries spanning diverse biological domains including pathways, diseases, drugs, cell types, tissues, and functional annotations.

## Key Features

### Comprehensive Integration
- Integrates gene set libraries from Enrichr covering multiple biological domains
- Connects genes to functional terms, pathways, diseases, and drug perturbations
- Spans multiple species with focus on human, mouse, and other model organisms
- Contains millions of gene-term associations from curated and computational sources

### Multi-Modal Connectivity
- Gene-to-pathway associations from KEGG, Reactome, WikiPathways
- Gene-disease relationships from DisGeNET, GWAS Catalog, and clinical databases
- Drug-gene interactions from LINCS L1000, CREEDS, and chemical perturbation datasets
- Cell type and tissue-specific expression patterns from single-cell and bulk RNA-seq

### Interactive Exploration
- Web-based interface for single and two-term graph searches
- Shortest path analysis between biological entities
- Neighborhood exploration around genes, diseases, drugs, and pathways
- Customizable visualization and export capabilities

## Applications

### Drug Repurposing
- Identify potential therapeutic targets through disease-gene-drug networks
- Explore mechanism of action for existing drugs
- Predict drug side effects and contraindications

### Biomarker Discovery
- Connect disease phenotypes to molecular signatures
- Identify diagnostic and prognostic biomarkers
- Explore tissue-specific disease mechanisms

### Pathway Analysis
- Multi-layered pathway enrichment across different databases
- Cross-species pathway conservation analysis
- Identification of pathway crosstalk and regulatory networks

## Data Sources
Enrichr-KG integrates data from numerous high-quality biological databases and resources including pathway databases (KEGG, Reactome), disease databases (OMIM, DisGeNET), drug databases (DrugBank, LINCS), expression databases (GTEx, Human Protein Atlas), and many specialized functional annotation resources.