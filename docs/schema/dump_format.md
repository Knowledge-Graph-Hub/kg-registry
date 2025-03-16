---
layout: schema_doc
mermaid: true
---



# Slot: dump_format


_The format of a dump of the product as a file. Note the product may also be compressed._





URI: [kgr:dump_format](https://w3id.org/bridge2ai/data-sheets-schema/dump_format)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProgrammingInterface](ProgrammingInterface.html) | A product that is a programming interface (API) to a resource |  no  |
| [DataModelProduct](DataModelProduct.html) | A product that is a data model, such as an ontology or schema |  no  |
| [Product](Product.html) | A top-level class for all products in the knowledge graph registry |  no  |
| [GraphProduct](GraphProduct.html) | A product that is a graph, represented as nodes and edges |  no  |
| [MappingProduct](MappingProduct.html) | A product that is a mapping between two or more data sources |  no  |
| [ProcessProduct](ProcessProduct.html) | A product that is a process or algorithm |  no  |
| [GraphicalInterface](GraphicalInterface.html) | A product that is a graphical interface to a resource |  no  |







## Properties

* Range: [DumpFormatEnum](DumpFormatEnum.html)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:dump_format |
| native | kgr:dump_format |




## LinkML Source

<details>
```yaml
name: dump_format
description: The format of a dump of the product as a file. Note the product may also
  be compressed.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: dump_format
owner: Product
domain_of:
- Product
range: DumpFormatEnum

```
</details>
