---
activity_status: inactive
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: info@ncbi.nlm.nih.gov
  id: ncbi
  label: NCBI Help Desk
creation_date: '2025-11-04T00:00:00Z'
description: HomoloGene was NCBI's database of homologs (genes with common ancestry)
  from completely sequenced eukaryotic genomes. The database organized genes into
  homology groups representing putative orthologs and paralogs across multiple species.
  HomoloGene was retired in January 2024 and replaced by the NCBI Orthologs dataset,
  which is now accessible through NCBI Datasets and the Gene database. The last HomoloGene
  build (build 68) was produced in 2014 and is no longer aligned with current data
  in NCBI RefSeq and Gene. Historical data from build 68 remains available on FTP
  for archival purposes only.
domains:
- biological systems
- genomics
homepage_url: https://www.ncbi.nlm.nih.gov/homologene
id: homologene
infores_id: homologene
last_modified_date: '2026-04-16T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/home/about/policies/
  label: Public Domain
name: HomoloGene
products:
- category: Product
  description: Tab-delimited file containing HomoloGene group IDs, taxonomy IDs, gene
    IDs, gene symbols, and protein accessions for the final build 68 (2014)
  format: tsv
  id: homologene.data
  name: HomoloGene Data File (Build 68 - Archive)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: homologene
  product_file_size: 13803677
  product_url: https://ftp.ncbi.nih.gov/pub/HomoloGene/build68/homologene.data
- category: Product
  compression: gzip
  description: XML dump of the HomoloGene build 68 containing detailed homology group
    information, gene and protein links, and distance analysis results
  format: xml
  id: homologene.xml
  name: HomoloGene XML Data (Build 68 - Archive)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: homologene
  product_file_size: 175849799
  product_url: https://ftp.ncbi.nih.gov/pub/HomoloGene/build68/homologene.xml.gz
- category: DocumentationProduct
  description: Complete FTP archive of all HomoloGene builds from build 35 (2004)
    through build 68 (2014), retained for historical purposes
  format: http
  id: homologene.ftp_archive
  name: HomoloGene FTP Archive
  original_source:
  - relation_type: prov:hadPrimarySource
    source: homologene
  product_url: https://ftp.ncbi.nih.gov/pub/HomoloGene/
