---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: ingredient_support@hc-sc.gc.ca
  - contact_type: url
    value: https://www.canada.ca/en/health-canada/services/drugs-health-products/natural-non-prescription/applications-submissions/online-solution/ingredients-database.html
  label: Natural and Non-prescription Health Products Directorate, Health Canada
creation_date: '2026-10-19T00:00:00Z'
description: The Natural Health Products Ingredients Database (NHPID) is Health Canada's
  repository of scientific terminology and pre-cleared information approved by the
  Natural and Non-prescription Health Products Directorate (NNHPD). It lists acceptable
  medicinal, non-medicinal, homeopathic, and non-NHP ingredients for natural health
  products with their restrictions and details such as CAS numbers, organism parts,
  and preparations; controlled vocabularies used in NHP product licence applications
  (dosage forms, routes of administration, units, ingredient categories, organism
  parts, non-medicinal purposes, test methods); and single-ingredient and product
  monographs.
domains:
- natural products
- chemistry and biochemistry
- pharmacology
- nutrition
homepage_url: https://webprod.hc-sc.gc.ca/nhpid-bdipsn/?lang=eng
id: nhpid
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://www.canada.ca/en/transparency/terms.html
  label: Government of Canada Terms and Conditions (non-commercial reproduction permitted)
name: Natural Health Products Ingredients Database
products:
- category: GraphicalInterface
  description: Web application for searching NHPID ingredients by name or CAS number
    and role (homeopathic, medicinal, non-medicinal, non-NHP, component), and for
    searching the NHP controlled vocabularies by category. Controlled vocabulary terms
    for dosage forms, routes of administration, and units are adapted from ICH M5
    lists, and ingredient naming conventions from the TGA approved terminology.
  format: http
  id: nhpid.web
  name: NHPID Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nhpid
  product_url: https://webprod.hc-sc.gc.ca/nhpid-bdipsn/?lang=eng
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: tga-approved-terminology
  - relation_type: prov:wasDerivedFrom
    source: ich-m5
- category: Product
  description: List of NNHPD single ingredient monographs, which describe pre-cleared
    information (sources, doses, uses, risks, quality) for natural health products
    containing a single medicinal ingredient. Monographs marked with an asterisk are
    generated directly from the NHPID.
  format: http
  id: nhpid.single-ingredient-monographs
  name: NHPID Single Ingredient Monographs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nhpid
  product_url: https://webprod.hc-sc.gc.ca/nhpid-bdipsn/monosReq?monotype=single&lang=eng
- category: Product
  description: List of NNHPD product monographs, which describe pre-cleared information
    for multi-ingredient natural health product types.
  format: http
  id: nhpid.product-monographs
  name: NHPID Product Monographs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nhpid
  product_url: https://webprod.hc-sc.gc.ca/nhpid-bdipsn/monosReq?monotype=product&lang=eng
synonyms:
- NHPID
- Base de données des ingrédients des produits de santé naturels
- BDIPSN
---
# Natural Health Products Ingredients Database

## Overview

The Natural Health Products Ingredients Database (NHPID) is maintained by the Natural and Non-prescription Health Products Directorate (NNHPD) of Health Canada as part of the Natural Health Products Online Solution. It is the reference repository of approved ingredient information and terminology used to prepare and validate electronic product licence applications for natural health products (NHPs) in Canada, and it is open to the public for searching.

## Data Content

- **Ingredients**: medicinal, non-medicinal, and homeopathic ingredients, plus non-NHP ingredients that are not allowed as medicinal ingredients or are allowed only under restrictions. Records include details relevant to the ingredient type, such as Chemical Abstracts Service (CAS) numbers for chemical substances and organism parts and preparations for organism substances, along with restriction details. Homeopathic ingredient names come mainly from one French and four English pharmacopoeias.
- **Controlled vocabularies**: standard terms for chemical classes and subclasses, countries, dosage forms and dosage form groups, geographical areas, ingredient categories, NHP classifications, non-medicinal ingredient purposes, organism parts and preparation types, organism types, routes of administration, solvents, test methods, and units of measurement. Ingredient naming conventions are adapted from the Australian Therapeutic Goods Administration (TGA) approved terminology, and dosage forms, routes, and units from the ICH M5 controlled lists.
- **Pre-cleared information**: NNHPD single-ingredient monographs, product monographs, and abbreviated labelling standards.

The data were last updated on 2026-09-02 (as reported on the site). Product-level licensing data are in the related Licensed Natural Health Products Database (LNHPD).

## Access

The database is available through a bilingual web search interface (English and French). Health Canada does not publish a bulk download or API for the NHPID. Requests to add or change ingredients or controlled vocabulary go through the NHPID Ingredient Request Form and ingredient_support@hc-sc.gc.ca.

## License

The NHPID web application falls under the Government of Canada Terms and Conditions: content may be reproduced for non-commercial purposes with attribution, while commercial redistribution requires written permission. The Open Government Portal records that describe the NHPID and its guides are published under the Open Government Licence - Canada, but those records cover documentation pages, not a data release.
