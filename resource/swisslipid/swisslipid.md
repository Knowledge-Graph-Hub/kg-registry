---
layout: resource_detail
activity_status: active
id: swisslipid
name: swisslipid
description: SwissLipids is a knowledge resource for lipids and their biology.
domains:
- chemistry and biochemistry
contacts:
- category: Organization
  label: SwissLipids team
  contact_details:
  - contact_type: email
    value: swisslipids@sib.swiss
homepage_url: https://www.swisslipids.org/
repository: https://www.swisslipids.org/
category: DataSource
last_modified_date: '2026-02-20T00:00:00Z'
publications:
- doi: doi:10.1093/bioinformatics/btv285
  id: doi:10.1093/bioinformatics/btv285
  preferred: true
  year: '2015'
  authors:
  - Aimo L
  - Liechti R
  - Hyka-Nouspikel N
  - Niknejad A
  - Gleizes A
  - "G\xF6tz L"
  - Kuznetsov D
  - David FPA
  - van der Goot FG
  - Riezman H
  - Bougueleret L
  - Xenarios I
  - Bridge A
  title: The SwissLipids knowledgebase for lipid biology
products:
- category: GraphicalInterface
  description: Main SwissLipids interface for browsing lipid classes and analytes.
  format: http
  id: swisslipid.portal
  name: SwissLipids Portal
  original_source:
  - swisslipid
  product_url: https://www.swisslipids.org/
- category: Product
  description: TSV export of lipid-related enzymes with UniProt, Rhea, and evidence links.
  format: tsv
  id: swisslipid.enzymes
  name: SwissLipids Enzymes
  original_source:
  - swisslipid
  - uniprot
  - rhea
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=enzymes.tsv
- category: Product
  description: TSV export of evidence annotations including ECO terms and supporting PMIDs.
  format: tsv
  id: swisslipid.evidences
  name: SwissLipids Evidences
  original_source:
  - swisslipid
  - eco
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=evidences.tsv
- category: Product
  description: TSV export of SwissLipids links to Gene Ontology terms with taxon context.
  format: tsv
  id: swisslipid.go
  name: SwissLipids GO Annotations
  original_source:
  - swisslipid
  - go
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=go.tsv
- category: Product
  description: Comprehensive TSV catalogue of SwissLipids lipid entities and identifiers.
  format: tsv
  id: swisslipid.lipids
  name: SwissLipids Lipids
  original_source:
  - swisslipid
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=lipids.tsv
- category: MappingProduct
  description: TSV mapping between SwissLipids lipid entries and UniProtKB proteins.
  format: tsv
  id: swisslipid.lipids2uniprot
  name: SwissLipids Lipids to UniProt
  original_source:
  - swisslipid
  - uniprot
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=lipids2uniprot.tsv
- category: Product
  description: TSV export of lipid tissue and cell annotations with taxon and evidence tags.
  format: tsv
  id: swisslipid.tissues
  name: SwissLipids Tissues
  original_source:
  - swisslipid
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=tissues.tsv
- category: ProgrammingInterface
  connection_url: https://www.swisslipids.org/#/api
  description: Public API page for programmatic SwissLipids access.
  format: http
  id: swisslipid.api
  is_public: true
  name: SwissLipids API
  original_source:
  - swisslipid
  product_url: https://www.swisslipids.org/#/api
---

SwissLipids is a knowledge resource for lipids and their biology.
