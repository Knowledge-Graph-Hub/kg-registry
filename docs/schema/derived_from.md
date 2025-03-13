---
layout: schema_doc
mermaid: true
---



# Slot: derived_from


_The resource that the product is derived from. This only needs to be the identifier of the resource. It may be the parent resource or another resource, e.g., an Aggregator._





URI: [kgr:derived_from](https://w3id.org/bridge2ai/data-sheets-schema/derived_from)



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
| self | kgr:derived_from |
| native | kgr:derived_from |




## LinkML Source

<details>
```yaml
name: derived_from
description: The resource that the product is derived from. This only needs to be
  the identifier of the resource. It may be the parent resource or another resource,
  e.g., an Aggregator.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: derived_from
owner: Product
domain_of:
- Product
range: Resource

```
</details>
