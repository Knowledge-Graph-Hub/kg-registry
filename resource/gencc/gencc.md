---
activity_status: active
category: DataSource
contacts:
  - category: Organization
    label: GenCC Team
    contact_details:
      - contact_type: email
        value: "gencc@thegencc.org"
      - contact_type: url
        value: "https://thegencc.org/"
creation_date: '2025-11-08T00:00:00Z'
description: The Gene Curation Coalition (GenCC) is a global collaborative effort to harmonize gene-disease validity curation across multiple expert organizations and clinical testing laboratories. GenCC brings together leading resources including ClinGen, OMIM, Orphanet, DECIPHER, Genomics England PanelApp, and multiple clinical diagnostic laboratories to standardize terminology and share gene-disease validity assertions publicly. The coalition was formed in 2018 to address the lack of universal standards and terminologies for defining gene-disease relationships used in genomic medicine and research. Through a modified Delphi survey involving the international genetics community, GenCC established consensus terminology for grading gene-disease validity, including standardized terms such as Definitive, Strong, Moderate, Limited, Disputed Evidence, Refuted Evidence, No Known Disease Relationship, and Animal Model Only. The GenCC database provides curated gene-disease validity assertions with a focus on monogenic Mendelian diseases, including information on mode of inheritance, classification confidence level, supporting evidence, and links to detailed curations from member organizations.
domains:
- genomics
id: "gencc"
infores_id: "gencc"
last_modified_date: '2025-11-08T00:00:00Z'
layout: resource_detail
name: The Gene Curation Coalition (GenCC)
homepage_url: https://thegencc.org/
products:
  - category: Product
    description: The GenCC database containing over 15,000 curated gene-disease validity assertions on 4,500+ unique genes from 12 international submitters, with standardized classifications and evidence links
    format: http
    id: "gencc.database"
    name: GenCC Database
    product_url: https://search.thegencc.org/
  - category: GraphicalInterface
    description: Interactive web-based search and browse interface at search.thegencc.org allowing users to filter gene-disease assertions by gene symbol, disease, submitter, and validity classification
    format: http
    id: "gencc.search_interface"
    name: GenCC Search Interface
    product_url: https://search.thegencc.org/
  - category: Product
    description: Freely available downloadable datasets in multiple formats (XLSX, XLS, TSV, CSV) containing all GenCC gene-disease assertions with comprehensive metadata under CC0 1.0 Public Domain Dedication
    format: http
    id: "gencc.downloads"
    name: GenCC Data Downloads
    product_url: https://search.thegencc.org/download
publications:
  - authors:
      - Marina T. DiStefano
      - Scott Goehringer
      - Heidi L. Rehm
    doi: "10.1016/j.gim.2022.04.017"
    id: "doi:10.1016/j.gim.2022.04.017"
    journal: Genetics in Medicine
    preferred: true
    title: 'The Gene Curation Coalition: A global effort to harmonize gene–disease evidence resources'
    year: "2022"
taxon:
  - NCBITaxon:9606
---

# The Gene Curation Coalition (GenCC)

## Overview

The Gene Curation Coalition (GenCC) is a groundbreaking international consortium formed to standardize and harmonize gene-disease validity curation across the genetics community. Established in February 2018 during a joint meeting of the Transforming Genetic Medicine Initiative and ClinGen at the Wellcome Trust in London, GenCC addresses a critical need in genomic medicine: the lack of consistent terminology and shared standards for evaluating gene-disease relationships.

## Mission and Impact

With the increasing use of exome and genome sequencing in clinical practice, confidence in gene-disease associations has become more critical than ever. Unless a gene is convincingly linked to a disease, the pathogenicity of variants cannot be accurately interpreted. GenCC tackles this challenge by bringing together organizations engaged in gene-disease validity evaluation with a commitment to publicly share their curations, develop consistent terminology, and facilitate uniform assessment of genes reported in association with disease.

## Information Resource ID

This resource has the Information Resource identifier: `infores:gencc`

## Member Organizations

GenCC comprises 17 leading organizations including public gene-level resources and diagnostic laboratories committed to sharing their internally curated gene-level knowledge:

