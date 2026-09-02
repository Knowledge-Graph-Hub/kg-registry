---
activity_status: active
category: Resource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: feedback@clinpgx.org
  label: ClinPGx
creation_date: '2026-09-02T00:00:00Z'
description: ClinPGx is a clinical pharmacogenomics knowledge resource that unifies
  the PharmGKB knowledge base, the CPIC prescribing guidelines and the PharmCAT
  genotype-to-phenotype tool under one site. It launched on 2025-07-30 as the
  successor to PharmGKB; pharmgkb.org and cpicpgx.org URLs redirect to their
  clinpgx.org equivalents and the PharmGKB bulk downloads are served from
  api.clinpgx.org. Content includes curated clinical and variant annotations,
  drug labels, pathways, gene-drug pairs drawn from CPIC, DPWG and FDA sources,
  and allele definition and frequency tables.
domains:
- biomedical
- chemistry and biochemistry
- clinical
- pharmacology
- genomics
- precision medicine
homepage_url: https://www.clinpgx.org/
id: clinpgx
last_modified_date: '2026-09-02T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC-BY-SA-4.0
name: ClinPGx
products:
- category: GraphicalInterface
  description: ClinPGx web portal for browsing genes, variants, drugs, clinical annotations,
    drug labels, pathways and CPIC guidelines, integrating PharmGKB and CPIC content
  id: clinpgx.portal
  is_public: true
  name: ClinPGx Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinpgx
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  - relation_type: prov:wasDerivedFrom
    source: cpic
  product_url: https://www.clinpgx.org/
- category: DocumentationProduct
  description: Downloads page listing the bulk data files (formerly the PharmGKB downloads),
    with data usage policy and file descriptions
  id: clinpgx.downloads
  is_public: true
  name: ClinPGx Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinpgx
  - relation_type: prov:wasDerivedFrom
    source: pharmgkb
  product_url: https://www.clinpgx.org/downloads
- category: ProgrammingInterface
  connection_url: https://api.clinpgx.org/
  description: REST API for ClinPGx data and bulk file downloads, keeping the path
    structure of the former PharmGKB API (for example /v1/download/file/data/)
  id: clinpgx.api
  is_public: true
  name: ClinPGx API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: clinpgx
  product_url: https://api.clinpgx.org/swagger/
taxon:
- NCBITaxon:9606
---

ClinPGx is the clinical pharmacogenomics resource that succeeded PharmGKB. It
brings PharmGKB, CPIC and PharmCAT together on one site.

## Transition from PharmGKB and CPIC

ClinPGx launched on 2025-07-30. From that date every pharmgkb.org link redirects
to its ClinPGx equivalent, and the standalone CPIC site (cpicpgx.org) redirects
into the CPIC section of ClinPGx. The bulk download files that PharmGKB served
from `api.pharmgkb.org` are served from `api.clinpgx.org` on the same paths.
The old API host no longer resolves.

In this registry the PharmGKB and CPIC pages are kept as separate resources.
Many downstream resources cite `pharmgkb` as a provenance source and that
identifier stays stable. The [PharmGKB](pharmgkb) page is marked inactive and
points here with `use_instead`. The [CPIC](cpic) page remains active because the
CPIC guidelines keep their own name and section within ClinPGx.

## Content

- Clinical annotations, variant annotations and drug label annotations curated
  from the literature and regulatory sources
- Gene-drug pairs annotated from CPIC, DPWG and FDA information
- Pathways, haplotype and allele definition tables, and allele frequency data
- CPIC prescribing guidelines and supporting tables
- PharmCAT, a tool for calling pharmacogenomic genotypes and phenotypes from
  sequence data

## Access

The portal is at https://www.clinpgx.org/. Bulk files are listed on the
downloads page and are fetched through the API host, for example
`https://api.clinpgx.org/v1/download/file/data/clinicalAnnotations.zip`. The
individual download files are listed as products on the [PharmGKB](pharmgkb)
page.

## Licensing

The download archives carry a `LICENSE.txt` stating the Creative Commons
Attribution-ShareAlike 4.0 International License, checked on 2026-09-02 against
`clinicalAnnotations_LOE1-2.zip`.

## Contact

Feedback address: feedback@clinpgx.org.
