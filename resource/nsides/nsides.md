---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: "nick.tatonetti@gmail.com"
      - contact_type: github
        value: "tatonetti-lab"
    label: Tatonetti Lab
creation_date: '2025-10-30T00:00:00Z'
description: nSIDES is a comprehensive collection of drug side effect and drug interaction resources developed by the Tatonetti Lab. It includes OnSIDES (adverse events from drug labels), KidSIDES (pediatric drug safety signals), AwareDX (sex-specific adverse drug effects), OffSIDES (off-label side effects), TwoSIDES (drug-drug interactions), and ManySIDES (combinations of 3+ drugs).
domains:
  - pharmacology
  - drug discovery
  - health
  - precision medicine
homepage_url: https://nsides.io/
id: "nsides"
infores_id: "nsides"
last_modified_date: '2025-10-31T00:00:00Z'
layout: resource_detail
name: nSIDES
products:
  - category: Product
    description: Adverse drug events extracted from FDA drug labels using fine-tuned PubMedBERT, covering 3.6M+ drug-ADE pairs for 2,793 drug ingredients from 46,686 labels
    format: csv
    id: "nsides.onsides"
    name: OnSIDES
    product_url: https://github.com/tatonetti-lab/onsides/releases
  - category: Product
    description: Pediatric drug safety signals across developmental phases, covering adverse events specific to children
    format: csv
    id: "nsides.kidsides"
    name: KidSIDES
    original_source:
      - nsides
    product_url: https://tatonettilab-resources.s3.amazonaws.com/KidSIDES/ade_nichd.csv.gz
  - category: GraphicalInterface
    description: Interactive RShiny web portal for browsing pediatric drug safety signals
    format: http
    id: "nsides.pdsportal"
    name: PDSPortal
    original_source:
      - nsides
    product_url: https://pdsportal.shinyapps.io/pdsportal/
  - category: Product
    description: Drug safety signals with differential risk between men and women, covering 20,817 adverse drug effects with sex-specific risks
    format: http
    id: "nsides.awaredx"
    name: AwareDX
    original_source:
      - nsides
    product_url: http://tatonettilab-resources.s3-website-us-west-1.amazonaws.com/?p=nsides/
  - category: ProcessProduct
    description: Code repository for OnSIDES model training and data generation
    id: "nsides.onsides.code"
    name: OnSIDES Code
    original_source:
      - nsides
    product_url: https://github.com/tatonetti-lab/onsides
  - category: ProcessProduct
    description: Code repository for KidSIDES pediatric adverse drug event database study
    id: "nsides.kidsides.code"
    name: KidSIDES Code
    original_source:
      - nsides
    product_url: https://github.com/ngiangre/pediatric_ade_database_study
publications:
  - authors:
      - Chandak P
      - Tatonetti NP
    doi: "10.1016/j.patter.2020.100108"
    id: "doi:10.1016/j.patter.2020.100108"
    journal: Patterns (N Y)
    title: Using Machine Learning to Identify Adverse Drug Effects Posing Increased Risk to Women
    year: "2020"
  - authors:
      - Giangreco N
      - Tatonetti NP
    doi: "10.1016/j.medj.2022.08.001"
    id: "doi:10.1016/j.medj.2022.08.001"
    journal: Med
    title: A database of pediatric drug effects to evaluate ontogenic mechanisms from child growth and development
    year: "2022"
  - authors:
      - Giangreco N
      - Tatonetti NP
    doi: "10.1186/s13040-021-00264-9"
    id: "doi:10.1186/s13040-021-00264-9"
    journal: BioData Mining
    title: Evaluating risk detection methods to uncover ontogenic-mediated adverse drug effect mechanisms in children
    year: "2021"
repository: https://github.com/tatonetti-lab
synonyms:
  - nSIDES
---

# nSIDES

## Overview

nSIDES is the home for comprehensive drug side effect and drug interaction resources developed by the Tatonetti Lab at Columbia University. The platform provides multiple interconnected databases and tools for analyzing adverse drug events across different populations and contexts. nSIDES represents one of the most extensive collections of drug safety information available, combining machine learning extraction from drug labels with pharmacovigilance signal detection from post-marketing surveillance data.

The nSIDES ecosystem includes resources for general adverse drug events (OnSIDES), pediatric populations (KidSIDES), sex-specific risks (AwareDX), off-label effects (OffSIDES), drug-drug interactions (TwoSIDES), and higher-order drug combinations (ManySIDES).

## Data Content

### OnSIDES - Drug Label Adverse Events
OnSIDES extracts adverse drug events from FDA-approved drug labels using a fine-tuned PubMedBERT language model:
- **Coverage**: 3.6 million+ drug-ADE pairs
- **Drug ingredients**: 2,793 unique compounds
- **Labels processed**: 46,686 drug labels from DailyMed
- **Model performance**: F1 score of 0.90, AUROC of 0.92 for adverse reactions sections
- **Updates**: Quarterly releases
- **International variants**: OnSIDES-INTL (Japan, UK, EU labels), OnSIDES-PED (pediatric-specific)
- **Data source**: DailyMed structured product labels (November 2023)

