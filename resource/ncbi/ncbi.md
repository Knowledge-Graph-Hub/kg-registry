---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://support.nlm.nih.gov/?pagename=guide%3ANONE%3AHomePage%3ANONE
  label: NCBI and NLM Support
creation_date: '2026-02-26T00:00:00Z'
description: The National Center for Biotechnology Information advances science and
  health by providing access to biomedical and genomic information, databases, tools,
  and services.
domains:
- biomedical
- genomics
- literature
homepage_url: https://www.ncbi.nlm.nih.gov/
id: ncbi
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
license:
  id: https://www.nlm.nih.gov/web_policies.html
  label: Public Domain
name: National Center for Biotechnology Information
products:
- category: DocumentationProduct
  description: NCBI Datasets API documentation for genome, gene, taxonomy, virus,
    and BioSample programmatic access.
  format: http
  id: ncbi.datasets-api
  name: NCBI Datasets API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbi
  product_url: https://www.ncbi.nlm.nih.gov/datasets/docs/v2/api/rest-api/
- category: DataModelProduct
  description: NCBI Genetic Codes tables summarizing translation tables used in GenBank
    and the NCBI taxonomy.
  format: http
  id: ncbi.gc
  name: NCBI Genetic Codes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbi
  product_url: https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi
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
  description: ncbi.gc Nodes TSV
  format: tsv
  id: obo-db-ingest.ncbi.gc.tsv
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: ncbi.gc Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ncbi.gc
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 531
  product_url: https://w3id.org/biopragmatics/resources/ncbi.gc/ncbi.gc.tsv
---
# National Center for Biotechnology Information

NCBI is a major biomedical information resource at the U.S. National Library of Medicine, offering databases, search systems, analysis tools, and download services across genomics, literature, taxonomy, and related domains.

Its public platform spans popular resources such as PubMed, Gene, Protein, Genome, Taxonomy, and BLAST, and NCBI Datasets provides an increasingly broad API and download surface for genome, gene, taxonomy, virus, and BioSample workflows.