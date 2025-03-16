---
layout: schema_doc
mermaid: true
---



# Slot: homepage_url


_The primary URL of the resource. This may be a link to download a specific file, a base URL to an API, or a link to a graphical interface, but it should preferentially be the main page documenting the resource._





URI: [kgr:homepage_url](https://w3id.org/bridge2ai/data-sheets-schema/homepage_url)



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

* Range: [Uriorcurie](Uriorcurie.html)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:homepage_url |
| native | kgr:homepage_url |




## LinkML Source

<details>
```yaml
name: homepage_url
description: The primary URL of the resource. This may be a link to download a specific
  file, a base URL to an API, or a link to a graphical interface, but it should preferentially
  be the main page documenting the resource.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: homepage_url
owner: Resource
domain_of:
- Resource
range: uriorcurie

```
</details>
