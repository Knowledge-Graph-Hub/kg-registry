---
layout: schema_doc
mermaid: true
---



# Slot: usages


_The usage(s) of the resource._





URI: [kgr:usages](https://w3id.org/bridge2ai/data-sheets-schema/usages)
Alias: usages

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataModel](DataModel.html) | A data model is a formal representation of concepts and relationships within ... |  no  |
| [DataSource](DataSource.html) | A data source |  no  |
| [KnowledgeGraph](KnowledgeGraph.html) | A knowledge graph resource |  no  |
| [Aggregator](Aggregator.html) | An aggregator of data sources |  no  |
| [Ontology](Ontology.html) | An ontology is a formal representation of a set of concepts within a domain a... |  no  |
| [Resource](Resource.html) | A top-level class for all resources in the knowledge graph registry |  no  |






## Properties

* Range: [Usage](Usage.html)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:usages |
| native | kgr:usages |




## LinkML Source

<details>
```yaml
name: usages
description: The usage(s) of the resource.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: usages
owner: Resource
domain_of:
- Resource
range: Usage
multivalued: true
inlined: true
inlined_as_list: true

```
</details>
