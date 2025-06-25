---
layout: intro_doc
---

# Products

All products have the following attributes:

- `name`: A short name for the product.
- `description`: Details about the product.
- `product_url`: Access point for the product. This may be a direct link to a file or to documentation.
- `license`: Product-specific licensing. This may differ from that of its Resource.
- `format`: Data serialization type. See _Formats_ below.
- `tags`: Additional categories for the product.

Three additional attributes define the provenance of each Product:
- `original_source`: A list of origin Resource(s) of the product. 
- `secondary_source`: A list of secondary Resource(s) of the product.
- `produced_by`: The software or other process leading to creation of the product.

## Specialized Product Types

Each Product may have a more specific type.

### DataModelProduct

These Products are conceptual models, often defining hierarchical relationships. This includes ontologies.

### GraphicalInterface

These Products provide access to a graph or other data set through a visualization or other visual interface. If a KG has a web site for browsing its contents, that website is a GraphicalInterface.

### GraphProduct

These Products have a graph structure.

They have attributes to track graph metrics:
  - `edge_count`
  - `node_count`
  - `predicates`
  - `node_categories`

### MappingProduct

These products are mappings between identifiers from different data sources. They are often in the [Simple Standard for Sharing Ontological Mappings (SSSOM)](https://mapping-commons.github.io/sssom/) format.

### ProcessProduct

These Products are computational processes used to transform, manipulate, or otherwise work with data.

### ProgrammingInterface

These Products are services offering computational or programmable access to a data collection, including to a graph.

They may have these attributes:
  - `is_public`: True if the interface is publicly accessible
  - `is_neo4j`: True if the interface is for a Neo4j database
  - `connection_url`: The URL leading directly to the interface

### DocumentationProduct

These Products are documentation for a resource. This may be a website, a stand-alone document, or a collection of documents.

## Formats

Products may have one of the following formats:

- **json**: The JSON format.
- **jsonld**: The JSON-LD format.
- **rdfxml**: The RDF/XML format.
- **ttl**: The Turtle format.
- **ntriples**: The N-Triples format.
- **nquads**: The N-Quads format.
- **owl**: The OWL format.
- **obo**: The OBO format.
- **graphql**: The GraphQL format.
- **protobuf**: The Protobuf format.
- **shacl**: The SHACL format.
- **shex**: The ShEx format.
- **kgx**: The KGX standard, which is a graph exchange format for knowledge graphs. By default, this assumes KGX as TSV with separate node and edge files, usually named nodes.tsv and edges.tsv. KGX may also be represented as
  - **kgx-json**: The KGX JSON format, with nodes and edges in a single file.
  - **kgx-jsonl**: The KGX JSON Lines format, with separate node and edge files, usually named nodes.jsonl and edges.jsonl.
  - **kgx-rdf**: The KGX RDF Turtle (TTL) format, with nodes and edges in a single file.
- **sssom**: The Simple Standard for Sharing Ontological Mappings (SSSOM) format, which a format for mapping between different ontologies and other identifier systems.
