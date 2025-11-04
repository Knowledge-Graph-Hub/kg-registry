---
activity_status: inactive
category: DataSource
creation_date: '2025-11-04T00:00:00Z'
description: HomoloGene was NCBI's database of homologs (genes with common ancestry) from completely sequenced eukaryotic genomes. The database organized genes into homology groups representing putative orthologs and paralogs across multiple species. HomoloGene was retired in January 2024 and replaced by the NCBI Orthologs dataset, which is now accessible through NCBI Datasets and the Gene database. The last HomoloGene build (build 68) was produced in 2014 and is no longer aligned with current data in NCBI RefSeq and Gene. Historical data from build 68 remains available on FTP for archival purposes only.
domains:
  - biological systems
  - genomics
id: "homologene"
infores_id: "homologene"
last_modified_date: '2025-11-04T00:00:00Z'
layout: resource_detail
name: HomoloGene
homepage_url: https://www.ncbi.nlm.nih.gov/homologene
contacts:
  - category: Organization
    label: NCBI Help Desk
    contact_details:
      - contact_type: email
        value: "info@ncbi.nlm.nih.gov"
products:
  - id: "homologene.data"
    category: Product
    name: HomoloGene Data File (Build 68 - Archive)
    description: Tab-delimited file containing HomoloGene group IDs, taxonomy IDs, gene IDs, gene symbols, and protein accessions for the final build 68 (2014)
    product_url: https://ftp.ncbi.nih.gov/pub/HomoloGene/build68/homologene.data
    format: tsv
    original_source:
      - homologene
  - id: "homologene.xml"
    category: Product
    name: HomoloGene XML Data (Build 68 - Archive)
    description: XML dump of the HomoloGene build 68 containing detailed homology group information, gene and protein links, and distance analysis results
    product_url: https://ftp.ncbi.nih.gov/pub/HomoloGene/build68/homologene.xml.gz
    format: xml
    compression: gzip
    original_source:
      - homologene
  - id: "homologene.ftp_archive"
    category: DocumentationProduct
    name: HomoloGene FTP Archive
    description: Complete FTP archive of all HomoloGene builds from build 35 (2004) through build 68 (2014), retained for historical purposes
    product_url: https://ftp.ncbi.nih.gov/pub/HomoloGene/
    format: http
    original_source:
      - homologene
warnings:
  - HomoloGene was officially retired in January 2024
  - The last build (build 68) is from 2014 and is not aligned with current NCBI RefSeq and Gene data
---

# HomoloGene

## Overview

HomoloGene was NCBI's system for automatically detecting homologs (genes with common ancestry) among the annotated genes of completely sequenced eukaryotic genomes. The database organized genes into homology groups representing putative orthologs (genes in different species that evolved from a common ancestral gene) and paralogs (genes related by duplication within a genome).

## Retirement Notice

**HomoloGene was officially retired in January 2024.** The website has been redirected to the NCBI Orthologs site, which provides updated ortholog information through NCBI Datasets and the Gene database. The last HomoloGene build (build 68) was produced in 2014 and is significantly outdated compared to current genomic annotations.

## Replacement Resource

Users should now use the **NCBI Orthologs** dataset, which provides:
- Updated ortholog annotations aligned with current RefSeq and Gene data
- Access through NCBI Datasets API and web interface
- Integration with NCBI Gene pages
- More comprehensive species coverage

For more information, see:
- [HomoloGene retirement announcement](https://ncbiinsights.ncbi.nlm.nih.gov/2024/01/30/homologene-redirects-ncbi-datasets-gene/)
- [NCBI Datasets Gene page](https://www.ncbi.nlm.nih.gov/datasets/gene/)

## Historical Data Content

HomoloGene build 68 (2014) contained:
- Homology groups for 20 eukaryotic species
- Putative orthologs and paralogs
- Protein alignments and similarity scores
- Gene and protein cross-references
- Distance analysis results

## Data Files (Archive Only)

Historical HomoloGene data files from build 68 include:
- **homologene.data**: Tab-delimited file with HID, taxonomy ID, gene ID, gene symbol, protein GI, and protein accession
- **homologene.xml.gz**: Gzipped XML file with complete homology group information
- **build_inputs/**: Supporting files including protein sequences and taxonomic information

## Information Resource ID

This resource has the Information Resource identifier: `infores:homologene`

## Important Notes

- **This resource is RETIRED and should not be used for current research**
- Historical data is retained for archival and reproducibility purposes
- Data is from 2014 and does not reflect current gene annotations
- For current ortholog information, use NCBI Orthologs via NCBI Datasets or Gene
