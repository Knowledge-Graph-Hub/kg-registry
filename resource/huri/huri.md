---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://ccsb.dana-farber.org/
  label: Center for Cancer Systems Biology
- category: Individual
  label: Marc Vidal
  orcid: 0000-0002-9500-6065
- category: Individual
  label: Frederick P. Roth
creation_date: '2025-08-05T00:00:00Z'
description: The Human Reference Interactome (HuRI) is a comprehensive map of binary
  protein-protein interactions in human cells, generated through systematic high-throughput
  yeast two-hybrid screening. HuRI provides the largest experimentally verified collection
  of human protein interactions and serves as a foundational resource for understanding
  cellular networks and disease mechanisms.
domains:
- biomedical
- biological systems
- proteomics
- systems biology
homepage_url: https://www.interactome-atlas.org/
id: huri
infores_id: huri
last_modified_date: '2026-06-02T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: HuRI
products:
- category: GraphProduct
  description: Human Reference Interactome (HuRI) binary protein-protein interaction
    data from Luck et al. 2020.
  edge_count: 52569
  format: tsv
  id: huri.interactions
  latest_version: HuRI
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: HuRI Protein-Protein Interactions
  original_source:
  - relation_type: prov:hadPrimarySource
    source: huri
  product_file_size: 1681536
  product_url: https://www.interactome-atlas.org/data/HuRI.tsv
- category: GraphProduct
  description: Literature-curated high-quality protein-protein interactions from comparable
    experimental approaches, provided as the HuRI Lit-BM benchmark.
  edge_count: 13441
  format: tsv
  id: huri.literature_benchmark
  latest_version: Lit-BM
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: HuRI Literature Benchmark
  original_source:
  - relation_type: prov:hadPrimarySource
    source: huri
  product_file_size: 430112
  product_url: https://www.interactome-atlas.org/data/Lit-BM.tsv
- category: GraphProduct
  description: Human Reference Interactome (HuRI) binary protein-protein interaction
    data in PSI-MI format from Luck et al. 2020.
  edge_count: 52569
  format: psi_mi_mitab
  id: huri.interactions.psi
  latest_version: HuRI
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC BY 4.0
  name: HuRI Protein-Protein Interactions PSI-MI
  original_source:
  - relation_type: prov:hadPrimarySource
    source: huri
  product_file_size: 169848924
  product_url: https://www.interactome-atlas.org/data/HuRI.psi
- category: GraphicalInterface
  description: Web portal for searching and browsing human protein interactions
  format: http
  id: huri.portal
  name: HuRI Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: huri
  product_url: https://www.interactome-atlas.org/
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  format: mixed
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: achilles
  - relation_type: prov:hadPrimarySource
    source: bioteque
  - relation_type: prov:hadPrimarySource
    source: bto
  - relation_type: prov:hadPrimarySource
    source: ccle
  - relation_type: prov:hadPrimarySource
    source: cellosaurus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chemicalchecker
  - relation_type: prov:hadPrimarySource
    source: clue
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: corum
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: creeds
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: depmap
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: dorothea
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: huri
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: lincs
  - relation_type: prov:hadPrimarySource
    source: offsides
  - relation_type: prov:hadPrimarySource
    source: omnipath
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: pharmacodb
  - relation_type: prov:hadPrimarySource
    source: prism
  - relation_type: prov:hadPrimarySource
    source: progeny
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: repohub
  - relation_type: prov:hadPrimarySource
    source: sider
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tissues
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
- category: Product
  description: Current HuRI TSV file containing 52,569 systematically mapped binary
    human protein-protein interactions, provided as interacting Ensembl gene ID pairs
  format: tsv
  id: hrpimp.data
  latest_version: HuRI
  name: HuRI Protein-Protein Interaction Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: huri
  product_file_size: 1681536
  product_url: https://www.interactome-atlas.org/data/HuRI.tsv
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: gencode
  - relation_type: prov:wasInformedBy
    source: ensembl
  - relation_type: prov:wasInformedBy
    source: hgnc
- category: Product
  description: Current HuRI PSI-MI formatted interaction file with detailed experimental
    information and isoform-specific ORF, transcript, and protein identifiers
  format: psi_mi_mitab
  id: hrpimp.huri.psi
  latest_version: HuRI
  name: HuRI PSI-MI Interaction Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: huri
  product_file_size: 169848924
  product_url: https://www.interactome-atlas.org/data/HuRI.psi
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: gencode
  - relation_type: prov:wasInformedBy
    source: ensembl
- category: GraphicalInterface
  description: Web interface for browsing and exploring the Human Reference Interactome
  format: http
  id: hrpimp.web
  name: Interactome Atlas Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hrpimp
  - relation_type: prov:hadPrimarySource
    source: huri
  product_url: https://www.interactome-atlas.org/
