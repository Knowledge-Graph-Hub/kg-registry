---
activity_status: active
category: DataSource
creation_date: '2025-10-30T00:00:00Z'
description: The NCATS BioPlanet is a comprehensive, publicly accessible informatics
  resource that catalogues all pathways, their healthy and disease state annotations,
  and targets within and relationships among them.
domains:
- pathways
- toxicology
homepage_url: https://tripod.nih.gov/bioplanet/
id: bioplanet
infores_id: bioplanet
last_modified_date: '2026-09-16T00:00:00Z'
layout: resource_detail
name: BioPlanet
products:
- category: Product
  description: Comprehensive integrated pathway resource that incorporates 1,658 distinct
    human pathways.
  format: csv
  id: bioplanet.data
  name: BioPlanet Pathway Data
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioplanet
  product_file_size: 4696219
  product_url: https://tripod.nih.gov/bioplanet/download/pathway.csv
- category: ProgrammingInterface
  description: TRAPI endpoint for the Service Provider team, served by BioThings Explorer,
    querying the BioThings and other APIs registered to the team in SmartAPI.
  format: http
  id: service-kp.trapi
  is_public: true
  name: Service Provider TRAPI
  original_source:
  - relation_type: prov:hadPrimarySource
    source: service-kp
  - relation_type: prov:hadPrimarySource
    source: biothings
  - relation_type: prov:hadPrimarySource
    source: monarchinitiative
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: complexportal
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: litvar
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: ols
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: bindingdb
  - relation_type: prov:hadPrimarySource
    source: bioplanet
  - relation_type: prov:hadPrimarySource
    source: ddinter
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: gene2phenotype
  - relation_type: prov:hadPrimarySource
    source: foodb
  - relation_type: prov:hadPrimarySource
    source: gtrx
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: idisk
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: pfocr
  - relation_type: prov:hadPrimarySource
    source: repodb
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: semmeddb
  - relation_type: prov:hadPrimarySource
    source: suppkg
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: uberon
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: clingen
  - relation_type: prov:hadPrimarySource
    source: cpdb
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: aeolus
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: drugcentral
  - relation_type: prov:hadPrimarySource
    source: disgenet
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: multiomics-kp
  - relation_type: prov:hadPrimarySource
    source: text-mining-kp
  - relation_type: prov:hadPrimarySource
    source: gdsc
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:wasInformedBy
    source: biothings-explorer
  product_url: https://bte.transltr.io/v1/team/Service%20Provider
publications:
- authors:
  - Huang R
  - Grishagin I
  - Wang Y
  - Zhao T
  - Greene J
  - Obenauer JC
  - Ngan D
  - Nguyen D-T
  - Guha R
  - Jadhav A
  - Southall N
  - Simeonov A
  - Austin CP
  doi: 10.3389/fphar.2019.00445
  id: doi:10.3389/fphar.2019.00445
  journal: Frontiers in Pharmacology
  title: The NCATS BioPlanet – An Integrated Platform for Exploring the Universe of
    Cellular Signaling Pathways for Toxicology, Systems Biology, and Chemical Genomics
  year: '2019'
---
# BioPlanet

## Overview

The NCATS BioPlanet is a comprehensive, publicly accessible informatics resource that catalogues all pathways, their healthy and disease state annotations, and targets within and relationships among them. The BioPlanet integrates pathway annotations from publicly available, manually curated sources that have been subjected to thorough redundancy and consistency cross-evaluation via extensive manual curation.

The resource hosts information only from public sources that have been further manually curated to ensure the quality of the data. Along with the pathway warehouse, the NCATS BioPlanet software platform allows easy browsing and visualization of the universe of pathways, and exploration of associations among them.

## Information Resource ID

This resource has the Information Resource identifier: `infores:bioplanet`

## Key Features

- **Comprehensive Pathway Catalog**: Incorporates 1,658 distinct human pathways encompassing 9,818 human genes (as of v1.0).
- **Integrated Data**: Combines data from KEGG, Reactome, WikiPathways, BioCarta, NCI-Nature PID, and Science Signaling.
- **Manual Curation**: Extensive manual curation to remove redundancy and ensure data quality.
- **Assay Availability**: Annotates pathways with availability of bioassays from Tox21, NCATS, PubChem, and commercial sources.
- **Visualization**: Provides interactive pathway diagrams and a 3D globe view of pathway relationships.

## Publications

- Huang R, Grishagin I, Wang Y, Zhao T, Greene J, Obenauer JC, Ngan D, Nguyen D-T, Guha R, Jadhav A, Southall N, Simeonov A, Austin CP. The NCATS BioPlanet – An Integrated Platform for Exploring the Universe of Cellular Signaling Pathways for Toxicology, Systems Biology, and Chemical Genomics. Front Pharmacol. 2019;10:445. doi: 10.3389/fphar.2019.00445.