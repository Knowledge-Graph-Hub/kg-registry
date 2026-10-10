---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: ODScomments@mail.nih.gov
  - contact_type: url
    value: https://ods.od.nih.gov/
  label: NIH Office of Dietary Supplements
creation_date: '2026-10-10T00:00:00Z'
description: The Dietary Supplement Label Database (DSLD) from the NIH Office of Dietary
  Supplements records the full label contents of dietary supplement products sold
  in the United States, including label images, ingredient names and forms, amounts
  of dietary ingredients, and all label statements. It holds more than 214,000 labels
  for products both on and off the market, categorized with LanguaL codes. Labels
  come mainly from manufacturers through an NIH contractor and from products reported
  in NHANES. Launched in 2013 and modernized with a public API in 2021, it is updated
  with regular releases.
domains:
- nutrition
- food
- natural products
- chemistry and biochemistry
- public health
homepage_url: https://dsld.od.nih.gov/
id: dsld
last_modified_date: '2026-10-10T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: Dietary Supplement Label Database
products:
- category: GraphicalInterface
  description: DSLD web interface for searching and browsing dietary supplement labels
    by product, brand, or ingredient. Search results and product pages can be exported
    as CSV, Excel, or JSON.
  format: http
  id: dsld.portal
  name: DSLD Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dsld
  product_url: https://dsld.od.nih.gov/
- category: ProgrammingInterface
  description: REST API for retrieving individual label records and for searching
    and browsing labels, brands, and ingredient groups. Usable without a key; an api.data.gov
    key raises the rate limit.
  format: json
  id: dsld.api
  is_public: true
  name: DSLD Label API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dsld
  product_url: https://api.ods.od.nih.gov/dsld/v9/
- category: DocumentationProduct
  description: Guide to the DSLD API, covering endpoints, rate limits, and the CC0
    licensing statement.
  format: http
  id: dsld.api-guide
  name: DSLD API Guide
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dsld
  product_url: https://dsld.od.nih.gov/api-guide
- category: Product
  compression: zip
  description: Full DSLD database download in JSON, with complete label information
    for all current and historical products. Updated with each release.
  format: json
  id: dsld.json
  name: DSLD Full Database (JSON)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dsld
  product_file_size: 584344994
  product_url: https://api.ods.od.nih.gov/dsld/s3/data/DSLD-full-database-JSON.zip
- category: Product
  compression: zip
  description: Full DSLD database download as Excel workbooks. Updated with each release.
  format: xlsx
  id: dsld.xlsx
  name: DSLD Full Database (Excel)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dsld
  product_file_size: 271506687
  product_url: https://api.ods.od.nih.gov/dsld/s3/data/DSLD-full-database-XLSX.zip
- category: Product
  compression: zip
  description: Full DSLD database download as CSV files. Updated with each release.
  format: csv
  id: dsld.csv
  name: DSLD Full Database (CSV)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: dsld
  product_file_size: 92613625
  product_url: https://api.ods.od.nih.gov/dsld/s3/data/DSLD-full-database-CSV.zip
- category: Product
  description: iDISK 2.0 entity files (dietary supplement ingredients, products, drugs,
    diseases, and signs and symptoms) in CSV format, integrating DSLD, LNHPD, and
    MSKCC About Herbs.
  format: csv
  id: idisk.idisk2-entities
  name: iDISK 2.0 Entities
  original_source:
  - relation_type: prov:hadPrimarySource
    source: idisk
  - relation_type: prov:hadPrimarySource
    source: dsld
  - relation_type: prov:hadPrimarySource
    source: lnhpd
  - relation_type: prov:hadPrimarySource
    source: mskcc-about-herbs
  product_url: https://drive.google.com/drive/folders/10mpvyHbRhhsrylw2o3xToT8RihvSWIA4
- category: Product
  description: iDISK 2.0 relationship files (product-ingredient, ingredient-disease,
    ingredient-drug, and ingredient-symptom) in CSV format.
  format: csv
  id: idisk.idisk2-relations
  name: iDISK 2.0 Relations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: idisk
  - relation_type: prov:hadPrimarySource
    source: dsld
  - relation_type: prov:hadPrimarySource
    source: lnhpd
  - relation_type: prov:hadPrimarySource
    source: mskcc-about-herbs
  product_url: https://drive.google.com/drive/folders/1XTtb4KKxUXfqG8tZTbvxtwv7IDUHe424
publications:
- authors:
  - Dwyer JT
  - Bailen RA
  - Saldanha LG
  - Gahche JJ
  - Costello RB
  - Betz JM
  - Davis CD
  - Bailey RL
  - Potischman N
  - Ershow AG
  - Sorkin BC
  - Kuszak AJ
  - Rios-Avila L
  - Chang F
  - Goshorn J
  - Andrews KW
  - Pehrsson PR
  - Gusev PA
  - Harnly JM
  - Hardy CJ
  - Emenaker NJ
  - Herrick KA
  doi: 10.1093/jn/nxy082
  id: PMID:31249427
  journal: J Nutr
  preferred: true
  title: 'The Dietary Supplement Label Database: Recent Developments and Applications'
  year: '2018'
- authors:
  - Saldanha LG
  - Dwyer JT
  - Bailen RA
  doi: 10.1016/j.jfca.2021.104058
  id: PMID:34366563
  journal: J Food Compost Anal
  title: Modernization of the National Institutes of Health Dietary Supplement Label
    Database
  year: '2021'
- authors:
  - Dwyer JT
  - Saldanha LG
  - Bailen RA
  - Bailey RL
  - Costello RB
  - Betz JM
  - Chang FF
  - Goshorn J
  - Andrews KW
  - Pehrsson PR
  - Milner JA
  - Burt VL
  - Gahche JJ
  - Hardy CJ
  - Emenaker NJ
  doi: 10.1016/j.jand.2014.04.015
  id: PMID:24928780
  journal: J Acad Nutr Diet
  title: A free new dietary supplement label database for registered dietitian nutritionists
  year: '2014'
synonyms:
- DSLD
taxon:
- NCBITaxon:9606
---
# Dietary Supplement Label Database

The Dietary Supplement Label Database (DSLD) is maintained by the Office of Dietary Supplements (ODS) at the National Institutes of Health. It captures all information printed on the labels of dietary supplement products sold in the United States: label images, the names and forms of ingredients, the amounts of dietary ingredients, and all label statements. It covers products both on and off the market.

## Data

Labels come mainly from manufacturers, who submit them to the curation contractor (the Therapeutic Research Center) under NIH contract. DSLD also includes labels of products reported in NHANES, from the 2011–2012 survey onward, and labels that federal partners ask to include. Label information is categorized with LanguaL codes for product type, target group, supplement form, and dietary claims. As of the May 2026 release (API version 9.5.0), the database holds more than 214,000 labels.

## Access

DSLD launched in June 2013 and was modernized in 2021 with a new interface and a public API. Data can be searched on the website, retrieved through the REST API, or downloaded in full as JSON, Excel, or CSV files, which are updated with each release. The data are in the public domain under CC0 1.0. ODS asks users to cite DSLD as the source of the data.