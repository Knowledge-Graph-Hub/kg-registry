---
activity_status: active
category: Database
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://rampdb.nih.gov/
  - contact_type: email
    value: rampdb@nih.gov
  id: ncats-rampdb
  label: NCATS RaMP-DB Team
creation_date: '2025-10-30T00:00:00Z'
description: RaMP-DB (Relational database of Metabolomic Pathways) is a multi-sourced
  integrated database with comprehensive annotations on biological pathways, structure/chemistry,
  disease and ontology annotations for genes, proteins, and metabolites. RaMP-DB provides
  a framework for single and batch queries of annotations, and for performing chemical
  and biological pathway enrichment analyses on multi-omic datasets.
domains:
- systems biology
- pathways
- biomedical
id: rampdb
infores_id: rampdb
last_modified_date: '2026-01-15T00:00:00Z'
layout: resource_detail
name: RaMPDB
homepage_url: https://rampdb.nih.gov/
synonyms:
- RaMP-DB
- RaMPDB
- Relational database of Metabolomic Pathways
products:
- id: rampdb.database
  name: RaMP-DB Integrated Database
  description: Multi-sourced relational database integrating metabolomic pathway information,
    biochemical reactions, ontologies, and chemical descriptors for genes, proteins,
    and metabolites with query and enrichment analysis capabilities.
  category: DatabaseProduct
  product_url: https://rampdb.nih.gov/
  original_source:
  - kegg
  - reactome
  - hmdb
  - wikipathways
  - rampdb
  is_public: true
- id: rampdb.api
  name: RaMP-DB API
  description: Programmatic interface for accessing RaMP-DB integrated metabolomic
    pathway data and performing enrichment analyses.
  category: ProgrammingInterface
  product_url: https://rampdb.nih.gov/api
  original_source:
  - rampdb
  is_public: true
taxon:
- NCBITaxon:9606
---

# RaMPDB

## Overview

RaMP-DB (Relational database of Metabolomic Pathways) is a comprehensive relational database that integrates metabolomic pathway information from multiple authoritative sources. The database provides unified access to pathway annotations, biochemical reactions, chemical structures, disease associations, and ontology mappings for genes, proteins, and metabolites.

Hosted by NCATS (National Center for Advancing Translational Sciences), RaMP-DB serves as a central resource for metabolomics researchers, enabling multi-omic data interpretation through integrated pathway analysis and enrichment testing.

## Key Features

### Multi-Source Integration

RaMP-DB integrates data from major metabolomicpathway and biochemical databases including:
- **KEGG** (Kyoto Encyclopedia of Genes and Genomes)
- **Reactome**: Curated pathway database
- **HMDB** (Human Metabolome Database)
- **WikiPathways**: Community-curated pathway resource

### Comprehensive Annotations

- **Biochemical Pathways**: Complete pathway membership for metabolites, genes, and proteins
- **Reactions**: Enzymatic and non-enzymatic biochemical transformations
- **Chemical Descriptors**: Structural and physicochemical properties
- **Ontologies**: Standardized classifications and relationships
- **Disease Associations**: Links to disease contexts and clinical relevance
- **Identifier Harmonization**: Cross-references among different identifier systems

### Analysis Capabilities

- **Single and Batch Queries**: Individual lookups or bulk data queries
- **Pathway Enrichment Analysis**: Statistical testing for overrepresented pathways
- **Chemical Enrichment**: Analysis of enriched chemical classes or properties
- **Multi-Omic Integration**: Combined analysis of metabolomic, proteomic, and genomic data

## Applications

### Metabolomics Research

- Interpretation of untargeted metabolomics experiments
- Pathway-level analysis of metabolite abundance changes
- Biomarker identification and validation
- Metabolic phenotyping

### Systems Biology

- Multi-omic data integration and interpretation
- Metabolic network reconstruction
- Flux balance analysis support
- Systems-level understanding of metabolism

### Translational Research

- Disease mechanism elucidation through metabolic profiling
- Drug target identification
- Precision medicine biomarker development
- Therapeutic intervention evaluation

## Web Interface

The RaMP-DB website (https://rampdb.nih.gov/) provides:
- Interactive search and browse functionality
- Enrichment analysis tools
- Data visualization
- Bulk data download options
- API access for programmatic queries

## Technical Implementation

- **Architecture**: Relational database structure enabling complex queries
- **API**: RESTful API for programmatic access
- **Update Cycle**: Regular updates incorporating latest source database releases
- **Data Format**: Standardized identifiers and controlled vocabularies

## Data Coverage

- **Genes**: Human and model organism genes involved in metabolism
- **Proteins**: Enzymes and metabolic proteins
- **Metabolites**: Small molecule metabolites with pathway assignments
- **Pathways**: Biochemical pathways from integrated sources
- **Reactions**: Enzyme-catalyzed and spontaneous reactions

## Integration

RaMP-DB is registered as an information resource (infores:rampdb) in the NCATS Biomedical Data Translator ecosystem, supporting federated queries across biomedical knowledge sources.

---

*For current database version, data statistics, API documentation, and tutorials, visit the official RaMP-DB website at https://rampdb.nih.gov/*

**Note:** This is a stub entry that was automatically created from the [Translator Information Resource Registry](https://biolink.github.io/information-resource-registry/). It requires manual curation to add complete metadata, products, and additional information.

