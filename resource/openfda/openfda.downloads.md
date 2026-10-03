---
category: Product
compression: zip
description: Bulk downloads of every openFDA endpoint as zipped JSON files, split
  into partitions for large datasets such as drug adverse events (FAERS) and device
  adverse events (MAUDE), with a machine-readable manifest at https://api.fda.gov/download.json
  listing each endpoint's export date and file partitions.
format: json
id: openfda.downloads
name: openFDA Bulk Downloads
original_source:
- relation_type: prov:hadPrimarySource
  source: openfda
- relation_type: prov:hadPrimarySource
  source: faers
- relation_type: prov:hadPrimarySource
  source: maude
- relation_type: prov:hadPrimarySource
  source: ndcd
- relation_type: prov:hadPrimarySource
  source: fda-orange-book
- relation_type: prov:hadPrimarySource
  source: unii
product_url: https://open.fda.gov/data/downloads/
layout: product_detail
---
