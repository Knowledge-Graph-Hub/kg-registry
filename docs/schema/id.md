---
layout: schema_doc
mermaid: true
---



# Slot: id


_The identifier of an entity. This is used to identify it within the registry._





URI: [dcterms:identifier](http://purl.org/dc/terms/identifier)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataModel](DataModel.html) | A data model, such as an ontology or schema |  no  |
| [MappingProduct](MappingProduct.html) | A product that is a mapping between two or more data sources |  no  |
| [Aggregator](Aggregator.html) | An aggregator of data sources |  no  |
| [Usage](Usage.html) | The usage of a resource |  no  |
| [Publication](Publication.html) | A publication associated with a resource |  no  |
| [ProgrammingInterface](ProgrammingInterface.html) | A product that is a programming interface (API) to a resource |  no  |
| [DataSource](DataSource.html) | A data source |  no  |
| [Product](Product.html) | A top-level class for all products in the knowledge graph registry |  no  |
| [FundingSource](FundingSource.html) | A funding source for a resource |  no  |
| [ProcessProduct](ProcessProduct.html) | A product that is a process or algorithm |  no  |
| [License](License.html) | A license for a resource or product |  no  |
| [NamedThing](NamedThing.html) | A generic grouping for any identifiable entity |  no  |
| [Resource](Resource.html) | A top-level class for all resources in the knowledge graph registry |  no  |
| [DataModelProduct](DataModelProduct.html) | A product that is a data model, such as an ontology or schema |  no  |
| [GraphProduct](GraphProduct.html) | A product that is a graph, represented as nodes and edges |  no  |
| [KnowledgeGraph](KnowledgeGraph.html) | A knowledge graph resource |  no  |
| [GraphicalInterface](GraphicalInterface.html) | A product that is a graphical interface to a resource |  no  |







## Properties

* Range: [String](String.html)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:identifier |
| native | kgr:id |




## LinkML Source

<details>
```yaml
name: id
description: The identifier of an entity. This is used to identify it within the registry.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
slot_uri: dcterms:identifier
identifier: true
alias: id
domain_of:
- NamedThing
range: string
required: true

```
</details>
