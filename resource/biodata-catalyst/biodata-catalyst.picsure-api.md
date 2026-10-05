---
category: ProgrammingInterface
description: PIC-SURE REST API for programmatic query and export of BDC study variables,
  used through the PicSureClient and PicSureBdcAdapter Python packages (and an R client)
  with a personal access token from the PIC-SURE interface.
format: http
id: biodata-catalyst.picsure-api
is_public: false
name: BDC PIC-SURE API
original_source:
- relation_type: prov:hadPrimarySource
  source: biodata-catalyst
- relation_type: prov:hadPrimarySource
  source: topmed
product_url: https://picsure.biodatacatalyst.nhlbi.nih.gov/picsure/
secondary_source:
- relation_type: prov:wasInfluencedBy
  source: dbgap
warnings:
- API endpoint returned HTTP 401 Unauthorized for anonymous requests when checked
  on 2026-10-05; a PIC-SURE access token is required.
layout: product_detail
---
