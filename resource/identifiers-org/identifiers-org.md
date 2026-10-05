---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: identifiers-org@ebi.ac.uk
  - contact_type: url
    value: https://www.ebi.ac.uk/
  id: ebi
  label: EMBL-EBI
- category: Individual
  contact_details:
  - contact_type: email
    value: hhe@ebi.ac.uk
  - contact_type: github
    value: hHermjakob
  label: Henning Hermjakob
  orcid: 0000-0001-8479-0262
creation_date: '2026-10-04T00:00:00Z'
description: Identifiers.org, run by EMBL-EBI as an ELIXIR Interoperability Platform
  resource, is a registry of namespace prefixes for life science identifiers together
  with a resolver that turns compact identifiers (CURIEs such as taxonomy:9606) into
  URLs at the providing resources. It grew out of the MIRIAM Registry. When checked
  on 2026-10-04 the registry held 865 namespaces with 1,037 provider resources, available
  through a web interface, REST APIs, a full JSON dataset export and a SPARQL endpoint
  that models the registry with VoID and DCAT.
domains:
- information technology
- metadata
homepage_url: https://identifiers.org/
id: identifiers-org
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: Identifiers.org
products:
- category: ProgrammingInterface
  description: Identifiers.org resolver. Appending a compact identifier (prefix:accession)
    to https://identifiers.org/ redirects to the record at the recommended provider
    for that namespace.
  format: http
  id: identifiers-org.resolver
  name: Identifiers.org Resolver
  original_source:
  - relation_type: prov:hadPrimarySource
    source: identifiers-org
  product_url: https://identifiers.org/
- category: GraphicalInterface
  description: Web interface for browsing and searching the Identifiers.org registry
    of namespaces and providers, and for submitting prefix and resource registration
    requests.
  format: http
  id: identifiers-org.registry
  name: Identifiers.org Registry Web Interface
  original_source:
  - relation_type: prov:hadPrimarySource
    source: identifiers-org
  product_url: https://registry.identifiers.org/registry
- category: ProgrammingInterface
  description: Identifiers.org Registry REST API (Spring Data REST, HAL+JSON) for
    querying namespaces, resources and institutions, plus the resolution dataset service.
    The API root requires authentication, but the restApi and resolutionApi paths
    are open.
  format: http
  id: identifiers-org.registry-api
  name: Identifiers.org Registry API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: identifiers-org
  product_url: https://registry.api.identifiers.org/restApi/namespaces
- category: ProgrammingInterface
  description: Identifiers.org Resolution API, which returns the list of providers
    for a compact identifier as JSON, sorted by recommended usage, and converts provider
    URLs back into identifiers.org URIs.
  format: http
  id: identifiers-org.resolver-api
  name: Identifiers.org Resolution API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: identifiers-org
  product_url: https://resolver.api.identifiers.org/
- category: Product
  description: Full export of the Identifiers.org registry as a single JSON document,
    with every namespace (prefix, MIRIAM id, name, description, local identifier pattern)
    and its provider resources and URL patterns.
  format: json
  id: identifiers-org.dataset
  name: Identifiers.org Resolver Dataset
  original_source:
  - relation_type: prov:hadPrimarySource
    source: identifiers-org
  product_url: https://registry.api.identifiers.org/resolutionApi/getResolverDataset
- category: ProgrammingInterface
  description: SPARQL endpoint over the Identifiers.org registry, generated with Ontop
    from R2RML mappings; the registry is modeled as a dcat:Catalog, namespaces as dcat:Dataset
    and resources as dcat:DataService.
  format: http
  id: identifiers-org.sparql
  name: Identifiers.org SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: identifiers-org
  product_url: https://sparql.api.identifiers.org/sparql
- category: OntologyProduct
  description: Ontology of the terms Identifiers.org created for registry attributes
    not covered by VoID and DCAT, kept with the Ontop mappings used by the SPARQL
    endpoint.
  format: mixed
  id: identifiers-org.ontology
  name: Identifiers.org Registry Ontology
  original_source:
  - relation_type: prov:hadPrimarySource
    source: identifiers-org
  product_url: https://github.com/identifiers-org/ontop/tree/main/idorg-ontology
