---
activity_status: active
category: Aggregator
contacts:
- category: Individual
  contact_details:
  - contact_type: github
    value: cthoyt
  label: Charles Tapley Hoyt
  orcid: 0000-0003-4423-4370
- category: Organization
  contact_details:
  - contact_type: github
    value: biopragmatics
  label: Biopragmatics
creation_date: '2026-10-04T00:00:00Z'
description: The Bioregistry is an open, community-curated registry of prefixes, CURIE
  patterns, URI formats and resolution rules for identifier resources in biomedicine
  and the life and natural sciences. It imports and aligns metadata from other registries,
  such as identifiers.org, the OBO Foundry, BioPortal, OLS, FAIRsharing, re3data,
  Wikidata and N2T, and adds manual curation of its own. It also resolves CURIEs to
  provider URLs and publishes the registry, its cross-registry mappings and derived
  prefix maps as open data. As of 2026-10-04 the registry export held 2,856 prefixes.
domains:
- information technology
- metadata
- biomedical
fairsharing_id: FAIRsharing.250a8c
homepage_url: https://bioregistry.io/
id: bioregistry
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
name: Bioregistry
products:
- category: Product
  description: Full Bioregistry export as JSON, with every prefix record including
    names, synonyms, URI formats, local identifier patterns, providers and mappings
    to the prefixes of other registries.
  format: json
  id: bioregistry.registry.json
  name: Bioregistry JSON Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:wasInfluencedBy
    source: obofoundry
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  - relation_type: prov:wasInfluencedBy
    source: ols
  - relation_type: prov:wasInfluencedBy
    source: wikidata
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: cellosaurus
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  - relation_type: prov:wasInfluencedBy
    source: biolink
  product_file_size: 786637
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/registry/registry.json
- category: Product
  description: Full Bioregistry export as YAML, with the same content as the JSON
    export.
  format: yaml
  id: bioregistry.registry.yml
  name: Bioregistry YAML Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  product_file_size: 762017
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/registry/registry.yml
- category: Product
  description: Flattened tabular Bioregistry export with one row per prefix.
  format: tsv
  id: bioregistry.registry.tsv
  name: Bioregistry TSV Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  product_file_size: 411960
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/registry/registry.tsv
- category: MappingProduct
  description: SSSOM mappings between Bioregistry prefixes and the equivalent prefixes
    in other registries, such as OBO Foundry, BioPortal, OLS, Wikidata, the Gene Ontology
    registry, Cellosaurus, UniProt and NCBI.
  format: sssom
  id: bioregistry.sssom
  name: Bioregistry SSSOM Mappings
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  - relation_type: prov:wasInfluencedBy
    source: obofoundry
  - relation_type: prov:wasInfluencedBy
    source: bioportal
  - relation_type: prov:wasInfluencedBy
    source: ols
  - relation_type: prov:wasInfluencedBy
    source: wikidata
  - relation_type: prov:wasInfluencedBy
    source: go
  - relation_type: prov:wasInfluencedBy
    source: cellosaurus
  - relation_type: prov:wasInfluencedBy
    source: uniprot
  - relation_type: prov:wasInfluencedBy
    source: ncbi
  - relation_type: prov:wasInfluencedBy
    source: biolink
  product_file_size: 136267
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/sssom/bioregistry.sssom.tsv
- category: Product
  description: RDF export of the Bioregistry in Turtle, describing prefixes, providers,
    registries and collections with the Bioregistry RDF schema.
  format: ttl
  id: bioregistry.rdf.ttl
  name: Bioregistry RDF (Turtle)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  product_file_size: 786214
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/rdf/bioregistry.ttl
- category: Product
  description: RDF export of the Bioregistry in JSON-LD.
  format: jsonld
  id: bioregistry.rdf.jsonld
  name: Bioregistry RDF (JSON-LD)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  product_file_size: 1117078
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/rdf/bioregistry.jsonld
- category: Product
  description: JSON-LD context mapping each Bioregistry prefix to its preferred URI
    prefix, for expanding and contracting CURIEs. Other contexts (OBO, semantic web,
    extended prefix maps) are in the same exports directory.
  format: jsonld
  id: bioregistry.context.jsonld
  name: Bioregistry JSON-LD Context
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  product_file_size: 40691
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/contexts/bioregistry.context.jsonld
- category: GraphicalInterface
  description: Bioregistry web site for searching and browsing prefixes, registries
    and collections and for resolving CURIEs to provider URLs.
  format: http
  id: bioregistry.portal
  name: Bioregistry Web Site
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  product_url: https://bioregistry.io/
- category: ProgrammingInterface
  description: REST API for querying Bioregistry records, metaregistry entries, collections
    and CURIE resolution, documented with OpenAPI.
  format: http
  id: bioregistry.api
  name: Bioregistry REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  product_url: https://bioregistry.io/apidocs
- category: Product
  description: Python package for loading and querying the Bioregistry, normalizing
    prefixes and CURIEs, and generating prefix maps. Released under the MIT License.
  format: python
  id: bioregistry.python
  license:
    id: https://opensource.org/licenses/MIT
    label: MIT
  name: Bioregistry Python Package
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  product_url: https://pypi.org/project/bioregistry/
  repository: https://github.com/biopragmatics/bioregistry
- category: DocumentationProduct
  description: Bioregistry documentation, including the Python package reference and
    curation guidance.
  format: http
  id: bioregistry.docs
  name: Bioregistry Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: bioregistry
  product_url: https://bioregistry.readthedocs.io/
publications:
- authors:
  - Charles Tapley Hoyt
  - Meghan Balk
  - Tiffany J. Callahan
  - Daniel Domingo-Fernández
  - Melissa A. Haendel
  - Harshad B. Hegde
  - Daniel S. Himmelstein
  - Klas Karis
  - John Kunze
  - Tiago Lubiana
  - Nicolas Matentzoglu
  - Julie McMurry
  - Sierra Moxon
  - Christopher J. Mungall
  - Adriano Rutz
  - Deepak R. Unni
  - Egon Willighagen
  - Donald Winston
  - Benjamin M. Gyori
  doi: 10.1038/s41597-022-01807-3
  id: doi:10.1038/s41597-022-01807-3
  journal: Scientific Data
  preferred: true
  title: Unifying the identification of biomedical entities with the Bioregistry
  year: '2022'
repository: https://github.com/biopragmatics/bioregistry
---
# Bioregistry

The Bioregistry is an open registry of prefixes for identifier resources, used to write and resolve compact identifiers (CURIEs) such as `CHEBI:24867`. Each record gives a prefix's name, synonyms, URI format, local identifier pattern, example and providers.

It works as a metaregistry. Records are imported and aligned from other registries, including identifiers.org, the OBO Foundry, BioPortal, OLS, FAIRsharing, re3data, Wikidata, N2T and Prefix Commons, and then curated by hand. The alignments are published as SSSOM mappings.

## Data

The registry lives in the GitHub repository and is exported nightly as JSON, YAML, TSV, RDF (Turtle and JSON-LD) and SSSOM, along with JSON-LD contexts and extended prefix maps. Curated data are released under CC0 1.0. Aggregated data keep their original licenses. The code is MIT licensed.

## Access

The web site at https://bioregistry.io/ offers search, a CURIE resolver and a REST API. The `bioregistry` Python package loads the same data locally.