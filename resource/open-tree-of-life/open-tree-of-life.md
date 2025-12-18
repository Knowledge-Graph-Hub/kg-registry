---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: "https://tree.opentreeoflife.org/"
    id: "open-tree-of-life-collaboration"
    label: "Open Tree of Life Collaboration"
creation_date: '2025-12-17T00:00:00Z'
description: Open Tree of Life (OToL) is a comprehensive, collaborative online phylogenetic tree synthesizing published evolutionary estimates with taxonomic data. It combines phylogenetic data from 1,216 published papers with 10 source taxonomies to construct a dynamic tree of life with 2.4 million tips representing species and infraspecific taxa.
domains: []
homepage_url: https://tree.opentreeoflife.org/
id: "open-tree-of-life"
infores_id: "open-tree-of-life"
layout: resource_detail
license:
  id: "https://creativecommons.org/publicdomain/zero/1.0/"
  label: CC0 Public Domain
name: Open Tree of Life
products:
  - category: GraphicalInterface
    description: Interactive zoomable phylogenetic tree browser enabling exploration of taxonomic relationships and phylogenetic structure across 2.4 million tips
    format: http
    id: "otol.tree-browser"
    name: Open Tree of Life Browser
    product_url: "https://tree.opentreeoflife.org/tree"
  - category: ProgrammingInterface
    description: RESTful APIs providing programmatic access to synthetic tree, taxonomy, and taxonomic name resolution services with support for MRCA queries and subtree extraction
    format: http
    id: "otol.api"
    is_public: true
    name: Open Tree of Life APIs
    product_url: "https://opentreeoflife.github.io/develop/api"
  - category: ProgrammingInterface
    description: Taxonomic Name Resolution Service (TNRS) providing exact and fuzzy matching of taxonomic names to Open Tree Taxonomy with context-based disambiguation
    format: http
    id: "otol.tnrs"
    is_public: true
    name: Taxonomic Name Resolution Service (TNRS)
    product_url: "https://tree.opentreeoflife.org/tnrs"
  - category: Product
    description: Complete phylesystem repository containing 4,500+ curated phylogenetic studies in NexSON JSON format with full version control history
    id: "otol.phylesystem"
    name: Phylesystem Data Repository
    product_url: "https://github.com/opentreeoflife/phylesystem"
  - category: Product
    description: Preprocessed source trees and taxonomy files available for bulk download in Newick, Nexus, and JSON formats
    id: "otol.bulk-download"
    name: Open Tree of Life Bulk Downloads
    product_url: "https://files.opentreeoflife.org/preprocessed/v3.0/"
  - category: DocumentationProduct
    description: API reference, developer guides, and integration documentation for accessing Open Tree of Life data programmatically
    format: http
    id: "otol.documentation"
    is_public: true
    name: Open Tree of Life Developer Documentation
    product_url: "https://opentreeoflife.github.io/develop"
publications:
  - authors:
      - Hinchliff CE
      - Smith SA
      - Allman JF
      - Burleigh JG
      - Chaudhary R
      - Cogdell-Waters LM
      - Crandall KA
      - Deng J
      - Drew BT
      - Gazis R
      - Gude K
      - Hibbett DS
      - Katz LA
      - Laughinghouse HD
      - McTavish EJ
      - Midford PE
      - Oliver PM
      - Olds BS
      - Soltis DE
      - Soltis PS
    doi: "10.1073/pnas.1423041112"
    id: "doi:10.1073/pnas.1423041112"
    journal: "Proceedings of the National Academy of Sciences"
    preferred: true
    title: "Synthesis of phylogeny and taxonomy into a comprehensive tree of life"
    year: "2015"
  - authors:
      - McTavish EJ
      - Cranston KA
      - Domman D
      - Sindbäck J
      - Freund J
      - Steele PR
      - Gude K
      - Midford PE
    doi: "10.1093/bioinformatics/btv128"
    id: "doi:10.1093/bioinformatics/btv128"
    journal: "Bioinformatics"
    title: "Phylesystem: a git-based data store for community curated phylogenetic estimates"
    year: "2015"
  - authors:
      - Sanchez-Reyes LL
      - Mishler BD
      - Merow C
      - Enquist BJ
    doi: "10.1093/sysbio/syab038"
    id: "doi:10.1093/sysbio/syab038"
    journal: "Systematic Biology"
    title: "OpenTree: A Python Package for Accessing and Analyzing Data from the Open Tree of Life"
    year: "2021"
  - authors:
      - Michonneau F
      - Brown JW
      - Winter DJ
    doi: "10.1111/2041-210X.12593"
    id: "doi:10.1111/2041-210X.12593"
    journal: "Methods in Ecology and Evolution"
    title: "rotl: an R package to interact with the Open Tree of Life data"
    year: "2016"
