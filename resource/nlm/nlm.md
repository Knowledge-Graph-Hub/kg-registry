---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://support.nlm.nih.gov/
  label: National Library of Medicine
creation_date: '2026-02-26T00:00:00Z'
description: The National Library of Medicine is the world's largest biomedical library
  and a national resource for health professionals, scientists, and the public.
domains:
- biomedical
- literature
homepage_url: https://www.nlm.nih.gov/
id: nlm
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
license:
  id: https://www.nlm.nih.gov/web_policies.html
  label: Public Domain
name: National Library of Medicine
products:
- category: DocumentationProduct
  description: NLM public homepage and organizational entry point for literature,
    terminology, clinical, and informatics resources.
  format: http
  id: nlm.portal
  name: NLM Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_url: https://www.nlm.nih.gov/
- category: Product
  description: nlm Nodes TSV
  format: tsv
  id: obo-db-ingest.nlm.tsv
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nlm
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 1156325
  product_url: https://w3id.org/biopragmatics/resources/nlm/nlm.tsv
- category: MappingProduct
  description: nlm.publisher SSSOM
  format: sssom
  id: obo-db-ingest.nlm.publisher.sssom.tsv
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm.publisher SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nlm
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 140
  product_url: https://w3id.org/biopragmatics/resources/nlm.publisher/nlm.publisher.sssom.tsv
- category: Product
  description: nlm.publisher Nodes TSV
  format: tsv
  id: obo-db-ingest.nlm.publisher.tsv
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm.publisher Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: nlm
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 8289
  product_url: https://w3id.org/biopragmatics/resources/nlm.publisher/nlm.publisher.tsv
- category: Product
  description: nlm OBO
  format: obo
  id: obo-db-ingest.nlm.obo
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_file_size: 2007193
  product_url: https://w3id.org/biopragmatics/resources/nlm/nlm.obo
- category: Product
  description: nlm OWL
  format: owl
  id: obo-db-ingest.nlm.owl
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_file_size: 2471988
  product_url: https://w3id.org/biopragmatics/resources/nlm/nlm.owl
- category: Product
  description: nlm OBO Graph JSON
  format: json
  id: obo-db-ingest.nlm.json
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_file_size: 2497051
  product_url: https://w3id.org/biopragmatics/resources/nlm/nlm.json
- category: MappingProduct
  description: nlm SSSOM
  format: sssom
  id: obo-db-ingest.nlm.sssom.tsv
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_file_size: 422890
  product_url: https://w3id.org/biopragmatics/resources/nlm/nlm.sssom.tsv
- category: Product
  description: nlm.publisher OBO
  format: obo
  id: obo-db-ingest.nlm.publisher.obo
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm.publisher OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_file_size: 9570
  product_url: https://w3id.org/biopragmatics/resources/nlm.publisher/nlm.publisher.obo
- category: Product
  description: nlm.publisher OWL
  format: owl
  id: obo-db-ingest.nlm.publisher.owl
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm.publisher OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_file_size: 12531
  product_url: https://w3id.org/biopragmatics/resources/nlm.publisher/nlm.publisher.owl
- category: Product
  description: nlm.publisher OBO Graph JSON
  format: json
  id: obo-db-ingest.nlm.publisher.json
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: nlm.publisher OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: nlm
  product_file_size: 12675
  product_url: https://w3id.org/biopragmatics/resources/nlm.publisher/nlm.publisher.json
---
# National Library of Medicine

NLM develops and maintains biomedical literature, terminology, health information, and informatics resources that support discovery, interoperability, and public access to health knowledge.

As part of NIH, the library serves as the institutional home for widely used resources such as PubMed, ClinicalTrials.gov, MeSH, and the UMLS terminology ecosystem, alongside intramural biomedical informatics research and public-facing health information services.