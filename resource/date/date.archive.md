---
category: Product
compression: zip
description: 'ZIP with two TSV files: Drug_target_reactome_pathway.tsv (611,655 rows)
  and Drug_target_reactome_pathway_filtered.tsv (238,317 rows, parent pathways removed),
  with columns for expression dataset, drug name and STITCH ID, tissue, cell line,
  target UniProt ID and symbol, target class, pathway and pathway size.'
dump_format: other
format: tsv
id: date.archive
name: DATE Archive ZIP
original_source:
- relation_type: prov:hadPrimarySource
  source: date
- relation_type: prov:hadPrimarySource
  source: drugbank
- relation_type: prov:hadPrimarySource
  source: reactome
- relation_type: prov:hadPrimarySource
  source: gtex
- relation_type: prov:hadPrimarySource
  source: biogps
- relation_type: prov:hadPrimarySource
  source: stitch
- relation_type: prov:hadPrimarySource
  source: uniprot
- relation_type: prov:hadPrimarySource
  source: gtopdb
- relation_type: prov:hadPrimarySource
  source: nci60
- relation_type: prov:hadPrimarySource
  source: human-proteome-map
product_file_size: 7261526
product_url: https://tatonettilab-resources.s3.amazonaws.com/syspharm/DATE.zip
layout: product_detail
---
