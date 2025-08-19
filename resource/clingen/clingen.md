---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: support@clinicalgenome.org
  - contact_type: url
    value: https://clinicalgenome.org/about/contact-clingen/
  label: ClinGen
description: The Clinical Genome Resource (ClinGen) is a National Institutes of Health
  (NIH)-funded resource dedicated to building a central resource that defines the
  clinical relevance of genes and variants for use in precision medicine and research.
  ClinGen brings together clinical and research experts to develop standard approaches
  for interpreting genomic variants, curate evidence for gene-disease relationships,
  and share this knowledge through freely accessible databases.
domains:
- genomics
- biomedical
- clinical
- health
homepage_url: https://clinicalgenome.org/
id: clingen
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: ClinGen
products:
- category: DataProduct
  description: ClinGen Gene-Disease Validity curations assess the strength of evidence
    supporting or refuting a gene's role in a given disease. These curations classify
    evidence as Definitive, Strong, Moderate, Limited, No Reported Evidence, or Disputed.
  format: csv
  id: clingen.gene-disease
  name: Gene-Disease Validity Curations
  product_url: https://search.clinicalgenome.org/kb/gene-validity
- category: DataProduct
  description: ClinGen Dosage Sensitivity curations evaluate whether genes and genomic
    regions are sensitive to copy number variation. These curations determine if haploinsufficiency
    (loss of one copy) or triplosensitivity (gain of one copy) of a gene/region causes
    disease.
  format: tsv
  id: clingen.dosage
  name: Dosage Sensitivity Curations
  product_url: https://search.clinicalgenome.org/kb/gene-dosage
- category: DataProduct
  description: ClinGen Clinical Actionability evaluations assess the clinical actions
    available to manage risk for patients with specific genetic disorders. These curations
    score the actionability of gene-disease pairs based on severity, likelihood of
    disease, efficacy of interventions, and knowledge base.
  format: tsv
  id: clingen.actionability
  name: Clinical Actionability Curations
  product_url: https://search.clinicalgenome.org/kb/actionability
- category: DataProduct
  description: ClinGen Variant Pathogenicity curations assess the clinical significance
    of genetic variants based on ACMG/AMP guidelines. Expert panels classify variants
    as Pathogenic, Likely Pathogenic, Uncertain Significance, Likely Benign, or Benign.
  format: csv
  id: clingen.variant
  name: Variant Pathogenicity Curations
  product_url: https://search.clinicalgenome.org/kb/variant-pathogenicity/all
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-14: Timeout connecting
    to URL'
- category: ProgrammingInterface
  description: REST API providing access to ClinGen's Evidence Repository for variant
    pathogenicity assessments. Allows programmatic retrieval of structured evidence
    used to evaluate the clinical significance of genetic variants.
  id: clingen.evrepo.api
  name: ClinGen Evidence Repository API
  product_url: https://erepo.clinicalgenome.org/evrepo/api/
- category: GraphicalInterface
  description: Web-based interface for accessing ClinGen's curated data. Allows users
    to search and browse curated gene-disease pairs, variant interpretations, and
    other ClinGen resources.
  id: clingen.web.interface
  name: ClinGen Search Interface
  product_url: https://search.clinicalgenome.org/
- category: ProcessProduct
  description: Framework for standardized interpretation of genetic variants, including
    disease-specific modifications to the ACMG/AMP guidelines. These frameworks guide
    variant classification by expert panels and clinical laboratories.
  id: clingen.variant.frameworks
  name: Variant Interpretation Frameworks
  product_url: https://www.clinicalgenome.org/working-groups/sequence-variant-interpretation/
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
- category: GraphProduct
  description: KGX Distribution of KG-Monarch
  format: kgx
  id: kg-monarch.graph
  name: KGX Distribution of KG-Monarch
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  product_file_size: 230877741
  product_url: http://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.tar.gz
  secondary_source:
  - kg-monarch
- category: GraphProduct
  description: KGX JSON-Lines Distribution of KG-Monarch
  format: kgx-jsonl
  id: kg-monarch.graph.jsonl
  name: KGX JSON-L Distribution of KG-Monarch
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.jsonl.tar.gz
  secondary_source:
  - kg-monarch
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-14: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-19: HTTP 404 error
    when accessing file'
- category: GraphProduct
  description: RDF Distribution of KG-Monarch
  format: rdfxml
  id: kg-monarch.graph.rdf
  name: RDF Distribution of KG-Monarch
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  product_file_size: 879238775
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.nt.gz
  secondary_source:
  - kg-monarch
- category: GraphProduct
  description: Neo4j Dump of KG-Monarch
  dump_format: neo4j
  id: kg-monarch.graph.neo4j
  name: Neo4j Dump of KG-Monarch
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.neo4j.dump
  secondary_source:
  - kg-monarch
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-14: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-19: HTTP 404 error
    when accessing file'
- category: GraphProduct
  description: DuckDB database of KG-Monarch
  id: kg-monarch.graph.duckdb
  name: DuckDB database of KG-Monarch
  original_source:
  - phenio
  - alliance
  - bgee
  - biogrid
  - clingen
  - clinvar
  - ctd
  - dictybase
  - go
  - hp
  - maxo
  - panther
  - pombase
  - reactome
  - string
  - xenbase
  - zfin
  product_url: https://data.monarchinitiative.org/monarch-kg/latest/monarch-kg.duckdb.gz
  secondary_source:
  - kg-monarch
  warnings:
  - 'File was not able to be retrieved when checked on 2025-08-14: HTTP 404 error
    when accessing file'
  - 'File was not able to be retrieved when checked on 2025-08-19: HTTP 404 error
    when accessing file'
