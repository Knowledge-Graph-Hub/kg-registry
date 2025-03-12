---
layout: schema_doc
mermaid: true
---



# Slot: category


_The category of the entity. This should be identical to its class name._





URI: [kgr:category](https://w3id.org/bridge2ai/data-sheets-schema/category)




## Inheritance

* [type](type.html)
    * **category**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProgrammingInterface](ProgrammingInterface.html) | A product that is a programming interface (API) to a resource |  no  |
| [Usage](Usage.html) | The usage of a resource |  no  |
| [KnowledgeGraph](KnowledgeGraph.html) | A knowledge graph resource |  no  |
| [Resource](Resource.html) | A top-level class for all resources in the knowledge graph registry |  no  |
| [GraphProduct](GraphProduct.html) | A product that is a graph, represented as nodes and edges |  no  |
| [Individual](Individual.html) | An individual person |  no  |
| [DataModelProduct](DataModelProduct.html) | A product that is a data model, such as an ontology or schema |  no  |
| [Organization](Organization.html) | An organization |  no  |
| [FundingSource](FundingSource.html) | A funding source for a resource |  no  |
| [MappingProduct](MappingProduct.html) | A product that is a mapping between two or more data sources |  no  |
| [DataSource](DataSource.html) | A data source |  no  |
| [Contact](Contact.html) | A contact point for a resource or product |  no  |
| [NamedThing](NamedThing.html) | A generic grouping for any identifiable entity |  no  |
| [ProcessProduct](ProcessProduct.html) | A product that is a process or algorithm |  no  |
| [Publication](Publication.html) | A publication associated with a resource |  no  |
| [DataModel](DataModel.html) | A data model, such as an ontology or schema |  no  |
| [GraphicalInterface](GraphicalInterface.html) | A product that is a graphical interface to a resource |  no  |
| [License](License.html) | A license for a resource or product |  no  |
| [Aggregator](Aggregator.html) | An aggregator of data sources |  no  |
| [Product](Product.html) | A top-level class for all products in the knowledge graph registry |  no  |







## Properties

* Range: [CategoryType](CategoryType.html)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:category |
| native | kgr:category |




## LinkML Source

<details>
```yaml
name: category
description: The category of the entity. This should be identical to its class name.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
is_a: type
domain: NamedThing
alias: category
domain_of:
- NamedThing
- Contact
range: category_type

```
</details>
