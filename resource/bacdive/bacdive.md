---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: contact@bacdive.de
  id: dsmz-leibniz-institute-dsmz-german-collection-of-m
  label: BacDive
creation_date: '2025-11-25T00:00:00Z'
description: BacDive (Bacterial Diversity Metadatabase) is the world's largest database
  for standardized bacterial information, containing strain-level data on morphology,
  physiology, growth conditions, and isolation sources for over 99,000 bacterial strains.
  It integrates research data from diverse sources and provides freely accessible,
  standardized information with Digital Object Identifiers for each strain.
domains:
- microbiology
- biological systems
homepage_url: https://bacdive.dsmz.de/
id: bacdive
infores_id: bacdive
last_modified_date: '2026-06-17T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY-4.0
name: BacDive
products:
- category: GraphProduct
  compression: targz
  description: Raw source files for all KG-Microbe framework transforms (all 4 KGs)
  format: kgx
  id: kg-microbe.graph.raw
  license:
    id: https://creativecommons.org/publicdomain/zero/1.0/
    label: CC0 1.0
  name: KG-Microbe KGX Graph - Raw
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
- category: GraphProduct
  compression: targz
  description: The core KG KG-Microbe-Core with ontologies, organismal traits, and
    growth preferences.
  format: kgx
  id: kg-microbe.graph.core
  name: KG-Microbe KGX Graph - Core
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
- category: GraphProduct
  compression: targz
  description: Core plus human biomedical data (ontologies, CTD, Wallen et al)
  format: kgx
  id: kg-microbe.graph.biomedical
  name: KG-Microbe KGX Graph - Biomedical
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
- category: GraphProduct
  compression: targz
  description: Core plus Uniprot genome annotations
  format: kgx
  id: kg-microbe.graph.function
  name: KG-Microbe KGX Graph - Function
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_url: https://github.com/Knowledge-Graph-Hub/kg-microbe/releases/latest
- category: GraphProduct
  compression: targz
  description: Biomedical plus Uniprot genome annotations
  format: kgx
  id: kg-microbe.graph.biomedical-function
  name: KG-Microbe KGX Graph - Biomedical-Function
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bactotraits
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: disbiome
  - relation_type: prov:hadPrimarySource
    source: ec
  - relation_type: prov:hadPrimarySource
    source: envo
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: kg-microbe
  - relation_type: prov:hadPrimarySource
    source: mediadive
  - relation_type: prov:hadPrimarySource
    source: metpo
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbitaxon
  - relation_type: prov:hadPrimarySource
    source: rhea
  - relation_type: prov:hadPrimarySource
    source: uniprot
  product_file_size: 4640682152
  product_url: https://portal.nersc.gov/project/m4689/KGMicrobe-biomedical-function-20250222.tar.gz
- category: Product
  description: Trait data table listing all 140+ harmonized traits available in metaTraits,
    mapped to standardized ontologies.
  format: http
  id: metatraits.traits
  name: metaTraits Trait List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bacdive
  - relation_type: prov:hadPrimarySource
    source: bv-brc
  - relation_type: prov:hadPrimarySource
    source: goldterms
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:hadPrimarySource
    source: progenomes
  product_url: https://metatraits.embl.de/traits
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
  description: Family-level harmonized trait annotations aggregated for GTDB taxonomy
    in compressed TSV format.
  format: tsv
  id: metatraits.gtdb.family-summary
  name: metaTraits GTDB Family Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: gtdb
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: bv-brc
  - relation_type: prov:wasDerivedFrom
    source: goldterms
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 1513013
  product_url: https://www.bork.embl.de/~robbani/metatraits/gtdb_family_summary_no_predictions.tsv.gz
- category: Product
  description: Genus-level harmonized trait annotations aggregated for GTDB taxonomy
    in compressed TSV format.
  format: tsv
  id: metatraits.gtdb.genus-summary
  name: metaTraits GTDB Genus Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: gtdb
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: bv-brc
  - relation_type: prov:wasDerivedFrom
    source: goldterms
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 4965442
  product_url: https://www.bork.embl.de/~robbani/metatraits/gtdb_genus_summary_no_predictions.tsv.gz
- category: Product
  description: Species-level harmonized trait annotations aggregated for GTDB taxonomy
    in compressed TSV format.
  format: tsv
  id: metatraits.gtdb.species-summary
  name: metaTraits GTDB Species Summary
  original_source:
  - relation_type: prov:hadPrimarySource
    source: metatraits
  - relation_type: prov:wasDerivedFrom
    source: gtdb
  - relation_type: prov:wasDerivedFrom
    source: bacdive
  - relation_type: prov:wasDerivedFrom
    source: bv-brc
  - relation_type: prov:wasDerivedFrom
    source: goldterms
  - relation_type: prov:wasDerivedFrom
    source: progenomes
  product_file_size: 12570522
  product_url: https://www.bork.embl.de/~robbani/metatraits/gtdb_species_summary_no_predictions.tsv.gz
