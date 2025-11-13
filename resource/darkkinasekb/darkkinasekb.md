---
activity_status: active
category: DataSource
creation_date: '2025-11-13T00:00:00Z'
description: The Dark Kinase Knowledgebase (DKK) is a comprehensive resource focused
  on providing data and reagents for 162 poorly studied or 'dark' kinases to the broader
  research community. Supported through NIH's Illuminating the Druggable Genome (IDG)
  Program, the DKK collects and disseminates experimental and computational data that
  provides functional context for understudied kinases, including parallel reaction
  monitoring peptides, protein interactions, NanoBRET reagents, kinase-specific compounds,
  tissue expression profiles, and functional relationships.
domains:
- genomics
- proteomics
homepage_url: https://darkkinome.org
id: darkkinasekb
infores_id: darkkinasekb
last_modified_date: '2025-11-13T00:00:00Z'
layout: resource_detail
name: Dark Kinase Knowledgebase
products:
- category: Portal
  description: Main web portal for Dark Kinase Knowledgebase providing comprehensive
    data on 162 understudied kinases including tool compounds, PRM peptides, protein
    interactions, and expression profiles
  format: http
  id: darkkinasekb.portal
  name: DKK Main Portal
  original_source:
  - darkkinasekb
  product_url: https://darkkinome.org
- category: Browser
  description: Interactive expression browser showing tissue-specific expression of
    dark kinases using GTEx RNA-seq and Human Proteome Map data with kinome-wide comparisons
  format: http
  id: darkkinasekb.expression
  name: DKK Expression Browser
  original_source:
  - darkkinasekb
  product_url: http://expression.darkkinome.org/
- category: Dataset
  description: Parallel reaction monitoring (PRM) peptides for quantitative mass spectrometry
    of dark kinases with standard curves and detection limits
  format: http
  id: darkkinasekb.prm
  name: DKK PRM Peptides
  original_source:
  - darkkinasekb
  product_url: https://darkkinome.org/PRM_params
- category: Dataset
  description: Tool compounds for dark kinases with kinome-wide selectivity profiles
    and NanoBRET validation
  format: http
  id: darkkinasekb.compounds
  name: DKK Tool Compounds
  original_source:
  - darkkinasekb
  product_url: https://darkkinome.org/compounds
- category: Dataset
  description: Protein interaction networks for dark kinases from affinity purification
    mass spectrometry and proximity labeling experiments
  format: http
  id: darkkinasekb.interactions
  name: DKK Protein Interactions
  original_source:
  - darkkinasekb
  product_url: https://darkkinome.org
- category: Repository
  description: GitHub repository containing source code for Dark Kinase Knowledgebase
    website
  format: http
  id: darkkinasekb.github
  name: DKK GitHub Repository
  original_source:
  - darkkinasekb
  product_url: https://github.com/IDG-Kinase/darkkinasekb
- category: Dataset
  description: Bulk datasets and resources distributed through Synapse platform
  format: http
  id: darkkinasekb.synapse
  name: DKK Synapse Data Repository
  original_source:
  - darkkinasekb
  product_url: https://www.synapse.org/#!Synapse:syn18360482/files/
- category: GraphicalInterface
  description: Interactive web interface for exploring and visualizing kinase-substrate
    interactions
  format: http
  id: kinace.portal
  name: KinAce Web Portal
  original_source:
  - phosphositeplus
  - iptmnet
  - uniprot
  - epsd
  - kinhub
  - coralkinome
  - darkkinasekb
  - hgnc
  - kegg
  - interpro
  product_url: https://kinace.kinametrix.com/
  secondary_source:
  - kinace
publications:
- id: PMID:33079988
synonyms:
- DKK
---
# Dark Kinase Knowledgebase

## Description
The Dark Kinase Knowledgebase (DKK) is a comprehensive resource focused on providing data and reagents for 162 poorly studied or "dark" kinases to the broader research community. Supported through NIH's Illuminating the Druggable Genome (IDG) Program, the DKK collects and disseminates experimental and computational data that provides functional context for understudied kinases.

## Background
Nearly one-third of the ~500 human kinases lack sufficient understanding of their biological function. Despite this knowledge gap, recent work demonstrates the potential importance of these understudied kinases in multiple disease contexts. The IDG Kinase Data and Resource Generating Center (DRGC) was established to generate, systematize, and disseminate knowledge about dark kinases, the biological networks in which they function, and their connections to cellular phenotypes and human disease.

## Focus Kinases
Initial project focus on five exemplar kinases:
- **PKMYT1**: Protein kinase, membrane-associated tyrosine/threonine 1
- **TLK2**: Tousled-like kinase 2
- **BRSK2**: BR serine/threonine kinase 2
- **CDK12**: Cyclin-dependent kinase 12
- **CDK13**: Cyclin-dependent kinase 13

## Data Types Provided

### DRGC-Generated Data
1. **Parallel Reaction Monitoring (PRM) Peptides**: Unique peptides for quantitative proteomics enabling femtomolar resolution quantification of dark kinases via mass spectrometry, including:
   - Peptide sequences specific to each kinase
   - Standard curve assay performance data
   - Limit of detection information

