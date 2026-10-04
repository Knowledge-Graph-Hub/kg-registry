---
activity_status: inactive
category: DataSource
creation_date: '2025-10-30T00:00:00Z'
description: DATE (Drugs to target pAthways by the Tissue Expression) is a dataset from the Tatonetti lab connecting 1,034 drugs to 954 Reactome pathways in 259 human tissues and cell lines. It combines DrugBank drug-target pairs with tissue expression from GTEx, the GNF U133A gene atlas, the NCI-60 cell lines and the Human Proteome Map. It has not been updated since 2018.
domains:
  - pharmacology
  - systems biology
homepage_url: https://tatonettilab-resources.s3.amazonaws.com/syspharm/DATE.zip
id: date
infores_id: date
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
name: Drugs to target pAthways by the Tissue Expression
products:
  - category: Product
    compression: zip
    description: 'ZIP with two TSV files: Drug_target_reactome_pathway.tsv (611,655 rows) and Drug_target_reactome_pathway_filtered.tsv (238,317 rows, parent pathways removed), with columns for expression dataset, drug name and STITCH ID, tissue, cell line, target UniProt ID and symbol, target class, pathway and pathway size.'
    dump_format: other
    format: tsv
    id: date.archive
    name: DATE Archive ZIP
    original_source:
      - source: date
        relation_type: prov:hadPrimarySource
      - source: drugbank
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: biogps
        relation_type: prov:hadPrimarySource
      - source: stitch
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: gtopdb
        relation_type: prov:hadPrimarySource
    product_file_size: 7261526
    product_url: https://tatonettilab-resources.s3.amazonaws.com/syspharm/DATE.zip
synonyms:
  - DATE
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://tatonettilab.org/
      - contact_type: github
        value: tatonetti-lab
    label: Tatonetti Lab
publications:
  - authors:
      - Hao Y
      - Quinnies K
      - Realubit R
      - Karan C
      - Tatonetti NP
    doi: 10.1002/psp4.12305
    id: doi:10.1002/psp4.12305
    journal: 'CPT: Pharmacometrics & Systems Pharmacology'
    preferred: true
    title: Tissue-Specific Analysis of Pharmacological Pathways
    year: '2018'
---

# Drugs to target pAthways by the Tissue Expression

## Overview

DATE (Drugs to target pAthways by the Tissue Expression) was a computational resource developed to integrate drug-target information with biological pathway data and tissue-specific gene expression patterns. The goal was to predict tissue-specific drug effects and identify therapeutic opportunities based on pathway perturbations in specific tissue contexts.

## Approach

- **Drug-Target Integration**: Connected drugs to their molecular targets
- **Pathway Mapping**: Linked targets to biological pathways
- **Tissue Expression**: Incorporated tissue-specific gene expression data
- **Systems Pharmacology**: Predicted tissue-specific drug effects

## Applications

- Predicting tissue-specific adverse drug effects
- Identifying repurposing opportunities
- Understanding drug mechanism of action in context
- Prioritizing therapeutic targets by tissue

## Activity Status

The DATE resource appears to be inactive. The homepage URL points to an archived ZIP file on Amazon S3, suggesting the resource is no longer actively maintained or updated. No recent publications or updates are available.

## Related Concepts

- **Systems Pharmacology**: Integrative approach to understanding drug action
- **Tissue-Specific Effects**: Importance of cellular context in drug response
- **Network Medicine**: Using biological networks to understand disease and drugs

## Legacy

DATE represented an important approach to integrating multiple data types (drugs, targets, pathways, expression) for predicting tissue-specific pharmacological effects, contributing to the field of computational systems pharmacology.
