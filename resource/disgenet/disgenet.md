---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: info@disgenet.com
  label: MedBioinformatics Solutions SL
description: DisGeNET is the world's largest and most extensive gene-disease association
  (GDA) network, integrating data from expert-curated repositories, GWAS catalogs,
  animal models, and scientific literature. It contains gene-disease associations,
  variant-disease associations, and disease-disease associations with extensive evidence
  supporting each connection.
domains:
- biomedical
- genomics
- clinical
- precision medicine
- translational
- drug discovery
homepage_url: https://www.disgenet.com/
id: disgenet
layout: resource_detail
license:
  id: https://www.disgenet.com/Legal
  label: DisGeNET License
name: DisGeNET
products:
- category: GraphProduct
  description: DisGeNET data, including gene to disease associations and variant to
    disease associations (requires registration and subscription).
  id: disgenet.data
  name: DisGeNET Data
  original_source:
  - clingen
  - clinvar
  - mgd
  - rgd
  - orphanet
  - psygenet
  - uniprot
  - disgenet
  - hp
  - gwascat
  - phewascat
  - ukbiobank
  - finngen
  - clinicaltrialsgov
  product_url: https://www.disgenet.com/
  secondary_source:
  - disgenet
- category: ProgrammingInterface
  description: API access to DisGeNET data (requires registration and subscription).
  format: http
  id: disgenet.api
  name: DisGeNET API
  original_source:
  - disgenet
  product_url: https://www.disgenet.com/
  secondary_source:
  - disgenet
- category: GraphicalInterface
  description: Browser for DisGeNET data (requires registration and subscription).
  format: http
  id: disgenet.browser
  name: DisGeNET Browser
  original_source:
  - disgenet
  product_url: https://www.disgenet.com/search?view=ALL&idents=ALL&source=ALL&tab=GDA
  secondary_source:
  - disgenet
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
- category: GraphProduct
  description: Nodes for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.nodes
  name: RTX-KG2.10.1c KGX JSONL Nodes
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-nodes.jsonl.gz
  secondary_source:
  - rtx-kg2.code
- category: GraphProduct
  description: Edges for KGX distribution of the RTX-KG2 (RTX-KG2.10.1c)
  format: kgx-jsonl
  id: rtx-kg2.graph.edges
  name: RTX-KG2.10.1c KGX JSONL Edges
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  product_url: https://rtx-kg2-public.s3.us-west-2.amazonaws.com/kg2c-2.10.1-v1.0-edges.jsonl.gz
  secondary_source:
  - rtx-kg2.code
- category: ProgrammingInterface
  description: Neo4j distribution of the RTX-KG2 as a graph database
  dump_format: neo4j
  id: rtx-kg2.neo4j
  is_neo4j: true
  is_public: false
  name: RTX-KG2 Neo4j
  original_source:
  - chembl
  - drugbank
  - kegg
  - reactome
  - go
  - drugcentral
  - uniprot
  - mondo
  - hp
  - chebi
  - uberon
  - ncbitaxon
  - dgidb
  - disgenet
  - ensembl
  - gtopdb
  - rtx-kg2
  product_url: https://arax.ncats.io/
  secondary_source:
  - rtx-kg2.code
- category: GraphicalInterface
  description: A browser interface for a knowledge graph for Alzheimer's Disease.
  format: http
  id: alzkb.browser
  name: AlzKB Graph Database Browser
  original_source:
  - aop-db
  - bgee
  - disgenet
  - do
  - drugbank
  - dsstox
  - go
  - gwas-catalog
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
  - do
  - drugbank
  - dsstox
  - go
  - gwas-catalog
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
  - pharmdb
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
publications:
- authors:
  - "Janet Pi\xF1ero"
  - "Juan Manuel Ram\xEDrez-Anguita"
  - "Josep Sa\xFCch-Pitarch"
  - Francesco Ronzano
  - Emilio Centeno
  - Ferran Sanz
  - Laura I. Furlong
  doi: 10.1093/nar/gkz1021
  id: doi:10.1093/nar/gkz1021
  journal: Nucleic Acids Research
  preferred: true
  title: The DisGeNET knowledge platform for disease genomics - 2019 update
  year: '2020'
---
# DisGeNET

DisGeNET is the world's largest and most extensive gene-disease association network, integrating data from numerous expert-curated repositories, GWAS catalogs, animal models, and the scientific literature. It provides a comprehensive resource for investigating the genetic basis of human diseases and facilitates research in genomics, precision medicine, and drug discovery.

## Overview

DisGeNET version 25.1.1 (current as of June 2025) contains:
- 1,982,885 gene-disease associations (GDAs) between 29,460 genes and 42,277 diseases and phenotypes
- 4,397,303 variant-disease associations (VDAs) between 1,425,623 variants and 19,067 diseases and phenotypes
- Over 28 million disease-disease associations (DDAs) based on shared genes and variants
- 14,643 chemicals and drugs associated with GDAs and VDAs
- Over 13 million individual pieces of evidence supporting 6.38 million genotype-phenotype associations
- Evidence supported by 1.6 million scientific publications

## Data Sources

DisGeNET integrates data from multiple types of sources:

### Curated Sources
- Expert-curated databases: UniProt/SwissProt, ClinVar, PsyGeNET, Orphanet, ClinGen
- Model organism databases: Mouse Genome Database (MGD), Rat Genome Database (RGD)

### GWAS & Clinical Studies
- GWAS Catalog
- Phewas Catalog
- UK Biobank (545,400 VDAs between 1,330 clinical endpoints and 213,328 SNPs)
- FinnGen (2.7M VDAs between 2,026 clinical endpoints and 636,644 SNPs)
- Clinical trials data from ClinicalTrials.gov

### Literature-Based Sources
- Text-mined associations from scientific literature on human studies
- Text-mined associations from studies using animal models

## Applications

DisGeNET is designed to support multiple use cases:
- Target identification and validation for drug discovery
- Genomic data interpretation for precision medicine
- Disease mechanism exploration
- Drug repurposing
- Patient stratification
- Biomarker discovery
- Genetic test development

## Access & Availability

DisGeNET offers different access options based on user needs:
- Web platform for searching and exploring data
- API for programmatic access (requires registration)
- R package (disgenet2r) for data analysis within R
- Integration with multiple knowledge graphs like UBKG and RTX-KG2

Access to DisGeNET is tiered, with different plans available for academic researchers (free) and commercial users. The academic plan provides access to curated resources, while more comprehensive plans include text-mined data, drug/chemical annotations, and API access.