---
activity_status: active
category: DataSource
collection:
- ber
contacts:
- category: Organization
  contact_details:
  - contact_type: github
    value: https://github.com/wikipathways
  - contact_type: url
    value: https://www.wikipathways.org/
  label: WikiPathways Team
- category: Individual
  contact_details:
  - contact_type: email
    value: apico@gladstone.ucsf.edu
  label: Alex Pico
- category: Individual
  contact_details:
  - contact_type: email
    value: martina.kutmon@maastrichtuniversity.nl
  label: Martina Kutmon
creation_date: '2025-06-05T00:00:00Z'
description: WikiPathways is an open, collaborative platform dedicated to the curation
  of biological pathways. The database contains 1,913 human-curated pathways across
  27 species with 36,334 gene products and 7,052 metabolites, supporting multiple
  data formats (GPML, GMT, RDF) and programmatic access via SPARQL endpoints and web
  APIs. Community-driven curation with version control and CI/CD infrastructure enables
  rapid pathway annotation and knowledge sharing in an open science framework.
domains:
- pathways
- genomics
- biomedical
homepage_url: https://www.wikipathways.org/
id: wikipathways
infores_id: wikipathways
last_modified_date: '2025-12-20T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/share-your-work/public-domain/cc0/
  label: CC0 (Creative Commons Zero)
  logo: http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png
name: WikiPathways
products:
- category: GraphProduct
  description: The SPOKE knowledge graph containing nodes and edges from multiple
    biomedical data sources.
  id: spoke.graph
  name: SPOKE Graph
  original_source:
  - ncbigene
  - pubmed
  - mesh
  - pid
  - doid
  - diseases
  - drugcentral
  - go
  - gwascatalog
  - reactome
  - lincs-l1000
  - uberon
  - wikipathways
  - bindingdb
  - drugbank
  - sider
  - bgee
  - uniprot
  - string
  - omim
  - chembl
  - foodb
  - civic
  - gdsc
  - clinicaltrialsgov
  - hpa
  - cl
  - kegg
  - metacyc
  - bv-brc
  - ncbitaxon
  - pathophenodb
  - pfam
  - interpro
  - protcid
  secondary_source:
  - spoke
- category: Product
  description: Pathways in Graphical Pathway Markup Language (GPML) format, which
    is a custom XML format for biological pathways
  format: xml
  id: wikipathways.gpml
  name: WikiPathways GPML
  product_url: https://data.wikipathways.org/current/gpml/
- category: Product
  description: Pathways in Gene Matrix Transposed (GMT) format for Gene Set Enrichment
    Analysis
  format: tsv
  id: wikipathways.gmt
  name: WikiPathways GMT
  product_url: https://data.wikipathways.org/current/gmt/
- category: Product
  description: Pathways in RDF (Resource Description Framework) format
  format: ttl
  id: wikipathways.rdf
  name: WikiPathways RDF
  product_url: http://data.wikipathways.org/current/rdf/
- category: ProgrammingInterface
  description: SPARQL endpoint for querying WikiPathways content
  id: wikipathways.sparql
  name: WikiPathways SPARQL Endpoint
  product_url: https://sparql.wikipathways.org/
- category: ProgrammingInterface
  description: Web service API for programmatic access to WikiPathways content
  id: wikipathways.api
  name: WikiPathways API
  product_url: https://webservice.wikipathways.org/ui/
- category: GraphicalInterface
  description: The main web interface for browsing, viewing, and downloading pathways
  id: wikipathways.web
  name: WikiPathways Web Interface
  product_url: https://www.wikipathways.org/
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
  - doid
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
  - connectivitymap
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
  - sckan
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
  - doid
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
  - connectivitymap
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
  - sckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - aop-db
  - bgee
  - disgenet
  - doid
  - drugbank
  - dsstox
  - go
  - gwascatalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://alzkb.ai:7473/login
  secondary_source:
  - alzkb
  - hetionet
- category: GraphProduct
  description: Memgraph data release for AlzKB.
  id: alzkb.data
  name: AlzKB Data Release (Version 2.0.0)
  original_source:
  - aop-db
  - bgee
  - disgenet
  - doid
  - drugbank
  - dsstox
  - go
  - gwascatalog
  - hrpimp
  - lincs-l1000
  - mesh
  - ncbigene
  - pharmacotherapydb
  - pid
  - pubchem
  - reactome
  - reactome
  - sider
  - tissues
  - uberon
  - wikipathways
  product_url: https://github.com/EpistasisLab/AlzKB/releases/tag/v2.0.0
  secondary_source:
  - alzkb
  - hetionet
