---
layout: schema_doc
mermaid: true
---


# Slot: inferred_from 


_For an inferred license, the identifiers of the sources (resources or products) whose licenses sit at the chosen restrictiveness tier. Any one of them is enough to impose this license._






URI: [kgr:inferred_from](https://w3id.org/bridge2ai/data-sheets-schema/inferred_from)
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
| self | kgr:inferred_from |
| native | kgr:inferred_from |




## LinkML Source

<details>
```yaml
name: inferred_from
description: For an inferred license, the identifiers of the sources (resources or
  products) whose licenses sit at the chosen restrictiveness tier. Any one of them
  is enough to impose this license.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
owner: License
domain_of:
- License
range: string
multivalued: true

```
</details>
