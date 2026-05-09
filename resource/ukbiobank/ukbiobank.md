---
activity_status: active
category: DataSource
description: UK Biobank is a large-scale biomedical database and research resource containing genetic, lifestyle and health information from half a million UK participants, designed to improve the prevention, diagnosis and treatment of a wide range of serious and life-threatening illnesses.
domains:
  - biomedical
  - genomics
  - health
  - clinical
  - phenotype
homepage_url: https://www.ukbiobank.ac.uk/
id: ukbiobank
layout: resource_detail
license:
  id: https://www.ukbiobank.ac.uk/terms-and-conditions/
  label: UK Biobank Data Access Agreement
name: UK Biobank
products:
  - category: GraphicalInterface
    description: The UK Biobank Data Showcase provides summary statistics of all UK Biobank data and allows researchers to identify variables for inclusion in research applications.
    format: http
    id: ukbiobank.showcase
    name: UK Biobank Data Showcase
    product_url: https://biobank.ndph.ox.ac.uk/showcase/
  - category: GraphProduct
    description: DisGeNET data, including gene to disease associations and variant to disease associations (requires registration and subscription).
    id: disgenet.data
    name: DisGeNET Data
    original_source:
      - source: clingen
        relation_type: prov:hadPrimarySource
      - source: clinvar
        relation_type: prov:hadPrimarySource
      - source: mgd
        relation_type: prov:hadPrimarySource
      - source: rgd
        relation_type: prov:hadPrimarySource
      - source: orphanet
        relation_type: prov:hadPrimarySource
      - source: psygenet
        relation_type: prov:hadPrimarySource
      - source: uniprot
        relation_type: prov:hadPrimarySource
      - source: disgenet
        relation_type: prov:hadPrimarySource
      - source: hp
        relation_type: prov:hadPrimarySource
      - source: gwascatalog
        relation_type: prov:hadPrimarySource
      - source: phewascat
        relation_type: prov:hadPrimarySource
      - source: ukbiobank
        relation_type: prov:hadPrimarySource
      - source: finngen
        relation_type: prov:hadPrimarySource
      - source: clinicaltrialsgov
        relation_type: prov:hadPrimarySource
    product_url: https://www.disgenet.com/
    secondary_source:
      - source: disgenet
        relation_type: prov:wasInfluencedBy
  - category: GraphProduct
    description: Integrated graph knowledge base combining Mendelian randomization causal estimates, pathway, QTL, drug, literature-derived, and ontology-backed relationships (Neo4j backend)
    format: neo4j
    id: epigraphdb.graph
    name: EpiGraphDB Graph Database
    original_source:
      - source: epigraphdb
        relation_type: prov:hadPrimarySource
      - source: kg-monarch
        relation_type: prov:hadPrimarySource
      - source: vectology
        relation_type: prov:hadPrimarySource
      - source: ukbiobank
        relation_type: prov:hadPrimarySource
      - source: prsatlas
        relation_type: prov:hadPrimarySource
      - source: eqtlgen
        relation_type: prov:hadPrimarySource
      - source: mondo
        relation_type: prov:hadPrimarySource
      - source: gtex
        relation_type: prov:hadPrimarySource
      - source: ensembl
        relation_type: prov:hadPrimarySource
      - source: cpic
        relation_type: prov:hadPrimarySource
      - source: opentargets
        relation_type: prov:hadPrimarySource
      - source: efo
        relation_type: prov:hadPrimarySource
      - source: semmeddb
        relation_type: prov:hadPrimarySource
      - source: intact
        relation_type: prov:hadPrimarySource
      - source: string
        relation_type: prov:hadPrimarySource
      - source: reactome
        relation_type: prov:hadPrimarySource
      - source: mrbase
        relation_type: prov:hadPrimarySource
    product_url: https://docs.epigraphdb.org/graph-database/
    secondary_source:
      - source: epigraphdb
        relation_type: prov:wasInfluencedBy
