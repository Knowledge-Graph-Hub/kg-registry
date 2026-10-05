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
    source: ncbi
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  product_file_size: 531
  product_url: https://w3id.org/biopragmatics/resources/ncbi.gc/ncbi.gc.tsv
- category: Product
  description: ncbi.gc OBO
  format: obo
  id: obo-db-ingest.ncbi.gc.obo
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: ncbi.gc OBO
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: ncbi
  product_file_size: 1425
  product_url: https://w3id.org/biopragmatics/resources/ncbi.gc/ncbi.gc.obo
- category: Product
  description: ncbi.gc OWL
  format: owl
  id: obo-db-ingest.ncbi.gc.owl
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: ncbi.gc OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: ncbi
  product_file_size: 2223
  product_url: https://w3id.org/biopragmatics/resources/ncbi.gc/ncbi.gc.owl
- category: Product
  description: ncbi.gc OBO Graph JSON
  format: json
  id: obo-db-ingest.ncbi.gc.json
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: ncbi.gc OBO Graph JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: ncbi
  product_file_size: 1886
  product_url: https://w3id.org/biopragmatics/resources/ncbi.gc/ncbi.gc.json
- category: MappingProduct
  description: ncbi.gc SSSOM
  format: sssom
  id: obo-db-ingest.ncbi.gc.sssom.tsv
  license:
    id: https://creativecommons.org/public-domain/pdm/
    label: public domain
  name: ncbi.gc SSSOM
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: ncbi
  product_file_size: 191
  product_url: https://w3id.org/biopragmatics/resources/ncbi.gc/ncbi.gc.sssom.tsv
- category: Product
  description: Full Bioregistry export as JSON, with every prefix record including
    names, synonyms, URI formats, local identifier patterns, providers and mappings
    to the prefixes of other registries.
  format: json
  id: bioregistry.registry.json
  name: Bioregistry JSON Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:wasInfluencedBy
    source: obofoundry
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  - relation_type: prov:wasInfluencedBy
    source: ols
  - relation_type: prov:wasInfluencedBy
    source: wikidata
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: cellosaurus
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  - relation_type: prov:wasInfluencedBy
    source: biolink
  - relation_type: prov:wasInfluencedBy
    source: n2t
  - relation_type: prov:wasInfluencedBy
    source: identifiers-org
  - relation_type: prov:wasInfluencedBy
    source: fairsharing
  - relation_type: prov:wasInfluencedBy
    source: re3data
  - relation_type: prov:wasInfluencedBy
    source: agroportal
  - relation_type: prov:wasInfluencedBy
    source: ecoportal
  - relation_type: prov:wasInfluencedBy
    source: aberowl
  product_file_size: 786637
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/registry/registry.json
- category: MappingProduct
  description: SSSOM mappings between Bioregistry prefixes and the equivalent prefixes
    in other registries, such as OBO Foundry, BioPortal, OLS, Wikidata, the Gene Ontology
    registry, Cellosaurus, UniProt and NCBI.
  format: sssom
  id: bioregistry.sssom
  name: Bioregistry SSSOM Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:wasInfluencedBy
    source: obofoundry
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  - relation_type: prov:wasInfluencedBy
    source: ols
  - relation_type: prov:wasInfluencedBy
    source: wikidata
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: cellosaurus
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  - relation_type: prov:wasInfluencedBy
    source: biolink
  - relation_type: prov:wasInfluencedBy
    source: n2t
  - relation_type: prov:wasInfluencedBy
    source: identifiers-org
  - relation_type: prov:wasInfluencedBy
    source: fairsharing
  - relation_type: prov:wasInfluencedBy
    source: re3data
  - relation_type: prov:wasInfluencedBy
    source: agroportal
  - relation_type: prov:wasInfluencedBy
    source: ecoportal
  - relation_type: prov:wasInfluencedBy
    source: aberowl
  product_file_size: 136267
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/sssom/bioregistry.sssom.tsv
- category: GraphicalInterface
  description: CNGBdb web portal for searching CNSA records and the integrated literature,
    gene, protein, sequence, organism, variation and other sub-databases, which include data
    from NCBI and EBI.
  format: http
  id: cngbdb.portal
  name: CNGBdb Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: cngbdb
  - relation_type: prov:wasDerivedFrom
    source: ncbi
  - relation_type: prov:wasDerivedFrom
    source: ena
  product_url: https://db.cngb.org/
- category: GraphicalInterface
  description: Search interface for metadata across DDBJ, DRA, BioProject, BioSample and JGA
    (study, dataset and policy records), with entry pages linking related records.
  format: http
  id: ddbj.search
  name: DDBJ Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ddbj
  - relation_type: prov:wasInfluencedBy
    source: ena
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  product_url: https://ddbj.nig.ac.jp/search
- category: ProgrammingInterface
  connection_url: https://getentry.ddbj.nig.ac.jp/getentry/
  description: getentry, a web service and URL-based API for retrieving INSDC nucleotide entries,
    translated protein entries and related records by accession number, in flat file, FASTA
    and other formats.
  format: http
  id: ddbj.getentry
  is_public: true
  name: DDBJ getentry
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ddbj
  - relation_type: prov:wasInfluencedBy
    source: ena
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  product_url: https://getentry.ddbj.nig.ac.jp/top-e.html
- category: GraphicalInterface
  description: ARSA (All-round Retrieval of Sequence and Annotation), a keyword and field
    search over INSDC nucleotide sequence records held at DDBJ.
  format: http
  id: ddbj.arsa
  name: DDBJ ARSA
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ddbj
  - relation_type: prov:wasInfluencedBy
    source: ena
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  product_url: https://ddbj.nig.ac.jp/arsa/
- category: Product
  compression: gzip
  description: Release flat files of the DDBJ nucleotide sequence database (division files
    such as ddbjbct*.seq.gz, accession indexes and file lists for release 143 at time of curation),
    plus TLS, TSA and WGS file lists.
  format: mixed
  id: ddbj.release
  name: DDBJ Release Files
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ddbj
  - relation_type: prov:wasInfluencedBy
    source: ena
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  product_url: https://ddbj.nig.ac.jp/public/ddbj_database/ddbj/
- category: Product
  description: BioProject XML records (all INSDC projects and the DDBJ-registered subset)
    with a summary file and XML schema.
  format: xml
  id: ddbj.bioproject
  name: DDBJ BioProject
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ddbj
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  product_url: https://ddbj.nig.ac.jp/public/ddbj_database/bioproject/
- category: Product
  compression: gzip
  description: BioSample XML records (all INSDC samples and the DDBJ-registered subset) with
    a summary file and XML schema.
  format: xml
  id: ddbj.biosample
  name: DDBJ BioSample
  original_source:
  - relation_type: prov:hadPrimarySource
    source: ddbj
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  product_url: https://ddbj.nig.ac.jp/public/ddbj_database/biosample/
---
# National Center for Biotechnology Information

NCBI is a major biomedical information resource at the U.S. National Library of Medicine, offering databases, search systems, analysis tools, and download services across genomics, literature, taxonomy, and related domains.

Its public platform spans popular resources such as PubMed, Gene, Protein, Genome, Taxonomy, and BLAST, and NCBI Datasets provides an increasingly broad API and download surface for genome, gene, taxonomy, virus, and BioSample workflows.