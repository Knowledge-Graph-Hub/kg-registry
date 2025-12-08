---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: chembl-help@ebi.ac.uk
  - contact_type: url
    value: https://chembl.gitbook.io/unichem
  id: ebi
  label: ChEMBL Team at EMBL-EBI
creation_date: '2025-11-04T00:00:00Z'
description: UniChem is a large-scale non-redundant database maintained by EMBL-EBI
  that provides cross-references between chemical structures across multiple chemistry
  resources. It serves as a unified system for creating and maintaining structure-based
  hyperlinks between chemistry databases, particularly optimized for on-the-fly link
  creation via REST web services. UniChem aggregates compound identifiers from major
  chemistry resources including ChEMBL, ChEBI, SureChEMBL, PubChem, DrugBank, and
  many others, enabling efficient cross-database chemical structure queries using
  InChI, InChIKey, or source-specific identifiers.
domains:
- chemistry and biochemistry
- drug discovery
- pharmacology
homepage_url: https://www.ebi.ac.uk/unichem/
id: unichem
infores_id: unichem
last_modified_date: '2025-11-04T00:00:00Z'
layout: resource_detail
name: UniChem
products:
- category: GraphicalInterface
  description: Web-based search interface for finding compound sources and performing
    connectivity searches across chemical databases
  format: http
  id: unichem.search
  name: UniChem Search Interface
  original_source:
  - unichem
  product_url: https://www.ebi.ac.uk/unichem/search
- category: ProgrammingInterface
  description: RESTful web services API for programmatic access to UniChem cross-references
    and connectivity searches
  format: http
  id: unichem.api
  name: UniChem REST API
  original_source:
  - unichem
  product_url: https://www.ebi.ac.uk/unichem/api/docs
- category: Product
  description: Comprehensive list of all integrated chemistry databases and their
    metadata in UniChem
  format: http
  id: unichem.sources
  name: UniChem Source Database List
  original_source:
  - unichem
  product_url: https://www.ebi.ac.uk/unichem/sources
- category: DocumentationProduct
  description: Complete documentation covering UniChem functionality, API usage, data
    model, and integration guidelines
  format: http
  id: unichem.docs
  name: UniChem Documentation
  original_source:
  - unichem
  product_url: https://chembl.gitbook.io/unichem
synonyms:
- unichem
---

# UniChem

## Overview

UniChem is a unified chemical identifier cross-reference system developed and maintained by EMBL-EBI. It provides a large-scale, non-redundant database of pointers between chemical structures and chemistry resources, with particular focus on EMBL-EBI chemistry databases and services.

## Primary Purpose

UniChem is designed to optimize the efficiency with which structure-based hyperlinks can be built and maintained between chemistry-based resources. The system is particularly suitable for creating such links "on the fly" through REST web services, making it ideal for dynamic web applications and data integration pipelines.

## Integrated Resources

UniChem primarily serves to maintain cross-references between:

**Primary Chemistry Resources:**
- ChEMBL (bioactive drug-like small molecules)
- ChEBI (Chemical Entities of Biological Interest)
- SureChEMBL (chemistry from patent documents)

**Other EBI Resources with Chemical Data:**
- Gene Expression Atlas
- PDBe (Protein Data Bank in Europe)

**External Chemistry Databases:**
- PubChem
- DrugBank
- ZINC
- Many other chemistry and drug databases

## Key Features

### Connectivity Search
UniChem's connectivity search allows users to find all source identifiers for compounds that share the same molecular connectivity (based on standard InChI representation). This enables:
- Discovery of the same compound across multiple databases
- Identification of alternative identifiers for the same structure
- Cross-database structure queries

### Compound Source Search
Find all databases that contain information about a specific compound using:
- Source-specific database IDs
- InChI (International Chemical Identifier)
- InChIKey (hashed version of InChI)
- UCI (UniChem Compound Identifier)

### REST API
The UniChem API provides programmatic access for:
- Batch structure lookups
- Real-time cross-reference retrieval
- Integration into computational workflows
- Building automated data pipelines

## Use Cases

1. **Cross-Database Linking**: Creating hyperlinks between chemical databases
2. **Data Integration**: Merging chemical information from multiple sources
3. **Structure Searching**: Finding the same compound across different repositories
4. **Identifier Translation**: Converting between different chemical identifier systems
5. **Resource Discovery**: Identifying which databases contain information about specific compounds

## Information Resource ID

This resource has the Information Resource identifier: `infores:unichem`

## Technical Details

- **Structure Representation**: Uses standard InChI for chemical structure matching
- **Connectivity Matching**: Based on first connectivity layer of InChI
- **Update Frequency**: Regular updates from source databases
- **Access Methods**: Web interface and REST API