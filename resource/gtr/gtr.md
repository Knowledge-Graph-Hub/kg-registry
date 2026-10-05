---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.ncbi.nlm.nih.gov/gtr/docs/about/
  id: ncbi
  label: National Center for Biotechnology Information (NCBI)
creation_date: '2026-10-04T00:00:00Z'
description: The NIH Genetic Testing Registry (GTR) is NCBI's central database of
  genetic test information submitted voluntarily by test providers. Each test record
  covers the test's purpose, methods, analytical and clinical validity, the laboratory
  offering it, and the conditions and genes it targets. Conditions are identified
  by MedGen concept IDs with OMIM and SNOMED CT cross-references, and genes by NCBI
  Gene IDs. NIH does not independently verify submitted information.
domains:
- genomics
- clinical
- biomedical
homepage_url: https://www.ncbi.nlm.nih.gov/gtr/
id: gtr
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/home/about/policies/
  label: Public Domain (U.S. Government work; NCBI and NLM Data Usage Policies)
name: Genetic Testing Registry
products:
- category: GraphicalInterface
  description: Web portal for searching genetic tests, laboratories, conditions and
    genes registered in GTR.
  format: http
  id: gtr.portal
  name: GTR Web Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtr
  product_url: https://www.ncbi.nlm.nih.gov/gtr/
- category: Product
  compression: gzip
  description: Comprehensive XML extraction of all publicly available tests registered
    in GTR, validated by the GTRPublicData.xsd schema in the documentation directory.
    A copy is archived at the end of each month in the xml_archive subdirectory.
  format: xml
  id: gtr.xml
  name: GTR Full XML Extraction
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtr
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/GTR/data/gtr_ftp.xml.gz
- category: Product
  description: Tab-delimited listing of every registered test and the conditions and
    genes it targets, updated daily. Conditions carry MedGen concept IDs, OMIM numbers
    and SNOMED CT IDs where available; genes carry NCBI Gene IDs and symbols.
  format: tsv
  id: gtr.test_condition_gene
  name: GTR Test, Condition and Gene Table
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtr
  - relation_type: prov:hadPrimarySource
    source: medgen
  - relation_type: prov:hadPrimarySource
    source: omim
  - relation_type: prov:hadPrimarySource
    source: snomedct
  - relation_type: prov:hadPrimarySource
    source: ncbigene
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/GTR/data/test_condition_gene.txt
- category: Product
  compression: gzip
  description: Tab-delimited test version history for all publicly available GTR tests,
    with laboratory, location, CLIA number, conditions, methods, platforms, genes and
    status fields for each test version.
  format: tsv
  id: gtr.test_version
  name: GTR Test Version History
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtr
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/GTR/data/test_version.gz
- category: DocumentationProduct
  description: GTR documentation pages describing the registry, its data model and
    submission process.
  format: http
  id: gtr.docs
  name: About GTR
  original_source:
  - relation_type: prov:hadPrimarySource
    source: gtr
  product_url: https://www.ncbi.nlm.nih.gov/gtr/docs/about/
publications:
- authors:
  - Wendy S. Rubinstein
  - Donna R. Maglott
  - Jennifer M. Lee
  - Brandi L. Kattman
  - Adriana J. Malheiro
  - Michael Ovetsky
  - Vichet Hem
  - Viatcheslav Gorelenkov
  - Guangfeng Song
  - Craig Wallin
  - Nora Husain
  - Shanmuga Chitipiralla
  - Kenneth S. Katz
  - Douglas Hoffman
  - Wonhee Jang
  - Mark Johnson
  - Fedor Karmanov
  - Alexander Ukrainchik
  - Mikhail Denisenko
  - Cathy Fomous
  - Kathy Hudson
  - James M. Ostell
  doi: 10.1093/nar/gks1173
  id: doi:10.1093/nar/gks1173
  journal: Nucleic Acids Research
  preferred: true
  title: 'The NIH genetic testing registry: a new, centralized database of genetic
    tests to enable access to comprehensive information and improve transparency'
  year: '2012'
synonyms:
- GTR
- NIH Genetic Testing Registry
- NCBI Genetic Testing Registry
taxon:
- NCBITaxon:9606
---
# Genetic Testing Registry

The NIH Genetic Testing Registry (GTR) is a database of genetic test information submitted by test providers, run by NCBI. It covers clinical and research tests for heritable and somatic conditions, pharmacogenetic responses and some microbial tests.

Each test record names the offering laboratory and describes the test's purpose, methodology, platforms, validity and the conditions and genes it targets. Conditions are identified by MedGen concept unique identifiers, with OMIM and SNOMED CT cross-references where available. Genes are identified by NCBI Gene IDs.

NIH does not independently verify submitted information, and listing a test or laboratory is not an endorsement.

## Data Downloads

The GTR FTP site (`https://ftp.ncbi.nlm.nih.gov/pub/GTR/data/`) provides:

- `gtr_ftp.xml.gz`: full XML extraction of all public tests, with monthly copies in `xml_archive/`.
- `test_condition_gene.txt` (also as `.xlsx`): tests with their target conditions and genes, updated daily.
- `test_version.gz`: test version history with laboratory and method details.
- Summary tables of laboratories by country and tests by method category.

NCBI asks users who redistribute GTR data to link to the GTR website or cite the 2013 NAR paper.