publications:
- authors:
  - Katja Luck
  - Dae-Kyum Kim
  - Luke Lambourne
  - Kerstin Spirohn
  - et al.
  doi: 10.1038/s41586-020-2188-x
  id: doi:10.1038/s41586-020-2188-x
  journal: Nature
  preferred: true
  title: A reference map of the human binary protein interactome
  year: '2020'
repository: https://github.com/CCSB-DFCI/HuRI_paper
taxon:
- NCBITaxon:9606
---
# HuRI - Human Reference Interactome

The Human Reference Interactome (HuRI) represents the largest systematically generated map of binary protein-protein interactions in human cells. Developed at the Center for Cancer Systems Biology (CCSB) at Dana-Farber Cancer Institute, HuRI provides a foundational reference for understanding cellular networks, disease mechanisms, and biological processes.

## Overview

HuRI was created through systematic high-throughput yeast two-hybrid (Y2H) screening, testing pairwise combinations of human protein-coding genes to identify direct physical interactions. The project represents a landmark achievement in systems biology, providing unprecedented insight into the human protein interaction landscape.

### Current Statistics

**HuRI Database:**
- **52,569 protein-protein interactions** in the HuRI download
- **17,500 proteins** tested in the comprehensive search space

**Literature Benchmark:**
- **13,441 protein-protein interactions** curated from comparable experimental approaches

## Methodology and Quality Control

### Experimental Approach
HuRI interactions are identified using high-throughput yeast two-hybrid screens with rigorous quality control:

1. **Systematic Screening**: Pairwise testing of human protein-coding genes using standardized protocols
2. **Orthogonal Validation**: Multiple independent assay systems to confirm interactions
3. **Quality Assessment**: Systematic comparison with literature-curated interactions
4. **Reproducibility Testing**: Multiple replicates and independent validations

### Data Integration
The HuRI project integrates:
- Experimentally determined interactions from systematic screens
- Literature-curated interactions from comparable high-quality experiments
- Cross-references to major biological databases
- GENCODE gene, transcript, and protein annotations

## Research Impact and Applications

### Disease Research
HuRI has enabled groundbreaking research in:
- **Cancer Biology**: Understanding protein networks disrupted in cancer
- **Infectious Diseases**: Mapping host-pathogen interactions, including COVID-19 research
- **Genetic Disorders**: Identifying disease mechanisms through network analysis
- **Drug Discovery**: Finding new therapeutic targets and understanding drug mechanisms

### Network Biology
Key applications include:
- **Systems-level analysis** of cellular processes
- **Pathway reconstruction** and functional annotation
- **Evolutionary studies** of protein interaction networks
- **Prediction algorithms** for novel protein interactions

### Precision Medicine
HuRI contributes to:
- **Biomarker discovery** through network analysis
- **Patient stratification** based on network disruptions
- **Therapeutic targeting** of network components
- **Understanding drug resistance** mechanisms

## Collaborative Framework

HuRI is developed through collaboration between multiple research groups:

- **Vidal Lab** (Dana-Farber Cancer Institute) - Project leadership and Y2H screening
- **Roth Lab** (University of Toronto) - Computational analysis and validation
- **Tavernier Lab** (Ghent University) - Alternative interaction detection methods
- **Bader Lab** (University of Toronto) - Network analysis and bioinformatics

## Data Standards and Quality

### Experimental Standards
- Standardized Y2H protocols across all participating laboratories
- Systematic quality control measures
- Independent validation using orthogonal assays
- Comprehensive documentation of experimental conditions

### Data Annotation
- GENCODE-based gene and protein identifiers
- UniProt cross-references
- GO functional annotations
- Disease associations and pathway mappings

### Accessibility
- Open access under Creative Commons licensing
- Multiple download formats available
- Web-based search and visualization tools

## Technical Infrastructure

### Data Processing
- Automated quality control pipelines
- Standardized data formats
- Version control and data provenance tracking
- Integration with major biological databases

### Web Portal Features
- Interactive search interface
- Network visualization tools
- Bulk data download capabilities
- Cross-references to external resources

## Future Directions

Ongoing developments include:
- **Expansion of screening coverage** to achieve comprehensive proteome coverage
- **Integration with structural data** for mechanistic insights
- **Temporal and conditional interactions** under different cellular states
- **Cross-species comparative analysis** for evolutionary insights
- **Machine learning applications** for interaction prediction and validation

## Significance

HuRI represents a paradigm shift in understanding human cellular networks, providing:
- The most comprehensive experimentally validated human interactome
- A reference standard for computational prediction methods
- A foundation for systems-level understanding of human biology
- Critical insights into disease mechanisms and therapeutic opportunities

The resource continues to drive discoveries across multiple biological disciplines and serves as an essential tool for the global research community working to understand human health and disease.

---