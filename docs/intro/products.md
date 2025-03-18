# Product Classes

## Product

Base class for resource representations:

### Key Attributes
- `name`: Product name
- `description`: Product details
- `product_url`: Access point
- `license`: Product-specific licensing
- `format`: Data serialization type
- `tags`: Categorization

### Provenance
- `original_source`: Origin of the product
- `secondary_source`: Additional sources
- `produced_by`: Creation process

## Specialized Product Types

### GraphProduct
- Tracks graph metrics:
  - `edge_count`
  - `node_count`
  - `predicates`
  - `node_categories`

### ProgrammingInterface
- Additional API-specific attributes:
  - `is_public`: Public accessibility
  - `is_neo4j`: Neo4j database flag
  - `connection_url`

### Other Product Types
- `DataModelProduct`: Ontology or schema
- `MappingProduct`: Mappings between data sources
- `ProcessProduct`: Algorithms or processes
- `GraphicalInterface`: Visualization tools