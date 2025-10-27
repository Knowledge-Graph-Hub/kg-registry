---
activity_status: active
category: Resource
creation_date: '2014-01-01T00:00:00Z'
description: RiboVision is a comprehensive webserver suite for visualization and analysis of ribosomal RNA structures, designed to integrate phylogenetic, structural, and evolutionary information about ribosomes in multiple dimensions. It provides interactive tools for exploring ribosomal RNA sequences, secondary structures, 3D structures, and associated data.
domains:
  - genomics
  - biological systems
homepage_url: https://ribovision2.chemistry.gatech.edu/
id: "ribovision"
last_modified_date: '2025-10-27T00:00:00Z'
layout: resource_detail
name: RiboVision
products:
  - category: GraphicalInterface
    description: Main web portal for RiboVision 2.0 with advanced visualization of RNA molecules
    format: http
    id: "ribovision.portal"
    name: RiboVision 2.0 Portal
    product_url: https://ribovision2.chemistry.gatech.edu/
  - category: GraphicalInterface
    description: Interactive phylogenetic browser for exploring ribosomal RNA sequences across 152 species
    format: http
    id: "ribovision.phylogeny-browser"
    name: Phylogenetic Browser
    product_url: https://ribovision2.chemistry.gatech.edu/
  - category: GraphicalInterface
    description: 2D RNA topology viewer for visualizing ribosomal RNA secondary structures
    format: http
    id: "ribovision.2d-viewer"
    name: 2D RNA Topology Viewer
    product_url: https://ribovision2.chemistry.gatech.edu/
  - category: GraphicalInterface
    description: MolStar-based 3D structure viewer for interactive exploration of ribosome structures
    format: http
    id: "ribovision.3d-viewer"
    name: 3D Structure Viewer
    product_url: https://ribovision2.chemistry.gatech.edu/
  - category: GraphicalInterface
    description: MSA viewer for exploring multiple sequence alignments of ribosomal RNA
    format: http
    id: "ribovision.msa-viewer"
    name: Alignment Viewer
    product_url: https://ribovision2.chemistry.gatech.edu/
  - category: Product
    description: Database of 152 ribosomal RNA sequences from the DESIRE dataset organized by phylogeny
    format: http
    id: "ribovision.sequences"
    name: rRNA Sequence Database
    product_url: https://ribovision2.chemistry.gatech.edu/
  - category: Product
    description: Multiple sequence alignments for ribosomal RNAs generated according to DESIRE methodology
    format: http
    id: "ribovision.alignments"
    name: rRNA Alignments
    product_url: https://ribovision2.chemistry.gatech.edu/
  - category: Product
    description: Pre-generated 2D layouts of ribosomal RNAs exported from PDBe API
    format: http
    id: "ribovision.2d-maps"
    name: 2D Structure Maps
    product_url: https://ribovision2.chemistry.gatech.edu/
  - category: Product
    description: 3D ribosome structures fetched from RCSB PDB with coordinate data
    format: http
    id: "ribovision.3d-structures"
    name: 3D Structure Data
    product_url: https://ribovision2.chemistry.gatech.edu/
  - category: Product
    description: RNA-protein contact data computed using BioPython NeighborSearch with 3.5Å cutoff
    format: http
    id: "ribovision.protein-contacts"
    name: RNA-Protein Contacts
    product_url: https://ribovision2.chemistry.gatech.edu/
  - category: Product
    description: Chemical modification data extracted from PDB CIF files
    format: http
    id: "ribovision.chemical-modifications"
    name: Chemical Modifications
    product_url: https://ribovision2.chemistry.gatech.edu/
  - category: Product
    description: Nucleotide frequency data from MSA columns with gap-adjusted probabilities
    format: http
    id: "ribovision.nucleotide-frequencies"
    name: Nucleotide Frequencies
    product_url: https://ribovision2.chemistry.gatech.edu/
  - category: Product
    description: Shannon entropy calculations for sequence conservation analysis
    format: http
    id: "ribovision.shannon-entropy"
    name: Shannon Entropy Data
    product_url: https://ribovision2.chemistry.gatech.edu/
  - category: Product
    description: TwinCons scores for two-group phylogenetic comparisons
    format: http
    id: "ribovision.twincons"
    name: TwinCons Comparison Data
    product_url: https://ribovision2.chemistry.gatech.edu/
  - category: Product
    description: Helix definitions and annotations for ribosomal RNA structures
    format: http
    id: "ribovision.helices"
    name: Helix Annotations
    product_url: https://ribovision2.chemistry.gatech.edu/
  - category: Product
    description: Expansion segment annotations from evolutionary accretion model
    format: http
    id: "ribovision.expansion-segments"
    name: Expansion Segment Annotations
    product_url: https://ribovision2.chemistry.gatech.edu/
  - category: DocumentationProduct
    description: About page with introduction to RiboVision 2 and contributors
    format: http
    id: "ribovision.about"
    name: About RiboVision
    product_url: https://apollo2.chemistry.gatech.edu/AboutRiboVision2/about/
  - category: DocumentationProduct
    description: Documentation for basic navigation and interface usage
    format: http
    id: "ribovision.basic-navigation"
    name: Basic Navigation Guide
    product_url: https://apollo2.chemistry.gatech.edu/AboutRiboVision2/basic_navigation/
  - category: DocumentationProduct
    description: Documentation for advanced features and analysis capabilities
    format: http
    id: "ribovision.advanced-features"
    name: Advanced Features Guide
    product_url: https://apollo2.chemistry.gatech.edu/AboutRiboVision2/Advanced_Features/
  - category: DocumentationProduct
    description: Detailed documentation about RiboVision data sources and computational methods
    format: http
    id: "ribovision.data-documentation"
    name: Data Documentation
    product_url: https://apollo2.chemistry.gatech.edu/AboutRiboVision2/ribovision_data/
  - category: DocumentationProduct
    description: User guide for upload mode with custom structures and alignments
    format: http
    id: "ribovision.user-upload-guide"
    name: User Upload Mode Guide
    product_url: https://apollo2.chemistry.gatech.edu/AboutRiboVision2/User_upload_Mode/
  - category: DocumentationProduct
    description: Gallery of examples demonstrating RiboVision capabilities
    format: http
    id: "ribovision.examples"
    name: Examples Gallery
    product_url: https://apollo2.chemistry.gatech.edu/AboutRiboVision2/examples/
