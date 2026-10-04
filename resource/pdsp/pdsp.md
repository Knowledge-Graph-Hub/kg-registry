---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://pdsp.unc.edu/
  label: UNC Chapel Hill PDSP
creation_date: '2025-11-05T00:00:00Z'
description: The Psychoactive Drug Screening Program (PDSP) at UNC Chapel Hill provides
  screening of novel psychoactive compounds for pharmacological and functional activity
  at cloned human or rodent CNS receptors, channels, and transporters. The PDSP Ki
  Database contains binding affinities for thousands of drugs and drug candidates
  at neuroreceptors, providing critical pharmacological data for drug discovery and
  neuroscience research.
domains:
- pharmacology
- neuroscience
- drug discovery
- biomedical
- high-throughput screening
homepage_url: https://pdsp.unc.edu/
id: pdsp
infores_id: pdsp
last_modified_date: '2026-09-23T00:00:00Z'
layout: resource_detail
name: Psychoactive Drug Screening Program
products:
- category: GraphicalInterface
  description: Web interface for searching and browsing PDSP Ki Database
  format: http
  id: pdsp.web
  name: PDSP Ki Database
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pdsp
  product_url: https://pdsp.unc.edu/databases/kidb.php
- category: Product
  description: Downloadable PDSP Ki values with SMILES codes for receptor binding
    affinity data on psychoactive compounds
  format: csv
  id: pdsp.data
  name: PDSP Binding Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pdsp
  product_url: https://pdsp.unc.edu/databases/kiDownload/
- category: GraphicalInterface
  description: PDSP Ki Database data-mining interface for customized searches across
    Ki records
  format: http
  id: pdsp.data_mining
  name: PDSP Ki Data Mining Tools
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pdsp
  product_url: https://pdsp.unc.edu/databases/dataMining/
- category: DocumentationProduct
  description: Screening assay protocols and methodologies
  format: pdf
  id: pdsp.protocols
  name: PDSP Assay Protocols
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pdsp
  product_file_size: 24885088
  product_url: https://pdsp.unc.edu/pdspweb/content/PDSP%20Protocols%20II%202013-03-28.pdf
- category: Product
  description: Web interface for searching and visualizing chemical-protein interactions
    across organisms
  format: http
  id: stitch.portal
  is_public: true
  name: STITCH Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: pdsp
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: matador
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: glida
  product_url: http://stitch-db.org/
- category: Product
  description: Downloadable data files containing chemical-protein interaction networks
  format: tsv
  id: stitch.downloads
  is_public: true
  name: STITCH Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: pdsp
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: matador
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: glida
  product_url: http://stitch-db.org/cgi/download.pl
- category: ProgrammingInterface
  description: API for programmatic access to STITCH chemical-protein interaction
    data
  format: http
  id: stitch.api
  is_public: true
  name: STITCH API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: stitch
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: pdsp
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: matador
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: kegg
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pmc
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: nihreporter
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: glida
  product_url: http://stitch-db.org/cgi/access.pl?footer_active_subpage=apis
publications:
- authors:
  - Roth BL
  - Kroeze WK
  - Patel S
  - Lopez E
  doi: 10.1177/107385840000600408
  id: doi:10.1177/107385840000600408
  journal: The Neuroscientist
  preferred: true
  title: 'The multiplicity of serotonin receptors: uselessly diverse molecules or
    an embarrassment of riches?'
  year: '2000'
synonyms:
- PDSP
- NIMH PDSP
taxon:
- NCBITaxon:9606
- NCBITaxon:10116
---
# Psychoactive Drug Screening Program

## Overview

The Psychoactive Drug Screening Program (PDSP) at UNC Chapel Hill provides screening of novel psychoactive compounds for pharmacological and functional activity at cloned human or rodent CNS receptors, channels, and transporters.

Funded by the National Institute of Mental Health (NIMH), PDSP offers both screening services and a comprehensive database of receptor binding data (Ki values) for thousands of psychoactive drugs and drug candidates.

## Key Features

- **Comprehensive Receptor Panel**: Screening across 50+ CNS receptors, channels, and transporters
- **Ki Database**: Binding affinity data for thousands of compounds
- **Standardized Assays**: Validated radioligand binding and functional assays
- **Drug Discovery Support**: Critical pharmacological data for lead optimization
- **Public Access**: Free database access for research community

## Research Applications

- Drug discovery and lead optimization
- Off-target effect prediction
- Polypharmacology analysis
- Structure-activity relationship (SAR) studies
- CNS drug safety assessment

## Products

### PDSP Ki Database
Searchable web database containing receptor binding affinities (Ki values) for psychoactive drugs and drug candidates across multiple neuroreceptor targets.

### PDSP Binding Data
Downloadable datasets of receptor binding data for computational analysis and modeling.

### Assay Protocols
Detailed protocols for PDSP's standardized receptor binding and functional assays.

## Information Resource ID

This resource has the Information Resource identifier: `infores:pdsp`

## Domains

- Pharmacology
- Neuroscience
- Drug Discovery
- Biomedical