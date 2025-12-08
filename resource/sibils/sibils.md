---
activity_status: active
category: DataSource
contacts:
- category: Individual
  contact_details:
  - contact_type: email
    value: julien.gobeill@hesge.ch
  label: Julien Gobeill
- category: Organization
  contact_details:
  - contact_type: url
    value: https://sibils.org/
  id: sib
  label: SIBiLS - Swiss Institute of Bioinformatics Literature Services
description: SIBiLS (Swiss Institute of Bioinformatics Literature Services) provides
  personalized information retrieval in biological literature, with customizable search
  in semantically enriched contents based on keywords and mapped biomedical entities
  from standardized vocabularies.
domains:
- biological systems
- health
homepage_url: https://sibils.org/
id: sibils
layout: resource_detail
license:
  id: https://creativecommons.org/licenses/by/3.0/ch/
  label: CC-BY-3.0-CH
name: SIBiLS
products:
- category: GraphicalInterface
  description: Web interface for exploring SIBiLS data
  id: sibils.site
  is_public: true
  name: SIBiLS Web Interface
  original_source:
  - sibils
  product_url: https://sibils.org/
  secondary_source:
  - sibils
- category: ProgrammingInterface
  description: SPARQL endpoint for querying SIBiLS data
  id: sibils.api.sparql
  is_public: true
  name: SIBiLS SPARQL Endpoint
  original_source:
  - sibils
  product_url: https://sparql.sibils.org/sparql
  secondary_source:
  - sibils
- category: ProgrammingInterface
  description: RESTful API for fetching annotated contents from SIBiLS collections
  id: sibils.api.rest.fetch
  is_public: true
  name: SIBiLS Fetch API
  original_source:
  - sibils
  product_url: https://sibils.org/API#Fetch-API
  secondary_source:
  - sibils
- category: ProgrammingInterface
  description: RESTful API for customizable search in SIBiLS collections
  id: sibils.api.rest.search
  is_public: true
  name: SIBiLS Search API
  original_source:
  - sibils
  product_url: https://sibils.org/API#Customizable-search-API
  secondary_source:
  - sibils
- category: ProgrammingInterface
  description: RESTful API for question answering using natural language in SIBiLS
    collections
  id: sibils.api.rest.qa
  is_public: true
  name: SIBiLS Question Answering API
  original_source:
  - sibils
  product_url: https://sibils.org/API#Question-Answering-API
  secondary_source:
  - sibils
publications:
- authors:
  - Gobeill J
  - Caucheteur D
  - Michel PA
  - Mottin L
  - Pasche E
  - Ruch P
  doi: doi:10.1093/nar/gkaa328
  id: doi:10.1093/nar/gkaa328
  preferred: true
  title: 'SIB Literature Services: RESTful customizable search engines in biomedical
    literature, enriched with automatically mapped biomedical concepts'
  year: '2020'
---

SIBiLS (Swiss Institute of Bioinformatics Literature Services) provides personalized information retrieval services in biological literature. The platform offers fully customizable search capabilities in semantically enriched contents based on keywords and/or mapped biomedical entities from a growing set of standardized and legacy vocabularies.

The services cover four main collections that are updated daily:
- MEDLINE citations
- PubMed Central (PMC) full texts
- Plazi treatments (taxonomic treatments from biodiversity literature)
- PMC supplementary files

Key features of SIBiLS include:
- Semantically enriched content with billions of mapped biomedical entities
- Customizable search engines to assist curation of genes and gene products
- RESTful APIs for programmatic access to literature services
- Natural language question answering capabilities
- Specialized services for different domains (biodiversity, biotechnology, genetic variations)
- SPARQL endpoint for semantic queries

SIBiLS content is parsed and enriched with mapped biomedical entities from reference vocabularies, making it particularly valuable for life science researchers and curation teams. The platform is built on modern technologies that scale with big data, including MongoDB and Elasticsearch.

The services are developed by the Swiss Institute of Bioinformatics in collaboration with the Haute Ecole de Gestion in Geneva and are supported by Elixir, swissuniversities, and HES-SO. The tagged entities in SIBiLS are licensed under Creative Commons Attribution 3.0 Switzerland License.