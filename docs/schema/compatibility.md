---
layout: schema_doc
mermaid: true
---



# Slot: compatibility


_A list of standards that the product conforms to. This is not the same as its serialization/format._





URI: [kgr:compatibility](https://w3id.org/bridge2ai/data-sheets-schema/compatibility)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProcessProduct](ProcessProduct.html) | A product that is a process or algorithm |  no  |
| [MappingProduct](MappingProduct.html) | A product that is a mapping between two or more data sources |  no  |
| [GraphProduct](GraphProduct.html) | A product that is a graph, represented as nodes and edges |  no  |
| [ProgrammingInterface](ProgrammingInterface.html) | A product that is a programming interface (API) to a resource |  no  |
| [GraphicalInterface](GraphicalInterface.html) | A product that is a graphical interface to a resource |  no  |
| [DataModelProduct](DataModelProduct.html) | A product that is a data model, such as an ontology or schema |  no  |
| [Product](Product.html) | A top-level class for all products in the knowledge graph registry |  no  |







## Properties

* Range: [StandardCompatibility](StandardCompatibility.html)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:compatibility |
| native | kgr:compatibility |




## LinkML Source

<details>
```yaml
name: compatibility
description: A list of standards that the product conforms to. This is not the same
  as its serialization/format.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: compatibility
owner: Product
domain_of:
- Product
range: StandardCompatibility
multivalued: true
inlined: true

```
</details>
