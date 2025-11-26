---
activity_status: active
category: KnowledgeGraph
creation_date: '2025-10-30T00:00:00Z'
description: The integrated DIetary Supplements Knowledge base (iDISK) is a standardized knowledge base integrating dietary supplement information from multiple authoritative sources including ingredients, products, drug interactions, effectiveness, adverse effects, and therapeutic uses, represented according to established terminology principles with UMLS and MedDRA mappings.
domains:
  - nutrition
  - biomedical
  - health
  - pharmacology
homepage_url: https://doi.org/10.13020/d6bm3v
id: "idisk"
infores_id: "idisk"
last_modified_date: '2025-11-25T00:00:00Z'
layout: resource_detail
name: integrated Dietary Supplement Knowledge Base
products:
  - category: GraphProduct
    description: The integrative Biomedical Knowledge Hub (iBKH) knowledge graph, harmonizing and integrating information from diverse biomedical resources including DRKG, iDISK, and multiple databases (BRENDA, CTD, DrugBank, KEGG, PharmGKB, Reactome, SIDER, and others).
    id: "ibkh.graph"
    name: iBKH Knowledge Graph
    original_source:
      - drkg
      - idisk
      - brenda
      - ctd
      - drugbank
      - kegg
      - pharmgkb
      - reactome
      - sider
      - tissues
      - bgee
      - doid
      - uberon
      - cl
      - hgnc
      - chembl
      - chebi
synonyms:
  - iDISK
publications:
  - id: "doi:10.1093/jamia/ocz216"
    title: "iDISK: the integrated DIetary Supplements Knowledge base"
    year: "2020"
    preferred: true
repository: https://github.com/zhang-informatics/iDISK
contacts:
  - category: Individual
    label: Rui Zhang
    contact_details:
      - contact_type: url
        value: "https://github.com/zhang-informatics"
---

# integrated Dietary Supplement Knowledge Base (iDISK)

## Overview

iDISK (integrated DIetary Supplements Knowledge base) is a comprehensive, standardized knowledge base of dietary supplement (DS) information developed to address the critical need for structured, computable DS knowledge. By integrating information from four well-regarded DS resources into a unified data model and linking to established controlled vocabularies (UMLS, MedDRA), iDISK facilitates information retrieval, decision support, and interoperability across DS systems and applications.

## Data Model

The iDISK data model comprises four core data elements:

### Concept Types (7 types)
1. **Semantic Dietary Supplement Ingredient (SDSI)**: Non-branded individual ingredients (4,208 concepts)
2. **Dietary Supplement Product (DSP)**: Marketed supplement products (137,568 concepts)
3. **Pharmacological Drug (PD)**: Prescription and OTC drugs (495 concepts)
4. **Disease (DIS)**: Diseases and conditions (776 concepts)
5. **Therapeutic Class (TC)**: Functional classifications (605 concepts)
6. **System Organ Class (SOC)**: Biological system categories (17 concepts)
7. **Signs/Symptoms (SS)**: Physical manifestations (985 concepts)

### Relationship Types (6 types)
- **is_effective_for**: DS effectiveness for diseases/conditions (5,363 relationships)
- **has_therapeutic_class**: Functional classification (5,454 relationships)
- **has_adverse_effect_on**: Adverse effects on organ systems (3,168 relationships)
- **has_adverse_reaction**: Specific adverse symptoms (2,233 relationships)
- **has_ingredient**: Product ingredient composition (689,826 relationships)
- **interacts_with**: Drug-supplement interactions (3,631 relationships)

### Concept Attributes (7 types)
- Source Material
- UMLS Semantic Type
- Ingredient Category
- Background (summaries)
- Safety (concerns)
- Mechanism of Action
- LanguaL Product Type

### Relationship Attributes (3 types)
- **Interaction Rating**: Likelihood of drug interaction (Likely/Probable/Possible/Unlikely)
- **Interaction Severity**: Severity if occurs (High/Moderate/Mild/Insignificant)
- **Effectiveness Rating**: Evidence for effectiveness (Likely/Probable/Possible/Unlikely)

