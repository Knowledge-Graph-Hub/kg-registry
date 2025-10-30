---
activity_status: active
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: Ribocentre is a comprehensive database containing information about natural ribozymes, including sequences, structures, catalytic mechanisms, and applications. It provides searchable and browsable access to ribozyme research data with interactive 2D and 3D visualizations.
domains:
  - genomics
  - biological systems
homepage_url: https://www.ribocentre.org/
id: ribocentre
last_modified_date: '2025-10-30T00:00:00Z'
layout: resource_detail
name: Ribocentre
contacts:
  - category: Individual
    contact_details:
      - contact_type: email
        value: miao_zhichao@gzlab.ac.cn
    label: Zhichao Miao
  - category: Individual
    contact_details:
      - contact_type: email
        value: huanglin36@mail.sysu.edu.cn
    label: Lin Huang
products:
  - category: GraphicalInterface
    description: Web portal for searching and browsing ribozyme data including sequences, structures, catalytic information, and publications
    format: http
    id: ribocentre.portal
    name: Ribocentre Web Portal
    original_source:
      - ribocentre
    product_url: https://www.ribocentre.org/
  - category: GraphicalInterface
    description: Browse comprehensive information about different ribozyme types with timelines, structures, and mechanisms
    format: http
    id: ribocentre.ribozymes
    name: Ribozyme Browser
    original_source:
      - ribocentre
    product_url: https://www.ribocentre.org/ribozyme/
  - category: GraphicalInterface
    description: Interactive 2D and 3D structure visualization tools for ribozymes
    format: http
    id: ribocentre.structures
    name: Structure Visualization
    original_source:
      - ribocentre
    product_url: https://www.ribocentre.org/structure/
  - category: GraphicalInterface
    description: Search functionality integrated with RNAcentral for sequence searching
    format: http
    id: ribocentre.search
    name: Sequence Search
    original_source:
      - ribocentre
      - rnacentral
    product_url: https://www.ribocentre.org/search.html
  - category: DocumentationProduct
    description: Comprehensive publication database with 293+ entries of ribozyme research articles
    format: http
    id: ribocentre.publications
    name: Publications Database
    original_source:
      - ribocentre
    product_url: https://www.ribocentre.org/publications/
publications:
  - id: PMID:36399504
    preferred: true
  - id: PMID:37883399
synonyms:
  - RiboCentre
---

# Ribocentre

## Overview

Ribocentre is a comprehensive web-based database designed to contain information about all natural ribozymes. Ribozymes are catalytic RNA molecules found across all kingdoms of life that play crucial roles in important biological reactions such as peptide-bond formation, RNA splicing, transfer RNA biosynthesis, and viral replication. The database provides an excellent resource for understanding the 'sequence-structure-function' relationship of RNA molecules.

## Data Content

The database contains comprehensive information about natural ribozymes including:

- **Sequences**: RNA sequences of various ribozyme types
- **Structures**: Representative 2D and 3D structures with interactive visualization
- **Catalytic Mechanisms**: Detailed chemical mechanisms and catalytic center information
- **Publications**: Over 293 research articles spanning from 1975 to present
- **Applications**: Examples of ribozyme applications in research
- **Timelines**: Historical breakthroughs in ribozyme research

## Key Features

- **Multiple Browsing Methods**: Browse by ribozyme type, structure, catalysis, applications, and publications
- **Interactive Visualizations**: 2D and 3D dynamic interactive structure viewers
- **Search Integration**: Sequence search functionality powered by RNAcentral
- **Comprehensive Coverage**: Information about all major ribozyme classes including Group I and II self-splicing introns, ribosomes, and various self-cleaving ribozymes
- **Publication Database**: Searchable and sortable collection of ribozyme research papers
- **User Submissions**: Portal for users to submit new ribozyme cases and provide feedback

## Database Versions

- **Current Version**: v1.5 (March 2023) - Added sequence search function from RNAcentral
- **v1.4** (July 2022): Added 3D dynamic interactive visualization
- **v1.3** (July 2022): Added 2D dynamic interactive visualization
- **v1.2** (June 2022): Added Catalysis section
- **v1.1** (June 2022): Added Applications section
- **v1.0** (June 2022): Initial release

## Access Methods

- **Web Interface**: Browse and search through the web portal
- **Publication Search**: Search and filter the comprehensive publication database
- **Structure Viewer**: Interactive 2D and 3D visualization tools
- **Submission Portal**: Google Sheets-based feedback and submission system

## Use Cases

1. **Research**: Understanding ribozyme structure-function relationships
2. **Education**: Learning about catalytic RNA and RNA mechanisms
3. **Comparative Studies**: Analyzing ribozyme catalytic mechanisms across different types
4. **Literature Review**: Accessing curated collection of ribozyme publications
5. **Structure Analysis**: Viewing and analyzing ribozyme 3D structures interactively

## Management

**Affiliated Organizations**:
- Guangzhou National Laboratory (GZNL-RDC)
- Sun Yat-sen University
- RNAcentre
- University of Dundee (collaboration with Prof. David Lilley)

**Principal Investigators**:
- Zhichao (Chichau) Miao - Guangzhou Laboratory
- Lin Huang - Sun Yat-sen University
- David Lilley - University of Dundee

## Funding

- R&D Programs of Guangzhou Laboratory
- MOST IT+BT projects
- National Natural Science Foundation of China (NSFC)

## Related Resources

- [Ribocentre-switch](https://riboswitch.ribocentre.org/): Database for riboswitches
- [Aptamer Database](https://aptamer.ribocentre.org/): Database for aptamers
- [RNAcentral](https://rnacentral.org/): Sequence search integration

## Citation

Deng, J., Shi, Y., Peng, X., He, Y., Chen, X., Li, M., Lin, X., Liao, W., Huang, Y., Jiang, T., Lilley, D. M. J., Miao, Z., & Huang, L. (2023). Ribocentre: a database of ribozymes. *Nucleic Acids Research*, 51(D1), D262-D268. https://doi.org/10.1093/nar/gkac840