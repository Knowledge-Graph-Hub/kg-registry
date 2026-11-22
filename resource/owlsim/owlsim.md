---
activity_status: inactive
category: DataSource
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: cjmungall@lbl.gov
      - contact_type: github
        value: cmungall
    label: Chris Mungall
    orcid: 0000-0002-6601-2165
creation_date: '2025-11-19T00:00:00Z'
description: OWLSim is ontology-based profile matching software for calculating semantic similarity between ontology classes and individuals. The tool was used by the Monarch Initiative and related phenotype-comparison projects, and has since been replaced by Semsimian.
domains:
  - biomedical
  - information technology
  - phenotype
  - genomics
  - systems biology
homepage_url: https://berkeleybop.org/software/owlsim/
id: owlsim
infores_id: owlsim
last_modified_date: '2026-11-22T00:00:00Z'
layout: resource_detail
name: OWLSim Ontology Based Profile Matching
products:
  - category: ProcessProduct
    description: Java source repository for OWLSim v3 ontology-based profile matching and semantic similarity services
    format: http
    id: owlsim.v3
    name: OWLSim v3 Source Repository
    original_source:
      - source: owlsim
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/monarch-initiative/owlsim-v3
  - category: ProcessProduct
    description: OWLTools Java library and command-line tools historically associated with OWLSim workflows
    format: http
    id: owlsim.owltools
    name: OWLTools Source Repository
    original_source:
      - source: owlsim
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/owlcollab/owltools
  - category: ProgrammingInterface
    description: Local Dropwizard REST service documented by OWLSim v3 for ontology profile matching and matcher discovery
    format: http
    id: owlsim.rest
    name: OWLSim v3 REST Service
    original_source:
      - source: owlsim
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/monarch-initiative/owlsim-v3
    warnings:
      - The OWLSim v3 README documents a locally run REST service; no maintained public production endpoint was identified during 2026-06-02 curation or the 2026-11-22 recheck.
publications:
  - preferred: true
    id: doi:10.1101/gr.160325.113
    doi: 10.1101/gr.160325.113
    title: Improved exome prioritization of disease genes through cross-species phenotype comparison
    authors:
      - Peter N. Robinson
      - Sebastian Köhler
      - Anika Oellrich
      - Kai Wang
      - Christopher J. Mungall
      - Suzanna E. Lewis
      - Nicole Washington
      - Sebastian Bauer
      - Dominik Seelow
      - Peter Krawitz
      - Christian Gilissen
      - Melissa Haendel
      - Damian Smedley
    journal: Genome Research
    year: '2014'
  - id: doi:10.1093/database/bat025
    doi: 10.1093/database/bat025
    title: 'PhenoDigm: analyzing curated annotations to associate animal models with human diseases'
    authors:
      - D. Smedley
      - A. Oellrich
      - S. Kohler
      - B. Ruef
      - M. Westerfield
      - P. Robinson
      - S. Lewis
      - C. Mungall
    journal: Database
    year: '2013'
  - id: doi:10.1002/humu.22051
    doi: 10.1002/humu.22051
    title: 'MouseFinder: Candidate disease genes from mouse phenotype data'
    authors:
      - Chao-Kung Chen
      - Christopher J. Mungall
      - Georgios V. Gkoutos
      - Sandra C. Doelken
      - Sebastian Köhler
      - Barbara J. Ruef
      - Cynthia Smith
      - Monte Westerfield
      - Peter N. Robinson
      - Suzanna E. Lewis
      - Paul N. Schofield
      - Damian Smedley
    journal: Human Mutation
    year: '2012'
repository: https://github.com/monarch-initiative/owlsim-v3
rrid: SCR_006819
synonyms:
  - OWLSim
  - OwlSim
  - owlsim-v3
taxon:
  - NCBITaxon:9606
  - NCBITaxon:10090
  - NCBITaxon:7955
warnings:
  - BBOP documents OWLSim as replaced by Semsimian; this entry describes the legacy OWLSim resource and its historical products.
  - The owlsim-v3 repository has had no commits since May 2022. The former homepage domain owlsim.org (still listed in the SciCrunch record) now hosts an unrelated site and should not be used.
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
