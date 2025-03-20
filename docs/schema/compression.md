---
layout: schema_doc
mermaid: true
---



# Slot: compression


_The type of compression used with the product. If this is not specified, it is assumed to be uncompressed._





URI: [kgr:compression](https://w3id.org/bridge2ai/data-sheets-schema/compression)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MappingProduct](MappingProduct.html) | A product that is a mapping between two or more data sources |  no  |
| [ProgrammingInterface](ProgrammingInterface.html) | A product that is a programming interface (API) to a resource |  no  |
| [Product](Product.html) | A top-level class for all products in the knowledge graph registry |  no  |
| [ProcessProduct](ProcessProduct.html) | A product that is a process or algorithm |  no  |
| [DataModelProduct](DataModelProduct.html) | A product that is a data model, such as an ontology or schema |  no  |
| [GraphProduct](GraphProduct.html) | A product that is a graph, represented as nodes and edges |  no  |
| [GraphicalInterface](GraphicalInterface.html) | A product that is a graphical interface to a resource |  no  |







## Properties

* Range: [CompressionEnum](CompressionEnum.html)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:compression |
| native | kgr:compression |




## LinkML Source

<details>
```yaml
name: compression
description: The type of compression used with the product. If this is not specified,
  it is assumed to be uncompressed.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: compression
owner: Product
domain_of:
- Product
range: CompressionEnum

```
</details>