publications:
  - authors:
      - Bernier
      - Petrov
      - Waterbury
      - Jett
      - Li
      - Freil
      - Xiong
      - Wang
      - Migliozzi
      - Hershkovits
      - Xue
      - Hsiao
      - Bowman
      - Harvey
      - Grover
      - Wartell
      - Williams
    id: "https://pubmed.ncbi.nlm.nih.gov/25340471/"
    journal: Faraday Discussions
    preferred: true
    title: RiboVision suite for visualization and analysis of ribosomes
    year: "2014"
  - authors:
      - Petrov
      - Bernier
      - Gulen
      - Waterbury
      - Hershkovits
      - Hsiao
      - Harvey
      - Hud
      - Fox
      - Wartell
      - Williams
    id: "https://pubmed.ncbi.nlm.nih.gov/24505437/"
    journal: PLoS One
    title: Secondary structures of rRNAs from all three domains of life
    year: "2014"
---

# RiboVision

RiboVision 2.0 is a comprehensive webserver suite designed for visualization and analysis of ribosomal RNA structures. Developed at the Center for the Origins of Life at Georgia Institute of Technology, RiboVision integrates phylogenetic, structural, and evolutionary information about ribosomes, enabling researchers to explore ribosomal RNA in multiple dimensions.

## Overview

RiboVision provides an integrated platform for exploring ribosomal RNA through multiple complementary views:
- **Phylogenetic organization**: Browse 152 species from the DESIRE database with taxonomic hierarchy
- **2D topology**: Interactive secondary structure diagrams with R2DT-based layouts
- **3D structures**: MolStar-based viewer for exploring atomic-level ribosome structures
- **Multiple sequence alignments**: Compare sequences across species with MSAViewer
- **Evolutionary data**: Map conservation, entropy, and functional annotations onto structures

## Key Features

### Visualization Tools
- **Phylogenetic Browser**: Navigate ribosomal RNA sequences organized by phylogenetic relationships
- **2D RNA Topology Viewer**: Explore secondary structures with base pairing and stacking interactions
- **3D Structure Viewer**: Interactive MolStar-based visualization of ribosome atomic structures
- **Alignment Viewer**: Examine multiple sequence alignments with gap-adjusted frequencies

### Data Analysis
- **Shannon Entropy**: Calculate and visualize sequence conservation across alignments
- **TwinCons**: Compare two phylogenetic groups using substitution matrix-based scoring
- **Nucleotide Frequencies**: Analyze base composition with gap-adjusted probabilities
- **RNA-Protein Contacts**: Identify interactions between rRNA and ribosomal proteins (3.5Å cutoff)
- **Chemical Modifications**: View post-transcriptional modifications from PDB data

### Structural Annotations
- **Helix Definitions**: Contiguous base-paired or stacked regions from Petrov et al. 2014
- **Expansion Segments**: Evolutionary accretion features from PNAS 2014-2015 studies
- **FR3D Base Pairs**: Leontis-Westhof notation for base pairing interactions

### User Upload Mode
- Upload custom 3D structures (PDB or CIF format)
- Provide custom alignments for mapping
- Visualize user data with RiboVision's analysis tools

## Data Sources

RiboVision integrates data from multiple authoritative sources:
- **Sequences**: NCBI, UniProt, RNAcentral (152 species from DESIRE dataset)
- **Phylogeny**: Tree topology from Banfield lab
- **3D Structures**: RCSB PDB via coordinate server API
- **2D Layouts**: EMBL-EBI PDBe API with R2DT secondary structures
- **Alignments**: Generated using DESIRE methodology
- **Base Pairs**: FR3D annotations from RNA 3D Hub

## Color Schemes

RiboVision employs matplotlib-based colormaps for data visualization:
- **Single continuum**: Viridis and rainbow colormaps for entropy, helices, and custom data
- **Diverging**: Blue-White-Red for TwinCons comparisons
- All colormaps exported to JavaScript using js-colormaps package

## Technical Implementation

- **License**: MIT license
- **Frontend**: React-based interface with custom viewers
- **RNA Topology**: Modified PDBe RNA viewer
- **MSA Visualization**: Modified react-msa-viewer
- **3D Rendering**: MolStar viewer with custom color wrapper
- **Sequence Processing**: BioPython for parsing and frequency calculations
- **Alignment Mapping**: MAFFT for sequence-alignment mapping

## Contributors

RiboVision 2 was developed by Holly McCann, Caeden Meade, and Anton S. Petrov at the Center for the Origins of Life, Georgia Institute of Technology, under the direction of Loren Dean Williams. Additional contributors include Petar I. Penev and Biswajit Banerjee.

## Funding

This work was funded by NASA grant 80NSSC18K1139 awarded to Loren Dean Williams and Anton S. Petrov.

## Contact

For questions about RiboVision 2, contact: RiboZones@gmail.com

RiboVision complements ProteoVision, a companion tool for visualizing ribosomal proteins.
