---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: avi.maayan@mssm.edu
      - contact_type: url
        value: https://labs.icahn.mssm.edu/maayanlab/
    label: Ma'ayan Laboratory
creation_date: '2025-09-23T00:00:00Z'
description: Enrichr-KG is a Ma'ayan Lab knowledge graph and enrichment web resource built from Enrichr gene set libraries, connecting genes to pathways, diseases, drugs, cell types, ontologies, and other functional annotations for graph-based exploration and enrichment analysis.
domains:
  - biomedical
  - genomics
  - systems biology
  - drug discovery
  - biological systems
homepage_url: https://maayanlab.cloud/enrichr-kg/
id: enrichr-kg
last_modified_date: '2026-05-28T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Enrichr-KG
products:
  - category: GraphicalInterface
    description: Interactive web interface for gene set enrichment analysis, Enrichr term expansion, and graph exploration across integrated Enrichr-KG libraries
    format: http
    id: enrichr-kg.portal
    name: Enrichr-KG Explorer
    product_url: https://maayanlab.cloud/enrichr-kg/
    original_source:
      - source: enrichr-kg
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: enrichr
        relation_type: prov:wasInfluencedBy
  - category: ProgrammingInterface
    description: API surface for programmatic access to Enrichr-KG enrichment analysis and graph-backed query results
    format: json
    id: enrichr-kg.api
    is_public: true
    name: Enrichr-KG API
    product_url: https://maayanlab.cloud/enrichr-kg/api/
    original_source:
      - source: enrichr-kg
        relation_type: prov:hadPrimarySource
    secondary_source:
      - source: enrichr
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Neo4j graph database integrating Enrichr gene set libraries with genes, terms, pathways, diseases, drugs, cell types, and other functional annotations
    dump_format: neo4j
    format: neo4j
    id: enrichr-kg.graph
    name: Enrichr-KG Neo4j Database
    original_source:
      - source: enrichr-kg
        relation_type: prov:hadPrimarySource
      - source: enrichr
        relation_type: prov:hadPrimarySource
      - source: kegg
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: wikipathways
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
publications:
  - authors:
      - Evangelista JE
      - Xie Z
      - Marino GB
      - Nguyen N
      - Clarke DJB
      - Ma'ayan A
    id: doi:10.1093/nar/gkad393
    journal: Nucleic Acids Research
    preferred: true
    title: 'Enrichr-KG: bridging enrichment analysis across multiple libraries'
    year: '2023'
repository: https://github.com/MaayanLab/enrichr-kg
taxon:
  - NCBITaxon:9606
---

# Enrichr-KG

Enrichr-KG is a Ma'ayan Lab knowledge graph and enrichment-analysis resource that builds on the Enrichr library ecosystem. Its public interface supports standard gene-list submission, term-centric exploration of Enrichr libraries, and graph traversal across connected biological entities.

## Key Features

### Comprehensive Integration
- Integrates Enrichr gene set libraries covering multiple biological domains
- Connects genes to functional terms, pathways, diseases, and drug perturbations
- Spans multiple species with focus on human, mouse, and other model organisms
- Contains large numbers of gene-term associations from curated, imported, and derived libraries exposed through the Enrichr ecosystem

### Multi-Modal Connectivity
- Gene-to-pathway associations from KEGG, Reactome, WikiPathways
- Gene-disease relationships from DisGeNET, GWAS Catalog, and clinical databases
- Drug-gene interactions from LINCS L1000, CREEDS, and chemical perturbation datasets
- Cell type and tissue-specific expression patterns from single-cell and bulk RNA-seq

### Interactive Exploration
- Web-based interface for gene-list enrichment, single-term search, and two-term graph searches
- Shortest path analysis between biological entities
- Neighborhood exploration around genes, diseases, drugs, and pathways
- Customizable visualization and export capabilities

## Original Sources

- Enrichr gene set libraries and associated enrichment-analysis workflows

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
Enrichr-KG is built from the Enrichr collection of gene set libraries, which in turn aggregate and normalize content from many upstream biological resources. The public Enrichr-KG site highlights integrated library families spanning pathway databases such as KEGG, Reactome, and WikiPathways; disease and phenotype resources such as GWAS Catalog, DisGeNET, HPO, and MGI; perturbation and drug-signature resources including LINCS and DepMap; and expression- or cell-type-oriented resources such as ARCHS4, Tabula Sapiens, Tabula Muris, HuBMAP, and GTEx-derived collections.

## Automated Evaluation

- View the automated evaluation: [enrichr-kg automated evaluation](enrichr-kg_eval_automated.html)
