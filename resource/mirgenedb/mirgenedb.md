---
activity_status: active
category: DataSource
creation_date: '2025-09-09T00:00:00Z'
description: MirGeneDB is a manually curated database of microRNA genes, providing validated and annotated microRNA gene entries for over 21,000 genes from 114 metazoan species. It offers uniform nomenclature, evolutionary context, and downloadable data for all species and families.
domains:
  - genomics
  - biological systems
id: mirgenedb
last_modified_date: '2025-10-15T00:00:00Z'
layout: resource_detail
name: MirGeneDB
products:
  - category: GraphicalInterface
    name: MirGeneDB Web Portal
    id: mirgenedb.portal
    description: Web interface for browsing, searching, and exploring curated microRNA gene entries and families across 114 metazoan species.
    format: http
    product_url: https://mirgenedb.org/
  - category: Product
    name: MirGeneDB Species-Specific Downloads
    id: mirgenedb.species_downloads
    description: Downloadable FASTA, GFF, BED, and tabular files for microRNA genes from individual species.
    format: http
    product_url: https://mirgenedb.org/download
  - category: Product
    name: MirGeneDB Covariance Models
    id: mirgenedb.covariance
    description: Downloadable covariance models for more than 700 conserved microRNA families.
    format: http
    product_url: https://mirgenedb.org/covariance
  - category: Product
    name: MirGeneDB Processed Read Data
    id: mirgenedb.reads
    description: Downloadable processed FASTA files of all read data used in MirGeneDB annotations.
    format: fasta
    product_url: https://mirgenedb.org/download
  - category: Product
    name: MirGeneDB Bulk Data Archive
    id: mirgenedb.bulk
    description: Bulk download ZIP archives for all microRNA gene data across species.
    format: http
    product_url: https://mirgenedb.org/download
  - category: DocumentationProduct
    name: MirGeneDB Information and Help
    id: mirgenedb.info
    description: Documentation and information about MirGeneDB nomenclature, annotation standards, and database usage.
    format: http
    product_url: https://mirgenedb.org/information
publications:
  - id: "https://doi.org/10.1093/nar/gkae1094"
    preferred: true
    title: "MirGeneDB 3.0: improved taxonomic sampling, uniform nomenclature of novel conserved microRNA families and updated covariance models"
    authors:
      - Clarke AW
      - Høye E
      - Hembrom AA
      - Paynter VM
      - Vinther J
      - Wyrożemski Ł
      - Biryukova I
      - Formaggioni A
      - Ovchinnikov V
      - Herlyn H
    year: "2024"
    journal: "Nucleic Acids Research"
---

# MirGeneDB

MirGeneDB is a manually curated database of microRNA genes, providing validated and annotated entries for over 21,000 genes from 114 metazoan species. The database offers uniform nomenclature, evolutionary context, and downloadable data for all species and families. Users can browse, search, and download microRNA gene data in multiple formats (FASTA, GFF, BED, tabular, ZIP) and access covariance models for conserved families. For more information, visit the [MirGeneDB portal](https://mirgenedb.org/).
