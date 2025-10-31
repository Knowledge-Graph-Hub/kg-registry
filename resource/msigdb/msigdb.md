---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: genesets@broadinstitute.org
  label: MSigDB Team
creation_date: '2025-10-30T00:00:00Z'
description: The Molecular Signatures Database (MSigDB) is a comprehensive collection
  of tens of thousands of annotated gene sets for use with Gene Set Enrichment Analysis
  (GSEA) software. MSigDB includes curated gene sets from pathway databases, gene
  ontology annotations, hallmark gene sets, immunologic signatures, regulatory target
  sets, and cell type-specific signatures derived from single-cell sequencing studies.
  Available for both human and mouse.
domains:
- genomics
- systems biology
- pathways
homepage_url: https://www.gsea-msigdb.org/gsea/msigdb/
id: msigdb
infores_id: msigdb
last_modified_date: '2025-10-30T00:00:00Z'
layout: resource_detail
license:
  id: https://www.gsea-msigdb.org/gsea/license_terms_list.jsp
  label: GSEA/MSigDB License Terms
name: Molecular Signatures Database
products:
- category: GraphicalInterface
  description: Web interface for browsing, searching, and investigating gene sets
    across all MSigDB collections
  format: http
  id: msigdb.browser
  name: MSigDB Web Browser
  original_source:
  - msigdb
  product_url: https://www.gsea-msigdb.org/gsea/msigdb/
- category: Product
  description: Downloadable gene set files in GMT, XML, and other formats for human
    collections including hallmarks, curated pathways, ontologies, and computational
    signatures
  format: mixed
  id: msigdb.downloads.human
  name: MSigDB Human Gene Sets Downloads
  product_url: https://www.gsea-msigdb.org/gsea/downloads.jsp#msigdb
- category: Product
  description: Downloadable gene set files for mouse collections including mouse-ortholog
    hallmarks, curated pathways, ontologies, and cell type signatures
  format: mixed
  id: msigdb.downloads.mouse
  name: MSigDB Mouse Gene Sets Downloads
  product_url: https://www.gsea-msigdb.org/gsea/downloads.jsp#msigdb
- category: GraphicalInterface
  description: Interactive tool for computing overlaps between user-provided gene
    sets and MSigDB collections
  id: msigdb.investigate
  name: MSigDB Investigate Tool
  original_source:
  - msigdb
  product_url: https://www.gsea-msigdb.org/gsea/msigdb/human/annotate.jsp
- category: GraphicalInterface
  description: Tool for categorizing gene set members by gene families
  id: msigdb.gene_families
  name: MSigDB Gene Families Tool
  original_source:
  - msigdb
  product_url: https://www.gsea-msigdb.org/gsea/msigdb/human/gene_families.jsp
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
publications:
- id: PMID:37653294
  title: Extending support for mouse data in the Molecular Signatures Database (MSigDB).
synonyms:
- MSigDB
---
# Molecular Signatures Database (MSigDB)

## Overview

The Molecular Signatures Database (MSigDB) is a comprehensive resource of tens of thousands of annotated gene sets designed for use with Gene Set Enrichment Analysis (GSEA) software. Developed as a joint project between UC San Diego and the Broad Institute, MSigDB provides systematic gene set collections that enable researchers to interpret genome-wide expression profiles and identify coordinate changes in gene expression.

## Collections

### Human Collections (v2025.1.Hs)

- **Hallmark Gene Sets**: Coherently expressed signatures representing well-defined biological states or processes
- **Curated Gene Sets**: From pathway databases, PubMed publications, and domain experts
- **Regulatory Target Gene Sets**: microRNA seed sequences and transcription factor binding sites
- **Computational Gene Sets**: Mined from large cancer-oriented expression datasets
- **Gene Ontology Gene Sets**: Genes annotated by the same ontology term
- **Oncogenic Signature Gene Sets**: From cancer gene perturbations
- **Immunologic Signature Gene Sets**: Cell states and perturbations in the immune system
- **Cell Type Signature Gene Sets**: Cluster markers from single-cell sequencing studies
- **Positional Gene Sets**: Chromosome cytogenetic band locations

### Mouse Collections (v2025.1.Mm)

- Mouse-ortholog versions of hallmark gene sets
- Curated gene sets from pathways and literature
- Gene ontology annotations
- Immunologic signatures
- Cell type signatures from single-cell studies
- Regulatory target gene sets
- Positional gene sets

## Features

- Browse and search gene sets by name, keyword, or collection
- Examine individual gene set annotations and member genes
- Compute overlaps between custom gene sets and MSigDB collections
- Categorize genes by gene families
- View expression profiles in public compendia
- Integration with NDEx biological network repository
- Download gene sets in multiple formats (GMT, XML, etc.)

## Access

- Free registration required for downloads and web tools
- Used to track usage for funding agency reports
- No charge for academic and non-commercial use

## Use with GSEA

MSigDB gene sets are designed for direct use with GSEA (Gene Set Enrichment Analysis) software to identify whether predefined sets of genes show statistically significant, concordant differences between two biological states.

## Funding

Currently funded by NCI's Informatics Technology for Cancer Research (ITCR) program.

## Community Contributions

MSigDB welcomes suggestions and contributions of new gene sets from the research community.