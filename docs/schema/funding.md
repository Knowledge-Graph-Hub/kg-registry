---
layout: schema_doc
mermaid: true
---



# Slot: funding


_The funding source(s) for the resource._





URI: [kgr:funding](https://w3id.org/bridge2ai/data-sheets-schema/funding)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataModel](DataModel.html) | A data model, such as an ontology or schema |  no  |
| [KnowledgeGraph](KnowledgeGraph.html) | A knowledge graph resource |  no  |
| [DataSource](DataSource.html) | A data source |  no  |
| [Aggregator](Aggregator.html) | An aggregator of data sources |  no  |
| [Resource](Resource.html) | A top-level class for all resources in the knowledge graph registry |  no  |







## Properties

* Range: [FundingSource](FundingSource.html)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:funding |
| native | kgr:funding |




## LinkML Source

<details>
```yaml
name: funding
description: The funding source(s) for the resource.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: funding
owner: Resource
domain_of:
- Resource
range: FundingSource
multivalued: true

```
</details>
