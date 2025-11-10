---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.omim.org/contact
  label: OMIM (Johns Hopkins University)
description: OMIM (Online Mendelian Inheritance in Man) is a continuously updated,
  expert-curated catalog of human genes and genetic disorders, focusing on genotype–phenotype
  relationships and the molecular basis of disease.
domains:
- biomedical
- clinical
- genomics
homepage_url: https://www.omim.org/
id: omim
infores_id: omim
layout: resource_detail
license:
  id: https://www.omim.org/help/agreement
  label: OMIM Use Agreement (research/educational use; license required for commercial/redistribution)
name: OMIM
products:
- category: GraphicalInterface
  description: Web interface for browsing and searching OMIM entries
  format: http
  id: omim.web
  name: OMIM Website
  original_source:
  - omim
  product_url: https://www.omim.org/
- category: ProgrammingInterface
  description: REST-based API for programmatic access to OMIM data (registration and
    API key required)
  format: http
  id: omim.api
  is_public: false
  name: OMIM API
  original_source:
  - omim
  product_url: https://www.omim.org/api
- category: MappingProduct
  description: Public mapping of MIM numbers to NCBI Gene IDs, Ensembl Gene IDs, and
    HGNC symbols
  format: tsv
  id: omim.mim2gene
  name: OMIM mim2gene.txt
  original_source:
  - omim
  - ncbigene
  - ensembl
  - hgnc
  product_file_size: 974440
  product_url: https://www.omim.org/static/omim/data/mim2gene.txt
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
- category: MappingProduct
  description: MIM to Gene and MedGen mapping data connecting genetic disorders to
    genes
  format: tsv
  id: ncbigene.mim2gene_medgen
  name: MIM to Gene MedGen Mapping
  original_source:
  - ncbigene
  - medgen
  - omim
  product_file_size: 954971
  product_url: https://ftp.ncbi.nih.gov/gene/DATA/mim2gene_medgen
- category: GraphProduct
  description: Cleaned benchmark graph (PharmKG-8k) with typed relations between genes,
    chemicals, and diseases
  edge_count: 500958
  id: pharmkg.graph
  name: PharmKG graph
  node_count: 7603
  original_source:
  - omim
  - drugbank
  - pharmgkb
  - ttd
  - sider
  - humannet
  - ncbigene
  - mesh
  - pubchem
  - gnbr
  - biogps
  - connectivitymap
  product_url: https://zenodo.org/record/4077338
  secondary_source:
  - pharmkg
- category: Product
  description: Integrated gene annotation data aggregated from HGNC, OMIM, Ensembl,
    NCBI Gene, UniProt and other genomic databases
  format: http
  id: genecards.gene.annotations
  name: GeneCards Gene Annotations
  original_source:
  - hgnc
  - omim
  - ensembl
  - ncbigene
  - uniprot
  - refseq
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-11-09_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-11-06_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-11-10: HTTP 403 error
    when accessing file'
- category: Product
  description: Disease association data integrated from OMIM, MalaCards, ClinVar,
    Orphanet, DisGeNET and other disease databases
  format: http
  id: genecards.disease.associations
  name: GeneCards Disease Associations
  original_source:
  - omim
  - malacards
  - clinvar
  - orphanet
  - disgenet
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-11-09_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-11-06_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-11-10: HTTP 403 error
    when accessing file'
publications:
- id: https://doi.org/10.1093/nar/gky1151
  journal: Nucleic Acids Research
  preferred: true
  title: OMIM.org—leveraging knowledge across phenotype–gene relationships
  year: '2019'
- id: https://doi.org/10.1093/nar/gku1205
  journal: Nucleic Acids Research
  title: OMIM.org—an online catalog of human genes and genetic disorders
  year: '2015'
warnings:
- OMIM data are for research and educational use. Redistribution and commercial use
  require a license from Johns Hopkins University; API access requires registration
  and an API key.
---
# OMIM

OMIM (Online Mendelian Inheritance in Man) is a comprehensive, expert-curated knowledgebase of human genes and genetic phenotypes with a focus on genotype–phenotype relationships. Access is provided via the public website and a REST API (registration required). Most bulk download files require registration; the mim2gene.txt mapping is publicly available. Please cite OMIM and relevant literature when using the resource.