---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://cdlib.org/
  label: California Digital Library
- category: Individual
  contact_details:
  - contact_type: github
    value: datadavev
  label: Dave Vieglais
creation_date: '2026-10-05T00:00:00Z'
description: N2T (Name-to-Thing) is a resolver for persistent and compact identifiers
  run by the California Digital Library. Given an identifier of the form scheme:prefix/value,
  such as an ARK, DOI or biomedical compact identifier (CURIE), it matches the scheme
  to a registered definition and redirects to the target resolver. N2T shares a common
  compact identifier prefix space with identifiers.org under an agreement between
  CDL and EMBL-EBI. The service was re-platformed as a lighter scheme resolver (version
  0.12.5 when checked on 2026-10-05); the legacy N2T service is deprecated, ARK resolution
  now forwards to arks.org, and the ARK NAAN and shoulder registries moved to GitHub
  Pages. As of 2026-10-05 it listed 1,776 registered schemes.
domains:
- information technology
- metadata
homepage_url: https://n2t.net/
id: n2t
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
name: N2T
products:
- category: ProgrammingInterface
  description: The N2T resolver. Identifiers appended to https://n2t.net/ (for example
    https://n2t.net/pdb:2gc4 or https://n2t.net/ark:/88435/hq37vq534) are matched
    to a registered scheme and redirected to its resolver. An OpenAPI description
    of the resolution and scheme information endpoints is served at https://n2t.net/api.
  format: http
  id: n2t.resolver
  name: N2T Resolver
  original_source:
  - relation_type: prov:hadPrimarySource
    source: n2t
  product_url: https://n2t.net/
- category: Product
  description: JSON list of the identifier schemes and compact identifier prefixes
    currently registered with the N2T resolver (1,776 schemes when checked on 2026-10-05),
    from the service's scheme information endpoint.
  format: json
  id: n2t.schemes
  name: N2T Registered Schemes
  original_source:
  - relation_type: prov:hadPrimarySource
    source: n2t
  product_url: https://n2t.net/.info?valid=1
- category: Product
  description: Full YAML list of N2T prefix records with their names, redirect rules,
    test identifiers and probe URLs, combining records from the ARK NAAN registry,
    EZID shoulders, the shared identifiers.org prefix list and Prefix Commons. The
    file was last modified in July 2025.
  format: yaml
  id: n2t.prefixes
  name: N2T Full Prefix List
  original_source:
  - relation_type: prov:hadPrimarySource
    source: n2t
  product_file_size: 1385629
  product_url: https://n2t.net/e/n2t_full_prefixes.yaml
- category: Product
  description: Registry of ARK Name Assigning Authority Numbers (NAANs) and the organizations
    that hold them, formerly served by N2T and now published on GitHub Pages.
  format: txt
  id: n2t.naan-registry
  name: ARK NAAN Registry
  original_source:
  - relation_type: prov:hadPrimarySource
    source: n2t
  product_file_size: 325008
  product_url: https://cdluc3.github.io/naan_reg_priv/naan_registry.txt
- category: DocumentationProduct
  description: Documentation of N2T, covering the origins of the resolver, compact
    identifiers and the legacy N2T API and user interface.
  format: http
  id: n2t.docs
  name: N2T Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: n2t
  product_url: https://n2t.net/e/about.html
- category: ProcessProduct
  description: Source code of the next-generation N2T Python scheme resolver, including
    the scheme configuration, released under the MIT License.
  format: http
  id: n2t.code
  license:
    id: https://opensource.org/licenses/MIT
    label: MIT
  name: N2T Resolver Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: n2t
  product_url: https://github.com/CDLUC3/N2T
  repository: https://github.com/CDLUC3/N2T
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
  - relation_type: prov:wasInfluencedBy
    source: n2t
  product_file_size: 786637
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/registry/registry.json
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
  - relation_type: prov:wasInfluencedBy
    source: n2t
  product_file_size: 136267
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/sssom/bioregistry.sssom.tsv
publications:
- authors:
  - Sarala M. Wimalaratne
  - Nick Juty
  - John Kunze
  - Greg Janée
  - Julie A. McMurry
  - Niall Beard
  - Rafael Jimenez
  - Jeffrey S. Grethe
  - Henning Hermjakob
  - Maryann E. Martone
  - Tim Clark
  doi: 10.1038/sdata.2018.29
  id: doi:10.1038/sdata.2018.29
  journal: Scientific Data
  preferred: true
  title: Uniform resolution of compact identifiers for biomedical data
  year: '2018'
repository: https://github.com/CDLUC3/N2T
synonyms:
- Name-to-Thing
- N2T.net
---
# N2T

N2T (Name-to-Thing) is a persistent identifier resolver run by the California Digital Library. It works like a URL shortener for persistent identifiers: a request such as `https://n2t.net/pdb:2gc4` is matched to a registered scheme or prefix and redirected to the resolver for that scheme.

N2T resolves ARKs, DOIs and other identifier schemes, and compact identifiers (CURIEs) for biomedical data. Its compact identifier prefixes are shared with identifiers.org, as described in Wimalaratne et al. 2018.

## Status

The legacy N2T service is deprecated. The current resolver is a smaller Python application (https://github.com/CDLUC3/N2T, MIT License). ARK resolution forwards to arks.org, and the ARK NAAN and shoulder registries are published at https://cdluc3.github.io/naan_reg_priv/. The full legacy prefix list is still served but was last modified in July 2025.

## Access

The scheme list is available as JSON from `https://n2t.net/.info?valid=1`, and an OpenAPI description of the resolver is at https://n2t.net/api.