---
activity_status: active
category: DataSource
creation_date: '2025-11-19T00:00:00Z'
description: OWLSim is a Java library and set of command-line tools for calculating
  semantic similarity between ontology classes and individuals. Part of the OWLTools
  suite, OWLSim implements various semantic similarity algorithms including Information
  Content-based methods for comparing phenotypes, diseases, and other ontology-based
  profiles. It is extensively used by the Monarch Initiative for phenotype matching,
  disease gene prioritization, and model organism comparison. OWLSim enables researchers
  to find similar disease profiles, identify candidate genes based on phenotypic similarity,
  and connect human diseases with model organism phenotypes using semantic similarity
  metrics across biological ontologies.
domains:
- biomedical
- information technology
- phenotype
- genomics
- systems biology
homepage_url: https://github.com/owlcollab/owltools
id: owlsim
infores_id: owlsim
last_modified_date: '2025-11-19T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/BSD-3-Clause
  label: BSD-3-Clause
name: OWLSim Ontology Based Profile Matching
products:
- category: ProcessProduct
  description: Java library implementing semantic similarity algorithms for ontology-based
    profile matching
  id: owlsim.library
  name: OWLTools-Sim Library
  original_source:
  - owlsim
  product_url: https://github.com/owlcollab/owltools
- category: ProcessProduct
  description: Command-line tools for batch processing of semantic similarity calculations
  id: owlsim.cli
  name: OWLSim Command-Line Tools
  original_source:
  - owlsim
  product_url: https://github.com/owlcollab/owltools/releases
publications:
- id: PMID:18371930
  title: Walking the interactome for prioritization of candidate disease genes
  authors:
  - "K\xF6hler S"
  - Bauer S
  - Horn D
  - Robinson PN
  journal: American Journal of Human Genetics
  year: '2008'
  doi: 10.1016/j.ajhg.2008.02.013
repository: https://github.com/owlcollab/owltools
synonyms:
- OWLSim
taxon:
- NCBITaxon:9606
---

# OWLSim Ontology Based Profile Matching

OWLSim is a comprehensive toolkit for semantic similarity analysis using ontologies. Developed as part of the OWLTools suite, it provides sophisticated algorithms for comparing biological entities based on their ontological annotations, enabling researchers to find similar phenotypes, prioritize disease genes, and connect human diseases with model organism data.

## Key Features

- **Multiple Similarity Metrics**: Implements various semantic similarity algorithms including Resnik, Lin, and Jaccard-based measures
- **Information Content-Based Scoring**: Uses information content to weight ontology term importance
- **Ontology Agnostic**: Works with any OWL ontology including HPO, MP, GO, and others
- **Integrated with Monarch**: Powers phenotype matching in the Monarch Initiative
- **Java Library**: Can be embedded in applications for programmatic access
- **Command-Line Interface**: Supports batch processing and scripting workflows

## Applications

- **Disease Gene Prioritization**: Ranks candidate genes based on phenotypic similarity
- **Cross-Species Comparison**: Matches human disease phenotypes with model organism phenotypes
- **Patient Similarity**: Finds similar patients based on clinical features
- **Variant Interpretation**: Helps interpret genetic variants using phenotype information

## Information Resource ID

This resource has the Information Resource identifier: `infores:owlsim`
