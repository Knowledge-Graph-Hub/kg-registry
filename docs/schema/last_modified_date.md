---
layout: schema_doc
mermaid: true
---



# Slot: last_modified_date


_The date the entry was last modified. It should be in ISO 8601 format, e.g., 2024-02-12T00:00:00Z._





URI: [kgr:last_modified_date](https://w3id.org/bridge2ai/data-sheets-schema/last_modified_date)
Alias: last_modified_date

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GraphProduct](GraphProduct.html) | A product that is a graph, represented as nodes and edges |  no  |
| [GraphicalInterface](GraphicalInterface.html) | A product that is a graphical interface to a resource |  no  |
| [Usage](Usage.html) | The usage of a resource |  no  |
| [Publication](Publication.html) | A publication associated with a resource |  no  |
| [Organization](Organization.html) | An organization |  no  |
| [OntologyProduct](OntologyProduct.html) | A product that is an ontology, a formal representation of a set of concepts w... |  no  |
| [License](License.html) | A license for a resource or product |  no  |
| [DataSource](DataSource.html) | A data source |  no  |
| [ProgrammingInterface](ProgrammingInterface.html) | A product that is a programming interface (API) to a resource |  no  |
| [FundingSource](FundingSource.html) | A funding source for a resource |  no  |
| [ProcessProduct](ProcessProduct.html) | A product that is a process or algorithm |  no  |
| [Resource](Resource.html) | A top-level class for all resources in the knowledge graph registry |  no  |
| [DataModel](DataModel.html) | A data model is a formal representation of concepts and relationships within ... |  no  |
| [DataModelProduct](DataModelProduct.html) | A product that provides the rules of a data model |  no  |
| [MappingProduct](MappingProduct.html) | A product that is a mapping between two or more data sources |  no  |
| [Ontology](Ontology.html) | An ontology is a formal representation of a set of concepts within a domain a... |  no  |
| [DocumentationProduct](DocumentationProduct.html) | A product that is documentation for a resource |  no  |
| [Product](Product.html) | A top-level class for all products in the knowledge graph registry |  no  |
| [KnowledgeGraph](KnowledgeGraph.html) | A knowledge graph resource |  no  |
| [NamedThing](NamedThing.html) | A generic grouping for any identifiable entity |  no  |
| [Aggregator](Aggregator.html) | An aggregator of data sources |  no  |






## Properties

* Range: [Datetime](Datetime.html)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:last_modified_date |
| native | kgr:last_modified_date |




## LinkML Source

<details>
```yaml
name: last_modified_date
description: The date the entry was last modified. It should be in ISO 8601 format,
  e.g., 2024-02-12T00:00:00Z.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: last_modified_date
domain_of:
- NamedThing
- Organization
range: datetime

```
</details>
