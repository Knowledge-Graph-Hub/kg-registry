---
activity_status: active
category: Aggregator
collection:
- translator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://renci.org/
  label: Renaissance Computing Institute (RENCI)
- category: Individual
  contact_details:
  - contact_type: email
    value: gaurav@renci.org
  - contact_type: github
    value: gaurav
  label: Gaurav Vaidya
  orcid: 0000-0003-0587-0454
creation_date: '2026-10-04T00:00:00Z'
description: The Name Resolver (also called Name Lookup or NameRes) is an NCATS Biomedical
  Data Translator Standards and Reference Implementation (SRI) service developed at
  RENCI. It maps free-text names and synonyms to normalized identifiers (CURIEs), with
  labels and Biolink types, and offers autocomplete, bulk lookup and reverse lookup
  of the synonyms known for a CURIE. Its index is built from the Babel synonym files,
  and all returned identifiers are normalized consistently with the SRI Node Normalizer,
  with GeneProtein and DrugChemical conflation applied.
domains:
- biomedical
- information technology
homepage_url: https://name-resolution-sri.renci.org/docs
id: name-resolver
infores_id: sri-name-resolver
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://opensource.org/license/mit/
  label: MIT
name: SRI Name Resolver
products:
- category: ProgrammingInterface
  connection_url: https://name-resolution-sri.renci.org/
  description: RENCI-hosted Name Resolver REST API (version 1.7.0 when checked) with
    lookup, autocomplete, bulk-lookup, synonyms and reverse_lookup endpoints for mapping
    biomedical concept names to normalized CURIEs, documented with an OpenAPI/Swagger
    page.
  format: http
  id: name-resolver.api
  is_public: true
  name: Name Resolver API (RENCI)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: name-resolver
  product_url: https://name-resolution-sri.renci.org/docs
- category: ProgrammingInterface
  connection_url: https://name-lookup.transltr.io/
  description: NCATS Translator production deployment of the Name Resolver REST API
    (version 1.4.5 when checked), offering the same lookup, synonyms and reverse lookup
    endpoints for Translator tools and user interfaces.
  format: http
  id: name-resolver.translator-api
  is_public: true
  name: Name Resolver API (Translator production)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: name-resolver
  product_url: https://name-lookup.transltr.io/docs
- category: ProcessProduct
  description: Python source code for the Name Resolver service, including the FastAPI
    application, Solr data-loading scripts for Babel synonym files, Docker deployment
    files and tests, released under the MIT license.
  format: http
  id: name-resolver.code
  is_public: true
  license:
    id: https://opensource.org/license/mit/
    label: MIT
  name: Name Resolver Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: name-resolver
  product_url: https://github.com/NCATSTranslator/NameResolution
- category: DocumentationProduct
  description: Documentation for the Name Resolver, covering the API, the scoring
    algorithm used to rank matches, deployment instructions and an example Jupyter
    notebook.
  format: http
  id: name-resolver.docs
  is_public: true
  name: Name Resolver Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: name-resolver
  product_url: https://github.com/NCATSTranslator/NameResolution/tree/main/documentation
publications:
- authors:
  - Evan Morris
  - Gaurav Vaidya
  - Phil Owen
  - Jason Reilly
  - Karamarie Fecho
  - Patrick Wang
  - Yaphet Kebede
  - E. Kathleen Carter
  - Chris Bizon
  doi: 10.48550/arXiv.2601.10008
  id: doi:10.48550/arXiv.2601.10008
  journal: arXiv
  preferred: true
  title: 'The "I" in FAIR: Translating from Interoperability in Principle to Interoperation
    in Practice'
  year: '2026'
repository: https://github.com/NCATSTranslator/NameResolution
synonyms:
- Name Lookup
- NameRes
- Name Resolution
---
# SRI Name Resolver

The Name Resolver (Name Lookup, NameRes) is a service of the NCATS Biomedical Data Translator's Standards and Reference Implementation (SRI) team, developed at the Renaissance Computing Institute (RENCI). It takes lexical strings, such as a disease or drug name typed into a search box, and returns candidate identifiers (CURIEs) from biomedical vocabularies and ontologies, each with a preferred label, synonyms and Biolink types.

## How it works

Name Resolver indexes the synonym files produced by Babel, the RENCI pipeline that builds cliques of equivalent identifiers across sources. The index is served from Apache Solr. Because Babel also feeds the SRI Node Normalizer, every identifier Name Resolver returns is already normalized to the same preferred CURIE that Node Normalizer would give, with GeneProtein and DrugChemical conflation applied. Matches are ranked with a scoring algorithm described in the repository documentation.

## API

The API offers:

- `/lookup`: search by name, with an optional autocomplete mode for partial queries and filters by Biolink type, CURIE prefix or taxon.
- `/bulk-lookup`: run several lookups in one request.
- `/synonyms` and `/reverse_lookup`: return the known synonyms for given preferred CURIEs.

RENCI hosts a public instance at https://name-resolution-sri.renci.org/, and the Translator production instance is at https://name-lookup.transltr.io/.

## Citation

The repository's citation file points to the Zenodo software record (doi:10.5281/zenodo.18488923). Babel and the APIs built on it, including Name Resolver, are described in Morris et al. 2026 (arXiv:2601.10008).
