---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://emerge-network.org/
    label: eMERGE Network
creation_date: '2026-06-02T00:00:00Z'
description: The Electronic Medical Records and Genomics Network is an NIH/NHGRI-funded consortium that combines DNA biorepositories with electronic medical record systems for genomic discovery and genomic medicine implementation research.
domains:
  - genomics
  - clinical
  - precision medicine
homepage_url: https://emerge-network.org/
id: emerge
last_modified_date: '2026-06-03T00:00:00Z'
layout: resource_detail
name: Electronic Medical Records and Genomics Network
products:
  - category: GraphicalInterface
    description: eMERGE Network website describing network phases, study sites, working groups, genomic medicine implementation activities, and consortium resources.
    id: emerge.portal
    name: eMERGE Network Website
    original_source:
      - relation_type: prov:hadPrimarySource
        source: emerge
    product_url: https://emerge-network.org/
  - category: DocumentationProduct
    description: NHGRI project page summarizing eMERGE as an NIH-organized and funded consortium for combining biorepositories and electronic medical record systems in genomic medicine research.
    id: emerge.nhgri-project-page
    name: NHGRI eMERGE Project Page
    original_source:
      - relation_type: prov:hadPrimarySource
        source: emerge
    product_url: https://www.genome.gov/Funded-Programs-Projects/Electronic-Medical-Records-and-Genomics-Network-eMERGE
  - category: Product
    compression: zip
    description: PheWAS association results for SNPs from GWAS Catalog analyzed against EMR-derived phenotypes
    format: csv
    id: phewascat.associations
    name: PheWAS Association Data
    original_source:
      - relation_type: prov:hadPrimarySource
        source: phewascat
    product_file_size: 8229506
    product_url: https://phewascatalog.org/phewas/data/phewas-catalog.csv.zip
    secondary_source:
      - relation_type: prov:wasInformedBy
        source: gwascatalog
      - relation_type: prov:wasInformedBy
        source: emerge
publications:
  - authors:
      - J Denny
      - L Ritchie
      - M A Basford
      - J C Pulley
      - L Bastarache
      - K Brown-Gentry
    doi: 10.1093/bioinformatics/bts578
    id: doi:10.1093/bioinformatics/bts578
    journal: Bioinformatics
    preferred: true
    title: PheWAS with electronic medical records to find clinical phenotypes associated with SNPs
    year: '2013'
synonyms:
  - eMERGE
  - Electronic Medical Records and Genomics Network
taxon:
  - NCBITaxon:9606
---

# Electronic Medical Records and Genomics Network

The Electronic Medical Records and Genomics Network links genomic data, DNA
biorepositories, and electronic medical record systems across participating sites
to support genomic discovery and genomic medicine implementation research.
