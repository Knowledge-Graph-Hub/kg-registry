---
layout: schema_doc
mermaid: true
---



# Slot: connection_url


_A URL specific to the product. For example, a URL to a specific Neo4j database. Do not include a prefix._





URI: [kgr:connection_url](https://w3id.org/bridge2ai/data-sheets-schema/connection_url)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProgrammingInterface](ProgrammingInterface.html) | A product that is a programming interface (API) to a resource |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.html)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:connection_url |
| native | kgr:connection_url |




## LinkML Source

<details>
```yaml
name: connection_url
description: A URL specific to the product. For example, a URL to a specific Neo4j
  database. Do not include a prefix.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
alias: connection_url
owner: ProgrammingInterface
domain_of:
- ProgrammingInterface
range: uriorcurie

```
</details>
