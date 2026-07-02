---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://ncats.nih.gov/
  label: National Center for Advancing Translational Sciences (NCATS)
creation_date: '2026-06-18T00:00:00Z'
description: CURE ID is a crowdsourcing platform and mobile/web app developed by the
  U.S. National Center for Advancing Translational Sciences (NCATS) at NIH in collaboration
  with the U.S. Food and Drug Administration (FDA). It allows clinicians around the
  world to report and share real-world clinical experiences treating difficult-to-treat
  and rare diseases, with an emphasis on novel uses of existing (off-label) drugs.
  The collected case reports and treatment outcomes form a repository intended to
  surface promising therapies and inform clinical research. CURE ID serves as an upstream
  ingest source for the Monarch/SRI Reference Knowledge Graph.
domains:
- clinical
- drug discovery
- public health
homepage_url: https://cure.ncats.io/
id: cureid
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: ''
  label: Not specified
name: CURE ID
products:
- category: GraphicalInterface
  description: Web application for exploring and contributing crowdsourced real-world
    clinical treatment cases for difficult-to-treat and rare diseases, including off-label
    drug use.
  format: http
  id: cureid.app
  name: CURE ID Web App
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cureid
  product_url: https://cure.ncats.io/
- category: GraphicalInterface
  description: Browseable interface for exploring diseases, treatments, and submitted
    clinical case reports within the CURE ID platform.
  format: http
  id: cureid.explore
  name: CURE ID Explore
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cureid
  product_url: https://cure.ncats.io/explore
- category: DocumentationProduct
  description: About page describing the CURE ID initiative, its NCATS/FDA partnership,
    and how clinicians can participate.
  id: cureid.about
  name: CURE ID About
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cureid
  product_url: https://cure.ncats.io/about
  warnings:
  - 'File was not able to be retrieved when checked on 2026-07-02: HTTP 404 error
    when accessing file'
- category: GraphProduct
  description: KGX distribution of the SRI-Reference KG
  format: kgx
  id: sri-reference-kg.graph
  name: SRI-Reference KG (KGX distribution)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: sri-reference-kg
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dictybase
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: goa
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pombase
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: wormbase
  - relation_type: prov:hadPrimarySource
    source: xenbase
  - relation_type: prov:hadPrimarySource
    source: zfin
  - relation_type: prov:hadPrimarySource
    source: phenio
  - relation_type: prov:hadPrimarySource
    source: bfo
  - relation_type: prov:hadPrimarySource
    source: bspo
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: cl
  - relation_type: prov:hadPrimarySource
    source: ddanat
  - relation_type: prov:hadPrimarySource
    source: ddpheno
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: dpo
  - relation_type: prov:hadPrimarySource
    source: eco
  - relation_type: prov:hadPrimarySource
    source: emapa
  - relation_type: prov:hadPrimarySource
    source: fbbt
  - relation_type: prov:hadPrimarySource
    source: fbdv
  - relation_type: prov:hadPrimarySource
    source: foodon
  - relation_type: prov:hadPrimarySource
    source: fypo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hsapdv
  - relation_type: prov:hadPrimarySource
    source: maxo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: mp
  - relation_type: prov:hadPrimarySource
    source: mpath
  - relation_type: prov:hadPrimarySource
    source: nbo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: oba
  - relation_type: prov:hadPrimarySource
    source: ordo
  - relation_type: prov:hadPrimarySource
    source: pato
  - relation_type: prov:hadPrimarySource
    source: pr
  - relation_type: prov:hadPrimarySource
    source: ro
  - relation_type: prov:hadPrimarySource
    source: so
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: upheno
  - relation_type: prov:hadPrimarySource
    source: wbbt
  - relation_type: prov:hadPrimarySource
    source: wbls
  - relation_type: prov:hadPrimarySource
    source: wbphenotype
  - relation_type: prov:hadPrimarySource
    source: xao
  - relation_type: prov:hadPrimarySource
    source: xpo
  - relation_type: prov:hadPrimarySource
    source: zfa
  - relation_type: prov:hadPrimarySource
    source: zfs
  - relation_type: prov:hadPrimarySource
    source: zp
  - relation_type: prov:hadPrimarySource
    source: icd10cm
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: decipher
  - relation_type: prov:hadPrimarySource
    source: mmrrc
  - relation_type: prov:hadPrimarySource
    source: cureid
  - relation_type: prov:hadPrimarySource
    source: phenopacket-store
  product_file_size: 230046094
  product_url: https://data.monarchinitiative.org/monarch-kg-dev/latest/monarch-kg.tar.gz
---
# CURE ID

## Description

CURE ID is an NIH/NCATS and FDA crowdsourcing platform and app that lets clinicians worldwide report and share real-world clinical experiences treating difficult-to-treat and rare diseases. It focuses especially on novel, off-label uses of existing approved drugs, building a community-driven repository of case reports and treatment outcomes. These data are intended to help identify promising therapies and prioritize candidates for formal clinical research. CURE ID is used as an upstream ingest source for the Monarch/SRI Reference Knowledge Graph.

## Products

- **CURE ID Web App** (GraphicalInterface) — the main web/mobile application for contributing and exploring crowdsourced clinical treatment cases.
- **CURE ID Explore** (GraphicalInterface) — interface for browsing diseases, drugs, and submitted case reports.
- **CURE ID About** (DocumentationProduct) — overview of the initiative and the NCATS/FDA partnership.