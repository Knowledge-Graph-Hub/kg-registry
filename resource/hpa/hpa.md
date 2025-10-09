---
activity_status: active
category: Aggregator
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: contact@proteinatlas.org
      - contact_type: url
        value: https://www.proteinatlas.org/about/organization
    label: Human Protein Atlas Team
creation_date: '2025-10-09T00:00:00Z'
description: The Human Protein Atlas (HPA) is a Swedish-based program aiming to map all human proteins in cells, tissues and organs using an integration of various omics technologies, including antibody-based imaging, mass spectrometry-based proteomics, transcriptomics and systems biology. The HPA aggregates and presents data from eight different resources covering tissue, brain, single cell, subcellular, cancer, blood, cell line, and structure & interaction atlases.
domains:
  - biomedical
  - proteomics
  - genomics
  - anatomy and development
  - health
homepage_url: https://www.proteinatlas.org/
id: hpa
last_modified_date: '2025-10-09T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/3.0/
  label: CC-BY-SA-3.0
name: Human Protein Atlas
products:
  - category: GraphicalInterface
    description: Main web portal for exploring protein expression profiles across tissues, cells, and disease states
    format: http
    id: hpa.portal
    name: Human Protein Atlas Portal
    product_url: https://www.proteinatlas.org/
  - category: Product
    description: Complete Human Protein Atlas data in TSV format, version 24.1
    format: tsv
    id: hpa.proteinatlas.tsv
    name: HPA Complete Data (TSV)
    product_url: https://www.proteinatlas.org/download/proteinatlas.tsv.zip
  - category: Product
    description: Complete Human Protein Atlas data in JSON format, version 24.1
    format: json
    id: hpa.proteinatlas.json
    name: HPA Complete Data (JSON)
    product_url: https://www.proteinatlas.org/download/proteinatlas.json.gz
  - category: Product
    description: Complete Human Protein Atlas data in XML format, version 24.0 with comprehensive protein expression and annotation data
    format: xml
    id: hpa.proteinatlas.xml
    name: HPA Complete Data (XML)
    product_url: https://www.proteinatlas.org/download/proteinatlas.xml.gz
  - category: Product
    description: Normal tissue expression data based on immunohistochemistry using tissue microarrays
    format: tsv
    id: hpa.normal_tissue
    name: HPA Normal Tissue Data
    product_url: https://www.proteinatlas.org/download/normal_tissue.tsv.zip
  - category: Product
    description: Pathology data including cancer tissue expression and patient survival information
    format: tsv
    id: hpa.pathology
    name: HPA Pathology Data
    product_url: https://www.proteinatlas.org/download/pathology.tsv.zip
  - category: Product
    description: Subcellular localization data based on immunofluorescent staining of human cell lines
    format: tsv
    id: hpa.subcellular_location
    name: HPA Subcellular Location Data
    product_url: https://www.proteinatlas.org/download/subcellular_location.tsv.zip
  - category: Product
    description: RNA expression data in human tissues based on transcriptomic analysis
    format: tsv
    id: hpa.rna_tissue
    name: HPA RNA Tissue Expression Data
    product_url: https://www.proteinatlas.org/download/rna_tissue.tsv.zip
  - category: Product
    description: RNA expression data in human cell lines based on RNA-seq analysis
    format: tsv
    id: hpa.rna_celline
    name: HPA RNA Cell Line Expression Data
    product_url: https://www.proteinatlas.org/download/rna_celline.tsv.zip
  - category: Product
    description: Single cell expression data from human tissues based on scRNA-seq analysis
    format: tsv
    id: hpa.rna_single_cell
    name: HPA Single Cell RNA Expression Data
    product_url: https://www.proteinatlas.org/download/rna_single_cell.tsv.zip
  - category: Product
    description: Brain-specific expression data including regional and cellular distribution
    format: tsv
    id: hpa.brain_rna
    name: HPA Brain RNA Expression Data
    product_url: https://www.proteinatlas.org/download/brain_rna.tsv.zip
  - category: Product
    description: Blood protein expression data from healthy individuals and disease states
    format: tsv
    id: hpa.blood_protein
    name: HPA Blood Protein Data
    product_url: https://www.proteinatlas.org/download/blood_protein.tsv.zip
  - category: Product
    description: Immune cell expression data from single cell transcriptomics studies
    format: tsv
    id: hpa.rna_immune_cell
    name: HPA Immune Cell RNA Data
    product_url: https://www.proteinatlas.org/download/rna_immune_cell.tsv.zip
  - category: ProgrammingInterface
    description: Programmatic access to individual protein entries in XML format via Ensembl ID
    format: xml
    id: hpa.api.xml
    name: HPA XML API
    product_url: https://www.proteinatlas.org/about/download
  - category: ProgrammingInterface
    description: Programmatic access to individual protein entries in TSV format via Ensembl ID
    format: tsv
    id: hpa.api.tsv
    name: HPA TSV API
    product_url: https://www.proteinatlas.org/about/download
  - category: ProgrammingInterface
    description: Programmatic access to individual protein entries in JSON format via Ensembl ID
    format: json
    id: hpa.api.json
    name: HPA JSON API
    product_url: https://www.proteinatlas.org/about/download
  - category: ProgrammingInterface
    description: Programmatic access to individual protein entries in RDF format via Ensembl ID
    format: rdfxml
    id: hpa.api.rdf
    name: HPA RDF API
    product_url: https://www.proteinatlas.org/about/download
