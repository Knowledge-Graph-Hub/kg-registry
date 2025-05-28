---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/taxonomy
  label: NCBI Taxonomy Database
- category: Organization
  contact_details:
  - contact_type: email
    value: info@ncbi.nlm.nih.gov
  label: NCBI Help Desk
description: The NCBI Taxonomy Database is the standard nomenclature and classification repository for the International Nucleotide Sequence Database Collaboration (INSDC), comprising the GenBank, ENA (EMBL), and DDBJ databases. It includes organism names and taxonomic lineages for each of the sequences represented in the INSDC's nucleotide and protein sequence databases. The taxonomy database is manually curated by a small group of scientists at the NCBI who use current taxonomic literature to maintain a phylogenetic taxonomy for source organisms represented in sequence databases.
domains:
- organisms
- taxonomy
- biology
- biodiversity
fairsharing_id: FAIRsharing.fj07xj
homepage_url: https://www.ncbi.nlm.nih.gov/taxonomy
id: ncbitaxon
layout: resource_detail
name: NCBI Taxonomy
products:
- category: GraphProduct
  description: NCBI Taxonomy database in dump format containing hierarchical taxonomic classification data
  format: ascii
  id: ncbitaxon.dump
  name: NCBI Taxonomy Dump Files
  original_source:
  - ncbitaxon
  product_url: https://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz
- category: GraphProduct
  description: NCBI Taxonomy containing the new-style taxonomy dump files with extended node data
  format: ascii
  id: ncbitaxon.new_dump
  name: NCBI Taxonomy New-Style Dump Files
  original_source:
  - ncbitaxon
  product_url: https://ftp.ncbi.nih.gov/pub/taxonomy/new_taxdump/new_taxdump.tar.gz
- category: GraphicalInterface
  description: Web interface for browsing and searching the NCBI Taxonomy database
  id: ncbitaxon.web
  name: NCBI Taxonomy Browser
  original_source:
  - ncbitaxon
  product_url: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi
- category: DataModelProduct
  description: OWL format version of the NCBI Taxonomy, automatically translated from the NCBI taxonomy database
  format: owl
  id: ncbitaxon.owl
  name: NCBI Taxonomy OWL
  original_source:
  - ncbitaxon
  product_url: http://purl.obolibrary.org/obo/ncbitaxon.owl
- category: DataModelProduct
  description: OBO format version of the NCBI Taxonomy, providing a standardized representation for use with other OBO ontologies
  format: obo
  id: ncbitaxon.obo
  name: NCBI Taxonomy OBO
  original_source:
  - ncbitaxon
  product_url: http://purl.obolibrary.org/obo/ncbitaxon.obo
- category: DataModelProduct
  description: OBOGraphs JSON version of the NCBI Taxonomy
  format: json
  id: ncbitaxon.json
  name: NCBI Taxonomy JSON
  original_source:
  - ncbitaxon
  product_url: http://purl.obolibrary.org/obo/ncbitaxon.json
- category: DataModelProduct
  description: Slimmed-down version of the NCBI Taxonomy ontology containing commonly used taxa
  format: owl
  id: ncbitaxon.taxslim
  name: NCBI Taxonomy Slim
  original_source:
  - ncbitaxon
  product_url: http://purl.obolibrary.org/obo/ncbitaxon/subsets/taxslim.owl
publications:
- authors:
  - "Scott Federhen"
  id: doi:10.1093/nar/gkr1178
  journal: "Nucleic Acids Research"
  preferred: true
  title: "The NCBI Taxonomy database"
  year: "2012"
repository: https://github.com/obophenotype/ncbitaxon
license:
  url: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
---