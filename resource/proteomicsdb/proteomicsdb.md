---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.proteomicsdb.org/
  label: ProteomicsDB - Technical University of Munich
creation_date: '2026-06-17T00:00:00Z'
description: ProteomicsDB is a multi-omics and multi-organism resource for life
  science research, originally built to expedite the identification of the human
  proteome and to enable its use across the scientific community. It integrates
  quantitative proteomics, transcriptomics, and drug-sensitivity data with interactive
  analysis tools.
domains:
- proteomics
- biomedical
homepage_url: https://www.proteomicsdb.org/
id: proteomicsdb
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
name: ProteomicsDB
products:
- category: GraphicalInterface
  description: Web interface for exploring protein expression, peptides, and analysis
    tools across organisms.
  format: http
  id: proteomicsdb.site
  is_public: true
  name: ProteomicsDB Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  product_url: https://www.proteomicsdb.org/
- category: ProgrammingInterface
  description: REST API (with Swagger documentation) for programmatic access to
    ProteomicsDB data.
  format: http
  id: proteomicsdb.api
  is_public: true
  name: ProteomicsDB API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  product_url: https://www.proteomicsdb.org/swagger-ui.html
publications:
- authors:
  - Tobias Schmidt
  - Patroklos Samaras
  - Martin Frejno
  - Siegfried Gessulat
  - Maximilian Barnert
  - Harald Kienegger
  - Helmut Krcmar
  - Judith Schlegl
  - Hans-Christian Ehrlich
  - Stephan Aiche
  - Bernhard Kuster
  - Mathias Wilhelm
  doi: 10.1093/nar/gkx1029
  id: https://doi.org/10.1093/nar/gkx1029
  journal: Nucleic Acids Research
  preferred: true
  title: ProteomicsDB
  year: '2018'
---
# ProteomicsDB

ProteomicsDB is a protein-centric, multi-omics resource originally developed at the
Technical University of Munich to support assembly and exploration of the human proteome.
It has since expanded to integrate data across multiple organisms and data types.

Content and features include:

- Quantitative protein and peptide expression data across tissues, cell lines, and fluids
- Integration of transcriptomics and drug-sensitivity data
- Interactive visualization and analysis tools
- A documented REST API for programmatic access

GeneCards integrates proteomic expression data from ProteomicsDB.