repository: "https://github.com/opentreeoflife"
taxon:
  - "NCBITaxon:1"
---

# Open Tree of Life

## Overview

The Open Tree of Life (OToL) is a comprehensive, collaborative, online phylogenetic tree that synthesizes published evolutionary estimates with taxonomic data to provide a unified framework for representing life's evolutionary relationships. First released in September 2015, the project continues to be actively maintained, updated, and funded by the National Science Foundation, representing one of the most ambitious attempts to create a global phylogenetic synthesis accessible to the scientific community and the public.

The Open Tree of Life combines a supertree approach with a community-curated system, enabling researchers worldwide to contribute phylogenetic data and taxonomic corrections, creating a dynamic, living tree that grows and improves with community input.

## Data Content and Scale

### Overall Scale

The current Open Tree of Life represents an unprecedented synthesis of phylogenetic and taxonomic data:

- **2.4 million tips** - Representative of species and infraspecific taxa across all domains of life
- **1,216 published phylogenetic papers** - Scientific studies contributing evolutionary estimates
- **87,000 tip taxa** - Distinct taxonomic units represented in source phylogenies
- **4,500+ curated studies** - Phylogenetic estimates stored in Phylesystem repository
- **484 source trees** - From 478 distinct published studies
- **10 source taxonomies** - Integrated to provide phylogenetic backbone and taxonomy framework

### Taxonomic Coverage

Open Tree of Life provides comprehensive coverage of all major domains of life:

**Bacteria and Archaea**
- Microorganisms and prokaryotic diversity
- Sourced from SILVA microbial taxonomy
- Phylogenetic relationships from genomic studies

**Eukaryotes**
- **Protists** - Single-celled eukaryotes and related organisms
- **Fungi** - Complete fungal diversity including yeasts and molds
  - Sourced from Index Fungorum and research databases
- **Plants** - Land plants and marine vegetation
- **Animals** - Complete animal phyla including:
  - Invertebrates (insects, mollusks, cnidarians, echinoderms, arthropods)
  - Vertebrates (fish, amphibians, reptiles, birds, mammals)

### Phylogenetic Data Structure

The synthesis includes:
- **Overlapping source phylogenies** - Multiple trees for same taxa groups resolved via supertree methods
- **Annotation system** - Tracking which source trees support or conflict with clades
- **Support values** - Phylogenetic support metrics from input studies
- **Conflict information** - Documentation of disagreement between source trees
- **Time-calibrated estimates** - Some studies include divergence time estimates

## Data Access and Formats

### Interactive Web Interface

**Open Tree of Life Browser**
- Zoomable, interactive visualization of the complete tree
- Taxon search and navigation
- Node information display with support values and conflicting relationships
- Real-time exploration of evolutionary relationships
- Access to source tree information and citations

### Programmatic Access via APIs

**v3 Synthetic Tree API**
- `/tree_of_life/about` - Information about current draft tree
- `/tree_of_life/mrca` - Most recent common ancestor of taxa set
- `/tree_of_life/induced_subtree` - Extract subtree for any node set
- `/tree_of_life/taxon_info` - Detailed information about specific taxon

