---
activity_status: inactive
category: Ontology
creation_date: '2025-10-30T00:00:00Z'
description: The Disease Ontology Annotation Framework (DOAF) was a semantic framework
  for representing and sharing disease annotations, enabling standardized disease
  ontology annotations across biomedical resources.
domains:
- biomedical
- clinical
id: doaf
infores_id: doaf
last_modified_date: '2026-02-20T00:00:00Z'
layout: resource_detail
name: Disease Ontology Annotation Framework
homepage_url: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0049686
synonyms:
- DOAF
- Disease Ontology Annotation Framework
publications:
- id: https://doi.org/10.1371/journal.pone.0049686
  title: 'The Disease Ontology: Structuring the Landscape of Human Disease'
  year: '2012'
products:
- category: DocumentationProduct
  description: PLOS ONE article describing the Disease Ontology Annotation Framework and its use for disease annotation.
  format: http
  id: doaf.framework-publication
  name: DOAF Framework Publication
  original_source:
  - doaf
  product_url: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0049686
taxon:
- NCBITaxon:9606
---

# Disease Ontology Annotation Framework

## Overview

The Disease Ontology Annotation Framework (DOAF) was a semantic framework designed to standardize disease annotations across biomedical databases and resources. Built on the Disease Ontology (DO), DOAF provided RDF-based representations for disease annotations, enabling machine-readable, interoperable disease data sharing across the biomedical research community.

## Key Concepts (Historical)

### Framework Components

- **RDF Schema**: Formal semantic representation of disease annotations
- **Standardized Vocabulary**: Controlled terms from the Disease Ontology
- **Annotation Properties**: Predicates for linking entities to diseases
- **Provenance Tracking**: Metadata about annotation sources and evidence
- **Version Control**: Temporal tracking of annotation changes

### Core Features

- **Semantic Web Compatibility**: RDF/OWL-based representations for linked data
- **Interoperability**: Common framework for disease annotations across resources
- **Machine Readability**: Structured data enabling computational analysis
- **Evidence Codes**: Standardized codes indicating annotation confidence and source
- **Cross-References**: Links to external disease identifiers and databases

## Applications (Historical)

- **Database Integration**: Standardizing disease annotations across biological databases
- **Literature Mining**: Representing disease-entity associations from publications
- **Clinical Systems**: Disease coding and terminology mapping
- **Knowledge Graphs**: Semantic representation of disease relationships
- **Comparative Analysis**: Cross-database disease annotation comparison

## Relationship to Disease Ontology

DOAF was closely tied to the Disease Ontology (DO):
- **DO**: Hierarchical classification of human diseases
- **DOAF**: Framework for annotating entities with DO terms
- Together, they provided both the vocabulary (DO) and the annotation mechanism (DOAF)

## Status

DOAF appears to be inactive as a standalone framework. Disease annotation efforts have been incorporated into:

### Current Alternatives

- **Disease Ontology (DO)**: Active development continues (https://disease-ontology.org/)
- **Mondo Disease Ontology**: Comprehensive disease ontology integrating multiple sources
- **OMIM**: Human genetic disease annotations
- **Orphanet**: Rare disease annotations
- **Human Phenotype Ontology (HPO)**: Disease-phenotype associations
- **EFO (Experimental Factor Ontology)**: Disease terms in experimental contexts

### Modern Approaches

Contemporary disease annotation frameworks use:
- Biolink Model for semantic standardization
- OBAN (Ontology of Biomedical Association Networks) for evidence representation
- SEPIO (Scientific Evidence and Provenance Information Ontology)
- Knowledge graph representations (RDF, OWL)

## Legacy Contributions

DOAF contributed to:
- Development of semantic disease annotation standards
- Integration of disease ontologies with biomedical databases
- Advancement of machine-readable disease representations
- Foundation for modern disease knowledge graphs

## Information Resource ID

This resource has the Information Resource identifier: `infores:doaf`

## References

- **Original Publication**: Schriml LM, et al. (2012). "Disease Ontology: a backbone for disease semantic integration." PLoS ONE 7(11):e49686. https://doi.org/10.1371/journal.pone.0049686

For current disease ontology work, see:
- Disease Ontology: https://disease-ontology.org/
- Mondo Disease Ontology: https://mondo.monarchinitiative.org/
