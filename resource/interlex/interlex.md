---
activity_status: active
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://www.fdilab.org/
  label: FAIR Data Informatics Lab, University of California, San Diego
- category: Individual
  contact_details:
  - contact_type: email
    value: mmartone@ucsd.edu
  - contact_type: github
    value: memartone
  label: Maryann E. Martone
  orcid: 0000-0002-8406-3871
creation_date: '2026-10-27T00:00:00Z'
description: InterLex is a dynamic lexicon of biomedical terms maintained by SciCrunch
  and the FAIR Data Informatics Lab at UC San Diego. It was built on NeuroLex, the
  neuroscience lexicon of the Neuroscience Information Framework, and contains all
  NeuroLex terms, extended to other biomedical domains. Terms are modeled with OWL
  primitives and carry stable ILX identifiers; users can contribute, annotate, and
  fork terms into their own namespaces, and InterLex maps data fields and values to
  common data elements and existing terminologies to support data integration. InterLex
  identifiers and NeuroLex cross-references appear in resources such as the Foundational
  Model of Anatomy and the NIF Standard ontologies.
domains:
- neuroscience
- biomedical
- metadata
- information technology
fairsharing_id: FAIRsharing.67sssf
homepage_url: https://interlex.org/
id: interlex
last_modified_date: '2026-10-27T00:00:00Z'
layout: resource_detail
name: InterLex
products:
- category: GraphicalInterface
  description: InterLex web dashboard for searching, browsing, and contributing biomedical
    terms (including all former NeuroLex terms) and resolving ILX identifiers.
  format: http
  id: interlex.dashboard
  name: InterLex Dashboard
  original_source:
  - relation_type: prov:hadPrimarySource
    source: interlex
  product_url: https://scicrunch.org/scicrunch/interlex/dashboard
- category: GraphicalInterface
  description: Term pages resolving InterLex ILX identifiers (pattern https://scicrunch.org/scicrunch/interlex/view/ilx_NNNNNNN),
    with labels, definitions, synonyms, superclasses, and mappings.
  format: http
  id: interlex.term-resolver
  name: InterLex Term Resolver
  original_source:
  - relation_type: prov:hadPrimarySource
    source: interlex
  product_url: https://scicrunch.org/scicrunch/interlex/view/ilx_0101963
- category: OntologyProduct
  description: Foundational Model of Anatomy Ontology in OWL format
  format: owl
  id: fma.owl
  latest_version: 5.1.0
  name: fma.owl
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fma
  product_file_size: 208047132
  product_url: http://purl.obolibrary.org/obo/fma.owl
  secondary_source:
  - relation_type: prov:wasInfluencedBy
    source: radlex
  - relation_type: prov:wasInfluencedBy
    source: interlex
  - relation_type: prov:wasDerivedFrom
    source: terminologia-anatomica
  warnings: []
publications:
- authors:
  - Stephen D. Larson
  - Maryann E. Martone
  doi: 10.3389/fninf.2013.00018
  id: doi:10.3389/fninf.2013.00018
  journal: Frontiers in Neuroinformatics
  preferred: true
  title: 'NeuroLex.org: an online framework for neuroscience knowledge'
  year: '2013'
rrid: SCR_016178
synonyms:
- NeuroLex
- ILX
---
# InterLex

## Overview

InterLex is a dynamic lexicon of biomedical terms from SciCrunch and the FAIR Data Informatics Lab at UC San Diego. It grew out of NeuroLex, the Neuroscience Information Framework's neuroscience lexicon, and holds all of its terms. Terms are modeled with OWL primitives and carry ILX identifiers. Users can add and annotate terms or fork them into their own namespaces; terms for the same concept under the same superclass keep the same identifier fragment.

## Access

- InterLex dashboard on SciCrunch for search, browsing, and contribution.
- Term pages that resolve ILX identifiers (CURIE prefix `ILX`/`interlex`).

The SciCrunch pages may block scripted requests, but they are live in a browser.

## Citation

Larson SD, Martone ME. NeuroLex.org: an online framework for neuroscience knowledge. Front Neuroinform. 2013;7:18. doi:10.3389/fninf.2013.00018