---
activity_status: active
category: Aggregator
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://cemse.kaust.edu.sa/borg
  - contact_type: github
    value: bio-ontology-research-group
  label: Bio-Ontology Research Group, KAUST
- category: Individual
  contact_details:
  - contact_type: email
    value: maxat.kulmanov@kaust.edu.sa
  - contact_type: github
    value: coolmaksat
  label: Maxat Kulmanov
  orcid: 0000-0003-1710-1820
creation_date: '2026-10-04T00:00:00Z'
description: AberOWL is an ontology repository and reasoning service developed by
  the Bio-Ontology Research Group (BORG) at KAUST. It loads biomedical ontologies
  into OWL reasoners (ELK by default) and offers Description Logic queries in Manchester
  OWL Syntax, full-text search over classes and ontologies, rewriting of SPARQL queries
  that embed OWL DL frames, a REST API and an MCP server for AI agents. Ontology metadata
  is synced daily from the OBO Foundry and BioPortal. As of 2026-10-04 it listed 971
  ontologies with about 12.1 million classes, running on the redesigned Aber-OWL 2
  software.
domains:
- biomedical
- information technology
homepage_url: https://aber-owl.net/
id: aberowl
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  display_note: 'No license is declared for this resource. This is the most restrictive
    license (custom) among its sources: bioportal.'
  id: https://www.bioontology.org/terms/
  inferred_from:
  - bioportal
  label: BioPortal Terms of Use (individual ontologies carry their own licenses)
  restrictiveness: custom
  status: inferred
  unresolved_sources: []
name: AberOWL
products:
- category: GraphicalInterface
  description: Web portal for searching and browsing the AberOWL ontology repository,
    viewing class hierarchies and metadata, and running DL and SPARQL-rewriting queries.
  format: http
  id: aberowl.portal
  is_public: true
  name: AberOWL Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aberowl
  - relation_type: prov:hadPrimarySource
    source: bioportal
  product_url: https://aber-owl.net/
- category: ProgrammingInterface
  description: REST API (FastAPI, documented with Swagger UI) for listing ontologies,
    retrieving classes, full-text search and DL queries (subclass, superclass, equivalent)
    across the AberOWL repository.
  format: http
  id: aberowl.api
  is_public: true
  name: AberOWL REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aberowl
  - relation_type: prov:hadPrimarySource
    source: bioportal
  product_url: https://aber-owl.net/api/docs
  warnings:
  - When checked on 2026-10-04, listing, search and statistics endpoints responded,
    but DL query endpoints (/api/dlquery, /api/dlquery_all) returned "API server is
    down!".
- category: ProgrammingInterface
  description: SPARQL rewriting service (Aber-OWL SPARQL) that expands OWL DL frames
    embedded in SPARQL queries into concrete class IRIs, using the AberOWL reasoners.
    The rewritten query is returned for execution at an external SPARQL endpoint;
    AberOWL does not host a triple store.
  format: http
  id: aberowl.sparql
  is_public: true
  name: AberOWL SPARQL Rewriter
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aberowl
  product_url: https://aber-owl.net/api/sparql
- category: ProgrammingInterface
  description: Model Context Protocol (MCP) server exposing AberOWL search, reasoning
    and SPARQL rewriting to AI agents over Streamable HTTP.
  format: http
  id: aberowl.mcp
  is_public: true
  name: AberOWL MCP Server
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aberowl
  product_url: https://aber-owl.net/mcp/ontology/mcp
- category: Product
  description: JSON listing of all ontologies in AberOWL with metadata, reasoner status,
    class counts and relative download URLs for the mirrored OWL files.
  format: json
  id: aberowl.ontology-list
  is_public: true
  name: AberOWL Ontology Listing
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aberowl
  - relation_type: prov:hadPrimarySource
    source: bioportal
  product_url: https://aber-owl.net/api/listOntologies
