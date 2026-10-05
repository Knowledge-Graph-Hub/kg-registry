---
category: ProgrammingInterface
description: MyVariant.info REST API (v1) for variant query and annotation retrieval
  by HGVS id or rsid, with batch POST queries and field filtering. Returns JSON documents
  merged from the integrated sources, on hg19 and hg38.
format: http
id: myvariant.api
infores_id: myvariant-info
name: MyVariant.info API
original_source:
- relation_type: prov:hadPrimarySource
  source: myvariant
- relation_type: prov:hadPrimarySource
  source: dbsnp
- relation_type: prov:hadPrimarySource
  source: clinvar
- relation_type: prov:hadPrimarySource
  source: gnomad
- relation_type: prov:hadPrimarySource
  source: civic
- relation_type: prov:hadPrimarySource
  source: cosmic
- relation_type: prov:hadPrimarySource
  source: docm
- relation_type: prov:hadPrimarySource
  source: cancer-genome-interpreter
- relation_type: prov:hadPrimarySource
  source: gwascatalog
- relation_type: prov:hadPrimarySource
  source: snpeff
product_url: https://myvariant.info/v1/query
layout: product_detail
---