### KidSIDES - Pediatric Drug Safety
Pediatric drug safety signals across developmental phases:
- **Scope**: Drug safety signals specific to childhood developmental stages
- **Method**: Pharmacovigilance algorithm applied to post-marketing reports
- **Application**: Identifies age-specific adverse event risks
- **Interactive access**: PDSPortal RShiny web application
- **Data formats**: MySQL, SQLite, and CSV files
- **Coverage**: Adverse events analyzed across NICHD developmental phases

### AwareDX - Sex-Specific Drug Risks
Machine learning-identified adverse drug effects with differential risk by biological sex:
- **Coverage**: 20,817 adverse drug effects with sex-specific risks
- **Focus**: Effects disproportionately affecting women
- **Method**: ML algorithm accounting for confounding biases
- **Validation**: Validated against pharmacogenetic mechanisms of sex-differentially expressed genes
- **Clinical relevance**: Women experience 2x risk of ADRs compared to men

### OffSIDES and TwoSIDES
Classic resources for off-label side effects and drug-drug interactions:
- **OffSIDES**: Off-label drug side effects not listed on FDA labels
- **TwoSIDES**: Comprehensive drug-drug-effect relationships
- **Drugs covered**: 3,300+ drugs
- **Drug combinations**: 63,000+ pairs
- **Adverse reactions**: Millions of potential effects
- **Note**: Currently being updated for 2022+ with quarterly updates planned

### ManySIDES
Side effect signals for combinations of 3 or more drugs:
- **Status**: Active development (v0.1 released)
- **Scope**: Higher-order drug combination effects
- **Use case**: Polypharmacy risk assessment

## Key Features

- **Machine learning extraction**: Fine-tuned PubMedBERT for label processing
- **Population-specific**: Dedicated resources for pediatrics, sex differences
- **Comprehensive coverage**: Labels, post-marketing surveillance, interactions
- **Regular updates**: Quarterly releases for OnSIDES and derivatives
- **Multiple formats**: CSV, SQL, SQLite for flexible integration
- **Interactive tools**: Web portals for browsing (PDSPortal)
- **Open source**: Code and data freely available
- **Validated methods**: Published algorithms with performance metrics

## Access Methods

1. **Direct Download**: CSV, SQL, and SQLite files from S3 buckets and GitHub
2. **GitHub Releases**: Versioned releases with release notes
3. **Interactive Web Portals**: PDSPortal for browsing pediatric signals
4. **API Access**: (Under development for some components)
5. **Code Repositories**: Full source code for reproduction and extension

## Technology Stack

- **Machine Learning**: Fine-tuned PubMedBERT language model
- **NLP**: Named entity recognition and relation extraction
- **Statistics**: Propensity score methods, disproportionality analysis
- **Web Applications**: RShiny for interactive visualization
- **Data Processing**: Python, SQL
- **Model Training**: PyTorch/Transformers
- **Data Sources**: FDA FAERS, DailyMed, clinical trial databases

## Use Cases

1. **Drug Development**: Early identification of potential safety signals
2. **Pharmacovigilance**: Post-marketing surveillance and signal detection
3. **Precision Medicine**: Tailoring drug prescriptions based on sex, age
4. **Clinical Decision Support**: Informing prescribing decisions for vulnerable populations
5. **Research**: Studying mechanisms of adverse drug events
6. **Regulatory Science**: Supporting drug safety assessments
7. **Polypharmacy Analysis**: Understanding risks of multi-drug regimens

## Model Performance

### OnSIDES Extraction Accuracy
- **F1 Score**: 0.90 (Adverse Reactions section)
- **AUROC**: 0.92 (Adverse Reactions)
- **AUPR**: 0.95 (Adverse Reactions)
- **TAC 2017 Evaluation**: Micro-F1 0.87, Macro-F1 0.85
- **Boxed Warnings**: F1 0.71, AUROC 0.85

## Management

Developed and maintained by the Tatonetti Lab at Columbia University, led by Dr. Nicholas P. Tatonetti. The lab specializes in computational pharmacology, pharmacovigilance, and precision medicine applications of machine learning and data science.

## Related Resources

- [FAERS](faers): FDA Adverse Event Reporting System, source data for many nSIDES analyses
- [DailyMed](dailymed): Source of drug labels for OnSIDES extraction
- [SIDER](sider): Alternative drug side effect database
- [DrugBank](drugbank): Comprehensive drug information database

## Last Update

OnSIDES: November 2023 (labels), with quarterly updates planned
KidSIDES: Version 0.3 (2019 Q2 data), November 2021
AwareDX: 2020 publication
OffSIDES/TwoSIDES: 2022 update in progress
