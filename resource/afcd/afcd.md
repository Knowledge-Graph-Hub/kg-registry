---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.foodstandards.gov.au/
  label: Food Standards Australia New Zealand (FSANZ)
creation_date: '2026-10-21T00:00:00Z'
description: The Australian Food Composition Database (AFCD) is Food Standards Australia New
  Zealand's (FSANZ) reference database of the nutrient content of foods available in Australia,
  and is the successor to the NUTTAB series. The current edition, Release 3 (December 2025),
  covers 1,588 foods with up to 268 nutrient values per food. It is distributed as downloadable
  Excel files and through a searchable online food-search interface.
domains:
- food
- nutrition
homepage_url: https://www.foodstandards.gov.au/science-data/monitoringnutrients/afcd
id: afcd
last_modified_date: '2026-10-21T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: Creative Commons Attribution 4.0 International
name: Australian Food Composition Database (AFCD)
products:
- category: GraphicalInterface
  description: Interactive online search of the Australian Food Composition Database by food,
    alphabetical list, food group, or nutrient.
  format: http
  id: afcd.search
  name: AFCD Searchable Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afcd
  product_url: https://afcd.foodstandards.gov.au/
- category: Product
  description: Per-food descriptive details for the AFCD Release 3 foods, as an Excel file.
  format: xlsx
  id: afcd.food-details
  name: AFCD Release 3 Food Details
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afcd
  product_url: https://www.foodstandards.gov.au/sites/default/files/2025-12/AFCD%20Release%203%20-%20Food%20Details.xlsx
- category: Product
  description: Nutrient values for each food in AFCD Release 3, as an Excel file.
  format: xlsx
  id: afcd.nutrient-profiles
  name: AFCD Release 3 Nutrient Profiles
  original_source:
  - relation_type: prov:hadPrimarySource
    source: afcd
  product_url: https://www.foodstandards.gov.au/sites/default/files/2025-12/AFCD%20Release%203%20-%20Nutrient%20profiles.xlsx
synonyms:
- AFCD
- NUTTAB
version: Release 3
---

# Australian Food Composition Database (AFCD)

## Overview

The Australian Food Composition Database (AFCD), formerly NUTTAB, is FSANZ's reference database of the nutrient content of foods available in Australia. Release 3 (December 2025) covers 1,588 foods with up to 268 nutrient values each.

## Access

- Searchable online database: search by food, food group, or nutrient.
- Downloadable Excel files: Food Details and Nutrient Profiles (and related metadata files).

## Citation

Food Standards Australia New Zealand. Australian Food Composition Database — Release 3. 2025. https://www.foodstandards.gov.au/science-data/monitoringnutrients/afcd
