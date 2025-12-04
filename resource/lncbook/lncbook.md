---
activity_status: active
category: DataSource
creation_date: '2019-01-05T00:00:00Z'
description: LncBook is a comprehensive database of human long non-coding RNAs (lncRNAs)
  with multi-omics annotations. It accommodates 95,243 lncRNA genes and 323,950 transcripts,
  integrated from multiple resources including GENCODE, RefLnc, CHESS, FANTOM-CAT,
  and BIGTranscriptome, with strict quality control and curation. The database provides
  abundant annotations including conservation features across 40 vertebrates, disease/trait-associated
  variants, DNA methylation profiles, expression profiles across 9 biological contexts,
  lncRNA-encoded small proteins, lncRNA-protein interactions, and lncRNA-miRNA interactions.
domains:
- genomics
- biological systems
homepage_url: https://ngdc.cncb.ac.cn/lncbook/home
id: lncbook
last_modified_date: '2025-10-21T00:00:00Z'
layout: resource_detail
name: LncBook
products:
- category: GraphicalInterface
  description: Main web portal for searching and browsing human long non-coding RNAs
    with multi-omics annotations
  format: http
  id: lncbook.portal
  name: LncBook Portal
  product_url: https://ngdc.cncb.ac.cn/lncbook/home
- category: GraphicalInterface
  description: Browse conservation features of lncRNA genes across 40 vertebrates
  format: http
  id: lncbook.conservation
  name: Conservation Browser
  product_url: https://ngdc.cncb.ac.cn/lncbook/omics/conservation
- category: GraphicalInterface
  description: Browse 959,138 disease/trait-associated variants across lncRNA genes
  format: http
  id: lncbook.variation
  name: Variation Browser
  product_url: https://ngdc.cncb.ac.cn/lncbook/omics/variation
- category: GraphicalInterface
  description: Browse DNA methylation profiles in 16 diseases (14 cancers and 2 neurodevelopmental
    disorders)
  format: http
  id: lncbook.methylation
  name: Methylation Browser
  product_url: https://ngdc.cncb.ac.cn/lncbook/omics/methylation
- category: GraphicalInterface
  description: Browse expression profiles across 9 biological contexts (normal tissue,
    organ development, cell differentiation, etc.)
  format: http
  id: lncbook.expression
  name: Expression Browser
  product_url: https://ngdc.cncb.ac.cn/lncbook/omics/expression
- category: GraphicalInterface
  description: Browse 34,012 small proteins encoded by lncRNAs
  format: http
  id: lncbook.sprotein
  name: Small Protein Browser
  product_url: https://ngdc.cncb.ac.cn/lncbook/omics/sprotein
- category: GraphicalInterface
  description: Browse lncRNA-miRNA and lncRNA-protein interactions (146,092,274 lncRNA-miRNA
    and 772,745 lncRNA-protein interactions)
  format: http
  id: lncbook.interaction
  name: Interaction Browser
  product_url: https://ngdc.cncb.ac.cn/lncbook/omics/interaction
- category: GraphicalInterface
  description: ID conversion tool across 14 resources
  format: http
  id: lncbook.conversion
  name: ID Conversion Tool
  product_url: https://ngdc.cncb.ac.cn/lncbook/tools/conversion
- category: GraphicalInterface
  description: BLAST search tool for sequence similarity
  format: http
  id: lncbook.blast
  name: BLAST Search
  product_url: https://ngdc.cncb.ac.cn/lncbook/tools/blast
- category: GraphicalInterface
  description: Genomic location annotation and classification tool
  format: http
  id: lncbook.classification
  name: Classification Tool
  product_url: https://ngdc.cncb.ac.cn/lncbook/tools/classification
- category: GraphicalInterface
  description: LGC coding potential prediction tool
  format: http
  id: lncbook.lgc
  name: LGC Coding Potential Predictor
  product_url: https://ngdc.cncb.ac.cn/lgc
- category: DocumentationProduct
  description: Comprehensive database statistics and analysis results
  format: http
  id: lncbook.statistics
  name: Statistics Page
  product_url: https://ngdc.cncb.ac.cn/lncbook/statistics
- category: Product
  description: Downloadable data files including gene annotations, expression profiles,
    and multi-omics annotations
  format: http
  id: lncbook.downloads
  name: Downloads
  product_url: https://ngdc.cncb.ac.cn/lncbook/download
  warnings:
  - File was not able to be retrieved when checked on 2025-12-04_ HTTP 404 error when
    accessing file
  - 'File was not able to be retrieved when checked on 2025-12-04: HTTP 404 error
    when accessing file'
- category: GraphicalInterface
  description: Web portal for searching and browsing ncRNA sequences, structures,
    and annotations
  format: http
  id: rnacentral.portal
  name: RNAcentral Portal
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://rnacentral.org/
- category: ProgrammingInterface
  description: REST API for programmatic access to RNAcentral data
  format: http
  id: rnacentral.api
  name: RNAcentral REST API
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://rnacentral.org/api
- category: Product
  description: FTP archive with current and archived release files (sequences and
    annotations)
  format: http
  id: rnacentral.ftp
  name: RNAcentral FTP Archive
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://ftp.ebi.ac.uk/pub/databases/RNAcentral
- category: DataModelProduct
  description: Public PostgreSQL database for direct SQL access to RNAcentral data
  format: postgres
  id: rnacentral.public-db
  name: RNAcentral Public Postgres Database
  original_source:
  - 5srrnadb
  - crd
  - dictybase
  - ena
  - ensembl
  - evlncrnas
  - expressionatlas
  - flybase
  - genecards
  - greengenes
  - gtrnadb
  - hgnc
  - intact
  - lncbase
  - lncbook
  - lncipedia
  - lncrnadb
  - malacards
  - mgnify
  - mirbase
  - mirgenedb
  - modomics
  - noncode
  - pdbe
  - pirbase
  - plncdb
  - pombase
  - rdp
  - rediportal
  - rfam
  - rgd
  - ribocentre
  - ribovision
  - sgd
  - silva
  - snodb
  - snopy
  - snornadatabase
  - srpdb
  - tair
  - tarbase
  - tmrnawebsite
  - zfin
  - zwd
  - rnacentral
  product_url: https://rnacentral.org/help/public-database