- category: DocumentationProduct
  description: AberOWL documentation page for the REST API and MCP server.
  format: http
  id: aberowl.docs
  is_public: true
  name: AberOWL API Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aberowl
  product_url: https://aber-owl.net/docs
- category: ProcessProduct
  description: Source code for Aber-OWL 2, the distributed version of AberOWL with
    a FastAPI central server, Elasticsearch search, an MCP server and OWLAPI reasoner
    worker containers.
  format: http
  id: aberowl.code
  is_public: true
  license:
    id: https://opensource.org/licenses/BSD-3-Clause
    label: BSD-3-Clause
  name: Aber-OWL 2 Source Code
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aberowl
  product_url: https://github.com/bio-ontology-research-group/aberowl2
- category: ProcessProduct
  description: Source code for the original AberOWL ontology repository and reasoning
    service.
  format: http
  id: aberowl.code-legacy
  is_public: true
  license:
    id: https://opensource.org/licenses/BSD-3-Clause
    label: BSD-3-Clause
  name: AberOWL Source Code (original)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: aberowl
  product_url: https://github.com/bio-ontology-research-group/AberOWL
- category: OntologyProduct
  description: OWL-DL edition of the Lipid Ontology (LiPrO), representing the LIPIDMAPS
    nomenclature classification. Served as an archived mirror via AberOWL; the original
    OBO PURL no longer resolves.
  format: owl
  id: lipro.owl
  name: Lipid Ontology OWL product
  original_source:
  - relation_type: prov:hadPrimarySource
    source: lipro
  - relation_type: prov:wasDerivedFrom
    source: aberowl
  product_file_size: 50539
  product_url: http://aber-owl.net/media/ontologies/LIPRO/4/lipro.owl
  warnings:
  - File was not able to be retrieved when checked on 2026-10-04. The AberOWL mirror
    returned HTTP 404 and LIPRO no longer appears in the AberOWL ontology list.
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
  - Robert Hoehndorf
  - Karin Slater
  - Paul N Schofield
  - Georgios V Gkoutos
  doi: 10.1186/s12859-015-0456-9
  id: doi:10.1186/s12859-015-0456-9
  journal: BMC Bioinformatics
  preferred: true
  title: 'Aber-OWL: a framework for ontology-based data access in biology'
  year: '2015'
- authors:
  - Luke Slater
  - Georgios V. Gkoutos
  - Paul N. Schofield
  - Robert Hoehndorf
  doi: 10.1186/s13326-016-0090-0
  id: doi:10.1186/s13326-016-0090-0
  journal: Journal of Biomedical Semantics
  title: Using AberOWL for fast and scalable reasoning over BioPortal ontologies
  year: '2016'
synonyms:
- Aber-OWL
- Aber-OWL 2
---
# AberOWL

AberOWL is an ontology repository that provides reasoning as a service. It is developed by the Bio-Ontology Research Group (BORG) at King Abdullah University of Science and Technology (KAUST). Each ontology is loaded into an OWL reasoner (ELK by default, with Structural and HermiT available), so users can query it semantically and not just by label.

## Features

- **DL queries**: subclass, superclass and equivalent-class queries written in Manchester OWL Syntax, for example `'part of' some 'cell'`.
- **Full-text search** over class labels, synonyms and OBO IDs across the whole repository.
- **SPARQL rewriting** (Aber-OWL SPARQL): OWL DL frames embedded in SPARQL queries are expanded into concrete class IRIs. The rewritten query can then be run at an external endpoint such as UniProt's.
- **REST API** and an **MCP server**, so AI agents can use the same search and reasoning services.

Ontology metadata is synced daily from the OBO Foundry and BioPortal. The current deployment runs Aber-OWL 2, which splits the service into a central server and reasoner worker containers. When checked on 2026-10-04, the site listed 971 ontologies with about 12.1 million classes. Search and listing worked, but DL query endpoints reported that the reasoning backend was down.