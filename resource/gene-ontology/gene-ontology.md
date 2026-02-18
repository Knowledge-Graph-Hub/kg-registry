---
activity_status: active
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://geneontology.org/
  id: gene-ontology-consortium
  label: Gene Ontology Consortium
creation_date: '2025-12-18T00:00:00Z'
description: The Gene Ontology (GO) is a major bioinformatics initiative to standardize
  the representation of gene and gene product attributes across species, databases,
  and data types. It provides controlled vocabularies (ontologies) for describing
  molecular functions, cellular components, and biological processes associated with
  gene products.
domains:
- biomedical
- biological systems
homepage_url: https://geneontology.org/
id: gene-ontology
last_modified_date: '2025-01-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Gene Ontology (GO)
products:
- category: OntologyProduct
  description: The main ontology in OWL. This is self contained and does not have
    connections to other OBO ontologies
  format: owl
  id: go.owl
  name: GO (OWL edition)
  product_url: http://purl.obolibrary.org/obo/go.owl
- category: OntologyProduct
  description: Equivalent to go.owl, in obo format
  format: obo
  id: go.obo
  name: GO (OBO Format edition)
  product_url: http://purl.obolibrary.org/obo/go.obo
- category: GraphicalInterface
  description: Gene Ontology web browser and search interface
  format: http
  id: gene-ontology.amigo
  is_public: true
  name: AmiGO 2
  product_url: http://amigo.geneontology.org/amigo
- category: ProgrammingInterface
  description: Gene Ontology API for programmatic access
  format: http
  id: gene-ontology.api
  is_public: true
  name: Gene Ontology API
  product_url: https://www.ebi.ac.uk/QuickGO/api/
- category: Product
  description: Gene Ontology Causal Activity Model (GO-CAM) annotations manually curated
    by Gene Ontology biocurators linking genes, proteins, and biological processes
  id: cam-kp.go-cams
  name: Gene Ontology CAMs
  original_source:
  - gene-ontology
repository: https://github.com/geneontology
synonyms:
- GO
taxon:
- NCBITaxon:all
---
# Gene Ontology (GO)

The Gene Ontology is one of the foundational resources in bioinformatics, providing standardized vocabularies to describe the functions, locations, and biological processes associated with gene products across all domains of life.

## Overview

The Gene Ontology (GO) project provides a set of dynamically controlled vocabularies that can be applied to all organisms. GO terms represent biological concepts, and the relationships between these terms provide a structured network of biological knowledge. GO annotations link gene products (proteins, RNAs, etc.) to GO terms, enabling systematic annotation and computational analysis.

## Three Main Components

- **Molecular Function**: Describes activities at the molecular level (e.g., catalytic activity, binding)
- **Biological Process**: Describes biological objectives (e.g., cell cycle, development, immune response)
- **Cellular Component**: Describes cellular structures and locations (e.g., nucleus, ribosome, membrane)

## Impact and Usage

GO is used by thousands of researchers and computational tools worldwide for:
- Functional annotation of genes and proteins
- Enrichment analysis in high-throughput biology
- Integration of biological information across databases
- Quality control of genome annotation
- Training and validation of machine learning models

## Key Features

- Community-driven curation with expert annotation
- Multiple ontology formats (OWL, OBO, RDF)
- Cross-species applicability (covers all organisms)
- Deep hierarchical structure for precise annotation
- Integration with other biological resources and ontologies