---
layout: schema_doc
mermaid: true
---



# Slot: repository



URI: [kgr:repository](https://w3id.org/bridge2ai/data-sheets-schema/repository)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MappingProduct](MappingProduct.html) | A product that is a mapping between two or more data sources |  no  |
| [ProcessProduct](ProcessProduct.html) | A product that is a process or algorithm |  no  |
| [GraphProduct](GraphProduct.html) | A product that is a graph, represented as nodes and edges |  no  |
| [DataModel](DataModel.html) | A data model, such as an ontology or schema |  no  |
| [ProgrammingInterface](ProgrammingInterface.html) | A product that is a programming interface (API) to a resource |  no  |
| [GraphicalInterface](GraphicalInterface.html) | A product that is a graphical interface to a resource |  no  |
| [KnowledgeGraph](KnowledgeGraph.html) | A knowledge graph resource |  no  |
| [DataSource](DataSource.html) | A data source |  no  |
| [Aggregator](Aggregator.html) | An aggregator of data sources |  no  |
| [DataModelProduct](DataModelProduct.html) | A product that is a data model, such as an ontology or schema |  no  |
| [Resource](Resource.html) | A top-level class for all resources in the knowledge graph registry |  no  |
| [Product](Product.html) | A top-level class for all products in the knowledge graph registry |  no  |







## Properties

* Range: [String](String.html)





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:repository |
| native | kgr:repository |




## LinkML Source

<details>
```yaml
name: repository
alias: repository
domain_of:
- Resource
- Product
range: string

```
</details>
