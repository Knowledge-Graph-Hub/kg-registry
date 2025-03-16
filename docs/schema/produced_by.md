---
layout: schema_doc
mermaid: true
---



# Slot: produced_by


_The process(es) that produced the product, referred to by the identifier of each process._





URI: [kgr:produced_by](https://w3id.org/bridge2ai/data-sheets-schema/produced_by)



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

* Range: [ProcessProduct](ProcessProduct.html)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:produced_by |
| native | kgr:produced_by |




## LinkML Source

<details>
```yaml
name: produced_by
description: The process(es) that produced the product, referred to by the identifier
  of each process.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: produced_by
owner: Product
domain_of:
- Product
range: ProcessProduct
multivalued: true

```
</details>
