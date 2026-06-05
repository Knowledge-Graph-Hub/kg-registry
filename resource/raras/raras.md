---
activity_status: active
category: KnowledgeGraph
contacts:
  - category: Organization
    contact_details:
      - contact_type: email
        value: contato@raras.org
      - contact_type: url
        value: https://raras.org/sobre
    label: Raras Health Ltda
creation_date: '2026-05-26T00:00:00Z'
description: Raras is a Brazilian Portuguese-language rare disease knowledge platform and knowledge graph that connects diseases, phenotypes, genes, and patient-facing information. The platform presents a rare disease encyclopedia and knowledge map spanning more than 10,000 diseases, 11,000 phenotypes, and 5,000 genes.
domains:
  - biomedical
  - genomics
homepage_url: https://raras.org/
id: raras
last_modified_date: '2026-05-26T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-nc-sa/4.0/
  label: CC BY-NC-SA 4.0
name: Raras
products:
  - category: GraphicalInterface
    description: Main Raras portal for searching rare diseases, symptoms, genes, and patient communities
    format: http
    id: raras.portal
    name: Raras Portal
    original_source:
      - relation_type: prov:hadPrimarySource
        source: raras
      - relation_type: prov:wasInformedBy
        source: mondo
      - relation_type: prov:wasInformedBy
        source: omim
      - relation_type: prov:wasInformedBy
        source: orphanet
      - relation_type: prov:wasInformedBy
        source: icd10
      - relation_type: prov:wasInformedBy
        source: icd11
      - relation_type: prov:wasInformedBy
        source: wikidata
      - relation_type: prov:wasInformedBy
        source: clinvar
    product_url: https://raras.org/
  - category: GraphicalInterface
    description: Rare disease encyclopedia for browsing disease families, disease records, and related knowledge graph content
    format: http
    id: raras.encyclopedia
    name: Raras Encyclopedia
    original_source:
      - relation_type: prov:hadPrimarySource
        source: raras
      - relation_type: prov:wasInformedBy
        source: mondo
      - relation_type: prov:wasInformedBy
        source: omim
      - relation_type: prov:wasInformedBy
        source: orphanet
      - relation_type: prov:wasInformedBy
        source: icd10
      - relation_type: prov:wasInformedBy
        source: icd11
      - relation_type: prov:wasInformedBy
        source: wikidata
      - relation_type: prov:wasInformedBy
        source: clinvar
    product_url: https://raras.org/explorar
---

Raras is a Brazil-based Portuguese-language rare disease knowledge platform maintained
by Raras Health Ltda. It combines a patient- and clinician-facing portal with a knowledge
map that organizes rare disease information across diseases, phenotypes, genes, and
related research content.

The public site presents Raras as the largest rare disease database in Brazil and
exposes a searchable encyclopedia plus a graph-oriented knowledge map. As of the
current public homepage, the platform reports coverage of 10,468 rare diseases,
11,652 phenotypes, and 5,571 mapped genes.
