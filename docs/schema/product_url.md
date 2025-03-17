---
layout: schema_doc
mermaid: true
---



# Slot: product_url


_The URL of the product. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface._





URI: [kgr:product_url](https://w3id.org/bridge2ai/data-sheets-schema/product_url)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GraphProduct](GraphProduct.html) | A product that is a graph, represented as nodes and edges |  no  |
| [Product](Product.html) | A top-level class for all products in the knowledge graph registry |  no  |
| [DataModelProduct](DataModelProduct.html) | A product that is a data model, such as an ontology or schema |  no  |
| [GraphicalInterface](GraphicalInterface.html) | A product that is a graphical interface to a resource |  no  |
| [ProgrammingInterface](ProgrammingInterface.html) | A product that is a programming interface (API) to a resource |  no  |
| [MappingProduct](MappingProduct.html) | A product that is a mapping between two or more data sources |  no  |
| [ProcessProduct](ProcessProduct.html) | A product that is a process or algorithm |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.html)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:product_url |
| native | kgr:product_url |




## LinkML Source

<details>
```yaml
name: product_url
description: The URL of the product. This may be a link to download a specific file,
  a base URL to an API, or a link to a graphical interface.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: product_url
owner: Product
domain_of:
- Product
range: uriorcurie

```
</details>
