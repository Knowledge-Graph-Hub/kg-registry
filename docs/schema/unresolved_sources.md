---
layout: schema_doc
mermaid: true
---


# Slot: unresolved_sources 


_For an inferred license, the identifiers of sources for which no license could be found, either directly or through their own sources. The inferred license does not account for these._






URI: [kgr:unresolved_sources](https://w3id.org/bridge2ai/data-sheets-schema/unresolved_sources)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [License](License.html) | A license for a resource or product |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.html) |
| Domain Of | [License](License.html) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [License](License.html) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kgr:unresolved_sources |
| native | kgr:unresolved_sources |




## LinkML Source

<details>
```yaml
name: unresolved_sources
description: For an inferred license, the identifiers of sources for which no license
  could be found, either directly or through their own sources. The inferred license
  does not account for these.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
owner: License
domain_of:
- License
range: string
multivalued: true

```
</details>
