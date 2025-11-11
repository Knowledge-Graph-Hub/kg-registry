---
activity_status: active
category: Aggregator
contacts:
  - category: Organization
    label: The Jackson Laboratory
    contact_details:
      - contact_type: url
        value: "https://www.jax.org/"
      - contact_type: email
        value: "mgi-help@jax.org"
  - category: Organization
    label: Mouse Genome Informatics
    contact_details:
      - contact_type: url
        value: "https://www.informatics.jax.org/"
creation_date: '2025-01-10T00:00:00Z'
description: The Mouse Genome Database (MGD) is the international database resource for the laboratory mouse serving as the authoritative source of integrated genetic, genomic, and biological data to facilitate the study of human health and disease through mouse models. Developed and maintained by the Mouse Genome Informatics consortium at The Jackson Laboratory, MGD provides comprehensive information on mouse genes, genome features, mammalian orthology, phenotypes, allelic variants, disease models, and extensive curated experimental data. The database integrates multiple specialized resources including the Gene Expression Database documenting spatial and temporal patterns of gene expression during mouse development and adulthood, the Mouse Models of Human Cancer database cataloging spontaneous and induced tumors, and extensive phenotype annotations using the Mammalian Phenotype Ontology. MGD contains curated data for all mouse genes with standardized nomenclature, genomic coordinates, functional annotations from Gene Ontology, expression patterns, phenotype associations, human disease connections, and literature references. The resource supports comparative genomics by providing detailed orthology relationships between mouse and human genes enabling translation of findings between species for biomedical research. MGD offers sophisticated search interfaces for genes, phenotypes, alleles, strains, polymorphisms including dramatically expanded SNP data, recombinase activity patterns for cre lines, and RNA-seq experiments, along with genome browsers, batch query tools, and data downloads in various formats. The database integrates data from high-throughput projects including the International Mouse Phenotyping Consortium systematic knockout phenotyping and Ensembl regulatory annotations. With over 30 years of continuous development since its 1994 web release, MGD collaborates with the Alliance of Genome Resources to harmonize model organism data and serves as an essential resource for the global mouse research community providing standardized, expert-curated knowledge.
domains:
  - genomics
homepage_url: https://www.informatics.jax.org/
id: "mgd"
infores_id: "mgi"
last_modified_date: '2025-01-10T00:00:00Z'
layout: resource_detail
name: Mouse Genome Database
products:
  - category: GraphicalInterface
    description: Primary web interface providing integrated access to mouse genes, phenotypes, expression data, disease models, and genome features
    id: "mgd.portal"
    name: MGI Web Portal
    original_source:
      - mgd
    product_url: https://www.informatics.jax.org/
  - category: Product
    description: Downloadable data reports including genes, markers, phenotypes, expression annotations, and orthology in various formats
    format: txt
    id: "mgd.downloads"
    name: MGD Data Downloads
    original_source:
      - mgd
    product_url: https://www.informatics.jax.org/downloads/reports/index.html
  - category: ProgrammingInterface
    description: MouseMine data mining platform providing programmatic access to MGD data through InterMine query interface
    id: "mgd.mousemine"
    is_public: true
    name: MouseMine
    original_source:
      - mgd
    product_url: http://www.mousemine.org/
  - category: GraphicalInterface
    description: Gene Expression Database documenting spatiotemporal gene expression patterns during mouse development and adulthood
    id: "mgd.gxd"
    name: Gene Expression Database (GXD)
    original_source:
      - mgd
    product_url: https://www.informatics.jax.org/expression.shtml
publications:
  - id: "https://doi.org/10.1093/genetics/iyae031"
    title: "Mouse Genome Informatics: an integrated knowledgebase system for the laboratory mouse"
  - id: "https://doi.org/10.1093/nar/gkaa1083"
    title: "Mouse Genome Database (MGD): Knowledgebase for mouse-human comparative biology"
repository: https://github.com/mgijax
synonyms:
  - MGD
  - Mouse Genome Database
  - MGI
  - Mouse Genome Informatics
---

# Mouse Genome Database

## Overview

The Mouse Genome Database (MGD) is the international database resource for the laboratory mouse, providing integrated genetic, genomic, and biological data to facilitate the study of human health and disease through mouse models. Part of the Mouse Genome Informatics consortium at The Jackson Laboratory.

## Information Resource ID

This resource has the Information Resource identifier: `infores:mgi`