- category: ProcessProduct
  description: GitHub organization holding the source code for the Identifiers.org
    resolver, registry, web front ends, Java client library and SPARQL service.
  format: http
  id: identifiers-org.code
  name: Identifiers.org Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: identifiers-org
  product_url: https://github.com/identifiers-org
- category: DocumentationProduct
  description: Identifiers.org documentation, covering the identification scheme,
    resolving mechanisms, REST APIs (with Swagger UI), SPARQL service, terms of use
    and FAQ.
  format: http
  id: identifiers-org.docs
  name: Identifiers.org Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: identifiers-org
  product_url: https://docs.identifiers.org/
- category: Product
  description: Full Bioregistry export as JSON, with every prefix record including names,
    synonyms, URI formats, local identifier patterns, providers and mappings to the prefixes
    of other registries.
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
  - relation_type: prov:wasInfluencedBy
    source: identifiers-org
  - relation_type: prov:wasInfluencedBy
    source: fairsharing
  - relation_type: prov:wasInfluencedBy
    source: re3data
  - relation_type: prov:wasInfluencedBy
    source: agroportal
  - relation_type: prov:wasInfluencedBy
    source: ecoportal
  - relation_type: prov:wasInfluencedBy
    source: aberowl
  product_file_size: 786637
  product_url: https://raw.githubusercontent.com/biopragmatics/bioregistry/main/exports/registry/registry.json
- category: MappingProduct
  description: SSSOM mappings between Bioregistry prefixes and the equivalent prefixes in
    other registries, such as OBO Foundry, BioPortal, OLS, Wikidata, the Gene Ontology registry,
    Cellosaurus, UniProt and NCBI.
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
  - relation_type: prov:wasInfluencedBy
    source: identifiers-org
  - relation_type: prov:wasInfluencedBy
    source: fairsharing
  - relation_type: prov:wasInfluencedBy
    source: re3data
  - relation_type: prov:wasInfluencedBy
    source: agroportal
  - relation_type: prov:wasInfluencedBy
    source: ecoportal
  - relation_type: prov:wasInfluencedBy
    source: aberowl
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
- authors:
  - N. Juty
  - N. Le Novere
  - C. Laibe
  doi: 10.1093/nar/gkr1097
  id: doi:10.1093/nar/gkr1097
  journal: Nucleic Acids Research
  title: 'Identifiers.org and MIRIAM Registry: community resources to provide persistent
    identification'
  year: '2012'
repository: https://github.com/identifiers-org
synonyms:
- identifiers.org
- MIRIAM Registry
- Identifiers.org (MIRIAM Registry)
---
# Identifiers.org

Identifiers.org is a central registry and resolver for compact identifiers in the life sciences, run by EMBL-EBI and part of the ELIXIR Interoperability Platform. Each registered namespace has a prefix (for example `taxonomy`, `uniprot` or `GO`), a regular expression for valid local identifiers, and one or more provider resources with URL patterns. The service grew out of the MIRIAM Registry, which originally collected identifier schemes for annotating systems biology models.

## Resolution

Appending a compact identifier to `https://identifiers.org/` (for example `https://identifiers.org/taxonomy:9606`) redirects to the record at the recommended provider. The Resolution API at `https://resolver.api.identifiers.org/` returns all providers for a compact identifier as JSON and can map provider URLs back to identifiers.org URIs.

## Registry Access

- **Web interface**: browse namespaces and submit prefix or resource registration requests at <https://registry.identifiers.org/registry>.
- **Registry REST API**: HAL+JSON endpoints under `https://registry.api.identifiers.org/restApi/` (the API root itself returns HTTP 401).
- **Dataset export**: the whole registry as one JSON file from `getResolverDataset` (865 namespaces and 1,037 providers on 2026-10-04).
- **SPARQL**: `https://sparql.api.identifiers.org/sparql`, modeling the registry with VoID and DCAT through Ontop.

The registry data is released under CC BY 4.0.
