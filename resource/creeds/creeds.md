---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: avi.maayan@mssm.edu
  - contact_type: github
    value: MaayanLab
  label: Avi Ma'ayan
  orcid: 0000-0002-6628-6249
description: CREEDS (CRowd Extracted Expression of Differential Signatures) is a database of crowdsourced gene expression signatures for drug, genetic, and disease perturbations.
domains:
- pharmacology
- genomics
id: creeds
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
layout: resource_detail
name: CREEDS
publications:
- doi: 10.1038/ncomms12846
  id: doi:10.1038/ncomms12846
  title: Extraction and analysis of signatures from the Gene Expression Omnibus by the crowd
  year: "2016"
products:
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - chebi
  - cosmic
  - achilles
  - depmap
  - ccle
  - gdsc
  - cellosaurus
  - clue
  - ctd
  - pharmdb
  - prism
  - drugbank
  - lincs
  - compartments
  - offsides
  - sider
  - drugcentral
  - repohub
  - chemicalchecker
  - repodb
  - disgenet
  - opentargets
  - creeds
  - interpro
  - reactome
  - tissues
  - dorothea
  - progeny
  - gtex
  - hpa
  - go
  - corum
  - huri
  - intact
  - omnipath
  - string
  - bto
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
  secondary_source:
  - bioteque
- category: Product
  description: Manual gene expression signatures derived from single gene perturbations
  format: json
  id: creeds.manual_single_gene
  name: CREEDS Manual Single Gene Perturbations
  product_url: https://maayanlab.cloud/CREEDS/download/single_gene_perturbations-v1.0.json
- category: Product
  description: Manual gene expression signatures derived from disease signatures
  format: json
  id: creeds.manual_disease_signatures
  name: CREEDS Manual Disease Signatures
  product_url: https://maayanlab.cloud/CREEDS/download/disease_signatures-v1.0.json
- category: Product
  description: Manual gene expression signatures derived single drug perturbations
  format: json
  id: creeds.manual_single_drug
  name: CREEDS Manual Single Drug Perturbations
  product_url: https://maayanlab.cloud/CREEDS/download/single_drug_perturbations-v1.0.json
- category: Product
  description: DrugMatrix single drug perturbations
  format: json
  id: creeds.drugmatrix
  name: CREEDS DrugMatrix single drug perturbations
  product_url: https://maayanlab.cloud/CREEDS/download/single_drug_perturbations-DM.json
- category: Product
  description: Automatic gene expression signatures derived from single gene perturbations
  format: json
  id: creeds.automatic_single_gene
  name: CREEDS Automatic Single Gene Perturbations
  product_url: https://maayanlab.cloud/CREEDS/download/single_gene_perturbations-p1.0.json
- category: Product
  description: Automatic gene expression signatures derived from disease signatures
  format: json
  id: creeds.automatic_disease_signatures
  name: CREEDS Automatic Disease Signatures
  product_url: https://maayanlab.cloud/CREEDS/download/disease_signatures-p1.0.json
- category: Product
  description: Automatic gene expression signatures derived from single drug perturbations
  format: json
  id: creeds.automatic_single_drug
  name: CREEDS Automatic Single Drug Perturbations
  product_url: https://maayanlab.cloud/CREEDS/download/single_drug_perturbations-p1.0.json
- category: GraphicalInterface
  description: Web interface for exploring CREEDS gene expression signatures
  id: creeds.web_interface
  name: CREEDS Web Interface
  product_url: https://maayanlab.cloud/CREEDS/
---
# CREEDS: Crowd Extracted Expression of Differential Signatures

CREEDS (CRowd Extracted Expression of Differential Signatures) is a database of crowdsourced gene expression signatures for drug, genetic, and disease perturbations. The database was developed by the Ma'ayan Lab at the Icahn School of Medicine at Mount Sinai.

## About CREEDS

CREEDS contains a collection of gene expression signatures extracted from the Gene Expression Omnibus (GEO). These signatures represent the differential expression of genes in response to:

- **Drug Treatments**: Gene expression changes after exposure to pharmaceutical compounds, capturing drug effects at the molecular level
- **Gene Perturbations**: Signatures from knockdown, knockout, or overexpression experiments showing how modifying specific genes affects overall gene expression
- **Disease States**: Differential expression between disease and normal tissue samples, highlighting the molecular basis of various pathological conditions

The signatures were extracted through a crowdsourcing approach, where contributors manually curated gene expression data from GEO to identify control and perturbation samples. This process involved:

1. Identifying relevant GEO datasets
2. Carefully selecting appropriate case/control samples
3. Processing raw data to generate differential expression signatures
4. Quality control and validation of the extracted signatures

Each signature consists of lists of up-regulated and down-regulated genes, along with metadata about the experimental conditions, sample characteristics, and statistical significance.

## Data Access

The CREEDS database is freely accessible through a web interface at [https://maayanlab.cloud/CREEDS/](https://maayanlab.cloud/CREEDS/). Users can search for signatures by various criteria including drugs, genes, or diseases. The complete dataset is also available for download.

## Applications

CREEDS signatures can be used for a variety of applications in biomedical research:

- **Drug Signatures**: 
  - Drug repositioning and repurposing
  - Identifying mechanisms of action for compounds
  - Predicting drug side effects
  - Finding similar drugs with shared mechanisms

- **Genetic Signatures**:
  - Understanding gene function
  - Identifying gene regulatory networks
  - Pathway analysis and enrichment
  - Target discovery for therapeutics

- **Disease Signatures**:
  - Characterizing disease mechanisms
  - Identifying biomarkers
  - Drug discovery for specific diseases
  - Patient stratification and precision medicine

These signatures are particularly valuable when used for signature matching algorithms to connect drugs, genes, and diseases through their shared gene expression patterns.

## Related Projects

CREEDS is related to other Ma'ayan Lab projects including:

- LINCS Program (Library of Integrated Network-Based Cellular Signatures)
- BD2K (Big Data to Knowledge)
- IDG (Illuminating the Druggable Genome)