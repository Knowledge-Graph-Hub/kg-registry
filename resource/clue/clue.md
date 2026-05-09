---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://clue.io/about
    id: broad
    label: Broad Institute of MIT and Harvard
creation_date: '2025-08-12T00:00:00Z'
description: CLUE (formerly known as the Connectivity Map or CMap 2.0) is a comprehensive resource for connecting drugs, genes, and diseases through large-scale perturbational data. Built and maintained by the Broad Institute, CLUE provides access to over 1.3 million gene expression profiles from the LINCS L1000 assay, covering more than 42,000 perturbagens (drugs, genetic reagents, and other compounds) tested across multiple cell lines. The platform enables researchers to discover connections between diseases, drugs, and biological mechanisms through gene expression signatures.
domains:
  - drug discovery
  - genomics
  - biomedical
  - systems biology
homepage_url: https://clue.io/
id: clue
last_modified_date: '2025-10-07T00:00:00Z'
layout: resource_detail
name: CLUE
products:
  - category: Product
    description: Network embeddings of the Bioteque graph that represent biological entities and their associations
    id: bioteque.embeddings
    name: Bioteque Embeddings
    original_source:
      - source: chebi
        relation_type: prov:hadPrimarySource
      - source: cosmic
        relation_type: prov:hadPrimarySource
      - source: achilles
        relation_type: prov:hadPrimarySource
      - source: depmap
        relation_type: prov:hadPrimarySource
      - source: ccle
        relation_type: prov:hadPrimarySource
      - source: gdsc
        relation_type: prov:hadPrimarySource
      - source: cellosaurus
        relation_type: prov:hadPrimarySource
      - source: clue
        relation_type: prov:hadPrimarySource
      - source: ctd
        relation_type: prov:hadPrimarySource
      - source: pharmacodb
        relation_type: prov:hadPrimarySource
      - source: prism
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: lincs
        relation_type: prov:hadPrimarySource
      - source: compartments
        relation_type: prov:hadPrimarySource
      - source: offsides
        relation_type: prov:hadPrimarySource
      - source: sider
        relation_type: prov:hadPrimarySource
      - source: drugcentral
        relation_type: prov:hadPrimarySource
      - source: repohub
        relation_type: prov:hadPrimarySource
      - source: chemicalchecker
        relation_type: prov:hadPrimarySource
      - source: repodb
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
      - source: creeds
        relation_type: prov:hadPrimarySource
      - source: interpro
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: tissues
        relation_type: prov:hadPrimarySource
      - source: dorothea
        relation_type: prov:hadPrimarySource
      - source: progeny
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: hpa
        relation_type: prov:hadPrimarySource
      - source: go
        relation_type: prov:hadPrimarySource
      - source: corum
        relation_type: prov:hadPrimarySource
      - source: huri
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: omnipath
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: bto
        relation_type: prov:hadPrimarySource
    product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
    secondary_source:
      - source: bioteque
        relation_type: prov:wasInfluencedBy
repository: https://github.com/cmap
taxon:
  - NCBITaxon:9606
---

# CLUE

CLUE (Connectivity Map 2.0) is a next-generation platform for drug discovery and biological research that builds upon the original Connectivity Map project. Developed and maintained by the Broad Institute of MIT and Harvard, CLUE provides unprecedented access to large-scale perturbational gene expression data.

## Overview

CLUE hosts the world's largest collection of perturbational gene expression profiles, with over 1.3 million profiles generated using the LINCS L1000 high-throughput gene expression assay. The platform covers:

- **42,000+ perturbagens**: Including FDA-approved drugs, experimental compounds, genetic perturbations (shRNA, CRISPR), and other bioactive molecules
- **Multiple cell lines**: Expression data across diverse cellular contexts
- **Comprehensive coverage**: Systematic profiling of chemical and genetic perturbations

## Key Features

### Data Access
The CLUE platform provides free access to:
- Raw and processed L1000 gene expression data
- Pre-computed gene expression signatures
- Perturbagen metadata and annotations
- Cell line information

### Discovery Tools
CLUE offers sophisticated tools for:
- **Signature matching**: Find perturbagens that produce similar expression patterns
- **Target discovery**: Identify potential mechanisms of action
- **Drug repurposing**: Discover new therapeutic applications for existing drugs
- **Disease signature matching**: Connect disease states with potential therapeutic interventions

## Applications

CLUE enables researchers to:
- Discover unexpected connections between drugs, genes, and diseases
- Identify compounds that mimic or reverse disease signatures
- Understand mechanisms of action for drugs and genetic perturbations
- Prioritize drug candidates for development or repurposing
- Explore systems-level effects of perturbations

## Data Resources

CLUE provides multiple data access points through [clue.io/data](https://clue.io/data), including:
- Interactive web-based query tools
- Downloadable datasets
- API access for programmatic queries
- Pre-computed signature libraries

## Relationship to Connectivity Map

CLUE represents the evolution and expansion of the original Connectivity Map (CMap) project. While the original CMap provided proof-of-concept with approximately 7,000 expression profiles, CLUE has scaled the approach by orders of magnitude, providing a much more comprehensive resource for connecting perturbational biology.