**v3 Taxonomy API**
- `/taxonomy/about` - Current taxonomy information and version
- `/taxonomy/mrca` - MRCA for taxa in taxonomy
- `/taxonomy/subtree` - Complete subtree from specified taxon
- `/taxonomy/taxon_info` - Taxonomy entry details and synonyms

**Taxonomic Name Resolution Service (TNRS)**
- `/tnrs/match_names` - Match up to 1,000 names per query
- `/tnrs/contexts` - Available taxonomic contexts for query restriction
- `/tnrs/autocomplete` - Interactive name completion with disambiguation

**Client Libraries**
- Python: opentree and peyotl packages
- R: rotl package for R users
- Ruby support available

### Data Formats

Open Tree of Life supports multiple phylogenetic data formats:

- **Newick** - Standard phylogenetic text format
- **Nexus/NEXUS** - Standard format for phylogenetic data
- **NeXML** - XML-based phylogenetic format
- **NexSON** - JSON-based phylogenetic format used internally
- **JSON** - API responses with tree data as objects

### Bulk Data Downloads

**Preprocessed Data**
- Available at https://files.opentreeoflife.org/preprocessed/v3.0/
- Source trees in multiple formats
- Taxonomy files
- Regular version releases

**Git Repositories**
- Full version-controlled source code and data
- Community contribution via GitHub
- Complete audit trail of changes
- Phylesystem repositories for curated studies

## Data Sources and Integration

### Integrated Taxonomies (10 Sources)

1. **NCBI Taxonomy** - Prokaryotic and eukaryotic taxonomy foundation
2. **GBIF Backbone Taxonomy** - Comprehensive biodiversity taxonomy
3. **SILVA** - Ribosomal RNA sequence-based microbial taxonomy
4. **Index Fungorum** - Specialized fungal taxonomy
5. **World Register of Marine Species (WoRMS)** - Marine organism taxonomy
6. **IRMNG** - Interim Register of Marine and Nonmarine Genera
7. Publication-derived taxonomies
8. Curated major group taxonomies
9. User-contributed taxonomic amendments
10. Open Tree Taxonomy enhancements

### Phylogenetic Source Data

- 1,216 peer-reviewed phylogenetic papers
- 4,500+ studies curated in Phylesystem
- Diverse organisms from bacteria to mammals
- Studies using various molecular markers and morphological data
- Time-calibrated phylogenies for evolutionary dating

### Cross-Database Linking

- GBIF species identifiers
- NCBI taxonomy identifiers
- WoRMS identifiers
- SILVA taxonomy identifiers
- Index Fungorum identifiers
- Comprehensive synonymy mapping

## Technical Infrastructure

### Supertree Methodology

Open Tree of Life uses advanced supertree algorithms:
- **Propinquity software** - Rapid inference on millions of leaves
- Conflict resolution between overlapping source trees
- Support value computation for synthesized relationships
- Efficient computation for tree updates and new data integration

### Technologies

- **Version Control**: Git and GitHub for data management
- **Data Format**: NexSON (JSON-based phylogenetic format)
- **Query System**: RESTful web services
- **Phylogenetic Backend**: Custom supertree inference methods
- **Database**: Phylesystem for curated study storage

## Key Features

### Community-Driven Curation

- Open-source model enabling worldwide contributions
- GitHub-based workflow for submitting phylogenetic data
- Quality control and peer review of contributions
- Full version history and change tracking
- Continuous improvement and error correction

### Dynamic and Updatable

- Regular updates incorporating new published studies
- Taxonomy updates as new information becomes available
- Community feedback integration
- Systematic incorporation of corrections
- Transparent change documentation

### Comprehensive Cross-Reference System

- Links unique identifiers across major taxonomic databases
- Maps taxonomic synonymies and name variants
- Enables data integration with other resources
- Facilitates downstream analyses combining traits, distributions, and evolutionary history

