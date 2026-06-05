---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://www.pmda.go.jp/english/"
    label: Pharmaceuticals and Medical Devices Agency
creation_date: '2026-06-02T00:00:00Z'
description: The Pharmaceuticals and Medical Devices Agency (PMDA) is Japan's regulatory agency for pharmaceuticals, medical devices, regenerative medical products, and related safety information, providing product searches, package inserts, review reports, adverse event information, and safety communications.
domains:
  - biomedical
  - clinical
homepage_url: https://www.pmda.go.jp/english/
id: "pmda"
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: Pharmaceuticals and Medical Devices Agency
products:
  - category: GraphicalInterface
    description: English PMDA website for regulatory review, safety, health damage relief, and product-related information for drugs, medical devices, and regenerative medical products in Japan.
    format: http
    id: "pmda.portal"
    name: PMDA English Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pmda
    product_url: https://www.pmda.go.jp/english/
  - category: GraphicalInterface
    description: PMDA English index linking to safety alerts, recalls, review reports, package inserts, and other information for individual products.
    format: http
    id: "pmda.english-search-index"
    name: PMDA English Product Information Index
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pmda
    product_url: https://www.pmda.go.jp/english/search_index.html
  - category: GraphicalInterface
    description: Japanese PMDA search interface for prescription drug package inserts and related drug safety information.
    format: http
    id: "pmda.iyaku-search"
    name: PMDA Prescription Drug Information Search
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pmda
    product_url: https://www.pmda.go.jp/PmdaSearch/iyakuSearch/
  - category: DocumentationProduct
    description: PMDA documentation explaining newly introduced electronic package inserts, including electronic browsing of drug, medical device, in vitro diagnostic, and regenerative medical product information.
    format: http
    id: "pmda.e-package-inserts-info"
    name: PMDA Electronic Package Inserts Information
    original_source:
      - relation_type: prov:hadPrimarySource
        source: pmda
    product_url: https://www.pmda.go.jp/english/safety/info-services/e-pack-ins/0001.html
  - category: Product
    description: PMDA regulatory source extract from the medic v1.0.1 release
    id: "medi.pmda"
    latest_version: "v1.0.1"
    name: MeDI PMDA Extract
    original_source:
      - relation_type: prov:hadPrimarySource
        source: medi
    product_file_size: 569703
    product_url: https://github.com/marcello-deluca/medic/releases/download/v1.0.1/pmda.xlsx
    secondary_source:
      - relation_type: prov:wasDerivedFrom
        source: pmda
synonyms:
  - PMDA
---

# Pharmaceuticals and Medical Devices Agency

The Pharmaceuticals and Medical Devices Agency is Japan's regulator and public
information source for pharmaceutical, medical device, regenerative medical
product, and related safety information.