- category: ProcessProduct
  description: INDRA CoGEx is a graph database integrating causal relations, ontological
    relations, properties, and data, assembled at scale automatically from the scientific
    literature and structured sources. This is the code to build the graph.
  id: indra.cogex.code
  name: INDRA CoGEx Build Code
  original_source:
  - chembl
  - sider
  - reactome
  - wikipathways
  - hp
  - nihreporter
  - disgenet
  - pubmed
  - gwascatalog
  - cellmarker
  - go
  - bgee
  - ccle
  - clinicaltrialsgov
  - indra
  product_url: https://github.com/gyorilab/indra_cogex
  secondary_source:
  - indra
- category: GraphProduct
  description: RNA-KG as a Neo4j Dump
  format: neo4j
  id: rna-kg.kg.neo4j
  name: RNA-KG Neo4j Dump
  original_source:
  - dbsnp
  - cosmic
  - rnacentral
  - ensembl
  - circbase
  - chebi
  - pr
  - ncbigene
  - cl
  - go
  - mondo
  - hp
  - uberon
  - vo
  - pw
  - reactome
  - wikipathways
  product_file_size: 3976840239
  product_url: https://rna-kg.biodata.di.unimi.it/rnakgv20.dump
  secondary_source:
  - rna-kg
- category: GraphProduct
  description: RNA-KG Nodes in CSV format
  format: csv
  id: rna-kg.kg.nodes
  name: RNA-KG Nodes
  original_source:
  - dbsnp
  - cosmic
  - rnacentral
  - ensembl
  - circbase
  - chebi
  - pr
  - ncbigene
  - cl
  - go
  - mondo
  - hp
  - uberon
  - vo
  - pw
  - reactome
  - wikipathways
  product_file_size: 4424633304
  product_url: https://rna-kg.biodata.di.unimi.it/nodes.csv
  secondary_source:
  - rna-kg
- category: GraphProduct
  description: RNA-KG Edges in CSV format
  format: csv
  id: rna-kg.kg.edges
  name: RNA-KG Edges
  original_source:
  - dbsnp
  - cosmic
  - rnacentral
  - ensembl
  - circbase
  - chebi
  - pr
  - ncbigene
  - cl
  - go
  - mondo
  - hp
  - uberon
  - vo
  - pw
  - reactome
  - wikipathways
  product_file_size: 18370248815
  product_url: https://rna-kg.biodata.di.unimi.it/edges.csv
  secondary_source:
  - rna-kg
- category: Product
  description: Pathway information integrated from Reactome, WikiPathways and other
    pathway databases
  format: http
  id: genecards.pathway.data
  name: GeneCards Pathway Data
  original_source:
  - reactome
  - wikipathways
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2026-01-30_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2026-01-28_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2026-02-04: HTTP 403 error
    when accessing file'
- category: Product
  description: WikiPathways data for all targets
  format: txt
  id: ttd.wiki-pathways
  name: Target WikiPathways
  original_source:
  - wikipathways
  product_url: https://idrblab.net/ttd/sites/default/files/ttd_download/P4-06-Target_wikipathway.txt
  secondary_source:
  - ttd
  warnings:
  - File was not able to be retrieved when checked on 2025-10-29_ Error connecting
    to URL_ ('Connection aborted.', ConnectionResetError(104, 'Connection reset by
    peer'))
- category: DatabaseProduct
  description: Multi-sourced relational database integrating metabolomic pathway information,
    biochemical reactions, ontologies, and chemical descriptors for genes, proteins,
    and metabolites with query and enrichment analysis capabilities.
  id: rampdb.database
  is_public: true
  name: RaMP-DB Integrated Database
  original_source:
  - kegg
  - reactome
  - hmdb
  - wikipathways
  - rampdb
  product_url: https://rampdb.nih.gov/
- category: GraphProduct
  compression: gzip
  description: protein network data (full network, scored links between proteins)
  format: txt
  id: string.protein.links
  name: STRING Protein Links
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 138154280240
  product_url: https://stringdb-downloads.org/download/protein.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (full network, incl. subscores per channel)
  format: txt
  id: string.protein.links.detailed
  name: STRING Protein Links Detailed
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 203534412387
  product_url: https://stringdb-downloads.org/download/protein.links.detailed.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: 'protein network data (full network, incl. distinction: direct vs.
    interologs)'
  format: txt
  id: string.protein.links.full
  name: STRING Protein Links Full
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 214269334954
  product_url: https://stringdb-downloads.org/download/protein.links.full.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (physical subnetwork, scored links between proteins)
  format: txt
  id: string.protein.physical.links
  name: STRING Protein Physical Links
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 11867396121
  product_url: https://stringdb-downloads.org/download/protein.physical.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: protein network data (physical subnetwork, incl. subscores per channel)
  format: txt
  id: string.protein.physical.links.detailed
  name: STRING Protein Physical Links Detailed
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 14859366689
  product_url: https://stringdb-downloads.org/download/protein.physical.links.detailed.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: 'protein network data (physical subnetwork, incl. distinction: direct
    vs. interologs)'
  format: txt
  id: string.protein.physical.links.full
  name: STRING Protein Physical Links Full
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 15528028374
  product_url: https://stringdb-downloads.org/download/protein.physical.links.full.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: association scores between orthologous groups
  format: txt
  id: string.cog.links
  name: STRING COG Links
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 185338269
  product_url: https://stringdb-downloads.org/download/COG.links.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: association scores (incl. subscores per channel)
  format: txt
  id: string.cog.links.detailed
  name: STRING COG Links Detailed
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 250279091
  product_url: https://stringdb-downloads.org/download/COG.links.detailed.v12.0.txt.gz
