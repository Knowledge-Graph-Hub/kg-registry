---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://trchealthcare.com/
  label: Therapeutic Research Center (TRC)
creation_date: '2026-10-27T00:00:00Z'
description: The Natural Medicines Comprehensive Database (NMCD), now offered as NatMed
  Pro, is a commercial, evidence-based reference on dietary supplements, herbs, natural
  medicines, and complementary and integrative therapies published by Therapeutic
  Research Center (TRC). It provides monographs on more than a thousand ingredients
  and therapies with graded effectiveness ratings by condition, safety and adverse
  effect information, pregnancy and lactation safety, nutrient depletions caused by
  medications, and interactions with prescription and over-the-counter drugs, alongside
  a database of commercially available supplement products. It absorbed Natural Standard
  in 2013. Access requires a subscription; NMCD was a licensed source for iDISK 1.0.
domains:
- natural products
- chemistry and biochemistry
- nutrition
- pharmacology
- drug interactions
- clinical
- biomedical
homepage_url: https://naturalmedicines.therapeuticresearch.com/
id: nmcd
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
license:
  id: https://naturalmedicines.therapeuticresearch.com/
  label: Proprietary (subscription)
name: Natural Medicines Comprehensive Database (NMCD)
products:
- category: GraphicalInterface
  description: Subscription web database of evidence-based monographs on foods, herbs,
    supplements, diets, and integrative therapies, with effectiveness ratings, safety,
    adverse effects, and drug interaction information.
  format: http
  id: nmcd.monographs
  name: Natural Medicines Ingredients and Therapies Monographs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nmcd
  product_url: https://naturalmedicines.therapeuticresearch.com/
- category: GraphicalInterface
  description: Subscription Interactions Checker that screens natural medicines and
    supplements against prescription and over-the-counter drugs.
  format: http
  id: nmcd.interaction-checker
  name: Natural Medicines Interactions Checker
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nmcd
  product_url: https://naturalmedicines.therapeuticresearch.com/
- category: ProcessProduct
  description: Code used to build iDISK 1.0 from its source databases, including normalization
    against UMLS and MedDRA.
  format: python
  id: idisk.code
  name: iDISK Build Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: idisk
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: meddra
  - relation_type: prov:hadPrimarySource
    source: nmcd
  product_url: https://github.com/jvasilakes/iDISK
synonyms:
- NatMed Pro
- Natural Medicines Database
---
# Natural Medicines Comprehensive Database (NMCD)

## Overview

The Natural Medicines Comprehensive Database, now marketed as NatMed Pro, is a subscription reference on dietary supplements, herbs, and integrative therapies from Therapeutic Research Center. Its monographs grade effectiveness by condition and cover safety, adverse effects, pregnancy and lactation, nutrient depletions, and drug interactions. A companion database describes commercially available supplement products and their manufacturers.

## Access

- Ingredient and therapy monographs, with effectiveness-by-condition search.
- Interactions Checker, Nutrient Depletions, Adverse Effects, and Pregnancy and Lactation Safety tools.

All content requires a subscription; there is no open bulk download or public API.

## Relationship to other resources

NMCD was a licensed source for iDISK 1.0. The iDISK 1.0 release was withdrawn in April 2025 when that license expired, and iDISK 2.0 no longer includes NMCD content.