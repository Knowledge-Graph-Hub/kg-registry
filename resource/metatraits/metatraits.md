---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://metatraits.embl.de/
  label: EMBL
creation_date: '2026-02-21T00:00:00Z'
description: metaTraits is a unified and accessible microbial trait resource that
  integrates culture-derived trait information from BacDive, BV-BRC, JGI IMG, and
  GOLD, with genome-based predictions for medium- and high-quality isolate and metagenome-assembled
  genomes (MAGs) from proGenomes and SPIRE. metaTraits covers over 2.2 million genomes
  and more than 140 harmonized traits mapped to standardized ontologies, spanning
  cell morphology (e.g., shape, size, Gram staining), physiology (e.g., motility,
  sporulation), metabolic and enzymatic activities, environmental preferences (e.g.,
  temperature, salinity, oxygen tolerance), and lifestyle categories. All records
  are linked to their original evidence and cross-referenced to both NCBI and GTDB
  taxonomies.
domains:
- microbiology
- genomics
- microbiome
- biological systems
homepage_url: https://metatraits.embl.de/
id: metatraits
last_modified_date: '2026-05-29T00:00:00Z'
layout: resource_detail
name: metaTraits
products:
- category: GraphicalInterface
  description: Web interface to explore and query microbial trait data in metaTraits,
    covering over 2.2 million genomes and 140+ harmonized traits.
  format: http
  id: metatraits.site
  name: metaTraits Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  product_url: https://metatraits.embl.de/
- category: Product
  description: Trait data table listing all 140+ harmonized traits available in metaTraits,
    mapped to standardized ontologies.
  format: http
  id: metatraits.traits
  name: metaTraits Trait List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: goldterms
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:hadPrimarySource
    source: progenomes
  product_url: https://metatraits.embl.de/traits
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
taxon:
- NCBITaxon:2
---
metaTraits is a unified and accessible microbial trait resource that integrates culture-derived trait information from BacDive, BV-BRC, JGI IMG, and GOLD, with genome-based predictions for medium- and high-quality isolate and metagenome-assembled genomes (MAGs) from proGenomes and SPIRE.

metaTraits covers over 2.2 million genomes and more than 140 harmonized traits mapped to standardized ontologies, spanning cell morphology (e.g., shape, size, Gram staining), physiology (e.g., motility, sporulation), metabolic and enzymatic activities, environmental preferences (e.g., temperature, salinity, oxygen tolerance), and lifestyle categories. All records are linked to their original evidence and cross-referenced to both NCBI and GTDB taxonomies.