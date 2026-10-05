---
activity_status: active
category: Ontology
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: agrovoc@fao.org
  - contact_type: url
    value: https://www.fao.org/agrovoc
  label: Food and Agriculture Organization of the United Nations (FAO)
creation_date: '2026-10-05T00:00:00Z'
description: AGROVOC is the multilingual controlled vocabulary of the Food and Agriculture
  Organization of the United Nations (FAO), covering agriculture, food, nutrition,
  fisheries, forestry, the environment and related areas. It is a SKOS-XL thesaurus
  of more than 41,400 concepts and 1.2 million terms in up to 42 languages, edited
  in VocBench and published as linked open data with mappings to other vocabularies
  such as the NAL Thesaurus, EuroVoc, DBpedia and GeoNames. AGROVOC is used to index
  and retrieve agricultural information and to align terms across datasets, and is
  available through a Skosmos browser, a SPARQL endpoint, a REST API and monthly RDF
  dumps.
domains:
- agriculture
- nutrition
- food
- environment
fairsharing_id: FAIRsharing.anpj91
homepage_url: https://www.fao.org/agrovoc
id: agrovoc
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
name: AGROVOC
products:
- category: GraphicalInterface
  description: Skosmos browser for searching and browsing AGROVOC concepts, labels
    and hierarchies in all supported languages. It always loads the latest AGROVOC
    LOD release.
  format: http
  id: agrovoc.browser
  name: AGROVOC Skosmos Browser
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agrovoc
  product_url: https://agrovoc.fao.org/browse/agrovoc/en/
- category: ProgrammingInterface
  description: Public SPARQL endpoint (Apache Jena Fuseki) serving the AGROVOC LOD
    distribution, with a web form, sample queries and CSV download of results.
  format: http
  id: agrovoc.sparql
  name: AGROVOC SPARQL Endpoint
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agrovoc
  product_url: https://agrovoc.fao.org/sparql
- category: ProgrammingInterface
  description: Skosmos REST API for AGROVOC, returning vocabulary metadata, concept
    search results, labels and hierarchy as JSON-LD.
  format: http
  id: agrovoc.api
  name: AGROVOC REST API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agrovoc
  product_url: https://agrovoc.fao.org/browse/rest/v1/agrovoc/
- category: OntologyProduct
  compression: zip
  description: AGROVOC Core release in N-Triples, with all concepts and labels in
    all languages exported from VocBench plus the mappings to other vocabularies.
  format: ntriples
  id: agrovoc.core.nt
  name: AGROVOC Core Dump (N-Triples)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agrovoc
  product_url: https://agrovoc.fao.org/latestAgrovoc/agrovoc_core.nt.zip
- category: OntologyProduct
  compression: zip
  description: AGROVOC Core release in RDF/XML, with all concepts and labels in all
    languages exported from VocBench plus the mappings to other vocabularies.
  format: rdfxml
  id: agrovoc.core.rdf
  name: AGROVOC Core Dump (RDF/XML)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agrovoc
  product_url: https://agrovoc.fao.org/latestAgrovoc/agrovoc_core.rdf.zip
- category: GraphProduct
  compression: zip
  description: AGROVOC LOD release in N-Triples (about 10 million triples), the distribution
    behind the SPARQL endpoint and web services. It adds SKOS core labels materialized
    from SKOS-XL, inverse and symmetric inferred triples, VoID links and the Agrontology
    vocabulary to the Core release.
  format: ntriples
  id: agrovoc.lod.nt
  name: AGROVOC LOD Dump (N-Triples)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agrovoc
  product_file_size: 96365215
  product_url: https://agrovoc.fao.org/latestAgrovoc/agrovoc_lod.nt.zip
- category: GraphProduct
  compression: zip
  description: AGROVOC LOD release in N-Quads, with named graphs carrying provenance
    (for example, Agrontology in its own graph).
  format: nquads
  id: agrovoc.lod.nq
  name: AGROVOC LOD Dump (N-Quads)
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agrovoc
  product_file_size: 96881450
  product_url: https://agrovoc.fao.org/latestAgrovoc/agrovoc_lod.nq.zip
- category: Product
  description: VoID description of the AGROVOC linked dataset, listing dumps, the
    SPARQL endpoint, triple counts, license and linksets to mapped vocabularies.
  format: ttl
  id: agrovoc.void
  name: AGROVOC VoID Descriptor
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agrovoc
  product_url: https://aims.fao.org/aos/agrovoc/void.ttl
- category: DocumentationProduct
  description: AGROVOC documentation on access options (Skosmos, SPARQL, REST API
    and downloads), release contents and linked data mappings.
  format: http
  id: agrovoc.docs
  name: AGROVOC Access Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: agrovoc
  product_url: https://www.fao.org/agrovoc/access
publications:
- authors:
  - Caterina Caracciolo
  - Armando Stellato
  - Ahsan Morshed
  - Gudrun Johannsen
  - Sachit Rajbhandari
  - Yves Jaques
  - Johannes Keizer
  doi: 10.3233/SW-130106
  id: doi:10.3233/SW-130106
  journal: Semantic Web
  preferred: true
  title: The AGROVOC Linked Dataset
  year: '2013'
synonyms:
- AGROVOC Multilingual Thesaurus
- FAO AGROVOC
---
# AGROVOC

AGROVOC is the multilingual thesaurus of the Food and Agriculture Organization of the United Nations (FAO). It was first published in the early 1980s to index documents in FAO's AGRIS bibliographic database, and is now a SKOS-XL linked open dataset maintained by FAO with a community of editors in VocBench. It has more than 41,400 concepts and 1.2 million terms in up to 42 languages. Concept URIs take the form `http://aims.fao.org/aos/agrovoc/c_<number>`.

Not to be confused with the Agronomy Ontology (AgrO), which is a separate OBO-style ontology.

## Distributions

FAO publishes two RDF distributions, updated about monthly and linked from the [FAO data catalog](https://data.apps.fao.org/catalog/dataset/agrovoc-release):

- **AGROVOC Core**: the VocBench export in all languages, including mappings to other vocabularies, as RDF/XML and N-Triples.
- **AGROVOC LOD**: the Core content plus materialized SKOS labels, simple inferred triples, VoID links and the Agrontology vocabulary, as N-Triples and N-Quads. This distribution backs the SPARQL endpoint, the REST API and the Skosmos browser.

The VoID descriptor states the CC BY 4.0 license and lists linksets to vocabularies such as the NAL Thesaurus, EuroVoc, GEMET, DBpedia, GeoNames, UniProt taxonomy and several plant name databases.
