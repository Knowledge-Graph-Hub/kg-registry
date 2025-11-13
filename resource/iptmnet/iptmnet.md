---
activity_status: active
category: DataSource
creation_date: '2025-11-13T00:00:00Z'
description: iPTMnet is an integrated resource for protein post-translational modification (PTM) network discovery that employs an integrative bioinformatics approach combining text mining, data mining, and ontological representation to capture rich PTM information, including PTM enzyme-substrate-site relationships, PTM-specific protein-protein interactions (PPIs), and PTM conservation across species.
domains:
  - proteomics
homepage_url: https://research.bioinformatics.udel.edu/iptmnet/
id: "iptmnet"
infores_id: "iptmnet"
last_modified_date: '2025-11-13T00:00:00Z'
layout: resource_detail
name: iPTMnet
products: []
publications:
- id: PMID:29145615
synonyms: []
---

# iPTMnet

## Description
iPTMnet is an integrated resource for protein post-translational modification (PTM) network discovery that employs an integrative bioinformatics approach combining text mining, data mining, and ontological representation to capture rich PTM information, including PTM enzyme-substrate-site relationships, PTM-specific protein-protein interactions (PPIs), and PTM conservation across species.

## Coverage
As of Release 4.1 (August 2017), iPTMnet contains:

- **654,500+** unique PTM sites in over **62,100** modified proteins
- **1,200** PTM enzymes
- **12,700** distinct enzyme-substrate pairs
- **24,300** distinct enzyme-substrate-site combinations
- **1,470** PTM-dependent protein-protein interactions
- **30,500** publications describing PTM and/or PPI relations

### PTM Types Covered
Eight major PTM types:
1. Phosphorylation (primary)
2. Ubiquitination
3. Acetylation
4. Methylation
5. Glycosylation
6. S-nitrosylation
7. Sumoylation
8. Myristoylation

### Organisms
Top organisms represented:
- Human
- Mouse
- Rat
- Arabidopsis thaliana
- Saccharomyces cerevisiae
- Schizosaccharomyces pombe

## Data Sources

### Text Mining Systems
- **RLIMS-P**: Rule-based information extraction system for literature mining of protein phosphorylation information from PubMed abstracts and full-length articles
- **eFIP**: Full-scale mining of PubMed Central Open Access articles for phosphorylation information

### Curated Databases (11 sources integrated)
1. **PhosphoSitePlus (PSP)**: Phosphorylation, ubiquitination, acetylation, methylation (human, rat, mouse)
2. **Phospho.ELM**: Phosphorylation sites in animal proteins
3. **PhosPhAt**: Mass spectrometry phosphorylation sites in Arabidopsis thaliana
4. **PhosphoGrid**: In vivo phosphorylation sites in Saccharomyces cerevisiae
5. **PomBase**: Fission yeast (Schizosaccharomyces pombe) comprehensive database
6. **UniProtKB**: Comprehensive protein database with expert-annotated PTM features
7. **P3DB**: Plant protein phosphorylation data
8. **neXtProt**: Human protein knowledgebase with kinase focus
9. **HPRD**: Human protein PTMs and enzyme-substrate relationships
10. **Signor**: Causal relationships between biological entities including PTM-enzyme substrate relations
11. **dbSNO**: Experimentally verified cysteine S-nitrosylation sites

### Ontological Framework
- **Protein Ontology (PRO)**: Organizes proteins and PTM proteoforms with hierarchical representation (family→gene→sequence→modification) enabling representation of experimentally validated PTM combinations

## Key Features

### Unique Capabilities
1. **Proteoform Representation**: Shows experimentally validated combinations of PTMs on proteins (unique feature)
2. **PTM Conservation Analysis**: Alignment of orthologous proteoforms across species enabling PTM site and proteoform prediction
3. **Confidence Scoring**: Quality scores (0-4 stars) for PTM information based on source quality, multiple source support, and publication evidence
4. **Network Visualization**: Cytoscape-based PTM sites and proteoforms as nodes with enzyme-site and PPI relationships as edges
5. **Integrated Text Mining**: Up-to-date PTM information from automated monthly processing of all PubMed abstracts and PMC Open Access full-text articles

### Search & Browse Functionality
- Search by UniProtKB AC/ID, protein/gene name, PRO ID, PMID
- Restrict by PTM type, enzyme/substrate role, organism
- **Batch Retrieval**: Process up to 500 PTM sites at once to obtain PTM enzyme or PTM-dependent PPI information
- **Literature Search**: Dual search modes (protein database search + phosphorylation literature search)
- Interactive Entry Reports with multiple data tables (substrate, PTM enzyme, proteoform, PPI)

### Visualization Tools
1. **Cytoscape Network View**: Interactive network visualization of PTM enzyme-substrate-site, proteoform-site, and PPI relationships
2. **Sequence Alignment Viewer**: Multiple sequence alignment (MUSCLE algorithm) showing PTM conservation across species with color-coded modifications
3. **Overlapping PTMs**: Highlights residues with multiple modification types (potential PTM cross-talk sites)

### RESTful API
- Programmatic access to iPTMnet data
- Documented in Methods Mol Biol (2022) and Database (Oxford) (2020)
- Enables automated integration with external analysis workflows

## Quality Control
- Monthly updates of text mining results
- Integrity checks on kinase information (verification against UniProtKB 'kinase' keyword)
- PTM type validation (conformance to known residue types)
- PTM site sequence validation (residue at expected position in UniProtKB sequence)
- Monitoring for retracted articles with correction/removal of affected data

## Applications
- Functional interpretation of phosphoproteomic data
- Kinase signaling pathway analysis (e.g., connecting phosphosites from mass spec experiments to kinase pathways)
- PTM-dependent PPI discovery
- Cross-species PTM conservation studies
- Drug target identification (e.g., EGFR inhibitor erlotinib response analysis)
- Hypothesis generation for PTM cross-talk and proteoform biology

## Maintenance & Support
- Maintained by Protein Information Resource (PIR)
- University of Delaware: 15 Innovation Way, Suite 205, Newark, DE 19711
- Georgetown University Medical Center: 3300 Whitehaven Street, NW, Suite 1200, Washington, DC 20007
- Funding: NSF grant ABI-1062520, NIH/NIGMS grant U01GM120953
- Website traffic: >6 million hits from >16,000 unique IPs (first half of 2017)

## Technical Implementation
- Database: Oracle 12c release 1, dimensional model design
- Front-end: Django (Python Web Framework)
- Visualization: Cytoscape.js (version 2.4.2 graph theory library)
- Sequence Alignment: MUSCLE algorithm
- Text Mining: PubTator for NCBI gene ID mapping
- ID Mapping: UniProt Protein ID and gene name mapping tools

## Access & Documentation
- Main Portal: [https://research.bioinformatics.udel.edu/iptmnet/](https://research.bioinformatics.udel.edu/iptmnet/)
- Statistics: [http://research.bioinformatics.udel.edu/iptmnet/stat](http://research.bioinformatics.udel.edu/iptmnet/stat)
- Help Documentation: Available online (PDF)
- Tutorial: [http://research.bioinformatics.udel.edu/iptmnet/static/iptmnet/files/iPTMnet_Help.pdf](http://research.bioinformatics.udel.edu/iptmnet/static/iptmnet/files/iPTMnet_Help.pdf)
- API Documentation: See publications PMID:35696082 and PMID:32395768
- Europe PubMed Central Integration: External link tab connection for literature cross-referencing
