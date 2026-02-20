---
activity_status: inactive
category: DataSource
creation_date: '2025-10-30T00:00:00Z'
description: iProClass was an integrated protein classification database that provided comprehensive annotations by integrating information from UniProt, PIR, and multiple external databases including protein family, function, pathway, and interaction data.
domains:
  - proteomics
id: "iproclass"
infores_id: "iproclass"
last_modified_date: '2026-02-20T00:00:00Z'
layout: resource_detail
name: iProClass
homepage_url: http://pir.georgetown.edu/iproclass/
synonyms:
  - iProClass
  - Integrated Protein Classification
products:
  - category: GraphicalInterface
    description: Historical iProClass web interface for integrated protein annotation lookup.
    format: http
    id: iproclass.portal
    name: iProClass Portal
    original_source:
      - iproclass
    product_url: http://pir.georgetown.edu/iproclass/
  - category: DocumentationProduct
    description: Protein Information Resource site with parent documentation and context for iProClass.
    format: http
    id: iproclass.pir-docs
    name: PIR Documentation
    original_source:
      - iproclass
    product_url: https://proteininformationresource.org/
---

# iProClass

## Overview

iProClass was an integrated protein classification and annotation database developed by the Protein Information Resource (PIR) at Georgetown University. It provided comprehensive protein information by integrating data from UniProt, PIR-PSD, and over 90 biological databases, offering a unified view of protein families, functions, pathways, structures, and interactions.

## Key Features (Historical)

- **Comprehensive Integration**: Unified protein annotations from 90+ databases
- **Protein Family Classification**: Links to InterPro, Pfam, PIRSF, and other family databases
- **Functional Annotations**: Gene Ontology terms, enzyme classifications, and pathway memberships
- **Structural Information**: PDB structures and structural classifications
- **Sequence Features**: Domain architecture, post-translational modifications, variants
- **Interaction Data**: Protein-protein and protein-small molecule interactions
- **Cross-References**: Extensive links to external protein databases
- **Proteome Analysis**: Tools for batch retrieval and proteome-scale analysis

## Data Content (Historical)

### Protein Classifications
- **Sequence-based families**: Pfam, PIRSF, TIGRFAMs
- **Structure-based families**: SCOP, CATH
- **Functional classifications**: Enzyme Commission (EC), Gene Ontology (GO)
- **Domain architectures**: InterPro domains and domain combinations

### Integrated Annotations
- Protein names and synonyms
- Gene names and symbols
- Taxonomic information
- Subcellular localization
- Tissue expression patterns
- Disease associations
- Bibliographic references

### External Database Links
- Sequence databases: UniProt, RefSeq, GenBank
- Structure databases: PDB, DSSP
- Family databases: InterPro, Pfam, SMART
- Pathway databases: KEGG, Reactome, BioCyc
- Interaction databases: IntAct, BioGRID, MINT
- Disease databases: OMIM, GeneCards

## Applications (Historical)

- **Protein Function Prediction**: Inferring function from family membership and homology
- **Comparative Proteomics**: Analyzing protein distributions across organisms
- **Systems Biology**: Integrating proteins into pathway and network contexts
- **Drug Discovery**: Identifying protein targets and understanding drug mechanisms
- **Structural Genomics**: Connecting sequences to structures and structural features

## Status

iProClass is no longer actively maintained. The PIR website indicates that the iProClass database has been discontinued. Users seeking integrated protein classification and annotation should consider:

### Alternative Resources
- **UniProt**: Comprehensive protein sequence and annotation database
- **InterPro**: Integrated protein family and domain classifications
- **PANTHER**: Protein family classifications with phylogenetic trees
- **Pfam**: Protein family database based on multiple sequence alignments
- **PIR**: Protein Information Resource (parent organization)

## Legacy Impact

iProClass contributed significantly to:
- Development of integrated protein annotation standards
- Cross-database mapping and identifier resolution
- Proteome-scale analysis methodologies
- Integration approaches for heterogeneous biological data

## Information Resource ID

This resource has the Information Resource identifier: `infores:iproclass`

## Historical Access

- **Former Homepage**: http://pir.georgetown.edu/iproclass/ (no longer active)
- **Parent Organization**: Protein Information Resource (PIR) - https://proteininformationresource.org/

For current integrated protein information, users should consult UniProt (https://www.uniprot.org/) and InterPro (https://www.ebi.ac.uk/interpro/).
