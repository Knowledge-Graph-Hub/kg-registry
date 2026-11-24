---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.lifemapsc.com/
  label: LifeMap Sciences
creation_date: '2026-11-24T00:00:00Z'
description: PathCards is a database of human biological pathways in the GeneCards Suite. It
  consolidates pathways from multiple sources into SuperPaths by clustering on gene content.
  Version 5.26 reports 1,686 SuperPath entries from 11 sources; the 2015 publication describes
  1,073 SuperPaths from 3,215 pathways in 12 sources.
domains:
- pathways
- biomedical
- systems biology
homepage_url: https://pathcards.genecards.org/
id: pathcards
last_modified_date: '2026-11-24T00:00:00Z'
layout: resource_detail
license:
  id: https://www.lifemapsc.com/genecards-suite-terms-of-use/
  label: Free for non-profit academic/hospital use; commercial license required (proprietary,
    LifeMap Sciences)
name: PathCards
products:
- category: GraphicalInterface
  description: Web interface for searching SuperPaths, with their constituent pathways, pathway
    networks, and genes.
  format: http
  id: pathcards.portal
  name: PathCards Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathcards
  product_url: https://pathcards.genecards.org/
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: genecards
publications:
- authors:
  - Frida Belinky
  - Noam Nativ
  - Gil Stelzer
  - Shahar Zimmerman
  - Tsippi Iny Stein
  - Marilyn Safran
  - Doron Lancet
  doi: 10.1093/database/bav006
  id: doi:10.1093/database/bav006
  journal: Database
  preferred: true
  title: 'PathCards: multi-source consolidation of human biological pathways'
  year: '2015'
taxon:
- NCBITaxon:9606
version: '5.26'
warnings:
- The GeneCards Suite terms of use prohibit automated scraping and prohibit use of the data
  for training AI models without written permission from LifeMap Sciences (read 2026-11-24).
---

# PathCards

PathCards is a member of the GeneCards Suite, from the Weizmann Institute of Science and LifeMap
Sciences. Each card covers one SuperPath, a group of human pathways with similar gene content.