publications:
  - authors:
      - Uhlén M
      - Fagerberg L
      - Hallström BM
      - Lindskog C
      - Oksvold P
      - Mardinoglu A
    doi: 10.1126/science.1260419
    id: doi:10.1126/science.1260419
    journal: Science
    title: Tissue-based map of the human proteome
    year: '2015'
  - authors:
      - Karlsson M
      - Zhang C
      - Méar L
      - Zhong W
      - Digre A
      - Katona B
    doi: 10.1126/science.aal3321
    id: doi:10.1126/science.aal3321
    journal: Science
    title: A single-cell type transcriptomics map of human tissues
    year: '2021'
repository: https://github.com/human-protein-atlas
---

# Human Protein Atlas

The Human Protein Atlas (HPA) is a comprehensive Swedish-based program that aims to map all human proteins in cells, tissues, and organs using integration of various omics technologies. As one of the world's largest proteomics initiatives, HPA aggregates and presents data from multiple sources to create a comprehensive resource for understanding human protein expression and localization.

## About the Human Protein Atlas

The Human Protein Atlas integrates antibody-based imaging, mass spectrometry-based proteomics, transcriptomics, and systems biology to provide a comprehensive view of the human proteome. The resource is organized into eight interconnected atlases, each focusing on different aspects of protein biology.

### Key Features

- **Comprehensive Coverage**: Maps protein expression across tissues, cells, and disease states
- **Multi-modal Data**: Integrates antibody-based imaging, RNA-seq, mass spectrometry, and single-cell data
- **Open Access**: All data freely available under Creative Commons licensing
- **Regular Updates**: Quarterly releases with new data and improved annotations
- **Multiple Formats**: Data accessible via web portal, bulk downloads, and programmatic APIs

## Eight Atlas Resources

### 1. Tissue Atlas
Protein and RNA expression profiles in normal human tissues based on antibodies and transcriptomics, covering:
- 44 normal tissue types
- Over 15,000 protein-coding genes
- Immunohistochemistry and RNA-seq data

### 2. Brain Atlas
Detailed protein and spatial RNA expression profiles in the human brain:
- Regional brain expression mapping
- Cellular distribution in brain regions
- Neurological disease associations

### 3. Single Cell Atlas
Comprehensive single-cell RNA expression profiles across tissues:
- 700+ cell types across human tissues
- Single-cell transcriptomics data
- Cell type-specific expression patterns

### 4. Subcellular Atlas
Spatial subcellular protein localization in human cells:
- Immunofluorescence microscopy
- Organelle-specific protein distribution
- Subcellular compartment mapping

### 5. Cancer Atlas
Protein and RNA profiles in human cancers:
- 17 major cancer types
- Prognostic significance analysis
- Cancer-specific expression patterns

### 6. Blood Atlas
Blood protein levels in health and disease:
- Plasma protein concentrations
- Disease-specific protein signatures
- Longitudinal studies across age groups

### 7. Cell Line Atlas
RNA expression profiles in human cell lines:
- Cancer cell line models
- Tissue-specific cell line collections
- Comparative expression analysis

### 8. Structure & Interaction Atlas
3D protein structures, interaction networks, and metabolic pathways:
- Protein structure predictions
- Protein-protein interaction networks
- Metabolic pathway integration

## Data Types and Formats

### Expression Data
- **Tissue Expression**: Immunohistochemistry-based protein expression
- **RNA Expression**: Transcriptomic data from RNA-seq analyses
- **Single Cell**: scRNA-seq expression profiles
- **Blood Proteins**: Mass spectrometry-based plasma protein levels

### Localization Data
- **Subcellular**: Immunofluorescence-based protein localization
- **Tissue Distribution**: Organ and tissue-specific expression patterns
- **Disease Context**: Pathological expression changes

### Data Formats
- **Bulk Downloads**: Complete datasets in TSV, JSON, and XML formats
- **Individual Entries**: Per-protein data via RESTful APIs
- **Integrated Views**: Web-based visualization and exploration tools

## Applications

The Human Protein Atlas serves multiple research communities:

### Biomedical Research
- Disease biomarker discovery
- Drug target identification
- Therapeutic development support

### Basic Biology
- Protein function annotation
- Cellular localization studies
- Comparative proteomics

### Clinical Applications
- Diagnostic marker development
- Prognostic indicator identification
- Precision medicine approaches

## Data Access

### Web Portal
Interactive exploration of protein expression data with advanced search and filtering capabilities.

### Bulk Downloads
Complete datasets available in multiple formats for computational analysis and integration.

### Programmatic Access
RESTful APIs for automated data retrieval using Ensembl gene identifiers.

### Integration
Data integrated into major biological databases and analysis platforms.

## Citation and Licensing

All Human Protein Atlas data is freely available under the Creative Commons Attribution-ShareAlike 3.0 International License. Users are encouraged to cite the appropriate HPA publications when using the data in research.
