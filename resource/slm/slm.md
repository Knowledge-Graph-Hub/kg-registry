---
activity_status: active
category: DataSource
creation_date: '2026-02-26T00:00:00Z'
description: SwissLipids is a curated knowledge resource for lipids and their biology, providing information about lipid structures, metabolism, interactions, localization, provenance, and evidence.
domains:
  - chemistry and biochemistry
homepage_url: https://www.swisslipids.org/
id: slm
last_modified_date: '2026-05-20T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: SwissLipids
contacts:
  - category: Organization
    label: SwissLipids
    contact_details:
      - contact_type: email
        value: swisslipids@sib.swiss
      - contact_type: url
        value: https://www.swisslipids.org/
synonyms:
  - slm
products:
  - category: Product
    compression: gzip
    description: slm Nodes TSV
    format: tsv
    id: obo-db-ingest.slm.tsv
    license:
      id: https://creativecommons.org/licenses/by/4.0/
      label: CC-BY-4.0
    name: slm Nodes TSV
    original_source:
      - relation_type: prov:hadPrimarySource
        source: obo-db-ingest
      - relation_type: prov:hadPrimarySource
        source: slm
    product_file_size: 9655893
    product_url: https://w3id.org/biopragmatics/resources/slm/slm.tsv.gz
---

# SwissLipids

SwissLipids is maintained by SIB Swiss Institute of Bioinformatics as a curated resource for lipid biology, including lipid identifiers, structures, reactions, and linked evidence.
