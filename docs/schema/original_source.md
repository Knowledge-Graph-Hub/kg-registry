---
layout: schema_doc
mermaid: true
---



# Slot: original_source


_The original source of the product. This only needs to be the identifier of the resource. This may be the parent resource or another resource. Note this is not the same as components of a graph; this should only be used when a single source is known._





URI: [kgr:original_source](https://w3id.org/bridge2ai/data-sheets-schema/original_source)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProgrammingInterface](ProgrammingInterface.html) | A product that is a programming interface (API) to a resource |  no  |
| [GraphicalInterface](GraphicalInterface.html) | A product that is a graphical interface to a resource |  no  |
| [DataModelProduct](DataModelProduct.html) | A product that is a data model, such as an ontology or schema |  no  |
| [ProcessProduct](ProcessProduct.html) | A product that is a process or algorithm |  no  |
| [GraphProduct](GraphProduct.html) | A product that is a graph, represented as nodes and edges |  no  |
| [MappingProduct](MappingProduct.html) | A product that is a mapping between two or more data sources |  no  |
| [Product](Product.html) | A top-level class for all products in the knowledge graph registry |  no  |







## Properties

* Range: [Resource](Resource.html)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:original_source |
| native | kgr:original_source |




## LinkML Source

<details>
```yaml
name: original_source
description: The original source of the product. This only needs to be the identifier
  of the resource. This may be the parent resource or another resource. Note this
  is not the same as components of a graph; this should only be used when a single
  source is known.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: original_source
owner: Product
domain_of:
- Product
range: Resource

```
</details>
