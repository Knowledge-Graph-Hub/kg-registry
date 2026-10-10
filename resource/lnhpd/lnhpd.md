---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: nhp_initiative_psn@hc-sc.gc.ca
  - contact_type: url
    value: https://www.canada.ca/en/health-canada/services/drugs-health-products/natural-non-prescription/applications-submissions/product-licensing/licensed-natural-health-products-database.html
  label: Natural and Non-prescription Health Products Directorate, Health Canada
creation_date: '2026-10-10T00:00:00Z'
description: The Licensed Natural Health Products Database (LNHPD), managed by Health
  Canada, holds information about natural health products that have been issued a
  product licence in Canada, including vitamin and mineral supplements, herbal remedies,
  traditional medicines, probiotics, and homeopathic medicines. Each product is identified
  by a Natural Product Number (NPN) or Homeopathic Medicine Number (DIN-HM), and records
  give the licence holder, medicinal and non-medicinal ingredients, dosage form, recommended
  dose and use, route, and risk information. It covers more than 150,000 licensed
  and discontinued products and is updated nightly.
domains:
- natural products
- chemistry and biochemistry
- nutrition
- public health
- pharmacology
homepage_url: https://health-products.canada.ca/lnhpd-bdpsnh/
id: lnhpd
last_modified_date: '2026-10-10T00:00:00Z'
layout: resource_detail
license:
  id: https://open.canada.ca/en/open-government-licence-canada
  label: Open Government Licence - Canada
name: Licensed Natural Health Products Database
products:
- category: GraphicalInterface
  description: Web search for licensed natural health products by product name, NPN
    or DIN-HM, ingredient, company, and other fields, with basic and advanced search.
  format: http
  id: lnhpd.search
  name: LNHPD Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lnhpd
  product_url: https://health-products.canada.ca/lnhpd-bdpsnh/
- category: ProgrammingInterface
  description: REST API (base URI https://health-products.canada.ca/api/natural-licences/)
    returning product licence, medicinal and non-medicinal ingredient, ingredient
    source, dose, purpose, risk, and route records in JSON or XML, in English or French.
    The product URL is a sample product licence query.
  format: json
  id: lnhpd.api
  is_public: true
  name: LNHPD API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lnhpd
  product_url: https://health-products.canada.ca/api/natural-licences/productlicence/?lang=en&type=json&id=3894657
- category: Product
  description: Full extract of all LNHPD product licence records in JSON, returned
    by the API's product licence endpoint without an id or page parameter. Other entities
    (ingredients, dose, purpose, risk, route) have matching endpoints, also offered
    as XML. Updated daily.
  format: json
  id: lnhpd.productlicence.json
  name: LNHPD Product Licence Extract (JSON)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lnhpd
  product_file_size: 148389462
  product_url: https://health-products.canada.ca/api/natural-licences/productlicence/?lang=en&type=json
- category: DocumentationProduct
  description: LNHPD API guide describing endpoints, parameters, response fields,
    and sample responses.
  format: http
  id: lnhpd.api-guide
  name: LNHPD API Guide
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lnhpd
  product_url: https://health-products.canada.ca/api/documentation/lnhpd-documentation-en.html
- category: Product
  description: Open Government Portal dataset record for licensed natural health products,
    listing the API JSON and XML extract endpoints for each entity in English and
    French.
  format: http
  id: lnhpd.open-data
  name: LNHPD Open Data Record
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lnhpd
  product_url: https://open.canada.ca/data/en/dataset/ef546c83-43a8-4404-943e-ab324164eeb3
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
synonyms:
- LNHPD
- Base de données des produits de santé naturels homologués
- BDPSNH
---
# Licensed Natural Health Products Database

The Licensed Natural Health Products Database (LNHPD) is managed by the Natural and Non-prescription Health Products Directorate of Health Canada. It contains information about natural health products (NHPs) that have been issued a product licence in Canada.

## Data

Licensed NHPs include vitamin and mineral supplements, herbal remedies, traditional medicines such as Traditional Chinese Medicine and Ayurvedic products, probiotics, homeopathic medicines, and some consumer products. Each product has an eight-digit Natural Product Number (NPN) or Homeopathic Medicine Number (DIN-HM). Records give the licence holder, medicinal and non-medicinal ingredients and their sources, dosage form, recommended dose, route of administration, recommended use or purpose, and risk information such as cautions, warnings, contraindications, and known adverse reactions. The database includes both licensed and discontinued products, with more than 150,000 product licences as of October 2026, and it is updated nightly.

## Access

Products can be searched on the web or retrieved through the LNHPD REST API, which returns JSON or XML in English or French. The Open Government Portal lists the API extract endpoints in place of the flat-file extracts that were offered earlier. The data are released under the Open Government Licence - Canada. Ingredient information is related to Health Canada's Natural Health Products Ingredients Database (NHPID), which is not yet in KG-Registry.