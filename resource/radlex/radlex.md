---
activity_status: active
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: radlex-feedback@lists.rsna.org
  - contact_type: url
    value: https://radlex.org/
  label: Radiological Society of North America (RSNA)
creation_date: '2026-10-27T00:00:00Z'
description: RadLex is the Radiological Society of North America's comprehensive lexicon
  and ontology of radiology terms, used for reporting, indexing and retrieval of radiology
  information, decision support, data mining, registries, education, and research.
  It covers imaging modalities, procedures and procedure steps, anatomical entities,
  imaging observations and findings, and related properties. Version 4.3 contains
  about 34,000 active classes with 35 relationship slots. RadLex is freely licensed
  for commercial and non-commercial use under the RadLex License Agreement and Terms
  of Use, and is also distributed through NCBO BioPortal and as a FHIR CodeSystem.
domains:
- medical imaging
- clinical
- clinical coding
- biomedical
fairsharing_id: FAIRsharing.shm2f2
homepage_url: https://radlex.org/
id: radlex
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
license:
  id: https://www.rsna.org/uploadedFiles/RSNA/Content/Informatics/RadLex_License_Agreement_and_Terms_of_Use_V2_Final.pdf
  label: RadLex License Agreement and Terms of Use (V2)
name: RadLex
products:
- category: OntologyProduct
  compression: zip
  description: RadLex 4.3 release in OWL format, with punned classes and individuals,
    distributed as a ZIP archive.
  format: owl
  id: radlex.owl
  latest_version: '4.3'
  name: RadLex OWL (with puns)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: radlex
  product_file_size: 4223156
  product_url: https://radlex.org/download/PunRadLex_Owl4.3.zip
- category: OntologyProduct
  description: RadLex terms as a CSV spreadsheet export, with RadLex IDs, preferred
    names, synonyms, definitions, and parent classes.
  format: csv
  id: radlex.csv
  latest_version: '4.3'
  name: RadLex CSV
  original_source:
  - relation_type: prov:hadPrimarySource
    source: radlex
  product_url: https://radlex.org/Files/Radlex.csv
- category: GraphicalInterface
  description: RadLex term browser and search interface on radlex.org.
  format: http
  id: radlex.browser
  name: RadLex Term Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: radlex
  product_url: https://radlex.org/
- category: OntologyProduct
  description: RadLex hosted in NCBO BioPortal for browsing, API access, and annotation.
  format: http
  id: radlex.bioportal
  name: RadLex in BioPortal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: radlex
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  product_url: https://bioportal.bioontology.org/ontologies/RADLEX
- category: GraphicalInterface
  description: RadLex Playbook, a lexicon of radiology orderables and imaging procedure
    step names built on RadLex. The Playbook is now harmonized with LOINC as the LOINC/RSNA
    Radiology Playbook.
  format: http
  id: radlex.playbook
  name: RadLex Playbook
  original_source:
  - relation_type: prov:hadPrimarySource
    source: radlex
  - relation_type: prov:hadPrimarySource
    source: loinc
  product_url: https://playbook.radlex.org/
publications:
- authors:
  - Curtis P. Langlotz
  doi: 10.1148/rg.266065168
  id: doi:10.1148/rg.266065168
  journal: RadioGraphics
  preferred: true
  title: 'RadLex: A New Method for Indexing Online Educational Materials'
  year: '2006'
- authors:
  - Sanjoy Kundu
  - Maxim Itkin
  - Debra A. Gervais
  - Venkataramu N. Krishnamurthy
  - Michael J. Wallace
  - John F. Cardella
  - et al.
  doi: 10.1016/j.jvir.2009.04.031
  id: doi:10.1016/j.jvir.2009.04.031
  journal: Journal of Vascular and Interventional Radiology
  title: 'The IR Radlex Project: an interventional radiology lexicon--a collaborative
    project of the Radiological Society of North America and the Society of Interventional
    Radiology'
  year: '2009'
rrid: SCR_010418
version: '4.3'
---
# RadLex

## Overview

RadLex is the RSNA's lexicon and ontology of radiology terms. It standardizes the names of imaging modalities, procedures, anatomy, findings, and related properties so radiology reports, teaching files, and research data can be indexed and retrieved consistently. Version 4.3 holds about 34,000 active classes.

## Access

- OWL release (with puns) and a CSV export from radlex.org.
- RadLex term browser on radlex.org.
- NCBO BioPortal (ontology acronym RADLEX), WebProtégé, and a FHIR CodeSystem (via HL7 Terminology).
- RadLex Playbook of orderables and procedure step names, harmonized with LOINC as the LOINC/RSNA Radiology Playbook.

Use requires agreeing to the RadLex License Agreement and Terms of Use (V2), which permits free commercial and non-commercial use.

## Citation

Langlotz CP. RadLex: a new method for indexing online educational materials. RadioGraphics. 2006;26(6):1595-1597. doi:10.1148/rg.266065168
