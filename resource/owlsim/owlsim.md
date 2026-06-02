---
activity_status: inactive
category: DataSource
creation_date: '2025-11-19T00:00:00Z'
description: OWLSim is ontology-based profile matching software for calculating semantic
  similarity between ontology classes and individuals. The tool was used by the
  Monarch Initiative and related phenotype-comparison projects, and has since
  been replaced by Semsimian.
domains:
  - biomedical
  - information technology
  - phenotype
  - genomics
  - systems biology
homepage_url: https://berkeleybop.org/software/owlsim/
id: owlsim
infores_id: owlsim
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
name: OWLSim Ontology Based Profile Matching
products:
  - category: ProcessProduct
    description: Java source repository for OWLSim v3 ontology-based profile matching
      and semantic similarity services
    format: http
    id: owlsim.v3
    name: OWLSim v3 Source Repository
    original_source:
      - source: owlsim
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/monarch-initiative/owlsim-v3
  - category: ProcessProduct
    description: OWLTools Java library and command-line tools historically associated
      with OWLSim workflows
    format: http
    id: owlsim.owltools
    name: OWLTools Source Repository
    original_source:
      - source: owlsim
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/owlcollab/owltools
  - category: ProgrammingInterface
    description: Local Dropwizard REST service documented by OWLSim v3 for ontology
      profile matching and matcher discovery
    format: http
    id: owlsim.rest
    name: OWLSim v3 REST Service
    original_source:
      - source: owlsim
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/monarch-initiative/owlsim-v3
    warnings:
      - The OWLSim v3 README documents a locally run REST service; no maintained
        public production endpoint was identified during 2026-06-02 curation.
publications:
  - id: PMID:24281164
    title: Improved exome prioritization of disease genes through cross-species phenotype
      comparison
    authors:
      - Robinson PN
      - Köhler S
      - Oellrich A
      - Wang K
      - Mungall CJ
      - Lewis SE
      - Washington N
      - Bauer S
      - Seelow D
      - Krawitz P
      - Gilissen C
      - Haendel M
      - Smedley D
    doi: 10.1101/gr.160325.113
    journal: Genome Research
    preferred: true
    year: '2014'
repository: https://github.com/monarch-initiative/owlsim-v3
synonyms:
  - OWLSim
taxon:
  - NCBITaxon:9606
warnings:
  - BBOP documents OWLSim as replaced by Semsimian; this entry describes the
    legacy OWLSim resource and its historical products.
---

# OWLSim Ontology Based Profile Matching

OWLSim is a legacy toolkit for semantic similarity analysis using ontologies. It
provided algorithms for comparing biological entities based on their ontological
annotations, supporting phenotype matching, candidate gene prioritization, and
cross-species model organism comparison. BBOP now documents Semsimian as the
replacement for OWLSim.

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

## Status

OWLSim remains registered as `infores:owlsim`, but the software is legacy and
has been superseded by Semsimian.
