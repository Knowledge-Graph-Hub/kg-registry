---
layout: schema_doc
mermaid: true
---



# Slot: url



URI: [kgr:url](https://w3id.org/bridge2ai/data-sheets-schema/url)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Usage](Usage.html) | The usage of a resource |  no  |
| [ProgrammingInterface](ProgrammingInterface.html) | A product that is a programming interface (API) to a resource |  no  |
| [Organization](Organization.html) | An organization |  no  |
| [GraphicalInterface](GraphicalInterface.html) | A product that is a graphical interface to a resource |  no  |
| [DataModelProduct](DataModelProduct.html) | A product that is a data model, such as an ontology or schema |  no  |
| [ProcessProduct](ProcessProduct.html) | A product that is a process or algorithm |  no  |
| [GraphProduct](GraphProduct.html) | A product that is a graph, represented as nodes and edges |  no  |
| [MappingProduct](MappingProduct.html) | A product that is a mapping between two or more data sources |  no  |
| [Product](Product.html) | A top-level class for all products in the knowledge graph registry |  no  |







## Properties

* Range: [String](String.html)





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:url |
| native | kgr:url |




## LinkML Source

<details>
```yaml
name: url
alias: url
domain_of:
- Product
- Organization
- Usage
range: string

```
</details>
