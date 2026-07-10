---
category: Product
description: Tab-delimited dbSNO 3.0 S-nitrosylation dataset containing UniProt identifiers,
  organisms, positions, and sequence context for manually curated and experimentally
  identified S-nitrosylated peptides.
format: tsv
id: dbsno.downloads
name: dbSNO Download Dataset
original_source:
- relation_type: prov:hadPrimarySource
  source: dbsno
product_url: https://biomics.lab.nycu.edu.tw/dbSNO/download.php
secondary_source:
- relation_type: prov:wasDerivedFrom
  source: pubmed
- relation_type: prov:wasDerivedFrom
  source: uniprot
warnings:
- File was not able to be retrieved when checked on 2026-07-03_ HTTP 500 error when
  accessing file
- File was not able to be retrieved when checked on 2026-06-27_ HTTP 500 error when
  accessing file. The dbSNO 3.0 download page (download.php) renders its page shell
  but the server errors before emitting download links; the rest of the site (index.php,
  statistics.php) is live (200).
layout: product_detail
---