- category: GraphProduct
  compression: gzip
  description: 'full database, part II: the networks (nodes, edges, scores,...)'
  id: string.database
  name: STRING Database Network Schema
  original_source:
  - biocyc
  - biogrid
  - cog
  - compartments
  - dip
  - diseases
  - eggnog
  - ensembl
  - flybase
  - geo
  - go
  - hprd
  - hgnc
  - intact
  - interpro
  - kegg
  - mint
  - omim
  - pdb
  - pfam
  - proteomehd
  - pubmedcentral
  - reactome
  - refseq
  - sgd
  - simap
  - smart
  - swissmodel
  - tissues
  - uniprot
  - wikipathways
  - wormbase
  - progenomes
  product_file_size: 281505096430
  product_url: https://stringdb-downloads.org/download/network_schema.v12.0.sql.gz
publications:
- authors:
  - Agrawal A
  - et al.
  doi: doi:10.1093/nar/gkad960
  id: https://doi.org/10.1093/nar/gkad960
  journal: Nucleic Acids Research
  preferred: true
  title: WikiPathways 2024 - next generation pathway database
  year: '2024'
- authors:
  - Martens M
  - et al.
  doi: doi:10.1093/NAR/gkaa1024
  id: https://doi.org/10.1093/NAR/gkaa1024
  journal: Nucleic Acids Research
  title: WikiPathways - connecting communities
  year: '2021'
repository: https://github.com/wikipathways/wikipathways-database
taxon:
- NCBITaxon:9606
- NCBITaxon:10090
---
# WikiPathways

WikiPathways is an open, collaborative platform dedicated to the curation and dissemination of biological pathways. Established to facilitate community contribution and maintenance of pathway knowledge, WikiPathways provides researchers with a user-friendly web interface and comprehensive toolkit for discovering, visualizing, analyzing, and sharing biological pathway information across 27 organisms.

## Overview and Mission

WikiPathways operates on open science principles with a mission to democratize pathway knowledge curation by leveraging the expertise of the global research community. The platform reduces barriers to participation through intuitive web-based tools while maintaining rigorous quality standards through peer review and modern software development practices including version control and continuous integration testing.

## Database Content and Scale

### Pathway Coverage

**Current Content (2024):**
- **1,913 curated pathways** across 27 species
- **866 human pathways** (approximately 45% of total)
- **36,334 gene products** integrated across all pathways
- **7,052 metabolites** represented in pathway models
- **85,647 molecular interactions** documented
- **201 pathway authors** with contributions over the past three years
- **10,873 edits** in the past three years reflecting active community engagement

### Species Coverage

WikiPathways provides comprehensive pathway information for:
- **Human** (primary focus with 866 curated pathways)
- **Model organisms** with automatic homology-based translations:
  - Mouse
  - Rat
  - Zebrafish
  - Fruit fly (Drosophila melanogaster)
  - Caenorhabditis elegans
  - Yeast (Saccharomyces cerevisiae)
  - Arabidopsis thaliana
  - And 4 additional vertebrate organisms

### Pathway Types and Coverage

