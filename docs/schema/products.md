---
layout: schema_doc
mermaid: true
---



# Slot: products


_The products or representations of the resource._





URI: [kgr:products](https://w3id.org/bridge2ai/data-sheets-schema/products)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Resource](Resource.html) | A top-level class for all resources in the knowledge graph registry |  no  |
| [DataSource](DataSource.html) | A data source |  no  |
| [KnowledgeGraph](KnowledgeGraph.html) | A knowledge graph resource |  no  |
| [DataModel](DataModel.html) | A data model, such as an ontology or schema |  no  |
| [Aggregator](Aggregator.html) | An aggregator of data sources |  no  |







## Properties

* Range: [Product](Product.html)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:products |
| native | kgr:products |




## LinkML Source

<details>
```yaml
name: products
description: The products or representations of the resource.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: products
owner: Resource
domain_of:
- Resource
range: Product
multivalued: true
inlined: true
inlined_as_list: true

```
</details>
