---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: swisslipids@sib.swiss
  label: SwissLipids team
creation_date: '2025-03-09T00:00:00Z'
description: SwissLipids is a knowledge resource for lipids and their biology.
domains:
- chemistry and biochemistry
homepage_url: https://www.swisslipids.org/
id: swisslipid
last_modified_date: '2026-05-30T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: SwissLipids
products:
- category: GraphicalInterface
  description: Main SwissLipids interface for browsing lipid classes and analytes.
  format: http
  id: swisslipid.portal
  name: SwissLipids Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  product_url: https://www.swisslipids.org/
- category: Product
  description: TSV export of lipid-related enzymes with UniProt, Rhea, and evidence
    links.
  format: tsv
  id: swisslipid.enzymes
  name: SwissLipids Enzymes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: rhea
  product_file_size: 126760
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=enzymes.tsv
- category: Product
  description: TSV export of evidence annotations including ECO terms and supporting
    PMIDs.
  format: tsv
  id: swisslipid.evidences
  name: SwissLipids Evidences
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: eco
  product_file_size: 47076
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=evidences.tsv
- category: Product
  description: TSV export of SwissLipids links to Gene Ontology terms with taxon context.
  format: tsv
  id: swisslipid.go
  name: SwissLipids GO Annotations
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: go
  product_file_size: 48388
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=go.tsv
- category: Product
  description: Comprehensive TSV catalogue of SwissLipids lipid entities and identifiers.
  format: tsv
  id: swisslipid.lipids
  name: SwissLipids Lipids
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  product_file_size: 76772233
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=lipids.tsv
- category: MappingProduct
  description: TSV mapping between SwissLipids lipid entries and UniProtKB proteins.
  format: tsv
  id: swisslipid.lipids2uniprot
  name: SwissLipids Lipids to UniProt
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_file_size: 37147786
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=lipids2uniprot.tsv
- category: Product
  description: TSV export of lipid tissue and cell annotations with taxon and evidence
    tags.
  format: tsv
  id: swisslipid.tissues
  name: SwissLipids Tissues
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  product_file_size: 9540
  product_url: https://www.swisslipids.org/api/file.php?cas=download_files&file=tissues.tsv
- category: ProgrammingInterface
  connection_url: https://www.swisslipids.org/#/api
  description: Public API page for programmatic SwissLipids access.
  format: http
  id: swisslipid.api
  is_public: true
  name: SwissLipids API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  product_url: https://www.swisslipids.org/#/api
- category: Product
  compression: gzip
  description: swisslipid Nodes TSV
  format: tsv
  id: obo-db-ingest.swisslipid.tsv
  license:
    id: https://creativecommons.org/licenses/by/4.0/
    label: CC-BY-4.0
  name: swisslipid Nodes TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: obo-db-ingest
  - relation_type: prov:hadPrimarySource
    source: swisslipid
  product_file_size: 9655893
  product_url: https://w3id.org/biopragmatics/resources/slm/slm.tsv.gz
publications:
- authors:
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
  doi: doi:10.1093/bioinformatics/btv285
  id: doi:10.1093/bioinformatics/btv285
  preferred: true
  title: The SwissLipids knowledgebase for lipid biology
  year: '2015'
repository: https://www.swisslipids.org/
synonyms:
- slm
- swisslipid
---
# SwissLipids

SwissLipids is a curated knowledge resource for lipids and lipid biology
developed by SIB Swiss Institute of Bioinformatics teams. It combines a browseable
web interface with downloadable reference tables for lipid entities, enzyme
associations, GO annotations, tissues, evidences, and lipid-to-UniProt mappings.

In KG-Registry, SwissLipids is represented both as a public portal and as a set
of concrete downloadable products that support identifier mapping, lipid
classification, and metabolism-oriented integration workflows. The downstream
OBO-DB-Ingest TSV remains attached as a propagated derivative of the underlying
SwissLipids content.