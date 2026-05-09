---
activity_status: active
category: DataSource
collection:
  - omop
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.wolterskluwer.com/en/solutions/medi-span/contact-us/support
    label: Medi-Span Customer Support
creation_date: '2026-04-10T00:00:00Z'
description: The Medi-Span Generic Product Identifier (GPI) is a proprietary 14-character concept and therapeutic classification system from Wolters Kluwer's Medi-Span suite. GPI is used to identify and hierarchically group drug products for medication reconciliation, clinical screening, formulary management, and interoperability workflows. It remains actively maintained as part of the commercial Medi-Span drug data ecosystem and is used in OMOP/Athena contexts as one of the source vocabularies incorporated into standardized vocabulary distributions.
domains:
  - clinical
  - health
  - pharmacology
homepage_url: https://www.wolterskluwer.com/en/solutions/medi-span/about/gpi
id: medispan-gpi
last_modified_date: '2026-04-10T00:00:00Z'
layout: resource_detail
name: Medi-Span Generic Product Identifier
products:
  - category: DocumentationProduct
    description: Official Wolters Kluwer product page describing the Medi-Span Generic Product Identifier and its therapeutic classification model
    format: http
    id: medispan-gpi.documentation
    name: Medi-Span GPI Documentation
    original_source:
      - source: medispan-gpi
        relation_type: prov:hadPrimarySource
    product_url: https://www.wolterskluwer.com/en/solutions/medi-span/about/gpi
  - category: DocumentationProduct
    description: Customer support and access point for Medi-Span subscribers with product delivery, account, and content questions
    format: http
    id: medispan-gpi.support
    name: Medi-Span Customer Support
    original_source:
      - source: medispan-gpi
        relation_type: prov:hadPrimarySource
    product_url: https://www.wolterskluwer.com/en/solutions/medi-span/contact-us/support
  - category: Product
    description: Downloadable standardized vocabulary bundles for OMOP CDM assembled through the authenticated Athena web application
    format: csv
    id: athena.vocabularies
    name: Athena Vocabulary Downloads
    original_source:
      - source: snomedct
        relation_type: prov:hadPrimarySource
      - source: icd10
        relation_type: prov:hadPrimarySource
      - source: icd10cm
        relation_type: prov:hadPrimarySource
      - source: mesh
        relation_type: prov:hadPrimarySource
      - source: loinc
        relation_type: prov:hadPrimarySource
      - source: cdiscvocab
        relation_type: prov:hadPrimarySource
      - source: ciel
        relation_type: prov:hadPrimarySource
      - source: rxnorm
        relation_type: prov:hadPrimarySource
      - source: ndcd
        relation_type: prov:hadPrimarySource
      - source: gemscript
        relation_type: prov:hadPrimarySource
      - source: medispan-gpi
        relation_type: prov:hadPrimarySource
    product_url: https://athena.ohdsi.org/vocabulary/list
    secondary_source:
      - source: athena
        relation_type: prov:wasInfluencedBy
    warnings:
      - Athena vocabulary downloads are prepared through the logged-in web application; stable direct public file URLs are not exposed.
synonyms:
  - Medi-Span GPI
  - GPI
  - Generic Product Identifier
taxon:
  - NCBITaxon:9606
---

# Medi-Span Generic Product Identifier

## Overview

The Medi-Span Generic Product Identifier (GPI) is a proprietary drug concept and
therapeutic classification system from Wolters Kluwer. The official Medi-Span description
emphasizes that GPI uses a 14-character hierarchical value structure to group and
identify drug products at multiple levels of granularity for screening, formulary,
and interoperability workflows.

Within KG-Registry, this entry represents the GPI terminology itself rather than
the broader Medi-Span commercial platform. Public documentation exists, but access
to the full maintained data appears to be subscription-mediated rather than distributed
as a public bulk download.

## Products

### Medi-Span GPI Documentation

Official product documentation describing GPI structure, use cases, and role in the
Medi-Span drug data suite.

### Medi-Span Customer Support

Support and customer-service entry point for access, account, and content questions
related to Medi-Span products.