## Data Sources

iDISK integrates information from four authoritative resources:

1. **Natural Medicines Comprehensive Database (NMCD)**: Evidence-based ingredient monographs with effectiveness, interactions, adverse effects
2. **Memorial Sloan Kettering Cancer Center (MSKCC) About Herbs**: Consumer/professional herb information
3. **Dietary Supplement Label Database (DSLD)**: 76,000+ US product labels with detailed ingredient information
4. **Natural Health Products Database (NHP)**: Canadian natural health products licensed by Health Canada

## Key Statistics

- **Total Concepts**: 144,654
- **Total Relationships**: 709,675
- **Total Attributes**: 84,674
- **DS Ingredients**: 4,208
- **DS Products**: 137,568
- **Accuracy**: 99.7% (atoms), 97.4% (relationships), 99.6% (attributes)

## Key Features

### Standardization
- **Terminology Normalization**: RxNorm-inspired model for ingredient naming
- **UMLS Mapping**: Concepts mapped to Unified Medical Language System
- **MedDRA Mapping**: System organ classes aligned to MedDRA
- **Structured Representation**: Consistent data model across all sources

### Comprehensive Coverage
- Ingredient-level and product-level information
- Drug-supplement interactions with severity ratings
- Disease/condition effectiveness with evidence ratings
- Adverse effects and safety information
- Therapeutic classifications
- Cross-source integration and synonym resolution

### Interoperability
- Links to UMLS concepts
- Standardized identifiers
- Semantic type annotations
- Cross-reference mappings
- Compatible with health IT systems

## Applications

### Clinical Decision Support
- Drug-supplement interaction checking
- Safety assessment for supplement use
- Effectiveness evaluation for conditions
- Patient education material generation

### Research
- Adverse event surveillance and reporting
- Literature mining for DS mentions
- Effectiveness studies and meta-analyses
- Pharmacovigilance investigations

### Information Retrieval
- Standardized searching across DS resources
- Synonym resolution for varied naming
- Cross-database information integration
- Clinical note mining for DS usage

### Consumer and Provider Education
- Evidence-based supplement information
- Safety and interaction warnings
- Treatment effectiveness data
- Product ingredient transparency

## Technical Implementation

### Distribution Formats
1. **Neo4j Database**: Graph database format for relationship querying
2. **UMLS-style Flat Files**: Pipe-delimited text files for compatibility

### Build Process
- Automated data collection from sources
- Text preprocessing and cleaning
- Concept normalization via QuickUMLS
- Synonym matching and merging
- Relationship extraction and attribution
- Quality validation and accuracy assessment

### Maintenance
- Semantic versioning (MAJOR.MINOR.PATCH)
- Regular updates as sources change
- Continuous improvement of algorithms
- Community contributions via GitHub

## Access and Availability

- **Current Version**: Publicly available at https://doi.org/10.13020/d6bm3v
- **Source Code**: https://github.com/zhang-informatics/iDISK
- **Format**: Neo4j database and UMLS-style flat files
- **License**: Publicly available with permission from Therapeutic Research Center for NMCD content

## Integration with iBKH

iDISK serves as a component of the integrative Biomedical Knowledge Hub (iBKH), contributing DS knowledge to a larger integrated biomedical knowledge graph alongside:
- DRKG (Drug Repurposing Knowledge Graph)
- Multiple biomedical databases (BRENDA, CTD, DrugBank, KEGG, PharmGKB, Reactome, SIDER)
- Biological ontologies (GO, Uberon, CL, CHEBI)

## Publication

**Rizvi RF, Vasilakes J, Adam TJ, Melton GB, Bishop JR, Bian J, Zhang R.** "iDISK: the integrated DIetary Supplements Knowledge base." *J Am Med Inform Assoc.* 2020 Feb 18;27(4):539–548. doi: 10.1093/jamia/ocz216

## Information Resource ID

This resource has the Information Resource identifier: `infores:idisk`

For more information, see the publication at https://pmc.ncbi.nlm.nih.gov/articles/PMC7075538/ and access data at https://doi.org/10.13020/d6bm3v.