WikiPathways covers diverse biological processes including:
- **Signal transduction pathways** - Cell signaling and communication
- **Metabolic pathways** - Biochemical transformations and energy production
- **Gene regulatory networks** - Transcriptional control and expression
- **Disease pathways** - Mechanisms underlying specific diseases
- **Drug response pathways** - Pharmacological interactions and responses
- **Developmental pathways** - Organism growth and differentiation
- **Immune response pathways** - Immunological mechanisms
- **Cross-kingdom interactions** - Plant-pathogen, host-microbe interactions

## Data Access Methods

### Web Interface

**Main Portal:** https://www.wikipathways.org/

The redesigned WikiPathways website (2024 update) offers:
- **Interactive pathway browsing** with expandable pathway trees and hierarchical organization
- **Full-text search** across pathway names, descriptions, and molecular components
- **Pathway pages** displaying current diagrams, descriptions, authors, references, citations, annotations
- **Community features** for connecting with authors, viewing edit history, and learning contribution guidelines
- **Pathway editing interface** with integrated collaboration tools
- **Version history tracking** via Git-backed version control
- **Export capabilities** in multiple formats directly from the web interface

### Programmatic Interfaces

**SPARQL Endpoint:** https://sparql.wikipathways.org/
- Full W3C SPARQL 1.1 protocol support
- Query WikiPathways RDF data using semantic graph patterns
- Complex federated queries for cross-database integration
- Result formats: JSON, XML, CSV, TSV, N-Triples

**Web Service API:** https://webservice.wikipathways.org/ui/
- RESTful API for programmatic pathway queries
- Query types: search, getPathways, getPathwaysByXref, getPathwaysByParentOntology
- Return formats: JSON, XML
- Supports batch operations and complex filtering

**R Package - rWikiPathways:**
- CRAN package for R environments
- Programmatic queries from R/Bioconductor
- Integrates with pathway analysis workflows
- Available at: https://cran.r-project.org/web/packages/rWikiPathways/

**Python Package - pywikipathways:**
- Python interface to WikiPathways API
- Integration with scientific Python stack
- Supports data analysis and visualization workflows

### Data Download Services

**Download Portal:** https://data.wikipathways.org/

Available in multiple formats:
- **GPML** (Graphical Pathway Markup Language) - Native WikiPathways XML format
- **GMT** (Gene Matrix Transposed) - Gene set format for pathway enrichment analysis
- **RDF** (Resource Description Framework) - Semantic web format
- **SVG and PNG** - Image formats for visualization and publication
- **TSV** - Tab-separated tabular data

Organized by:
- Species-specific exports
- Individual pathway downloads
- Batch downloads with compressed archives
- Versioned releases for reproducibility

## Data Standards and Technical Infrastructure

### Biological Data Representation

**GPML (Graphical Pathway Markup Language):**
- Custom XML format purpose-built for pathway diagrams
- Supports visualization of nodes (genes, proteins, metabolites) and interactions
- Compatible with pathway visualization tools (PathVisio, Cytoscape)
- Preserves layout, styling, and annotation information

**Gene Matrix Transposed (GMT):**
- Standard format for pathway enrichment analysis
- Compatible with GSEA (Gene Set Enrichment Analysis) and similar tools
- Lists genes/proteins per pathway for statistical testing

**RDF and Semantic Web:**
- Triple-based knowledge representation for linked data
- Enables integration with biomedical ontologies and cross-database queries
- Semantic reasoning over implicit pathway relationships
- Interoperability with other linked data resources

### Curation Infrastructure

**Community-Driven Curation Process:**
- Version control via Git for all pathway content
- Pull request workflow for quality control
- Automated testing of pathway structure and data integrity
- Continuous integration ensuring only valid pathways are published
- Distinction between automated and human-reviewed merges
- Focus on human expertise for biologically significant changes

**Quality Assurance:**
- Peer review by domain experts
- Cross-reference validation (genes, proteins, metabolites)
- Consistency checking across species homologs
- Automated identifier validation and standardization

## Use Cases and Applications

### Pathway Analysis and Discovery

- **Gene Set Enrichment Analysis (GSEA)** - Using GMT-formatted pathways for statistical significance testing
- **Network analysis** - Visualizing interaction networks and identifying functional modules
- **Pathway visualization** - Creating publication-quality pathway diagrams
- **Cross-species comparison** - Leveraging homology mappings for comparative pathway analysis

### Systems Biology and Modeling

