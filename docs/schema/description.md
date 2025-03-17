---
layout: schema_doc
mermaid: true
---



# Slot: description



URI: [kgr:description](https://w3id.org/bridge2ai/data-sheets-schema/description)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Resource](Resource.html) | A top-level class for all resources in the knowledge graph registry |  no  |
| [GraphProduct](GraphProduct.html) | A product that is a graph, represented as nodes and edges |  no  |
| [DataSource](DataSource.html) | A data source |  no  |
| [Product](Product.html) | A top-level class for all products in the knowledge graph registry |  no  |
| [DataModelProduct](DataModelProduct.html) | A product that is a data model, such as an ontology or schema |  no  |
| [KnowledgeGraph](KnowledgeGraph.html) | A knowledge graph resource |  no  |
| [GraphicalInterface](GraphicalInterface.html) | A product that is a graphical interface to a resource |  no  |
| [ProgrammingInterface](ProgrammingInterface.html) | A product that is a programming interface (API) to a resource |  no  |
| [MappingProduct](MappingProduct.html) | A product that is a mapping between two or more data sources |  no  |
| [Usage](Usage.html) | The usage of a resource |  no  |
| [ProcessProduct](ProcessProduct.html) | A product that is a process or algorithm |  no  |
| [DataModel](DataModel.html) | A data model, such as an ontology or schema |  no  |
| [Aggregator](Aggregator.html) | An aggregator of data sources |  no  |







## Properties

* Range: [String](String.html)





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:description |
| native | kgr:description |




## LinkML Source

<details>
```yaml
name: description
alias: description
domain_of:
- Resource
- Product
- Usage
range: string

```
</details>
