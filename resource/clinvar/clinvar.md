---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: clinvar@ncbi.nlm.nih.gov
  label: ClinVar Team, National Center for Biotechnology Information (NCBI)
description: ClinVar is a freely accessible, public archive of reports of human genetic
  variations and their relationships to human health. It collects and presents data
  on variants found in patient samples, classifications for diseases and drug responses,
  and supporting evidence. ClinVar enables access to and communication about the clinical
  significance of genetic variants, providing healthcare professionals, researchers,
  and the public with vital information for interpreting genetic test results.
domains:
- biomedical
- genomics
- clinical
- precision medicine
- health
- translational
homepage_url: https://www.ncbi.nlm.nih.gov/clinvar/
id: clinvar
layout: resource_detail
license:
  id: https://www.ncbi.nlm.nih.gov/home/about/policies/
  label: NCBI and NLM Data Usage Policies and Disclaimers
name: ClinVar
products:
- category: Product
  description: Complete public data set in XML format containing comprehensive variant
    information, clinical significance classifications, and supporting evidence.
  format: xml
  id: clinvar.xml
  name: ClinVar XML
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/clinvar/xml/
- category: Product
  description: ClinVar data in VCF format for GRCh37 human genome assembly, containing
    variant information and clinical significance.
  format: vcf
  id: clinvar.vcf.grch37
  name: ClinVar VCF (GRCh37)
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/
- category: Product
  description: ClinVar data in VCF format for GRCh38 human genome assembly, containing
    variant information and clinical significance.
  format: vcf
  id: clinvar.vcf.grch38
  name: ClinVar VCF (GRCh38)
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/
- category: Product
  description: Tab-delimited files summarizing variant data, gene-condition relationships,
    and other aspects of ClinVar data.
  format: tsv
  id: clinvar.tab
  name: ClinVar Tab-Delimited Files
  product_url: https://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/
- category: ProgrammingInterface
  description: API access to ClinVar data through NCBI's E-utilities, supporting programmatic
    queries and data retrieval.
  format: http
  id: clinvar.api
  name: ClinVar API (E-utilities)
  product_url: https://www.ncbi.nlm.nih.gov/clinvar/docs/maintenance_use/
- category: GraphicalInterface
  description: Web interface for searching and browsing ClinVar data, with detailed
    variant information and evidence.
  format: http
  id: clinvar.web
  name: ClinVar Web Interface
  product_url: https://www.ncbi.nlm.nih.gov/clinvar/
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
  - do
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
  - cmap
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
  - nposckan
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
  - do
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
  - cmap
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
  - nposckan
  - disgenet
  - biomarker
  - opentargets
  product_url: https://ubkg-downloads.xconsortia.org/
  secondary_source:
  - ubkg
- category: GraphProduct
  description: DisGeNET data, including gene to disease associations and variant to
    disease associations (requires registration and subscription).
  id: disgenet.data
  name: DisGeNET Data
  original_source:
  - clingen
  - clinvar
  - mgd
  - rgd
  - orphanet
  - psygenet
  - uniprot
  - disgenet
  - hp
  - gwascat
  - phewascat
  - ukbiobank
  - finngen
  - clinicaltrialsgov
  product_url: https://www.disgenet.com/
  secondary_source:
  - disgenet
publications:
- authors:
  - Landrum MJ
  - Chitipiralla S
  - Kaur K
  - Brown G
  - Chen C
  - Hart J
  - Hoffman D
  - Jang W
  - Liu C
  - Maddipatla Z
  - Maiti R
  - Mitchell J
  - Rezaie T
  - Riley G
  - Song G
  - Yang J
  - Ziyabari L
  - Russette A
  - Kattman BL
  doi: 10.1093/nar/gkae1090
  id: doi:10.1093/nar/gkae1090
  journal: Nucleic Acids Research
  preferred: true
  title: 'ClinVar: updates to support classifications of both germline and somatic
    variants'
  year: '2024'
- authors:
  - Landrum MJ
  - Lee JM
  - Benson M
  - Brown GR
  - Chao C
  - Chitipiralla S
  - Gu B
  - Hart J
  - Hoffman D
  - Jang W
  - Karapetyan K
  - Katz K
  - Liu C
  - Maddipatla Z
  - Malheiro A
  - McDaniel K
  - Ovetsky M
  - Riley G
  - Zhou G
  - Holmes JB
  - Kattman BL
  - Maglott DR
  doi: 10.1093/nar/gkx1153
  id: doi:10.1093/nar/gkx1153
  journal: Nucleic Acids Research
  title: ClinVar - improving access to variant interpretations and supporting evidence
  year: '2018'
---
# ClinVar

ClinVar is a freely accessible, public archive maintained by the National Center for Biotechnology Information (NCBI) that catalogs the relationships between human genetic variations and phenotypes, with supporting evidence. It serves as a critical resource for the clinical genetics community by providing a centralized repository of variant interpretations and their clinical significance.

## Overview

ClinVar collects, curates, and distributes information about:
- Human genomic variations (from single nucleotide variants to large structural variants)
- Clinical significance classifications (pathogenic, likely pathogenic, uncertain significance, likely benign, benign)
- Supporting evidence for classifications
- Relationships between variants and diseases or drug responses
- Submitter information and review status

The database integrates submissions from clinical testing laboratories, research groups, expert panels, and professional societies, making it a comprehensive resource for variant interpretation in clinical settings.

## Content

ClinVar contains data on variants across the entire human genome, including:

- **Variant classifications**: Clinical significance determinations from submitters
- **Variant details**: HGVS expressions, genomic locations, allele identifiers
- **Condition information**: Medical conditions associated with variants, mapped to MedGen
- **Evidence details**: Supporting evidence for classifications, including case data, functional studies, and population frequencies
- **Submitter information**: Source of variant classifications and contact details
- **Review status**: Level of expert review for each classification, from no assertion criteria to practice guideline
- **Version history**: Previous versions of submitted records and changes over time

ClinVar accepts submissions for variants identified through various methods, including clinical testing, research, and literature curation. It does not include GWAS data or variants observed but not classified.

## Data Access

ClinVar data is available through multiple channels:

1. **Web Interface**: Interactive search and browsing, with detailed variant pages
2. **API Access**: Programmatic access via NCBI's E-utilities for integration into bioinformatics workflows
3. **Data Downloads**: Full and partial data dumps in multiple formats:
   - XML files containing the complete dataset
   - VCF files for GRCh37 and GRCh38 assemblies
   - Tab-delimited summary files of variants, gene-disease relationships, and more

The data is updated weekly on the website, with comprehensive monthly releases available for download on the first Thursday of each month.

## Integration and Collaboration

ClinVar works closely with the ClinGen project and other initiatives to improve the quality and interpretation of genomic variants. It provides data exchange mechanisms with numerous resources, including:

- NCBI resources (Gene, MedGen, dbSNP, dbVar)
- External databases (OMIM, GTR, Variation Viewer)
- Professional organization guidelines and expert panel evaluations

As a vital component of the clinical genomics ecosystem, ClinVar continuously evolves to meet the needs of the genetics community and support the implementation of precision medicine.