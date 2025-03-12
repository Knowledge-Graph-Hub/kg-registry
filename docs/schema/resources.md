---
layout: schema_doc
mermaid: true
---



# Slot: resources


_A list of entries in the registry._





URI: [kgr:resources](https://w3id.org/bridge2ai/data-sheets-schema/resources)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Registry](Registry.html) | A registry of knowledge graphs and their components |  no  |







## Properties

* Range: [Resource](Resource.html)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:resources |
| native | kgr:resources |




## LinkML Source

<details>
```yaml
name: resources
description: A list of entries in the registry.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: resources
domain_of:
- Registry
range: Resource
multivalued: true
inlined: true
inlined_as_list: true

```
</details>
