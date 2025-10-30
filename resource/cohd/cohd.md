---
activity_status: unknown
category: OntologyResource
creation_date: '2025-10-30T00:00:00Z'
description: "The Columbia Open Health Data (COHD) API provides access to counts and frequencies (i.e., EHR prevalence) of conditions, procedures, drug exposures, and patient demographics, and the co-occurrence frequencies between them. Count and frequency data were derived from the [Columbia University Medical Center''s](http://www.cumc.columbia.edu/) [OHDSI](https://www.ohdsi.org/) database including inpatient and outpatient data. Counts are the number of patients associated with the concept, e.g., diagnosed with a condition, exposed to a drug, or who had a procedure. Frequencies are the number of unique patients associated with the concept divided by the total number of patients in the dataset, i.e., prevalence in the electronic health records. To protect patient privacy, all concepts and pairs of concepts where the count <= 10 were excluded, and counts were randomized by the Poisson distribution.           Four datasets are available:  1) 5-year non-hierarchical dataset: Includes clinical data from 2013-2017   2) lifetime non-hierarchical dataset: Includes clinical data from all dates   3) 5-year hierarchical dataset: Counts for each concept include patients from descendant concepts. Includes clinical data from 2013-2017. 4) BETA! Temporal co-occurrence data  In the 5-year hierarchical data set, the counts for each concept include the patients from all descendant concepts. For example, the count for ibuprofen (ID 1177480) includes patients with Ibuprofen 600 MG Oral Tablet
  (ID 19019073 patients), Ibuprofen 400 MG Oral Tablet (ID 19019072), Ibuprofen 20 MG/ML Oral Suspension (ID 19019050), etc.   While the lifetime dataset captures a larger patient population and range of concepts, the 5-year dataset has better underlying data consistency.   Clinical concepts (e.g., conditions, procedures, drugs) are coded by their standard concept ID in the [OMOP Common Data Model](https://github.com/OHDSI/CommonDataModel/wiki). API methods are provided to map to/from other vocabularies supported in OMOP and other ontologies using the EMBL-EBI Ontology Xref Service (OxO).    The following resources are available through this API:    1. Metadata: Metadata on the COHD database, including dataset descriptions, number of concepts, etc.    2. OMOP: Access to the common vocabulary for name and concept identifier mapping   3. Clinical Frequencies: Access to the counts and frequencies of conditions, procedures, and drug exposures, and the associations between them. Frequency was determined as the number of patients with the code(s) / total number of patients.    4. Concept Associations: Inferred associations between concepts using chi-square analysis, ratio between observed to expected frequency, and relative frequency.    A [Python notebook](https://github.com/WengLab-InformaticsResearch/cohd_api/blob/master/notebooks/COHD_API_Example.ipynb) demonstrates simple examples of how to use the COHD API.   COHD was developed at the [Columbia University Department of Biomedical
  Informatics](https://www.dbmi.columbia.edu/) as a collaboration between the [Weng Lab](http://people.dbmi.columbia.edu/~chw7007/), [Tatonetti Lab](http://tatonettilab.org/), and the [NCATS Biomedical Data Translator](https://ncats.nih.gov/translator) program (Red Team). This work was supported in part by grants: NCATS OT3TR002027, NLM R01LM009886-08A1, and NIGMS R01GM107145.  The following external resources may be useful:   [OHDSI](https://www.ohdsi.org/)   [OMOP Common Data Model](https://github.com/OHDSI/CommonDataModel/wiki)   [Athena](http://athena.ohdsi.org) (OMOP vocabularies, search, concept relationships, concept hierarchy)   [Atlas](http://www.ohdsi.org/web/atlas/) (OMOP vocabularies, search, concept relationships, concept hierarchy, concept sets)"
domains:
  - stub
id: cohd
infores_id: cohd
last_modified_date: '2025-10-30T00:00:00Z'
layout: resource_detail
name: Columbia Open Health Data (COHD)
homepage_url: https://github.com/NCATSTranslator/Translator-All/wiki/COHD-KP
---

# Columbia Open Health Data (COHD)

## Overview

The Columbia Open Health Data (COHD) API provides access to counts and frequencies (i.e., EHR prevalence) of conditions, procedures, drug exposures, and patient demographics, and the co-occurrence frequencies between them. Count and frequency data were derived from the [Columbia University Medical Center''s](http://www.cumc.columbia.edu/) [OHDSI](https://www.ohdsi.org/) database including inpatient and outpatient data. Counts are the number of patients associated with the concept, e.g., diagnosed with a condition, exposed to a drug, or who had a procedure. Frequencies are the number of unique patients associated with the concept divided by the total number of patients in the dataset, i.e., prevalence in the electronic health records. To protect patient privacy, all concepts and pairs of concepts where the count <= 10 were excluded, and counts were randomized by the Poisson distribution.           Four datasets are available:  1) 5-year non-hierarchical dataset: Includes clinical data from 2013-2017   2) lifetime non-hierarchical dataset: Includes clinical data from all dates   3) 5-year hierarchical dataset: Counts for each concept include patients from descendant concepts. Includes clinical data from 2013-2017. 4) BETA! Temporal co-occurrence data  In the 5-year hierarchical data set, the counts for each concept include the patients from all descendant concepts. For example, the count for ibuprofen (ID 1177480) includes patients with Ibuprofen 600 MG Oral Tablet (ID 19019073 patients), Ibuprofen 400 MG Oral Tablet (ID 19019072), Ibuprofen 20 MG/ML Oral Suspension (ID 19019050), etc.   While the lifetime dataset captures a larger patient population and range of concepts, the 5-year dataset has better underlying data consistency.   Clinical concepts (e.g., conditions, procedures, drugs) are coded by their standard concept ID in the [OMOP Common Data Model](https://github.com/OHDSI/CommonDataModel/wiki). API methods are provided to map to/from other vocabularies supported in OMOP and other ontologies using the EMBL-EBI Ontology Xref Service (OxO).    The following resources are available through this API:    1. Metadata: Metadata on the COHD database, including dataset descriptions, number of concepts, etc.    2. OMOP: Access to the common vocabulary for name and concept identifier mapping   3. Clinical Frequencies: Access to the counts and frequencies of conditions, procedures, and drug exposures, and the associations between them. Frequency was determined as the number of patients with the code(s) / total number of patients.    4. Concept Associations: Inferred associations between concepts using chi-square analysis, ratio between observed to expected frequency, and relative frequency.    A [Python notebook](https://github.com/WengLab-InformaticsResearch/cohd_api/blob/master/notebooks/COHD_API_Example.ipynb) demonstrates simple examples of how to use the COHD API.   COHD was developed at the [Columbia University Department of Biomedical Informatics](https://www.dbmi.columbia.edu/) as a collaboration between the [Weng Lab](http://people.dbmi.columbia.edu/~chw7007/), [Tatonetti Lab](http://tatonettilab.org/), and the [NCATS Biomedical Data Translator](https://ncats.nih.gov/translator) program (Red Team). This work was supported in part by grants: NCATS OT3TR002027, NLM R01LM009886-08A1, and NIGMS R01GM107145.  The following external resources may be useful:   [OHDSI](https://www.ohdsi.org/)   [OMOP Common Data Model](https://github.com/OHDSI/CommonDataModel/wiki)   [Athena](http://athena.ohdsi.org) (OMOP vocabularies, search, concept relationships, concept hierarchy)   [Atlas](http://www.ohdsi.org/web/atlas/) (OMOP vocabularies, search, concept relationships, concept hierarchy, concept sets)

**Note:** This is a stub entry that was automatically created from the [Translator Information Resource Registry](https://biolink.github.io/information-resource-registry/). It requires manual curation to add complete metadata, products, and additional information.

## Information Resource ID

This resource has the Information Resource identifier: `infores:cohd`

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
