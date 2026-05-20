---
activity_status: active
category: DataSource
creation_date: '2026-02-26T00:00:00Z'
description: The Genome Taxonomy Database provides a standardized bacterial and archaeal taxonomy derived from genome phylogeny.
domains:
  - microbiology
homepage_url: https://gtdb.ecogenomic.org/
id: gtdb
last_modified_date: '2026-05-20T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC-BY-SA-4.0
name: Genome Taxonomy Database
products:
  - category: Product
    compression: gzip
    description: gtdb Nodes TSV
    format: tsv
    id: obo-db-ingest.gtdb.tsv
    license:
      id: https://creativecommons.org/licenses/by-sa/4.0/
      label: CC-BY-SA-4.0
    name: gtdb Nodes TSV
    original_source:
      - relation_type: prov:hadPrimarySource
        source: gtdb
      - relation_type: prov:hadPrimarySource
        source: obo-db-ingest
    product_file_size: 2918783
    product_url: https://w3id.org/biopragmatics/resources/gtdb/gtdb.tsv.gz
---

# Genome Taxonomy Database

GTDB organizes bacterial and archaeal genomes into a standardized taxonomy and provides releases, trees, and associated data products for microbial comparative genomics.
