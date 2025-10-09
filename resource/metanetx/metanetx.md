---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: help@metanetx.org
  - contact_type: url
    value: https://www.metanetx.org/
  label: MetaNetX Team - SIB Swiss Institute of Bioinformatics
description: MetaNetX is an online platform for accessing, analyzing, and manipulating
  genome-scale metabolic networks (GSM) and biochemical pathways, integrating data
  from multiple sources with a unified namespace for metabolites and biochemical reactions.
domains:
- biological systems
- chemistry and biochemistry
homepage_url: https://www.metanetx.org/
id: metanetx
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: MetaNetX
products:
- category: GraphicalInterface
  description: Web interface for exploring and analyzing metabolic networks
  id: metanetx.site
  is_public: true
  name: MetaNetX Web Interface
  original_source:
  - metanetx
  product_url: https://www.metanetx.org/
  secondary_source:
  - metanetx
- category: ProgrammingInterface
  description: SPARQL endpoint for querying MetaNetX RDF data
  id: metanetx.sparql
  is_public: true
  name: MetaNetX SPARQL Endpoint
  original_source:
  - metanetx
  product_url: https://rdf.metanetx.org/
  secondary_source:
  - metanetx
- category: Product
  description: MNXref unified namespace for metabolites across databases
  format: tsv
  id: metanetx.mnxref.metabolites
  name: MetaNetX MNXref Metabolites
  original_source:
  - metanetx
  product_url: https://www.metanetx.org/cgi-bin/mnxget/mnxref/chem_xref.tsv
  secondary_source:
  - metanetx
  warnings:
  - File was not able to be retrieved when checked on 2025-10-08_ No Content-Length
    header found
  - File was not able to be retrieved when checked on 2025-09-23_ Timeout connecting
    to URL
  - 'File was not able to be retrieved when checked on 2025-10-09: No Content-Length
    header found'
- category: Product
  description: MNXref unified namespace for reactions across databases
  format: tsv
  id: metanetx.mnxref.reactions
  name: MetaNetX MNXref Reactions
  original_source:
  - metanetx
  product_url: https://www.metanetx.org/cgi-bin/mnxget/mnxref/reac_xref.tsv
  secondary_source:
  - metanetx
  warnings:
  - 'File was not able to be retrieved when checked on 2025-09-16: No Content-Length
    header found'
  - File was not able to be retrieved when checked on 2025-09-14_ No Content-Length
    header found
- category: Product
  compression: gzip
  description: RDF version of the MetaNetX data for semantic web applications
  format: ttl
  id: metanetx.rdf
  name: MetaNetX RDF Data
  original_source:
  - metanetx
  product_file_size: 237044998
  product_url: https://www.metanetx.org/ftp/latest/metanetx.ttl.gz
  secondary_source:
  - metanetx
publications:
- authors:
  - Moretti S
  - Tran VDT
  - Mehl F
  - Ibberson M
  - Pagni M
  doi: doi:10.1093/nar/gkaa992
  id: doi:10.1093/nar/gkaa992
  preferred: true
  title: MetaNetX/MNXref - unified namespace for metabolites and biochemical reactions
    in the context of metabolic models
  year: '2021'
- authors:
  - Moretti S
  - Martin O
  - Tran VDT
  - Bridge A
  - Morgat A
  - Pagni M
  doi: doi:10.1093/nar/gkv1117
  id: doi:10.1093/nar/gkv1117
  title: MetaNetX/MNXref - reconciliation of metabolites and biochemical reactions
    to bring together genome-scale metabolic networks
  year: '2016'
- authors:
  - Ganter M
  - Bernard T
  - Moretti S
  - Stelling J
  - Pagni M
  doi: doi:10.1093/bioinformatics/btt036
  id: doi:10.1093/bioinformatics/btt036
  title: MetaNetX.org - a website and repository for accessing, analysing and manipulating
    metabolic networks
  year: '2013'
- authors:
  - Bernard T
  - Bridge A
  - Morgat A
  - Moretti S
  - Xenarios I
  - Pagni M
  doi: doi:10.1093/bib/bbs058
  id: doi:10.1093/bib/bbs058
  title: Reconciliation of metabolites and biochemical reactions for metabolic networks
  year: '2014'
---
MetaNetX is a comprehensive platform for accessing, analyzing, and manipulating genome-scale metabolic networks (GSMs) and biochemical pathways. Its primary focus is providing a unified namespace for metabolites and biochemical reactions in the context of metabolic models.

Key features of MetaNetX include:

- MNXref: A unified namespace and identifier system for metabolites and reactions across numerous biochemical databases
- Repository of curated metabolic models from various organisms
- Tools for metabolic network analysis, including flux balance analysis (FBA), reaction knockout analysis, and pathway visualization
- Support for building and customizing metabolic models from annotated genomes
- ID mapping services to convert between different database identifiers
- Semantic web interface through RDF and a SPARQL endpoint

MetaNetX integrates data from multiple major biochemical databases including KEGG, BiGG, MetaCyc, Rhea, and SEED, making it a valuable resource for metabolic modeling, systems biology, and biochemistry research. The platform is maintained by the Swiss Institute of Bioinformatics (SIB) with support from SystemsX.ch and other organizations.

The database provides access through a user-friendly web interface, programmatic access via a SPARQL endpoint, and downloadable data files containing the metabolite and reaction cross-references and other relevant data.