---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.ema.europa.eu/
    label: European Medicines Agency
creation_date: '2026-06-02T00:00:00Z'
description: The European Medicines Agency is the European Union agency responsible for scientific evaluation, supervision, and safety monitoring of medicines in the EU and EEA, including public medicine pages, EPARs, regulatory data, and pharmacovigilance resources.
domains:
  - pharmacology
  - clinical
  - health
homepage_url: https://www.ema.europa.eu/
id: ema
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: European Medicines Agency
products:
  - category: GraphicalInterface
    description: EMA medicines portal for searching centrally authorised medicines, medicines under evaluation, herbal medicines, EPARs, product information, and other regulatory medicine records.
    id: ema.medicines
    name: EMA Medicines Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ema
    product_url: https://www.ema.europa.eu/en/medicines
  - category: Product
    description: EMA downloadable medicine data tables covering human medicines, veterinary medicines, opinions for medicines used outside the EU, and herbal medicines.
    format: mixed
    id: ema.medicine-data
    name: EMA Downloadable Medicine Data
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ema
    product_url: https://www.ema.europa.eu/en/medicines/download-medicine-data
  - category: Product
    description: Public data from the EMA Article 57 database on all medicines authorised in the European Union.
    format: mixed
    id: ema.article-57
    name: EMA Article 57 Authorised Medicines Data
    original_source:
      - relation_type: prov:hadPrimarySource
        source: ema
    product_url: https://www.ema.europa.eu/en/human-regulatory-overview/post-authorisation/data-medicines-iso-idmp-standards/public-data-article-57-database
  - category: Product
    description: EMA regulatory source extract from the medic v1.0.1 release
    id: medi.ema
    latest_version: v1.0.1
    name: MeDI EMA Extract
    original_source:
      - relation_type: prov:hadPrimarySource
        source: medi
    product_file_size: 507869
    product_url: https://github.com/marcello-deluca/medic/releases/download/v1.0.1/ema.xlsx
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: ema
synonyms:
  - EMA
---

# European Medicines Agency

The European Medicines Agency publishes regulatory information on medicines
evaluated or monitored at the EU level. Its data products include searchable
medicine pages, downloadable medicine data tables, and public Article 57
authorised-medicine data used by downstream resources.
