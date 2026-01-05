---
activity_status: active
category: DataModel
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: "http://www.sequenceontology.org/"
    id: "sequence-ontology"
    label: Sequence Ontology Consortium
creation_date: '2025-09-04T00:00:00Z'
description: GFF (General Feature Format) is a standard file format for describing genomic features including genes, transcripts, exons, and other sequence annotations, widely used in genome annotation and bioinformatics.
domains:
  - genomics
homepage_url: http://www.sequenceontology.org/gff3.shtml
id: "gff"
last_modified_date: '2026-01-05T00:00:00Z'
layout: resource_detail
name: GFF
synonyms:
  - GFF
  - General Feature Format
  - GFF3
products:
  - category: DocumentationProduct
    description: GFF3 specification and documentation from Sequence Ontology
    format: http
    id: "gff.specification"
    is_public: true
    name: GFF3 Specification
    product_url: http://www.sequenceontology.org/gff3.shtml
  - category: OntologyProduct
    description: OWL release of Monochrom Ontology
    format: owl
    id: "chr.model.owl"
    name: Monochrom Ontology OWL release
    original_source:
      - ro
      - go
      - ncbitaxon
      - iao
      - geno
      - skos
      - gff
    product_file_size: 102365
    product_url: https://raw.githubusercontent.com/monarch-initiative/monochrom/refs/heads/master/chr.owl
    secondary_source:
      - chr
---

# GFF (General Feature Format)

## Overview

GFF (General Feature Format) is a standard tab-delimited text file format for describing genomic features. It is widely used in bioinformatics and genome annotation to represent genes, transcripts, exons, regulatory elements, and other sequence features. The format has evolved through several versions, with GFF3 being the current standard maintained by the Sequence Ontology consortium.

## Format Versions

- **GFF1**: Original format (deprecated)
- **GFF2/GTF**: Gene Transfer Format, widely used for gene annotations
- **GFF3**: Current standard with improved structure and semantics

## GFF3 Structure

Each line in a GFF3 file contains 9 tab-separated fields:

1. **seqid**: Chromosome or scaffold identifier
2. **source**: Algorithm or procedure that generated the feature
3. **type**: Feature type (gene, mRNA, exon, CDS, etc.)
4. **start**: Start position (1-based, inclusive)
5. **end**: End position (1-based, inclusive)
6. **score**: Numeric value (or . if not applicable)
7. **strand**: + (forward), - (reverse), or . (not stranded)
8. **phase**: Reading frame for CDS features (0, 1, 2, or .)
9. **attributes**: Semicolon-separated key=value pairs

## Key Features

- **Hierarchical Relationships**: Parent-child relationships via ID and Parent attributes
- **Controlled Vocabulary**: Uses Sequence Ontology terms for feature types
- **Flexible Attributes**: Extensible key-value pairs for metadata
- **Multi-line Features**: Support for features with discontinuous coordinates
- **Comments and Directives**: Special lines for metadata and file structure

## Common Feature Types

### Gene Structure
- **gene**: Gene loci
- **mRNA**: Messenger RNA transcripts
- **exon**: Exonic regions
- **CDS**: Coding sequence
- **UTR**: Untranslated regions (five_prime_UTR, three_prime_UTR)
- **intron**: Intronic regions

### Non-coding Features
- **ncRNA**: Non-coding RNA genes
- **tRNA**: Transfer RNA
- **rRNA**: Ribosomal RNA
- **miRNA**: MicroRNA
- **lncRNA**: Long non-coding RNA

### Regulatory Elements
- **promoter**: Promoter regions
- **enhancer**: Enhancer elements
- **TF_binding_site**: Transcription factor binding sites

## Applications

### Genome Annotation
- Representing gene models from annotation pipelines
- Storing results from gene prediction algorithms
- Documenting manual curation efforts
- Tracking annotation versions and provenance

### Comparative Genomics
- Comparing gene structures across species
- Identifying orthologous features
- Analyzing synteny and gene order

### Functional Genomics
- Mapping RNA-seq reads to genomic features
- ChIP-seq peak annotation
- Variant effect prediction (relative to annotated features)
- Expression quantification by feature

### Visualization
- Displaying features in genome browsers (IGV, UCSC, JBrowse)
- Creating publication-quality genomic figures
- Interactive exploration of annotations

## Tools and Software

### Parsing and Manipulation
- **BEDOPS**: Convert and manipulate genomic interval formats
- **GenomeTools**: GFF3 validation and manipulation
- **gffutils**: Python library for GFF/GTF files
- **rtracklayer**: R/Bioconductor package for genomic annotations

### Validation
- **GenomeTools gff3validator**: Validates GFF3 syntax and semantics
- **Sequence Ontology tools**: Check feature type compliance

### Conversion
- GTF ↔ GFF3 conversion
- BED format conversion
- GenBank/EMBL format conversion

## Standards and Specifications

- **Maintained by**: Sequence Ontology Consortium
- **Specification**: http://www.sequenceontology.org/gff3.shtml
- **Feature Types**: Based on Sequence Ontology (SO) terms
- **File Extension**: .gff, .gff3

## Best Practices

- Use Sequence Ontology terms for feature types
- Include proper Parent-child relationships for hierarchical features
- Provide unique IDs for all features
- Sort by seqid and start position
- Validate files before distribution
- Document the genome assembly version
- Include ##gff-version pragma

## Integration

GFF files are integrated into:
- Genome browsers (UCSC, Ensembl, NCBI)
- Annotation databases (RefSeq, Gencode, FlyBase)
- Analysis pipelines (variant annotation, RNA-seq)
- Knowledge graphs (linking genomic features to biological entities)

For more information and specifications, visit http://www.sequenceontology.org/gff3.shtml