publications:
  - authors:
      - Clare Bycroft
      - Colin Freeman
      - Desislava Petkova
      - Gavin Band
      - Lloyd T. Elliott
      - Kevin Sharp
      - Allan Motyer
      - Damjan Vukcevic
      - Olivier Delaneau
      - Jared O'Connell
      - Adrian Cortes
      - Samantha Welsh
      - Alan Young
      - Mark Effingham
      - Gil McVean
      - Stephen Leslie
      - Naomi Allen
      - Peter Donnelly
      - Jonathan Marchini
    doi: 10.1038/s41586-018-0579-z
    id: doi:10.1038/s41586-018-0579-z
    journal: Nature
    title: The UK Biobank resource with deep phenotyping and genomic data
    year: '2018'
  - authors:
      - Cathie Sudlow
      - John Gallacher
      - Naomi Allen
      - Valerie Beral
      - Paul Burton
      - John Danesh
      - Paul Downey
      - Paul Elliott
      - Jane Green
      - Martin Landray
      - Bette Liu
      - Paul Matthews
      - Giok Ong
      - Jill Pell
      - Alan Silman
      - Alan Young
      - Tim Sprosen
      - Tim Peakman
      - Rory Collins
    doi: 10.1371/journal.pmed.1001779
    id: doi:10.1371/journal.pmed.1001779
    journal: PLOS Medicine
    title: 'UK Biobank: An Open Access Resource for Identifying the Causes of a Wide Range of Complex Diseases of Middle and Old Age'
    year: '2015'
taxon:
  - NCBITaxon:9606
creation_date: '2025-06-27T00:00:00Z'
last_modified_date: '2025-12-13T00:00:00Z'
---

# UK Biobank

UK Biobank is a large-scale biomedical database and research resource, containing in-depth genetic and health information from half a million UK participants. The database is regularly augmented with additional data and is globally accessible to approved researchers undertaking vital research into the most common and life-threatening diseases.

## Overview

UK Biobank recruited 500,000 people aged between 40-69 years in 2006-2010 from across the UK. With their consent, they provided detailed information about their lifestyle, physical measures, and had blood, urine and saliva samples collected and stored for future analysis. UK Biobank's database is a major contributor to the advancement of modern medicine and treatment and has enabled several scientific discoveries that improve human health.

## Data Resources

UK Biobank contains an unprecedented wealth of biological data, including:

- **Genotyping data** for all 500,000 participants
- **Whole exome sequencing** data for 200,000 participants
- **Whole genome sequencing** data for 200,000 participants
- **Health-related outcomes** via linkage to electronic health records
- **Imaging data** (brain, heart, body) for 100,000 participants
- **Extensive phenotype data** including physical measurements, biomarkers, and questionnaire data

## Access Model

UK Biobank is not an open access resource - researchers must apply for access and their institutions must sign a Material Transfer Agreement. However, it is designed to be widely accessible to bona fide researchers for health-related research that is in the public interest. The application process includes:

1. Registration with UK Biobank
2. Submission of a research application
3. Payment of access fees (which vary depending on the institution type)
4. Approval by UK Biobank's Access Committee

## Impact on Knowledge Graphs

While UK Biobank data itself is not openly available as downloadable products, it has been utilized in the creation of numerous derived knowledge graphs and resources. It serves as a critical source for:

- Genotype-phenotype association studies
- Risk prediction models
- Biomarker discovery
- Drug target validation
- Clinical decision support systems

## Related Resources

UK Biobank data has been used by numerous projects that have then made their derivative analyses publicly available, including:

- PheWAS (Phenome-Wide Association Studies) catalogs
- GWAS (Genome-Wide Association Studies) summaries
- Polygenic risk scores
- Various disease prediction models

## More Information

For more detailed information about UK Biobank, visit:
- [UK Biobank Website](https://www.ukbiobank.ac.uk/)
- [Data Showcase](https://biobank.ndph.ox.ac.uk/showcase/)
- [Access Application Process](https://www.ukbiobank.ac.uk/enable-your-research/apply-for-access)
