---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    label: GARD Information Specialists
    contact_details:
      - contact_type: url
        value: "https://contact.rarediseases.info.nih.gov/Gard/s/?language=en_US"
creation_date: '2026-02-26T00:00:00Z'
description: The Genetic and Rare Diseases Information Center provides free, reliable, and easy-to-understand information and resources about rare and genetic diseases.
domains:
  - biomedical
homepage_url: https://rarediseases.info.nih.gov/
id: "gard"
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
name: Genetic and Rare Diseases Information Center
products:
  - category: DocumentationProduct
    description: Public GARD website for disease summaries, support resources, and contact-center access.
    format: http
    id: "gard.portal"
    name: GARD Web Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: gard
    product_url: https://rarediseases.info.nih.gov/
  - category: Product
    description: gard Nodes TSV
    format: tsv
    id: "obo-db-ingest.gard.tsv"
    name: gard Nodes TSV
    original_source:
      - relation_type: prov:hadPrimarySource
        source: gard
      - relation_type: prov:hadPrimarySource
        source: obo-db-ingest
    product_file_size: 314439
    product_url: https://w3id.org/biopragmatics/resources/gard/gard.tsv
---

# Genetic and Rare Diseases Information Center

GARD is an NCATS/NIH information service that helps patients, families, and clinicians find current, reliable information and support resources for rare and genetic diseases.

The service combines a large browseable disease catalog with a contact center staffed by information specialists, making it both a public information portal and a curated referral resource for people navigating diagnosis, care, research, and support options in the rare disease community.
