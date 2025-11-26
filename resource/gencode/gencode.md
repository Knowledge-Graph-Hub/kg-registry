---
activity_status: active
category: DataSource
creation_date: '2025-11-26T00:00:00Z'
description: GENCODE is a comprehensive and high-quality reference annotation of the human and mouse genomes, providing evidence-based gene annotations including protein-coding genes, long non-coding RNAs, small RNAs, pseudogenes, and other genomic features based on manual curation and computational analysis.
domains:
- genomics
id: "gencode"
homepage_url: https://www.gencodegenes.org/
last_modified_date: '2025-11-26T00:00:00Z'
layout: resource_detail
name: GENCODE
synonyms:
  - GENCODE
  - Encyclopedia of genes and gene variants
taxon:
  - NCBITaxon:9606
  - NCBITaxon:10090
products:
  - category: Product
    description: Comprehensive gene annotations for human genome in GTF format
    format: gff
    id: "gencode.human.gtf"
    name: GENCODE Human Annotations GTF
    product_url: https://www.gencodegenes.org/human/
    original_source:
      - gencode
  - category: Product
    description: Comprehensive gene annotations for mouse genome in GTF format
    format: gff
    id: "gencode.mouse.gtf"
    name: GENCODE Mouse Annotations GTF
    product_url: https://www.gencodegenes.org/mouse/
    original_source:
      - gencode
  - category: Product
    description: GENCODE Primary transcript set capturing minimal transcripts at protein coding genes
    format: gff
    id: "gencode.primary"
    name: GENCODE Primary Transcripts
    product_url: https://www.gencodegenes.org/pages/gencode_primary/
    original_source:
      - gencode
  - category: GraphProduct
    description: Turnkey neo4j distributions that deploy fully-indexed, standalone UBKG instances as neo4j graph databases, running in a Docker container. Requires UMLS API key to access.
    dump_format: neo4j
    id: "ubkg.neo4j"
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
    description: Ontology CSV files that can be imported into a neo4j instance to create a UBKG database. Requires UMLS API key to access.
    format: csv
    id: "ubkg.csv"
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
---

# GENCODE

## Overview

GENCODE (Encyclopedia of Genes and Gene Variants) is a scientific project aimed at identifying and classifying all gene features in the human and mouse genomes with high accuracy based on biological evidence. It provides comprehensive, evidence-based annotations that serve as a reference standard for genome interpretation and biomedical research.

## Mission

The goal of the GENCODE project is to identify and classify all gene features in the human and mouse genomes with high accuracy based on biological evidence, and to release these annotations for the benefit of biomedical research and genome interpretation.

## Key Features

- **Comprehensive Annotations**: Protein-coding genes, long non-coding RNAs (lncRNAs), small RNAs, pseudogenes, and other genomic features
- **Evidence-Based**: Combines manual curation with computational analysis
- **Regular Updates**: New releases approximately every 3-4 months
- **High Quality**: Integrates experimental data including Capture Long-read Sequencing
- **Global Core Biodata Resource**: Recognized as essential infrastructure for life sciences research

## Current Releases (September 2025)

- **GENCODE 49**: Human genome annotations
- **GENCODE M38**: Mouse genome annotations

## Annotation Types

### Protein-Coding Genes
- Comprehensive transcript annotations
- Alternative splicing isoforms
- Coding sequence (CDS) definitions
- Translation information

### Non-Coding RNAs
- **Long non-coding RNAs (lncRNAs)**: Significantly expanding through Capture Long-read Sequencing project integration
- **Small RNAs**: miRNAs, snoRNAs, snRNAs
- **Pseudogenes**: Processed and unprocessed pseudogenes

### Special Annotation Sets

- **GENCODE Primary**: Minimal set of transcripts at protein-coding genes
- **Promoter Windows**: First catalog of human promoter windows
- **Ribo-seq ORFs**: Non-canonical human ORFs predicted by ribosome profiling data, including peptidomics and immunopeptidomics integration

## Data Formats

- **GTF/GFF3**: Gene transfer format files
- **FASTA**: Sequence files for transcripts and proteins
- **Metadata**: Gene and transcript metadata

## Applications

- RNA-seq analysis and transcript quantification
- Variant annotation and interpretation
- Comparative genomics
- Functional genomics studies
- Gene expression analysis
- Knowledge graph construction (UBKG)
- Clinical genomics and precision medicine

## Integration

GENCODE annotations are integrated into:
- Ensembl genome browser
- UCSC Genome Browser
- NCBI RefSeq
- UniProt
- UBKG (Unified Biomedical Knowledge Graph)
- GTEx (Genotype-Tissue Expression)
- Various RNA-seq analysis pipelines

## Consortium Members

- EMBL-EBI (European Bioinformatics Institute)
- The Wellcome Sanger Institute
- CRG (Centre for Genomic Regulation, Barcelona)
- UCSC (University of California, Santa Cruz)
- CNIO (Spanish National Cancer Research Centre)
- MIT (Massachusetts Institute of Technology)
- Yale University

## Funding

GENCODE is supported by the National Human Genome Research Institute (NHGRI) of the US National Institutes of Health.

## Access

- **Website**: https://www.gencodegenes.org/
- **FTP Downloads**: Gene annotations, sequences, and metadata
- **Genome Browsers**: Via Ensembl and UCSC
- **Social Media**: @GencodeGenes on Twitter

## Citation

When using GENCODE data, please cite the GENCODE project and relevant publications describing the specific release used.

## License

GENCODE data are freely available for research use. See EMBL-EBI Terms of Use for details.
