---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.guidetopharmacology.org/
  label: IUPHAR/BPS Guide to PHARMACOLOGY
creation_date: '2026-06-17T00:00:00Z'
description: The IUPHAR/BPS Guide to PHARMACOLOGY is an expert-curated database of
  molecular interactions between drug targets and their ligands. It provides concise
  overviews of the key properties of a wide range of established and potential drug
  targets, with curated quantitative information on the prescription medicines and
  experimental compounds that act on them.
domains:
- pharmacology
- drug discovery
- proteomics
homepage_url: https://www.guidetopharmacology.org/
id: guidetopharmacology
infores_id: gtopdb
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by-sa/4.0/
  label: CC-BY-SA-4.0
name: Guide to PHARMACOLOGY
products:
- category: GraphicalInterface
  description: Web interface for searching and browsing drug targets and their ligands.
  format: http
  id: guidetopharmacology.site
  is_public: true
  name: Guide to PHARMACOLOGY Website
  original_source:
  - relation_type: prov:hadPrimarySource
    source: guidetopharmacology
  product_url: https://www.guidetopharmacology.org/
- category: Product
  description: Bulk downloads of targets, ligands, and interactions in CSV and SQL
    formats.
  format: mixed
  id: guidetopharmacology.downloads
  name: Guide to PHARMACOLOGY Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: guidetopharmacology
  product_url: https://www.guidetopharmacology.org/download.jsp
- category: ProgrammingInterface
  description: Web services API for programmatic access to the database.
  format: http
  id: guidetopharmacology.api
  is_public: true
  name: Guide to PHARMACOLOGY Web Services
  original_source:
  - relation_type: prov:hadPrimarySource
    source: guidetopharmacology
  product_url: https://www.guidetopharmacology.org/webServices.jsp
publications:
- authors:
  - Simon D Harding
  - Jane F Armstrong
  - Elena Faccenda
  - Christopher Southan
  - Stephen P H Alexander
  - Anthony P Davenport
  - Michael Spedding
  - Jamie A Davies
  doi: 10.1093/nar/gkad944
  id: https://doi.org/10.1093/nar/gkad944
  journal: Nucleic Acids Research
  preferred: true
  title: The IUPHAR/BPS Guide to PHARMACOLOGY in 2024
  year: '2024'
---
# Guide to PHARMACOLOGY

The IUPHAR/BPS Guide to PHARMACOLOGY (GtoPdb) is an open-access, expert-curated database
of molecular interactions between drug targets and their ligands. It is developed as a
collaboration between the International Union of Basic and Clinical Pharmacology (IUPHAR)
and the British Pharmacological Society (BPS).

The database provides curated information on:

- Drug targets organized by class (GPCRs, ion channels, nuclear hormone receptors,
  kinases, enzymes, transporters, and other proteins)
- Approved drugs, experimental compounds, and endogenous ligands
- Quantitative interaction data (affinities, potencies) extracted from the literature
- Links to related resources including UniProt, Ensembl, ChEMBL, and PubChem

GeneCards integrates target and ligand information from the Guide to PHARMACOLOGY.
