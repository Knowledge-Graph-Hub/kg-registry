---
activity_status: active
category: Resource
contacts:
- category: Individual
  label: Pablo Cingolani
  contact_details:
  - contact_type: github
    value: pcingola
  - contact_type: url
    value: http://www.linkedin.com/in/pablocingolani
creation_date: '2025-10-31T00:00:00Z'
description: SnpEff is a genetic variant annotation and functional effect prediction toolbox widely used in genomics pipelines. It annotates and predicts the effects of genetic variants on genes and proteins (such as amino acid changes), supports over 38,000 genomes, uses standardized Sequence Ontology terms, and implements the VCF annotation standard ANN field. SnpEff is bundled with SnpSift, a companion tool for filtering and manipulating genomic annotated variants. Both tools are integrated with Galaxy and GATK, making them essential components of sequencing data analysis workflows.
domains:
- biomedical
- genomics
- precision medicine
- biological systems
homepage_url: https://pcingola.github.io/SnpEff/
id: snpeff
infores_id: snpeff
last_modified_date: '2025-10-31T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/licenses/MIT
  label: MIT
name: SnpEff
products:
- category: ProgrammingInterface
  description: SnpEff core package with command-line interface for variant annotation and effect prediction
  id: snpeff.download
  name: SnpEff Download Package
  original_source:
  - snpeff
  product_url: https://snpeff.odsp.astrazeneca.com/versions/snpEff_latest_core.zip
- category: GraphicalInterface
  description: Comprehensive documentation website for SnpEff with usage examples, tutorials, and command references
  format: http
  id: snpeff.documentation
  name: SnpEff Documentation
  original_source:
  - snpeff
  product_url: https://pcingola.github.io/SnpEff/snpeff/introduction/
- category: GraphicalInterface
  description: SnpSift documentation covering tools for filtering, annotating, and manipulating VCF files
  format: http
  id: snpsift.documentation
  name: SnpSift Documentation
  original_source:
  - snpeff
  product_url: https://pcingola.github.io/SnpEff/snpsift/introduction/
- category: Product
  description: Over 38,000 pre-built genome databases available for automatic download and annotation
  id: snpeff.databases
  name: SnpEff Genome Databases
  original_source:
  - snpeff
  product_url: https://pcingola.github.io/SnpEff/download/
  warnings:
  - Databases are automatically downloaded when running SnpEff; manual download is optional
- category: ProgrammingInterface
  description: SnpEff source code repository on GitHub
  id: snpeff.github
  name: SnpEff GitHub Repository
  original_source:
  - snpeff
  product_url: https://github.com/pcingola/SnpEff
- category: Product
  description: Historical releases and versions of SnpEff available on SourceForge
  id: snpeff.sourceforge
  name: SnpEff SourceForge Archive
  original_source:
  - snpeff
  product_url: https://sourceforge.net/projects/snpeff/files/
publications:
- authors:
  - Cingolani P
  - Platts A
  - Wang le L
  - Coon M
  - Nguyen T
  - Wang L
  - Land SJ
  - Lu X
  - Ruden DM
  id: https://pubmed.ncbi.nlm.nih.gov/22728672/
  journal: Fly
  preferred: true
  title: 'A program for annotating and predicting the effects of single nucleotide polymorphisms, SnpEff: SNPs in the genome of Drosophila melanogaster strain w1118; iso-2; iso-3'
  year: '2012'
- authors:
  - Cingolani P
  - Patel VM
  - Coon M
  - Nguyen T
  - Land SJ
  - Ruden DM
  - Lu X
  journal: Frontiers in Genetics
  id: https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2012.00035/full
  title: 'Using Drosophila melanogaster as a model for genotoxic chemical mutational studies with a new program, SnpSift'
  year: '2012'
repository: https://github.com/pcingola/SnpEff
---

# SnpEff - Genetic Variant Annotation and Effect Prediction

## Overview

SnpEff is a widely-used open-source tool for annotating and predicting the functional effects of genetic variants. It analyzes how genetic variations affect genes, transcripts, and proteins, making it an essential component of genomics and precision medicine workflows. SnpEff is bundled with SnpSift, a complementary toolset for filtering and manipulating annotated variants.

### Current Version

**Latest version: 5.3** (released 2025-09-02)