publications:
- authors:
  - Zhao Li
  - Lin Liu
  - Changrui Feng
  - Yuxin Qin
  - Jingfa Xiao
  - Zhang Zhang
  - Lina Ma
  id: https://doi.org/10.1093/nar/gkac999
  journal: Nucleic Acids Research
  preferred: true
  title: 'LncBook 2.0: integrating human long non-coding RNAs with multi-omics annotations'
  year: '2023'
- authors:
  - Lina Ma
  - Jingfa Cao
  - Lin Liu
  - Qiuye Du
  - Zhilei Li
  - Dahai Zou
  - Vladimir B. Bajic
  - Zhang Zhang
  id: https://doi.org/10.1093/nar/gky960
  journal: Nucleic Acids Research
  title: 'LncBook: a curated knowledgebase of human long non-coding RNAs'
  year: '2019'
---
# LncBook

LncBook is a comprehensive resource for human long non-coding RNAs (lncRNAs) that
provides high-quality annotations at multiple omics levels. It is maintained by the
National Genomics Data Center (NGDC) at the China National Center for Bioinformation.

## Database Contents

LncBook accommodates a comprehensive, high-quality collection of 95,243 human lncRNA
genes and 323,950 lncRNA transcripts. These lncRNAs are integrated from five major
resources: RefLnc, GENCODE v33, CHESS v2.2, FANTOM-CAT, and BIGTranscriptome. The
database applies strict quality control measures, removing transcripts with redundancy,
background noise, mapping errors, as well as pseudogenes, small RNAs, and miRNA
precursors. Coding potential is estimated using four algorithms (CPC2, LGC, CPAT,
and PLEK), with transcripts identified as lncRNAs by at least three algorithms retained.

## Multi-omics Annotations

LncBook provides comprehensive annotations at different omics levels:

### Evolutionary Conservation
- Conservation features characterized across 40 vertebrates
- 139,306 homologous genes identified for 22,347 human lncRNA genes
- Gene age classification from human-specific to Euteleostomi

### Genome Variation
- 959,138 disease/trait-associated variants
- Variants from COSMIC (confirmed somatic mutations), ClinVar (pathogenic/benign
  variants), and GWAS Catalog
- Associations with 50,165 lncRNA genes

### DNA Methylation
- Profiles across 16 diseases: 14 cancers and 2 neurodevelopmental disorders
- Data from TCGA and GEO
- 19,543 featured lncRNA genes with differential methylation in promoter or body
  regions

### Expression Profiles
- Expression data across 337 biological conditions
- Organized into 9 biological contexts: normal tissue/cell line, organ development,
  preimplantation embryo, cell differentiation, subcellular localization, exosome,
  cancer cell line, virus infection, and circadian rhythm
- 24,157 featured lncRNA genes (specifically/consistently/differentially/dynamically/periodically
  expressed)
- Data from LncExpDB covering gene expression capacity and tissue/cell specificity

### Small Proteins
- 34,012 small proteins encoded by lncRNAs
- Identified from 5,743 lncRNA genes
- Supported by Ribo-seq or mass spectrometry evidence from SmProt

### Molecular Interactions
- 772,745 lncRNA-protein interactions identified for 2,005 lncRNA genes
- Based on 848,077 RNA Binding Protein (RBP) binding sites from ENCODE (150 RBPs
  in HepG2 and K562 cell lines)
- 146,092,274 predicted lncRNA-miRNA interactions
- Predictions from three tools: miRanda, TargetScan, and RNAhybrid

## Tools and Features

LncBook provides several useful tools for lncRNA analysis:

1. **ID Conversion Tool**: Convert identifiers across 14 different resources
2. **BLAST Search**: Sequence similarity search using NCBI BLAST+
3. **Classification Tool**: Annotate genomic locations of lncRNAs
4. **LGC Tool**: Predict coding potential using the LGC algorithm based on feature
   relationships

## Data Organization

The database is gene-centric with user-friendly web interfaces. Each lncRNA gene
has a dedicated web page with nine sections: gene summary, transcript information,
coding potential, conservation, variation, methylation, expression, small protein,
and interaction. The database allows interactive visualization and customized comparisons
across different omics features. All data and figures are freely downloadable.

## Integration with Related Resources

LncBook works in close partnership with:
- **LncExpDB**: Expression database of human long non-coding RNAs
- **LncRNAWiki**: Knowledgebase with literature curation results
- **RNAcentral**: International database of non-coding RNA sequences (LncBook data
  is integrated into RNAcentral)

## Latest Updates

Version 2.1 (September 2024):
- Integrated newly identified lncRNAs from 10 expert databases
- Identified full-length lncRNA transcripts using 94 PacBio long-read RNA sequencing
  datasets
- Expanded from 323,950 to 526,318 lncRNA transcripts
- Note: v2.1 is ongoing and unstable; v2.0 is recommended for analysis

Version 2.0 (June 2022):
- Incorporated 119,722 new transcripts and 9,632 new genes
- Updated gene structure for 21,305 lncRNAs
- Added conservation features across 40 vertebrates
- Integrated small protein annotations
- Expanded expression profiles to 9 biological contexts
- Increased disease types for methylation profiles from 9 to 16
- Enhanced interaction predictions and annotations