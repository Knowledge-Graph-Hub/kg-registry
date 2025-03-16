---
layout: schema_doc
mermaid: true
---



# Slot: domain


_The domain that the resource is relevant to. This is not multivalued._





URI: [kgr:domain](https://w3id.org/bridge2ai/data-sheets-schema/domain)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [KnowledgeGraph](KnowledgeGraph.html) | A knowledge graph resource |  no  |
| [Aggregator](Aggregator.html) | An aggregator of data sources |  no  |
| [DataModel](DataModel.html) | A data model, such as an ontology or schema |  no  |
| [DataSource](DataSource.html) | A data source |  no  |
| [Resource](Resource.html) | A top-level class for all resources in the knowledge graph registry |  no  |







## Properties

* Range: [DomainEnum](DomainEnum.html)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:domain |
| native | kgr:domain |




## LinkML Source

<details>
```yaml
name: domain
description: The domain that the resource is relevant to. This is not multivalued.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: domain
owner: Resource
domain_of:
- Resource
range: DomainEnum
required: true

```
</details>
