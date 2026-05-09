---
layout: schema_doc
mermaid: true
---



# Slot: product_file_size


_The size of the product file, in bytes. The build process will attempt to determine this based on the file header and populate the metadata where possible._





URI: [kgr:product_file_size](https://w3id.org/bridge2ai/data-sheets-schema/product_file_size)
Alias: product_file_size

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DocumentationProduct](DocumentationProduct.html) | A product that is documentation for a resource |  no  |
| [DataModelProduct](DataModelProduct.html) | A product that provides the rules of a data model |  no  |
| [GraphProduct](GraphProduct.html) | A product that is a graph, represented as nodes and edges |  no  |
| [GraphicalInterface](GraphicalInterface.html) | A product that is a graphical interface to a resource |  no  |
| [Product](Product.html) | A top-level class for all products in the knowledge graph registry |  no  |
| [ProcessProduct](ProcessProduct.html) | A product that is a process or algorithm |  no  |
| [ProgrammingInterface](ProgrammingInterface.html) | A product that is a programming interface (API) to a resource |  no  |
| [OntologyProduct](OntologyProduct.html) | A product that is an ontology, a formal representation of a set of concepts w... |  no  |
| [MappingProduct](MappingProduct.html) | A product that is a mapping between two or more data sources |  no  |






## Properties

* Range: [Integer](Integer.html)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:product_file_size |
| native | kgr:product_file_size |




## LinkML Source

<details>
```yaml
name: product_file_size
description: The size of the product file, in bytes. The build process will attempt
  to determine this based on the file header and populate the metadata where possible.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: product_file_size
owner: Product
domain_of:
- Product
range: integer

```
</details>
