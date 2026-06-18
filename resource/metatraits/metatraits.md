---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://metatraits.embl.de/
  - contact_type: email
    value: bork@embl.de
  id: european-molecular-biology-laboratory-embl
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
- biological systems
homepage_url: https://metatraits.embl.de/
id: metatraits
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
license:
  id: http://creativecommons.org/licenses/by-sa/4.0/
  label: CC-BY-SA-4.0
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
  description: Family-level harmonized trait annotations aggregated for NCBI taxonomy
    in compressed TSV format.
  format: tsv
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
  product_file_size: 913932
  product_url: https://www.bork.embl.de/~robbani/metatraits/ncbi_family_summary_no_predictions.tsv.gz
- category: Product
  description: Genus-level harmonized trait annotations aggregated for NCBI taxonomy
    in compressed TSV format.
  format: tsv
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
  product_file_size: 2431808
  product_url: https://www.bork.embl.de/~robbani/metatraits/ncbi_genus_summary_no_predictions.tsv.gz
- category: Product
  description: Species-level harmonized trait annotations aggregated for NCBI taxonomy
    in compressed TSV format.
  format: tsv
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
  product_file_size: 6523019
  product_url: https://www.bork.embl.de/~robbani/metatraits/ncbi_species_summary_no_predictions.tsv.gz
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
  - Podlesny D
  - Kim CY
  - Robbani SM
  - Schudoma C
  - Fullam A
  - Reimer LC
  - Koblitz J
  - Schober I
  - Iyappan A
  - Van Rossum T
  - Schiller J
  - Grekova A
  - Kuhn M
  - Bork P
  doi: doi:10.1093/nar/gkaf1241
  id: https://doi.org/10.1093/nar/gkaf1241
  journal: Nucleic Acids Research
  preferred: true
  title: 'metaTraits: a large-scale integration of microbial phenotypic trait information'
  year: '2026'
repository: https://github.com/grp-bork/porTraits
taxon:
- NCBITaxon:2
---
metaTraits is a unified and accessible microbial trait resource that integrates culture-derived trait information from BacDive, BV-BRC, JGI IMG, and GOLD, with genome-based predictions for medium- and high-quality isolate and metagenome-assembled genomes (MAGs) from proGenomes and SPIRE.

metaTraits covers over 2.2 million genomes and more than 140 harmonized traits mapped to standardized ontologies, spanning cell morphology (e.g., shape, size, Gram staining), physiology (e.g., motility, sporulation), metabolic and enzymatic activities, environmental preferences (e.g., temperature, salinity, oxygen tolerance), and lifestyle categories. All records are linked to their original evidence and cross-referenced to both NCBI and GTDB taxonomies.