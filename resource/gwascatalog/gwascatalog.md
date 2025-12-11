---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: gwas-info@ebi.ac.uk
  - contact_type: url
    value: https://www.ebi.ac.uk/gwas/
  id: ebi
  label: NHGRI-EBI GWAS Catalog Team
creation_date: '2025-07-20T00:00:00Z'
description: The NHGRI-EBI GWAS Catalog is a curated, searchable, and freely available
  database of SNP-trait associations from published and submitted genome-wide association
  studies. Expert curators extract reported traits, significant variant-trait associations,
  and study metadata, providing an integrated resource updated on a weekly cycle and
  accessible via web interfaces, bulk downloads, summary statistics, and a REST API.
domains:
- genomics
- health
- biomedical
- investigations
homepage_url: https://www.ebi.ac.uk/gwas/
id: gwascatalog
infores_id: gwas-catalog
last_modified_date: '2025-09-02T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ebi.ac.uk/about/terms-of-use
  label: EMBL-EBI Terms of Use (summary statistics CC0 unless otherwise stated)
name: GWAS Catalog
products:
- category: GraphicalInterface
  description: Web interface for searching, browsing, and visualizing curated GWAS
    variant-trait associations and study metadata
  format: http
  id: gwascatalog.web
  name: GWAS Catalog Web Portal
  original_source:
  - gwascatalog
  product_url: https://www.ebi.ac.uk/gwas/
- category: ProgrammingInterface
  description: REST API providing programmatic access to GWAS Catalog studies, associations,
    variants, traits, and summary statistics metadata
  id: gwascatalog.api
  is_public: true
  name: GWAS Catalog REST API v2
  original_source:
  - gwascatalog
  product_url: https://www.ebi.ac.uk/gwas/docs/api
- category: Product
  description: Full data dump of GWAS Catalog associations in tab-delimited format
    (SNP-trait association data)
  format: tsv
  id: gwascatalog.associations.tsv
  name: GWAS Catalog Associations TSV
  original_source:
  - gwascatalog
  product_file_size: 482336061
  product_url: https://ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/gwas-catalog-associations.tsv
- category: Product
  description: Full data dump of GWAS Catalog associations in JSON format
  format: json
  id: gwascatalog.associations.json
  name: GWAS Catalog Associations JSON
  original_source:
  - gwascatalog
  product_url: https://ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/gwas-catalog-associations.json
  warnings:
  - File was not able to be retrieved when checked on 2025-12-09_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-11_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-11: HTTP 404 error
    when accessing file'
- category: Product
  description: Study metadata file containing per-study information for GWAS Catalog
    entries
  format: tsv
  id: gwascatalog.studies.tsv
  name: GWAS Catalog Studies TSV
  original_source:
  - gwascatalog
  product_file_size: 48604130
  product_url: https://ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/gwas-catalog-studies.tsv
- category: Product
  description: Variant metadata file containing per-variant information (e.g., rsIDs)
    present in the GWAS Catalog
  format: tsv
  id: gwascatalog.variants.tsv
  name: GWAS Catalog Variants TSV
  original_source:
  - gwascatalog
  product_url: https://ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/gwas-catalog-variants.tsv
  warnings:
  - File was not able to be retrieved when checked on 2025-12-09_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-11_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-11: HTTP 404 error
    when accessing file'
- category: Product
  description: EFO trait mapping file linking GWAS Catalog reported traits to Experimental
    Factor Ontology terms
  format: tsv
  id: gwascatalog.traits_efo.tsv
  name: GWAS Catalog Trait EFO Mappings TSV
  original_source:
  - gwascatalog
  product_url: https://ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/gwas-catalog-traits-efo.tsv
  warnings:
  - File was not able to be retrieved when checked on 2025-12-09_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-11_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-11: HTTP 404 error
    when accessing file'
- category: Product
  description: RDF/OWL representation of GWAS Catalog associations enabling semantic
    integration
  format: owl
  id: gwascatalog.associations.owl
  name: GWAS Catalog Associations OWL
  original_source:
  - gwascatalog
  product_url: https://ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/gwas-catalog-associations.owl.gz
  warnings:
  - File was not able to be retrieved when checked on 2025-12-09_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-11_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-11: HTTP 404 error
    when accessing file'
- category: DocumentationProduct
  description: Compressed GWAS Catalog diagram (karyotype visualization) in SVG format
    (current release)
  format: svg
  id: gwascatalog.diagram.current
  name: GWAS Catalog Diagram (Current SVG)
  original_source:
  - gwascatalog
  product_url: https://ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/gwas-catalog-diagram.svg
  warnings:
  - File was not able to be retrieved when checked on 2025-12-09_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-11_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-11: HTTP 404 error
    when accessing file'
