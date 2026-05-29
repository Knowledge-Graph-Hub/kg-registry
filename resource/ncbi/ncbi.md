---
activity_status: active
category: DataSource
creation_date: '2026-02-26T00:00:00Z'
description: The National Center for Biotechnology Information advances science and
  health by providing access to biomedical and genomic information, databases, tools,
  and services.
domains:
- biomedical
homepage_url: https://www.ncbi.nlm.nih.gov/
id: ncbi
last_modified_date: '2026-05-20T00:00:00Z'
layout: resource_detail
license:
  id: https://www.nlm.nih.gov/web_policies.html
  label: Public Domain
name: National Center for Biotechnology Information
products:
- category: DataModelProduct
  description: NCBI Genetic Codes tables summarizing translation tables used in GenBank
    and the NCBI taxonomy.
  id: ncbi.gc
  name: NCBI Genetic Codes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbi
  product_url: https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi
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
  description: Family-level harmonized trait annotations aggregated for NCBI taxonomy
    in compressed JSONL format.
  format: mixed
  id: metatraits.ncbi.family-summary
  name: metaTraits NCBI Family Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: ncbi
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: bv-brc
  - relation_type: prov:wasDerivedFrom
    source: goldterms
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 1540253
  product_url: https://metatraits.embl.de/static/downloads/ncbi_family_summary.jsonl.gz
- category: Product
  description: Genus-level harmonized trait annotations aggregated for NCBI taxonomy
    in compressed JSONL format.
  format: mixed
  id: metatraits.ncbi.genus-summary
  name: metaTraits NCBI Genus Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: ncbi
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: bv-brc
  - relation_type: prov:wasDerivedFrom
    source: goldterms
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 5417182
  product_url: https://metatraits.embl.de/static/downloads/ncbi_genus_summary.jsonl.gz
- category: Product
  description: Species-level harmonized trait annotations aggregated for NCBI taxonomy
    in compressed JSONL format.
  format: mixed
  id: metatraits.ncbi.species-summary
  name: metaTraits NCBI Species Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: ncbi
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: bv-brc
  - relation_type: prov:wasDerivedFrom
    source: goldterms
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 34062481
  product_url: https://metatraits.embl.de/static/downloads/ncbi_species_summary.jsonl.gz
---
# National Center for Biotechnology Information

NCBI is a major biomedical information resource at the U.S. National Library of Medicine, offering databases, search systems, analysis tools, and download services across genomics, literature, taxonomy, and related domains.