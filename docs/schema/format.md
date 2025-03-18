---
layout: schema_doc
mermaid: true
---



# Slot: format


_The format or serialization of the product. Generally corresponds to the file extension._





URI: [kgr:format](https://w3id.org/bridge2ai/data-sheets-schema/format)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Product](Product.html) | A top-level class for all products in the knowledge graph registry |  no  |
| [MappingProduct](MappingProduct.html) | A product that is a mapping between two or more data sources |  no  |
| [GraphicalInterface](GraphicalInterface.html) | A product that is a graphical interface to a resource |  no  |
| [ProcessProduct](ProcessProduct.html) | A product that is a process or algorithm |  no  |
| [GraphProduct](GraphProduct.html) | A product that is a graph, represented as nodes and edges |  no  |
| [ProgrammingInterface](ProgrammingInterface.html) | A product that is a programming interface (API) to a resource |  no  |
| [DataModelProduct](DataModelProduct.html) | A product that is a data model, such as an ontology or schema |  no  |







## Properties

* Range: [FormatEnum](FormatEnum.html)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:format |
| native | kgr:format |




## LinkML Source

<details>
```yaml
name: format
description: The format or serialization of the product. Generally corresponds to
  the file extension.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: format
owner: Product
domain_of:
- Product
range: FormatEnum

```
</details>
