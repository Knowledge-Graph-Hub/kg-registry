---
activity_status: inactive
category: Aggregator
creation_date: '2025-10-30T00:00:00Z'
description: iRefIndex is a consolidated protein interaction database that aggregates and indexes interaction data from multiple primary databases using sequence-based hash keys to identify and group redundant interaction records while maintaining provenance information.
domains:
  - proteomics
  - biological systems
id: irefindex
infores_id: irefindex
last_modified_date: '2025-10-30T00:00:00Z'
layout: resource_detail
name: iRefIndex
homepage_url: https://irefindex.vib.be/wiki/index.php/iRefIndex
publications:
  - id: PMID:18823568
    category: Publication
    preferred: true
  - id: PMID:22115179
    category: Publication
  - id: PMID:21975162
    category: Publication
warnings:
  - The iRefIndex website appears to be inactive as of 2025. Historical data and methods remain available through publications and may be accessible through archived versions.
products:
  - category: Product
    description: Historical consolidated protein interaction index in PSI-MITAB 2.5 format aggregating data from BIND, BioGrid, DIP, HPRD, IntAct, MINT, MPact, MPPI and OPHID
    format: psi_mi_mitab
    id: irefindex.database
    name: iRefIndex Database
    original_source:
      - bind
      - biogrid
      - dip
      - hprd
      - intact
      - mint
  - category: Product
    description: R package for accessing and manipulating iRefIndex data
    format: http
    id: irefindex.irefr
    name: iRefR Package
    original_source:
      - irefindex
  - category: Product
    description: Cytoscape plugin for visualization and data mining of iRefIndex protein interaction data
    id: irefindex.irefscape
    name: iRefScape
    original_source:
      - irefindex
  - category: GraphicalInterface
    description: Web interface for navigating the global protein-protein interaction landscape
    id: irefindex.irefweb
    name: iRefWeb
    original_source:
      - irefindex
---

# iRefIndex

## Overview

iRefIndex was a consolidated protein interaction database that provided a unified index for protein interaction data from multiple primary databases. The resource used sequence-based hash keys (computed using the Secure Hash Algorithm) to uniquely identify protein interaction records and group together redundant data, while carefully tracking the provenance of all integrated information.

**Note**: The iRefIndex website appears to be inactive as of 2025. However, the methodology and historical data remain valuable references for the field, and the consolidation approach influenced subsequent protein interaction data integration efforts.

## Key Innovation

iRefIndex introduced a rigorous method for:

1. **Generating unique keys** for protein interaction records based on protein primary sequences and taxonomy identifiers
2. **Identifying redundant groups** where multiple records describe the same molecular interaction
3. **Recording provenance** by tracking all consolidation operations with mapping scores
4. **Maintaining quality feedback** by reporting problematic references (malformed, deprecated, ambiguous, or unfound) back to source databases

## Integrated Databases

iRefIndex consolidated data from multiple primary interaction databases:

- BIND (Biomolecular Interaction Network Database)
- BioGrid
- DIP (Database of Interacting Proteins)
- HPRD (Human Protein Reference Database)
- IntAct
- MINT (Molecular INTeraction database)
- MPact
- MPPI
- OPHID

## Data Format

The consolidated interaction reference index was provided in **PSI-MITAB 2.5 format**, a standardized tabular format for molecular interactions developed by the HUPO Proteomics Standards Initiative.

## Associated Tools

- **iRefR**: R package for programmatic access and manipulation of iRefIndex data
- **iRefScape**: Cytoscape plugin for visualization and data mining
- **iRefWeb**: Web-based interface for navigating the protein-protein interaction landscape

## Use Cases

- Meta-analysis of protein interactions across multiple data sources
- Removing redundancy when combining interaction datasets
- Training and validation of interaction prediction methods
- Network analysis requiring comprehensive interaction data
- Referenced by major resources like GeneMANIA, Reactome, and STRING

## Historical Impact

iRefIndex was widely adopted by the bioinformatics community and influenced major resources including:
- GeneMANIA (gene function prediction)
- Reactome (pathway database)
- STRING (protein association networks)
- Various computational biology tools and methods

## Publications

The iRefIndex methodology and applications were described in multiple peer-reviewed publications:

1. **Main paper**: Razick S, Magklaras G, Donaldson IM. "iRefIndex: a consolidated protein interaction database with provenance." BMC Bioinformatics. 2008;9:405. PMID:18823568

2. **R package**: Mora A, Donaldson IM. "iRefR: an R package to manipulate the iRefIndex consolidated protein interaction database." BMC Bioinformatics. 2011;12:455. PMID:22115179

3. **Cytoscape plugin**: Razick S, Mora A, Michalickova K, Boddie P, Donaldson IM. "iRefScape. A Cytoscape plug-in for visualization and data mining of protein interaction data from iRefIndex." BMC Bioinformatics. 2011;12:388. PMID:21975162