### Scalable Infrastructure

- Handles 2.4 million taxa efficiently
- Rapid response to MRCA and subtree queries
- Suitable for large-scale phylogenetic analyses
- Continuous backbone available for addition of new studies

## Use Cases and Applications

### Evolutionary and Comparative Biology

- **Comparative phylogenetic analysis** - Evolution of traits across taxa
- **Gene family evolution** - Evolutionary relationships of molecular sequences
- **Macroevolutionary studies** - Large-scale evolutionary patterns
- **Phylogenomic applications** - Integrating genomic and phylogenetic data
- **Codon usage analysis** - Genome-wide genotyping marker design

### Ecology and Conservation

- **Community phylogenetics** - Phylogenetic diversity of ecological communities
- **Conservation planning** - Assessing evolutionary distinctiveness
- **Biodiversity assessment** - Understanding species relationships
- **Life history evolution** - Large-scale trait distribution patterns
- **Climate adaptation** - Evolutionary potential for environmental change response

### Applied Biology

- **Agricultural genetics** - Crop and pest evolutionary relationships
- **Molecular evolution** - Gene family divergence and function
- **Biotechnology** - Identifying enzymes and compounds from diverse organisms
- **Vaccine development** - Understanding pathogen evolution

### Education and Public Outreach

- **Teaching phylogenetics** - Interactive learning about evolutionary relationships
- **Science communication** - Public understanding of life's diversity
- **Biodiversity education** - Exploring evolutionary connections
- **Research training** - Introduction to phylogenetic analysis tools

### Integration with Other Platforms

- **Phylotastic** - On-demand phylogenetic tree generation
- **DateLife** - Comparative phylogenetic dating
- **OneZoom** - Interactive tree of life visualization
- **GBIF** - Combined evolutionary and species occurrence data
- **Comparative biology software** - Foundation for phylogenetic analyses

## Funding and Support

### Primary Funding

**National Science Foundation (NSF) Grants:**
- **NSF AVAToL #1208809** - "Assembling, Visualizing and Analyzing a Tree of All Life"
- **NSF ABI #1759838 and #1759846** (2018-2022) - "Sustaining the Open Tree of Life"
- **GoLife Program** - Support for continued development

### Collaborative Institutions

The project involves collaboration among 11 principal investigators across 10 institutions:
- University of Michigan
- University of Kansas
- UC Merced
- University of California, Santa Cruz
- Additional partner institutions

### Ongoing Development

- Active maintenance and regular updates
- Community support infrastructure
- Continued funding for database operations
- Integration with emerging phylogenetic methods and data

## Citation and Usage

Open Tree of Life data is freely available under the CC0 Public Domain Dedication, allowing unrestricted use, modification, and distribution. When using Open Tree of Life data in research or applications, please cite the appropriate publications.

### Recommended Citation

For the tree of life:
"Hinchliff, C.E., et al. (2015). Synthesis of phylogeny and taxonomy into a comprehensive tree of life. Proceedings of the National Academy of Sciences, 112(41), 12764-12769. https://doi.org/10.1073/pnas.1423041112"

For the Phylesystem data store:
"McTavish, E.J., et al. (2015). Phylesystem: a git-based data store for community curated phylogenetic estimates. Bioinformatics, 31(17), 2794-2800. https://doi.org/10.1093/bioinformatics/btv128"

### Additional Resources

- **Main Website**: https://tree.opentreeoflife.org/
- **GitHub Organization**: https://github.com/opentreeoflife
- **API Documentation**: https://opentreeoflife.github.io/develop/api
- **Developer Hub**: https://opentreeoflife.github.io/develop
- **Contact Form**: https://tree.opentreeoflife.org/contact

The Open Tree of Life continues to grow and improve as a collaborative resource, supported by the broad scientific community and maintained through sustained NSF funding.
