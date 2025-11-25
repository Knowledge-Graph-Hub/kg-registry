---
activity_status: unknown
category: DataSource
creation_date: '2025-10-30T00:00:00Z'
description: STARGEO is a gene expression search application that enables researchers to search and analyze gene expression data from the Gene Expression Omnibus (GEO) repository using statistical methods to identify differentially expressed genes and relevant datasets.
domains:
  - genomics
  - biomedical
id: "startgeo"
infores_id: "startgeo"
last_modified_date: '2025-11-25T00:00:00Z'
layout: resource_detail
name: STAR GEO Search Application
homepage_url: http://stargeo.org/
synonyms:
  - STARGEO
---

# STAR GEO Search Application

## Overview

STARGEO (Search Tool for Analysis of GEO) is a web-based application designed to search and analyze gene expression data from NCBI's Gene Expression Omnibus (GEO), one of the largest public repositories of genomics data. STARGEO enables researchers to identify datasets containing significant differential expression for genes of interest, facilitating discovery of relevant experimental data and biological insights.

**Note:** Website availability appears intermittent (http://stargeo.org/). Users may experience connectivity issues.

## Key Features

### Gene Expression Search
- **Query by Gene**: Search for datasets where specific genes show differential expression
- **Statistical Significance**: Identify datasets with significant expression changes
- **Cross-Dataset Search**: Discover relevant experiments across thousands of GEO datasets
- **Multiple Gene Queries**: Search for expression patterns of multiple genes simultaneously

### Data Integration
- **GEO Integration**: Direct access to Gene Expression Omnibus metadata and samples
- **Automated Processing**: Pre-processed gene expression data from GEO Series
- **Standardized Analysis**: Consistent differential expression analysis across datasets
- **Dataset Annotations**: Access to experimental condition and sample metadata

### Analysis Capabilities
- **Differential Expression**: Statistical identification of significantly changed genes
- **Dataset Ranking**: Prioritize datasets by relevance and statistical significance
- **Expression Visualization**: Graphical representation of gene expression patterns
- **Sample Comparisons**: Compare expression across experimental conditions

## Use Cases

### Research Discovery
- Finding datasets relevant to specific genes or pathways
- Literature validation through independent datasets
- Meta-analysis planning and dataset identification
- Hypothesis generation from expression patterns

### Biomarker Discovery
- Identifying consistent expression changes across studies
- Validating potential biomarkers in multiple datasets
- Discovering disease-associated expression signatures

### Target Validation
- Assessing gene expression changes in disease contexts
- Exploring therapeutic target expression profiles
- Identifying relevant experimental models

## Technical Details

### Data Sources
- **Gene Expression Omnibus (GEO)**: Primary data repository
- **Platform Support**: Multiple microarray and RNA-seq platforms
- **Dataset Coverage**: Extensive coverage of human, mouse, and other species
- **Regular Updates**: Integration of new GEO submissions

### Analytical Methods
- Statistical differential expression testing
- Multiple testing correction
- Expression fold-change calculation
- P-value and FDR computation

### Access Methods
- Web-based interface
- Gene symbol or identifier queries
- Interactive results browsing
- Links to original GEO entries

## Applications

### Functional Genomics
- Gene function investigation
- Pathway analysis support
- Expression pattern characterization
- Biological process exploration

### Translational Research
- Disease mechanism investigation
- Drug response profiling
- Clinical relevance assessment
- Biomarker development

### Comparative Studies
- Cross-study validation
- Expression pattern conservation
- Species comparison
- Experimental condition analysis

## Limitations

- **Website Availability**: Service may experience downtime or connectivity issues
- **Data Currency**: Depends on GEO update frequency
- **Platform Coverage**: May not include all GEO datasets or platforms
- **Analysis Scope**: Limited to differential expression analysis

## Information Resource ID

This resource has the Information Resource identifier: `infores:startgeo`

## Related Resources

- **GEO**: https://www.ncbi.nlm.nih.gov/geo/ - Gene Expression Omnibus
- **GEO2R**: https://www.ncbi.nlm.nih.gov/geo/geo2r/ - GEO's built-in analysis tool
- **ArrayExpress**: https://www.ebi.ac.uk/biostudies/arrayexpress - EBI gene expression repository

For more information, visit http://stargeo.org/ (when available).
