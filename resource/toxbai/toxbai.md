---
activity_status: active
category: DataSource
collection:
- nams
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: http://www.chembai.co.kr/en
  - contact_type: email
    value: info@chembai.co.kr
  label: ChemBAI
- category: Organization
  contact_details:
  - contact_type: url
    value: http://toxbai.com/
  label: Environmental Systems Toxicology (EST) Group, University of Seoul
creation_date: '2026-10-28T00:00:00Z'
description: ToxBAI is a desktop application for predicting the toxicity of chemicals
  with mechanistically explainable AI organized around the adverse outcome pathway
  (AOP) framework. From a chemical structure (CAS number or SMILES), it computes molecular
  descriptors and fingerprints and performs Active/Inactive binary classification
  across toxicity endpoints, reporting a confidence level, performance metrics (F1,
  recall, AUC), training dataset size, and an applicability-domain reliability flag
  for each prediction. It offers two families of models — apical-outcome (AO) prediction
  models trained on OECD Test Guideline data that map to regulatory endpoints, and
  mechanism prediction models trained on ToxCast high-throughput bioactivity data
  that correspond to molecular initiating events and key events; predicted MIEs and
  KEs are mapped to AOP networks in the OECD AOP-Wiki for mechanistic interpretation.
  ToxBAI is developed by the Environmental Systems Toxicology group at the University
  of Seoul and operated by ChemBAI, in collaboration with RTI International. It supports
  pre-screening of untested chemicals under the Next Generation Risk Assessment (NGRA)
  framework.
domains:
- toxicology
- adverse outcome pathways
- cheminformatics
- machine learning
- information technology
- chemistry and biochemistry
homepage_url: http://toxbai.com/
id: toxbai
last_modified_date: '2026-10-28T00:00:00Z'
layout: resource_detail
license:
  id: http://toxbai.com/
  label: Custom (free to use; requires Google sign-in and in-app terms acceptance)
name: ToxBAI
products:
- category: GraphicalInterface
  description: ToxBAI desktop application (Windows and macOS) for predicting chemical
    toxicity. Users enter substances by CAS number or SMILES, or upload an Excel file,
    and run the AO prediction models (OECD Test Guideline data) and mechanism prediction
    models (ToxCast data); results are shown as a toxicity-category heatmap and per-substance
    detail with applicability-domain flags, with AOP-linked interpretation and Excel
    report export. Requires a Google sign-in. In version 1.0 the prediction toolbox
    is available; the AOP-based AI and NGRA 1.0 panels are coming-soon placeholders.
  format: http
  id: toxbai.app
  name: ToxBAI Prediction Application
  original_source:
  - relation_type: prov:hadPrimarySource
    source: toxbai
  - relation_type: prov:hadPrimarySource
    source: toxcast
  - relation_type: prov:hadPrimarySource
    source: aop-wiki
  product_url: http://toxbai.com/
- category: DocumentationProduct
  description: ToxBAI user guide (beta, English), covering installation, sign-in,
    substance entry, model selection, and result review and export.
  format: pdf
  id: toxbai.userguide
  name: ToxBAI User Guide
  original_source:
  - relation_type: prov:hadPrimarySource
    source: toxbai
  product_file_size: 12208208
  product_url: http://toxbai.com/downloads/manual/TOXBAI_Userguide_beta_EN.pdf
version: '1.0'
---
# ToxBAI

## Overview

ToxBAI is a desktop application for predicting chemical toxicity using mechanistically explainable AI built around the adverse outcome pathway (AOP) framework. Given a chemical structure (CAS number or SMILES), it computes molecular descriptors and fingerprints and classifies the chemical as Active or Inactive for a range of toxicity endpoints, reporting a confidence level, performance metrics (F1, recall, AUC), training set size, and an applicability-domain reliability flag for each prediction.

It provides two families of models:

- **AO prediction models**, trained on OECD Test Guideline data, corresponding to regulatory apical endpoints.
- **Mechanism prediction models**, trained on ToxCast high-throughput bioactivity data, corresponding to molecular initiating events (MIEs) and key events (KEs).

Predicted MIEs and KEs are mapped to AOP networks in the OECD AOP-Wiki, so a prediction can be interpreted at the biological-pathway level. Endpoint areas include endocrine disruption and developmental and reproductive toxicity (ED-DART), developmental neurotoxicity, inhalation toxicity, genotoxicity and cancer, and liver toxicity bioactivity.

ToxBAI is developed by the Environmental Systems Toxicology (EST) group at the University of Seoul and operated by ChemBAI, in collaboration with RTI International. It is designed to support pre-screening of untested chemicals under the Next Generation Risk Assessment (NGRA) framework.

## Access

- Download the Windows or macOS application from http://toxbai.com/. A Google sign-in and one-time acceptance of the terms are required.
- The user guide is available as a PDF from the same site.

Version 1.0 provides the prediction toolbox; the AOP-based AI and NGRA 1.0 panels are shown as coming-soon placeholders. There is no public API or bulk data download.

## Citation

A describing manuscript (Kim et al., 2026) is in preparation; no DOI is available yet.