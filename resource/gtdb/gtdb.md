---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://gtdb.ecogenomic.org/
  label: Genome Taxonomy Database
creation_date: '2026-02-26T00:00:00Z'
description: The Genome Taxonomy Database provides a standardized bacterial and archaeal
  taxonomy derived from genome phylogeny.
domains:
- genomics
- microbiology
homepage_url: https://gtdb.ecogenomic.org/
id: gtdb
last_modified_date: '2026-06-18T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC-BY-SA-4.0
name: Genome Taxonomy Database
products:
- category: DocumentationProduct
  description: GTDB downloads page listing release mirrors, data files, and related
    software such as GTDB-Tk.
  format: http
  id: gtdb.downloads
  name: GTDB Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtdb
  product_url: https://gtdb.ecogenomic.org/downloads
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
  format: tsv
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
  product_url: https://www.bork.embl.de/~robbani/metatraits/GTDB2NCBI.tsv.gz
- category: Product
  description: Taxonomy crosswalk from NCBI taxonomy (2025-07-28) to GTDB release
    r220, with lineage context, genome counts, and majority-vote agreement fractions.
  format: tsv
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
  product_url: https://www.bork.embl.de/~robbani/metatraits/NCBI2GTDB.tsv.gz
- category: Product
  description: Family-level harmonized trait annotations aggregated for GTDB taxonomy
    in compressed TSV format.
  format: tsv
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
  product_file_size: 1513013
  product_url: https://www.bork.embl.de/~robbani/metatraits/gtdb_family_summary_no_predictions.tsv.gz
- category: Product
  description: Genus-level harmonized trait annotations aggregated for GTDB taxonomy
    in compressed TSV format.
  format: tsv
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
  product_file_size: 4965442
  product_url: https://www.bork.embl.de/~robbani/metatraits/gtdb_genus_summary_no_predictions.tsv.gz
- category: Product
  description: Species-level harmonized trait annotations aggregated for GTDB taxonomy
    in compressed TSV format.
  format: tsv
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
  product_file_size: 12570522
  product_url: https://www.bork.embl.de/~robbani/metatraits/gtdb_species_summary_no_predictions.tsv.gz
publications:
- authors:
  - Parks DH
  - Chuvochina M
  - Rinke C
  - Mussig AJ
  - Chaumeil PA
  - Hugenholtz P
  doi: 10.1093/nar/gkab776
  id: https://www.ncbi.nlm.nih.gov/pubmed/34520557
  journal: Nucleic Acids Res
  preferred: true
  title: 'GTDB: an ongoing census of bacterial and archaeal diversity through a phylogenetically
    consistent, rank normalized and complete genome-based taxonomy'
  year: '2022'
---
# Genome Taxonomy Database

GTDB organizes bacterial and archaeal genomes into a standardized taxonomy and provides releases, trees, and associated data products for microbial comparative genomics.

The public GTDB portal publishes genome-phylogeny-based bacterial and archaeal classifications, current release statistics, and mirrored download endpoints for taxonomy releases and supporting tools used in genome classification workflows.