- **ClinGen** (Clinical Genome Resource) - NIH-funded resource for clinical gene/variant relevance
- **OMIM** (Online Mendelian Inheritance in Man) - Comprehensive human genes and genetic phenotypes compendium
- **Orphanet** - Knowledge base on rare diseases spanning 38 countries
- **DECIPHER** - Database of genomic variation and phenotype using Ensembl resources
- **Genomics England PanelApp** - Crowdsourced expert gene panel curation
- **PanelApp Australia** - Australian consensus virtual gene panels
- **HGNC** (HUGO Gene Nomenclature Committee) - Worldwide authority for human gene nomenclature
- **G2P** (gene2phenotype) - Evidence-based datasets for diagnostic variant filtering
- **PharmGKB** - Pharmacogenomics knowledge base
- **Broad Center for Mendelian Genomics** - GREGoR Consortium member
- **Franklin by Genoox** - AI-based genomic interpretation engine
- **Ambry Genetics** - CLIA-certified clinical testing laboratory
- **Invitae** - CLIA-certified clinical testing laboratory
- **Illumina Clinical Services Laboratory** - TruGenome Undiagnosed Disease Test
- **Laboratory for Molecular Medicine** (Mass General Brigham) - Harvard-affiliated molecular diagnostic laboratory
- **Myriad Women's Health** - CLIA-certified genetic screening laboratory
- **King Faisal Specialist Hospital and Research Center** - Developmental genetics

## The GenCC Database

Launched in December 2020, the GenCC database serves as the gene-level equivalent of ClinVar, but for gene-disease assertions rather than variant-disease assertions. The database provides:

- **15,000+ gene-disease assertions** on over 4,500 unique genes (as of December 2021)
- **Standardized validity classifications**: Definitive, Strong, Moderate, Limited, Disputed Evidence, Refuted Evidence, No Known Disease Relationship, Animal Model Only, and Supportive
- **Harmonized disease ontologies**: Using MONDO, OMIM, and Orphanet identifiers
- **Mode of inheritance information**: Using Human Phenotype Ontology (HPO) terms
- **Evidence links**: Direct links to detailed curations from submitting organizations
- **Global usage**: 36,000+ page views from 4,000+ users across 120+ countries in 2021

## Data Access and Integration

All GenCC data are freely available under a CC0 1.0 Universal Public Domain Dedication through:
- **Interactive search interface** at search.thegencc.org with filtering by gene, disease, and submitter
- **Multiple download formats**: XLSX, XLS, TSV, CSV
- **API access** (planned for expanded functionality)
- **Integration** with DECIPHER, UCSC Genome Browser, ClinGen, and HGNC resources

## Standardization and Harmonization

GenCC achieved consensus terminology through a three-round modified Delphi survey involving 241 responses from the international genetics community, including major professional societies (ESHG, ASHG, ACGS, BSGM). The resulting standardized terms enable consistent interpretation of gene-disease validity across clinical and research settings, reducing discrepancies that previously ranged from 5-13% across different resources.

## Discrepancy Resolution

GenCC actively facilitates resolution of gene-disease validity conflicts through monthly steering committee meetings and engagement with ClinGen Gene Curation Expert Panels. This collaborative approach improves consistency in genetic testing and variant interpretation globally.

## Support and Funding

GenCC is supported by the National Human Genome Research Institute (U24HG006834), Wellcome Trust, Medical Research Council (UK), British Heart Foundation, NIHR, Australian Genomics (NHMRC), and contributions from member organizations. The steering committee includes representatives from all member organizations and meets monthly to set standards and ensure the coalition meets its goals.

# The Gene Curation Coalition (GenCC)

## Overview

The GenCC DB provides information pertaining to the validity of gene-disease relationships, with a current focus on Mendelian diseases

**Note:** This is a stub entry that was automatically created from the [Translator Information Resource Registry](https://biolink.github.io/information-resource-registry/). It requires manual curation to add complete metadata, products, and additional information.

## Information Resource ID

This resource has the Information Resource identifier: `infores:gencc`

## Curation Status

- **Stub**: Yes - needs manual curation
- **Creation Date**: 2025-10-30
- **Original Source**: Translator Information Resource Registry

## What Needs to be Curated

1. **Activity Status**: Verify if this resource is active, inactive, or deprecated
2. **Category**: Confirm the resource category is correct
3. **Description**: Expand and improve the description
4. **Homepage URL**: Verify and update if needed
5. **Products**: Add specific data products/files/APIs offered by this resource
6. **Contacts**: Add contact information
7. **Publications**: Add relevant publications
8. **Domains**: Add relevant domain tags
9. **Repository**: Add code repository if applicable

## Additional Notes