publications:
- authors:
  - Rehm HL
  - Berg JS
  - Brooks LD
  - Bustamante CD
  - Evans JP
  - Landrum MJ
  - Ledbetter DH
  - et al.
  doi: doi:10.1056/NEJMsr1406261
  id: https://doi.org/10.1056/NEJMsr1406261
  journal: New England Journal of Medicine
  preferred: true
  title: ClinGen — The Clinical Genome Resource
  year: '2015'
- authors:
  - ClinGen Consortium
  doi: doi:10.1016/j.gim.2024.101228
  id: https://doi.org/10.1016/j.gim.2024.101228
  journal: Genetics in Medicine
  title: 'The Clinical Genome Resource (ClinGen): Advancing genomic knowledge through
    global curation'
  year: '2024'
---
# ClinGen - Clinical Genome Resource

## Overview

The Clinical Genome Resource (ClinGen) is a National Institutes of Health (NIH)-funded resource dedicated to building a central database that defines the clinical relevance of genes and variants for use in precision medicine and research. Founded in 2013, ClinGen is a collaborative effort involving more than 2,700 contributors from over 72 countries who work to curate and standardize information about genomic variants and their relationship to human health.

ClinGen serves as a critical bridge between genomic research and clinical application, enabling better interpretation of genetic testing results and improving patient care through enhanced variant classification. The resource addresses the challenge of interpreting the vast amount of genomic data being generated by modern sequencing technologies.

## Mission and Activities

ClinGen's primary goal is to improve patient care by ensuring that clinicians, researchers, and patients have access to reliable genomic information. The resource achieves this through several key curation activities:

- **Gene-Disease Validity**: Evaluating the strength of evidence supporting relationships between genes and diseases. Gene Curation Expert Panels (GCEPs) classify evidence for gene-disease relationships as Definitive, Strong, Moderate, Limited, No Reported Evidence, or Disputed.
  
- **Variant Pathogenicity**: Assessing whether specific genetic variants cause disease. Variant Curation Expert Panels (VCEPs) apply the ACMG/AMP guidelines to classify variants as Pathogenic, Likely Pathogenic, Uncertain Significance, Likely Benign, or Benign.
  
- **Dosage Sensitivity**: Determining if changes in gene copy number (deletions or duplications) result in disease. The Dosage Sensitivity Working Group evaluates whether gains or losses of specific genomic regions lead to clinical phenotypes.
  
- **Clinical Actionability**: Evaluating medical interventions available for individuals with genetic conditions. The Actionability Working Group assesses what clinical interventions are available for patients with specific genetic disorders and scores their actionability.
  
- **Somatic Cancer Variant Interpretation**: Curating the clinical significance of genomic alterations in cancer. The Somatic Cancer Working Group applies specialized frameworks to classify cancer-related variants.

## Expert Panels

ClinGen coordinates numerous Expert Panels composed of international experts who evaluate evidence and generate consensus interpretations of genomic variants. As of 2025, there are over 60 active Variant Curation Expert Panels (VCEPs) and Gene Curation Expert Panels (GCEPs) focusing on specific diseases or genes including:

- Hereditary cancer syndromes (BRCA1/2, TP53, PTEN, etc.)
- Cardiovascular disorders (cardiomyopathies, arrhythmias)
- Neurodevelopmental disorders
- Inborn errors of metabolism
- Kidney disorders
- Hearing loss
- RASopathies
- Hereditary eye disorders

These panels follow standardized frameworks to ensure consistency across interpretations and periodically review their classifications as new evidence emerges.

## Data Sharing and Access

All curated content from ClinGen is freely available to the scientific and medical communities under a CC0 1.0 Universal license. The data can be accessed through:

1. The ClinGen website and search interfaces at [clinicalgenome.org](https://clinicalgenome.org/)
2. Downloadable files in various formats (CSV, TSV, BED) from the [ClinGen Downloads page](https://search.clinicalgenome.org/kb/downloads)
3. RESTful APIs for programmatic access, including the Evidence Repository API
4. Integration with other resources like ClinVar, NCBI's database of genomic variation
5. Variant curation interfaces that allow expert panels to submit evidence-based classifications

ClinGen also partners with patient registries and data sharing platforms like GenomeConnect to enhance the collection of phenotypic information associated with genetic variants.

## Impact on Clinical Practice

ClinGen resources are widely used in clinical genomics, serving as an authoritative source for variant interpretation in genetic testing. In 2018, the FDA recognized ClinGen as the first FDA-designated public genetic variant database, allowing test developers to use ClinGen's variant classifications as clinical validity support for genetic tests without the need for additional FDA review.

The resource has significantly improved standardization in variant interpretation across laboratories through:

- Development and refinement of the ACMG/AMP variant interpretation guidelines
- Creation of disease-specific modifications to these guidelines
- Providing a framework for resolving differences in variant interpretation between laboratories
- Supporting clinical decision-making for healthcare providers managing patients with genetic conditions

ClinGen has also established formal partnerships with other genomic resources including ClinVar, CPIC (Clinical Pharmacogenetics Implementation Consortium), PharmGKB, and international genomic medicine initiatives to enhance the global standardization of genomic information.

## Community Curation and Education

ClinGen supports community involvement through:

- The ClinGen Community Curation (C3) program that enables researchers, clinicians, and trainees to contribute to gene and variant curation
- Educational resources and training materials for variant interpretation
- Regular webinars and workshops for the genomic medicine community
- Support for implementation of genomic medicine in diverse healthcare settings

Through these efforts, ClinGen is driving the advancement of precision medicine by creating a standardized, centralized resource for clinically relevant genomic knowledge.