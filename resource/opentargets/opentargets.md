---
activity_status: active
category: KnowledgeGraph
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: contact@opentargets.org
  - contact_type: github
    value: opentargets
  - contact_type: url
    value: https://www.opentargets.org/contact
  label: Open Targets
description: Open Targets is a collaborative effort to systematically identify and
  prioritise the best targets to safely and effectively treat rare and common diseases.
domains:
- health
- biomedical
homepage_url: https://www.opentargets.org/
id: opentargets
layout: resource_detail
license:
  id: https://www.apache.org/licenses/LICENSE-2.0
  label: Apache License 2.0
name: Open Targets
products:
- category: GraphicalInterface
  description: The Open Targets Platform integrates and visualizes public data on
    target-disease associations to assist in drug target identification and prioritization.
  format: http
  id: opentargets.platform
  name: Open Targets Platform
  product_url: https://platform.opentargets.org/
  repository: https://github.com/opentargets/platform
- category: ProgrammingInterface
  description: GraphQL API for accessing Open Targets Platform data programmatically.
  id: opentargets.api.graphql
  is_public: true
  name: Open Targets Platform GraphQL API
  product_url: https://api.platform.opentargets.org/api/v4/graphql
- category: ProgrammingInterface
  description: REST API for accessing Open Targets Platform data programmatically.
  id: opentargets.api.rest
  is_public: true
  name: Open Targets Platform REST API
  product_url: https://api.platform.opentargets.org/api/v4/rest
- category: GraphProduct
  description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG
    instances as neo4j graph databases, running in a Docker container. Requires UMLS
    API key to access.
  dump_format: neo4j
  id: ubkg.neo4j
  name: UBKG Neo4j Docker Distribution
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - do
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - cmap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: Ontology CSV files that can be imported into a neo4j instance to create
    a UBKG database. Requires UMLS API key to access.
  format: csv
  id: ubkg.csv
  name: UBKG Ontology CSV Files
  original_source:
  - hgnc
  - loinc
  - icd10
  - snomedct
  - uberon
  - pato
  - cl
  - do
  - obi
  - obib
  - edam
  - hsapdv
  - sbo
  - mi
  - chebi
  - mp
  - ordo
  - uniprot
  - uo
  - mondo
  - efo
  - pgo
  - gencode
  - reactome
  - hra
  - hubmap
  - sennet
  - stellar
  - dct
  - clinvar
  - cmap
  - hp
  - mp
  - msigdb
  - wikipathways
  - clingen
  - string
  - 4dn
  - erccrbp
  - erccreg
  - faldo
  - glycordf
  - glycocoo
  - gtex
  - kidsfirst
  - lincs
  - motrpac
  - mw
  - npo
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: Product
  description: Network embeddings of the Bioteque graph that represent biological
    entities and their associations
  id: bioteque.embeddings
  name: Bioteque Embeddings
  original_source:
  - chebi
  - cosmic
  - achilles
  - depmap
  - ccle
  - gdsc
  - cellosaurus
  - clue
  - ctd
  - pharmacodb
  - prism
  - drugbank
  - lincs
  - compartments
  - offsides
  - sider
  - drugcentral
  - repohub
  - chemicalchecker
  - repodb
  - disgenet
  - opentargets
  - creeds
  - interpro
  - reactome
  - tissues
  - dorothea
  - progeny
  - gtex
  - hpa
  - go
  - corum
  - huri
  - intact
  - omnipath
  - string
  - bto
  product_url: https://bioteque.irbbarcelona.org/downloads/embeddings
  secondary_source:
  - bioteque
- category: GraphProduct
  description: Integrated graph knowledge base combining Mendelian randomization causal
    estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships
    (Neo4j backend)
  format: neo4j
  id: epigraphdb.graph
  name: EpiGraphDB Graph Database
  original_source:
  - epigraphdb
  - kg-monarch
  - vectology
  - ukbiobank
  - prsatlas
  - eqtlgen
  - mondo
  - gtex
  - ensembl
  - cpic
  - opentargets
  - efo
  - semmeddb
  - intact
  - string
  - reactome
  - mrbase
  product_url: https://docs.epigraphdb.org/graph-database/
  secondary_source:
  - epigraphdb
publications:
- authors:
  - Diederik S. Laman Trip
  - Marc van Oostrum
  - Danish Memon
  - Fabian Frommelt
  - Delora Baptista
  - Kalpana Panneerselvam
  - Glyn Bradley
  - Luana Licata
  - Henning Hermjakob
  - Sandra Orchard
  - Gosia Trynka
  - Ellen M. McDonagh
  - Andrea Fossati
  - Ruedi Aebersold
  - Matthias Gstaiger
  - Bernd Wollscheid
  - Pedro Beltrao
  doi: doi:10.1038/s41587-025-02659-z
  id: https://doi.org/10.1038/s41587-025-02659-z
  journal: Nature Biotechnology
  preferred: true
  title: "A tissue-specific atlas of protein\u2013protein associations enables prioritization\
    \ of candidate disease genes"
  year: '2025'
