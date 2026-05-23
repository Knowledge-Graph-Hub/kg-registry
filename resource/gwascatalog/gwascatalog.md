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
last_modified_date: '2026-05-23T00:00:00Z'
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
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  product_url: https://www.ebi.ac.uk/gwas/
- category: ProgrammingInterface
  description: REST API providing programmatic access to GWAS Catalog studies, associations,
    variants, traits, and summary statistics metadata
  id: gwascatalog.api
  is_public: true
  name: GWAS Catalog REST API v2
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  product_url: https://www.ebi.ac.uk/gwas/docs/api
- category: Product
  description: Full data dump of GWAS Catalog associations in tab-delimited format
    (SNP-trait association data)
  format: tsv
  id: gwascatalog.associations.tsv
  name: GWAS Catalog Associations TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  product_file_size: 482336061
  product_url: https://ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/gwas-catalog-associations.tsv
- category: Product
  description: Full data dump of GWAS Catalog associations in JSON format
  format: json
  id: gwascatalog.associations.json
  name: GWAS Catalog Associations JSON
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  product_url: https://ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/gwas-catalog-associations.json
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-21: HTTP 404 error
    when accessing file'
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 404 error when
    accessing file
- category: Product
  description: Study metadata file containing per-study information for GWAS Catalog
    entries
  format: tsv
  id: gwascatalog.studies.tsv
  name: GWAS Catalog Studies TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  product_file_size: 48604130
  product_url: https://ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/gwas-catalog-studies.tsv
- category: Product
  description: Variant metadata file containing per-variant information (e.g., rsIDs)
    present in the GWAS Catalog
  format: tsv
  id: gwascatalog.variants.tsv
  name: GWAS Catalog Variants TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  product_url: https://ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/gwas-catalog-variants.tsv
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-21: HTTP 404 error
    when accessing file'
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 404 error when
    accessing file
- category: Product
  description: EFO trait mapping file linking GWAS Catalog reported traits to Experimental
    Factor Ontology terms
  format: tsv
  id: gwascatalog.traits_efo.tsv
  name: GWAS Catalog Trait EFO Mappings TSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  product_url: https://ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/gwas-catalog-traits-efo.tsv
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-21: HTTP 404 error
    when accessing file'
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 404 error when
    accessing file
- category: Product
  description: RDF/OWL representation of GWAS Catalog associations enabling semantic
    integration
  format: owl
  id: gwascatalog.associations.owl
  name: GWAS Catalog Associations OWL
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  product_url: https://ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/gwas-catalog-associations.owl.gz
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-21: HTTP 404 error
    when accessing file'
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 404 error when
    accessing file
- category: DocumentationProduct
  description: Compressed GWAS Catalog diagram (karyotype visualization) in SVG format
    (current release)
  format: svg
  id: gwascatalog.diagram.current
  name: GWAS Catalog Diagram (Current SVG)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  product_url: https://ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/gwas-catalog-diagram.svg
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-21: HTTP 404 error
    when accessing file'
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 404 error when
    accessing file
- category: DocumentationProduct
  description: Archive of previous GWAS Catalog diagram versions (SVG format)
  format: svg
  id: gwascatalog.diagram.archive
  name: GWAS Catalog Diagram Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  product_url: https://ftp.ebi.ac.uk/pub/databases/gwas/releases/latest/gwas-catalog-diagram-archive.zip
  warnings:
  - 'File was not able to be retrieved when checked on 2026-05-21: HTTP 404 error
    when accessing file'
  - File was not able to be retrieved when checked on 2026-03-30_ HTTP 404 error when
    accessing file
- category: DocumentationProduct
  description: Harmonised summary statistics landing page (FTP directory containing
    per-study summary statistics under CC0 where available)
  id: gwascatalog.summary_statistics.ftp
  name: GWAS Catalog Summary Statistics FTP
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  product_url: ftp://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/
  warnings:
  - File was not able to be retrieved when checked on 2025-11-26_ Error connecting
    to URL_ No connection adapters were found for 'ftp_//ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/'
---
## Overview

The NHGRI-EBI GWAS Catalog provides a comprehensive, consistently curated, and publicly accessible collection of genome-wide association study (GWAS) results, including SNP-trait associations, study design and sample metadata, variant annotations, and trait ontology mappings. Data are curated by expert biocurators and released on a weekly schedule. Multiple access mechanisms are supported: interactive web portal, REST API, bulk downloads (TSV, JSON, OWL), ontology mappings, graphical diagram, and per-study summary statistics (including harmonised datasets).

## Access & Licensing

General usage is governed by EMBL-EBI Terms of Use. Unless otherwise noted, summary statistics are released under CC0. Users should also cite the 2025 Nucleic Acids Research publication (Cerezo et al. 2025) and individual studies when reusing summary statistics.

## Citation

Cerezo M, Sollis E, Ji Y, Lewis E, Abid A, Bircan KO, Hall P, et al. Nucleic Acids Research. 2025. doi:10.1093/nar/gkae1070.

## Contact

For questions or feedback email gwas-info@ebi.ac.uk. Mailing lists are available for announcements (gwas-announce@ebi.ac.uk) and user discussions (gwas-users@ebi.ac.uk).