- category: GraphicalInterface
  description: MediaDive web portal for browsing, searching, comparing, and building
    microbial cultivation media recipes.
  format: http
  id: mediadive.portal
  name: MediaDive Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mediadive
  product_url: https://mediadive.dsmz.de/
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: bacdive
  - relation_type: prov:used
    source: chebi
  - relation_type: prov:used
    source: ncbitaxon
- category: ProgrammingInterface
  description: MediaDive REST API documentation for programmatic retrieval of media,
    solutions, ingredients, strains, and related records.
  format: http
  id: mediadive.rest_api
  name: MediaDive REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mediadive
  product_url: https://mediadive.dsmz.de/doc/index.html
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: bacdive
  - relation_type: prov:used
    source: chebi
  - relation_type: prov:used
    source: ncbitaxon
- category: ProgrammingInterface
  description: MediaDive SPARQL endpoint for querying the DSMZ Digital Diversity RDF
    representation of MediaDive data.
  format: http
  id: mediadive.sparql
  name: MediaDive SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: mediadive
  product_url: https://sparql.dsmz.de/mediadive
  secondary_source:
  - relation_type: prov:wasInformedBy
    source: bacdive
  - relation_type: prov:used
    source: chebi
  - relation_type: prov:used
    source: ncbitaxon
publications:
- authors:
  - Schober I
  - Koblitz J
  - Sardà Carbasse J
  - Ebeling C
  - Schmidt ML
  - Podstawka A
  - Gupta R
  - Ilangovan V
  - Chamanara J
  - Overmann J
  - Reimer LC
  doi: doi:10.1093/nar/gkae959
  id: https://doi.org/10.1093/nar/gkae959
  journal: Nucleic Acids Research
  preferred: true
  title: 'BacDive in 2025: the core database for prokaryotic strain data'
  year: '2025'
repository: https://github.com/JKoblitz/bacdive-api
taxon:
- NCBITaxon:2
---
# BacDive

## Overview

BacDive (Bacterial Diversity Metadatabase) is the world's largest and most comprehensive database for standardized bacterial information at the strain level. Maintained by the Leibniz Institute DSMZ (German Collection of Microorganisms and Cell Cultures), BacDive mobilizes and integrates research data from diverse sources to make bacterial diversity information freely accessible to the scientific community.

## Key Features

- **Comprehensive Coverage**: Over 99,000 bacterial strains with 21,168 type strains
- **Standardized Information**: Morphology, physiology, growth conditions, isolation sources, and genomic data
- **Global Core Biodata Resource**: Recognized as both an ELIXIR Core Data Resource and Global Core Biodata Resource
- **Digital Object Identifiers**: All strain data are referenced by DOIs for permanent citability
- **Open Access**: Freely available under Creative Commons Attribution 4.0 International License

## Data Content

BacDive provides comprehensive information across multiple categories:

### Morphological Traits
- Cell shape, size, and arrangement
- Gram staining properties
- Motility characteristics
- Colony-forming properties

### Physiological Traits
- Oxygen tolerance (aerobe, anaerobe, facultative)
- Temperature optima and ranges
- pH preferences
- Metabolic capabilities
- Chemotaxonomy

### Growth Conditions
- Culture media requirements
- Temperature ranges
- Oxygen requirements
- Special growth conditions

### Isolation and Sampling
- Geographic origin
- Isolation sources
- Environmental context
- Collection information

### Molecular Data
- GC content
- Genome sequences
- 16S rRNA sequences
- Taxonomic classification

## Access Methods

- **Web Interface**: Interactive browsing and search at https://bacdive.dsmz.de/
- **Advanced Search**: Filtering by multiple parameters
- **TAXplorer**: Taxonomic exploration tool
- **API**: RESTful web services at https://api.bacdive.dsmz.de/
- **API Test Finder**: Tool for testing API queries

## Special Collections

BacDive provides statistics and focused access to:
- Well-known culture collections
- Specific bacterial groups
- Type strain collections
- Isolation source compilations

## Applications

- Comparative microbiology and taxonomy
- Selection of reference strains for research
- Culture optimization and strain characterization
- Ecological and environmental studies
- Systems biology and knowledge graph integration
- Biotechnology and industrial applications

## Integration

BacDive data is integrated into multiple knowledge graphs and resources:
- KG-Microbe (microbial knowledge graphs)
- NCBITaxon (taxonomic classifications)
- Environmental ontologies
- Genomic databases

## Support and Funding

BacDive is supported by:
- de.NBI (German Network for Bioinformatics Infrastructure)
- ELIXIR Europe
- DZIF (German Center for Infection Research)
- NFDI4Biodiversity
- NFDI4Microbiota

## Citation

When using BacDive, please cite the database and relevant publications. Each strain entry includes a DOI for permanent citation.

For more information, visit https://bacdive.dsmz.de/