- **Systems-level understanding** - Integrating multi-omics data with pathway context
- **Hypothesis generation** - Identifying novel pathway interactions and cross-talk
- **Computational modeling** - Using pathway diagrams as templates for mathematical models
- **Integrated pathway analysis** - Combining multiple pathways into larger biological systems

### Drug Discovery and Development

- **Target identification** - Identifying potential drug targets within pathways
- **Drug response pathways** - Understanding how drugs interact with biological systems
- **Adverse effect prediction** - Mapping potential side effects through pathway mechanisms
- **Polypharmacology** - Identifying off-target drug interactions

### Educational Applications

- **Pathway biology learning** - Educational resources for understanding biological mechanisms
- **Bioinformatics training** - Examples for computational biology education
- **Collaborative learning** - Community-driven knowledge building in research groups

### Integration with Other Tools and Databases

WikiPathways integrates with diverse analysis platforms:
- **Cytoscape plugins** - Direct pathway visualization in Cytoscape
- **PathVisio** - Pathway editing and analysis
- **Enrichment Map** - GSEA pathway enrichment visualization
- **BioGRID, STRING** - Protein interaction network overlays
- **Systems biology tools** - Including Reactome and KEGG integration

## Organizational Structure and Leadership

### Leadership Team

**Martina Kutmon** (Maastricht University)
- Pathway curator and database manager
- Contact: martina.kutmon@maastrichtuniversity.nl
- Expertise in pathway curation and knowledge management

**Alex Pico** (Gladstone Institutes, UCSF)
- Scientific director and original pathway curation lead
- Contact: apico@gladstone.ucsf.edu
- Long-standing commitment to open pathway knowledge

### Host and Partner Institutions

**Primary Affiliation:**
- Maastricht University (Department of Bioinformatics - BiGCaT)
- Provides infrastructure, funding, and institutional support

**Contributing Institutions:**
- Gladstone Institutes (UCSF)
- International research community contributions

### Community Model

- **Open-source development** with transparent governance
- **Community curation** leveraging global pathway expertise
- **Public Git repository** for source code and database content
- **Distributed development** with contributions from 201+ authors
- **Ongoing maintenance** with active community engagement

## Funding and Sustainability

**Primary Support:**
- Institutional funding from Maastricht University and partner institutions
- NIH and EU research funding for specific projects
- Community volunteer contributions
- OpenStack community infrastructure support

**Status:**
- Actively maintained with regular database releases
- Continuous improvements to infrastructure and tools
- Growing pathway collection with average of 84 new pathways per year

## Standards Compliance and Interoperability

- **Open Science Standards** - CC0 public domain licensing
- **Semantic Web Standards** - RDF, SPARQL, OWL compatibility
- **Biological Data Standards** - Integration with Gene Ontology, CHEBI, UniProt identifiers
- **Interoperability** - Support for pathway exchange formats and cross-database queries
- **FAIR Principles** - Findable, Accessible, Interoperable, Reusable data

## Citation and Usage

WikiPathways data and services are freely accessible with CC0 (public domain) licensing. All pathway content is available for unrestricted use with optional attribution to the original authors.

### Recommended Citation

For WikiPathways general use:
"WikiPathways. Available at: https://www.wikipathways.org/"

For research using WikiPathways data, cite the latest update:
"Agrawal A, et al. (2024) WikiPathways 2024: next generation pathway database. Nucleic Acids Research. 52(D1):D679-D685. https://doi.org/10.1093/nar/gkad960"

For previous versions, see full publication record below.

### Additional Resources

- **Main Website:** https://www.wikipathways.org/
- **SPARQL Endpoint:** https://sparql.wikipathways.org/
- **Web Service API:** https://webservice.wikipathways.org/ui/
- **Data Downloads:** https://data.wikipathways.org/
- **GitHub Repository:** https://github.com/wikipathways/wikipathways-database
- **R Package (rWikiPathways):** https://cran.r-project.org/web/packages/rWikiPathways/
- **Python Package:** https://github.com/wikipathways/pywikipathways
- **Pathway Editing Guide:** https://www.wikipathways.org/index.php/Help:EditPathway
- **API Documentation:** https://webservice.wikipathways.org/
- **GitHub Organization:** https://github.com/wikipathways

WikiPathways continues to serve as the premier open-source pathway database, enabling researchers worldwide to discover biological knowledge, share pathway expertise, and integrate pathway information into systems biology research through modern collaborative tools and open science practices.