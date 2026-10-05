---
activity_status: active
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: pride-support@ebi.ac.uk
  - contact_type: url
    value: https://www.ebi.ac.uk/pride/
  label: EMBL-EBI PRIDE Team
- category: Individual
  contact_details:
  - contact_type: email
    value: yperez@ebi.ac.uk
  - contact_type: github
    value: ypriverol
  label: Yasset Perez-Riverol
  orcid: 0000-0001-6579-6941
creation_date: '2026-10-04T00:00:00Z'
description: The PRIDE Controlled Vocabulary (PRIDE CV, PRIDE ontology) is a controlled
  vocabulary maintained by the EMBL-EBI PRIDE team for annotating mass spectrometry
  proteomics submissions to the PRIDE Archive and related resources, with terms for
  instruments, protocols, sample processing, quantification and dataset descriptors.
  It is developed in OBO format on GitHub, converted to OWL, imports CHMO and EFO, and
  is served in the EBI Ontology Lookup Service under the prefix PRIDE.
domains:
- biomedical
- proteomics
- information technology
- metadata
homepage_url: https://github.com/PRIDE-Utilities/pride-ontology
id: pride-cv
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: PRIDE Controlled Vocabulary
products:
- category: OntologyProduct
  description: PRIDE Controlled Vocabulary in OBO format (about 980 PRIDE terms), the
    source file that is edited directly in the repository.
  format: obo
  id: pride-cv.obo
  latest_version: releases/2026-09-22
  name: pride_cv.obo
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pride-cv
  product_file_size: 224700
  product_url: https://raw.githubusercontent.com/PRIDE-Utilities/pride-ontology/master/pride_cv.obo
  secondary_source:
  - relation_type: prov:used
    source: chmo
  - relation_type: prov:used
    source: efo
- category: OntologyProduct
  description: PRIDE Controlled Vocabulary in OWL format, generated from the OBO file
    with ROBOT; this is the file loaded by the Ontology Lookup Service.
  format: owl
  id: pride-cv.owl
  name: pride_cv.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pride-cv
  product_file_size: 1077959
  product_url: https://raw.githubusercontent.com/PRIDE-Utilities/pride-ontology/master/pride_cv.owl
  secondary_source:
  - relation_type: prov:used
    source: chmo
  - relation_type: prov:used
    source: efo
- category: GraphicalInterface
  description: Ontology Lookup Service (OLS4) page for browsing and searching the PRIDE
    Controlled Vocabulary, including its imported terms.
  format: http
  id: pride-cv.ols
  name: PRIDE CV in OLS
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pride-cv
  product_url: https://www.ebi.ac.uk/ols4/ontologies/pride
- category: ProgrammingInterface
  description: OLS4 REST API endpoint for the PRIDE Controlled Vocabulary, returning
    ontology metadata and links to its terms.
  format: http
  id: pride-cv.ols-api
  name: PRIDE CV OLS API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pride-cv
  product_url: https://www.ebi.ac.uk/ols4/api/ontologies/pride
- category: Product
  description: GitHub repository for the PRIDE ontology, with the OBO and OWL files,
    validation workflows, PRIDE annotation files and contribution guidelines.
  format: http
  id: pride-cv.repository
  name: PRIDE ontology GitHub repository
  original_source:
  - relation_type: prov:hadPrimarySource
    source: pride-cv
  product_url: https://github.com/PRIDE-Utilities/pride-ontology
publications:
- authors:
  - Yasset Perez-Riverol
  - Chakradhar Bandla
  - Deepti J Kundu
  - Selvakumar Kamatchinathan
  - Jingwen Bai
  - Suresh Hewapathirana
  - Nithu Sara John
  - Ananth Prakash
  - Mathias Walzer
  - Shengbo Wang
  - Juan Antonio Vizcaíno
  doi: 10.1093/nar/gkae1011
  id: doi:10.1093/nar/gkae1011
  journal: Nucleic Acids Research
  preferred: true
  title: 'The PRIDE database at 20 years: 2025 update'
  year: '2025'
repository: https://github.com/PRIDE-Utilities/pride-ontology
synonyms:
- PRIDE CV
- PRIDE ontology
- Proteomics Identification Database Ontology
---
# PRIDE Controlled Vocabulary

The PRIDE Controlled Vocabulary (PRIDE CV) provides terms for describing mass spectrometry proteomics data in the [PRIDE Archive](https://www.ebi.ac.uk/pride/) and related EMBL-EBI tools, such as instrument, protocol, sample and dataset descriptors. Term identifiers use the `PRIDE:` prefix (seven-digit local IDs).

The vocabulary is edited as an OBO file (`pride_cv.obo`) in the [PRIDE-Utilities/pride-ontology](https://github.com/PRIDE-Utilities/pride-ontology) repository. Continuous integration validates the OBO file with fastobo-validator, converts it to OWL with ROBOT and runs a ROBOT report. The OWL file imports the Chemical Methods Ontology (CHMO) and the Experimental Factor Ontology (EFO). The release checked on 2026-10-04 was `releases/2026-09-22`, with about 980 PRIDE terms.

PRIDE CV is browsable in the [Ontology Lookup Service](https://www.ebi.ac.uk/ols4/ontologies/pride). It is not an OBO Foundry ontology. Bioregistry's `pride` prefix record covers both the PRIDE database and this ontology.

The ontology is licensed under CC BY 4.0. For questions, contact the PRIDE Helpdesk at pride-support@ebi.ac.uk.