- category: DocumentationProduct
  description: Archive of previous GWAS Catalog diagram versions (SVG format)
  format: svg
  id: gwascatalog.diagram.archive
  name: GWAS Catalog Diagram Archive
  original_source:
  - gwascatalog
  product_url: https://ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/gwas-catalog-diagram-archive.zip
  warnings:
  - File was not able to be retrieved when checked on 2025-12-09_ HTTP 404 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-11_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-11: HTTP 404 error
    when accessing file'
- category: DocumentationProduct
  description: Harmonised summary statistics landing page (FTP directory containing
    per-study summary statistics under CC0 where available)
  id: gwascatalog.summary_statistics.ftp
  name: GWAS Catalog Summary Statistics FTP
  original_source:
  - gwascatalog
  product_url: ftp://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/
  warnings:
  - 'File was not able to be retrieved when checked on 2025-12-04: Error connecting
    to URL: No connection adapters were found for ''ftp://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/'''
  - File was not able to be retrieved when checked on 2025-11-26_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/'
- category: GraphProduct
  description: GWASCatalog Automat
  format: kgx-jsonl
  id: automat.gwascatalog
  infores_id: automat-gwas-catalog
  name: gwascatalog_automat
  original_source:
  - gwascatalog
  product_url: https://stars.renci.org/var/plater/bl-4.2.1/GWASCatalog_Automat/e30aceb322a33462/
  secondary_source:
  - automat
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - doid
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
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
  - gwascatalog
  - phewascat
  - ukbiobank
  - finngen
  - clinicaltrialsgov
  product_url: https://www.disgenet.com/
  secondary_source:
  - disgenet
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
- category: Product
  description: The EPA has developed the Adverse Outcome Pathway Database (AOP-DB)
    to better characterize adverse outcomes of toxicological interest that are relevant
    to human health and the environment. Since its inception, the AOP-DB has been
    developed with the aim of integrating AOP molecular target information with other
    publicly available datasets to facilitate computational analyses of AOP information.
  id: aop-db.data
  name: AOP-DB Data
  original_source:
  - aop-wiki
  - ctd
  - toxcast
  - disgenet
  - ncbigene
  - string
  - 1000genomes
  - ensembl
  - gwascatalog
  product_url: https://catalog.data.gov/dataset/adverse-outcome-pathway-database-aop-db-version-2
  secondary_source:
  - aop-db
- category: GraphProduct
  description: Neo4j database dump of the Clinical Knowledge Graph and additional
    relationships
  dump_format: neo4j
  edge_count: 220000000
  format: mixed
  id: cancer-genome-interpreter.clinicalkg.graph
  name: CKG Graph Dump
  node_count: 16000000
  original_source:
  - uniprot
  - tissues
  - string
  - stitch
  - smpdb
  - signor
  - sider
  - refseq
  - reactome
  - phosphositeplus
  - pfam
  - oncokb
  - mutationds
  - intact
  - hpa
  - hmdb
  - hgnc
  - gwascatalog
  - foodb
  - drugbank
  - disgenet
  - diseases
  - dgidb
  - corum
  - cancer-genome-interpreter
  - doid
  - bto
  - efo
  - go
  - hp
  - snomedct
  - mod
  - mi
  - ms
  - uo
  product_url: https://data.mendeley.com/datasets/mrcf7f4tc2/1
- category: Product
  description: Genetic variant data from ClinVar, dbSNP, GWAS Catalog and other variant
    databases
  format: http
  id: genecards.variant.data
  name: GeneCards Variant Data
  original_source:
  - clinvar
  - dbsnp
  - gwascatalog
  product_url: https://www.genecards.org/
  warnings:
  - File was not able to be retrieved when checked on 2025-12-11_ HTTP 403 error when
    accessing file
  - File was not able to be retrieved when checked on 2025-12-09_ HTTP 403 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-11: HTTP 403 error
    when accessing file'
---
## Overview

The NHGRI-EBI GWAS Catalog provides a comprehensive, consistently curated, and publicly accessible collection of genome-wide association study (GWAS) results, including SNP-trait associations, study design and sample metadata, variant annotations, and trait ontology mappings. Data are curated by expert biocurators and released on a weekly schedule. Multiple access mechanisms are supported: interactive web portal, REST API, bulk downloads (TSV, JSON, OWL), ontology mappings, graphical diagram, and per-study summary statistics (including harmonised datasets).

## Access & Licensing

General usage is governed by EMBL-EBI Terms of Use. Unless otherwise noted, summary statistics are released under CC0. Users should also cite the 2025 Nucleic Acids Research publication (Cerezo et al. 2025) and individual studies when reusing summary statistics.

## Citation

Cerezo M, Sollis E, Ji Y, Lewis E, Abid A, Bircan KO, Hall P, et al. Nucleic Acids Research. 2025. doi:10.1093/nar/gkae1070.

## Contact

For questions or feedback email gwas-info@ebi.ac.uk. Mailing lists are available for announcements (gwas-announce@ebi.ac.uk) and user discussions (gwas-users@ebi.ac.uk).

# Gwascatalog

This is an automatically generated stub page for gwascatalog. Please update with proper information.