---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: innatedb-mail@sfu.ca
  label: Brinkman Laboratory, Simon Fraser University
creation_date: '2025-10-30T00:00:00Z'
description: InnateDB is a publicly available database of genes, proteins, experimentally-verified
  interactions and signaling pathways involved in the innate immune response of humans,
  mice and bovines to microbial infection, with over 18,780 manually curated interactions
  and integrated bioinformatics and visualization tools for systems-level analysis.
domains:
- immunology
- biological systems
- systems biology
homepage_url: https://www.innatedb.com/
id: innatedb
infores_id: innatedb
last_modified_date: '2026-04-16T00:00:00Z'
layout: resource_detail
license:
  id: https://www.innatedb.com/
  label: Varies
name: InnateDB
products:
- category: GraphicalInterface
  description: Web interface for searching and analyzing innate immunity genes, proteins,
    interactions, and pathways
  format: http
  id: innatedb.portal
  name: InnateDB Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: innatedb
  product_url: https://www.innatedb.com/
- category: Product
  description: Downloadable data files for interactions, pathways, and annotations
  id: innatedb.downloads
  name: InnateDB Data Downloads
  original_source:
  - relation_type: prov:hadPrimarySource
    source: innatedb
  product_url: https://www.innatedb.com/
- category: Product
  compression: gzip
  description: PC v14 integrated BioPAX Level 3 unified model containing normalized
    pathway data, molecular interactions, and cross-database entity mappings
  format: biopax
  id: pathway-commons.biopax
  name: Integrated BioPAX Model
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pathway-commons
  product_file_size: 1700903742
  product_url: https://download.baderlab.org/PathwayCommons/PC2/v14/pc-biopax.owl.gz
  secondary_source:
  - relation_type: prov:wasDerivedFrom
    source: bind
  - relation_type: prov:wasDerivedFrom
    source: biogrid
  - relation_type: prov:wasDerivedFrom
    source: chebi
  - relation_type: prov:wasDerivedFrom
    source: corum
  - relation_type: prov:wasDerivedFrom
    source: ctd
  - relation_type: prov:wasDerivedFrom
    source: dip
  - relation_type: prov:wasDerivedFrom
    source: drugbank
  - relation_type: prov:wasDerivedFrom
    source: hprd
  - relation_type: prov:wasDerivedFrom
    source: innatedb
  - relation_type: prov:wasDerivedFrom
    source: intact
  - relation_type: prov:wasDerivedFrom
    source: kegg
  - relation_type: prov:wasDerivedFrom
    source: mirtarbase
  - relation_type: prov:wasDerivedFrom
    source: msigdb
  - relation_type: prov:wasDerivedFrom
    source: panther
  - relation_type: prov:wasDerivedFrom
    source: pathbank
  - relation_type: prov:wasDerivedFrom
    source: pid
  - relation_type: prov:wasDerivedFrom
    source: reactome
  - relation_type: prov:wasDerivedFrom
    source: uniprot
publications:
- id: https://doi.org/10.1093/nar/gks1147
  journal: Nucleic Acids Research
  title: 'InnateDB: systems biology of innate immunity and beyond - recent updates
    and continuing curation'
  year: '2013'
synonyms:
- InnateDB
taxon:
- NCBITaxon:2
---
# InnateDB

## Overview

InnateDB is a publicly available knowledge resource dedicated to the innate immune response. It provides comprehensive information about genes, proteins, experimentally-verified molecular interactions, and signaling pathways involved in innate immunity across humans, mice, and bovines. The database integrates data from major public databases with extensive manually-curated content to create a centralized resource for innate immunity research.

## Key Features

- **Extensive Manual Curation**: Over 18,780 interactions manually curated by the InnateDB team
- **Multi-Species Coverage**: Data for humans, mice, and bovines
- **Integrated Data**: Combines known interactions and pathways from major public databases
- **Systems Biology Tools**: Integrated bioinformatics and visualization tools for systems-level analysis
- **Comprehensive Content**: Genes, proteins, protein-protein interactions, and signaling pathways

## Content Coverage

### Molecular Entities
- Innate immunity-related genes
- Protein annotations
- Experimentally-verified protein-protein interactions
- Signaling pathways

### Analysis Capabilities
- Gene Ontology analysis
- Pathway analysis
- Network analysis
- Protein-protein interaction networks
- Integration with visualization tools

## Applications

- **Immunology Research**: Understanding innate immune responses to infection
- **Systems Biology**: Systems-level analysis of immune signaling networks
- **Drug Discovery**: Identifying potential therapeutic targets in innate immunity
- **Comparative Immunology**: Cross-species analysis of immune responses
- **Pathway Analysis**: Studying signaling cascades in immune responses
- **Network Biology**: Analyzing interaction networks in immunity

## Development Team

InnateDB is developed jointly by:
- **Brinkman Laboratory** - Simon Fraser University, British Columbia, Canada
- **Hancock Laboratory** - University of British Columbia, Vancouver, British Columbia
- **Lynn EMBL Australia Group** - South Australian Health & Medical Research Institute and Flinders University, Adelaide, Australia

## Funding

Supported by:
- Allergen NCE
- EMBL Australia
- Previously: Genome Canada, Genome BC, Foundation for NIH (Grand Challenges in Global Health), Teagasc

## Data Licensing

- InnateDB curated interactions: Design Science License
- Other data: Licensed under terms of originating databases

## Citation

Breuer et al., InnateDB: systems biology of innate immunity and beyond - recent updates and continuing curation. Nucleic Acids Research (2013) 41 (D1): D1228-D1233.

## Information Resource ID

This resource has the Information Resource identifier: `infores:innatedb`