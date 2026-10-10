---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.mskcc.org/cancer-care/diagnosis-treatment/symptom-management/integrative-medicine/herbs/e-mail-us
  label: Integrative Medicine Service, Memorial Sloan Kettering Cancer Center
creation_date: '2026-10-10T00:00:00Z'
description: About Herbs is a database from the Integrative Medicine Service at Memorial
  Sloan Kettering Cancer Center with evidence-based monographs on about 300 herbs,
  botanicals, dietary supplements, and other products. Each monograph has a version
  for patients and caregivers and one for healthcare professionals; the professional
  version covers the scientific name, clinical summary, purported uses, mechanism
  of action, contraindications, adverse reactions, herb-drug and herb-lab interactions,
  and references. A pharmacist and botanicals expert updates the content continually,
  and it is also offered as a mobile app for iOS and Android.
domains:
- natural products
- chemistry and biochemistry
- nutrition
- cancer
- biomedical
- drug interactions
- pharmacology
homepage_url: https://www.mskcc.org/cancer-care/diagnosis-treatment/symptom-management/integrative-medicine/herbs
id: mskcc-about-herbs
last_modified_date: '2026-10-10T00:00:00Z'
layout: resource_detail
license:
  id: https://www.mskcc.org/legal-disclaimer
  label: Copyright Memorial Sloan Kettering Cancer Center; all rights reserved
name: MSKCC About Herbs
products:
- category: GraphicalInterface
  description: Searchable web database of About Herbs monographs, browsable by name
    or letter, with patient and healthcare professional versions of each monograph.
  format: http
  id: mskcc-about-herbs.portal
  name: About Herbs Web Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mskcc-about-herbs
  product_url: https://www.mskcc.org/cancer-care/diagnosis-treatment/symptom-management/integrative-medicine/herbs/search
- category: GraphicalInterface
  description: About Herbs mobile app for iOS and Android devices, presented by the
    MSK Integrative Medicine Service. This page links to the App Store and Google
    Play listings.
  format: http
  id: mskcc-about-herbs.app
  name: About Herbs Mobile App
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mskcc-about-herbs
  product_url: https://www.mskcc.org/cancer-care/diagnosis-treatment/symptom-management/integrative-medicine/herbs/about-herbs
- category: DocumentationProduct
  description: Frequently asked questions about herbs, botanicals, and other products,
    covering supplements in cancer prevention and treatment and herb-drug interactions.
  format: http
  id: mskcc-about-herbs.faq
  name: Herbs, Botanicals and Other Products FAQs
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mskcc-about-herbs
  product_url: https://www.mskcc.org/cancer-care/diagnosis-treatment/symptom-management/integrative-medicine/herbs/herbs-botanicals-other-products-faqs
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
  - Hou YN
  - Deng G
  - Mao JJ
  doi: 10.1097/PPO.0000000000000403
  id: PMID:31567464
  journal: Cancer J
  preferred: true
  title: 'Practical Application of "About Herbs" Website: Herbs and Dietary Supplement
    Use in Oncology Settings'
  year: '2019'
synonyms:
- About Herbs
- About Herbs, Botanicals & Other Products
---
# MSKCC About Herbs

About Herbs is maintained by the Integrative Medicine Service at Memorial Sloan Kettering Cancer Center (MSK) to help patients and healthcare professionals weigh the value and risks of common herbs and other dietary supplements. It has been online since at least 2002, originally at aboutherbs.com, which now redirects to the MSK site.

## Content

The database holds about 300 monographs on herbs, botanicals, dietary supplements, and other products. Each monograph has two parts. The patient and caregiver part explains what the product is, its potential uses and benefits, and its side effects. The healthcare professional part gives the scientific name, a clinical summary, food sources, purported uses and benefits, mechanism of action, contraindications, adverse reactions, herb-drug interactions, herb-lab interactions, and literature references. Each monograph shows its last update date; a pharmacist and botanicals expert updates the content continually with other MSK Integrative Medicine Service experts.

## Access and terms

Monographs can be read on the MSK website or in the About Herbs app for iOS and Android. There is no bulk download or API. The content is copyrighted by MSK with all rights reserved, and each monograph carries a disclaimer that it is general health information, not a substitute for medical advice.