2. **Small Molecule Inhibitors**: Kinase-specific compounds with comprehensive characterization:
   - Broad kinome scanning via KinomeScan assay (DiscoverX)
   - NanoBRET probe validation
   - Detailed inhibition properties and compound availability

3. **Physical Interaction Networks**: Protein-protein interactions derived from:
   - Affinity purification mass spectrometry (V5-tagged kinases)
   - Proximity labeling experiments (miniTurbo-tagged kinases)
   - Interactive Cytoscape.js-based network visualizations

4. **NanoBRET Reagents**: Tools for measuring kinase-compound interactions in living cells with detailed usage protocols

### External Integrated Data
- **GTEx Consortium**: Median gene-level TPM by tissue for expression profiling
- **Human Proteome Map**: Relative protein abundance across tissues
- **TCGA Data**: Cancer-specific information including:
  - Mutation data
  - mRNA expression levels
  - Copy number variations
- **PDB Structures**: 3D molecular structures visualized with NGL viewer
- **Functional Interaction Networks**: Integration via INDRA platform

## Key Features

### Individual Kinase Pages
Each of the 162 dark kinases has a dedicated page containing:
- Position in canonical kinase phylogenetic tree (via CORAL)
- PRM peptide calibration curves for mass spectrometry
- Interactive protein interaction networks
- Chemical tool compound summaries with purchase links
- TCGA heatmaps (mutations, copy number, mRNA expression)
- Tissue expression profiles from DKK Expression Browser
- Links to complementary resources (Pharos, GeneCards, Monarch Initiative)

### DKK Expression Browser
Interactive web application ([http://expression.darkkinome.org/](http://expression.darkkinome.org/)) featuring:
- RNAseq data from GTEx Consortium
- Mass spectrometry-based protein abundance from Human Proteome Map
- Kinome-specific expression comparisons
- Organ-by-organ percentile rankings
- Anatogram visualizations showing tissue-specific expression
- Correlation analysis with well-studied kinases
- Interactive data filtering and export capabilities

**Expression Insights:**
- MKNK2 has highest average organ expression
- PSKH2 has lowest average organ expression
- Brain regions show generally higher dark kinase expression levels

### Affiliated Tools
1. **CORAL**: Kinase tree visualization tool for phylogenetic context
2. **Clinical Kinase Index**: Focuses on kinase roles in cancer
3. **IDG Reactome**: Pathway analysis centered on understudied proteins
4. **Small Molecule Suite**: Toolkit for kinase inhibitor selection

## Search and Navigation
- Search functionality with fuzzy matching for partial kinase name queries
- Browse by kinase or organ system
- Downloadable datasets in CSV format
- Consolidated compound and PRM peptide tables

## Technical Implementation
- **Server**: Red Hat Linux with Apache HTTP server
- **Framework**: Dancer2 web application framework (Perl)
- **Visualization**: 
  - D3.js for interactive charts
  - R Shiny framework for expression browser
  - gganatogram for anatomical visualizations
  - Cytoscape.js for network diagrams
  - NGL viewer for 3D protein structures
- **Search**: Text::Fuzzy Perl module for fuzzy matching
- **HTTPS**: Let's Encrypt certificate

## Data Quality & Standards
- PRM peptides selected using CPTAC consortium guidelines
- Small molecule inhibitor identification guided by community-developed criteria
- Detailed methods documentation available on-site for NanoBRET probes and protocols

## Code and Data Availability
- **Main Repository**: [https://github.com/IDG-Kinase/darkkinasekb](https://github.com/IDG-Kinase/darkkinasekb)
- **Expression Browser Code**: [https://github.com/IDG-Kinase/kinase_expression](https://github.com/IDG-Kinase/kinase_expression)
- **Group Projects**: [https://github.com/IDG-Kinase](https://github.com/IDG-Kinase)
- **Bulk Data Distribution**: Synapse platform ([https://www.synapse.org/#!Synapse:syn18360482/files/](https://www.synapse.org/#!Synapse:syn18360482/files/))

## Consortium & Funding
**IDG-Kinase Data and Resource Generating Center:**
- University of North Carolina (UNC): Gary Johnson, Tim Willson
- Washington University at St Louis (WUSTL): Ben Major, Reid Townsend
- Harvard Medical School: Peter K. Sorger

**Funding:** NIH Illuminating the Druggable Genome Program [U24DK116204]

## Future Directions
Ongoing DRGC efforts include:
- Expanding chemical tools, physical/functional interaction networks, and PRM peptides across all 162 dark kinases
- Transcriptional profiling in response to kinase inhibitor treatment
- Kinome-wide activity measurements post-inhibitor treatment
- Machine learning algorithms for predicting novel kinase inhibitors
- Integration with external tools like KinView

## Applications
- Discovery of novel druggable targets for therapeutic development
- Understanding kinase function in disease contexts (cancer, infectious disease, immune disorders)
- Functional annotation of understudied kinases
- Development of kinase-specific research tools
- Systems-level analysis of kinase signaling networks

## Citation
Berginski ME, Moret N, Liu C, Goldfarb D, Sorger PK, Gomez SM. The Dark Kinase Knowledgebase: an online compendium of knowledge and experimental results of understudied kinases. Nucleic Acids Research, 2021. doi: 10.1093/nar/gkaa853