- category: GraphicalInterface
  description: Web-based interface for searching and browsing comprehensive gene-centric
    information integrating data from over 200 sources
  format: http
  id: genecards.web.interface
  name: GeneCards Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: 5srrnadb
  - relation_type: prov:hadPrimarySource
    source: alliance
  - relation_type: prov:hadPrimarySource
    source: alphafold
  - relation_type: prov:hadPrimarySource
    source: aminode
  - relation_type: prov:hadPrimarySource
    source: bgee
  - relation_type: prov:hadPrimarySource
    source: biocyc
  - relation_type: prov:hadPrimarySource
    source: biogps
  - relation_type: prov:hadPrimarySource
    source: biogrid
  - relation_type: prov:hadPrimarySource
    source: bitterdb
  - relation_type: prov:hadPrimarySource
    source: cdd
  - relation_type: prov:hadPrimarySource
    source: chebi
  - relation_type: prov:hadPrimarySource
    source: chembl
  - relation_type: prov:hadPrimarySource
    source: civic
  - relation_type: prov:hadPrimarySource
    source: clinicaltrialsgov
  - relation_type: prov:hadPrimarySource
    source: clinvar
  - relation_type: prov:hadPrimarySource
    source: compartments
  - relation_type: prov:hadPrimarySource
    source: cosmic
  - relation_type: prov:hadPrimarySource
    source: craft
  - relation_type: prov:hadPrimarySource
    source: ctd
  - relation_type: prov:hadPrimarySource
    source: dbsnp
  - relation_type: prov:hadPrimarySource
    source: dbsuper
  - relation_type: prov:hadPrimarySource
    source: dgidb
  - relation_type: prov:hadPrimarySource
    source: dgv
  - relation_type: prov:hadPrimarySource
    source: diseases
  - relation_type: prov:hadPrimarySource
    source: doid
  - relation_type: prov:hadPrimarySource
    source: drugbank
  - relation_type: prov:hadPrimarySource
    source: efo
  - relation_type: prov:hadPrimarySource
    source: ena
  - relation_type: prov:hadPrimarySource
    source: encode
  - relation_type: prov:hadPrimarySource
    source: ensembl
  - relation_type: prov:hadPrimarySource
    source: epd
  - relation_type: prov:hadPrimarySource
    source: fabric
  - relation_type: prov:hadPrimarySource
    source: fantom5
  - relation_type: prov:hadPrimarySource
    source: flybase
  - relation_type: prov:hadPrimarySource
    source: gard
  - relation_type: prov:hadPrimarySource
    source: gencode
  - relation_type: prov:hadPrimarySource
    source: genecards
  - relation_type: prov:hadPrimarySource
    source: geneorganizer
  - relation_type: prov:hadPrimarySource
    source: genomernai
  - relation_type: prov:hadPrimarySource
    source: glyconnect
  - relation_type: prov:hadPrimarySource
    source: glygen
  - relation_type: prov:hadPrimarySource
    source: go
  - relation_type: prov:hadPrimarySource
    source: gtex
  - relation_type: prov:hadPrimarySource
    source: gtopdb
  - relation_type: prov:hadPrimarySource
    source: gtrnadb
  - relation_type: prov:hadPrimarySource
    source: gwascatalog
  - relation_type: prov:hadPrimarySource
    source: hgnc
  - relation_type: prov:hadPrimarySource
    source: hmdb
  - relation_type: prov:hadPrimarySource
    source: homologene
  - relation_type: prov:hadPrimarySource
    source: hp
  - relation_type: prov:hadPrimarySource
    source: hpa
  - relation_type: prov:hadPrimarySource
    source: hprd
  - relation_type: prov:hadPrimarySource
    source: humancyc
  - relation_type: prov:hadPrimarySource
    source: icd10
  - relation_type: prov:hadPrimarySource
    source: icd11
  - relation_type: prov:hadPrimarySource
    source: iid
  - relation_type: prov:hadPrimarySource
    source: imgt
  - relation_type: prov:hadPrimarySource
    source: innatedb
  - relation_type: prov:hadPrimarySource
    source: intact
  - relation_type: prov:hadPrimarySource
    source: interpro
  - relation_type: prov:hadPrimarySource
    source: kg-monarch
  - relation_type: prov:hadPrimarySource
    source: lncbase
  - relation_type: prov:hadPrimarySource
    source: lncbook
  - relation_type: prov:hadPrimarySource
    source: lncipedia
  - relation_type: prov:hadPrimarySource
    source: lncrnadisease
  - relation_type: prov:hadPrimarySource
    source: malacards
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: medlineplus
  - relation_type: prov:hadPrimarySource
    source: mesh
  - relation_type: prov:hadPrimarySource
    source: mgi
  - relation_type: prov:hadPrimarySource
    source: mint
  - relation_type: prov:hadPrimarySource
    source: mirbase
  - relation_type: prov:hadPrimarySource
    source: mirgenedb
  - relation_type: prov:hadPrimarySource
    source: mirtarbase
  - relation_type: prov:hadPrimarySource
    source: modomics
  - relation_type: prov:hadPrimarySource
    source: mondo
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  - relation_type: prov:hadPrimarySource
    source: ncit
  - relation_type: prov:hadPrimarySource
    source: nextprot
  - relation_type: prov:hadPrimarySource
    source: noncode
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: opentargets
  - relation_type: prov:hadPrimarySource
    source: orphanet
  - relation_type: prov:hadPrimarySource
    source: panther
  - relation_type: prov:hadPrimarySource
    source: pathwaycommons
  - relation_type: prov:hadPrimarySource
    source: paxdb
  - relation_type: prov:hadPrimarySource
    source: pdb
  - relation_type: prov:hadPrimarySource
    source: pdbe
  - relation_type: prov:hadPrimarySource
    source: pfam
  - relation_type: prov:hadPrimarySource
    source: pharmgkb
  - relation_type: prov:hadPrimarySource
    source: pid
  - relation_type: prov:hadPrimarySource
    source: pirsf
  - relation_type: prov:hadPrimarySource
    source: prosite
  - relation_type: prov:hadPrimarySource
    source: proteomicsdb
  - relation_type: prov:hadPrimarySource
    source: proteopedia
  - relation_type: prov:hadPrimarySource
    source: pubchem
  - relation_type: prov:hadPrimarySource
    source: pubmed
  - relation_type: prov:hadPrimarySource
    source: pubtator
  - relation_type: prov:hadPrimarySource
    source: reactome
  - relation_type: prov:hadPrimarySource
    source: refseq
  - relation_type: prov:hadPrimarySource
    source: rfam
  - relation_type: prov:hadPrimarySource
    source: rgd
  - relation_type: prov:hadPrimarySource
    source: rnacentral
  - relation_type: prov:hadPrimarySource
    source: scop
  - relation_type: prov:hadPrimarySource
    source: sfld
  - relation_type: prov:hadPrimarySource
    source: sgd
  - relation_type: prov:hadPrimarySource
    source: signor
  - relation_type: prov:hadPrimarySource
    source: silva
  - relation_type: prov:hadPrimarySource
    source: simap
  - relation_type: prov:hadPrimarySource
    source: smart
  - relation_type: prov:hadPrimarySource
    source: snodb
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: snopy
  - relation_type: prov:hadPrimarySource
    source: srpdb
  - relation_type: prov:hadPrimarySource
    source: string
  - relation_type: prov:hadPrimarySource
    source: tair
  - relation_type: prov:hadPrimarySource
    source: tarbase
  - relation_type: prov:hadPrimarySource
    source: tissues
  - relation_type: prov:hadPrimarySource
    source: treefam
  - relation_type: prov:hadPrimarySource
    source: ttd
  - relation_type: prov:hadPrimarySource
    source: ucnebase
  - relation_type: prov:hadPrimarySource
    source: ucsc
  - relation_type: prov:hadPrimarySource
    source: umls
  - relation_type: prov:hadPrimarySource
    source: uniprot
  - relation_type: prov:hadPrimarySource
    source: vista
  - relation_type: prov:hadPrimarySource
    source: wikipathways
  - relation_type: prov:hadPrimarySource
    source: wikipedia
  - relation_type: prov:hadPrimarySource
    source: wormbase
  product_url: https://www.genecards.org/
taxon:
- NCBITaxon:2759
warnings:
- HomoloGene was officially retired in January 2024
- The last build (build 68) is from 2014 and is not aligned with current NCBI RefSeq
  and Gene data
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