- authors:
  - Cruz-Castillo, C.
  - Fumis, L.
  - Mehta, C.
  - Martinez-Osorio, R.E.
  - Roldan-Romero, J.M.
  - Cornu, H.
  - Uniyal, P.
  - Solano-Roman, A.
  - Carmona, M.
  - Ochoa, D.
  - McDonagh, E.M.
  - Buniello, A.
  doi: doi:10.1093/bioinformatics/btaf070
  id: https://doi.org/10.1093/bioinformatics/btaf070
  journal: Bioinformatics
  title: Associations on the Fly, a new feature aiming to facilitate exploration of
    the Open Targets Platform evidence
  year: '2025'
repository: https://github.com/opentargets
---
## Open Targets: Delivering Systematic Drug Target Selection

**Open Targets** is a pre-competitive partnership that systematically identifies and prioritizes drug targets to improve the success rate for developing safe and effective medicines. The consortium brings together expertise from leading pharmaceutical companies and academic research institutions to generate and integrate public data for better target selection in drug discovery.

### Overview

Open Targets was established as a public-private partnership to use human genetics and genomics data for systematic drug target identification and prioritization. The consortium is built on three core principles:

1. **A systematic approach**: Systematically identifying and prioritizing the best targets to safely and effectively treat rare and common diseases
2. **Open exchange of ideas**: Commitment to making data, methods, and results publicly available to foster open research
3. **Multidisciplinary collaboration**: Non-exclusive partnerships that encourage free exchange of ideas, expertise, and data

The consortium is formed by partner institutions including the European Bioinformatics Institute (EMBL-EBI), Genentech, GSK, MSD, Pfizer, Sanofi, and the Wellcome Sanger Institute.

### Key Products and Resources

#### Open Targets Platform

The [Open Targets Platform](https://platform.opentargets.org/) is the flagship product that integrates public data relevant to the associations between targets and diseases. It provides evidence-based validation for therapeutic targets by bringing together information from genetics, genomics, transcriptomics, drugs, animal models, and scientific literature. The Platform helps researchers:

- Identify and prioritize targets with strong evidence for association with a disease
- Explore the target-disease associations through multiple data types
- Find potential safety concerns for targets
- Discover potential drug repurposing opportunities

#### Open Targets Genetics

The [Open Targets Genetics](https://genetics.opentargets.org/) portal provides access to genetics data from genome-wide association studies (GWAS) and connects these to potential causal genes using various functional genomics data types. It helps researchers:

- Identify genetic associations for human traits and diseases
- Link genetic variants to likely causal genes using both statistical and functional evidence
- Explore colocalizations between traits that might share causal variants
- Investigate the functional impact of genetic variants

### Data Integration and Informatics

Open Targets' core bioinformatics work focuses on bringing together various data types relevant to human disease biology and target identification. The data ecosystem includes:

1. **Target-disease associations**: Evidence connecting genes/proteins to diseases from multiple data sources
2. **Target annotation**: Information about targets including protein structure, expression, and pathway involvement
3. **Disease annotation**: Disease classification, phenotypes, and ontology mapping
4. **Drug annotation**: Information about compounds, clinical trials, and mechanism of action

All data is made available through user-friendly web interfaces and APIs (GraphQL and REST) that allow programmatic access for integration into computational workflows.

### Research Focus Areas

Open Targets' research program focuses on three main therapeutic areas:
- **Oncology**
- **Neurodegeneration**
- **Immunology and Inflammation**

The consortium applies whole genome approaches and high-throughput methods to these disease areas, leveraging the expertise of all partners in emerging and established technologies.

### Open Source Commitment

Open Targets is committed to open science principles. Its software, data, and methods are publicly available, with code repositories accessible on [GitHub](https://github.com/opentargets). This open approach facilitates collaboration and encourages the broader scientific community to build upon and extend Open Targets' work.

### Impact on Drug Discovery

By providing systematic evidence for target-disease associations, Open Targets helps to address one of the key challenges in drug development: selecting the right targets. The platform reduces the risk of failure in later clinical development by enabling data-driven decisions early in the drug discovery process.

Through its integrated data resources and research programs, Open Targets is transforming how targets are selected for drug discovery, leading to more effective treatments for patients with both common and rare diseases.