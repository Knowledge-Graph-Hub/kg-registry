---
activity_status: active
category: DataSource
creation_date: '2026-02-26T00:00:00Z'
description: The Genome Taxonomy Database provides a standardized bacterial and archaeal
  taxonomy derived from genome phylogeny.
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
- category: Product
  description: Taxonomy crosswalk from GTDB release r220 to NCBI taxonomy (2025-07-28),
    with lineage context, genome counts, and majority-vote agreement fractions.
  format: mixed
  id: metatraits.gtdb2ncbi
  name: GTDB to NCBI Taxonomy Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: gtdb
  - relation_type: prov:wasDerivedFrom
    source: ncbi
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 2937650
  product_url: https://metatraits.embl.de/static/downloads/GTDB2NCBI.tsv.gz
- category: Product
  description: Taxonomy crosswalk from NCBI taxonomy (2025-07-28) to GTDB release
    r220, with lineage context, genome counts, and majority-vote agreement fractions.
  format: mixed
  id: metatraits.ncbi2gtdb
  name: NCBI to GTDB Taxonomy Mapping
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: gtdb
  - relation_type: prov:wasDerivedFrom
    source: ncbi
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 2895086
  product_url: https://metatraits.embl.de/static/downloads/NCBI2GTDB.tsv.gz
- category: Product
  description: Family-level harmonized trait annotations aggregated for GTDB taxonomy
    in compressed JSONL format.
  format: mixed
  id: metatraits.gtdb.family-summary
  name: metaTraits GTDB Family Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: gtdb
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: bv-brc
  - relation_type: prov:wasDerivedFrom
    source: goldterms
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 4575050
  product_url: https://metatraits.embl.de/static/downloads/gtdb_family_summary.jsonl.gz
- category: Product
  description: Genus-level harmonized trait annotations aggregated for GTDB taxonomy
    in compressed JSONL format.
  format: mixed
  id: metatraits.gtdb.genus-summary
  name: metaTraits GTDB Genus Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: gtdb
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: bv-brc
  - relation_type: prov:wasDerivedFrom
    source: goldterms
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 16364735
  product_url: https://metatraits.embl.de/static/downloads/gtdb_genus_summary.jsonl.gz
- category: Product
  description: Species-level harmonized trait annotations aggregated for GTDB taxonomy
    in compressed JSONL format.
  format: mixed
  id: metatraits.gtdb.species-summary
  name: metaTraits GTDB Species Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: gtdb
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: bv-brc
  - relation_type: prov:wasDerivedFrom
    source: goldterms
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 48114108
  product_url: https://metatraits.embl.de/static/downloads/gtdb_species_summary.jsonl.gz
---
# Genome Taxonomy Database

GTDB organizes bacterial and archaeal genomes into a standardized taxonomy and provides releases, trees, and associated data products for microbial comparative genomics.