---
activity_status: active
category: Ontology
creation_date: '2025-10-10T00:00:00Z'
description: The Medical Subject Headings (MeSH) is a hierarchically-organized controlled vocabulary produced by the National Library of Medicine (NLM). It serves as the standard thesaurus for indexing and cataloging biomedical and health-related information in MEDLINE/PubMed and other NLM databases.
domains:
  - biomedical
  - health
  - literature
homepage_url: https://www.nlm.nih.gov/mesh/meshhome.html
id: "mesh"
last_modified_date: '2025-10-10T00:00:00Z'
layout: resource_detail
license:
  id: https://www.nlm.nih.gov/databases/download/terms_and_conditions_mesh.html
  label: NLM Terms and Conditions for MeSH Data
name: Medical Subject Headings (MeSH)
repository: https://nlmpubs.nlm.nih.gov/projects/mesh/
publications:
  - authors:
      - Henry J. Lowe
    id: "https://doi.org/10.1001/jama.1994.03510380059038"
    preferred: true
    title: Understanding and Using the Medical Subject Headings (MeSH) Vocabulary to Perform Literature Searches
    year: "1994"
products:
  - category: GraphicalInterface
    description: The official MeSH Browser for searching and browsing the Medical Subject Headings vocabulary. Provides hierarchical navigation and term details.
    format: http
    id: "mesh.browser"
    name: MeSH Browser
    product_url: https://meshb.nlm.nih.gov/search
  - category: OntologyProduct
    description: MeSH data in XML format containing descriptors, qualifiers, and supplemental concept records. Updated annually with daily updates for SCRs.
    format: xml
    id: "mesh.xml"
    name: MeSH XML Data
    product_url: https://nlmpubs.nlm.nih.gov/projects/mesh/MESH_FILES/xmlmesh/
  - category: OntologyProduct
    description: MeSH data in RDF (Resource Description Framework) format for semantic web applications. Updated daily Monday through Friday.
    format: rdfxml
    id: "mesh.rdf"
    name: MeSH RDF Data
    product_url: https://nlmpubs.nlm.nih.gov/projects/mesh/rdf/2025/
  - category: OntologyProduct
    description: MeSH data in ASCII text format containing descriptors, qualifiers, and supplemental concept records. Updated annually with daily SCR updates.
    format: txt
    id: "mesh.ascii"
    name: MeSH ASCII Data
    product_url: https://nlmpubs.nlm.nih.gov/projects/mesh/MESH_FILES/asciimesh/
  - category: OntologyProduct
    description: MeSH data in MARC 21 bibliographic format for library systems. Posted monthly.
    format: mixed
    id: "mesh.marc"
    name: MeSH MARC 21 Data
    product_url: https://nlmpubs.nlm.nih.gov/projects/mesh/MESH_FILES/meshmarc/
  - category: ProgrammingInterface
    description: E-utilities API for programmatic access to MeSH data through NCBI's Entrez system.
    format: http
    id: "mesh.api.eutilities"
    name: MeSH E-utilities API
    product_url: https://www.ncbi.nlm.nih.gov/books/NBK25500/
  - category: ProgrammingInterface
    description: SPARQL endpoint and REST API for querying MeSH RDF data with semantic web technologies.
    format: http
    id: "mesh.api.rdf"
    name: MeSH RDF API
    product_url: https://id.nlm.nih.gov/mesh/swagger/ui
  - category: GraphicalInterface
    description: SPARQL query editor interface for interactive querying of MeSH data using semantic web query language.
    format: http
    id: "mesh.sparql.editor"
    name: MeSH SPARQL Query Editor
    product_url: https://id.nlm.nih.gov/mesh/query
  - category: Product
    description: MeSH on Demand service for suggesting MeSH terms for text or citations. Helps identify appropriate subject headings for indexing.
    format: http
    id: "mesh.ondemand"
    name: MeSH on Demand
    product_url: https://meshb.nlm.nih.gov/MeSHonDemand
  - category: DocumentationProduct
    description: Comprehensive documentation about MeSH including tutorials, webinars, and user guides for understanding and using the vocabulary.
    format: http
    id: "mesh.documentation"
    name: MeSH Documentation and Tutorials
    product_url: https://www.nlm.nih.gov/bsd/disted/mesh.html
---

# Medical Subject Headings (MeSH)

The Medical Subject Headings (MeSH) is a hierarchically-organized controlled vocabulary developed and maintained by the National Library of Medicine (NLM). MeSH serves as the authoritative thesaurus for indexing, cataloging, and searching biomedical and health-related information across multiple NLM databases, most notably MEDLINE/PubMed.

## Overview

MeSH provides a consistent way to retrieve information that may use different terminology for the same concepts. It consists of descriptors arranged in a hierarchical structure that permits searching at various levels of specificity. The vocabulary is updated annually, with new descriptors added and existing ones modified to reflect advances in medical knowledge.

## Key Features

- **Hierarchical Structure**: MeSH terms are organized in a tree structure from general to specific, allowing both broad and narrow searches
- **Controlled Vocabulary**: Provides standardized terminology to improve search precision and recall
- **Cross-References**: Includes entry terms and see-also references to guide users to appropriate descriptors
- **Qualifiers**: Subheadings that can be combined with descriptors to specify particular aspects of a topic
- **Supplemental Concept Records (SCRs)**: Additional terms for chemicals, drugs, and other specific entities

## Applications

MeSH is primarily used for:
- Indexing articles in MEDLINE/PubMed and other biomedical databases
- Literature searching and systematic reviews
- Information retrieval in biomedical research
- Cataloging library materials in medical collections
- Supporting semantic web applications through RDF representation

## Data Formats and Access

MeSH data is available in multiple formats to support different use cases:
- **XML**: Structured data format with full hierarchical information
- **RDF**: Semantic web format for linked data applications
- **ASCII**: Plain text format for legacy systems
- **MARC 21**: Library cataloging format

The vocabulary is accessible through various interfaces including the MeSH Browser, programmatic APIs, and downloadable data files. Updates are provided annually for the main vocabulary, with daily updates for supplemental concept records.
