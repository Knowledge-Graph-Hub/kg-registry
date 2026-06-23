---
activity_status: inactive
category: KnowledgeGraph
contacts:
  - category: Individual
    label: James P. McCusker
    contact_details:
      - contact_type: email
        value: mccusj@cs.rpi.edu
      - contact_type: url
        value: https://tw.rpi.edu/web/person/JamesMcCusker
  - category: Organization
    label: Tetherless World Constellation, Rensselaer Polytechnic Institute
    contact_details:
      - contact_type: url
        value: https://tw.rpi.edu/
creation_date: '2025-11-22T00:00:00Z'
description: ReDrugs is a probabilistic knowledge graph for drug repositioning that integrates drug-target, protein-protein, and disease-gene interactions from multiple databases. The system uses evidence-weighted nanopublications to assign confidence scores to interactions based on experimental methods and manual curation. ReDrugs was designed to identify novel drug candidates for diseases, particularly melanoma, by filtering and analyzing systems biology networks with probabilistic methods. The platform included both a web interface and API for exploring molecular interaction networks. The hosted web interface, API, and data archive (formerly at redrugs.tw.rpi.edu and data.rpi.edu) are no longer accessible; the source code remains available on GitHub.
domains:
  - drug discovery
  - systems biology
  - biomedical
  - pharmacology
homepage_url: https://github.com/dlmcguinness/redrugs
id: redrugs
last_modified_date: '2026-06-23T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: ReDrugs
products:
  - category: Product
    description: ReDrugS source code (TurboGears/SADI web application and probabilistic nanopublication pipeline). The hosted service it ran (redrugs.tw.rpi.edu) is no longer available.
    id: redrugs.source
    format: python
    name: ReDrugs Source Code
    original_source:
      - source: redrugs
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: irefindex
        relation_type: prov:hadPrimarySource
      - source: omim
        relation_type: prov:hadPrimarySource
      - source: cosmic
        relation_type: prov:hadPrimarySource
    product_url: https://github.com/dlmcguinness/redrugs
publications:
  - authors:
      - McCusker JP
      - Dumontier M
      - Yan R
      - He S
      - Dordick JS
      - McGuinness DL
    doi: 10.7717/peerj-cs.106
    id: doi:10.7717/peerj-cs.106
    journal: PeerJ Computer Science
    title: Finding melanoma drugs through a probabilistic knowledge graph
    year: '2017'
repository: https://github.com/dlmcguinness/redrugs
synonyms:
  - ReDrugS
taxon:
  - NCBITaxon:9606
---

# ReDrugs

## Overview

ReDrugs (Drug Repositioning through Semantic Integration) is a probabilistic knowledge graph platform designed to identify drug repositioning candidates by integrating and analyzing molecular interactions from multiple biological databases. The system combines drug-target interactions from DrugBank, protein-protein interactions from iRefIndex, gene ontology annotations from UniProt GOA, and disease-gene associations from OMIM and the COSMIC gene census.

The platform's key innovation is its use of nanopublications with evidence-based probabilistic scoring. Each interaction assertion is assigned a confidence probability based on either manual curation (p=0.999) or the quality of the experimental method used (ranging from p=0.8 to p=0.99). These probabilities are combined using composite Z-scores to provide overall confidence scores for complex interaction pathways.

ReDrugs was successfully applied to melanoma drug discovery, identifying 25 high-quality drug candidates with a joint probability ≥0.93 and ≤3 interaction steps from the disease. The system validated well, with nearly all predicted drugs having evidence from clinical trials or experimental studies.

**Note**: The hosted ReDrugs web interface, API, and data archive (formerly at redrugs.tw.rpi.edu and data.rpi.edu) are no longer accessible as of 2025. The source code remains available at [github.com/dlmcguinness/redrugs](https://github.com/dlmcguinness/redrugs).

## Key Features

- **Evidence-Weighted Knowledge Graph**: 6,180 drugs, 3,820 diseases, 69,279 proteins, and 899,198 interactions
- **Probabilistic Filtering**: Joint probability calculations for multi-step interaction paths
- **Semantic Web Standards**: Uses RDF, OWL, SPARQL, PROV-O, and SIO ontologies
- **Interactive Visualization**: Cytoscape.js-based network exploration with filtering controls
- **Nanopublication Architecture**: Each interaction captured with assertion, provenance, and publication metadata

## Data Sources

- **DrugBank**: Drug-target interactions (manual curation)
- **iRefIndex**: Protein-protein interactions and complexes
- **UniProt GOA**: Gene ontology annotations
- **OMIM**: Disease-gene associations
- **COSMIC Gene Census**: Cancer-gene associations

## Technical Architecture

- **Backend**: Blazegraph RDF database with SPARQL endpoint
- **Web Framework**: Python TurboGears with SADI web services
- **Frontend**: AngularJS with Cytoscape.js visualization
- **Data Format**: RDF nanopublications with PSI-MI and SIO ontologies

## Automated Evaluation

- View the automated evaluation: [redrugs automated evaluation](redrugs_eval_automated.html)