### Key Features

1. **Comprehensive Genome Support**
   - Over 38,000 genome databases available
   - Automatic download and installation of genomic databases
   - Support for human, model organisms, plants, bacteria, and viruses
   - Multiple versions of human genomes (GRCh37, GRCh38, etc.)

2. **Standardized Annotations**
   - **VCF ANN field**: Implements standard VCF annotation format
   - **Sequence Ontology terms**: Uses SO standardized vocabulary for variant effects
   - **HGVS notation**: Human Genome Variation Society nomenclature
   - **GATK compatibility**: Native support for GATK pipelines (`-o gatk`)

3. **Variant Effect Prediction**
   - Predicts effects on genes and proteins
   - Amino acid changes
   - Nonsense and missense mutations
   - Frameshift variants
   - Splice site impacts
   - Start/stop codon effects
   - Upstream/downstream gene region effects

4. **Cancer Variant Analysis**
   - Specialized cancer sample analysis
   - Somatic mutation annotation
   - Integration with cancer databases

5. **Integration with Major Platforms**
   - **Galaxy**: Full integration with Galaxy workflows
   - **GATK**: Compatible with Broad Institute's Genome Analysis Toolkit
   - **Nextflow**: Used in Nextflow genomics pipelines
   - **Common Workflow Language (CWL)**: Available as CWL tools

## SnpSift - Companion Toolset

SnpSift is bundled with SnpEff and provides extensive capabilities for working with annotated VCF files:

### Core SnpSift Tools

- **Filter**: Filter VCF files using complex expressions
- **Annotate**: Add annotations from databases (dbSNP, ClinVar, etc.)
- **AnnotateMem**: Memory-efficient annotation for large databases
- **CaseControl**: Case-control analysis and statistics
- **Extract Fields**: Extract specific fields from VCF files
- **Join**: Combine multiple VCF files
- **Intervals**: Intersect with genomic intervals
- **TsTv**: Calculate transition/transversion ratios
- **Variant Type**: Classify variant types
- **GWAS Catalog**: Annotate with GWAS Catalog data
- **dbNSFP**: Annotate with dbNSFP database (functional predictions)
- **PhastCons**: Add conservation scores
- **Split**: Split multi-sample VCF files
- **Concordance**: Compare VCF files for concordance
- **GeneSets**: Gene set enrichment analysis

## Installation and Requirements

### System Requirements

- **Java**: Version 1.11 or later required
- **Memory**: At least 4GB recommended for large genomes (e.g., human)
- **Operating Systems**: Cross-platform (Linux, macOS, Windows)

### Installation

SnpEff installation is straightforward:

```bash
# Download latest version
wget https://snpeff.odsp.astrazeneca.com/versions/snpEff_latest_core.zip

# Unzip
unzip snpEff_latest_core.zip

# Run SnpEff
java -jar snpEff.jar [options] genome_version input.vcf > output.vcf
```

### Database Installation

Databases are automatically downloaded when first used:

```bash
# List available databases
java -jar snpEff.jar databases

# Pre-download a specific database (optional)
java -jar snpEff.jar download GRCh38.76
```

## Usage

### Basic Annotation

```bash
# Annotate variants (database downloaded automatically if needed)
java -jar snpEff.jar GRCh38.76 input.vcf > annotated.vcf

# With summary HTML report
java -jar snpEff.jar -v -stats summary.html GRCh38.76 input.vcf > annotated.vcf

# GATK-compatible output
java -jar snpEff.jar -o gatk GRCh38.76 input.vcf > annotated.vcf
```

### SnpSift Examples

```bash
# Filter variants
cat annotated.vcf | java -jar SnpSift.jar filter "(ANN[*].IMPACT = 'HIGH')" > high_impact.vcf

# Extract fields
cat annotated.vcf | java -jar SnpSift.jar extractFields - CHROM POS REF ALT "ANN[*].GENE" "ANN[*].EFFECT" > variants.txt

# Annotate with dbSNP
java -jar SnpSift.jar annotate dbsnp.vcf input.vcf > annotated_dbsnp.vcf
```

## Output Formats

### ANN Field Format

SnpEff adds annotations to the VCF ANN (Annotation) field with the following structure:

```
Allele | Annotation | Annotation_Impact | Gene_Name | Gene_ID | Feature_Type | Feature_ID | Transcript_BioType | Rank | HGVS.c | HGVS.p | cDNA.pos / cDNA.length | CDS.pos / CDS.length | AA.pos / AA.length | Distance | ERRORS / WARNINGS / INFO
```

### Summary Statistics

SnpEff generates HTML summary reports including:
- Variant statistics by type
- Effects by impact (HIGH, MODERATE, LOW, MODIFIER)
- Effects by functional class
- Count by effect type
- Count by genomic region
- Base changes analysis
- Ts/Tv ratios

## Use Cases

1. **Clinical Genomics**
   - Variant interpretation for rare diseases
   - Pharmacogenomics analysis
   - Cancer genomics and precision oncology

2. **Research Applications**
   - Population genomics studies
   - GWAS follow-up analysis
   - Evolutionary genomics
   - Functional genomics

3. **Quality Control**
   - Variant calling pipeline validation
   - Sequencing quality assessment
   - Transition/transversion ratio analysis

4. **Data Integration**
   - Combining annotations from multiple sources
   - Integration with clinical databases (ClinVar, COSMIC)
   - Linking to pathway and gene ontology databases

## Integration Capabilities

### Galaxy Integration

SnpEff is fully integrated with the Galaxy platform:
- Available as Galaxy tools
- Compatible with Galaxy workflows
- Supports Galaxy data formats

### GATK Integration

Native support for GATK pipelines:
- GATK-compatible VCF output format
- Integration with Broad's best practices
- Compatible with GATK variant calling workflows

### Other Integrations

- **Nextflow pipelines**: nf-core/sarek and other workflows
- **WDL workflows**: Cromwell-compatible
- **Snakemake**: Used in Snakemake pipelines
- **Docker/Singularity**: Containerized versions available

## Building Custom Databases

SnpEff supports building custom genome databases from:
- GTF/GFF annotation files
- GenBank files
- RefSeq annotations
- Regulatory elements
- Non-coding features
- PDB and AlphaFold structure data

## License

SnpEff and SnpSift are released under the **MIT License**, making them free for both academic and commercial use.

## Development

### Source Code

- **GitHub Repository**: https://github.com/pcingola/SnpEff
- **Language**: Java
- **Build Tools**: Maven, ANT
- **Dependencies**: BioJava, ANTLR

### Contributing

The project welcomes contributions:
- Bug reports and feature requests via GitHub Issues
- Pull requests for improvements
- Documentation contributions

## Citation

**SnpEff**:
Cingolani P, Platts A, Wang le L, Coon M, Nguyen T, Wang L, Land SJ, Lu X, Ruden DM. *A program for annotating and predicting the effects of single nucleotide polymorphisms, SnpEff: SNPs in the genome of Drosophila melanogaster strain w1118; iso-2; iso-3.* **Fly** (Austin). 2012 Apr-Jun;6(2):80-92. PMID: 22728672

**SnpSift**:
Cingolani P, Patel VM, Coon M, Nguyen T, Land SJ, Ruden DM, Lu X. *Using Drosophila melanogaster as a model for genotoxic chemical mutational studies with a new program, SnpSift.* **Frontiers in Genetics**, 3, 2012.

## In Memory

The SnpEff project honors the memory of **Dr. Xiangyi Lu**, a co-author on both the SnpEff and SnpSift papers, who passed away from ovarian cancer in 2017. Users are encouraged to consider donations to the Xiangyi Lu Graduate Student Fellowship in Bioinformatics Fund at Wayne State University.

## Community and Support

- **Documentation**: https://pcingola.github.io/SnpEff/
- **Help and Bugs**: GitHub Issues
- **Download**: https://snpeff.odsp.astrazeneca.com/versions/snpEff_latest_core.zip
- **Mailing List**: Via GitHub Discussions
- **Examples**: Extensive examples available in documentation

## Related Resources

SnpEff is commonly used alongside:
- **GATK**: Variant calling
- **bcftools**: VCF manipulation
- **VEP**: Alternative variant annotation (Ensembl)
- **ANNOVAR**: Alternative variant annotation
- **ClinVar**: Clinical variant interpretation
- **dbNSFP**: Functional prediction scores
